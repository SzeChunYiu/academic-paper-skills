#!/usr/bin/env python3
"""Fail-closed verifier for the paper-existence/scientific-mass ledger.

This verifier does not decide whether a paper is important or predict journal
acceptance. It checks whether the declared disposition is internally consistent
with the hostile scientific state: a full-paper route cannot coexist with an
unsupported surviving claim, fatal unresolved objections, claim-scope/external-
validity mismatch, integrity substituted for validity, or an evidence-acquisition
blocker that explicitly stops further polishing.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP = (
    "schema_version",
    "paper_id",
    "surviving_claim",
    "hostile_panel",
    "scientific_mass",
    "novelty",
    "comparisons",
    "external_validity",
    "integrity_vs_validity",
    "sibling_overlap",
    "next_discriminator",
    "decision",
)

CORE_LENSES = {
    "field_editor",
    "methods_benchmark_statistics",
    "theory",
    "systems_reproducibility",
    "literature_portfolio",
}

DISPOSITIONS = {
    "WRITE_FULL_PAPER",
    "WAIT_FOR_EVIDENCE",
    "MERGE_WITH_SIBLING",
    "RECLASSIFY_AS_NOTE",
    "KILL_CLAIM",
    "UNRESOLVED",
}


def finding(code: str, severity: str, message: str, pointer: str | None = None) -> dict[str, Any]:
    return {"code": code, "severity": severity, "message": message, "pointer": pointer}


def summarize(findings: list[dict[str, Any]], ledger: dict[str, Any]) -> dict[str, Any]:
    severities = {item["severity"] for item in findings}
    if "error" in severities:
        verdict = "BLOCKED"
    elif "unresolved" in severities:
        verdict = "UNRESOLVED"
    elif "review" in severities:
        verdict = "REVIEW"
    else:
        verdict = "PASS"
    return {
        "verdict": verdict,
        "paper_id": ledger.get("paper_id"),
        "disposition": (ledger.get("decision") or {}).get("disposition"),
        "findings": findings,
    }


def validate(ledger: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []

    for key in REQUIRED_TOP:
        if key not in ledger:
            findings.append(finding("missing_top_level", "error", f"Missing required top-level field: {key}", key))

    if findings:
        return summarize(findings, ledger)

    if ledger.get("schema_version") != "1.0.0":
        findings.append(finding("unsupported_schema_version", "error", "schema_version must be 1.0.0", "schema_version"))

    claim = ledger.get("surviving_claim") or {}
    panel = ledger.get("hostile_panel") or []
    mass = ledger.get("scientific_mass") or {}
    novelty = ledger.get("novelty") or {}
    comparisons = ledger.get("comparisons") or {}
    ext = ledger.get("external_validity") or {}
    integrity = ledger.get("integrity_vs_validity") or {}
    siblings = ledger.get("sibling_overlap") or {}
    next_disc = ledger.get("next_discriminator") or {}
    decision = ledger.get("decision") or {}
    disposition = decision.get("disposition")

    if disposition not in DISPOSITIONS:
        findings.append(finding("invalid_disposition", "error", f"Unsupported disposition: {disposition}", "decision.disposition"))

    seen_lenses = {item.get("lens") for item in panel}
    missing_lenses = sorted(CORE_LENSES - seen_lenses)
    if missing_lenses:
        findings.append(
            finding(
                "hostile_panel_incomplete",
                "error",
                f"Missing required hostile lenses: {', '.join(missing_lenses)}",
                "hostile_panel",
            )
        )

    fatal_rows = [item for item in panel if item.get("severity") == "fatal"]
    unresolved_rows = [item for item in panel if item.get("severity") == "unresolved"]
    major_rows = [item for item in panel if item.get("severity") == "major"]
    for index, item in enumerate(panel):
        if item.get("severity") in {"major", "fatal", "unresolved"} and not str(item.get("closure_test") or "").strip():
            findings.append(
                finding(
                    "blocking_concern_without_closure_test",
                    "error",
                    "Major/fatal/unresolved hostile concern requires a concrete closure test",
                    f"hostile_panel[{index}]",
                )
            )

    nearest = novelty.get("nearest_external_works") or []
    if len(nearest) < 3:
        findings.append(
            finding(
                "nearest_neighbour_set_thin",
                "review",
                "Fewer than three named nearest external works are recorded; verify that positioning is not category-only",
                "novelty.nearest_external_works",
            )
        )

    raw_rows = mass.get("raw_rows_or_cases")
    independent_n = mass.get("independent_unit_count")
    if isinstance(raw_rows, int) and isinstance(independent_n, (int, float)) and independent_n > 0 and raw_rows >= 10 * independent_n:
        findings.append(
            finding(
                "raw_count_far_exceeds_effective_n",
                "review",
                f"Raw case count ({raw_rows}) is at least 10x the declared independent-unit count ({independent_n:g}); headline precision and prose must use the scientific unit",
                "scientific_mass",
            )
        )

    if comparisons.get("interface_parity") == "mismatched":
        findings.append(
            finding(
                "comparator_interface_mismatch",
                "review",
                "At least one comparator cannot express the scored terminal/action; capability interpretation must be narrowed to interface attainability unless repaired",
                "comparisons.interface_parity",
            )
        )

    if comparisons.get("designer_advantage") == "high":
        findings.append(
            finding(
                "high_designer_advantage",
                "review",
                "System/benchmark/gold share substantial designer assumptions; treat same-programme success as conformance until external or independently governed evidence closes the gap",
                "comparisons.designer_advantage",
            )
        )

    if comparisons.get("scorer_latitude") == "high":
        findings.append(
            finding(
                "high_scorer_latitude",
                "review",
                "Outcome scoring has high interpretive latitude; prospective success claims require a tighter scorer or adjudication-stability evidence",
                "comparisons.scorer_latitude",
            )
        )

    if ext.get("claim_scope_matches_level") is False:
        findings.append(
            finding(
                "external_validity_scope_mismatch",
                "error",
                "Claim scope exceeds the strongest executed external-validity level",
                "external_validity.claim_scope_matches_level",
            )
        )

    if integrity.get("integrity_substituted_for_validity") is True:
        findings.append(
            finding(
                "integrity_substituted_for_validity",
                "error",
                "Reproducibility/provenance evidence is being used as a substitute for missing scientific-validity evidence",
                "integrity_vs_validity.integrity_substituted_for_validity",
            )
        )

    if siblings.get("reader_visible_separation") == "weak" and disposition == "WRITE_FULL_PAPER":
        findings.append(
            finding(
                "weak_sibling_separation_full_paper",
                "error",
                "Standalone paper is declared despite weak reader-visible separation from sibling work; run/resolve the merge test",
                "sibling_overlap.reader_visible_separation",
            )
        )

    claim_status = claim.get("status")
    if disposition == "WRITE_FULL_PAPER":
        if claim_status in {"unsupported", "withdrawn", "unresolved"}:
            findings.append(
                finding(
                    "full_paper_without_surviving_claim",
                    "error",
                    f"WRITE_FULL_PAPER is incompatible with surviving claim status {claim_status}",
                    "surviving_claim.status",
                )
            )
        if fatal_rows:
            findings.append(
                finding(
                    "full_paper_with_fatal_hostile_objection",
                    "error",
                    "WRITE_FULL_PAPER cannot coexist with a fatal hostile objection",
                    "hostile_panel",
                )
            )
        if unresolved_rows:
            findings.append(
                finding(
                    "full_paper_with_unresolved_hostile_objection",
                    "unresolved",
                    "WRITE_FULL_PAPER cannot be released while an independent hostile lens is unresolved",
                    "hostile_panel",
                )
            )
        if next_disc.get("blocks_further_polish") is True:
            findings.append(
                finding(
                    "full_paper_while_evidence_gate_blocks_polish",
                    "error",
                    "Evidence-acquisition stop rule blocks further manuscript polishing, so WRITE_FULL_PAPER is inconsistent",
                    "next_discriminator.blocks_further_polish",
                )
            )

    if disposition == "WAIT_FOR_EVIDENCE" and next_disc.get("blocks_further_polish") is not True:
        findings.append(
            finding(
                "wait_without_polish_block",
                "error",
                "WAIT_FOR_EVIDENCE must block prose optimization that cannot change the scientific decision",
                "next_discriminator.blocks_further_polish",
            )
        )

    if disposition == "MERGE_WITH_SIBLING" and not (siblings.get("siblings") or []):
        findings.append(
            finding(
                "merge_without_sibling",
                "error",
                "MERGE_WITH_SIBLING requires at least one named sibling candidate",
                "sibling_overlap.siblings",
            )
        )

    if decision.get("top_tier_status") == "candidate" and disposition != "WRITE_FULL_PAPER":
        findings.append(
            finding(
                "top_tier_candidate_without_full_paper",
                "error",
                "Top-tier candidate status is only valid after WRITE_FULL_PAPER",
                "decision.top_tier_status",
            )
        )

    if decision.get("top_tier_status") == "candidate" and (major_rows or fatal_rows or unresolved_rows):
        findings.append(
            finding(
                "top_tier_candidate_with_open_major_concerns",
                "review",
                "Top-tier candidate still carries major/fatal/unresolved hostile concerns; candidate label should be treated as provisional until they close",
                "decision.top_tier_status",
            )
        )

    if not str(next_disc.get("closure_test") or "").strip():
        findings.append(
            finding(
                "next_discriminator_without_closure_test",
                "error",
                "Next discriminator must state an observable closure test",
                "next_discriminator.closure_test",
            )
        )

    return summarize(findings, ledger)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path)
    parser.add_argument("--json", action="store_true", dest="emit_json")
    args = parser.parse_args()

    try:
        ledger = json.loads(args.ledger.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - CLI guard
        print(f"BLOCKED: cannot read ledger: {exc}", file=sys.stderr)
        return 2

    result = validate(ledger)
    if args.emit_json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"PAPER EXISTENCE GATE: {result['verdict']}")
        print(f"paper={result.get('paper_id')} disposition={result.get('disposition')}")
        for item in result["findings"]:
            pointer = f" [{item['pointer']}]" if item.get("pointer") else ""
            print(f"- {item['severity'].upper()} {item['code']}{pointer}: {item['message']}")

    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
