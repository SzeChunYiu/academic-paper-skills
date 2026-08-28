from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
ROOT = SHARED.parents[1]
CONTRACT_ROOT = SHARED / "data-contracts"
SCHEMA_PATH = CONTRACT_ROOT / "data-integrity-stewardship-contract.schema.json"
ADAPTERS_PATH = CONTRACT_ROOT / "maintained-data-adapters.json"
REGISTRY_PATH = CONTRACT_ROOT / "data-integrity-evidence-registry.json"
RESOLVER_PATH = SHARED / "scripts" / "resolve_data_integrity.py"
SEARCH_LOG_PATH = (
    SHARED
    / "research"
    / "data-integrity-stewardship-search-log-2026-08-28.json"
)
FIXTURE_PATH = (
    Path(__file__).parent
    / "fixtures"
    / "data-integrity"
    / "valid-tabular.json"
)


def fixture() -> dict:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def load_resolver():
    spec = importlib.util.spec_from_file_location("resolve_data_integrity", RESOLVER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import resolver from {RESOLVER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DataIntegrityContractTests(unittest.TestCase):
    def setUp(self) -> None:
        required = [SCHEMA_PATH, ADAPTERS_PATH, REGISTRY_PATH, RESOLVER_PATH]
        if self._testMethodName == "test_required_contract_artifacts_exist":
            return
        if not all(path.exists() for path in required):
            self.skipTest("data integrity implementation artifacts not present yet")
        self.resolver = load_resolver()
        self.adapters = self.resolver.load_adapter_catalog(ADAPTERS_PATH)

    def evaluate(self, contract: dict) -> dict:
        return self.resolver.evaluate_data_contract(contract, self.adapters)

    def make_multi_input(self, contract: dict) -> dict:
        external = json.loads(json.dumps(contract["snapshots"][0]))
        external["snapshot_id"] = "snapshot:external"
        external["role"] = "external_reference"
        external["sha256"] = "f" * 64
        contract["snapshots"].append(external)
        contract["transformations"][1]["input_snapshot_ids"].append(
            "snapshot:external"
        )
        return contract

    def test_required_contract_artifacts_exist(self) -> None:
        for path in (SCHEMA_PATH, ADAPTERS_PATH, REGISTRY_PATH, RESOLVER_PATH):
            self.assertTrue(path.exists(), path)

    def test_registry_has_substantial_auditable_non_universal_evidence(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        search_log = json.loads(SEARCH_LOG_PATH.read_text(encoding="utf-8"))
        sources = registry["sources"]
        self.assertGreaterEqual(len(sources), 40)
        self.assertGreaterEqual(
            sum(source["read_depth"] == "full_text" for source in sources), 20
        )
        self.assertGreaterEqual(
            sum(source["read_depth"].startswith("official") for source in sources),
            10,
        )
        self.assertEqual(12, registry["search_protocol"]["queries_executed"])
        self.assertEqual(84, registry["search_protocol"]["records_screened"])
        self.assertEqual(
            84, sum(len(query["records"]) for query in search_log["queries"])
        )
        for source in sources:
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
                self.assertIn(field, source)
                self.assertNotEqual("", source[field])

    def test_valid_tabular_contract_passes_only_bounded_checks(self) -> None:
        result = self.evaluate(fixture())
        self.assertEqual("pass", result["status"])
        self.assertEqual([], result["blockers"])
        self.assertIn("general-tabular-observational", result["matched_adapter_ids"])
        self.assertIn("raw_fixity", result["hard_checks"])
        self.assertNotIn("data_accurate", result)
        self.assertNotIn("accepted", result)

    def test_malformed_contract_fails_before_semantic_evaluation(self) -> None:
        contract = fixture()
        contract["snapshots"][0]["record_count"] = "one hundred"
        contract["transformations"][0]["input_snapshot_ids"] = None
        result = self.evaluate(contract)
        self.assertEqual("blocked", result["status"])
        self.assertEqual(["schema_validation_error"], result["blocker_codes"])

    def test_unknown_modality_requires_live_domain_research(self) -> None:
        contract = fixture()
        contract["data_context"]["modalities"] = ["quantum_sensorium"]
        contract["data_context"]["study_contexts"] = ["unknown_domain"]
        contract["source_provenance"]["resolved_adapter_ids"] = []
        result = self.evaluate(contract)
        self.assertEqual("unresolved", result["status"])
        self.assertEqual([], result["matched_adapter_ids"])
        self.assertIn("unmatched_data_modality", result["unresolved_codes"])
        self.assertNotIn("best_quality", result)

    def test_declared_adapter_provenance_must_match_live_resolution(self) -> None:
        contract = fixture()
        contract["source_provenance"]["resolved_adapter_ids"] = [
            "sensor-field-instrument"
        ]
        result = self.evaluate(contract)
        self.assertIn("resolved_adapter_provenance_mismatch", result["blocker_codes"])

    def test_contract_catalog_identity_must_match_loaded_catalog(self) -> None:
        contract = fixture()
        contract["source_provenance"]["adapter_catalog_id"] = "invented-catalog"
        result = self.evaluate(contract)
        self.assertIn("adapter_catalog_identity_mismatch", result["blocker_codes"])

    def test_raw_snapshot_must_be_immutable(self) -> None:
        contract = fixture()
        contract["snapshots"][0]["immutable"] = False
        result = self.evaluate(contract)
        self.assertIn("raw_snapshot_not_immutable", result["blocker_codes"])

    def test_contract_requires_an_authoritative_origin_snapshot(self) -> None:
        contract = fixture()
        contract["snapshots"] = contract["snapshots"][1:]
        result = self.evaluate(contract)
        self.assertIn("authoritative_origin_snapshot_missing", result["blocker_codes"])

    def test_external_reference_can_be_the_origin_without_a_local_raw_file(self) -> None:
        contract = fixture()
        contract["snapshots"][0]["role"] = "external_reference"
        result = self.evaluate(contract)
        self.assertEqual("pass", result["status"])
        self.assertNotIn(
            "authoritative_origin_snapshot_missing", result["blocker_codes"]
        )

    def test_external_reference_origin_must_be_version_fixed(self) -> None:
        contract = fixture()
        contract["snapshots"][0]["role"] = "external_reference"
        contract["snapshots"][0]["immutable"] = False
        result = self.evaluate(contract)
        self.assertIn("external_reference_origin_not_fixed", result["blocker_codes"])

    def test_source_record_identities_must_be_unique(self) -> None:
        contract = fixture()
        contract["source_records"].append(dict(contract["source_records"][0]))
        result = self.evaluate(contract)
        self.assertIn("duplicate_source_record_identity", result["blocker_codes"])

    def test_broken_transformation_lineage_is_blocking(self) -> None:
        contract = fixture()
        contract["transformations"][1]["input_snapshot_ids"] = ["snapshot:missing"]
        result = self.evaluate(contract)
        self.assertIn("transformation_lineage_broken", result["blocker_codes"])

    def test_transformation_lineage_cannot_form_a_cycle(self) -> None:
        contract = fixture()
        contract["transformations"][0]["input_snapshot_ids"] = ["snapshot:analysis"]
        result = self.evaluate(contract)
        self.assertIn("transformation_lineage_cycle", result["blocker_codes"])

    def test_transformation_identities_must_be_unique(self) -> None:
        contract = fixture()
        contract["transformations"][1]["transformation_id"] = contract[
            "transformations"
        ][0]["transformation_id"]
        result = self.evaluate(contract)
        self.assertIn("duplicate_transformation_identity", result["blocker_codes"])

    def test_transformation_requires_execution_receipt(self) -> None:
        contract = fixture()
        contract["transformations"][0]["execution_receipt_id"] = None
        result = self.evaluate(contract)
        self.assertIn("transformation_execution_unverified", result["blocker_codes"])

    def test_multi_input_transformation_requires_explicit_reconciliation(self) -> None:
        contract = self.make_multi_input(fixture())
        result = self.evaluate(contract)
        self.assertIn(
            "multi_input_transformation_reconciliation_missing",
            result["blocker_codes"],
        )

    def test_multi_input_transformation_checks_every_input_for_semantic_drift(self) -> None:
        contract = self.make_multi_input(fixture())
        contract["snapshots"][-1]["fields"][2]["unit"] = "percentile"
        contract["transformations"][1]["multi_input_reconciliation"] = {
            "combination_rule": "keyed_join",
            "expected_output_record_count": 100,
            "receipt_id": "receipt:multi-input-reconciliation",
            "field_conflict_policy_recorded": True,
        }
        result = self.evaluate(contract)
        self.assertIn("semantic_schema_drift_unlogged", result["blocker_codes"])

    def test_multi_input_removals_require_unit_level_decisions(self) -> None:
        contract = self.make_multi_input(fixture())
        contract["snapshots"][2]["record_count"] = 99
        transformation = contract["transformations"][1]
        transformation["records_removed"] = 1
        transformation["multi_input_reconciliation"] = {
            "combination_rule": "keyed_join",
            "expected_output_record_count": 99,
            "receipt_id": "receipt:multi-input-reconciliation",
            "field_conflict_policy_recorded": True,
        }
        result = self.evaluate(contract)
        self.assertIn("record_count_lineage_mismatch", result["blocker_codes"])

    def test_reconciled_multi_input_transformation_can_pass(self) -> None:
        contract = self.make_multi_input(fixture())
        contract["transformations"][1]["multi_input_reconciliation"] = {
            "combination_rule": "keyed_join",
            "expected_output_record_count": 100,
            "receipt_id": "receipt:multi-input-reconciliation",
            "field_conflict_policy_recorded": True,
        }
        result = self.evaluate(contract)
        self.assertEqual("pass", result["status"])

    def test_analysis_input_hash_must_match_declared_snapshot(self) -> None:
        contract = fixture()
        contract["analysis_bindings"][0]["input_sha256"] = "d" * 64
        result = self.evaluate(contract)
        self.assertIn("analysis_input_snapshot_mismatch", result["blocker_codes"])

    def test_hidden_adverse_or_null_exclusion_is_blocking(self) -> None:
        contract = fixture()
        contract["snapshots"][2]["record_count"] = 99
        contract["snapshots"][2]["adverse_or_null_record_count"] = 3
        contract["transformations"][1]["records_removed"] = 1
        contract["data_decisions"].append(
            {
                "decision_id": "decision:exclude-adverse",
                "unit_id": "participant:099",
                "action": "exclude",
                "reason": "Extreme adverse observation.",
                "source_evidence": "source-record:primary",
                "timing_status": "post_hoc",
                "visible": False,
                "affects_adverse_or_null": True,
                "transformation_id": "transform:analysis-ready",
            }
        )
        result = self.evaluate(contract)
        self.assertIn("hidden_adverse_or_null_decision", result["blocker_codes"])

    def test_record_count_changes_must_reconcile_to_unit_decisions(self) -> None:
        contract = fixture()
        contract["snapshots"][2]["record_count"] = 99
        contract["transformations"][1]["records_removed"] = 2
        result = self.evaluate(contract)
        self.assertIn("record_count_lineage_mismatch", result["blocker_codes"])

    def test_missingness_and_adverse_counts_cannot_exceed_denominators(self) -> None:
        contract = fixture()
        contract["snapshots"][2]["missingness"][2]["missing_count"] = 101
        contract["snapshots"][2]["adverse_or_null_record_count"] = 101
        result = self.evaluate(contract)
        self.assertIn("snapshot_count_bounds_invalid", result["blocker_codes"])

    def test_semantic_or_unit_drift_must_be_declared(self) -> None:
        contract = fixture()
        contract["snapshots"][2]["fields"][2]["unit"] = "percentile"
        result = self.evaluate(contract)
        self.assertIn("semantic_schema_drift_unlogged", result["blocker_codes"])

    def test_passed_required_qc_requires_a_receipt(self) -> None:
        contract = fixture()
        contract["quality_controls"][0]["receipt_id"] = None
        result = self.evaluate(contract)
        self.assertIn("quality_control_receipt_missing", result["blocker_codes"])

    def test_adapter_required_qc_cannot_be_marked_not_applicable(self) -> None:
        contract = fixture()
        qc = contract["quality_controls"][0]
        qc["applicability"] = "not_applicable"
        qc["status"] = "not_applicable"
        qc["receipt_id"] = None
        qc["checked_at"] = None
        qc["outcome"] = "Declared not applicable despite adapter requirement."
        result = self.evaluate(contract)
        self.assertIn("required_quality_control_unresolved", result["blocker_codes"])

    def test_failed_required_qc_cannot_be_repaired_by_prose(self) -> None:
        contract = fixture()
        contract["quality_controls"][0]["status"] = "failed"
        result = self.evaluate(contract)
        self.assertIn("required_quality_control_failed", result["blocker_codes"])

    def test_sensor_adapter_requires_calibration_receipt(self) -> None:
        contract = fixture()
        contract["data_context"]["modalities"] = ["sensor_stream"]
        contract["data_context"]["study_contexts"] = ["field_measurement"]
        result = self.evaluate(contract)
        self.assertIn("sensor-field-instrument", result["matched_adapter_ids"])
        self.assertIn("required_calibration_unverified", result["blocker_codes"])

    def test_realized_missingness_handling_must_match_plan_or_deviation(self) -> None:
        contract = fixture()
        contract["realized_missingness_handling"]["method"] = "complete_case"
        result = self.evaluate(contract)
        self.assertIn("missingness_handling_deviation_undisclosed", result["blocker_codes"])

    def test_sensitive_data_cannot_use_unauthorized_public_release(self) -> None:
        contract = fixture()
        contract["data_context"]["sensitivity_tags"] = ["identifiable_human"]
        contract["governance"]["sensitivity_class"] = "restricted_human"
        contract["governance"]["direct_identifiers_present"] = True
        contract["governance"]["public_release_permitted"] = False
        result = self.evaluate(contract)
        self.assertIn("unauthorized_public_release", result["blocker_codes"])
        self.assertIn(
            "public_release_contains_direct_identifiers", result["blocker_codes"]
        )

    def test_governed_sensitive_release_is_not_blocked_by_classification_alone(self) -> None:
        contract = fixture()
        contract["data_context"]["sensitivity_tags"] = ["sensitive_human"]
        contract["source_provenance"]["resolved_adapter_ids"] = [
            "general-tabular-observational",
            "human-clinical-sensitive",
        ]
        governance = contract["governance"]
        governance["sensitivity_class"] = "restricted_human"
        governance["direct_identifiers_present"] = False
        governance["indirect_reidentification_risk"] = "low"
        governance["consent_or_authority_requirement"] = "required"
        governance["consent_or_authority_status"] = "verified"
        governance["consent_or_authority_ids"] = ["authority:public-release"]
        governance["public_release_permitted"] = True
        contract["quality_controls"].append(
            {
                "qc_id": "qc:identifier-risk",
                "target_snapshot_id": "snapshot:analysis",
                "dimension": "identifier_risk_assessment",
                "applicability": "required",
                "status": "passed",
                "criteria": "Declared release was reviewed for direct and indirect identifier risk.",
                "receipt_id": "receipt:identifier-risk",
                "checked_at": "2026-08-28T09:00:00Z",
                "outcome": "No direct identifiers; governed release authorized.",
            }
        )
        result = self.evaluate(contract)
        self.assertEqual("pass", result["status"])
        self.assertNotIn("unauthorized_public_release", result["blocker_codes"])
        self.assertNotIn(
            "public_release_contains_direct_identifiers", result["blocker_codes"]
        )

    def test_missing_required_authority_is_not_repaired_by_claim_narrowing(self) -> None:
        contract = fixture()
        contract["data_context"]["sensitivity_tags"] = ["identifiable_human"]
        contract["governance"]["sensitivity_class"] = "restricted_human"
        contract["governance"]["consent_or_authority_requirement"] = "required"
        contract["governance"]["consent_or_authority_status"] = "missing"
        result = self.evaluate(contract)
        self.assertIn("required_data_authority_missing", result["blocker_codes"])
        route = next(
            item["route"]
            for item in result["repair_routes"]
            if item["code"] == "required_data_authority_missing"
        )
        self.assertNotIn("narrow", route.lower())

    def test_third_party_release_requires_rights(self) -> None:
        contract = fixture()
        contract["source_records"][0]["kind"] = "third_party"
        contract["source_records"][0]["rights_status"] = "missing"
        contract["source_records"][0]["authority_or_licence_ids"] = []
        contract["governance"]["third_party_rights_status"] = "missing"
        result = self.evaluate(contract)
        self.assertIn("third_party_rights_missing", result["blocker_codes"])

    def test_verified_release_requires_resolvable_identifier(self) -> None:
        contract = fixture()
        contract["release"]["persistent_id"] = None
        contract["release"]["locator"] = None
        contract["release"]["resolved_at"] = None
        result = self.evaluate(contract)
        self.assertIn("release_claim_unverified", result["blocker_codes"])

    def test_release_hash_must_match_the_released_snapshot(self) -> None:
        contract = fixture()
        contract["release"]["snapshot_sha256"] = "e" * 64
        result = self.evaluate(contract)
        self.assertIn("release_snapshot_mismatch", result["blocker_codes"])

    def test_verified_public_release_requires_a_reuse_licence(self) -> None:
        contract = fixture()
        contract["release"]["licence"] = None
        result = self.evaluate(contract)
        self.assertIn("public_release_licence_missing", result["blocker_codes"])

    def test_required_exact_policy_can_remain_explicitly_unresolved(self) -> None:
        contract = fixture()
        policy = contract["governance"]["exact_policy_resolution"]
        policy["applicability"] = "required"
        policy["status"] = "unresolved"
        policy["unresolved_items"] = ["Institutional retention rule not checked."]
        result = self.evaluate(contract)
        self.assertEqual("unresolved", result["status"])
        self.assertIn("exact_data_policy_unresolved", result["unresolved_codes"])

    def test_resolved_required_policy_requires_source_provenance(self) -> None:
        contract = fixture()
        policy = contract["governance"]["exact_policy_resolution"]
        policy["applicability"] = "required"
        policy["status"] = "resolved"
        policy["authorities"] = []
        result = self.evaluate(contract)
        self.assertEqual("unresolved", result["status"])
        self.assertIn("exact_data_policy_provenance_missing", result["unresolved_codes"])

    def test_exact_policy_as_of_date_must_match_the_contract(self) -> None:
        contract = fixture()
        policy = contract["governance"]["exact_policy_resolution"]
        policy["applicability"] = "required"
        policy["status"] = "resolved"
        policy["as_of_date"] = "2027-01-01"
        policy["authorities"] = [
            {
                "authority": "Example repository",
                "title": "Policy for a different decision date",
                "url": "https://example.org/policy-2027",
                "effective_from": "2027-01-01",
                "effective_until": None,
                "effective_date_basis": "official_explicit",
                "reviewed_at": "2026-08-28",
            }
        ]
        result = self.evaluate(contract)
        self.assertEqual("unresolved", result["status"])
        self.assertIn("exact_data_policy_as_of_mismatch", result["unresolved_codes"])

    def test_future_effective_policy_is_not_backcast(self) -> None:
        contract = fixture()
        policy = contract["governance"]["exact_policy_resolution"]
        policy["applicability"] = "required"
        policy["status"] = "resolved"
        policy["authorities"] = [
            {
                "authority": "Example repository",
                "title": "Future data policy",
                "url": "https://example.org/future-policy",
                "effective_from": "2027-01-01",
                "effective_until": None,
                "effective_date_basis": "official_explicit",
                "reviewed_at": "2026-08-28",
            }
        ]
        result = self.evaluate(contract)
        self.assertEqual("unresolved", result["status"])
        self.assertIn("future_effective_data_policy", result["unresolved_codes"])

    def test_observed_current_policy_cannot_prove_an_older_rule(self) -> None:
        contract = fixture()
        contract["as_of_date"] = "2025-01-01"
        policy = contract["governance"]["exact_policy_resolution"]
        policy["applicability"] = "required"
        policy["status"] = "resolved"
        policy["as_of_date"] = "2025-01-01"
        policy["authorities"] = [
            {
                "authority": "Example institution",
                "title": "Observed current data policy",
                "url": "https://example.org/current-policy",
                "effective_from": None,
                "effective_until": None,
                "effective_date_basis": "observed_active_not_backcastable",
                "reviewed_at": "2026-08-28",
            }
        ]
        result = self.evaluate(contract)
        self.assertEqual("unresolved", result["status"])
        self.assertIn(
            "historical_data_policy_not_backcastable", result["unresolved_codes"]
        )

    def test_certification_explicitly_excludes_truth_privacy_and_acceptance(self) -> None:
        result = self.evaluate(fixture())
        excluded = set(result["certification"]["does_not_certify"])
        self.assertTrue(
            {
                "measurement_accuracy",
                "completeness_or_representativeness",
                "absence_of_bias",
                "privacy_or_anonymity",
                "scientific_truth",
                "analytic_reproducibility",
                "journal_acceptance",
            }.issubset(excluded)
        )

    def test_canonical_skills_and_project_state_load_the_data_layer(self) -> None:
        writing = (ROOT / "skills" / "academic-writing" / "SKILL.md").read_text(encoding="utf-8")
        pipeline = (ROOT / "skills" / "academic-paper-pipeline" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        project_state = (
            ROOT / "docs" / "academic-paper-project-state.template.yaml"
        ).read_text(encoding="utf-8")
        for text in (writing, pipeline):
            self.assertIn("data-integrity-stewardship-contract.md", text)
            self.assertIn("raw snapshot", text.lower())
            self.assertIn("analysis-ready", text.lower())
        self.assertIn('schema_version: "0.5.0"', project_state)
        self.assertIn("data_integrity_contract:", project_state)
        self.assertIn("does_not_certify_measurement_accuracy: true", project_state)


if __name__ == "__main__":
    unittest.main()
