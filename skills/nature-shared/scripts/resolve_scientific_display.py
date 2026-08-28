#!/usr/bin/env python3
"""Resolve and evaluate scientific display decision contracts.

The resolver returns candidate representation families and obligations. It never
declares a universal best chart. The evaluator checks evidence lineage,
caption/data consistency, accessibility, omission disclosure, and high-risk
inference boundaries without pretending to validate the underlying science.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

import jsonschema


HERE = Path(__file__).resolve().parents[1]
DEFAULT_ADAPTERS = HERE / "display-contracts" / "maintained-adapters.json"
DEFAULT_SCHEMA = HERE / "display-contracts" / "scientific-display-contract.schema.json"


def load_adapter_catalog(path: str | Path = DEFAULT_ADAPTERS) -> dict[str, Any]:
    catalog_path = Path(path)
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    registry_file = catalog.get("evidence_registry_file")
    if registry_file:
        registry = json.loads((catalog_path.parent / registry_file).read_text(encoding="utf-8"))
        catalog["evidence_registry"] = registry
        catalog["sources"] = registry.get("sources", [])
    errors = validate_adapter_catalog(catalog)
    if errors:
        raise ValueError("invalid display adapter catalog: " + "; ".join(errors))
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
    if catalog.get("selection_mode") != "candidate_set_not_universal_best":
        errors.append("selection_mode must be candidate_set_not_universal_best")

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
            "candidate_families",
            "disallowed_families",
            "obligations",
            "source_refs",
        ):
            if field not in profile:
                errors.append(f"{adapter_id}: {field} is required")
        for source_ref in profile.get("source_refs", []):
            if source_ref not in source_ids:
                errors.append(f"{adapter_id}: unknown source_ref {source_ref}")
        if len(profile.get("source_refs", [])) < 2:
            errors.append(f"{adapter_id}: at least two source_refs are required")
    return errors


def validate_display_contract_shape(
    contract: dict[str, Any], schema_path: str | Path = DEFAULT_SCHEMA
) -> list[str]:
    schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    errors: list[str] = []
    for error in sorted(validator.iter_errors(contract), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "$"
        errors.append(f"{location}: {error.message}")
    return errors


def _matches(
    profile: dict[str, Any],
    *,
    reader_task: str,
    data_structure: set[str],
    claim_type: str,
) -> bool:
    applies = profile["applies_when"]
    tasks = set(applies.get("reader_tasks", []))
    structures = set(applies.get("any_data_structures", []))
    claim_types = set(applies.get("claim_types", []))
    return (
        (not tasks or reader_task in tasks)
        and (not structures or bool(data_structure & structures))
        and (not claim_types or claim_type in claim_types)
    )


def _unique(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(values))


def resolve_display_adapter(
    *,
    reader_task: str,
    data_structure: Iterable[str],
    claim_type: str,
    adapters: dict[str, Any],
) -> dict[str, Any]:
    """Return evidence-informed candidates; never choose a universal best chart."""

    structures = set(data_structure)
    matched = [
        profile
        for profile in adapters["profiles"]
        if _matches(
            profile,
            reader_task=reader_task,
            data_structure=structures,
            claim_type=claim_type,
        )
    ]
    return {
        "selection_mode": "candidate_set_not_universal_best",
        "matched_adapter_ids": [profile["adapter_id"] for profile in matched],
        "candidate_families": _unique(
            family for profile in matched for family in profile["candidate_families"]
        ),
        "disallowed_families": _unique(
            family for profile in matched for family in profile["disallowed_families"]
        ),
        "obligations": _unique(
            obligation for profile in matched for obligation in profile["obligations"]
        ),
        "source_refs": _unique(
            source_ref for profile in matched for source_ref in profile["source_refs"]
        ),
        "unresolved": []
        if matched
        else [
            "No maintained adapter matches this reader task/data structure. Research the domain-specific representation rather than forcing a generic chart."
        ],
    }


def _claim_types(contract: dict[str, Any]) -> set[str]:
    return {claim.get("claim_type", "") for claim in contract.get("claim_links", [])}


def _allowed_inferences(contract: dict[str, Any]) -> set[str]:
    return {
        inference
        for claim in contract.get("claim_links", [])
        for inference in claim.get("allowed_inferences", [])
    }


def evaluate_display_contract(
    contract: dict[str, Any], adapters: dict[str, Any]
) -> dict[str, Any]:
    """Evaluate high-risk semantic and provenance invariants.

    Passing means the recorded display contract satisfies these bounded checks.
    It does not validate the data, analysis, scientific claim, or journal acceptance.
    """

    blockers: list[dict[str, str]] = []
    warnings: list[str] = []

    def block(code: str, message: str, route: str) -> None:
        if code not in {item["code"] for item in blockers}:
            blockers.append({"code": code, "message": message, "route": route})

    schema_errors = validate_display_contract_shape(contract)
    if schema_errors:
        block(
            "schema_validation_error",
            "The display contract is structurally incomplete or invalid: "
            + "; ".join(schema_errors),
            "complete the required fields from verified project objects before relying on semantic evaluation; leave unknown evidence unresolved rather than inventing values.",
        )

    claims = contract.get("claim_links", [])
    claim_type = claims[0].get("claim_type", "unknown") if claims else "unknown"
    reader_task = contract.get("reader_task", {}).get("id", "unknown")
    scientific_object = contract.get("scientific_object", {})
    resolved = resolve_display_adapter(
        reader_task=reader_task,
        data_structure=scientific_object.get("data_structure", []),
        claim_type=claim_type,
        adapters=adapters,
    )
    representation = contract.get("representation", {})
    family = representation.get("family")

    if family in resolved["disallowed_families"]:
        code = (
            "paired_structure_not_visible"
            if "paired-change" in resolved["matched_adapter_ids"]
            else "representation_family_disallowed"
        )
        block(
            code,
            f"{family} hides or contradicts a required data relationship.",
            "Choose a candidate representation that exposes the scientific unit and dependence structure, or narrow the estimand.",
        )

    evidence = contract.get("evidence_links", {})
    data = evidence.get("data_snapshot", {})
    analysis = evidence.get("analysis_receipt", {})
    render = evidence.get("render_receipt", {})
    source_data = evidence.get("source_data", {})
    if data.get("sha256") != analysis.get("input_data_sha256"):
        block(
            "analysis_input_snapshot_mismatch",
            "The analysis receipt is not bound to the declared data snapshot.",
            "Re-run or re-bind the analysis to the declared immutable data snapshot; do not relabel an unrelated receipt.",
        )
    if analysis.get("sha256") != render.get("input_analysis_sha256"):
        block(
            "render_input_analysis_mismatch",
            "The render receipt is not bound to the declared analysis receipt.",
            "Re-render from the declared analysis output and record the resulting receipt.",
        )
    if data.get("sha256") != source_data.get("input_data_sha256"):
        block(
            "source_data_snapshot_mismatch",
            "The figure source-data object is not bound to the declared data snapshot.",
            "Regenerate source data from the declared snapshot or explicitly version the changed snapshot.",
        )

    denominator = scientific_object.get("population_denominator")
    caption_denominator = contract.get("caption", {}).get("denominator")
    if denominator != caption_denominator:
        block(
            "caption_denominator_mismatch",
            "The caption denominator differs from the scientific-object denominator.",
            "reconcile the population label and count against source data; if the analyzed population changed, version the contract and claim without inventing agreement.",
        )
    if scientific_object.get("statistical_unit") != contract.get("caption", {}).get(
        "statistical_unit"
    ):
        block(
            "statistical_unit_mismatch",
            "The caption and scientific object name different statistical units.",
            "Resolve the true independent unit and update the analysis, visual encoding, caption, and claim consistently.",
        )

    uncertainty = representation.get("uncertainty", {})
    if uncertainty.get("shown") and (
        uncertainty.get("kind") in (None, "", "unspecified")
        or not uncertainty.get("unit")
        or not contract.get("caption", {}).get("uncertainty_definition", "").strip()
    ):
        block(
            "uncertainty_semantics_missing",
            "Displayed uncertainty is not defined by kind, unit, and caption meaning.",
            "Name the uncertainty quantity, level where applicable, inferential unit, and construction method; otherwise remove unsupported error bars.",
        )

    transformations = {item.get("id") for item in representation.get("transformations", [])}
    disclosures = set(contract.get("caption", {}).get("transformation_disclosures", []))
    missing_disclosures = transformations - disclosures
    if missing_disclosures:
        block(
            "transformation_disclosure_missing",
            "One or more visual transformations are absent from the caption disclosure.",
            "Disclose the transformation and parameters, or remove it and re-render without changing the underlying evidence.",
        )
    for scale in representation.get("scales", []):
        if scale.get("truncated") and not scale.get("disclosed"):
            block(
                "undisclosed_scale_truncation",
                "A truncated scale is not disclosed.",
                "Disclose and justify the limits or restore a non-truncated view that preserves the relevant comparison.",
            )

    observed = set(representation.get("observed_groups", []))
    plotted = set(representation.get("plotted_groups", []))
    disclosed = {
        item.get("group") for item in representation.get("omission_disclosures", [])
    }
    undisclosed = observed - plotted - disclosed
    if undisclosed:
        block(
            "undisclosed_group_omission",
            "Observed groups are omitted without an explicit display or placement disclosure: "
            + ", ".join(sorted(undisclosed)),
            "Restore the groups, place them in a traceable companion display, or disclose a scientifically justified omission without erasing adverse or null evidence.",
        )

    allowed = _allowed_inferences(contract)
    types = _claim_types(contract)
    if family in {"embedding", "small_multiple_embedding"} and (
        "mechanism" in allowed or "mechanistic" in types or "causal_effect" in allowed
    ):
        block(
            "embedding_mechanism_overclaim",
            "An embedding alone cannot establish a causal or mechanistic claim.",
            "Add independent quantitative or experimental evidence, or narrow the claim to descriptive orientation in the embedding.",
        )
    if family == "workflow_diagram" and (
        "causal_effect" in allowed or "causal" in types or "mechanistic" in types
    ):
        block(
            "workflow_causal_overclaim",
            "A workflow diagram records sequence; it does not establish causal structure.",
            "Use workflow language only, or supply a separately contracted causal model and supporting identification/evidence.",
        )

    for claim in claims:
        overlap = set(claim.get("allowed_inferences", [])) & set(
            claim.get("prohibited_inferences", [])
        )
        if overlap:
            block(
                "contradictory_inference_boundary",
                "The same inference is both allowed and prohibited: "
                + ", ".join(sorted(overlap)),
                "Resolve the claim boundary from the evidence before rendering or revising prose.",
            )

    accessibility = contract.get("accessibility", {})
    if accessibility.get("color_only_encoding") and not accessibility.get(
        "redundant_channels"
    ):
        block(
            "color_only_encoding",
            "Color is the only channel carrying information.",
            "Add redundant position, shape, pattern, line style, text, or direct labels and verify the final rendering.",
        )
    if contract.get("stage") in {"final", "production", "post_publication"} and not accessibility.get(
        "alt_text", ""
    ).strip():
        block(
            "alt_text_missing",
            "A final-stage display lacks semantic alt text.",
            "Write alt text that states the display purpose, important pattern, and bounded conclusion without merely repeating the caption.",
        )

    if resolved["unresolved"]:
        warnings.extend(resolved["unresolved"])

    return {
        "display_id": contract.get("display_id"),
        "status": "blocked" if blockers else "pass",
        "blockers": blockers,
        "blocker_codes": [item["code"] for item in blockers],
        "repair_routes": [
            {"code": item["code"], "route": item["route"]} for item in blockers
        ],
        "warnings": warnings,
        "schema_errors": schema_errors,
        "matched_adapter_ids": resolved["matched_adapter_ids"],
        "candidate_families": resolved["candidate_families"],
        "selection_mode": resolved["selection_mode"],
        "certification": {
            "level": "bounded_display_contract_check",
            "passed": not blockers,
            "does_not_certify": [
                "truth_of_underlying_data",
                "validity_of_analysis",
                "truth_of_scientific_claim",
                "journal_acceptance",
            ],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path)
    parser.add_argument("--adapters", type=Path, default=DEFAULT_ADAPTERS)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    contract = json.loads(args.contract.read_text(encoding="utf-8"))
    result = evaluate_display_contract(contract, load_adapter_catalog(args.adapters))
    print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
