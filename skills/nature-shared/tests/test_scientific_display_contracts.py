from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

import jsonschema


SHARED = Path(__file__).parents[1]
DISPLAY_ROOT = SHARED / "display-contracts"
SCHEMA_PATH = DISPLAY_ROOT / "scientific-display-contract.schema.json"
ADAPTERS_PATH = DISPLAY_ROOT / "maintained-adapters.json"
EVIDENCE_REGISTRY_PATH = DISPLAY_ROOT / "display-evidence-registry.json"
RESOLVER_PATH = SHARED / "scripts" / "resolve_scientific_display.py"
VALID_FIXTURE = (
    Path(__file__).parent
    / "fixtures"
    / "display-contracts"
    / "paired-change-valid.json"
)


def load_resolver():
    spec = importlib.util.spec_from_file_location(
        "resolve_scientific_display", RESOLVER_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import resolver from {RESOLVER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fixture() -> dict:
    return json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))


class ScientificDisplayContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.resolver = load_resolver()
        cls.adapters = cls.resolver.load_adapter_catalog(ADAPTERS_PATH)

    def evaluate(self, contract: dict) -> dict:
        return self.resolver.evaluate_display_contract(contract, self.adapters)

    def test_valid_contract_and_catalog_conform_to_schema(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        jsonschema.validate(fixture(), schema)
        self.assertEqual([], self.resolver.validate_adapter_catalog(self.adapters))
        for source in self.adapters["sources"]:
            self.assertIn("accessed_at", source)
            self.assertTrue(source["supports"])

    def test_display_rules_have_a_substantial_auditable_research_base(self) -> None:
        registry = json.loads(EVIDENCE_REGISTRY_PATH.read_text(encoding="utf-8"))
        sources = registry["sources"]
        self.assertGreaterEqual(len(sources), 30)
        self.assertGreaterEqual(registry["search_protocol"]["records_screened"], 80)
        source_by_id = {source["source_id"]: source for source in sources}
        self.assertEqual(len(sources), len(source_by_id))
        self.assertGreaterEqual(len(self.adapters["profiles"]), 10)
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
        for profile in self.adapters["profiles"]:
            refs = profile["source_refs"]
            self.assertGreaterEqual(len(refs), 2, profile["adapter_id"])
            self.assertTrue(set(refs).issubset(source_by_id), profile["adapter_id"])
        ledger = SHARED / "research" / "scientific-display-evidence-ledger-2026-08.md"
        text = ledger.read_text(encoding="utf-8")
        self.assertIn("Search and screening protocol", text)
        self.assertIn("Descriptive frequency is not a normative rule", text)
        self.assertIn("Contradictions and transfer limits", text)
        search_log = json.loads(
            (
                SHARED
                / "research"
                / "scientific-display-search-log-2026-08-28.json"
            ).read_text(encoding="utf-8")
        )
        self.assertGreaterEqual(len(search_log["queries"]), 12)
        self.assertEqual(
            registry["search_protocol"]["records_screened"],
            sum(len(query["records"]) for query in search_log["queries"]),
        )

    def test_incomplete_contract_fails_closed_before_semantic_evaluation(self) -> None:
        contract = fixture()
        del contract["claim_links"]
        result = self.evaluate(contract)
        self.assertEqual("blocked", result["status"])
        self.assertIn("schema_validation_error", result["blocker_codes"])
        self.assertTrue(result["schema_errors"])

    def test_resolver_returns_candidates_not_a_universal_best_chart(self) -> None:
        result = self.resolver.resolve_display_adapter(
            reader_task="compare_change",
            data_structure=["paired", "repeated_measure"],
            claim_type="comparative",
            adapters=self.adapters,
        )
        self.assertEqual("candidate_set_not_universal_best", result["selection_mode"])
        self.assertIn("connected_points", result["candidate_families"])
        self.assertIn("paired_difference", result["candidate_families"])
        self.assertNotIn("best_family", result)
        self.assertTrue(result["obligations"])

    def test_complete_paired_change_contract_passes(self) -> None:
        contract = fixture()
        self.assertTrue(contract["representation"]["rationale"])
        result = self.evaluate(contract)
        self.assertEqual("pass", result["status"])
        self.assertEqual([], result["blockers"])
        self.assertIn("paired-change", result["matched_adapter_ids"])

    def test_paired_estimand_rejects_independent_summary_that_hides_pairing(self) -> None:
        contract = fixture()
        contract["representation"]["family"] = "independent_mean_bar"
        contract["representation"]["channels"] = [
            {"variable": "condition", "channel": "x_position"},
            {"variable": "mean_outcome", "channel": "bar_length"},
        ]
        result = self.evaluate(contract)
        self.assertIn("paired_structure_not_visible", result["blocker_codes"])

    def test_caption_denominator_drift_is_blocking(self) -> None:
        contract = fixture()
        contract["caption"]["denominator"]["value"] = 23
        result = self.evaluate(contract)
        self.assertIn("caption_denominator_mismatch", result["blocker_codes"])

    def test_analysis_and_render_snapshot_drift_are_blocking(self) -> None:
        contract = fixture()
        contract["evidence_links"]["analysis_receipt"]["input_data_sha256"] = "0" * 64
        contract["evidence_links"]["render_receipt"]["input_analysis_sha256"] = "1" * 64
        result = self.evaluate(contract)
        self.assertIn("analysis_input_snapshot_mismatch", result["blocker_codes"])
        self.assertIn("render_input_analysis_mismatch", result["blocker_codes"])

    def test_unspecified_error_bars_are_blocking(self) -> None:
        contract = fixture()
        contract["representation"]["uncertainty"]["kind"] = "unspecified"
        contract["caption"]["uncertainty_definition"] = ""
        result = self.evaluate(contract)
        self.assertIn("uncertainty_semantics_missing", result["blocker_codes"])

    def test_embedding_cannot_support_mechanism_without_independent_evidence(self) -> None:
        contract = fixture()
        contract["reader_task"] = {
            "id": "orient_high_dimensional_structure",
            "question": "What structure is visible in the embedding?",
        }
        contract["scientific_object"]["data_structure"] = ["high_dimensional"]
        contract["claim_links"][0]["claim_type"] = "mechanistic"
        contract["claim_links"][0]["allowed_inferences"] = ["mechanism"]
        contract["representation"]["family"] = "embedding"
        result = self.evaluate(contract)
        self.assertIn("embedding_mechanism_overclaim", result["blocker_codes"])

    def test_embedding_cannot_support_causal_claim_without_independent_evidence(self) -> None:
        contract = fixture()
        contract["reader_task"] = {
            "id": "orient_high_dimensional_structure",
            "question": "What structure is visible in the embedding?",
        }
        contract["scientific_object"]["data_structure"] = ["high_dimensional"]
        contract["claim_links"][0]["claim_type"] = "causal"
        contract["representation"]["family"] = "embedding"
        result = self.evaluate(contract)
        self.assertIn("embedding_mechanism_overclaim", result["blocker_codes"])

    def test_workflow_diagram_cannot_silently_become_a_causal_model(self) -> None:
        contract = fixture()
        contract["display_kind"] = "diagram"
        contract["reader_task"] = {
            "id": "explain_workflow",
            "question": "In what order were study operations performed?",
        }
        contract["scientific_object"]["data_structure"] = ["process"]
        contract["claim_links"][0]["claim_type"] = "causal"
        contract["claim_links"][0]["allowed_inferences"] = ["causal_effect"]
        contract["representation"]["family"] = "workflow_diagram"
        result = self.evaluate(contract)
        self.assertIn("workflow_causal_overclaim", result["blocker_codes"])

    def test_final_display_requires_accessible_non_color_only_encoding(self) -> None:
        contract = fixture()
        contract["accessibility"]["color_only_encoding"] = True
        contract["accessibility"]["redundant_channels"] = []
        contract["accessibility"]["alt_text"] = ""
        result = self.evaluate(contract)
        self.assertIn("color_only_encoding", result["blocker_codes"])
        self.assertIn("alt_text_missing", result["blocker_codes"])

    def test_selective_group_omission_requires_explicit_disclosure(self) -> None:
        contract = fixture()
        contract["representation"]["observed_groups"].append("adverse_event")
        result = self.evaluate(contract)
        self.assertIn("undisclosed_group_omission", result["blocker_codes"])

        contract["representation"]["omission_disclosures"].append(
            {
                "group": "adverse_event",
                "reason": "Shown in the adjacent safety panel with the same data snapshot.",
            }
        )
        repaired = self.evaluate(contract)
        self.assertNotIn("undisclosed_group_omission", repaired["blocker_codes"])

    def test_contract_repairs_are_specific_and_do_not_invent_evidence(self) -> None:
        contract = fixture()
        contract["caption"]["denominator"]["value"] = 23
        result = self.evaluate(contract)
        repair = next(
            item
            for item in result["repair_routes"]
            if item["code"] == "caption_denominator_mismatch"
        )
        self.assertIn("reconcile", repair["route"])
        self.assertNotIn("fabricate", repair["route"])

    def test_shared_manifest_routes_the_authoritative_contract(self) -> None:
        manifest = (SHARED / "manifest.yaml").read_text(encoding="utf-8")
        contract = SHARED / "core" / "scientific-display-decision-contract.md"
        self.assertTrue(contract.exists())
        self.assertIn("scientific-display-decision-contract.md", manifest)


if __name__ == "__main__":
    unittest.main()
