from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
CONTRACT_ROOT = SHARED / "study-contracts"
SCHEMA_PATH = CONTRACT_ROOT / "study-protocol-conduct-contract.schema.json"
ADAPTERS_PATH = CONTRACT_ROOT / "maintained-study-adapters.json"
REGISTRY_PATH = CONTRACT_ROOT / "study-protocol-evidence-registry.json"
RESOLVER_PATH = SHARED / "scripts" / "resolve_study_protocol.py"
FIXTURE_PATH = (
    Path(__file__).parent
    / "fixtures"
    / "study-protocols"
    / "randomized-valid.json"
)


def fixture() -> dict:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def load_resolver():
    spec = importlib.util.spec_from_file_location("resolve_study_protocol", RESOLVER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import resolver from {RESOLVER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class StudyProtocolContractTests(unittest.TestCase):
    def setUp(self) -> None:
        required = [SCHEMA_PATH, ADAPTERS_PATH, REGISTRY_PATH, RESOLVER_PATH]
        if self._testMethodName == "test_required_contract_artifacts_exist":
            return
        if not all(path.exists() for path in required):
            self.skipTest("study protocol/conduct implementation artifacts not present yet")
        self.resolver = load_resolver()
        self.adapters = self.resolver.load_adapter_catalog(ADAPTERS_PATH)

    def test_required_contract_artifacts_exist(self) -> None:
        for path in (SCHEMA_PATH, ADAPTERS_PATH, REGISTRY_PATH, RESOLVER_PATH):
            self.assertTrue(path.exists(), path)

    def evaluate(self, contract: dict) -> dict:
        return self.resolver.evaluate_study_contract(contract, self.adapters)

    def test_valid_randomized_contract_passes_bounded_checks(self) -> None:
        result = self.evaluate(fixture())
        self.assertEqual("pass", result["status"])
        self.assertEqual([], result["blockers"])
        self.assertIn("randomized-intervention", result["matched_adapter_ids"])
        self.assertNotIn("scientifically_valid", result)
        self.assertNotIn("accepted", result)

    def test_invalid_timestamp_fails_closed_without_crashing(self) -> None:
        contract = fixture()
        contract["protocol"]["frozen_at"] = "not-a-date"
        result = self.evaluate(contract)
        self.assertEqual("blocked", result["status"])
        self.assertIn("schema_validation_error", result["blocker_codes"])

    def test_non_string_timestamp_fails_closed_without_crashing(self) -> None:
        contract = fixture()
        contract["protocol"]["frozen_at"] = 123
        result = self.evaluate(contract)
        self.assertEqual("blocked", result["status"])
        self.assertIn("schema_validation_error", result["blocker_codes"])

    def test_timezone_free_timestamp_fails_closed_without_crashing(self) -> None:
        contract = fixture()
        contract["protocol"]["frozen_at"] = "2026-01-10T09:00:00"
        result = self.evaluate(contract)
        self.assertEqual("blocked", result["status"])
        self.assertIn("schema_validation_error", result["blocker_codes"])

    def test_structural_type_error_blocks_before_semantic_arithmetic(self) -> None:
        contract = fixture()
        contract["conduct"]["stopping"]["realized"] = None
        result = self.evaluate(contract)
        self.assertEqual("blocked", result["status"])
        self.assertEqual(["schema_validation_error"], result["blocker_codes"])

    def test_invalid_adapter_inputs_fail_closed_before_resolution(self) -> None:
        contract = fixture()
        contract["design_tags"] = None
        result = self.evaluate(contract)
        self.assertEqual("blocked", result["status"])
        self.assertEqual(["schema_validation_error"], result["blocker_codes"])

    def test_catalog_has_substantial_auditable_non_universal_evidence(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        search_log = json.loads(
            (
                SHARED
                / "research"
                / "study-protocol-conduct-search-log-2026-08-28.json"
            ).read_text(encoding="utf-8")
        )
        sources = registry["sources"]
        source_ids = {source["source_id"] for source in sources}
        self.assertGreaterEqual(len(sources), 30)
        self.assertGreaterEqual(registry["search_protocol"]["records_screened"], 80)
        self.assertEqual(
            registry["search_protocol"]["records_screened"],
            sum(len(query["records"]) for query in search_log["queries"]),
        )
        self.assertGreaterEqual(len(self.adapters["profiles"]), 8)
        for profile in self.adapters["profiles"]:
            self.assertTrue(profile["profile_is_not_universal_rule"])
            self.assertGreaterEqual(len(profile["source_refs"]), 2)
            self.assertTrue(set(profile["source_refs"]).issubset(source_ids))
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

    def test_resolver_returns_obligations_not_a_universal_design(self) -> None:
        result = self.resolver.resolve_study_adapter(
            study_archetype="qualitative_interpretive",
            design_tags=["interviews"],
            adapters=self.adapters,
        )
        self.assertEqual("applicable_obligations_not_universal_design", result["selection_mode"])
        self.assertIn("qualitative-interpretive", result["matched_adapter_ids"])
        self.assertNotIn("best_design", result)
        self.assertFalse(any("registration is universally required" in x for x in result["obligations"]))

    def test_false_prospective_status_is_blocking(self) -> None:
        contract = fixture()
        contract["protocol"]["frozen_at"] = "2026-03-10T09:00:00Z"
        result = self.evaluate(contract)
        self.assertIn("false_prospective_status", result["blocker_codes"])

    def test_undisclosed_primary_outcome_change_is_blocking(self) -> None:
        contract = fixture()
        contract["analysis_execution"]["reported_primary_outcome_ids"] = [
            "outcome:secondary"
        ]
        result = self.evaluate(contract)
        self.assertIn("undisclosed_primary_outcome_change", result["blocker_codes"])

    def test_documented_outcome_deviation_is_visible_not_erased(self) -> None:
        contract = fixture()
        contract["analysis_execution"]["reported_primary_outcome_ids"] = [
            "outcome:secondary"
        ]
        contract["deviations"].append(
            {
                "deviation_id": "deviation:outcome-001",
                "from_object_id": "outcome:primary",
                "detected_at": "2026-06-02T09:00:00Z",
                "description": "Primary instrument failed; secondary outcome analyzed instead.",
                "reason": "Instrument failure",
                "classification": "outcome_change",
                "affected_claim_ids": ["claim:primary-001"],
                "inference_consequence": "Original confirmatory claim is not retained.",
                "disclosure_locations": ["methods", "results", "limitations"],
                "status": "disclosed"
            }
        )
        contract["claims"][0]["evidential_status"] = "deviation"
        result = self.evaluate(contract)
        self.assertNotIn("undisclosed_primary_outcome_change", result["blocker_codes"])
        self.assertIn("outcome_change", result["visible_deviation_classes"])

    def test_randomized_assignment_must_be_executed_not_merely_planned(self) -> None:
        contract = fixture()
        contract["conduct"]["assignment"]["sequence_receipt"] = ""
        contract["conduct"]["assignment"]["execution_verified"] = False
        result = self.evaluate(contract)
        self.assertIn("randomization_execution_unverified", result["blocker_codes"])

    def test_hidden_blinding_change_is_blocking(self) -> None:
        contract = fixture()
        contract["conduct"]["blinding"]["executed_roles"] = []
        result = self.evaluate(contract)
        self.assertIn("undisclosed_blinding_deviation", result["blocker_codes"])

    def test_unlogged_stopping_change_is_blocking(self) -> None:
        contract = fixture()
        contract["conduct"]["stopping"]["realized"] = 120
        contract["conduct"]["stopping"]["rule_changed"] = True
        result = self.evaluate(contract)
        self.assertIn("stopping_rule_deviation_undisclosed", result["blocker_codes"])

    def test_exclusion_and_analysis_counts_must_reconcile(self) -> None:
        contract = fixture()
        contract["conduct"]["enrollment"]["analyzed"] = 97
        contract["analysis_execution"]["sample_size_analyzed"] = 97
        result = self.evaluate(contract)
        self.assertIn("exclusion_lineage_incomplete", result["blocker_codes"])

    def test_adverse_events_cannot_be_silently_omitted(self) -> None:
        contract = fixture()
        contract["conduct"]["adverse_events"]["observed_count"] = 4
        result = self.evaluate(contract)
        self.assertIn("adverse_event_omission", result["blocker_codes"])

    def test_computational_evaluation_leakage_is_blocking(self) -> None:
        contract = fixture()
        contract["study_archetype"] = "computational_ml"
        contract["design_tags"] = ["supervised_learning", "benchmark"]
        contract["conduct"]["assignment"]["required"] = False
        contract["analysis_plan"]["data_split"] = {
            "applicability": "required",
            "unit_key": "participant_id",
            "overlap_detected": True,
            "preprocessing_fit_scope": "all_data"
        }
        result = self.evaluate(contract)
        self.assertIn("evaluation_leakage", result["blocker_codes"])

    def test_confirmatory_claim_requires_timing_support(self) -> None:
        contract = fixture()
        contract["data_timing"]["protocol_freeze_relation"] = "after_outcome_access"
        result = self.evaluate(contract)
        self.assertIn("confirmatory_label_not_supported", result["blocker_codes"])
        repair = next(
            item
            for item in result["repair_routes"]
            if item["code"] == "confirmatory_label_not_supported"
        )
        self.assertIn("reclassify", repair["route"])
        self.assertIn("narrow", repair["route"])
        self.assertIn("never backdate", repair["route"])

    def test_outcome_blind_existing_data_can_retain_confirmatory_status(self) -> None:
        contract = fixture()
        contract["protocol"]["frozen_at"] = "2026-02-10T09:00:00Z"
        contract["analysis_plan"]["frozen_at"] = "2026-02-11T09:00:00Z"
        contract["data_timing"]["protocol_freeze_relation"] = (
            "after_data_before_outcome_access"
        )
        result = self.evaluate(contract)
        self.assertNotIn("confirmatory_label_not_supported", result["blocker_codes"])
        self.assertNotIn("false_prospective_status", result["blocker_codes"])

    def test_outcome_blind_confirmatory_status_requires_outcome_access_receipt(self) -> None:
        contract = fixture()
        contract["protocol"]["frozen_at"] = "2026-02-10T09:00:00Z"
        contract["analysis_plan"]["frozen_at"] = "2026-02-11T09:00:00Z"
        contract["data_timing"]["protocol_freeze_relation"] = (
            "after_data_before_outcome_access"
        )
        contract["data_timing"]["outcomes_first_observed_at"] = None
        result = self.evaluate(contract)
        self.assertIn("confirmatory_label_not_supported", result["blocker_codes"])
        repair = next(
            item
            for item in result["repair_routes"]
            if item["code"] == "confirmatory_label_not_supported"
        )
        self.assertIn("verify", repair["route"].lower())
        self.assertIn("reclassify", repair["route"].lower())

    def test_exclusions_reconcile_separately_before_and_after_assignment(self) -> None:
        contract = fixture()
        contract["conduct"]["enrollment"]["planned"] = 102
        contract["conduct"]["enrollment"]["entered"] = 102
        contract["conduct"]["enrollment"]["exclusions"].extend(
            [
                {
                    "unit_id": "participant:screen-101",
                    "stage": "screening",
                    "reason": "Failed prespecified eligibility criterion."
                },
                {
                    "unit_id": "participant:screen-102",
                    "stage": "screening",
                    "reason": "Withdrew before assignment."
                }
            ]
        )
        result = self.evaluate(contract)
        self.assertNotIn("exclusion_lineage_incomplete", result["blocker_codes"])

    def test_missing_required_ethics_authority_is_not_repaired_by_prose(self) -> None:
        contract = fixture()
        contract["ethics_governance"]["status"] = "missing"
        contract["ethics_governance"]["approval_or_waiver_ids"] = []
        result = self.evaluate(contract)
        self.assertIn("required_ethics_authority_missing", result["blocker_codes"])
        repair = next(
            item
            for item in result["repair_routes"]
            if item["code"] == "required_ethics_authority_missing"
        )
        self.assertNotIn("narrow the claim", repair["route"].lower())


if __name__ == "__main__":
    unittest.main()
