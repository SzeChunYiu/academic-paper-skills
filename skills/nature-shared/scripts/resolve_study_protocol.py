#!/usr/bin/env python3
"""Resolve and evaluate study protocol/conduct decision contracts.

The evaluator checks bounded, machine-verifiable traceability and contradiction
rules. It does not certify scientific validity, absence of bias, reporting-
guideline completion, or journal acceptance.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import jsonschema


HERE = Path(__file__).resolve().parents[1]
DEFAULT_ADAPTERS = HERE / "study-contracts" / "maintained-study-adapters.json"
DEFAULT_SCHEMA = (
    HERE / "study-contracts" / "study-protocol-conduct-contract.schema.json"
)


def load_adapter_catalog(path: str | Path = DEFAULT_ADAPTERS) -> dict[str, Any]:
    catalog_path = Path(path)
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    registry_file = catalog.get("evidence_registry_file")
    if registry_file:
        registry = json.loads(
            (catalog_path.parent / registry_file).read_text(encoding="utf-8")
        )
        catalog["evidence_registry"] = registry
        catalog["sources"] = registry.get("sources", [])
    errors = validate_adapter_catalog(catalog)
    if errors:
        raise ValueError("invalid study adapter catalog: " + "; ".join(errors))
    return catalog


def validate_adapter_catalog(catalog: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "catalog_schema_version",
        "catalog_id",
        "reviewed_at",
        "selection_mode",
        "scope",
        "profiles",
    }
    missing = sorted(required - catalog.keys())
    if missing:
        return ["missing catalog fields: " + ", ".join(missing)]
    if catalog.get("selection_mode") != "applicable_obligations_not_universal_design":
        errors.append(
            "selection_mode must be applicable_obligations_not_universal_design"
        )

    if not catalog.get("evidence_registry_file") and not catalog.get("sources"):
        errors.append("evidence_registry_file or embedded sources is required")
    registry = catalog.get("evidence_registry", {})
    if catalog.get("evidence_registry_file"):
        for field in (
            "registry_schema_version",
            "registry_id",
            "reviewed_at",
            "search_protocol",
            "sources",
            "generalization_rule",
            "update_policy",
        ):
            if not registry.get(field):
                errors.append(f"evidence_registry.{field} is required")

    sources = catalog.get("sources", [])
    source_ids = {source.get("source_id") for source in sources}
    if None in source_ids or not source_ids:
        errors.append("every source requires source_id")
    for index, source in enumerate(sources):
        for field in (
            "source_id",
            "title",
            "url",
            "source_type",
            "read_depth",
            "accessed_at",
            "metadata_verification",
            "supports",
            "limits",
        ):
            if not source.get(field):
                errors.append(f"sources[{index}].{field} is required")
        if source.get("read_depth") not in {"full_text", "abstract", "official_standard"}:
            errors.append(f"sources[{index}].read_depth is invalid")

    seen: set[str] = set()
    for index, profile in enumerate(catalog.get("profiles", [])):
        adapter_id = profile.get("adapter_id")
        if not adapter_id:
            errors.append(f"profiles[{index}].adapter_id is required")
        elif adapter_id in seen:
            errors.append(f"duplicate adapter_id {adapter_id}")
        else:
            seen.add(adapter_id)
        if profile.get("profile_is_not_universal_rule") is not True:
            errors.append(f"{adapter_id}: profile_is_not_universal_rule must be true")
        for field in (
            "applies_when",
            "obligations",
            "hard_checks",
            "source_refs",
            "transfer_limits",
        ):
            if field not in profile:
                errors.append(f"{adapter_id}: {field} is required")
        if len(profile.get("source_refs", [])) < 2:
            errors.append(f"{adapter_id}: at least two source_refs are required")
        for source_ref in profile.get("source_refs", []):
            if source_ref not in source_ids:
                errors.append(f"{adapter_id}: unknown source_ref {source_ref}")
    return errors


def validate_contract_shape(
    contract: dict[str, Any], schema_path: str | Path = DEFAULT_SCHEMA
) -> list[str]:
    schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    errors: list[str] = []
    for error in sorted(validator.iter_errors(contract), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "$"
        errors.append(f"{location}: {error.message}")
    return errors


def _matches(
    profile: dict[str, Any], study_archetype: str, design_tags: set[str]
) -> bool:
    applies = profile["applies_when"]
    archetypes = set(applies.get("study_archetypes", []))
    tags = set(applies.get("any_design_tags", []))
    return (study_archetype in archetypes) or bool(design_tags & tags)


def _unique(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(values))


def resolve_study_adapter(
    *,
    study_archetype: str,
    design_tags: Iterable[str],
    adapters: dict[str, Any],
) -> dict[str, Any]:
    """Return applicable obligations, never a universal best study design."""

    tags = set(design_tags) if isinstance(design_tags, (list, tuple, set)) else set()
    study_archetype = study_archetype if isinstance(study_archetype, str) else "unknown"
    matched = [
        profile
        for profile in adapters["profiles"]
        if _matches(profile, study_archetype, tags)
    ]
    return {
        "selection_mode": "applicable_obligations_not_universal_design",
        "matched_adapter_ids": [profile["adapter_id"] for profile in matched],
        "obligations": _unique(
            item for profile in matched for item in profile["obligations"]
        ),
        "hard_checks": _unique(
            item for profile in matched for item in profile["hard_checks"]
        ),
        "source_refs": _unique(
            item for profile in matched for item in profile["source_refs"]
        ),
        "transfer_limits": _unique(
            item for profile in matched for item in profile["transfer_limits"]
        ),
        "unresolved": []
        if matched
        else [
            "No maintained study adapter matches this archetype/design. Research the domain-specific protocol and conduct obligations rather than forcing a generic checklist."
        ],
    }


def _timestamp(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed if parsed.tzinfo is not None else None
    except (TypeError, ValueError):
        return None


def evaluate_study_contract(
    contract: dict[str, Any], adapters: dict[str, Any]
) -> dict[str, Any]:
    """Evaluate bounded protocol, execution, deviation, and claim invariants."""

    blockers: list[dict[str, str]] = []
    warnings: list[str] = [
        "Registration, reporting-checklist completion, and schema validity do not certify scientific validity or journal acceptance."
    ]

    def block(code: str, message: str, route: str) -> None:
        if code not in {item["code"] for item in blockers}:
            blockers.append({"code": code, "message": message, "route": route})

    schema_errors = validate_contract_shape(contract)
    if schema_errors:
        block(
            "schema_validation_error",
            "The study contract is structurally incomplete or invalid: "
            + "; ".join(schema_errors),
            "Complete fields from authoritative study records; preserve unknown rather than inventing a protocol, approval, receipt, date, outcome, or deviation.",
        )

    resolved = resolve_study_adapter(
        study_archetype=contract.get("study_archetype", "unknown"),
        design_tags=contract.get("design_tags", []),
        adapters=adapters,
    )
    if schema_errors:
        return {
            "status": "blocked",
            "selection_mode": resolved["selection_mode"],
            "matched_adapter_ids": resolved["matched_adapter_ids"],
            "obligations": resolved["obligations"],
            "source_refs": resolved["source_refs"],
            "transfer_limits": resolved["transfer_limits"],
            "unresolved": resolved["unresolved"],
            "schema_errors": schema_errors,
            "blockers": blockers,
            "blocker_codes": [item["code"] for item in blockers],
            "repair_routes": [
                {"code": item["code"], "route": item["route"]}
                for item in blockers
            ],
            "visible_deviation_classes": [],
            "warnings": warnings,
            "certification": {
                "schema_valid": False,
                "protocol_traceability_check": "blocked",
                "scope": "bounded_automatic_checks_only",
                "does_not_certify": [
                    "scientific_truth",
                    "absence_of_bias",
                    "reporting_guideline_completion",
                    "journal_acceptance",
                ],
            },
        }
    hard_checks = set(resolved["hard_checks"])
    protocol = contract.get("protocol", {})
    timing = contract.get("data_timing", {})
    plan = contract.get("analysis_plan", {})
    conduct = contract.get("conduct", {})
    execution = contract.get("analysis_execution", {})
    deviations = contract.get("deviations", [])
    claims = contract.get("claims", [])
    deviation_classes = {
        item.get("classification")
        for item in deviations
        if item.get("status") in {"disclosed", "resolved", "cannot_repair"}
    }

    protocol_frozen = _timestamp(protocol.get("frozen_at"))
    plan_frozen = _timestamp(plan.get("frozen_at"))
    first_data = _timestamp(timing.get("first_data_access_at"))
    first_outcome = _timestamp(timing.get("outcomes_first_observed_at"))
    relation = timing.get("protocol_freeze_relation")
    if relation == "before_data_access" and first_data and (
        not protocol_frozen or protocol_frozen >= first_data
    ):
        block(
            "false_prospective_status",
            "The contract says the protocol was frozen before data access, but its timestamp does not precede first data access.",
            "Reconcile timestamps from immutable records and reclassify affected analyses/claims; never backdate the protocol.",
        )
    if relation in {"before_data_access", "after_data_before_outcome_access"} and first_outcome:
        latest_freeze = max(
            value for value in (protocol_frozen, plan_frozen) if value is not None
        ) if protocol_frozen or plan_frozen else None
        if latest_freeze and latest_freeze >= first_outcome:
            block(
                "false_prospective_status",
                "A supposedly outcome-blind protocol or analysis plan was frozen after outcome access.",
                "Reconcile timing and reclassify the affected work as post hoc/exploratory; do not backdate records.",
            )

    registration = protocol.get("registration", {})
    if registration.get("applicability") == "required":
        registered = _timestamp(registration.get("registered_at"))
        enrollment = _timestamp(registration.get("enrollment_started_at"))
        if (
            registration.get("status") not in {"public", "embargoed"}
            or not registration.get("identifier")
            or (registered and enrollment and registered >= enrollment)
        ):
            block(
                "required_registration_missing_or_late",
                "Registration is marked required but is missing, unidentifiable, or not prospective to enrollment.",
                "Verify the governing requirement and registry record; disclose late/missing registration and its consequence. A new prospective study may be needed for a prospective claim.",
            )

    protocol_primary = {
        item.get("outcome_id") for item in protocol.get("primary_outcomes", [])
    }
    plan_primary = set(plan.get("primary_outcome_ids", []))
    reported_primary = set(execution.get("reported_primary_outcome_ids", []))
    if "primary_outcome_alignment" in hard_checks and (
        protocol_primary != plan_primary or protocol_primary != reported_primary
    ) and "outcome_change" not in deviation_classes:
        block(
            "undisclosed_primary_outcome_change",
            "Protocol, analysis plan, and reported primary outcomes do not agree and no disclosed outcome-change deviation reconciles them.",
            "Restore the prespecified outcome or add a dated deviation with reason, affected claims, inference consequence, and manuscript disclosure; reclassify or narrow the claim rather than retroactively renaming the outcome.",
        )

    assignment = conduct.get("assignment", {})
    if "randomization_execution" in hard_checks and assignment.get("required"):
        if (
            not assignment.get("sequence_receipt")
            or not assignment.get("execution_verified")
            or not assignment.get("concealment_executed")
        ):
            block(
                "randomization_execution_unverified",
                "Randomized assignment is required but the executed sequence/concealment is not verified by a conduct receipt.",
                "Locate and bind the actual assignment/concealment record, disclose execution as unknown or not performed, and narrow causal language when the design no longer licenses it; never infer execution from Methods prose.",
            )

    blinding = conduct.get("blinding", {})
    planned_roles = set(blinding.get("planned_roles", []))
    executed_roles = set(blinding.get("executed_roles", []))
    if "blinding_execution" in hard_checks and planned_roles != executed_roles and (
        "blinding_change" not in deviation_classes
    ):
        block(
            "undisclosed_blinding_deviation",
            "Planned and executed blinding roles differ without a disclosed deviation.",
            "Record which roles were actually blinded, why the plan changed, which outcomes are vulnerable, and any sensitivity or claim-boundary consequence.",
        )

    stopping = conduct.get("stopping", {})
    if "stopping_and_exclusions" in hard_checks and (
        stopping.get("rule_changed")
        or stopping.get("realized", 0) > stopping.get("planned_maximum", 0)
    ) and "stopping_change" not in deviation_classes:
        block(
            "stopping_rule_deviation_undisclosed",
            "The realized stopping/sample-size path differs from the recorded plan without a disclosed deviation.",
            "Version and disclose the stopping change, preserve its timing and reason, evaluate inferential consequences, and reclassify or narrow affected claims; do not rewrite the original plan.",
        )

    enrollment = conduct.get("enrollment", {})
    exclusion_records = enrollment.get("exclusions", [])
    pre_assignment_stages = {
        "screening",
        "eligibility",
        "pre_assignment",
        "pre_randomization",
        "enrollment",
    }
    pre_assignment_exclusions = sum(
        item.get("stage") in pre_assignment_stages for item in exclusion_records
    )
    post_assignment_exclusions = len(exclusion_records) - pre_assignment_exclusions
    entered = enrollment.get("entered", 0)
    assigned = enrollment.get("assigned", 0)
    analyzed = enrollment.get("analyzed", 0)
    if "stopping_and_exclusions" in hard_checks and (
        entered - assigned != pre_assignment_exclusions
        or assigned - analyzed != post_assignment_exclusions
        or execution.get("sample_size_analyzed") != analyzed
    ):
        block(
            "exclusion_lineage_incomplete",
            "Assigned, excluded, and analyzed counts do not reconcile with the unit-level exclusion log and analysis receipt.",
            "Reconcile counts from source records, restore omitted units or exclusions, and disclose all analysis-population changes without deleting null or adverse observations.",
        )

    adverse = conduct.get("adverse_events", {})
    if (
        "adverse_event_reconciliation" in hard_checks
        and adverse.get("applicability") == "required"
        and adverse.get("observed_count") != adverse.get("reported_count")
    ):
        block(
            "adverse_event_omission",
            "Observed and reported adverse-event counts differ.",
            "Reconcile the harms receipt and restore all required adverse-event reporting; do not repair a safety omission by narrowing only the efficacy claim.",
        )

    data_split = plan.get("data_split", {})
    if "evaluation_leakage" in hard_checks and data_split.get("applicability") == "required":
        if data_split.get("overlap_detected") or data_split.get(
            "preprocessing_fit_scope"
        ) in {"all_data", "unknown"}:
            block(
                "evaluation_leakage",
                "The held-out evaluation is contaminated by unit overlap or preprocessing fit outside training data.",
                "Rebuild the split at the true scientific unit, fit preprocessing/model selection within training or nested folds, rerun evaluation on uncontaminated data, or narrow the claim to an explicitly non-held-out diagnostic.",
            )

    confirmatory = any(
        claim.get("evidential_status") == "confirmatory" for claim in claims
    )
    outcome_blind_timing_verified = (
        relation == "after_data_before_outcome_access"
        and first_outcome is not None
        and protocol_frozen is not None
        and plan_frozen is not None
        and max(protocol_frozen, plan_frozen) < first_outcome
    )
    if confirmatory and not (
        relation == "before_data_access" or outcome_blind_timing_verified
    ):
        block(
            "confirmatory_label_not_supported",
            "At least one claim is labeled confirmatory without verified protocol and analysis-plan timing before data or outcome access.",
            "Verify the freeze and access timestamps from authoritative records; otherwise reclassify the analysis as exploratory/post hoc, narrow the claim to what the record supports, or conduct a new prospective study; never backdate or fabricate prespecification.",
        )

    ethics = contract.get("ethics_governance", {})
    if "ethics_authority" in hard_checks and ethics.get("required") and (
        ethics.get("status") not in {"approved", "waived"}
        or not ethics.get("approval_or_waiver_ids")
    ):
        block(
            "required_ethics_authority_missing",
            "Required ethics approval or waiver is missing or unverified.",
            "Verify the competent authority record before proceeding; if authority did not exist, stop unauthorized use and document the non-repairable limitation. Prose cannot create retrospective approval.",
        )

    raw_hash = conduct.get("raw_data_snapshot", {}).get("sha256")
    if raw_hash and execution.get("input_data_sha256") != raw_hash:
        block(
            "analysis_input_snapshot_mismatch",
            "The analysis execution is not bound to the declared raw-data snapshot.",
            "Rerun or bind the analysis to the authoritative snapshot and version all changed results and claims; do not relabel an unrelated receipt.",
        )

    return {
        "status": "blocked" if blockers else "pass",
        "selection_mode": resolved["selection_mode"],
        "matched_adapter_ids": resolved["matched_adapter_ids"],
        "obligations": resolved["obligations"],
        "source_refs": resolved["source_refs"],
        "transfer_limits": resolved["transfer_limits"],
        "unresolved": resolved["unresolved"],
        "schema_errors": schema_errors,
        "blockers": blockers,
        "blocker_codes": [item["code"] for item in blockers],
        "repair_routes": [
            {"code": item["code"], "route": item["route"]} for item in blockers
        ],
        "visible_deviation_classes": sorted(
            item for item in deviation_classes if item is not None
        ),
        "warnings": warnings,
        "certification": {
            "schema_valid": not schema_errors,
            "protocol_traceability_check": "pass" if not blockers else "blocked",
            "scope": "bounded_automatic_checks_only",
            "does_not_certify": [
                "scientific_truth",
                "absence_of_bias",
                "reporting_guideline_completion",
                "journal_acceptance",
            ],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("contract", type=Path)
    parser.add_argument("--adapters", type=Path, default=DEFAULT_ADAPTERS)
    args = parser.parse_args()
    contract = json.loads(args.contract.read_text(encoding="utf-8"))
    result = evaluate_study_contract(contract, load_adapter_catalog(args.adapters))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["status"] == "blocked" else 0


if __name__ == "__main__":
    raise SystemExit(main())
