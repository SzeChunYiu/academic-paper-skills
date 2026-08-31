#!/usr/bin/env python3
"""Validate a scientific figure representation decision record.

The verifier checks whether a claim-bearing display has a real reader task,
compares plausible representations when no representation is mandated, records
information loss and inference boundaries, and completes clean-reader/final-size
closure before final release. It does not score aesthetics or claim that a chart
is globally optimal.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


REQUIRED_TOP = (
    "schema_version",
    "display_id",
    "stage",
    "reader_question",
    "reader_state_transition",
    "claim_ids",
    "scientific_object",
    "statistical_unit",
    "dependence_structure",
    "alternative_explanation",
    "representation_mandate",
    "candidates",
    "chosen_representation",
    "chosen_reason",
    "information_loss",
    "uncertainty_encoding",
    "exact_value_companion",
    "placement",
    "inference_boundary",
    "clean_reader_status",
    "final_size_status",
    "release",
)
FINAL_STAGES = {"final", "production"}
VALID_STAGES = {"planning", "draft", "review", "final", "production"}
VALID_DECISIONS = {"chosen", "rejected", "retained_alternative"}


def finding(code: str, severity: str, message: str, pointer: str | None = None) -> dict[str, Any]:
    return {"code": code, "severity": severity, "message": message, "pointer": pointer}


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(record: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []

    for key in REQUIRED_TOP:
        if key not in record:
            findings.append(finding("missing_top_level", "error", f"Missing required field: {key}", key))

    if findings:
        return summarize(findings, record)

    if record.get("schema_version") != "1.0.0":
        findings.append(finding("unsupported_schema_version", "error", "schema_version must be 1.0.0", "schema_version"))

    stage = record.get("stage")
    if stage not in VALID_STAGES:
        findings.append(finding("invalid_stage", "error", f"Unsupported stage: {stage}", "stage"))

    for key in (
        "display_id",
        "reader_question",
        "scientific_object",
        "statistical_unit",
        "dependence_structure",
        "alternative_explanation",
        "chosen_representation",
        "chosen_reason",
        "uncertainty_encoding",
        "exact_value_companion",
        "inference_boundary",
    ):
        if not _nonempty(record.get(key)):
            findings.append(finding("empty_required_text", "error", f"{key} must be non-empty", key))

    state = record.get("reader_state_transition") or {}
    for key in ("before", "after", "remaining_uncertainty"):
        if not _nonempty(state.get(key)):
            findings.append(finding("reader_state_incomplete", "error", f"reader_state_transition.{key} must be non-empty", f"reader_state_transition.{key}"))

    claims = record.get("claim_ids") or []
    if not claims:
        findings.append(finding("claim_link_missing", "error", "Claim-bearing display requires at least one claim_id", "claim_ids"))
    elif len(set(claims)) != len(claims):
        findings.append(finding("duplicate_claim_id", "error", "claim_ids must be unique", "claim_ids"))

    mandate = record.get("representation_mandate") or {}
    mandate_status = mandate.get("status")
    mandate_reason = str(mandate.get("reason") or "").strip()
    if mandate_status not in {"not_mandated", "mandated"}:
        findings.append(finding("invalid_mandate_status", "error", f"Unsupported representation_mandate.status: {mandate_status}", "representation_mandate.status"))
    if mandate_status == "mandated" and not mandate_reason:
        findings.append(finding("mandate_reason_missing", "error", "Mandated representation requires an explicit scientific/reporting/venue reason", "representation_mandate.reason"))

    candidates = record.get("candidates") or []
    if not candidates:
        findings.append(finding("candidate_missing", "error", "At least one candidate representation is required", "candidates"))
    if mandate_status == "not_mandated" and len(candidates) < 2:
        findings.append(
            finding(
                "counterfactual_representation_missing",
                "error",
                "Non-mandated claim-bearing display must compare at least two plausible representation candidates",
                "candidates",
            )
        )

    chosen_family = str(record.get("chosen_representation") or "").strip()
    chosen_count = 0
    families: set[str] = set()
    required_candidate_fields = (
        "family",
        "reader_task_fit",
        "information_preserved",
        "information_hidden",
        "perceptual_task",
        "dependence_visibility",
        "uncertainty_visibility",
        "heterogeneity_failure_visibility",
        "exact_value_recovery",
        "transformations",
        "inference_risks",
        "space_attention_cost",
        "accessibility_risks",
        "decision",
        "rationale",
    )

    for index, candidate in enumerate(candidates):
        ptr = f"candidates[{index}]"
        for key in required_candidate_fields:
            if key not in candidate:
                findings.append(finding("candidate_field_missing", "error", f"Candidate missing {key}", f"{ptr}.{key}"))

        family = str(candidate.get("family") or "").strip()
        if not family:
            findings.append(finding("candidate_family_missing", "error", "Candidate family must be non-empty", f"{ptr}.family"))
        elif family in families:
            findings.append(finding("duplicate_candidate_family", "error", f"Duplicate candidate family: {family}", f"{ptr}.family"))
        else:
            families.add(family)

        for key in (
            "reader_task_fit",
            "perceptual_task",
            "dependence_visibility",
            "uncertainty_visibility",
            "heterogeneity_failure_visibility",
            "exact_value_recovery",
            "space_attention_cost",
            "rationale",
        ):
            if key in candidate and not _nonempty(candidate.get(key)):
                findings.append(finding("candidate_text_empty", "error", f"Candidate {key} must be non-empty", f"{ptr}.{key}"))

        for key in ("information_preserved", "information_hidden", "inference_risks", "accessibility_risks"):
            value = candidate.get(key)
            if key in candidate and (not isinstance(value, list) or len(value) == 0):
                findings.append(finding("candidate_audit_empty", "error", f"Candidate {key} must contain at least one audit entry", f"{ptr}.{key}"))

        decision = candidate.get("decision")
        if decision not in VALID_DECISIONS:
            findings.append(finding("invalid_candidate_decision", "error", f"Unsupported candidate decision: {decision}", f"{ptr}.decision"))
        if decision == "chosen":
            chosen_count += 1
            if family != chosen_family:
                findings.append(
                    finding(
                        "chosen_family_mismatch",
                        "error",
                        f"Candidate marked chosen ({family}) does not match chosen_representation ({chosen_family})",
                        ptr,
                    )
                )

    if chosen_count != 1:
        findings.append(finding("chosen_candidate_count", "error", f"Exactly one candidate must be marked chosen; found {chosen_count}", "candidates"))
    if chosen_family and chosen_family not in families:
        findings.append(finding("chosen_representation_not_candidate", "error", "chosen_representation must appear in candidate families", "chosen_representation"))

    info_loss = record.get("information_loss")
    if not isinstance(info_loss, list) or not info_loss:
        findings.append(finding("information_loss_missing", "error", "Chosen representation requires an explicit information-loss audit", "information_loss"))

    placement = record.get("placement")
    if placement not in {"main", "support", "methods", "repository", "omit"}:
        findings.append(finding("invalid_placement", "error", f"Unsupported placement: {placement}", "placement"))

    clean = record.get("clean_reader_status")
    final_size = record.get("final_size_status")
    valid_statuses = {"pass", "pending", "limited", "not_applicable"}
    if clean not in valid_statuses:
        findings.append(finding("invalid_clean_reader_status", "error", f"Unsupported clean_reader_status: {clean}", "clean_reader_status"))
    if final_size not in valid_statuses:
        findings.append(finding("invalid_final_size_status", "error", f"Unsupported final_size_status: {final_size}", "final_size_status"))

    if stage in FINAL_STAGES:
        if clean != "pass":
            findings.append(finding("clean_reader_closure_incomplete", "unresolved", "Final claim-bearing display requires clean-reader figure+caption pass", "clean_reader_status"))
        if final_size != "pass":
            findings.append(finding("final_size_closure_incomplete", "unresolved", "Final claim-bearing display requires final-size accessibility/legibility pass", "final_size_status"))

    if placement == "main" and stage in FINAL_STAGES and state.get("before") == state.get("after"):
        findings.append(
            finding(
                "no_reader_state_transition",
                "review",
                "Main figure does not record a changed reader state; verify that it earns main-text space rather than duplicating existing evidence",
                "reader_state_transition",
            )
        )

    computed = decision(findings)
    recorded = (record.get("release") or {}).get("decision")
    if recorded and recorded != computed:
        findings.append(
            finding(
                "stale_release_decision",
                "error",
                f"Recorded release decision {recorded} does not match computed decision {computed}",
                "release.decision",
            )
        )
        computed = decision(findings)

    return summarize(findings, record, forced_decision=computed)


def decision(findings: list[dict[str, Any]]) -> str:
    severities = {item["severity"] for item in findings}
    if "error" in severities:
        return "BLOCKED"
    if "unresolved" in severities:
        return "UNRESOLVED"
    if "review" in severities:
        return "REVIEW"
    return "PASS"


def summarize(
    findings: list[dict[str, Any]], record: dict[str, Any], forced_decision: str | None = None
) -> dict[str, Any]:
    counts = Counter(item["severity"] for item in findings)
    return {
        "decision": forced_decision or decision(findings),
        "counts": {
            "error": counts["error"],
            "unresolved": counts["unresolved"],
            "review": counts["review"],
        },
        "display_id": record.get("display_id"),
        "stage": record.get("stage"),
        "chosen_representation": record.get("chosen_representation"),
        "findings": findings,
        "notes": [
            "A representation tournament compares plausible alternatives; publication frequency is not a quality score.",
            "The verifier checks decision completeness and closure, not whether a chart is globally optimal.",
            "Final scientific judgment still requires the actual data, claim, audience, target, and final-size visual inspection.",
        ],
    }


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Validate a scientific figure representation decision record.")
    p.add_argument("record", type=Path)
    p.add_argument("--pretty", action="store_true")
    p.add_argument("--report", type=Path)
    return p


def main() -> int:
    args = parser().parse_args()
    try:
        record = json.loads(args.record.read_text(encoding="utf-8"))
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
