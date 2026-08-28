#!/usr/bin/env python3
"""Resolve and evaluate bounded data-integrity and stewardship contracts."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any, Iterable

import jsonschema


HERE = Path(__file__).resolve().parents[1]
DEFAULT_ADAPTERS = HERE / "data-contracts" / "maintained-data-adapters.json"
DEFAULT_SCHEMA = (
    HERE / "data-contracts" / "data-integrity-stewardship-contract.schema.json"
)


def _unique(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(values))


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
        raise ValueError("invalid data adapter catalog: " + "; ".join(errors))
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
    if (
        catalog.get("selection_mode")
        != "applicable_obligations_not_universal_quality_model"
    ):
        errors.append(
            "selection_mode must be applicable_obligations_not_universal_quality_model"
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
            "generalization_rule",
            "sources",
            "update_policy",
        ):
            if not registry.get(field):
                errors.append(f"evidence_registry.{field} is required")

    sources = catalog.get("sources", [])
    source_ids = {source.get("source_id") for source in sources}
    if None in source_ids or not source_ids:
        errors.append("every source requires source_id")
    allowed_depths = {
        "full_text",
        "abstract",
        "official_standard",
        "official_policy",
        "official_guidance",
    }
    for index, source in enumerate(sources):
        for field in (
            "source_id",
            "title",
            "url",
            "source_type",
            "read_depth",
            "published_at",
            "accessed_at",
            "metadata_verification",
            "supports",
            "limits",
            "contradictions_or_tensions",
        ):
            if field not in source or source[field] in (None, ""):
                errors.append(f"sources[{index}].{field} is required")
        if source.get("read_depth") not in allowed_depths:
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
            "required_qc_dimensions",
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
    profile: dict[str, Any],
    modalities: set[str],
    study_contexts: set[str],
    sensitivity_tags: set[str],
) -> bool:
    applies = profile["applies_when"]
    return bool(
        modalities & set(applies.get("any_modalities", []))
        or study_contexts & set(applies.get("any_study_contexts", []))
        or sensitivity_tags & set(applies.get("any_sensitivity_tags", []))
    )


def resolve_data_adapter(
    *,
    modalities: Iterable[str],
    study_contexts: Iterable[str],
    sensitivity_tags: Iterable[str],
    adapters: dict[str, Any],
) -> dict[str, Any]:
    """Return applicable obligations, never a universal data-quality model."""

    def as_set(value: Iterable[str]) -> set[str]:
        return set(value) if isinstance(value, (list, tuple, set)) else set()

    modality_set = as_set(modalities)
    context_set = as_set(study_contexts)
    sensitivity_set = as_set(sensitivity_tags)
    matched = [
        profile
        for profile in adapters["profiles"]
        if _matches(profile, modality_set, context_set, sensitivity_set)
    ]
    return {
        "selection_mode": "applicable_obligations_not_universal_quality_model",
        "matched_adapter_ids": [profile["adapter_id"] for profile in matched],
        "obligations": _unique(
            obligation for profile in matched for obligation in profile["obligations"]
        ),
        "required_qc_dimensions": _unique(
            dimension
            for profile in matched
            for dimension in profile["required_qc_dimensions"]
        ),
        "hard_checks": _unique(
            check for profile in matched for check in profile["hard_checks"]
        ),
        "source_refs": _unique(
            source for profile in matched for source in profile["source_refs"]
        ),
        "transfer_limits": _unique(
            limit for profile in matched for limit in profile["transfer_limits"]
        ),
        "unresolved": []
        if matched
        else [
            "No maintained data adapter matches this modality/context. Research the current domain, instrument, repository, governance, and quality obligations rather than forcing a generic score or checklist."
        ],
    }


def _certification(schema_valid: bool, blocked: bool) -> dict[str, Any]:
    state = "blocked" if blocked else "pass"
    return {
        "schema_valid": schema_valid,
        "identity_and_fixity_check": state,
        "lineage_traceability": state,
        "quality_control_traceability": state,
        "governance_and_release_traceability": state,
        "scope": "bounded_automatic_checks_only",
        "does_not_certify": [
            "measurement_accuracy",
            "completeness_or_representativeness",
            "absence_of_bias",
            "privacy_or_anonymity",
            "legal_or_ethics_compliance",
            "scientific_truth",
            "correct_analysis",
            "analytic_reproducibility",
            "independent_replication",
            "journal_acceptance",
        ],
    }


def evaluate_data_contract(
    contract: dict[str, Any], adapters: dict[str, Any]
) -> dict[str, Any]:
    """Evaluate explicit identity, lineage, QC, governance, and release invariants."""

    blockers: list[dict[str, str]] = []
    unresolved: list[dict[str, str]] = []
    warnings = [
        "Checksums, documentation, FAIR metadata, repository deposit, and passing automated checks do not certify measurement accuracy, privacy, scientific truth, reproducibility, or journal acceptance."
    ]

    def block(code: str, message: str, route: str) -> None:
        if code not in {item["code"] for item in blockers}:
            blockers.append({"code": code, "message": message, "route": route})

    def require_research(code: str, message: str, route: str) -> None:
        if code not in {item["code"] for item in unresolved}:
            unresolved.append({"code": code, "message": message, "route": route})

    shape_errors = validate_contract_shape(contract)
    context = contract.get("data_context", {})
    resolved = resolve_data_adapter(
        modalities=context.get("modalities", []),
        study_contexts=context.get("study_contexts", []),
        sensitivity_tags=context.get("sensitivity_tags", []),
        adapters=adapters,
    )
    if shape_errors:
        block(
            "schema_validation_error",
            "The data contract is structurally incomplete or invalid: "
            + "; ".join(shape_errors),
            "Complete the contract from authoritative records and preserve unknown or not-checked states; never invent snapshots, checksums, quality receipts, permissions, identifiers, or release objects.",
        )
        return {
            "status": "blocked",
            "selection_mode": resolved["selection_mode"],
            "matched_adapter_ids": resolved["matched_adapter_ids"],
            "obligations": resolved["obligations"],
            "required_qc_dimensions": resolved["required_qc_dimensions"],
            "hard_checks": resolved["hard_checks"],
            "source_refs": resolved["source_refs"],
            "transfer_limits": resolved["transfer_limits"],
            "schema_errors": shape_errors,
            "blockers": blockers,
            "blocker_codes": [item["code"] for item in blockers],
            "repair_routes": [
                {"code": item["code"], "route": item["route"]}
                for item in blockers
            ],
            "unresolved": unresolved,
            "unresolved_codes": [],
            "research_routes": [],
            "visible_deviation_classes": [],
            "warnings": warnings,
            "certification": _certification(False, True),
        }

    if resolved["unresolved"]:
        require_research(
            "unmatched_data_modality",
            resolved["unresolved"][0],
            "Resolve the exact domain, instrument, repository, governance, and community standard from current official sources; add a maintained adapter only after source reconciliation.",
        )

    provenance = contract["source_provenance"]
    if provenance["adapter_catalog_id"] != adapters["catalog_id"]:
        block(
            "adapter_catalog_identity_mismatch",
            "The contract names a different adapter catalog from the one used for live resolution.",
            "Re-evaluate the contract with the declared versioned catalog or update the provenance to the catalog actually used; never attribute obligations to an unexecuted catalog.",
        )
    expected_registry_id = adapters.get("evidence_registry", {}).get("registry_id")
    if expected_registry_id and provenance["evidence_registry_id"] != expected_registry_id:
        block(
            "evidence_registry_identity_mismatch",
            "The contract names a different evidence registry from the one loaded with the adapter catalog.",
            "Bind the exact reconciled evidence registry used by the resolver and rerun the decision; do not substitute an unrelated or invented registry identity.",
        )
    if set(provenance["resolved_adapter_ids"]) != set(resolved["matched_adapter_ids"]):
        block(
            "resolved_adapter_provenance_mismatch",
            "The adapters recorded in contract provenance do not match the adapters resolved from the declared modality, context, and sensitivity tags.",
            "Rerun adapter resolution for the exact contract context, record the actual matched adapter identities, and reassess every resulting obligation and downstream object.",
        )

    snapshots = contract["snapshots"]
    snapshot_by_id: dict[str, dict[str, Any]] = {}
    duplicate_snapshot_ids: set[str] = set()
    for snapshot in snapshots:
        snapshot_id = snapshot["snapshot_id"]
        if snapshot_id in snapshot_by_id:
            duplicate_snapshot_ids.add(snapshot_id)
        snapshot_by_id[snapshot_id] = snapshot
    if duplicate_snapshot_ids:
        block(
            "duplicate_snapshot_identity",
            "Snapshot identities are not unique: " + ", ".join(sorted(duplicate_snapshot_ids)),
            "Assign stable unique identities and reconcile every lineage, analysis, display, and release reference before proceeding.",
        )

    if not any(
        snapshot["role"] in {"raw", "external_reference"}
        for snapshot in snapshots
    ):
        block(
            "authoritative_origin_snapshot_missing",
            "The contract has no authoritative raw or externally versioned origin snapshot.",
            "Restore or freeze the source-derived raw snapshot, or bind the exact query/source version and retrieval snapshot for an external authority, then rerun every derived object; do not promote an undocumented processed object to an origin by relabeling it.",
        )

    source_ids: set[str] = set()
    duplicate_source_ids: set[str] = set()
    for source in contract["source_records"]:
        source_id = source["source_record_id"]
        if source_id in source_ids:
            duplicate_source_ids.add(source_id)
        source_ids.add(source_id)
    if duplicate_source_ids:
        block(
            "duplicate_source_record_identity",
            "Source-record identities are not unique: "
            + ", ".join(sorted(duplicate_source_ids)),
            "Assign stable unique source/acquisition identities and reconcile every dependent snapshot before proceeding; do not collapse distinct sources under one identifier.",
        )
    for snapshot in snapshots:
        if not set(snapshot["source_record_ids"]).issubset(source_ids):
            block(
                "source_snapshot_lineage_broken",
                f"Snapshot {snapshot['snapshot_id']} cites an unknown source record.",
                "Restore the source/acquisition record or correct the snapshot lineage from authoritative evidence; do not invent a source identifier.",
            )
        invalid_missingness = any(
            item["missing_count"] > item["denominator"]
            for item in snapshot["missingness"]
        )
        if (
            invalid_missingness
            or snapshot["adverse_or_null_record_count"] > snapshot["record_count"]
        ):
            block(
                "snapshot_count_bounds_invalid",
                f"Snapshot {snapshot['snapshot_id']} declares a missing/adverse/null count larger than its denominator or record count.",
                "Recompute the version-bound counts from the authoritative snapshot, correct the schema or scientific-unit denominator if misdeclared, and rerun dependent transformations, analyses, displays, and claims.",
            )
        if snapshot["role"] == "raw" and not snapshot["immutable"]:
            block(
                "raw_snapshot_not_immutable",
                f"Raw snapshot {snapshot['snapshot_id']} is declared mutable.",
                "Freeze or restore an authoritative raw snapshot, retain the mutated object as a separate version/deviation, and rerun every dependent transformation, analysis, result, and display.",
            )
        if snapshot["role"] == "external_reference" and not snapshot["immutable"]:
            block(
                "external_reference_origin_not_fixed",
                f"External origin snapshot {snapshot['snapshot_id']} is not bound to an immutable query/version/retrieval identity.",
                "Record the exact competent source, query or record selector, source version, retrieval time, returned snapshot identity, and fixity where available; do not treat a changing remote view as a frozen analysis input.",
            )

    transformations = contract["transformations"]
    transformation_ids: set[str] = set()
    duplicate_transformation_ids: set[str] = set()
    for transformation in transformations:
        transformation_id = transformation["transformation_id"]
        if transformation_id in transformation_ids:
            duplicate_transformation_ids.add(transformation_id)
        transformation_ids.add(transformation_id)
    if duplicate_transformation_ids:
        block(
            "duplicate_transformation_identity",
            "Transformation identities are not unique: "
            + ", ".join(sorted(duplicate_transformation_ids)),
            "Assign each executed transformation a stable unique identity and reconcile its inputs, output, procedure version, parameters, and receipt; do not merge distinct processing events by label reuse.",
        )
    producers: dict[str, list[str]] = {}
    lineage_edges: dict[str, set[str]] = {}
    for transformation in transformations:
        transformation_id = transformation["transformation_id"]
        output_id = transformation["output_snapshot_id"]
        input_ids = transformation["input_snapshot_ids"]
        producers.setdefault(output_id, []).append(transformation_id)
        for input_id in input_ids:
            if input_id in snapshot_by_id and output_id in snapshot_by_id:
                lineage_edges.setdefault(input_id, set()).add(output_id)
        if output_id not in snapshot_by_id or not set(input_ids).issubset(snapshot_by_id):
            block(
                "transformation_lineage_broken",
                f"Transformation {transformation_id} refers to a missing input or output snapshot.",
                "Restore the exact input/output snapshot objects and execution record or rerun the transformation; manuscript prose cannot close a missing lineage edge.",
            )
            continue
        if not transformation["execution_receipt_id"] or not transformation[
            "parameters_recorded"
        ]:
            block(
                "transformation_execution_unverified",
                f"Transformation {transformation_id} lacks an execution receipt or recorded parameters.",
                "Locate the actual receipt/parameters or rerun the transformation from the authoritative input; otherwise mark the derived object unverified and narrow or remove dependent claims.",
            )
        output = snapshot_by_id[output_id]
        if len(input_ids) == 1:
            input_snapshot = snapshot_by_id[input_ids[0]]
            expected_count = (
                input_snapshot["record_count"]
                - transformation["records_removed"]
                + transformation["records_added"]
            )
            removal_decisions = sum(
                decision["transformation_id"] == transformation_id
                and decision["action"] in {"exclude", "deduplicate", "quarantine"}
                for decision in contract["data_decisions"]
            )
            if (
                output["record_count"] != expected_count
                or removal_decisions != transformation["records_removed"]
            ):
                block(
                    "record_count_lineage_mismatch",
                    f"Transformation {transformation_id} record counts do not reconcile with its input, output, and unit-level removal decisions.",
                    "Reconcile unit identities and counts, restore omitted records or decisions, and rerun affected outputs; never delete adverse, null, harmful, or inconvenient observations silently.",
                )

            declared_changes = set(transformation["declared_semantic_changes"])
            input_fields = {
                field["field_id"]: field for field in input_snapshot["fields"]
            }
            output_fields = {field["field_id"]: field for field in output["fields"]}
            for field_id in input_fields.keys() & output_fields.keys():
                changed = any(
                    input_fields[field_id][key] != output_fields[field_id][key]
                    for key in ("semantic_name", "data_type", "unit", "missing_code")
                )
                if changed and field_id not in declared_changes:
                    block(
                        "semantic_schema_drift_unlogged",
                        f"Field {field_id} changed semantic name, type, unit, or missing-value code without a declared transformation change.",
                        "Version and document the semantic conversion, verify units/codes against source records, and rerun dependent analyses and displays; do not repair unit drift in captions alone.",
                    )

    lineage_indegree = {snapshot_id: 0 for snapshot_id in snapshot_by_id}
    for children in lineage_edges.values():
        for child in children:
            lineage_indegree[child] += 1
    lineage_roots = [
        snapshot_id
        for snapshot_id, indegree in lineage_indegree.items()
        if indegree == 0
    ]
    visited_lineage_count = 0
    while lineage_roots:
        parent = lineage_roots.pop()
        visited_lineage_count += 1
        for child in lineage_edges.get(parent, set()):
            lineage_indegree[child] -= 1
            if lineage_indegree[child] == 0:
                lineage_roots.append(child)

    if visited_lineage_count != len(snapshot_by_id):
        block(
            "transformation_lineage_cycle",
            "The transformation graph contains a cycle and therefore cannot establish a versioned source-to-derived authority chain.",
            "Restore an acyclic version history with immutable inputs and new output identities, then rerun every affected analysis, result, display, and release; do not overwrite an ancestor in place.",
        )

    for snapshot in snapshots:
        if snapshot["role"] in {"validated", "analysis_ready", "release", "quarantined"}:
            producer_count = len(producers.get(snapshot["snapshot_id"], []))
            if producer_count != 1:
                block(
                    "transformation_lineage_broken",
                    f"Derived snapshot {snapshot['snapshot_id']} has {producer_count} producing transformations rather than exactly one.",
                    "Restore one authoritative derivation edge or version competing outputs separately; do not select a lineage from prose or filename similarity.",
                )

    for decision in contract["data_decisions"]:
        if decision["transformation_id"] not in transformation_ids:
            block(
                "data_decision_lineage_broken",
                f"Data decision {decision['decision_id']} is not bound to a known transformation.",
                "Bind the decision to the actual processing step or restore the missing step and rerun dependent objects.",
            )
        if not decision["visible"]:
            block(
                "data_decision_hidden",
                f"Data decision {decision['decision_id']} is hidden from the scientific record.",
                "Make the correction, exclusion, redaction, imputation, deduplication, or quarantine decision visible with unit, timing, reason, evidence, and affected outputs.",
            )
        if decision["affects_adverse_or_null"] and not decision["visible"]:
            block(
                "hidden_adverse_or_null_decision",
                f"Data decision {decision['decision_id']} hides an adverse, harmful, null, or extreme observation.",
                "Restore and disclose the observation and decision, rerun sensitivity analyses, and narrow/remove only the claims the visible record no longer supports; never erase the adverse or null evidence.",
            )

    for binding in contract["analysis_bindings"]:
        snapshot = snapshot_by_id.get(binding["input_snapshot_id"])
        if snapshot is None or snapshot["sha256"] != binding["input_sha256"]:
            block(
                "analysis_input_snapshot_mismatch",
                f"Analysis {binding['analysis_id']} is not bound to the declared snapshot hash.",
                "Bind or rerun the analysis on the authoritative analysis-ready snapshot and regenerate dependent results, displays, source data, and claims.",
            )

    for qc in contract["quality_controls"]:
        if qc["target_snapshot_id"] not in snapshot_by_id:
            block(
                "quality_control_target_missing",
                f"Quality-control record {qc['qc_id']} targets an unknown snapshot.",
                "Bind the QC record to the actual snapshot or rerun the check; do not reuse a receipt from another data version.",
            )
        if qc["applicability"] == "required":
            if qc["status"] == "passed" and (
                not qc["receipt_id"] or not qc["checked_at"] or not qc["outcome"]
            ):
                block(
                    "quality_control_receipt_missing",
                    f"Required QC {qc['qc_id']} is marked passed without a complete receipt, time, and outcome.",
                    "Locate the actual QC receipt or rerun the check on the exact snapshot; otherwise mark it unknown/not run and do not claim that quality criterion passed.",
                )
            elif qc["status"] == "failed":
                block(
                    "required_quality_control_failed",
                    f"Required QC {qc['qc_id']} failed its declared criterion.",
                    "Investigate and correct or quarantine the affected data, rerun QC and descendants, or remove unsupported uses; changing manuscript wording alone cannot convert failed QC to passed.",
                )
            elif qc["status"] in {"planned", "not_run", "unknown", "not_applicable"}:
                block(
                    "required_quality_control_unresolved",
                    f"Required QC {qc['qc_id']} was not verified.",
                    "Execute the applicable QC on the exact snapshot or preserve the unresolved/failed state and remove claims that require it.",
                )

    for dimension in resolved["required_qc_dimensions"]:
        dimension_records = [
            item for item in contract["quality_controls"] if item["dimension"] == dimension
        ]
        if not dimension_records:
            code = (
                "required_calibration_unverified"
                if dimension == "calibration"
                else "required_quality_control_missing"
            )
            block(
                code,
                f"The applicable adapter requires QC dimension {dimension}, but no record exists.",
                "Resolve the exact domain criterion and execute it with a version-bound receipt; if it was not done, preserve that state and do not invent calibration or QC from Methods prose.",
            )
        elif not any(item["applicability"] == "required" for item in dimension_records):
            block(
                "required_quality_control_unresolved",
                f"The applicable adapter requires QC dimension {dimension}, but every record marks it optional, not applicable, or unknown.",
                "Resolve the exact domain criterion and mark the applicable check required, then execute it on the exact snapshot with a version-bound receipt; a local not-applicable label cannot override the resolved adapter silently.",
            )

    deviation_classes = {
        item["classification"]
        for item in contract["deviations"]
        if item["status"] in {"disclosed", "resolved", "cannot_repair"}
    }
    planned_missing = context["planned_missingness_handling"]["method"]
    realized_missing = contract["realized_missingness_handling"]["method"]
    if (
        planned_missing != realized_missing
        and "missingness_handling_change" not in deviation_classes
    ):
        block(
            "missingness_handling_deviation_undisclosed",
            "Realized missing-data handling differs from the recorded plan without a visible deviation.",
            "Restore the planned method or append a dated deviation with reason, assumptions, affected analyses/claims, and sensitivity analysis; reclassify or narrow claims rather than rewriting the plan.",
        )

    governance = contract["governance"]
    if governance["consent_or_authority_requirement"] == "required" and governance[
        "consent_or_authority_status"
    ] != "verified":
        block(
            "required_data_authority_missing",
            "Required consent, ethics, legal, or other competent data authority is missing or unverified.",
            "Verify the competent authority and permitted uses before processing or release; if authority did not exist, stop the unauthorized use and document the non-repairable limitation. Prose cannot create retrospective consent or permission.",
        )
    if governance["collective_authority_required"] and governance[
        "collective_authority_status"
    ] != "verified":
        block(
            "required_collective_authority_missing",
            "Required collective or Indigenous data authority is missing or unverified.",
            "Resolve authority, benefit, responsibility, ethics, attribution, and reuse terms with the actual rights-holders before processing or release; a generic open-data licence is not a substitute.",
        )

    third_party = any(
        source["kind"] == "third_party" for source in contract["source_records"]
    )
    third_party_source_unverified = any(
        source["kind"] == "third_party"
        and (
            source["rights_status"] != "verified"
            or not source["authority_or_licence_ids"]
        )
        for source in contract["source_records"]
    )
    if third_party and (
        third_party_source_unverified
        or governance["third_party_rights_status"] != "verified"
    ):
        block(
            "third_party_rights_missing",
            "Third-party data are used or released without verified rights and authority identifiers.",
            "Secure and record the actual licence/permission or remove and replace the third-party data and rerun descendants; manuscript wording or claim narrowing cannot create redistribution rights.",
        )

    release = contract["release"]
    public_route = release["route"] in {"public_repository", "within_article"}
    sensitive_class = governance["sensitivity_class"] not in {"non_sensitive"}
    if public_route and (
        not governance["public_release_permitted"]
        or governance["direct_identifiers_present"]
        or sensitive_class
    ):
        block(
            "unauthorized_sensitive_public_release",
            "The contract routes sensitive or identifiable data to public release without a verified permission basis.",
            "Stop public release and resolve consent, community authority, re-identification risk, law, and institutional policy; use a valid controlled-access, trusted-environment, safe-output, synthetic/representative, or metadata-only route where authorized.",
        )

    policy = governance["exact_policy_resolution"]
    if (
        policy["applicability"] == "required"
        and policy["as_of_date"] != contract["as_of_date"]
    ):
        require_research(
            "exact_data_policy_as_of_mismatch",
            "The exact-policy decision date does not match the data contract as-of date.",
            "Resolve the competent policy for the contract's exact as-of date and preserve other dates as separate historical or future policy snapshots; do not transfer a decision across dates silently.",
        )
    if policy["applicability"] == "required" and policy["status"] != "resolved":
        require_research(
            "exact_data_policy_unresolved",
            "An exact institutional, legal, funder, repository, or community data policy is required but unresolved.",
            "Resolve the exact authority from current official sources for the contract as-of date and record effective-date basis; do not substitute a maintained adapter or observed-current page for exact policy.",
        )
    if policy["status"] == "resolved":
        as_of = date.fromisoformat(policy["as_of_date"])
        if not policy["authorities"]:
            require_research(
                "exact_data_policy_provenance_missing",
                "The exact data policy is marked resolved without an authoritative source record.",
                "Resolve the competent official source for the contract tuple and as-of date, then record its title, URL, review date, and effective-date basis; do not certify policy from an empty source list.",
            )
        for authority in policy["authorities"]:
            effective_from = authority["effective_from"]
            effective_until = authority["effective_until"]
            reviewed_at = date.fromisoformat(authority["reviewed_at"])
            if authority["effective_date_basis"] == "unresolved":
                require_research(
                    "exact_data_policy_effective_date_unresolved",
                    f"Policy {authority['title']} has no resolved effective-date basis.",
                    "Confirm the policy's official effective interval or preserve it only as observed-current evidence; do not infer historical applicability from page content alone.",
                )
            if (
                authority["effective_date_basis"]
                == "observed_active_not_backcastable"
                and reviewed_at > as_of
            ):
                require_research(
                    "historical_data_policy_not_backcastable",
                    f"Policy {authority['title']} was observed after the contract as-of date and cannot establish the older rule.",
                    "Resolve an archived or explicitly effective official source governing the as-of date; retain the observed-current page only as present-day provenance.",
                )
            if effective_from and date.fromisoformat(effective_from) > as_of:
                require_research(
                    "future_effective_data_policy",
                    f"Policy {authority['title']} becomes effective after the contract as-of date.",
                    "Do not apply the future rule retroactively; resolve the policy actually governing the as-of date and retain the future source as prospective provenance.",
                )
            if effective_until and date.fromisoformat(effective_until) < as_of:
                require_research(
                    "expired_data_policy",
                    f"Policy {authority['title']} expired before the contract as-of date.",
                    "Resolve the successor or contemporaneous official policy rather than applying an expired snapshot.",
                )

    released_snapshot = (
        snapshot_by_id.get(release["snapshot_id"]) if release["snapshot_id"] else None
    )
    if release["status"] in {"deposited", "verified"}:
        if public_route and not release["licence"]:
            block(
                "public_release_licence_missing",
                "A deposited/verified public release has no recorded reuse licence or public-domain basis.",
                "Record the actual repository licence or public-domain basis authorized by the rights-holder, or use the valid restricted/controlled route; do not infer reuse permission from public accessibility alone.",
            )
        if (
            not release["persistent_id"]
            or not release["locator"]
            or not release["version"]
            or not release["resolved_at"]
            or released_snapshot is None
        ):
            block(
                "release_claim_unverified",
                "A deposited/verified release lacks a resolvable identifier, locator, version, resolution time, or bound snapshot.",
                "Deposit and verify the exact object and access route or state the real planned/restricted/unavailable status; never publish a placeholder DOI, accession, URL, or availability claim.",
            )
        if released_snapshot is not None and (
            release["snapshot_sha256"] != released_snapshot["sha256"]
        ):
            block(
                "release_snapshot_mismatch",
                "The release hash does not match the snapshot named in the release record.",
                "Verify and bind the actual deposited version, correct or replace the release with version/tombstone provenance, and update every availability and citation statement.",
            )

    for claim in contract["claims"]:
        if not set(claim["data_snapshot_ids"]).issubset(snapshot_by_id):
            block(
                "claim_data_snapshot_missing",
                f"Claim {claim['claim_id']} cites an unknown data snapshot.",
                "Bind the claim to the exact supporting snapshot or remove/narrow the claim; never infer support from a filename, repository page, or manuscript statement.",
            )

    status = "blocked" if blockers else ("unresolved" if unresolved else "pass")
    return {
        "status": status,
        "selection_mode": resolved["selection_mode"],
        "matched_adapter_ids": resolved["matched_adapter_ids"],
        "obligations": resolved["obligations"],
        "required_qc_dimensions": resolved["required_qc_dimensions"],
        "hard_checks": resolved["hard_checks"],
        "source_refs": resolved["source_refs"],
        "transfer_limits": resolved["transfer_limits"],
        "schema_errors": [],
        "blockers": blockers,
        "blocker_codes": [item["code"] for item in blockers],
        "repair_routes": [
            {"code": item["code"], "route": item["route"]} for item in blockers
        ],
        "unresolved": unresolved,
        "unresolved_codes": [item["code"] for item in unresolved],
        "research_routes": [
            {"code": item["code"], "route": item["route"]}
            for item in unresolved
        ],
        "visible_deviation_classes": sorted(deviation_classes),
        "warnings": warnings,
        "certification": _certification(True, bool(blockers)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resolve and evaluate a data-integrity/stewardship contract."
    )
    parser.add_argument("contract", help="Path to the contract JSON file")
    parser.add_argument("--adapters", default=str(DEFAULT_ADAPTERS))
    args = parser.parse_args()
    contract = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    adapters = load_adapter_catalog(args.adapters)
    result = evaluate_data_contract(contract, adapters)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
