#!/usr/bin/env python3
"""Resolve and evaluate bounded statistical-inference decision contracts.

The resolver composes applicable obligations. It never selects a universal best
test, model, interval, prior, threshold, chart, or evidential framework. The
evaluator checks recorded identities and contradictions; it does not certify
scientific truth, model adequacy, causal identification, or acceptance.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any, Iterable

import jsonschema


HERE = Path(__file__).resolve().parents[1]
DEFAULT_ADAPTERS = HERE / "analysis-contracts" / "maintained-analysis-adapters.json"
DEFAULT_SCHEMA = (
    HERE
    / "analysis-contracts"
    / "statistical-inference-uncertainty-contract.schema.json"
)


def _unique(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(values))


def load_adapter_catalog(path: str | Path = DEFAULT_ADAPTERS) -> dict[str, Any]:
    """Load a maintained catalog and its separately auditable evidence registry."""

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
        raise ValueError("invalid statistical adapter catalog: " + "; ".join(errors))
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
    if catalog.get("selection_mode") != "applicable_obligations_not_universal_method":
        errors.append(
            "selection_mode must be applicable_obligations_not_universal_method"
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
        "metadata",
        "official_guideline",
        "official_policy",
        "technical_standard",
    }
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
            if source.get(field) in (None, "", []):
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
            "hard_checks",
            "source_refs",
            "transfer_limits",
        ):
            if not profile.get(field):
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
    for error in sorted(
        validator.iter_errors(contract), key=lambda item: list(item.path)
    ):
        location = ".".join(str(part) for part in error.path) or "$"
        errors.append(f"{location}: {error.message}")
    return errors


def _matches(
    profile: dict[str, Any],
    analysis_families: set[str],
    study_archetypes: set[str],
    design_tags: set[str],
    inference_modes: set[str],
) -> bool:
    applies = profile["applies_when"]
    return bool(
        analysis_families & set(applies.get("any_analysis_families", []))
        or study_archetypes & set(applies.get("any_study_archetypes", []))
        or design_tags & set(applies.get("any_design_tags", []))
        or inference_modes & set(applies.get("any_inference_modes", []))
    )


def resolve_analysis_adapters(
    *,
    analysis_families: Iterable[str],
    study_archetypes: Iterable[str],
    design_tags: Iterable[str],
    inference_modes: Iterable[str],
    adapters: dict[str, Any],
) -> dict[str, Any]:
    """Return composable obligations, never a universal method recommendation."""

    families = set(analysis_families)
    archetypes = set(study_archetypes)
    tags = set(design_tags)
    modes = set(inference_modes)
    matched = [
        profile
        for profile in adapters["profiles"]
        if _matches(profile, families, archetypes, tags, modes)
    ]
    return {
        "selection_mode": "applicable_obligations_not_universal_method",
        "matched_adapter_ids": [profile["adapter_id"] for profile in matched],
        "obligations": _unique(
            obligation for profile in matched for obligation in profile["obligations"]
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
            "No maintained adapter matches this analysis domain. Research the current domain, method, regulator, reporting standard, and exact venue policy rather than forcing a universal method."
        ],
    }


def _certification(schema_valid: bool, blocked: bool) -> dict[str, Any]:
    state = "blocked" if blocked else "pass"
    return {
        "schema_valid": schema_valid,
        "recorded_identity_and_fixity_checks": state,
        "recorded_analysis_and_surface_consistency_checks": state,
        "recorded_inference_boundary_checks": state,
        "scope": "bounded_recorded_invariants_only",
        "does_not_certify": [
            "model_adequacy_or_assumption_truth",
            "causal_identification",
            "absence_of_bias",
            "measurement_validity",
            "adequate_power_or_precision",
            "analytic_reproducibility_or_independent_replication",
            "external_validity_or_generalization",
            "scientific_truth",
            "reporting_guideline_completion",
            "journal_acceptance",
        ],
    }


def evaluate_statistical_contract(
    contract: dict[str, Any], adapters: dict[str, Any]
) -> dict[str, Any]:
    """Evaluate explicit analysis, uncertainty, and cross-surface invariants."""

    blockers: list[dict[str, str]] = []
    unresolved: list[dict[str, str]] = []
    warnings = [
        "Passing recorded checks does not prove assumptions, model adequacy, causal identification, adequate precision, generalization, scientific truth, or journal acceptance."
    ]

    def block(code: str, message: str, route: str) -> None:
        if code not in {item["code"] for item in blockers}:
            blockers.append({"code": code, "message": message, "route": route})

    def require_research(code: str, message: str, route: str) -> None:
        if code not in {item["code"] for item in unresolved}:
            unresolved.append({"code": code, "message": message, "route": route})

    shape_errors = validate_contract_shape(contract)
    if shape_errors:
        block(
            "schema_validation_error",
            "; ".join(shape_errors),
            "Correct the contract shape before any semantic evaluation.",
        )
        return _result(blockers, unresolved, warnings, {}, [], False)

    context = contract["analysis_context"]
    resolved = resolve_analysis_adapters(
        analysis_families=context["analysis_families"],
        study_archetypes=context["study_archetypes"],
        design_tags=context["design_tags"],
        inference_modes=context["inference_modes"],
        adapters=adapters,
    )
    if not resolved["matched_adapter_ids"]:
        require_research(
            "unmatched_analysis_domain",
            resolved["unresolved"][0],
            "Resolve current methodological and official sources, record a bounded adapter with transfer limits, or declare a non-quantitative boundary.",
        )

    provenance = contract["source_provenance"]
    if provenance["adapter_catalog_id"] != adapters["catalog_id"]:
        block(
            "adapter_catalog_identity_mismatch",
            "The contract catalog identity differs from the loaded maintained catalog.",
            "Re-resolve against the intended dated catalog and preserve the catalog identity.",
        )
    registry_id = adapters.get("evidence_registry", {}).get("registry_id")
    if registry_id and provenance["evidence_registry_id"] != registry_id:
        block(
            "evidence_registry_identity_mismatch",
            "The contract evidence-registry identity differs from the loaded registry.",
            "Re-resolve and bind the intended dated evidence registry.",
        )
    if set(provenance["resolved_adapter_ids"]) != set(resolved["matched_adapter_ids"]):
        block(
            "resolved_adapter_provenance_mismatch",
            "Declared adapters do not match live resolution for the recorded context.",
            "Re-run adapter resolution, update provenance, and review newly activated obligations.",
        )

    input_sha = contract["upstream_bindings"]["analysis_input"]["sha256"]
    data_sha = contract["upstream_bindings"]["data_integrity"]["sha256"]
    if input_sha != data_sha:
        block(
            "analysis_input_snapshot_mismatch",
            "The statistical input is not the bound analysis-ready data snapshot.",
            "Rebind or rerun the analysis from the immutable authorized snapshot.",
        )

    plans = {item["plan_id"]: item for item in contract["analysis_plans"]}
    executions = contract["analysis_executions"]
    execution_ids = [item["analysis_id"] for item in executions]
    execution_map = {item["analysis_id"]: item for item in executions}
    results = contract["results"]
    result_map = {item["result_id"]: item for item in results}
    result_ids = [item["result_id"] for item in results]
    estimand_map = {item["estimand_id"]: item for item in contract["estimands"]}
    if len(execution_ids) != len(set(execution_ids)):
        block(
            "duplicate_analysis_identity",
            "Analysis-execution identities are not unique.",
            "Assign immutable unique analysis identities and repair every plan, result, and receipt binding.",
        )
    if len(result_ids) != len(set(result_ids)):
        block(
            "duplicate_result_identity",
            "Result identities are not unique.",
            "Assign immutable unique result identities and repair every dependent binding.",
        )

    for execution in executions:
        if execution["input_snapshot_sha256"] != input_sha:
            block(
                "analysis_input_snapshot_mismatch",
                "An execution used a snapshot other than the bound analysis input.",
                "Rerun from the bound snapshot or version and disclose the new input and outputs.",
            )
        if not execution["code_receipt"] or not execution["environment_receipt"]:
            block(
                "analysis_execution_receipt_missing",
                "An analysis execution lacks a code or environment receipt.",
                "Restore the execution provenance or rerun the analysis in a recorded environment; prose edits cannot create execution evidence.",
            )
        plan = plans.get(execution["plan_id"])
        if not plan:
            block(
                "analysis_plan_binding_broken",
                f"Analysis execution {execution['analysis_id']} references an unknown plan {execution['plan_id']}.",
                "Restore the exact plan binding or visibly classify the execution as unplanned with a versioned deviation; claim narrowing cannot create prespecification.",
            )
        else:
            method_changed = any(
                execution[field] != plan[field]
                for field in (
                    "estimator",
                    "model",
                    "independent_unit",
                    "dependence_handling",
                )
            )
            disclosed_method_change = any(
                deviation["classification"] == "analysis_method_change"
                and deviation["status"] == "disclosed"
                and (
                    deviation["to_object_id"] == execution["analysis_id"]
                    or bool(
                        set(deviation["affected_result_ids"])
                        & set(execution["result_ids"])
                    )
                )
                for deviation in contract["deviations"]
            )
            if method_changed and not disclosed_method_change:
                block(
                    "analysis_plan_execution_mismatch",
                    "The executed estimator, model, independent unit, or dependence handling differs from plan without a visible deviation.",
                    "Restore the planned analysis or version and disclose the deviation, reclassify its status, and narrow affected claims where needed.",
                )
            if (
                execution["missing_data_strategy"]
                != plan["missing_data"]["realized_strategy"]
            ):
                disclosed_missing_change = any(
                    deviation["classification"] == "missing_data_strategy_change"
                    and deviation["status"] == "disclosed"
                    and (
                        deviation["to_object_id"] == execution["analysis_id"]
                        or bool(
                            set(deviation["affected_result_ids"])
                            & set(execution["result_ids"])
                        )
                    )
                    for deviation in contract["deviations"]
                )
                if not disclosed_missing_change:
                    block(
                        "missing_data_plan_execution_mismatch",
                        "Executed missing-data handling differs from the recorded realized strategy.",
                        "Correct the binding or disclose and justify the changed strategy, rerun sensitivity work, and narrow the claim if needed.",
                    )
            multiplicity = plan["multiplicity"]
            if (
                plan["classification"] == "confirmatory"
                and multiplicity["applicability"] == "required"
                and (
                    multiplicity["method"] in {"", "none"}
                    or not multiplicity["receipt"]
                )
            ):
                block(
                    "confirmatory_multiplicity_unresolved",
                    "A confirmatory hypothesis family has no recorded error-control decision.",
                    "Resolve and execute the declared multiplicity objective, or visibly reclassify the analyses and narrow confirmatory claims.",
                )
            if plan["sample_size"]["observed_power_used_for_inference"]:
                block(
                    "post_hoc_observed_power_used_as_evidence",
                    "Observed post-result power is being used as inferential evidence.",
                    "Report the estimate and uncertainty, preserve the prospective rationale, and remove the post-hoc power inference.",
                )
        if execution["convergence_status"] == "failed":
            block(
                "analysis_nonconvergence",
                "A model-based result is linked to an execution recorded as nonconverged.",
                "Rerun or refit a justified model with diagnostics, or narrow/remove the model-dependent claim while preserving the failed result.",
            )
        if contract["stage"] in {"final", "submission"}:
            for diagnostic in execution["diagnostics"]:
                if not diagnostic["receipt"]:
                    block(
                        "diagnostic_receipt_missing",
                        "A final-stage diagnostic is represented without a receipt.",
                        "Execute and record the diagnostic or mark the check unresolved and narrow dependent claims.",
                    )

        owned_result_ids = {
            result["result_id"]
            for result in results
            if result["analysis_id"] == execution["analysis_id"]
        }
        if set(execution["result_ids"]) != owned_result_ids:
            block(
                "execution_result_binding_broken",
                f"Analysis execution {execution['analysis_id']} has a result manifest that does not match the results bound to it.",
                "Reconcile the execution manifest and result analysis IDs against the immutable execution receipt; do not invent or silently reassign outputs.",
            )

    units = contract["units_and_dependence"]
    if units["reported_n"] > units["independent_unit_count"] or any(
        item["independent_n"] > units["independent_unit_count"] for item in results
    ):
        block(
            "subsample_as_independent_n",
            "The reported independent n exceeds the recorded independent-unit count.",
            "Correct n and uncertainty using the true independent unit, refit dependence-aware analysis, and narrow affected claims.",
        )
    if units["dependence_structure"] and (
        units["dependence_handling"]["status"] in {"ignored", "unresolved"}
        or not units["dependence_handling"]["receipt"]
    ):
        block(
            "dependence_structure_unhandled",
            "Recorded clustering or repeated dependence is ignored or unverified.",
            "Model, aggregate, or otherwise justify the dependence handling and rerun the analysis.",
        )

    planned_primary_ids = {
        result_id
        for plan in contract["analysis_plans"]
        for result_id in plan["primary_result_ids"]
    }
    for result_id in sorted(planned_primary_ids - set(result_ids)):
        block(
            "planned_primary_result_missing",
            f"Planned primary result {result_id} is absent, including if null, adverse, harmful, or failed.",
            "Restore and report the result or visibly mark it unavailable/failed and narrow or remove every dependent claim.",
        )

    claim_map = {item["claim_id"]: item for item in contract["claim_links"]}
    for result in results:
        if result["analysis_id"] not in execution_map:
            block(
                "result_execution_binding_broken",
                f"Result {result['result_id']} references an unknown analysis execution {result['analysis_id']}.",
                "Restore the result-to-execution binding or rerun the analysis with code, environment, input, and diagnostic receipts; prose or claim narrowing cannot create an execution.",
            )
        decision = result["decision"]
        linked_claims = [claim_map[c] for c in result["claim_ids"] if c in claim_map]
        if decision["comparison_basis"] == "separate_significance_tests" or any(
            claim["comparison_basis"] == "separate_significance_tests"
            for claim in linked_claims
        ):
            block(
                "difference_in_significance_is_not_significant_difference",
                "Separate within-group significance decisions do not test a between-group difference.",
                "Estimate and test the direct contrast or narrow the claim to the separately estimated quantities.",
            )
        absence_supported = decision["state"] == "supported" and (
            decision["objective"] == "no_meaningful_effect"
            or any(
                claim["requested_inference"] == "no_meaningful_effect"
                and claim["state"] == "supported"
                for claim in linked_claims
            )
        )
        if absence_supported and decision["objective"] not in {
            "equivalence",
            "noninferiority",
        }:
            block(
                "absence_from_nonsignificance",
                "Nonsignificance is represented as evidence of no meaningful effect.",
                "Use a prospectively justified equivalence/precision objective or narrow the claim to inconclusive evidence.",
            )
        if decision["state"] == "supported" and decision["objective"] == "equivalence":
            margin = decision["margin"]
            interval = result["uncertainty"]
            crossed = margin is None
            if margin is not None:
                crossed = interval["lower"] <= -abs(margin) or interval["upper"] >= abs(
                    margin
                )
            if crossed or not decision["margin_provenance"]:
                block(
                    "equivalence_margin_missing_or_crossed",
                    "A supported equivalence decision lacks a justified margin or its interval crosses the decision boundary.",
                    "Prespecify and justify the margin, apply the correct interval decision, or mark the result inconclusive and narrow the claim.",
                )
        if (
            decision["state"] == "supported"
            and decision["objective"] == "noninferiority"
        ):
            margin_rule = decision.get("margin_rule")
            if (
                decision["margin"] is None
                or not decision["margin_provenance"]
                or margin_rule is None
            ):
                block(
                    "noninferiority_decision_rule_missing",
                    "A supported noninferiority decision lacks a justified margin or an explicit effect-scale, direction, bound, and boundary rule.",
                    "Record the prospectively justified margin and exact interval decision rule, or mark the result inconclusive and narrow the claim.",
                )
            else:
                estimand = estimand_map.get(result["estimand_id"])
                declared_direction = {
                    "higher_is_better": "higher",
                    "lower_is_better": "lower",
                }.get(estimand["direction"] if estimand else "")
                expected_bound = {
                    "higher": "lower",
                    "lower": "upper",
                }[margin_rule["favorable_direction"]]
                if (
                    margin_rule["effect_scale"] != result["estimate"]["scale"]
                    or margin_rule["required_interval_bound"] != expected_bound
                    or (
                        declared_direction is not None
                        and margin_rule["favorable_direction"] != declared_direction
                    )
                ):
                    block(
                        "noninferiority_decision_rule_mismatch",
                        "The noninferiority rule contradicts the result effect scale, favorable direction, estimand direction, or required interval bound.",
                        "Correct the recorded rule from the prespecified estimand and margin, rerun if needed, or mark the result inconclusive.",
                    )
                sidedness_bounds = {
                    "two_sided": {"lower", "upper"},
                    "one_sided_lower": {"lower"},
                    "lower_one_sided": {"lower"},
                    "one_sided_upper": {"upper"},
                    "upper_one_sided": {"upper"},
                }
                available_bounds = sidedness_bounds.get(
                    result["uncertainty"]["sidedness"]
                )
                required_bound = margin_rule["required_interval_bound"]
                if available_bounds is None or required_bound not in available_bounds:
                    block(
                        "noninferiority_interval_sidedness_mismatch",
                        "The recorded interval sidedness does not provide the bound required by the noninferiority rule.",
                        "Use and label the prespecified compatible one- or two-sided interval, or mark the decision inconclusive.",
                    )
                observed_bound = result["uncertainty"][required_bound]
                boundary = margin_rule["boundary_value"]
                crossed = (
                    observed_bound <= boundary
                    if required_bound == "lower"
                    else observed_bound >= boundary
                )
                if crossed:
                    block(
                        "noninferiority_margin_crossed",
                        "The interval bound required by the recorded noninferiority rule reaches or crosses its effect-scale boundary.",
                        "Report the result as inconclusive for noninferiority, or rerun only a prospectively justified analysis; claim narrowing cannot move the margin.",
                    )

        requested = {claim["requested_inference"] for claim in linked_claims}
        metric_kinds = {metric["kind"] for metric in result["specialist_metrics"]}
        if requested & {"calibrated_prediction", "clinical_utility"} and (
            not metric_kinds or metric_kinds <= {"discrimination"}
        ):
            block(
                "auc_only_cannot_support_calibration_or_utility",
                "Discrimination-only metrics are linked to calibration or utility claims.",
                "Add appropriately validated calibration/utility evidence or narrow the claim to discrimination in the evaluated setting.",
            )
        if (
            "future_setting_generalization" in requested
            and result["uncertainty"]["kind"] != "prediction_interval"
        ):
            block(
                "future_setting_claim_without_prediction_interval",
                "A future-setting meta-analytic claim lacks prediction uncertainty.",
                "Add a justified prediction interval and heterogeneity analysis or narrow the claim to the pooled target already estimated.",
            )

    for sensitivity in contract["sensitivity_analyses"]:
        primary = result_map.get(sensitivity["primary_result_id"])
        if (
            primary
            and sensitivity["claimed_as_same_estimand_robustness"]
            and sensitivity["target_estimand_id"] != primary["estimand_id"]
        ):
            block(
                "sensitivity_not_same_estimand",
                "A sensitivity result targeting a different estimand is labeled robustness of the primary estimand.",
                "Relabel it as a different target or rerun a sensitivity analysis that preserves the primary estimand.",
            )

    for surface in contract["surface_bindings"]:
        result = result_map.get(surface["result_id"])
        if not result:
            block(
                "surface_result_binding_broken",
                f"Surface {surface['surface_id']} references an unknown result {surface['result_id']}.",
                "Restore the exact result binding or remove the orphan surface; do not infer numeric authority from unbound prose, tables, or displays.",
            )
            continue
        if surface["analysis_receipt_sha256"] != result["analysis_receipt_sha256"]:
            block(
                "stale_statistical_surface_binding",
                "A manuscript surface is bound to a stale analysis receipt.",
                "Regenerate every dependent table, display, caption, and sentence from the current result receipt.",
            )
        if surface["reported_interval_kind"] != result["uncertainty"]["kind"]:
            block(
                "surface_interval_semantics_mismatch",
                "A surface changes the recorded interval kind.",
                "Correct the label and interpretation; confidence, credible, prediction, bootstrap, and compatibility intervals are not interchangeable.",
            )
        tolerance = surface["rounding"]["absolute_tolerance"]
        expected_p = result["test"]["p_value"] if result["test"] else None
        pairs = [
            (surface["reported_estimate"], result["estimate"]["value"]),
            (surface["reported_lower"], result["uncertainty"]["lower"]),
            (surface["reported_upper"], result["uncertainty"]["upper"]),
            (surface["reported_interval_level"], result["uncertainty"]["level"]),
        ]
        numeric_mismatch = any(
            abs(observed - expected) > tolerance for observed, expected in pairs
        )
        if surface["reported_n"] != result["independent_n"]:
            numeric_mismatch = True
        reported_p = surface["reported_p_value"]
        if (reported_p is None) != (expected_p is None):
            numeric_mismatch = True
        elif reported_p is not None and expected_p is not None:
            numeric_mismatch = (
                numeric_mismatch or abs(reported_p - expected_p) > tolerance
            )
        if numeric_mismatch:
            block(
                "surface_numeric_mismatch",
                "A table, display, caption, or sentence drifts from the bound result beyond declared rounding tolerance.",
                "Regenerate or correct every surface from the authoritative result and current receipt.",
            )

    policy_resolution = contract["exact_policy_resolution"]
    if policy_resolution["policy_as_of_date"] != contract["as_of_date"]:
        block(
            "policy_as_of_date_mismatch",
            "Exact-policy resolution used a different as-of date from the contract.",
            "Resolve exact domain, regulator, and venue policies for the contract as-of date.",
        )
    as_of = date.fromisoformat(contract["as_of_date"])
    for policy in policy_resolution["policies"]:
        if policy["resolution_status"] == "resolved" and not policy["source_url"]:
            block(
                "resolved_analysis_policy_source_missing",
                f"Resolved policy {policy['policy_id']} lacks official-source provenance.",
                "Attach the official source URL or return the policy to unresolved status.",
            )
        if (
            policy["applicability"] == "required"
            and policy["resolution_status"] != "resolved"
        ):
            require_research(
                "required_exact_analysis_policy_unresolved",
                f"Required exact policy {policy['policy_id']} remains unresolved.",
                "Read the current official source, record applicability and effective dates, or preserve the unresolved state.",
            )
        if (
            policy["effective_from"]
            and date.fromisoformat(policy["effective_from"]) > as_of
        ):
            require_research(
                "future_effective_analysis_policy",
                f"Policy {policy['policy_id']} is future-effective and cannot be backcast.",
                "Use the policy effective on the as-of date and record the future policy separately.",
            )
        if (
            policy["effective_until"]
            and date.fromisoformat(policy["effective_until"]) < as_of
        ):
            require_research(
                "expired_analysis_policy",
                f"Policy {policy['policy_id']} expired before the as-of date.",
                "Resolve the superseding official policy without erasing the historical record.",
            )
        if (
            policy["effective_from"] is None
            and policy["effective_date_basis"] == "observed_active_not_backcastable"
            and date.fromisoformat(policy["reviewed_at"]) > as_of
        ):
            require_research(
                "historical_analysis_policy_not_backcastable",
                f"Current observation of {policy['policy_id']} cannot establish its historical effect.",
                "Locate a dated archived official source or preserve the historical policy as unresolved.",
            )

    visible_deviations = _unique(
        deviation["classification"]
        for deviation in contract["deviations"]
        if deviation["status"] == "disclosed"
    )
    return _result(blockers, unresolved, warnings, resolved, visible_deviations, True)


def _result(
    blockers: list[dict[str, str]],
    unresolved: list[dict[str, str]],
    warnings: list[str],
    resolved: dict[str, Any],
    visible_deviations: list[str],
    schema_valid: bool,
) -> dict[str, Any]:
    status = "blocked" if blockers else "unresolved" if unresolved else "pass"
    routes = _unique(
        item["route"] for item in [*blockers, *unresolved] if item.get("route")
    )
    return {
        "status": status,
        "blockers": blockers,
        "blocker_codes": [item["code"] for item in blockers],
        "unresolved_research": unresolved,
        "unresolved_codes": [item["code"] for item in unresolved],
        "repair_routes": routes,
        "warnings": warnings,
        "visible_deviation_classes": visible_deviations,
        "selection_mode": resolved.get(
            "selection_mode", "applicable_obligations_not_universal_method"
        ),
        "matched_adapter_ids": resolved.get("matched_adapter_ids", []),
        "obligations": resolved.get("obligations", []),
        "hard_checks": resolved.get("hard_checks", []),
        "source_refs": resolved.get("source_refs", []),
        "transfer_limits": resolved.get("transfer_limits", []),
        "certification": _certification(schema_valid, bool(blockers)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path)
    parser.add_argument("--adapters", type=Path, default=DEFAULT_ADAPTERS)
    args = parser.parse_args()
    catalog = load_adapter_catalog(args.adapters)
    contract = json.loads(args.contract.read_text(encoding="utf-8"))
    print(json.dumps(evaluate_statistical_contract(contract, catalog), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
