#!/usr/bin/env python3
"""Structural content-type detector for a manuscript.

This module answers one narrow question: **does this manuscript body actually
contain primary research that the manuscript itself produced?**

It exists because preprint repositories and journals increasingly gate on
*content type* (research article vs review/survey vs position/perspective)
rather than on quality. A gate built on title keywords is worthless: it can be
satisfied by renaming. A gate built on structure cannot, because it reads what
the manuscript displays.

Two independent readings are produced and deliberately kept apart:

``structural``
    What the body shows: a results-bearing section, a methods-bearing section,
    displayed quantities, tables and figures that carry measurements, and
    availability statements. Derived only from the manuscript body.

``declared``
    What the paper calls itself in its title, abstract, and the free-text
    comments the author will paste into a submission form.

Keeping them apart is the point. Agreement is evidence. Disagreement is a
finding, and the *direction* of the disagreement decides what may be done:

* declared review/position + structural primary research
      -> the label understates the paper. Correcting the label is legitimate
         and makes the paper more accurate.
* declared research + structural synthesis-only
      -> the label overstates the paper. Correcting the *label* would be
         misrepresentation. This detector marks it and refuses to suggest a
         relabel; the manuscript must change or the route must change.

The detector never decides admissibility. It reports evidence.
``verify_preprint_admissibility.py`` applies repository policy to this output.

Exit codes
    0  detection succeeded
    2  detection could not be performed (unreadable/empty input)

There is deliberately no exit code 1: this tool has no pass/fail opinion.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "preprint.content-type-detection.v1"

# --------------------------------------------------------------------------
# Section vocabulary.
#
# Deliberately generous: we are asking "is there a section playing this role",
# not "is it named exactly this". Field conventions vary widely, and a gate
# that only recognises the word "Results" would misread a mathematics paper.
# --------------------------------------------------------------------------

RESULTS_ROLE = (
    "result",
    "results",
    "findings",
    "experiment",
    "experiments",
    "experimental results",
    "evaluation",
    "empirical evaluation",
    "empirical results",
    "experiments and results",
    "study",
    "studies",
    "analysis",
    "observations",
    "measurements",
    "theorem",
    "theorems",
    "main theorem",
    "main results",
    "construction",
    "proof",
    "proofs",
)

METHODS_ROLE = (
    "method",
    "methods",
    "methodology",
    "materials and methods",
    "experimental setup",
    "setup",
    "protocol",
    "study design",
    "design",
    "implementation",
    "model",
    "models",
    "formal setting",
    "preliminaries",
    "definitions",
    "problem statement",
    "problem setting",
    "approach",
    "algorithm",
    "algorithms",
)

SYNTHESIS_ROLE = (
    "background",
    "related work",
    "prior work",
    "literature review",
    "review of",
    "survey",
    "state of the art",
    "landscape",
    "taxonomy",
    "open problems",
    "open questions",
    "research agenda",
    "roadmap",
    "outlook",
    "vision",
    "call to action",
    "position",
    "recommendations",
)

AVAILABILITY_ROLE = (
    "data availability",
    "code availability",
    "data and code availability",
    "availability",
    "reproducibility",
    "artifact",
    "artefact",
)

# Words a paper uses to name its own content type. Matched only in the
# declared surfaces (title / abstract / comments), never in the body, because
# a research paper may legitimately discuss perspectives and programmes.
DECLARED_TYPE_MARKERS = {
    "review": ("review article", "we review", "this review", "survey of", "we survey", "this survey"),
    "position": (
        "position paper",
        "this position",
        "we argue that the field",
        "call to action",
        "manifesto",
    ),
    "perspective": ("this perspective", "perspective article", "in this perspective"),
    "programme": (
        "research programme",
        "research program",
        "programme proposal",
        "program proposal",
        "we propose a programme",
        "we propose a program",
        "research agenda",
        "roadmap for",
        "toward a science of",
        "towards a science of",
        "a new field",
        "a distinct field",
    ),
}

# Content-type words matched in the TITLE only. Restricting these to the title
# keeps the false-positive rate low: a research paper may discuss a "review
# process" in its body, but one that puts "Survey" in its own title is telling
# the moderator what it is.
TITLE_TYPE_WORDS = {
    "review": ("review", "overview"),
    "programme": ("roadmap", "agenda", "manifesto"),
    "perspective": ("perspective",),
    "position": ("position paper",),
    "survey": ("survey", "tutorial", "primer"),
}

# Explicit self-negations of primary research. These are strong signals and
# are reported verbatim, because a single such sentence can decide a
# content-type call on its own.
PRIMARY_RESEARCH_NEGATIONS = (
    "does not report a new primary empirical study",
    "does not report new primary research",
    "reports no new primary",
    "no new experiments are reported",
    "does not present new data",
    "no new data are presented",
    "does not report original research",
)

_TEX_SECTION = re.compile(
    r"\\(?:sub){0,2}section\*?\s*\{([^}]{1,200})\}",
    re.IGNORECASE,
)
_MD_SECTION = re.compile(r"^\s{0,3}#{1,4}\s+(.{1,200}?)\s*$", re.MULTILINE)

# A displayed quantity: a number that is doing reporting work. Bare years and
# reference markers are excluded by requiring either a decimal point, a
# comparison/relation context, a unit, or a percent sign.
_QUANTITY = re.compile(
    r"(?<![\w.])(?:"
    r"\d{1,3}(?:,\d{3})+"          # 1,200
    r"|\d+\.\d+"                    # 0.983
    r"|\d+\s*%"                     # 42 %
    r"|\d+\s*/\s*\d+"               # 1000/1000
    r"|[pP]\s*[=<>]\s*[\d.]+"       # p = 0.0032
    r"|\d+\s*(?:ms|s|GB|MB|KB|Hz|kHz|K|nm|mm|cm|km|kg|mg)\b"
    r")(?![\w])"
)

# Formal-result environments. A mathematics or theory paper displays its
# primary research as theorems and proofs, not as measurements, and a gate that
# only looks for tables of numbers would read such a paper as having produced
# nothing of its own.
_THEOREM_ENV = re.compile(
    r"\\begin\{(?:theorem|lemma|proposition|corollary|claim|definition|proof)\*?\}"
    r"|^\s*#{1,4}\s*(?:theorem|lemma|proposition|corollary)\b"
    r"|(?<![a-z])(?:theorem|lemma|proposition|corollary)\s+\d+(?:\.\d+)*",
    re.IGNORECASE | re.MULTILINE,
)

# First-person research acts: the author saying the manuscript did something.
# Counted as a whole-body signal because papers with essayistic section titles
# ("dense controlled studies", "robustness battery") carry their primary work
# without ever using the word "Results" as a heading.
_OWN_WORK = re.compile(
    r"(?<![a-z])(?:we|this (?:paper|study|article|work))\s+"
    r"(?:prove[sd]?|show[sn]?|demonstrate[sd]?|report[sd]?|measure[sd]?|"
    r"evaluate[sd]?|test(?:s|ed)?|run|ran|execute[sd]?|construct(?:s|ed)?|"
    r"implement(?:s|ed)?|register(?:s|ed)?|derive[sd]?|establish(?:es|ed)?|"
    r"introduce[sd]?|present(?:s|ed)?|compute[sd]?|verif(?:y|ies|ied))"
    r"|(?<![a-z])our (?:experiments?|study|studies|results?|analysis|benchmark|"
    r"protocol|implementation|construction)",
    re.IGNORECASE,
)

# Display mathematics. Short theory papers routinely carry their primary
# results as displayed definitions and derivations with no table or figure at
# all; without this signal four such manuscripts in the calibration corpus were
# indistinguishable from prose essays.
_DISPLAY_MATH = re.compile(
    r"\\begin\{(?:equation|align|gather|multline|eqnarray|displaymath)\*?\}"
    r"|\\\[",
)

_TEX_TABLE = re.compile(r"\\begin\{(?:table|tabular|longtable|tabularx)", re.IGNORECASE)
_TEX_FIGURE = re.compile(r"\\begin\{figure", re.IGNORECASE)
_MD_TABLE = re.compile(r"^\s*\|.+\|\s*$", re.MULTILINE)
_MD_FIGURE = re.compile(r"^\s*!\[", re.MULTILINE)
# Citation forms differ by toolchain and must all count, or a heavily-cited
# review reads as having no literature at all. Covers natbib/biblatex command
# families (cite, citep, parencite, autocite, textcite, footcite), pandoc
# markdown keys, and numeric bracket references in already-rendered bodies.
_CITATION = re.compile(
    r"\\[a-zA-Z]{0,6}cite[a-zA-Z]*\s*[\[{]"
    r"|\[@[\w:.-]+"
    r"|\[\d{1,3}(?:\s*[,\u2013-]\s*\d{1,3})*\]",
    re.IGNORECASE,
)


def evidence_displays_zero(tables: int, figures: int, theorem_envs: int) -> bool:
    """True when the manuscript displays no evidence object of any kind."""
    return (tables + figures + theorem_envs) == 0


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def _strip_tex_commands(title: str) -> str:
    """Remove markup so section titles compare cleanly."""
    out = re.sub(r"\\[a-zA-Z]+\s*", " ", title)
    out = out.replace("{", " ").replace("}", " ").replace("\\", " ")
    return _norm(out)


def _role_of(section_title: str) -> set[str]:
    """Map a section title to the roles it plays. A title may play several."""
    t = _strip_tex_commands(section_title)
    roles: set[str] = set()

    def hit(needles: tuple[str, ...]) -> bool:
        # Word-boundary matching throughout. Substring matching reads
        # "the composition calculus" as a position paper, because "composition"
        # contains "position"; that single false positive is enough to make a
        # gate untrustworthy on its first real run.
        return any(
            re.search(rf"(?<![a-z]){re.escape(n)}(?![a-z])", t) for n in needles
        )

    # Synthesis is not exclusive: "Related work" in a research paper is normal
    # and must not suppress the Results reading.
    if hit(SYNTHESIS_ROLE):
        roles.add("synthesis")
    if hit(AVAILABILITY_ROLE):
        roles.add("availability")
    if hit(RESULTS_ROLE):
        roles.add("results")
    if hit(METHODS_ROLE):
        roles.add("methods")
    return roles


def _section_marks(body: str, fmt: str) -> list[tuple[str, int, int]]:
    """Locate section headings, tolerating mixed-format bodies.

    A LaTeX master that pulls Markdown prose in via the ``markdown`` package
    (\\markdownInput) flattens to a file whose suffix says .tex but whose
    headings are Markdown. Keying the pattern off the suffix alone reports such
    a manuscript as having no sections at all, which silently turns a complete
    research paper into a synthesis reading. Both patterns are therefore always
    applied and their hits merged in document order.
    """
    marks = [(m.group(1), m.start(), m.end()) for m in _TEX_SECTION.finditer(body)]
    marks += [(m.group(1), m.start(), m.end()) for m in _MD_SECTION.finditer(body)]
    marks.sort(key=lambda t: t[1])
    return marks


def extract_sections(body: str, fmt: str) -> list[str]:
    return [t for t, _s, _e in _section_marks(body, fmt)]


def _section_spans(body: str, fmt: str) -> list[tuple[str, int, int]]:
    marks = _section_marks(body, fmt)
    spans: list[tuple[str, int, int]] = []
    for i, (title, _start, end) in enumerate(marks):
        stop = marks[i + 1][1] if i + 1 < len(marks) else len(body)
        spans.append((title, end, stop))
    return spans


def detect(body: str, fmt: str, declared: dict[str, str]) -> dict[str, Any]:
    sections = extract_sections(body, fmt)
    spans = _section_spans(body, fmt)

    roles_seen: dict[str, list[str]] = {}
    for title in sections:
        for role in _role_of(title):
            roles_seen.setdefault(role, []).append(_strip_tex_commands(title))

    # Quantities displayed inside results-bearing sections specifically. A
    # paper that cites other people's numbers in its introduction is not
    # thereby reporting results.
    results_text_len = 0
    results_quantities = 0
    for title, start, stop in spans:
        if "results" in _role_of(title):
            segment = body[start:stop]
            results_text_len += len(segment)
            results_quantities += len(_QUANTITY.findall(segment))

    total_quantities = len(_QUANTITY.findall(body))
    citations = len(_CITATION.findall(body))

    # Counted in both notations for the same reason section headings are: a
    # flattened body can carry LaTeX floats and Markdown pipe tables at once.
    md_table_lines = len(_MD_TABLE.findall(body))
    tables = len(_TEX_TABLE.findall(body)) + (1 if md_table_lines >= 2 else 0)
    figures = len(_TEX_FIGURE.findall(body)) + len(_MD_FIGURE.findall(body))

    lowered = _norm(body)
    negations = [n for n in PRIMARY_RESEARCH_NEGATIONS if n in lowered]

    declared_hits: dict[str, list[str]] = {}
    declared_blob = _norm(" ".join(v for v in declared.values() if v))
    for label, needles in DECLARED_TYPE_MARKERS.items():
        found = [n for n in needles if n in declared_blob]
        if found:
            declared_hits[label] = found

    # The title is the single strongest declared surface and is checked on its
    # own vocabulary. A calibration survey titled "Large Language Models: A
    # Survey" carries none of the sentence-level markers above, because it
    # never needs to say "this survey" in its own title.
    title_norm = _norm(declared.get("title", ""))
    for label, words in TITLE_TYPE_WORDS.items():
        found = [w for w in words if re.search(rf"(?<![a-z]){re.escape(w)}(?![a-z])", title_norm)]
        if found:
            declared_hits.setdefault(label, []).extend("title:" + w for w in found)

    has_results = "results" in roles_seen
    has_methods = "methods" in roles_seen
    has_availability = "availability" in roles_seen

    theorem_envs = len(_THEOREM_ENV.findall(body))
    own_work = len(_OWN_WORK.findall(body))
    display_math = len(_DISPLAY_MATH.findall(body))

    # Positive indicators that this manuscript IS a review or position piece.
    #
    # This is the block the repository-policy gate consumes, and it is kept
    # separate from the research reading on purpose. A rule that excludes
    # reviews and position papers must fire on evidence that a manuscript is
    # one, never on mere failure to prove it is not. Conflating the two turns
    # every terse theory paper into a suspected review.
    synthesis_indicators: list[str] = []
    if negations:
        synthesis_indicators.append("explicit_primary_research_negation")
    if declared_hits:
        synthesis_indicators.append("declared_review_or_position_label")
    if citations >= 40 and evidence_displays_zero(tables, figures, theorem_envs):
        synthesis_indicators.append("high_citation_density_with_no_evidence_display")
    # "Predominantly synthesis" means the synthesis sections outnumber the
    # results-bearing ones AND the manuscript displays no evidence of its own.
    # Counting synthesis sections alone flags any theory paper with a long
    # related-work treatment.
    synthesis_section_titles = roles_seen.get("synthesis", [])
    results_section_titles = roles_seen.get("results", [])
    if (
        len(synthesis_section_titles) >= 3
        and len(synthesis_section_titles) > len(results_section_titles)
        and evidence_displays_zero(tables, figures, theorem_envs)
    ):
        synthesis_indicators.append("predominantly_synthesis_sections")

    # Structural verdict.
    #
    # The burden of proof runs one way on purpose. A repository rule of this
    # kind excludes manuscripts that ARE reviews or position pieces; it does
    # not require every other manuscript to prove it is not one. So the
    # detector asks for positive evidence of synthesis-only before saying so,
    # and treats any evidence display as primary research.
    #
    # Section names are deliberately demoted to a supporting signal. Real
    # research papers routinely name their results sections descriptively, and
    # an earlier revision of this detector read five such papers as having no
    # results at all purely because no heading contained the word "Results".
    evidence_displays = tables + figures + theorem_envs
    formal_displays = evidence_displays + display_math
    has_own_output = (
        evidence_displays >= 1
        or own_work >= 3
        or results_quantities >= 3
        or display_math >= 5
    )

    if has_own_output and (has_results or has_methods) and formal_displays >= 1:
        structural = "PRIMARY_RESEARCH_PRESENT"
    elif has_own_output:
        structural = "PRIMARY_RESEARCH_LIKELY"
    elif "explicit_primary_research_negation" in synthesis_indicators or (
        citations >= 25 and formal_displays == 0 and own_work < 3
    ):
        structural = "SYNTHESIS_ONLY"
    else:
        structural = "INDETERMINATE"

    if negations:
        # An explicit self-negation is the strongest declared signal there is.
        # It never silently overrides a strong structural reading, because a
        # stale backmatter sentence contradicting a real Results section is
        # itself the defect worth surfacing.
        structural_conflict = structural in (
            "PRIMARY_RESEARCH_PRESENT",
            "PRIMARY_RESEARCH_LIKELY",
        )
        if not structural_conflict:
            structural = "SYNTHESIS_ONLY"
    else:
        structural_conflict = False

    declared_type = None
    for candidate in ("survey", "review", "position", "perspective", "programme"):
        if candidate in declared_hits:
            declared_type = candidate
            break

    # Direction of any label/structure mismatch decides what is permissible.
    mismatch = None
    remedy = None
    if declared_type and structural in ("PRIMARY_RESEARCH_PRESENT", "PRIMARY_RESEARCH_LIKELY"):
        mismatch = "LABEL_UNDERSTATES_CONTENT"
        remedy = (
            "The body carries primary research while the declared surfaces call the "
            "paper a {t}. Correcting the declared label to match the body is "
            "legitimate and makes the submission more accurate.".format(t=declared_type)
        )
    elif not declared_type and structural == "SYNTHESIS_ONLY":
        mismatch = "LABEL_OVERSTATES_CONTENT"
        remedy = (
            "The body carries no primary research while nothing declares the paper a "
            "review or position piece. Relabelling is NOT an available remedy: either "
            "the manuscript gains primary research, or the route changes to one that "
            "accepts synthesis."
        )

    return {
        "schema_version": SCHEMA_VERSION,
        "structural": {
            "verdict": structural,
            "has_results_section": has_results,
            "has_methods_section": has_methods,
            "has_availability_statement": has_availability,
            "section_titles": [_strip_tex_commands(s) for s in sections],
            "roles_seen": {k: v for k, v in sorted(roles_seen.items())},
            "quantities_in_results_sections": results_quantities,
            "quantities_in_body": total_quantities,
            "tables": tables,
            "figures": figures,
            "theorem_environments": theorem_envs,
            "display_math": display_math,
            "own_work_statements": own_work,
            "evidence_displays": evidence_displays,
            "formal_displays": formal_displays,
            "citations": citations,
            "explicit_primary_research_negations": negations,
            "negation_conflicts_with_structure": structural_conflict,
        },
        "declared": {
            "type": declared_type,
            "markers_found": declared_hits,
            "surfaces_checked": sorted(k for k, v in declared.items() if v),
        },
        "synthesis_indicators": synthesis_indicators,
        "mismatch": mismatch,
        "mismatch_remedy": remedy,
    }


def _read(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    fmt = "tex" if path.suffix.lower() in (".tex", ".latex") else "md"
    return text, fmt


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--manuscript", required=True, help="path to manuscript .tex or .md")
    ap.add_argument("--title", default="", help="declared title")
    ap.add_argument("--abstract", default="", help="declared abstract text or path")
    ap.add_argument("--comments", default="", help="submission-form comments field text")
    ap.add_argument("--json-out", default=None, help="write the detection record here")
    args = ap.parse_args(argv)

    path = Path(args.manuscript)
    if not path.is_file():
        print(json.dumps({"error": f"manuscript not found: {path}"}), file=sys.stderr)
        return 2
    body, fmt = _read(path)
    if not body.strip():
        print(json.dumps({"error": f"manuscript is empty: {path}"}), file=sys.stderr)
        return 2

    abstract = args.abstract
    if abstract and Path(abstract).is_file():
        abstract = Path(abstract).read_text(encoding="utf-8", errors="replace")

    # If no title was supplied, fall back to the manuscript's own title command.
    title = args.title
    if not title:
        m = re.search(r"\\title\s*\{(.{1,300}?)\}", body, re.DOTALL)
        if m:
            title = _strip_tex_commands(m.group(1))

    record = detect(body, fmt, {"title": title, "abstract": abstract, "comments": args.comments})
    record["manuscript"] = str(path)

    payload = json.dumps(record, indent=2, sort_keys=False)
    if args.json_out:
        Path(args.json_out).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
