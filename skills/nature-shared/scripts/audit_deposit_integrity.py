#!/usr/bin/env python3
"""Hard-artifact audit for a manuscript about to be deposited or submitted.

This audit looks only for things that are *objectively wrong* in a finished
manuscript: apparatus that is missing, text that was never meant to ship,
references that do not resolve. It makes no judgement about style, and it does
not score prose against any machine-text classifier.

That boundary is deliberate and worth stating, because the request this audit
answers is usually phrased as "remove the signs it was drafted with a model".
Two different things hide inside that phrasing:

*Defects*, which this audit finds and which must be fixed because they are
errors regardless of who or what wrote the manuscript. A research paper with no
bibliography, a stray assistant turn of phrase, an unresolved TODO, a citation
key with no entry: each is wrong on its own terms, and each is read by an editor
as evidence that nobody checked the manuscript.

*Disclosure*, which this audit will not touch. Venues require that AI assistance
be declared and that the author retain responsibility. Trimming or hiding such a
statement is misrepresentation, and no check here rewards it. Where a project
sets its own house form for the declaration, the audit reports divergence from
that form as a consistency finding, never as a reason to say less than the truth.

Prose quality is a separate concern handled by the writing skills. It is kept
out of here because a check that flags ordinary academic phrasing as suspicious
produces false accusations, and because published evaluations of machine-text
detectors report high false-positive rates against non-native English writers.
Targeting writing quality and factual integrity is defensible; targeting a
detector score is not.

Exit codes
    0  clean
    1  findings at ERROR severity
    2  could not audit
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "manuscript.deposit-integrity.v1"

# --- Reference apparatus --------------------------------------------------
_BIBCMD = re.compile(
    r"\\(?:printbibliography|bibliography\s*\{|begin\s*\{thebibliography\})"
)
_BIBITEM = re.compile(r"\\bibitem")
_REFHEAD = re.compile(
    r"(?:\\(?:sub)?section\*?\s*\{|^\s{0,3}#{1,3}\s*)\s*(?:\d+\.?\s*)?"
    r"(?:references|bibliography|works cited)\b",
    re.IGNORECASE | re.MULTILINE,
)
_CITE = re.compile(
    r"\\[a-zA-Z]{0,6}cite[a-zA-Z]*\s*[\[{]"
    r"|\[@[\w:.-]+"
    r"|\[\d{1,3}(?:\s*[,\u2013-]\s*\d{1,3})*\]"
)
# Citation commands are whitelisted rather than pattern-matched. A permissive
# "any command containing cite" rule reads \setcitestyle{authoryear,round} as
# three citations to undefined keys, and \nocite{*} as a citation to a key named
# "*". Both appeared in the calibration corpus, and both would have been
# reported as fabricated references.
_CITE_COMMANDS = (
    "cite", "citep", "citet", "citeal", "citealp", "citealt", "citeauthor",
    "citeyear", "citeyearpar", "citenum", "citetitle", "parencite", "autocite",
    "textcite", "footcite", "smartcite", "supercite", "fullcite", "cites",
    "parencites", "autocites", "textcites", "footcites",
)
_CITEKEY = re.compile(
    r"\\(?:" + "|".join(sorted(_CITE_COMMANDS, key=len, reverse=True)) + r")\*?"
    r"\s*(?:\[[^\]]*\]\s*)*\{([^}]*)\}",
    re.IGNORECASE,
)
_BIBENTRY = re.compile(r"^\s*@\w+\s*\{\s*([^,\s]+)", re.MULTILINE)

# --- Assistant-voice leakage ----------------------------------------------
# Kept to phrases that have no legitimate place in a manuscript body. Anything
# that could plausibly occur in scholarly prose is excluded on purpose: a false
# accusation here is far more damaging than a miss.
_ASSISTANT_VOICE = (
    "as an ai language model",
    "as a large language model",
    "i cannot provide",
    "i'm sorry, but i",
    "i am sorry, but i",
    "certainly! here",
    "sure! here",
    "here is the revised",
    "here's the revised",
    "here is a revised version",
    "as requested, i have",
    "i hope this helps",
    "let me know if you",
    "feel free to ask",
    "in this response",
    "knowledge cutoff",
)

# --- Placeholders ---------------------------------------------------------
_PLACEHOLDER = re.compile(
    r"(?<![A-Za-z])(?:TODO|TBD|FIXME|XXX+)(?![A-Za-z])"
    r"|\[(?:INSERT|ADD|CITATION NEEDED|REF|PLACEHOLDER)[^\]]{0,40}\]"
    r"|<(?:placeholder|insert)[^>]{0,40}>"
    r"|lorem ipsum"
    r"|\bYOUR[_ ](?:NAME|EMAIL|AFFILIATION)\b",
    re.IGNORECASE,
)

# --- Cross-references -----------------------------------------------------
_LABEL = re.compile(r"\\label\s*\{([^}]+)\}")
_REF = re.compile(r"\\(?:page|auto|c|C|eq|name)?ref\*?\s*\{([^}]+)\}")


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def audit(body: str, bib_sources: list[str], house_disclosure: str | None) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []

    def add(severity: str, code: str, message: str, evidence: Any = None) -> None:
        findings.append(
            {"severity": severity, "code": code, "message": message, "evidence": evidence}
        )

    lowered = body.lower()

    # 1. Reference apparatus.
    inline_cites = len(_CITE.findall(body))
    has_apparatus = bool(
        _BIBCMD.search(body) or _BIBITEM.search(body) or _REFHEAD.search(body) or bib_sources
    )
    if not has_apparatus:
        add(
            "ERROR",
            "no_reference_apparatus",
            "The manuscript carries no bibliography, no reference section and no "
            "bibliography file. A research manuscript that cites nothing reads as work "
            "that never positioned itself against prior literature, and is a standing "
            "desk-rejection and moderation risk at every venue.",
            {"inline_citations": inline_cites},
        )
    elif inline_cites == 0 and not _BIBITEM.search(body) and not _REFHEAD.search(body):
        add(
            "ERROR",
            "reference_list_never_cited",
            "A bibliography is present but nothing in the body cites it.",
            {"inline_citations": 0},
        )

    # 2. Dangling citation keys.
    if bib_sources:
        defined = set()
        for src in bib_sources:
            defined.update(m.group(1).strip() for m in _BIBENTRY.finditer(src))
        used: set[str] = set()
        for m in _CITEKEY.finditer(body):
            for key in m.group(1).split(","):
                key = key.strip()
                if key:
                    used.add(key)

        dangling = sorted(used - defined)
        if dangling and defined:
            add(
                "ERROR",
                "dangling_citation_keys",
                "Citation keys are used in the body with no matching bibliography entry. "
                "These render as unresolved markers and are read as fabricated references.",
                {"keys": dangling[:20], "count": len(dangling)},
            )

    # 3. Assistant-voice leakage.
    leaks = [p for p in _ASSISTANT_VOICE if p in lowered]
    if leaks:
        add(
            "ERROR",
            "assistant_voice_leakage",
            "Conversational assistant phrasing survives in the manuscript body. This is "
            "drafting residue, not scholarly prose, and must be removed.",
            {"phrases": leaks},
        )

    # 4. Placeholders, split by whether they reach the reader.
    #
    # A template default sitting in the preamble (an unfilled OpenReview forum
    # id, say) is a loose end but does not typeset; a placeholder in the body
    # does. Reporting both at the same severity trains the reader to ignore the
    # check.
    split = body.find(r"\begin{document}")
    preamble, main_body = (body[:split], body[split:]) if split != -1 else ("", body)

    body_ph = sorted({m.group(0) for m in _PLACEHOLDER.finditer(main_body)})
    pre_ph = sorted({m.group(0) for m in _PLACEHOLDER.finditer(preamble)})
    if body_ph:
        add(
            "ERROR",
            "unresolved_placeholder",
            "Placeholder or task-marker text remains in the manuscript body, where it "
            "typesets and reaches the reader.",
            {"tokens": body_ph[:20], "count": len(body_ph)},
        )
    if pre_ph:
        add(
            "WARN",
            "unresolved_placeholder_in_preamble",
            "Template placeholder text remains in the preamble. It does not typeset, but "
            "it ships in the source archive and should be filled or removed.",
            {"tokens": pre_ph[:20], "count": len(pre_ph)},
        )

    # 5. Unresolved cross-references.
    labels = {m.group(1).strip() for m in _LABEL.finditer(body)}
    refs = {m.group(1).strip() for m in _REF.finditer(body)}
    broken = sorted(r for r in refs - labels if r)
    if broken:
        add(
            "ERROR",
            "unresolved_cross_reference",
            "Cross-references point at labels that do not exist in the manuscript; these "
            "typeset as '??'.",
            {"targets": broken[:20], "count": len(broken)},
        )

    # 6. House disclosure form.
    #
    # Reported as a consistency finding only. The audit never proposes removing
    # or weakening a disclosure, and a manuscript that discloses MORE than the
    # house form is not in error, only inconsistent with the project's own
    # settled wording.
    if house_disclosure:
        norm_house = re.sub(r"\s+", " ", house_disclosure.strip().lower())
        norm_body = re.sub(r"\s+", " ", lowered)
        mentions_ai = any(
            k in norm_body
            for k in ("generative ai", "large language model", "ai-assist", "ai assistance")
        )
        if mentions_ai and norm_house not in norm_body:
            add(
                "INFO",
                "disclosure_diverges_from_house_form",
                "An AI-assistance disclosure is present but does not match the project's "
                "settled house wording. Align the form if the project requires it. Do not "
                "shorten the substance below what the venue requires, and never remove the "
                "disclosure: it is required, and the audit treats its presence as correct.",
                None,
            )
        elif not mentions_ai:
            add(
                "INFO",
                "no_ai_disclosure_found",
                "No AI-assistance disclosure was found. If assistance was used, most venues "
                "require it to be declared.",
                None,
            )

    errors = [f for f in findings if f["severity"] == "ERROR"]
    return {
        "schema_version": SCHEMA_VERSION,
        "verdict": "FINDINGS" if errors else "CLEAN",
        "error_count": len(errors),
        "findings": findings,
        "scope_note": (
            "Hard artifacts only. Prose style is out of scope by design, and no check "
            "here is keyed to a machine-text detector score."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--manuscript", required=True)
    ap.add_argument("--bib", action="append", default=[], help="bibliography file (repeatable)")
    ap.add_argument("--house-disclosure", default=None,
                    help="project's settled AI-disclosure sentence, or a file containing it")
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args(argv)

    path = Path(args.manuscript)
    if not path.is_file():
        print(json.dumps({"verdict": "CANNOT_AUDIT", "error": "not found: %s" % path}))
        return 2
    body = _read(path)
    if not body.strip():
        print(json.dumps({"verdict": "CANNOT_AUDIT", "error": "empty: %s" % path}))
        return 2

    bibs = []
    for b in args.bib:
        p = Path(b)
        if p.is_file():
            bibs.append(_read(p))

    house = args.house_disclosure
    if house and Path(house).is_file():
        house = _read(Path(house))

    result = audit(body, bibs, house)
    result["manuscript"] = str(path)
    payload = json.dumps(result, indent=2)
    if args.json_out:
        Path(args.json_out).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 1 if result["error_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
