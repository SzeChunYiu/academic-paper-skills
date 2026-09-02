#!/usr/bin/env python3
"""Validate a section/archetype scholarly-register observation profile.

The verifier checks that a persistent style calibration record is function-based,
evidence-layered, section-sensitive, and copyright-safe. It deliberately does
not score prose for "human-likeness", burstiness, lexical rarity, or resemblance
to a prestigious journal.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.0.0"
VALID_MODES = {"local_section", "whole_manuscript"}
SOURCE_TYPES = {"corpus_meta", "editorial_guidance", "deep_paper"}
TRANSFER_DECISIONS = {"adopt", "adapt", "reject", "unresolved"}
CONFIDENCE = {"low", "moderate", "high"}
RELEASE_DECISIONS = {"PASS", "REVIEW", "BLOCKED"}

REQUIRED_TOP = (
    "schema_version",
    "profile_id",
    "mode",
    "target",
    "article_type",
    "archetype",
    "evidence_sources",
    "sections",
    "manuscript_voice_invariants",
    "cross_section_register_transitions",
    "copyright_boundary",
    "unresolved_gaps",
    "release",
)

REQUIRED_SOURCE = (
    "source_id",
    "source_type",
    "reference",
    "scope",
    "support",
    "transfer_limit",
)

REQUIRED_SECTION = (
    "section_kind",
    "reader_job",
    "rhetorical_mode",
    "opening_moves",
    "paragraph_nuclei",
    "argument_tempo",
    "agency",
    "tense",
    "stance",
    "syntax_rhythm",
    "citation_integration",
    "numerical_formal_density",
    "list_box_use",
    "figure_table_interaction",
    "transition_behavior",
    "closing_handoff",
    "deliberately_absent",
    "legitimate_alternatives",
    "transfer_decision",
    "confidence",
)

FORBIDDEN_KEYS = {
    "phrase_templates",
    "sentence_templates",
    "copied_phrases",
    "copied_sentences",
    "source_sentences",
    "reusable_phrases",
    "prestige_phrase_bank",
    "ai_detector_score",
    "burstiness_score",
    "human_likeness_score",
}


def _finding(code: str, severity: str, message: str, pointer: str | None = None) -> dict[str, Any]:
    return {"code": code, "severity": severity, "message": message, "pointer": pointer}


def _nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _nonempty_text_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(_nonempty_text(v) for v in value)


def _walk_forbidden(value: Any, pointer: str = "$") -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_pointer = f"{pointer}.{key}"
            if key in FORBIDDEN_KEYS:
                findings.append(
                    _finding(
                        "forbidden_style_copy_or_detector_field",
                        "error",
                        f"Forbidden field {key!r}: store rhetorical abstractions, not source phrase banks or detector-oriented scores",
                        child_pointer,
                    )
                )
            findings.extend(_walk_forbidden(child, child_pointer))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            findings.extend(_walk_forbidden(child, f"{pointer}[{index}]"))
    return findings


def _register_fingerprint(section: dict[str, Any]) -> tuple[str, ...]:
    fields = (
        "rhetorical_mode",
        "argument_tempo",
        "agency",
        "stance",
        "syntax_rhythm",
        "list_box_use",
        "transition_behavior",
        "closing_handoff",
    )
    return tuple(str(section.get(field, "")).strip().casefold() for field in fields)


def _decision(findings: list[dict[str, Any]]) -> str:
    severities = {item["severity"] for item in findings}
    if "error" in severities:
        return "BLOCKED"
    if "review" in severities:
        return "REVIEW"
    return "PASS"


def validate(record: dict[str, Any]) -> dict[str, Any]:
    findings = _walk_forbidden(record)

    for key in REQUIRED_TOP:
        if key not in record:
            findings.append(_finding("missing_top_level", "error", f"Missing required field: {key}", key))

    if record.get("schema_version") != SCHEMA_VERSION:
        findings.append(
            _finding(
                "unsupported_schema_version",
                "error",
                f"schema_version must be {SCHEMA_VERSION}",
                "schema_version",
            )
        )

    for key in ("profile_id", "target", "article_type", "archetype"):
        if key in record and not _nonempty_text(record.get(key)):
            findings.append(_finding("empty_required_text", "error", f"{key} must be non-empty", key))

    mode = record.get("mode")
    if mode not in VALID_MODES:
        findings.append(_finding("invalid_mode", "error", f"Unsupported mode: {mode}", "mode"))

    sources = record.get("evidence_sources")
    source_types: set[str] = set()
    source_ids: set[str] = set()
    if not isinstance(sources, list) or not sources:
        findings.append(_finding("evidence_sources_missing", "error", "At least one evidence source is required", "evidence_sources"))
        sources = []

    for index, source in enumerate(sources):
        pointer = f"evidence_sources[{index}]"
        if not isinstance(source, dict):
            findings.append(_finding("invalid_source", "error", "Evidence source must be an object", pointer))
            continue
        for key in REQUIRED_SOURCE:
            if key not in source:
                findings.append(_finding("source_field_missing", "error", f"Evidence source missing {key}", f"{pointer}.{key}"))
        source_id = str(source.get("source_id") or "").strip()
        if not source_id:
            findings.append(_finding("source_id_empty", "error", "source_id must be non-empty", f"{pointer}.source_id"))
        elif source_id in source_ids:
            findings.append(_finding("duplicate_source_id", "error", f"Duplicate source_id: {source_id}", f"{pointer}.source_id"))
        else:
            source_ids.add(source_id)
        source_type = source.get("source_type")
        if source_type not in SOURCE_TYPES:
            findings.append(_finding("invalid_source_type", "error", f"Unsupported source_type: {source_type}", f"{pointer}.source_type"))
        else:
            source_types.add(source_type)
        for key in ("reference", "scope", "support", "transfer_limit"):
            if key in source and not _nonempty_text(source.get(key)):
                findings.append(_finding("source_text_empty", "error", f"{key} must be non-empty", f"{pointer}.{key}"))

    if mode == "whole_manuscript":
        missing_layers = SOURCE_TYPES - source_types
        if missing_layers:
            findings.append(
                _finding(
                    "whole_profile_evidence_layer_gap",
                    "review",
                    "Whole-manuscript register calibration should normally combine corpus/meta evidence, editorial/venue guidance, and deep-paper reading; missing: "
                    + ", ".join(sorted(missing_layers)),
                    "evidence_sources",
                )
            )
    elif mode == "local_section" and "deep_paper" not in source_types:
        findings.append(
            _finding(
                "local_profile_missing_close_paper",
                "review",
                "Local section calibration should normally include at least one genuinely close deep-paper observation rather than rely only on generic style guidance",
                "evidence_sources",
            )
        )

    sections = record.get("sections")
    if not isinstance(sections, list) or not sections:
        findings.append(_finding("sections_missing", "error", "At least one section observation is required", "sections"))
        sections = []

    seen_section_kinds: set[str] = set()
    fingerprints: list[tuple[str, ...]] = []
    unresolved_transfers = 0
    low_confidence = 0

    for index, section in enumerate(sections):
        pointer = f"sections[{index}]"
        if not isinstance(section, dict):
            findings.append(_finding("invalid_section", "error", "Section observation must be an object", pointer))
            continue
        for key in REQUIRED_SECTION:
            if key not in section:
                findings.append(_finding("section_field_missing", "error", f"Section observation missing {key}", f"{pointer}.{key}"))

        section_kind = str(section.get("section_kind") or "").strip()
        if not section_kind:
            findings.append(_finding("section_kind_empty", "error", "section_kind must be non-empty", f"{pointer}.section_kind"))
        elif section_kind in seen_section_kinds:
            findings.append(
                _finding(
                    "duplicate_section_kind",
                    "review",
                    f"Multiple observations use section_kind {section_kind!r}; consolidate them or explain the distinct sub-registers in one section record",
                    f"{pointer}.section_kind",
                )
            )
        else:
            seen_section_kinds.add(section_kind)

        for key in (
            "reader_job",
            "rhetorical_mode",
            "argument_tempo",
            "agency",
            "tense",
            "stance",
            "syntax_rhythm",
            "citation_integration",
            "numerical_formal_density",
            "list_box_use",
            "figure_table_interaction",
            "transition_behavior",
            "closing_handoff",
        ):
            if key in section and not _nonempty_text(section.get(key)):
                findings.append(_finding("section_text_empty", "error", f"{key} must be non-empty", f"{pointer}.{key}"))

        for key in ("opening_moves", "paragraph_nuclei"):
            if key in section and not _nonempty_text_list(section.get(key)):
                findings.append(_finding("section_list_empty", "error", f"{key} must contain at least one non-empty observation", f"{pointer}.{key}"))

        for key in ("deliberately_absent", "legitimate_alternatives"):
            value = section.get(key)
            if key in section and (not isinstance(value, list) or not all(_nonempty_text(v) for v in value)):
                findings.append(_finding("invalid_optional_text_list", "error", f"{key} must be a list of non-empty strings", f"{pointer}.{key}"))

        transfer = section.get("transfer_decision")
        if transfer not in TRANSFER_DECISIONS:
            findings.append(_finding("invalid_transfer_decision", "error", f"Unsupported transfer_decision: {transfer}", f"{pointer}.transfer_decision"))
        elif transfer == "unresolved":
            unresolved_transfers += 1

        confidence = section.get("confidence")
        if confidence not in CONFIDENCE:
            findings.append(_finding("invalid_confidence", "error", f"Unsupported confidence: {confidence}", f"{pointer}.confidence"))
        elif confidence == "low":
            low_confidence += 1

        fingerprints.append(_register_fingerprint(section))

    if mode == "whole_manuscript" and len(seen_section_kinds) < 3:
        findings.append(
            _finding(
                "whole_profile_too_narrow",
                "review",
                "Whole-manuscript calibration should normally observe at least three distinct manuscript surfaces so cross-section register differences can be assessed",
                "sections",
            )
        )

    if len(fingerprints) >= 3 and len(set(fingerprints)) == 1:
        findings.append(
            _finding(
                "uniform_register_across_sections",
                "review",
                "Three or more active sections have the same recorded register across rhetorical mode, tempo, agency, stance, syntax, list use, transitions, and closure. Verify that the manuscript has not been flattened into one generic prose template.",
                "sections",
            )
        )

    if unresolved_transfers:
        findings.append(
            _finding(
                "unresolved_style_transfer",
                "review",
                f"{unresolved_transfers} section observation(s) still have unresolved transfer decisions",
                "sections",
            )
        )
    if low_confidence:
        findings.append(
            _finding(
                "low_confidence_style_observation",
                "review",
                f"{low_confidence} section observation(s) are low-confidence; avoid turning them into hard writing rules",
                "sections",
            )
        )

    voice = record.get("manuscript_voice_invariants")
    if not _nonempty_text_list(voice):
        findings.append(
            _finding(
                "voice_invariants_missing",
                "error",
                "Record at least one manuscript-level voice invariant so section register switching does not erase author identity",
                "manuscript_voice_invariants",
            )
        )

    transitions = record.get("cross_section_register_transitions")
    if not isinstance(transitions, list) or not all(_nonempty_text(v) for v in transitions):
        findings.append(
            _finding(
                "invalid_register_transitions",
                "error",
                "cross_section_register_transitions must be a list of non-empty strings",
                "cross_section_register_transitions",
            )
        )
    elif mode == "whole_manuscript" and len(seen_section_kinds) >= 2 and not transitions:
        findings.append(
            _finding(
                "cross_section_transition_missing",
                "review",
                "Whole-manuscript profile has multiple section registers but records no deliberate register transition",
                "cross_section_register_transitions",
            )
        )

    copyright_boundary = record.get("copyright_boundary")
    if not isinstance(copyright_boundary, dict):
        findings.append(_finding("copyright_boundary_missing", "error", "copyright_boundary must be an object", "copyright_boundary"))
    else:
        for key in ("source_sentences_stored", "phrase_templates_stored", "distinctive_wording_reused"):
            value = copyright_boundary.get(key)
            if value is not False:
                findings.append(
                    _finding(
                        "copyright_boundary_failed",
                        "error",
                        f"{key} must be false; retain rhetorical abstractions, not source wording",
                        f"copyright_boundary.{key}",
                    )
                )
        if not _nonempty_text(copyright_boundary.get("note")):
            findings.append(_finding("copyright_note_missing", "error", "copyright_boundary.note must be non-empty", "copyright_boundary.note"))

    gaps = record.get("unresolved_gaps")
    if not isinstance(gaps, list) or not all(_nonempty_text(v) for v in gaps):
        findings.append(_finding("invalid_unresolved_gaps", "error", "unresolved_gaps must be a list of non-empty strings", "unresolved_gaps"))
    elif gaps:
        findings.append(
            _finding(
                "register_research_gaps_remain",
                "review",
                f"{len(gaps)} unresolved register research gap(s) remain; keep affected guidance provisional",
                "unresolved_gaps",
            )
        )

    computed = _decision(findings)
    release = record.get("release")
    if not isinstance(release, dict):
        findings.append(_finding("release_missing", "error", "release must be an object", "release"))
    else:
        recorded = release.get("decision")
        if recorded not in RELEASE_DECISIONS:
            findings.append(_finding("invalid_release_decision", "error", f"Unsupported release decision: {recorded}", "release.decision"))
        elif recorded != computed:
            findings.append(
                _finding(
                    "stale_release_decision",
                    "error",
                    f"Recorded release decision {recorded} does not match computed decision {computed}",
                    "release.decision",
                )
            )
        notes = release.get("notes")
        if not isinstance(notes, list) or not all(_nonempty_text(v) for v in notes):
            findings.append(_finding("invalid_release_notes", "error", "release.notes must be a list of non-empty strings", "release.notes"))

    return summarize(findings, record)


def summarize(findings: list[dict[str, Any]], record: dict[str, Any]) -> dict[str, Any]:
    counts = Counter(item["severity"] for item in findings)
    return {
        "decision": _decision(findings),
        "profile_id": record.get("profile_id"),
        "mode": record.get("mode"),
        "counts": {"error": counts["error"], "review": counts["review"]},
        "findings": findings,
        "notes": [
            "This verifier checks calibration completeness and section sensitivity, not whether prose is objectively human or publication-worthy.",
            "No detector score, sentence-length variance, vocabulary rarity, or resemblance-to-journal score is used.",
            "Published-paper observations remain descriptive priors; actual prose must follow scientific function, evidence, target requirements, and author voice.",
        ],
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate a scholarly-register observation profile.")
    parser.add_argument("profile", type=Path)
    parser.add_argument("--pretty", action="store_true")
    parser.add_argument("--report", type=Path)
    return parser


def main() -> int:
    args = _parser().parse_args()
    try:
        record = json.loads(args.profile.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"error: {exc}", file=sys.stderr)
        return 2

    payload = validate(record)
    rendered = json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if payload["decision"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
