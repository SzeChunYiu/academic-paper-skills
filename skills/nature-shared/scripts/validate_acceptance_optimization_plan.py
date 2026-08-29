#!/usr/bin/env python3
"""Validate an evidence-graded acceptance optimization plan.

The validator checks decision-readiness semantics, evidence-grade boundaries,
Registered Report routing, public-review-history survivorship safeguards, and
anti-manipulation fields. It does not predict journal acceptance.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import jsonschema


HERE = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = HERE / "acceptance-contracts" / "acceptance-optimization-plan.schema.json"

PROHIBITED_KEYS = {
    "acceptance_probability",
    "acceptance_score",
    "predicted_acceptance",
    "editor_leniency",
    "editor_harshness",
    "reviewer_friendliness",
    "friendly_reviewer_score",
    "friendly_editor_score",
    "citation_targeting",
    "strategic_editor_citations",
    "strategic_reviewer_citations",
    "prestige_score",
    "impact_factor_rank",
    "personality_targeting",
    "political_targeting",
    "religious_targeting",
    "demographic_targeting",
}

TARGET_POLICY_AXES = {
    "scope",
    "contribution_novelty",
    "significance_utility_readership",
    "editorial_routing",
    "cover_letter_submission_metadata",
    "reporting_compliance",
}

READY_STATES = {
    "acceptance_optimized_decision_ready_for_target",
    "decision_ready_but_editorial_outcome_uncertain",
}


def _walk_keys(value: Any, path: str = "$") -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            found.append((str(key), child_path))
            found.extend(_walk_keys(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(_walk_keys(child, f"{path}[{index}]"))
    return found


def _schema_errors(plan: dict[str, Any], schema_path: Path) -> list[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
    )
    return [
        f"{'.'.join(str(p) for p in error.path) or '$'}: {error.message}"
        for error in sorted(validator.iter_errors(plan), key=lambda item: list(item.path))
    ]


def validate_plan(plan: dict[str, Any], schema_path: Path = DEFAULT_SCHEMA) -> list[str]:
    errors = _schema_errors(plan, schema_path)

    for key, path in _walk_keys(plan):
        if key.lower() in PROHIBITED_KEYS:
            errors.append(f"{path}: prohibited acceptance-targeting field")

    target = plan.get("target", {})
    official_policy_urls = set(target.get("official_policy_urls", []) or [])

    rr = plan.get("registered_report")
    route = target.get("route")
    if route in {"registered_report_stage1", "registered_report_stage2"}:
        if not isinstance(rr, dict):
            errors.append("registered_report: required for a Registered Report target route")
        else:
            if rr.get("availability") != "available":
                errors.append("registered_report.availability: Registered Report route requires current availability")
            if rr.get("eligibility") != "eligible":
                errors.append("registered_report.eligibility: Registered Report route requires confirmed eligibility")
            policy_url = rr.get("official_policy_url")
            if not policy_url:
                errors.append("registered_report.official_policy_url: exact current policy source is required")
            elif official_policy_urls and policy_url not in official_policy_urls:
                errors.append(
                    "registered_report.official_policy_url: source must be registered in target.official_policy_urls"
                )

    if plan.get("objective") == "registered_report_stage1" and route != "registered_report_stage1":
        errors.append("target.route: registered_report_stage1 objective requires the Stage 1 route")

    if plan.get("objective") == "successful_publication" and not plan.get("target_ladder"):
        errors.append("target_ladder: successful_publication objective requires a fit-first target ladder")

    public_history = plan.get("public_review_history", {}) or {}
    has_h_lever = False

    seen_lever_ids: set[str] = set()
    for index, lever in enumerate(plan.get("levers", [])):
        lever_id = lever.get("id")
        if lever_id in seen_lever_ids:
            errors.append(f"levers.{index}.id: duplicate lever id {lever_id!r}")
        if lever_id:
            seen_lever_ids.add(lever_id)

        grade = lever.get("evidence_grade")
        sources = lever.get("source_urls", []) or []
        enforcement = lever.get("enforcement")
        axis = lever.get("decision_axis")
        stage = lever.get("stage")

        if grade != "MANUSCRIPT_INTERNAL" and not sources:
            errors.append(
                f"levers.{index}.source_urls: external evidence grade {grade!r} requires at least one source"
            )

        if enforcement == "hard_gate" and grade not in {"D", "MANUSCRIPT_INTERNAL"}:
            errors.append(
                f"levers.{index}.enforcement: hard acceptance gates require exact official policy or manuscript-internal scientific authority"
            )

        if grade == "H":
            has_h_lever = True
            if enforcement == "hard_gate":
                errors.append(
                    f"levers.{index}.evidence_grade: public review-history heuristics cannot become hard gates"
                )

        if grade in {"C", "E", "H"} and enforcement == "hard_gate":
            errors.append(
                f"levers.{index}.enforcement: observational/editorial/history evidence cannot be a hard acceptance gate"
            )

        if grade == "D" and (axis in TARGET_POLICY_AXES or stage in {"target_fit", "submission_package"}):
            if not official_policy_urls:
                errors.append(
                    f"levers.{index}: target-specific official-policy lever requires target.official_policy_urls"
                )
            elif not (set(sources) & official_policy_urls):
                errors.append(
                    f"levers.{index}.source_urls: target-specific Grade D lever must cite a registered exact target policy source"
                )

    if has_h_lever:
        if not public_history.get("used"):
            errors.append("public_review_history.used: Grade H lever requires an explicit public-history calibration record")
        if not public_history.get("survivorship_warning_recorded"):
            errors.append(
                "public_review_history.survivorship_warning_recorded: accepted/public histories require an explicit survivorship warning"
            )
        if int(public_history.get("accepted_case_count", 0) or 0) < 1:
            errors.append("public_review_history.accepted_case_count: Grade H use requires at least one annotated public case")
        if int(public_history.get("rejected_or_rejection_evidence_count", 0) or 0) < 1:
            errors.append(
                "public_review_history.rejected_or_rejection_evidence_count: pair accepted-case learning with rejection evidence"
            )

    seen_blocker_ids: set[str] = set()
    blockers = plan.get("blockers", [])
    for index, blocker in enumerate(blockers):
        blocker_id = blocker.get("id")
        if blocker_id in seen_blocker_ids:
            errors.append(f"blockers.{index}.id: duplicate blocker id {blocker_id!r}")
        if blocker_id:
            seen_blocker_ids.add(blocker_id)

    release_state = plan.get("release_state")
    if release_state in READY_STATES:
        if target.get("policy_state") != "resolved_current":
            errors.append("target.policy_state: decision-ready states require resolved current target policy")
        if route == "unknown":
            errors.append("target.route: decision-ready states cannot use an unknown publication route")

        for index, lever in enumerate(plan.get("levers", [])):
            if lever.get("enforcement") == "hard_gate" and lever.get("status") != "satisfied":
                errors.append(
                    f"levers.{index}.status: every hard gate must be satisfied before a decision-ready release state"
                )

        for index, blocker in enumerate(blockers):
            if blocker.get("class") == "uncontrollable_editorial_context":
                continue
            if blocker.get("status") in {"open", "uncertain"}:
                errors.append(
                    f"blockers.{index}.status: repairable blockers must be closed before a decision-ready release state"
                )

    if release_state == "decision_ready_but_editorial_outcome_uncertain":
        contextual = [
            item for item in plan.get("uncontrollable_context", [])
            if item.get("state") in {"unknown", "known_contextual_risk"}
        ]
        if not contextual:
            errors.append(
                "uncontrollable_context: editorial-outcome-uncertain release state requires at least one explicit uncontrollable-context item"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args()

    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    errors = validate_plan(plan, args.schema)
    if errors:
        print("Acceptance optimization plan validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Acceptance optimization plan validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
