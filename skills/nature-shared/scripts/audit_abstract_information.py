#!/usr/bin/env python3
"""Conservative audit for abstract information density and entry-point quality.

The scanner intentionally returns review signals rather than pretending that a
fixed number of numeric tokens or rhetorical moves defines a good abstract.
Exact venue requirements and reporting standards remain authoritative.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ABSTRACT_HEADING_RE = re.compile(
    r"(?im)^\s*(?:#{1,6}\s*)?(?:\\begin\{abstract\}\s*)?abstract\s*(?:\})?\s*$"
)
LATEX_ABSTRACT_RE = re.compile(r"(?is)\\begin\{abstract\}(.*?)\\end\{abstract\}")
STOP_HEADING_RE = re.compile(
    r"(?im)^\s*(?:keywords?\s*:|#{1,6}\s+|\\(?:section|chapter)\*?\{|\d+(?:\.\d+)*[.)]?\s+[A-Z])"
)
NUMBER_RE = re.compile(
    r"(?<![\w])[-+]?(?:\d+(?:\.\d+)?|\.\d+)(?:\s*%|/\d+)?(?![\w])"
)
LONG_DECIMAL_RE = re.compile(r"(?<![\w])[-+]?\d+\.\d{5,}(?!\d)")
OPAQUE_ID_RE = re.compile(r"\b(?:D|M|A|V|P|H)\d+(?:[-.][A-Z0-9]+)*\b")
CITATION_RE = re.compile(
    r"(?:\\cite\w*\{|\[[0-9]{1,3}(?:\s*[-,;]\s*[0-9]{1,3})*\]|\([A-Z][A-Za-z-]+\s+et\s+al\.,?\s+\d{4}\))"
)

RESULT_CONTEXT_RE = re.compile(
    r"\b(?:battery|batteries|holdout|corpus|corpora|benchmark|contracts?|cases?|cohort|dataset|domain|test|programme|program|sample)\b",
    re.IGNORECASE,
)
INFERENTIAL_RE = re.compile(
    r"\b(?:confidence interval|credible interval|bootstrap interval|\bCI\b|p\s*[=<>]|paired difference|effect size)\b",
    re.IGNORECASE,
)
DEFENSIVE_RE = re.compile(
    r"\b(?:we do not claim|does not establish|do not establish|should not be read as|not population evidence|does not imply|cannot establish|remains prospective)\b",
    re.IGNORECASE,
)


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _words(text: str) -> list[str]:
    return re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE)


def _sentences(text: str) -> list[str]:
    compact = " ".join(text.split())
    if not compact:
        return []
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", compact) if s.strip()]


def extract_abstract(text: str) -> tuple[str | None, int | None, int | None]:
    latex = LATEX_ABSTRACT_RE.search(text)
    if latex:
        return latex.group(1).strip(), latex.start(1), latex.end(1)

    heading = ABSTRACT_HEADING_RE.search(text)
    if not heading:
        # Accept common one-line LaTeX form: \abstract{...} only when braces close
        inline = re.search(r"(?is)\\abstract\{(.{20,20000}?)\}\s*(?=\\(?:keywords|section)|$)", text)
        if inline:
            return inline.group(1).strip(), inline.start(1), inline.end(1)
        return None, None, None

    start = heading.end()
    rest = text[start:]
    stop = STOP_HEADING_RE.search(rest)
    end = start + (stop.start() if stop else len(rest))
    return text[start:end].strip(), start, end


def _finding(
    findings: list[dict[str, Any]],
    *,
    code: str,
    severity: str,
    message: str,
    abstract: str,
    token: str | None = None,
    sentence_index: int | None = None,
    detail: str | None = None,
) -> None:
    findings.append(
        {
            "code": code,
            "severity": severity,
            "message": message,
            "token": token,
            "sentence_index": sentence_index,
            "detail": detail,
            "abstract_excerpt": " ".join(abstract.split())[:240],
        }
    )


def audit(
    text: str,
    *,
    max_words: int | None = None,
    reporting_mandated: bool = False,
    references_disallowed: bool = False,
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    abstract, start, end = extract_abstract(text)

    if abstract is None:
        return {
            "decision": "UNRESOLVED",
            "counts": {"error": 0, "unresolved": 1, "review": 0},
            "findings": [
                {
                    "code": "abstract_not_found",
                    "severity": "unresolved",
                    "message": "No abstract block was detected. Confirm whether the article type requires one and, if so, provide a parseable abstract heading/environment.",
                    "token": None,
                    "sentence_index": None,
                    "detail": None,
                    "abstract_excerpt": None,
                }
            ],
            "metrics": {},
            "notes": ["Absence is unresolved rather than automatically invalid because some article types do not require abstracts."],
        }

    sentences = _sentences(abstract)
    word_count = len(_words(abstract))
    number_matches = list(NUMBER_RE.finditer(abstract))
    long_decimals = list(LONG_DECIMAL_RE.finditer(abstract))
    opaque_ids = list(OPAQUE_ID_RE.finditer(abstract))
    inferential = list(INFERENTIAL_RE.finditer(abstract))
    defensive = list(DEFENSIVE_RE.finditer(abstract))
    citations = list(CITATION_RE.finditer(abstract))

    per_sentence_numbers: list[int] = []
    result_sentences: list[int] = []
    for i, sentence in enumerate(sentences, start=1):
        count = len(NUMBER_RE.findall(sentence))
        per_sentence_numbers.append(count)
        if count and RESULT_CONTEXT_RE.search(sentence):
            result_sentences.append(i)

    dense_sentences = [i + 1 for i, count in enumerate(per_sentence_numbers) if count >= 3]
    multi_numeric_sentences = [i + 1 for i, count in enumerate(per_sentence_numbers) if count >= 2]

    if max_words is not None and word_count > max_words:
        _finding(
            findings,
            code="abstract_word_limit_exceeded",
            severity="error",
            message=f"Abstract has {word_count} words but the supplied hard limit is {max_words}.",
            abstract=abstract,
            detail=f"overflow={word_count - max_words}",
        )

    # Long decimals are always worth review even for reporting-mandated abstracts;
    # the exact value may still be justified by the study or venue.
    if long_decimals:
        _finding(
            findings,
            code="abstract_formatter_precision",
            severity="review",
            message="The abstract contains values with five or more decimal places. Check that scientific resolution or a decision threshold—not formatter output—requires that precision.",
            abstract=abstract,
            token=long_decimals[0].group(0),
            detail=f"count={len(long_decimals)}",
        )

    if opaque_ids:
        unique = sorted({m.group(0) for m in opaque_ids})
        _finding(
            findings,
            code="abstract_private_identifier",
            severity="review",
            message="Opaque experiment/version identifiers appear in the abstract. Replace with reader-facing scientific names unless the identifier is itself a public field-standard object.",
            abstract=abstract,
            token=unique[0],
            detail=", ".join(unique[:12]),
        )

    if references_disallowed and citations:
        _finding(
            findings,
            code="abstract_reference_disallowed",
            severity="error",
            message="The supplied target regime disallows references in the abstract, but citation-like syntax was detected.",
            abstract=abstract,
            token=citations[0].group(0),
            detail=f"count={len(citations)}",
        )

    # Reporting standards such as CONSORT can legitimately require many numerical
    # objects. In that mode, density itself is not flagged; other defects remain.
    if not reporting_mandated:
        if len(number_matches) >= 10 or len(dense_sentences) >= 2 or len(multi_numeric_sentences) >= 4:
            _finding(
                findings,
                code="abstract_numeric_density",
                severity="review",
                message="The abstract carries a high density of numerical objects. Check whether secondary batteries, diagnostics, provenance counts, or duplicated inferential detail can be removed while retaining the minimum headline quantitative anchor(s).",
                abstract=abstract,
                detail=(
                    f"numeric_tokens={len(number_matches)}; dense_sentences={dense_sentences}; "
                    f"sentences_with_2plus_numbers={multi_numeric_sentences}"
                ),
            )

        if len(result_sentences) >= 3:
            _finding(
                findings,
                code="abstract_multiple_quantitative_substories",
                severity="review",
                message="Several abstract sentences attach numbers to different batteries/cases/benchmarks/datasets. Check whether the abstract is reproducing the Results ledger instead of compressing evidence at the claim level.",
                abstract=abstract,
                detail=f"result_context_sentences={result_sentences}",
            )

        if len(inferential) >= 3 and len(number_matches) >= 8:
            _finding(
                findings,
                code="abstract_inferential_detail_stack",
                severity="review",
                message="Multiple inferential-detail markers occur alongside many numbers. Verify that each CI/p-value/difference belongs to a distinct headline claim rather than duplicating uncertainty detail for secondary results.",
                abstract=abstract,
                detail=f"inferential_markers={len(inferential)}; numeric_tokens={len(number_matches)}",
            )

    if len(defensive) >= 3:
        _finding(
            findings,
            code="abstract_defensive_density",
            severity="review",
            message="Several defensive boundary phrases occur in the abstract. Preserve necessary scope limits, but check whether repeated non-claims are displacing the strongest positive bounded result and its meaning.",
            abstract=abstract,
            token=defensive[0].group(0),
            detail=f"count={len(defensive)}",
        )

    counts = Counter(item["severity"] for item in findings)
    if counts["error"]:
        decision = "BLOCKED"
    elif counts["unresolved"]:
        decision = "UNRESOLVED"
    elif counts["review"]:
        decision = "REVIEW"
    else:
        decision = "PASS"

    return {
        "decision": decision,
        "counts": {
            "error": counts["error"],
            "unresolved": counts["unresolved"],
            "review": counts["review"],
        },
        "findings": findings,
        "metrics": {
            "abstract_start_line": _line_number(text, start or 0),
            "abstract_word_count": word_count,
            "sentence_count": len(sentences),
            "numeric_token_count": len(number_matches),
            "long_decimal_count": len(long_decimals),
            "opaque_identifier_count": len(opaque_ids),
            "inferential_marker_count": len(inferential),
            "defensive_phrase_count": len(defensive),
            "numeric_tokens_per_sentence": per_sentence_numbers,
            "quantitative_result_context_sentences": result_sentences,
            "reporting_mandated_profile": reporting_mandated,
        },
        "notes": [
            "Numeric-density findings are contextual review signals, not universal number quotas.",
            "Use --reporting-mandated for abstract regimes where a reporting guideline legitimately requires multiple numerical objects; target-specific completeness still requires human/contract review.",
            "A confidence interval or estimate/comparator bundle should be judged semantically, not as an arbitrary count of digits.",
        ],
    }


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Audit abstract information density and entry-point quality.")
    p.add_argument("manuscript", type=Path)
    p.add_argument("--max-words", type=int)
    p.add_argument("--reporting-mandated", action="store_true")
    p.add_argument("--references-disallowed", action="store_true")
    p.add_argument("--pretty", action="store_true")
    p.add_argument("--fail-on-review", action="store_true")
    p.add_argument("--report", type=Path)
    return p


def main() -> int:
    args = parser().parse_args()
    payload = audit(
        args.manuscript.read_text(encoding="utf-8"),
        max_words=args.max_words,
        reporting_mandated=args.reporting_mandated,
        references_disallowed=args.references_disallowed,
    )
    rendered = json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if args.fail_on_review and payload["decision"] != "PASS":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
