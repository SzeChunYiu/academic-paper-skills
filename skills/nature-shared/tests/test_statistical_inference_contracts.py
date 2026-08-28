from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
CONTRACT_ROOT = SHARED / "analysis-contracts"
SCHEMA_PATH = CONTRACT_ROOT / "statistical-inference-uncertainty-contract.schema.json"
ADAPTERS_PATH = CONTRACT_ROOT / "maintained-analysis-adapters.json"
REGISTRY_PATH = CONTRACT_ROOT / "statistical-inference-evidence-registry.json"
RESOLVER_PATH = SHARED / "scripts" / "resolve_statistical_inference.py"
SEARCH_LOG_PATH = (
    SHARED / "research" / "statistical-inference-uncertainty-search-log-2026-08-28.json"
)
FIXTURE_PATH = (
    Path(__file__).parent
    / "fixtures"
    / "statistical-inference"
    / "valid-randomized.json"
)


def fixture() -> dict:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def load_resolver():
    spec = importlib.util.spec_from_file_location(
        "resolve_statistical_inference", RESOLVER_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import resolver from {RESOLVER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class StatisticalInferenceContractTests(unittest.TestCase):
    def setUp(self) -> None:
        required = [SCHEMA_PATH, ADAPTERS_PATH, REGISTRY_PATH, RESOLVER_PATH]
        if self._testMethodName == "test_required_contract_artifacts_exist":
            return
        if not all(path.exists() for path in required):
            self.skipTest(
                "statistical inference implementation artifacts not present yet"
            )
        self.resolver = load_resolver()
        self.adapters = self.resolver.load_adapter_catalog(ADAPTERS_PATH)

    def evaluate(self, contract: dict) -> dict:
        return self.resolver.evaluate_statistical_contract(contract, self.adapters)

    def result_by_code(self, evaluated: dict, code: str) -> dict:
        return next(item for item in evaluated["blockers"] if item["code"] == code)

    def test_required_contract_artifacts_exist(self) -> None:
        for path in (SCHEMA_PATH, ADAPTERS_PATH, REGISTRY_PATH, RESOLVER_PATH):
            self.assertTrue(path.exists(), path)

    def test_registry_has_substantial_reconciled_non_universal_evidence(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        search_log = json.loads(SEARCH_LOG_PATH.read_text(encoding="utf-8"))
        sources = registry["sources"]
        source_ids = {source["source_id"] for source in sources}
        self.assertGreaterEqual(len(sources), 40)
        self.assertGreaterEqual(
            sum(source["read_depth"] == "full_text" for source in sources), 24
        )
        self.assertGreaterEqual(
            sum(
                source["source_type"]
                in {"official_guideline", "official_policy", "technical_standard"}
                for source in sources
            ),
            7,
        )
        self.assertGreaterEqual(registry["search_protocol"]["queries_executed"], 12)
        self.assertGreaterEqual(registry["search_protocol"]["records_screened"], 100)
        self.assertEqual(
            registry["search_protocol"]["records_screened"],
            sum(len(query["records"]) for query in search_log["queries"]),
        )
        self.assertGreaterEqual(len(self.adapters["profiles"]), 10)
        for profile in self.adapters["profiles"]:
            self.assertTrue(profile["profile_is_not_universal_rule"])
            self.assertGreaterEqual(len(profile["source_refs"]), 2)
            self.assertTrue(set(profile["source_refs"]).issubset(source_ids))
            self.assertTrue(profile["transfer_limits"])
        for source in sources:
            for field in (
                "source_type",
                "read_depth",
                "supports",
                "limits",
                "url",
                "accessed_at",
                "metadata_verification",
            ):
                self.assertTrue(source.get(field), (source.get("source_id"), field))

    def test_valid_randomized_contract_passes_only_bounded_checks(self) -> None:
        result = self.evaluate(fixture())
        self.assertEqual("pass", result["status"])
        self.assertEqual([], result["blockers"])
        self.assertEqual(
            {
                "general-estimation-reporting",
                "randomized-intervention",
                "hierarchical-repeated-clustered",
            },
            set(result["matched_adapter_ids"]),
        )
        self.assertNotIn("scientifically_valid", result)
        self.assertNotIn("accepted", result)

    def test_malformed_contract_blocks_before_semantic_evaluation(self) -> None:
        contract = fixture()
        contract["units_and_dependence"]["independent_unit_count"] = "one hundred"
        result = self.evaluate(contract)
        self.assertEqual("blocked", result["status"])
        self.assertEqual(["schema_validation_error"], result["blocker_codes"])

    def test_resolver_returns_obligations_not_a_universal_best_method(self) -> None:
        result = self.resolver.resolve_analysis_adapters(
            analysis_families=["bayesian_model"],
            study_archetypes=["observational_association"],
            design_tags=["hierarchical"],
            inference_modes=["estimation"],
            adapters=self.adapters,
        )
        self.assertEqual(
            "applicable_obligations_not_universal_method", result["selection_mode"]
        )
        self.assertIn("bayesian-analysis", result["matched_adapter_ids"])
        self.assertIn("hierarchical-repeated-clustered", result["matched_adapter_ids"])
        self.assertNotIn("best_test", result)
        self.assertNotIn("best_model", result)

    def test_unknown_analysis_family_requires_live_domain_research(self) -> None:
        contract = fixture()
        contract["analysis_context"] = {
            "study_archetypes": ["hybrid_unknown"],
            "analysis_families": ["domain_specific_unknown"],
            "design_tags": ["domain_specific_unknown"],
            "inference_modes": ["domain_specific_unknown"],
        }
        contract["source_provenance"]["resolved_adapter_ids"] = []
        result = self.evaluate(contract)
        self.assertEqual("unresolved", result["status"])
        self.assertIn("unmatched_analysis_domain", result["unresolved_codes"])
        self.assertNotIn("universal_fallback", result["matched_adapter_ids"])

    def test_declared_adapter_provenance_must_match_live_resolution(self) -> None:
        contract = fixture()
        contract["source_provenance"]["resolved_adapter_ids"] = [
            "general-estimation-reporting"
        ]
        result = self.evaluate(contract)
        self.assertIn("resolved_adapter_provenance_mismatch", result["blocker_codes"])

    def test_contract_catalog_identity_must_match_loaded_catalog(self) -> None:
        contract = fixture()
        contract["source_provenance"]["adapter_catalog_id"] = "invented-catalog"
        result = self.evaluate(contract)
        self.assertIn("adapter_catalog_identity_mismatch", result["blocker_codes"])

    def test_analysis_input_hash_must_match_data_snapshot(self) -> None:
        contract = fixture()
        contract["analysis_executions"][0]["input_snapshot_sha256"] = "f" * 64
        result = self.evaluate(contract)
        self.assertIn("analysis_input_snapshot_mismatch", result["blocker_codes"])

    def test_result_identities_must_be_unique(self) -> None:
        contract = fixture()
        contract["results"].append(copy.deepcopy(contract["results"][0]))
        result = self.evaluate(contract)
        self.assertIn("duplicate_result_identity", result["blocker_codes"])

    def test_subsamples_cannot_be_reported_as_independent_n(self) -> None:
        contract = fixture()
        contract["units_and_dependence"]["reported_n"] = 200
        contract["results"][0]["independent_n"] = 200
        result = self.evaluate(contract)
        self.assertIn("subsample_as_independent_n", result["blocker_codes"])
        self.assertIn(
            "narrow",
            self.result_by_code(result, "subsample_as_independent_n")["route"].lower(),
        )

    def test_declared_dependence_cannot_be_ignored(self) -> None:
        contract = fixture()
        contract["units_and_dependence"]["dependence_handling"] = {
            "status": "ignored",
            "method": "none",
            "receipt": "",
        }
        result = self.evaluate(contract)
        self.assertIn("dependence_structure_unhandled", result["blocker_codes"])

    def test_plan_execution_estimator_change_requires_visible_deviation(self) -> None:
        contract = fixture()
        contract["analysis_executions"][0]["estimator"] = (
            "unplanned complete-case t test"
        )
        result = self.evaluate(contract)
        self.assertIn("analysis_plan_execution_mismatch", result["blocker_codes"])
        contract["deviations"].append(
            {
                "deviation_id": "deviation:method-1",
                "classification": "analysis_method_change",
                "from_object_id": "sap:trial-001-v1",
                "to_object_id": "analysis:primary-v1",
                "detected_at": "2026-06-01T11:00:00Z",
                "reason": "Prespecified model could not be fitted.",
                "consequence": "Analysis is exploratory and claim is narrowed.",
                "affected_result_ids": ["result:primary-effect"],
                "affected_claim_ids": ["claim:primary-effect"],
                "status": "disclosed",
            }
        )
        contract["results"][0]["selection_status"] = "deviation"
        contract["claim_links"][0]["state"] = "inconclusive"
        result = self.evaluate(contract)
        self.assertNotIn("analysis_plan_execution_mismatch", result["blocker_codes"])
        self.assertIn("analysis_method_change", result["visible_deviation_classes"])

    def test_unrelated_deviation_cannot_repair_analysis_method_drift(self) -> None:
        contract = fixture()
        contract["analysis_executions"][0]["estimator"] = "unplanned t test"
        contract["deviations"].append(
            {
                "deviation_id": "deviation:unrelated",
                "classification": "analysis_method_change",
                "from_object_id": "analysis-plan:other",
                "to_object_id": "analysis:other",
                "detected_at": "2026-06-01T11:00:00Z",
                "reason": "Another analysis changed.",
                "consequence": "No consequence for the primary analysis.",
                "affected_result_ids": ["result:other"],
                "affected_claim_ids": ["claim:other"],
                "status": "disclosed",
            }
        )
        result = self.evaluate(contract)
        self.assertIn("analysis_plan_execution_mismatch", result["blocker_codes"])

    def test_missing_data_strategy_change_requires_visible_deviation(self) -> None:
        contract = fixture()
        contract["analysis_executions"][0]["missing_data_strategy"] = "complete_case"
        result = self.evaluate(contract)
        self.assertIn("missing_data_plan_execution_mismatch", result["blocker_codes"])

    def test_confirmatory_multiplicity_family_cannot_be_silently_unaccounted(
        self,
    ) -> None:
        contract = fixture()
        multiplicity = contract["analysis_plans"][0]["multiplicity"]
        multiplicity["applicability"] = "required"
        multiplicity["planned_hypothesis_ids"] = [
            "hypothesis:primary",
            "hypothesis:secondary",
        ]
        multiplicity["executed_hypothesis_ids"] = [
            "hypothesis:primary",
            "hypothesis:secondary",
        ]
        multiplicity["method"] = "none"
        multiplicity["receipt"] = ""
        result = self.evaluate(contract)
        self.assertIn("confirmatory_multiplicity_unresolved", result["blocker_codes"])

    def test_exploratory_family_can_remain_uncorrected_if_transparent(self) -> None:
        contract = fixture()
        contract["analysis_plans"][0]["classification"] = "exploratory"
        contract["results"][0]["selection_status"] = "exploratory"
        contract["claim_links"][0]["state"] = "descriptive_only"
        multiplicity = contract["analysis_plans"][0]["multiplicity"]
        multiplicity["applicability"] = "exploratory_no_confirmatory_error_control"
        multiplicity["planned_hypothesis_ids"] = []
        multiplicity["executed_hypothesis_ids"] = [
            "hypothesis:primary",
            "hypothesis:secondary",
        ]
        multiplicity["method"] = "none_exploratory"
        multiplicity["receipt"] = "receipt:exploratory-family-v1"
        result = self.evaluate(contract)
        self.assertNotIn(
            "confirmatory_multiplicity_unresolved", result["blocker_codes"]
        )

    def test_observed_power_cannot_be_used_as_evidence_after_results(self) -> None:
        contract = fixture()
        contract["analysis_plans"][0]["sample_size"][
            "observed_power_used_for_inference"
        ] = True
        result = self.evaluate(contract)
        self.assertIn(
            "post_hoc_observed_power_used_as_evidence", result["blocker_codes"]
        )

    def test_nonconverged_model_blocks_model_based_claim(self) -> None:
        contract = fixture()
        contract["analysis_executions"][0]["convergence_status"] = "failed"
        result = self.evaluate(contract)
        self.assertIn("analysis_nonconvergence", result["blocker_codes"])
        route = self.result_by_code(result, "analysis_nonconvergence")["route"].lower()
        self.assertIn("rerun", route)
        self.assertIn("narrow", route)

    def test_final_required_diagnostic_needs_a_receipt(self) -> None:
        contract = fixture()
        contract["analysis_executions"][0]["diagnostics"][0]["receipt"] = ""
        result = self.evaluate(contract)
        self.assertIn("diagnostic_receipt_missing", result["blocker_codes"])

    def test_separate_significance_tests_do_not_establish_group_difference(
        self,
    ) -> None:
        contract = fixture()
        contract["results"][0]["decision"]["comparison_basis"] = (
            "separate_significance_tests"
        )
        contract["claim_links"][0]["comparison_basis"] = "separate_significance_tests"
        result = self.evaluate(contract)
        self.assertIn(
            "difference_in_significance_is_not_significant_difference",
            result["blocker_codes"],
        )

    def test_nonsignificant_p_value_cannot_establish_no_effect(self) -> None:
        contract = fixture()
        result_record = contract["results"][0]
        result_record["test"]["p_value"] = 0.21
        result_record["decision"].update(
            {
                "objective": "no_meaningful_effect",
                "state": "supported",
                "comparison_basis": "direct_contrast",
            }
        )
        contract["claim_links"][0].update(
            {"requested_inference": "no_meaningful_effect", "state": "supported"}
        )
        result = self.evaluate(contract)
        self.assertIn("absence_from_nonsignificance", result["blocker_codes"])

    def test_equivalence_with_justified_margin_and_interval_can_pass(self) -> None:
        contract = fixture()
        result_record = contract["results"][0]
        result_record["estimate"]["value"] = 0.1
        result_record["uncertainty"]["lower"] = -0.3
        result_record["uncertainty"]["upper"] = 0.4
        result_record["test"]["p_value"] = 0.01
        result_record["decision"] = {
            "objective": "equivalence",
            "state": "supported",
            "comparison_basis": "direct_contrast",
            "margin": 0.5,
            "margin_unit": "points",
            "margin_provenance": "prespecified domain-justified SESOI",
        }
        contract["claim_links"][0].update(
            {"requested_inference": "no_meaningful_effect", "state": "supported"}
        )
        for surface in contract["surface_bindings"]:
            surface["reported_estimate"] = 0.1
            surface["reported_lower"] = -0.3
            surface["reported_upper"] = 0.4
            surface["reported_p_value"] = 0.01
        result = self.evaluate(contract)
        self.assertNotIn("absence_from_nonsignificance", result["blocker_codes"])
        self.assertNotIn(
            "equivalence_margin_missing_or_crossed", result["blocker_codes"]
        )

    def test_equivalence_interval_crossing_margin_is_inconclusive(self) -> None:
        contract = fixture()
        result_record = contract["results"][0]
        result_record["uncertainty"]["lower"] = -0.7
        result_record["uncertainty"]["upper"] = 0.4
        result_record["decision"] = {
            "objective": "equivalence",
            "state": "supported",
            "comparison_basis": "direct_contrast",
            "margin": 0.5,
            "margin_unit": "points",
            "margin_provenance": "prespecified domain-justified SESOI",
        }
        contract["claim_links"][0].update(
            {"requested_inference": "no_meaningful_effect", "state": "supported"}
        )
        for surface in contract["surface_bindings"]:
            surface["reported_lower"] = -0.7
            surface["reported_upper"] = 0.4
        result = self.evaluate(contract)
        self.assertIn("equivalence_margin_missing_or_crossed", result["blocker_codes"])

    def test_interval_semantics_are_not_interchangeable_across_surfaces(self) -> None:
        contract = fixture()
        contract["surface_bindings"][2]["reported_interval_kind"] = (
            "prediction_interval"
        )
        result = self.evaluate(contract)
        self.assertIn("surface_interval_semantics_mismatch", result["blocker_codes"])

    def test_surface_numeric_drift_is_blocking_beyond_declared_tolerance(self) -> None:
        contract = fixture()
        contract["surface_bindings"][1]["reported_estimate"] = -1.4
        result = self.evaluate(contract)
        self.assertIn("surface_numeric_mismatch", result["blocker_codes"])

    def test_rounding_within_declared_tolerance_can_pass(self) -> None:
        contract = fixture()
        contract["surface_bindings"][1]["reported_estimate"] = -2.399
        result = self.evaluate(contract)
        self.assertNotIn("surface_numeric_mismatch", result["blocker_codes"])

    def test_surface_binding_must_use_current_analysis_receipt(self) -> None:
        contract = fixture()
        contract["surface_bindings"][0]["analysis_receipt_sha256"] = "e" * 64
        result = self.evaluate(contract)
        self.assertIn("stale_statistical_surface_binding", result["blocker_codes"])

    def test_primary_adverse_or_null_result_cannot_be_hidden(self) -> None:
        contract = fixture()
        contract["analysis_plans"][0]["primary_result_ids"].append(
            "result:null-primary"
        )
        result = self.evaluate(contract)
        self.assertIn("planned_primary_result_missing", result["blocker_codes"])
        self.assertIn(
            "narrow",
            self.result_by_code(result, "planned_primary_result_missing")[
                "route"
            ].lower(),
        )

    def test_sensitivity_analysis_must_target_same_estimand_for_robustness_claim(
        self,
    ) -> None:
        contract = fixture()
        contract["sensitivity_analyses"].append(
            {
                "sensitivity_id": "sensitivity:other-target",
                "primary_result_id": "result:primary-effect",
                "target_estimand_id": "estimand:different",
                "assumption_varied": "missingness",
                "scenario": "MNAR delta shift",
                "plausibility_basis": "domain range",
                "result_id": "result:sensitivity-other",
                "receipt": "receipt:sensitivity-v1",
                "decision_changed": False,
                "claimed_as_same_estimand_robustness": True,
            }
        )
        result = self.evaluate(contract)
        self.assertIn("sensitivity_not_same_estimand", result["blocker_codes"])

    def test_auc_only_cannot_support_calibration_or_utility_claim(self) -> None:
        contract = fixture()
        contract["results"][0]["specialist_metrics"] = [
            {
                "metric_id": "metric:auc",
                "kind": "discrimination",
                "name": "area_under_roc_curve",
                "value": 0.82,
                "uncertainty_interval_id": "interval:primary-95ci",
                "receipt": "receipt:auc-v1",
            }
        ]
        contract["claim_links"][0]["requested_inference"] = "calibrated_prediction"
        result = self.evaluate(contract)
        self.assertIn(
            "auc_only_cannot_support_calibration_or_utility", result["blocker_codes"]
        )

    def test_future_setting_meta_claim_requires_prediction_interval(self) -> None:
        contract = fixture()
        contract["claim_links"][0]["requested_inference"] = (
            "future_setting_generalization"
        )
        result = self.evaluate(contract)
        self.assertIn(
            "future_setting_claim_without_prediction_interval", result["blocker_codes"]
        )

    def test_bayesian_result_does_not_require_p_value_or_frequentist_interval(
        self,
    ) -> None:
        contract = fixture()
        contract["analysis_context"]["study_archetypes"] = ["hybrid_quantitative"]
        contract["analysis_context"]["analysis_families"] = ["bayesian_model"]
        contract["analysis_context"]["design_tags"] = ["hierarchical"]
        contract["analysis_context"]["inference_modes"] = ["estimation"]
        contract["source_provenance"]["resolved_adapter_ids"] = [
            "bayesian-analysis",
            "hierarchical-repeated-clustered",
        ]
        contract["analysis_plans"][0]["analysis_family"] = "bayesian_model"
        contract["analysis_plans"][0]["estimator"] = "posterior mean contrast"
        contract["analysis_plans"][0]["model"] = "Bayesian hierarchical model"
        contract["analysis_executions"][0]["estimator"] = "posterior mean contrast"
        contract["analysis_executions"][0]["model"] = "Bayesian hierarchical model"
        contract["analysis_executions"][0]["diagnostics"][0]["dimension"] = (
            "mcmc_convergence_and_posterior_predictive_fit"
        )
        result_record = contract["results"][0]
        result_record["uncertainty"]["kind"] = "credible_interval"
        result_record["test"] = None
        for surface in contract["surface_bindings"]:
            surface["reported_interval_kind"] = "credible_interval"
            surface["reported_p_value"] = None
        result = self.evaluate(contract)
        self.assertNotIn("p_value_required", result["blocker_codes"])
        self.assertNotIn("surface_interval_semantics_mismatch", result["blocker_codes"])

    def test_nonquantitative_boundary_does_not_invent_statistics(self) -> None:
        result = self.resolver.resolve_analysis_adapters(
            analysis_families=["nonquantitative_interpretive"],
            study_archetypes=["qualitative_interpretive"],
            design_tags=["interviews"],
            inference_modes=["interpretive"],
            adapters=self.adapters,
        )
        self.assertIn(
            "qualitative-nonquantitative-boundary", result["matched_adapter_ids"]
        )
        self.assertIn("Do not fabricate", " ".join(result["obligations"]))
        self.assertNotIn("p_value_required", result["hard_checks"])

    def test_required_exact_policy_can_remain_explicitly_unresolved(self) -> None:
        contract = fixture()
        policy = contract["exact_policy_resolution"]["policies"][0]
        policy["resolution_status"] = "unresolved"
        policy["source_url"] = None
        result = self.evaluate(contract)
        self.assertEqual("unresolved", result["status"])
        self.assertIn(
            "required_exact_analysis_policy_unresolved", result["unresolved_codes"]
        )

    def test_resolved_required_policy_requires_official_source_provenance(self) -> None:
        contract = fixture()
        contract["exact_policy_resolution"]["policies"][0]["source_url"] = None
        result = self.evaluate(contract)
        self.assertIn(
            "resolved_analysis_policy_source_missing", result["blocker_codes"]
        )

    def test_exact_policy_as_of_date_must_match_contract(self) -> None:
        contract = fixture()
        contract["exact_policy_resolution"]["policy_as_of_date"] = "2026-08-27"
        result = self.evaluate(contract)
        self.assertIn("policy_as_of_date_mismatch", result["blocker_codes"])

    def test_future_effective_policy_is_not_backcast(self) -> None:
        contract = fixture()
        policy = contract["exact_policy_resolution"]["policies"][0]
        policy["effective_from"] = "2027-01-01"
        result = self.evaluate(contract)
        self.assertEqual("unresolved", result["status"])
        self.assertIn("future_effective_analysis_policy", result["unresolved_codes"])

    def test_observed_current_policy_cannot_prove_older_rule(self) -> None:
        contract = fixture()
        policy = contract["exact_policy_resolution"]["policies"][0]
        policy["effective_from"] = None
        policy["effective_date_basis"] = "observed_active_not_backcastable"
        policy["reviewed_at"] = "2026-08-28"
        contract["as_of_date"] = "2025-08-28"
        contract["exact_policy_resolution"]["policy_as_of_date"] = "2025-08-28"
        result = self.evaluate(contract)
        self.assertEqual("unresolved", result["status"])
        self.assertIn(
            "historical_analysis_policy_not_backcastable", result["unresolved_codes"]
        )

    def test_claim_narrowing_is_valid_but_cannot_create_analysis_receipt(self) -> None:
        contract = fixture()
        contract["claim_links"][0]["requested_inference"] = "no_meaningful_effect"
        contract["claim_links"][0]["state"] = "inconclusive"
        result = self.evaluate(contract)
        self.assertNotIn("absence_from_nonsignificance", result["blocker_codes"])
        contract["analysis_executions"][0]["code_receipt"] = ""
        result = self.evaluate(contract)
        self.assertIn("analysis_execution_receipt_missing", result["blocker_codes"])
        self.assertNotIn(
            "narrow the claim",
            self.result_by_code(result, "analysis_execution_receipt_missing")[
                "route"
            ].lower(),
        )

    def test_certification_explicitly_excludes_validity_truth_and_acceptance(
        self,
    ) -> None:
        result = self.evaluate(fixture())
        exclusions = set(result["certification"]["does_not_certify"])
        self.assertTrue(
            {
                "model_adequacy_or_assumption_truth",
                "causal_identification",
                "absence_of_bias",
                "adequate_power_or_precision",
                "external_validity_or_generalization",
                "scientific_truth",
                "journal_acceptance",
            }.issubset(exclusions)
        )

    def test_canonical_skills_statistics_and_project_state_load_analysis_layer(
        self,
    ) -> None:
        writing = (SHARED.parent / "academic-writing" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        pipeline = (SHARED.parent / "academic-paper-pipeline" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        statistics = (SHARED.parent / "nature-statistics" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        writing_manifest = (
            SHARED.parent / "academic-writing" / "manifest.yaml"
        ).read_text(encoding="utf-8")
        pipeline_manifest = (
            SHARED.parent / "academic-paper-pipeline" / "manifest.yaml"
        ).read_text(encoding="utf-8")
        statistics_manifest = (
            SHARED.parent / "nature-statistics" / "manifest.yaml"
        ).read_text(encoding="utf-8")
        state = (
            SHARED.parents[1] / "docs" / "academic-paper-project-state.template.yaml"
        ).read_text(encoding="utf-8")
        for text in (
            writing,
            pipeline,
            statistics,
            writing_manifest,
            pipeline_manifest,
            statistics_manifest,
        ):
            self.assertIn("statistical-inference-uncertainty-contract.md", text)
        self.assertIn("statistical_inference_contract:", state)
        self.assertIn("statistical_inference_contract_status:", state)
        self.assertIn("statistical_result_bindings:", state)
        self.assertIn("future_effective_analysis_policy", state)


if __name__ == "__main__":
    unittest.main()
