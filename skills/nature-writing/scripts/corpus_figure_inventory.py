#!/usr/bin/env python3
"""Describe figure/table usage across an extracted academic-paper corpus.

This is a descriptive calibration tool, not a quality or acceptance scorer. It
extracts figure/table captions and in-text display calls from Markdown/plain text
and applies transparent keyword heuristics to propose *candidate* evidence roles.
Use semantic/manual review before turning any frequency into a writing rule.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


TEXT_SUFFIXES = {".md", ".markdown", ".txt"}

ROLE_PATTERNS: dict[str, tuple[str, ...]] = {
    "orientation_workflow": (
        "overview", "workflow", "study design", "experimental design", "framework",
        "pipeline", "schematic", "architecture", "cohort", "participant flow",
        "consort", "sampling", "study population", "dataset overview",
    ),
    "primary_effect_finding": (
        "effect", "primary outcome", "main result", "phenotype", "response",
        "difference", "change in", "performance", "association", "distribution",
    ),
    "mechanism_explanation": (
        "mechanism", "mediates", "regulates", "pathway", "force", "dynamics",
        "interaction", "causal", "dependency", "perturbation", "molecular",
    ),
    "validation_replication": (
        "validation", "validated", "replication", "independent cohort", "external cohort",
        "ground truth", "reference standard", "orthogonal", "reproducibility",
    ),
    "generalization_ood": (
        "generalization", "generalisation", "out-of-distribution", "ood", "external",
        "unseen", "transfer", "cross-site", "cross-dataset", "cross-domain",
    ),
    "robustness_sensitivity": (
        "robustness", "sensitivity", "sensitivity analysis", "ablation", "perturbation test",
        "parameter", "hyperparameter", "bootstrap", "subsample", "stability",
    ),
    "failure_limitation": (
        "limitation", "failure", "fails", "error analysis", "failure mode", "negative result",
        "does not", "no improvement", "bias", "breakdown", "boundary",
    ),
    "heterogeneity_subgroup": (
        "heterogeneity", "subgroup", "stratified", "site-specific", "site specific",
        "individual variation", "between-site", "between site", "forest plot",
    ),
    "calibration_diagnostic": (
        "calibration", "reliability", "diagnostic", "residual", "roc", "precision-recall",
        "precision recall", "confusion matrix", "survival", "cumulative incidence",
    ),
    "resource_coverage_quality": (
        "coverage", "geographic", "geographical", "temporal coverage", "data quality",
        "quality control", "missingness", "completeness", "richness", "composition",
        "resource", "dataset", "database",
    ),
    "theory_model": (
        "theorem", "proof", "bound", "convergence", "phase diagram", "mathematical model",
        "theoretical", "simulation", "numerical illustration", "regime",
    ),
    "qualitative_synthesis": (
        "theme", "thematic", "conceptual model", "qualitative", "interview", "framework analysis",
        "process model", "participant characteristics",
    ),
}

CAPTION_START = re.compile(
    r"^\s*(?P<label>(?:Fig(?:ure)?\.?|Table)\s*(?P<num>[A-Za-z]?\d+[A-Za-z]?))\s*(?:[|:.\-–—]|\s)\s*(?P<rest>.+?)\s*$",
    flags=re.IGNORECASE,
)
DISPLAY_CALL = re.compile(r"\b(?P<kind>Fig(?:ure)?\.?|Table)\s*(?P<num>[A-Za-z]?\d+[A-Za-z]?)\b", re.IGNORECASE)
MARKDOWN_IMAGE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<target>[^)]+)\)")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")


@dataclass(frozen=True)
class DisplayRecord:
    path: str
    kind: str
    number: str
    caption: str
    section: str | None
    candidate_roles: tuple[str, ...]
    role_method: str = "keyword_heuristic_review_required"


@dataclass(frozen=True)
class DocumentSummary:
    path: str
    figure_caption_count: int
    table_caption_count: int
    figure_call_count: int
    table_call_count: int
    unique_figure_calls: int
    unique_table_calls: int
    candidate_role_counts: dict[str, int]


def classify_roles(text: str) -> tuple[str, ...]:
    lowered = re.sub(r"\s+", " ", text.lower())
    roles: list[str] = []
    for role, terms in ROLE_PATTERNS.items():
        if any(term in lowered for term in terms):
            roles.append(role)
    return tuple(roles or ["unclassified"])


def _normalize_kind(raw: str) -> str:
    return "table" if raw.lower().startswith("table") else "figure"


def _looks_like_caption_continuation(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if HEADING.match(line) or CAPTION_START.match(line):
        return False
    if stripped.startswith(("- ", "* ", "> ", "```")):
        return False
    # Keep continuation conservative: likely prose, not a new section/list.
    return len(stripped) >= 12


def extract_displays(path: Path, text: str) -> list[DisplayRecord]:
    lines = text.splitlines()
    current_section: str | None = None
    records: list[DisplayRecord] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        heading = HEADING.match(line)
        if heading:
            current_section = re.sub(r"[*_`]+", "", heading.group(1)).strip()
            i += 1
            continue

        match = CAPTION_START.match(line)
        if match:
            kind = _normalize_kind(match.group("label"))
            number = match.group("num")
            parts = [match.group("rest").strip()]
            j = i + 1
            # Many extracted PDFs wrap captions over lines. Keep a small bounded
            # continuation window so article body paragraphs are not swallowed.
            while j < len(lines) and len(parts) < 4 and _looks_like_caption_continuation(lines[j]):
                candidate = lines[j].strip()
                if DISPLAY_CALL.match(candidate):
                    break
                parts.append(candidate)
                j += 1
            caption = " ".join(parts)
            records.append(
                DisplayRecord(
                    path=str(path),
                    kind=kind,
                    number=number,
                    caption=caption,
                    section=current_section,
                    candidate_roles=classify_roles(caption),
                )
            )
            i = j
            continue

        # If a Markdown image alt-text itself looks like a scientific caption,
        # retain it as an unnumbered figure only when no conventional caption is present.
        for image in MARKDOWN_IMAGE.finditer(line):
            alt = image.group("alt").strip()
            if len(alt) >= 20 and not alt.lower().startswith(("logo", "banner", "icon")):
                records.append(
                    DisplayRecord(
                        path=str(path),
                        kind="figure",
                        number="unnumbered",
                        caption=alt,
                        section=current_section,
                        candidate_roles=classify_roles(alt),
                    )
                )
        i += 1
    return records


def summarize_document(path: Path, text: str, displays: list[DisplayRecord]) -> DocumentSummary:
    calls = [( _normalize_kind(m.group("kind")), m.group("num") ) for m in DISPLAY_CALL.finditer(text)]
    figure_calls = [n for k, n in calls if k == "figure"]
    table_calls = [n for k, n in calls if k == "table"]
    roles: Counter[str] = Counter()
    for record in displays:
        roles.update(record.candidate_roles)
    return DocumentSummary(
        path=str(path),
        figure_caption_count=sum(d.kind == "figure" for d in displays),
        table_caption_count=sum(d.kind == "table" for d in displays),
        figure_call_count=len(figure_calls),
        table_call_count=len(table_calls),
        unique_figure_calls=len(set(figure_calls)),
        unique_table_calls=len(set(table_calls)),
        candidate_role_counts=dict(sorted(roles.items())),
    )


def iter_paths(inputs: Iterable[Path]) -> list[Path]:
    found: set[Path] = set()
    for item in inputs:
        if item.is_dir():
            for path in item.rglob("*"):
                if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                    found.add(path)
        elif item.is_file() and item.suffix.lower() in TEXT_SUFFIXES:
            found.add(item)
    return sorted(found)


def aggregate(summaries: list[DocumentSummary], displays: list[DisplayRecord]) -> dict:
    roles: Counter[str] = Counter()
    for display in displays:
        roles.update(display.candidate_roles)
    return {
        "documents": len(summaries),
        "figure_captions": sum(s.figure_caption_count for s in summaries),
        "table_captions": sum(s.table_caption_count for s in summaries),
        "candidate_role_counts": dict(sorted(roles.items())),
        "methodological_warning": (
            "Candidate roles are transparent keyword heuristics for corpus triage, not semantic ground truth, "
            "writing-quality scores, acceptance predictors, or instructions to copy frequent plot types."
        ),
    }


def write_csv(path: Path, displays: list[DisplayRecord]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["path", "kind", "number", "section", "caption", "candidate_roles", "role_method"],
        )
        writer.writeheader()
        for display in displays:
            row = asdict(display)
            row["candidate_roles"] = ";".join(display.candidate_roles)
            writer.writerow(row)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path, help="Paper text files or directories")
    parser.add_argument("--json", dest="json_path", type=Path, help="Write full JSON report")
    parser.add_argument("--csv", dest="csv_path", type=Path, help="Write display-level CSV")
    args = parser.parse_args()

    paths = iter_paths(args.inputs)
    all_displays: list[DisplayRecord] = []
    summaries: list[DocumentSummary] = []
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        displays = extract_displays(path, text)
        all_displays.extend(displays)
        summaries.append(summarize_document(path, text, displays))

    report = {
        "aggregate": aggregate(summaries, all_displays),
        "documents": [asdict(s) for s in summaries],
        "displays": [asdict(d) for d in all_displays],
    }
    print(json.dumps(report["aggregate"], indent=2, ensure_ascii=False))
    if args.json_path:
        args.json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    if args.csv_path:
        write_csv(args.csv_path, all_displays)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
