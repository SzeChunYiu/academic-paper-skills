#!/usr/bin/env python3
"""Validate fine-grained scientific rhetorical-act / result-state records.

This verifier checks semantic compatibility between evidence state and manuscript
claiming. It is intentionally conservative: it does not decide whether the
underlying statistical analysis is correct. That remains the responsibility of
the statistical-inference layer and expert review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.0.0"
RELEASE_DECISIONS = {"PASS", "REVIEW", "BLOCKED"}

COMPATIBLE_CLAIMS: dict[str, set[str]] = {
    "descriptive": {"descriptive_only"},
    "directional_supported": {"directional_effect"},
    "superiority_supported": {"superiority", "directional_effect"},
    "ordinary_non_significant": {"no_clear_difference"},
    "inconclusive": {"inconclusive"},
    "evidence_of_absence": {"bounded_absence"},
    "equivalence_supported": {"equivalence"},
    "noninferiority_supported": {"noninferiority"},
    "harm_supported": {"harm"},
    "failed_prespecified_hypothesis": {"failed_hypothesis"},
    "failed_replication": {"failed_replication", "inconclusive"},
    "contradictory_evidence": {"contradiction"},
    "heterogeneity_supported": {"heterogeneity"},
    "robustness_supported": {"robustness"},
    "sensitivity_changes_claim": {"assumption_dependent"},
    "positive_control": {"control_success", "control_failure"},
    "negative_control": {"control_success", "control_failure"},
    "unexpected_observation": {"exploratory_pattern", "descriptive_only"},
    "exploratory_post_hoc": {"exploratory_pattern"},
    "threshold_result": {"threshold_met", "threshold_not_met"},
    "boundary_failure": {"boundary"},
}

ABSENCE_STATES = {"evidence_of_absence", "equivalence_supported", "noninferiority_supported"}
CONTROL_STATES = {"positive_control", "negative_control"}
NULL_OVERCLAIM_PATTERNS = (
    re.compile(r"\bno effect\b", re.I),
    re.compile(r"\bno difference\b", re.I),
    re.compile(r"\bequivalent\b", re.I),
    re.compile(r"\bthe same\b", re.I),
    re.compile(r"\bineffective\b", re.I),
)
TREND_PATTERNS = (
    re.compile(r"trend(?:ed|ing)? toward significance", re.I),
    re.compile(r"approach(?:ed|ing)? significance", re.I),
    re.compile(r"marginally significant", re.I),
)
ALTERNATIVE_PROOF_PATTERNS = (
    re.compile(r"\bproves? (?:the )?alternative\b", re.I),
    re.compile(r"\brules? out\b", re.I),
    re.compile(r"\bdefinitively excludes?\b", re.I),
)


def _finding(code: str, severity: str, message: str, pointer: str | None = None) -> dict[str, Any]:
    return {"code": code, "severity": severity, "message": message, "pointer": pointer}


def _text(value: Any) -> str:
    return str(value or "").strip()


def _nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _nonempty_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(_nonempty_text(x) for x in value)


def _decision(findings: list[dict[str, Any]]) -> str:
    severities = {item["severity"] for item in findings}
    if "error" in severities:
        return "BLOCKED"
    if "review" in severities:
        return "REVIEW"
    return "PASS"


def _wording_blob(act: dict[str, Any]) -> str:
    plan = act.get("wording_plan")
    parts: list[str] = []
    if isinstance(plan, dict):
        parts.extend(_text(plan.get(key)) for key in ("lead_message", "quantitative_anchor", "qualification", "handoff"))
    parts.append(_text(act.get("scientific_consequence")))
    return " ".join(part for part in parts if part)


def validate(record: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []

    if record.get("schema_version") != SCHEMA_VERSION:
        findings.append(_finding("unsupported_schema_version", "error", f"schema_version must be {SCHEMA_VERSION}", "schema_version"))

    for key in ("record_id", "manuscript_scope"):
        if not _nonempty_text(record.get(key)):
            findings.append(_finding("missing_required_text", "error", f"{key} must be non-empty", key))

    acts = record.get("acts")
    if not isinstance(acts, list) or not acts:
        findings.append(_finding("acts_missing", "error", "At least one rhetorical act is required", "acts"))
        acts = []

    seen_act_ids: set[str] = set()
    primary_problem = False
    favorable_secondary = False

    for index, act in enumerate(acts):
        pointer = f"acts[{index}]"
        if not isinstance(act, dict):
            findings.append(_finding("invalid_act", "error", "Act must be an object", pointer))
            continue

        act_id = _text(act.get("act_id"))
        if not act_id:
            findings.append(_finding("act_id_missing", "error", "act_id must be non-empty", f"{pointer}.act_id"))
        elif act_id in seen_act_ids:
            findings.append(_finding("duplicate_act_id", "error", f"Duplicate act_id: {act_id}", f"{pointer}.act_id"))
        else:
            seen_act_ids.add(act_id)

        for key in (
            "result_id",
            "section",
            "rhetorical_act",
            "evidence_state",
            "claimed_state",
            "analysis_role",
            "prespecification",
            "scientific_direction",
            "target",
            "observation",
            "uncertainty",
            "scientific_consequence",
            "reader_job",
            "placement",
            "status",
        ):
            if not _nonempty_text(act.get(key)):
                findings.append(_finding("act_field_missing", "error", f"{key} must be non-empty", f"{pointer}.{key}"))

        if not _nonempty_list(act.get("allowed_inference")):
            findings.append(_finding("allowed_inference_missing", "error", "allowed_inference must contain at least one non-empty item", f"{pointer}.allowed_inference"))
        if not _nonempty_list(act.get("forbidden_inference")):
            findings.append(_finding("forbidden_inference_missing", "error", "forbidden_inference must contain at least one non-empty item", f"{pointer}.forbidden_inference"))

        evidence = _text(act.get("evidence_state"))
        claimed = _text(act.get("claimed_state"))
        if evidence in COMPATIBLE_CLAIMS and claimed not in COMPATIBLE_CLAIMS[evidence]:
            findings.append(
                _finding(
                    "evidence_claim_mismatch",
                    "error",
                    f"Evidence state {evidence!r} cannot directly support claimed_state {claimed!r}; allowed: {sorted(COMPATIBLE_CLAIMS[evidence])}",
                    f"{pointer}.claimed_state",
                )
            )

        absence = act.get("absence_basis")
        if evidence in ABSENCE_STATES:
            if not isinstance(absence, dict):
                findings.append(_finding("absence_basis_missing", "error", f"{evidence} requires an explicit absence/equivalence/non-inferiority basis", f"{pointer}.absence_basis"))
            else:
                for key in ("method", "meaningful_region", "status"):
                    if not _nonempty_text(absence.get(key)):
                        findings.append(_finding("absence_basis_incomplete", "error", f"absence_basis.{key} must be non-empty", f"{pointer}.absence_basis.{key}"))
                if evidence in {"equivalence_supported", "noninferiority_supported"} and not _nonempty_text(absence.get("margin")):
                    findings.append(_finding("margin_missing", "error", f"{evidence} requires an explicit margin", f"{pointer}.absence_basis.margin"))
                if absence.get("status") == "post_hoc_qualified":
                    findings.append(_finding("post_hoc_absence_basis", "review", "Post hoc absence/equivalence boundary requires explicit qualified interpretation", f"{pointer}.absence_basis.status"))

        if evidence == "heterogeneity_supported" and not isinstance(act.get("heterogeneity_basis"), dict):
            findings.append(_finding("heterogeneity_basis_missing", "error", "A heterogeneity claim requires an interaction/heterogeneity comparison basis", f"{pointer}.heterogeneity_basis"))

        if evidence in CONTROL_STATES:
            control = act.get("control_basis")
            if not isinstance(control, dict):
                findings.append(_finding("control_basis_missing", "error", f"{evidence} requires control purpose/expectation/observation fields", f"{pointer}.control_basis"))
            else:
                expected_type = "positive" if evidence == "positive_control" else "negative"
                if control.get("control_type") != expected_type:
                    findings.append(_finding("control_type_mismatch", "error", f"control_type must be {expected_type!r} for {evidence}", f"{pointer}.control_basis.control_type"))

        prespec = _text(act.get("prespecification"))
        role = _text(act.get("analysis_role"))
        if evidence == "failed_prespecified_hypothesis" and prespec != "prespecified":
            findings.append(_finding("failed_hypothesis_not_prespecified", "error", "A failed prespecified-hypothesis state requires prespecification='prespecified'", f"{pointer}.prespecification"))
        if evidence == "exploratory_post_hoc":
            if role != "exploratory":
                findings.append(_finding("exploratory_role_mismatch", "error", "exploratory_post_hoc evidence must remain analysis_role='exploratory'", f"{pointer}.analysis_role"))
            if prespec != "post_hoc":
                findings.append(_finding("post_hoc_status_missing", "error", "exploratory_post_hoc evidence must record prespecification='post_hoc'", f"{pointer}.prespecification"))
            if act.get("placement") == "abstract":
                findings.append(_finding("exploratory_abstract_elevation", "review", "A post hoc exploratory finding is placed in the abstract; verify that its status is unmistakable and scientifically justified", f"{pointer}.placement"))

        blob = _wording_blob(act)
        if evidence == "ordinary_non_significant":
            for pattern in NULL_OVERCLAIM_PATTERNS:
                if pattern.search(blob) and not re.search(r"\bno (?:clear|statistically significant) (?:evidence|effect|difference)\b", blob, re.I):
                    findings.append(_finding("null_as_absence_wording", "error", "Ordinary non-significance is worded as absence/equivalence; use an absence-capable analysis for that claim", f"{pointer}.wording_plan"))
                    break

        for pattern in TREND_PATTERNS:
            if pattern.search(blob):
                findings.append(_finding("trend_toward_significance", "review", "Avoid significance-trend rhetoric; report estimate, uncertainty and scientific compatibility instead", f"{pointer}.wording_plan"))
                break

        if evidence == "failed_prespecified_hypothesis" and not isinstance(absence, dict):
            for pattern in ALTERNATIVE_PROOF_PATTERNS:
                if pattern.search(blob):
                    findings.append(_finding("failed_hypothesis_proves_alternative", "error", "Failure of a prespecified hypothesis does not by itself prove/rule in the strongest alternative or rule out a mechanism", f"{pointer}.wording_plan"))
                    break

        if evidence == "harm_supported" or role == "adverse_harm":
            if act.get("placement") == "omitted" or act.get("status") == "omit":
                findings.append(_finding("harm_omitted", "error", "Supported/prespecified harm evidence cannot be repaired by omission", pointer))

        if role == "primary_confirmatory" and evidence in {
            "ordinary_non_significant",
            "inconclusive",
            "failed_prespecified_hypothesis",
            "boundary_failure",
        }:
            primary_problem = True
        if role == "secondary_confirmatory" and evidence in {
            "directional_supported",
            "superiority_supported",
        }:
            favorable_secondary = True

        plan = act.get("wording_plan")
        if not isinstance(plan, dict):
            findings.append(_finding("wording_plan_missing", "error", "wording_plan must be an object", f"{pointer}.wording_plan"))
        else:
            if not _nonempty_text(plan.get("lead_message")):
                findings.append(_finding("lead_message_missing", "error", "wording_plan.lead_message must be non-empty", f"{pointer}.wording_plan.lead_message"))

    if primary_problem and favorable_secondary:
        findings.append(
            _finding(
                "secondary_rescue_risk",
                "review",
                "A primary confirmatory result is non-supportive/inconclusive while a favorable secondary confirmatory result exists. Check that title/abstract/conclusion do not rhetorically rescue the primary claim with secondary evidence.",
                "acts",
            )
        )

    cross = record.get("cross_surface_consistency")
    if not isinstance(cross, dict):
        findings.append(_finding("cross_surface_missing", "error", "cross_surface_consistency must be an object", "cross_surface_consistency"))
    else:
        if cross.get("checked") is not True:
            findings.append(_finding("cross_surface_not_checked", "review", "Claim-bearing result states have not been checked across abstract/results/displays/discussion/conclusion", "cross_surface_consistency.checked"))
        if cross.get("optimism_drift_detected") is True:
            findings.append(_finding("optimism_drift", "error", "Abstract/title/conclusion is recorded as more favorable or certain than the underlying result state", "cross_surface_consistency.optimism_drift_detected"))
        surfaces = cross.get("surfaces")
        if not isinstance(surfaces, list):
            findings.append(_finding("surfaces_invalid", "error", "cross_surface_consistency.surfaces must be a list", "cross_surface_consistency.surfaces"))

    computed_pre_release = _decision(findings)
    release = record.get("release")
    if not isinstance(release, dict):
        findings.append(_finding("release_missing", "error", "release must be an object", "release"))
    else:
        recorded = release.get("decision")
        if recorded not in RELEASE_DECISIONS:
            findings.append(_finding("invalid_release_decision", "error", f"Unsupported release decision: {recorded}", "release.decision"))
        elif recorded != computed_pre_release:
            findings.append(_finding("stale_release_decision", "error", f"Recorded release decision {recorded} does not match computed decision {computed_pre_release}", "release.decision"))
        notes = release.get("notes")
        if not isinstance(notes, list) or not all(_nonempty_text(x) for x in notes):
            findings.append(_finding("release_notes_invalid", "error", "release.notes must be a list of non-empty strings", "release.notes"))

    computed = _decision(findings)
    counts = Counter(item["severity"] for item in findings)
    return {
        "decision": computed,
        "counts": {"error": counts.get("error", 0), "review": counts.get("review", 0)},
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()

    try:
        record = json.loads(args.record.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"decision": "BLOCKED", "error": str(exc)}, indent=2))
        return 2

    result = validate(record)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
