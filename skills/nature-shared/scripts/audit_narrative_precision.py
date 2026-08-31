#!/usr/bin/env python3
"""Conservative manuscript narrative/rhetoric/precision audit.

This scanner finds mechanically visible symptoms that should trigger contextual
review. It cannot decide whether a section is scientifically sufficient or a
qualification is necessary; those remain reader/editor judgments.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


REFERENCE_START_RE = re.compile(r"^\s*(?:References|Bibliography)\s*$", re.IGNORECASE | re.MULTILINE)
LONG_DECIMAL_RE = re.compile(r"(?<![\w./-])[-+]?\d+\.\d{5,}(?![\w/])")
PERFECT_FIXED_RE = re.compile(r"(?<![\w.])(?:0|1)\.0{5,}(?!\d)")
OPAQUE_ID_RE = re.compile(r"\b(?:D|M|A|V|P|H)\d+(?:[-.][A-Z0-9]+)*\b")
MARKDOWN_HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$", re.MULTILINE)
LATEX_HEADING_RE = re.compile(
    r"^\\(?P<kind>section|subsection|subsubsection)\*?\{(?P<title>[^}]+)\}\s*$",
    re.MULTILINE,
)

DEFENSIVE_PHRASES = (
    "we do not claim",
    "does not establish",
    "do not establish",
    "should not be read as",
    "nothing here claims",
    "not evidence of",
    "remains undetermined",
    "cannot check",
    "cannot-check",
    "does not authorize",
    "not population evidence",
    "retained terminal",
    "exact terminal is",
    "withdrawn rather than",
)

SETUP_TITLES = (
    "problem formulation",
    "problem definition",
    "formal setup",
    "framework",
    "theory",
    "task definition",
    "model formulation",
)

LATEX_LEVEL = {"section": 1, "subsection": 2, "subsubsection": 3}


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def excerpt(text: str, start: int, end: int, limit: int = 200) -> str:
    left = text.rfind("\n", 0, start) + 1
    right = text.find("\n", end)
    if right < 0:
        right = len(text)
    return " ".join(text[left:right].split())[:limit]


def add_finding(
    findings: list[dict[str, Any]],
    *,
    code: str,
    severity: str,
    message: str,
    text: str,
    start: int | None = None,
    end: int | None = None,
    token: str | None = None,
    detail: str | None = None,
) -> None:
    findings.append(
        {
            "code": code,
            "severity": severity,
            "line": line_number(text, start) if start is not None else None,
            "token": token,
            "message": message,
            "excerpt": excerpt(text, start, end or start) if start is not None else detail,
            "detail": detail,
        }
    )


def body_before_references(text: str) -> str:
    match = REFERENCE_START_RE.search(text)
    return text[: match.start()] if match else text


def words(value: str) -> list[str]:
    return re.findall(r"\b[\w'-]+\b", value, flags=re.UNICODE)


def section_headings(text: str) -> list[tuple[str, int, int]]:
    """Return headings as (title, start, hierarchy level)."""
    headings: list[tuple[str, int, int]] = []
    for match in MARKDOWN_HEADING_RE.finditer(text):
        headings.append((match.group("title").strip(), match.start(), len(match.group("marks"))))
    for match in LATEX_HEADING_RE.finditer(text):
        headings.append((match.group("title").strip(), match.start(), LATEX_LEVEL[match.group("kind")]))
    headings.sort(key=lambda item: item[1])
    return headings


def section_spans(text: str) -> list[tuple[str, int, int, int]]:
    """Return section spans, keeping child subsections inside their parent span.

    A heading ends at the next heading of the same or higher rank, not at the
    next child heading. This avoids measuring a parent Theory/Problem section as
    only its lead-in before the first subsection.
    """
    headings = section_headings(text)
    spans: list[tuple[str, int, int, int]] = []
    for index, (title, start, level) in enumerate(headings):
        end = len(text)
        for _next_title, next_start, next_level in headings[index + 1 :]:
            if next_level <= level:
                end = next_start
                break
        spans.append((title, start, end, level))
    return spans


def normalize_section_title(title: str) -> str:
    value = title.casefold().strip()
    value = re.sub(r"^\d+(?:\.\d+)*[.)]?\s+", "", value)
    return " ".join(value.split())


def audit(text: str) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    body = body_before_references(text)

    long_decimals = list(LONG_DECIMAL_RE.finditer(body))
    for match in long_decimals[:20]:
        token = match.group(0)
        add_finding(
            findings,
            code="excessive_decimal_precision",
            severity="review",
            message=(
                "Number has five or more decimal places in manuscript-facing text. Confirm that this precision is justified by the quantity, denominator, uncertainty, threshold, or target convention rather than raw formatter output."
            ),
            text=text,
            start=match.start(),
            end=match.end(),
            token=token,
        )

    perfect_fixed = list(PERFECT_FIXED_RE.finditer(body))
    if len(perfect_fixed) >= 2:
        add_finding(
            findings,
            code="fixed_width_perfect_metric",
            severity="review",
            message=(
                "Repeated 0.00000/1.00000-style values suggest fixed-width machine precision. Prefer scientifically justified manuscript precision unless exact fixed-width output is itself meaningful."
            ),
            text=text,
            start=perfect_fixed[0].start(),
            end=perfect_fixed[0].end(),
            token=perfect_fixed[0].group(0),
            detail=f"{len(perfect_fixed)} repeated fixed-width perfect/zero metrics",
        )

    lower = body.casefold()
    phrase_counts: Counter[str] = Counter()
    phrase_positions: list[tuple[int, str]] = []
    for phrase in DEFENSIVE_PHRASES:
        for match in re.finditer(re.escape(phrase), lower):
            phrase_counts[phrase] += 1
            phrase_positions.append((match.start(), phrase))

    wc = max(1, len(words(body)))
    defensive_total = sum(phrase_counts.values())
    defensive_per_1000 = defensive_total * 1000 / wc
    if defensive_total >= 5 and defensive_per_1000 >= 1.5:
        start, phrase = min(phrase_positions)
        add_finding(
            findings,
            code="defensive_qualification_density",
            severity="review",
            message=(
                "High density of defensive/non-claim phrasing. Check whether necessary boundaries can be consolidated and whether each headline result still has a direct positive bounded statement."
            ),
            text=text,
            start=start,
            end=start + len(phrase),
            token=phrase,
            detail=f"{defensive_total} matches; {defensive_per_1000:.2f} per 1000 words",
        )

    opaque_matches = list(OPAQUE_ID_RE.finditer(body))
    opaque_counts: Counter[str] = Counter(match.group(0) for match in opaque_matches)
    if len(opaque_counts) >= 6 or sum(opaque_counts.values()) >= 18:
        add_finding(
            findings,
            code="experiment_id_narrative_density",
            severity="review",
            message=(
                "Many opaque experiment/version IDs remain in the scientific narrative. Confirm that the paper is organized around scientific questions rather than project/version chronology and that each retained ID has a reader-facing identity before use."
            ),
            text=text,
            detail=", ".join(f"{key}×{value}" for key, value in opaque_counts.most_common(12)),
        )

    spans = section_spans(body)
    results_start: int | None = None
    for title, start, _end, _level in spans:
        normalized = normalize_section_title(title)
        if normalized == "results" or normalized.startswith("results "):
            results_start = start
            break

    first_opaque: dict[str, int] = {}
    for match in opaque_matches:
        first_opaque.setdefault(match.group(0), match.start())
    result_first_ids = sorted(
        token for token, position in first_opaque.items() if results_start is not None and position >= results_start
    )

    # Shortness by itself is never a warning: that would be a disguised word-count
    # quota. We only raise this review signal when a compact setup is followed by
    # paper-private IDs whose first occurrence is already inside Results, which is
    # concrete evidence that reader-state activation may have been deferred too far.
    if result_first_ids:
        for title, start, end, _level in spans:
            normalized = normalize_section_title(title)
            if not any(name in normalized for name in SETUP_TITLES):
                continue
            count = len(words(body[start:end]))
            if count >= 140:
                continue
            add_finding(
                findings,
                code="short_setup_section_review",
                severity="review",
                message=(
                    "A compact setup/formulation section is followed by paper-private identifiers first introduced in Results. Do not expand by quota; verify whether the missing reader-state activation, definitions, comparator roles, or experiment rationale belong before the result-bearing use."
                ),
                text=text,
                start=start,
                end=min(end, start + 120),
                token=title,
                detail=f"approximately {count} words; first-in-Results IDs: {', '.join(result_first_ids[:12])}",
            )
            break

    counts = Counter(item["severity"] for item in findings)
    return {
        "decision": "BLOCKED" if counts["error"] else ("REVIEW" if counts["review"] else "PASS"),
        "counts": {"error": counts["error"], "review": counts["review"]},
        "findings": findings,
        "metrics": {
            "body_word_count": wc,
            "long_decimal_count": len(long_decimals),
            "defensive_phrase_count": defensive_total,
            "defensive_phrases_per_1000_words": round(defensive_per_1000, 3),
            "opaque_id_occurrences": sum(opaque_counts.values()),
            "opaque_ids_first_seen_in_results": result_first_ids,
        },
        "notes": [
            "All findings are conservative review signals; section sufficiency, necessary caveats, and justified precision require contextual scientific judgment.",
            "The scanner does not impose a universal word count, significant-figure rule, or ban on caveats/experiment IDs.",
            "Short setup sections are not flagged solely for length; the setup review requires a downstream reader-activation signal.",
            "Section-length checks include child subsections rather than truncating the parent at the next lower-level heading.",
        ],
    }


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Audit manuscript narrative symptoms and numerical display precision.")
    p.add_argument("manuscript", type=Path)
    p.add_argument("--pretty", action="store_true")
    p.add_argument("--fail-on-review", action="store_true")
    p.add_argument("--report", type=Path)
    return p


def main() -> int:
    args = parser().parse_args()
    payload = audit(args.manuscript.read_text(encoding="utf-8"))
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
