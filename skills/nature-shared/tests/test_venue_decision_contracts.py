from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

import jsonschema


SHARED = Path(__file__).parents[1]
CONTRACTS = SHARED / "journal-formats" / "decision-contracts"
RESOLVER_PATH = SHARED / "scripts" / "resolve_venue_contract.py"
FUTURE_FIXTURE = Path(__file__).parent / "fixtures" / "venue-contracts" / "future-policy.json"


def load_resolver():
    spec = importlib.util.spec_from_file_location("resolve_venue_contract", RESOLVER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import resolver from {RESOLVER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class VenueDecisionContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.resolver = load_resolver()
        cls.contracts = cls.resolver.load_contracts(CONTRACTS / "profiles")

    def resolve(self, venue: str, article_type: str = "research article", **kwargs):
        return self.resolver.resolve_contract(
            venue=venue,
            article_type=article_type,
            stage=kwargs.pop("stage", "initial_submission"),
            as_of=kwargs.pop("as_of", "2026-08-28"),
            contracts=kwargs.pop("contracts", self.contracts),
            **kwargs,
        )

    def test_maintained_profiles_validate_the_complete_contract_shape(self) -> None:
        self.assertGreaterEqual(len(self.contracts), 3)
        required = {
            "scientific_gates",
            "novelty_gate",
            "impact_gate",
            "breadth_gate",
            "audience_interest_gate",
            "burden_of_doubt",
            "allowed_repair_routes",
            "review_model",
            "ai_confidentiality_policy",
            "acceptance_states",
            "certification_layer",
        }
        for contract in self.contracts:
            with self.subTest(contract=contract.get("contract_id")):
                self.assertEqual([], self.resolver.validate_contract(contract))
                self.assertTrue(required.issubset(contract["decision_contract"]))
                self.assertTrue(contract["provenance"]["sources"])
                self.assertIn("effective_from", contract["policy_validity"])
                self.assertIn("effective_date_basis", contract["policy_validity"])

    def test_profiles_and_future_fixture_conform_to_json_schema(self) -> None:
        schema = json.loads(
            (CONTRACTS / "venue-decision-contract.schema.json").read_text(encoding="utf-8")
        )
        for path in sorted((CONTRACTS / "profiles").glob("*.json")) + [FUTURE_FIXTURE]:
            with self.subTest(path=path.name):
                jsonschema.validate(json.loads(path.read_text(encoding="utf-8")), schema)

    def test_contract_rejects_dangling_policy_source_references(self) -> None:
        invalid = json.loads(json.dumps(self.contracts[0]))
        invalid["decision_contract"]["novelty_gate"]["source_refs"].append(
            "missing-official-source"
        )
        errors = self.resolver.validate_contract(invalid)
        self.assertTrue(
            any("unknown source_ref missing-official-source" in error for error in errors),
            errors,
        )

    def test_same_sound_modest_paper_has_different_target_outcomes(self) -> None:
        observations = {
            "in_scope": True,
            "original_work": True,
            "not_published_elsewhere": True,
            "evidence_supports_claims": True,
            "technical_rigor": True,
            "clear_narrative": True,
            "intelligible_presentation": True,
            "ethics_and_integrity": True,
            "reporting_and_data": True,
            "novelty": False,
            "impact": False,
            "breadth": False,
            "audience_interest": "some",
        }

        tmlr = self.resolver.evaluate_acceptance(self.resolve("TMLR")["contract"], observations)
        nature = self.resolver.evaluate_acceptance(
            self.resolve("Nature", article_type="Article")["contract"], observations
        )
        plos = self.resolver.evaluate_acceptance(
            self.resolve("PLOS ONE")["contract"], observations
        )

        self.assertEqual("contract_criteria_satisfied", tmlr["state"])
        self.assertEqual("target_objective_not_met", nature["state"])
        self.assertEqual("contract_criteria_satisfied", plos["state"])
        self.assertNotIn("score", tmlr)
        self.assertEqual("non_universal", tmlr["objective_scope"])
        self.assertEqual("non_universal", nature["objective_scope"])
        self.assertEqual("non_universal", plos["objective_scope"])

    def test_tmlr_interest_doubt_defaults_toward_satisfied(self) -> None:
        contract = self.resolve("Transactions on Machine Learning Research")["contract"]
        observations = {
            gate["observation_key"]: True
            for gate in contract["decision_contract"]["scientific_gates"]
        }
        observations["audience_interest"] = None
        result = self.resolver.evaluate_acceptance(contract, observations)
        self.assertEqual("contract_criteria_satisfied", result["state"])
        self.assertIn("audience_interest", result["doubt_defaults_applied"])

    def test_claim_narrowing_is_an_explicit_tmlr_repair_not_forced_experimentation(self) -> None:
        contract = self.resolve("TMLR")["contract"]
        repair = self.resolver.assess_repair_route(contract, "narrow_claim")
        self.assertTrue(repair["allowed"])
        self.assertEqual("explicitly_allowed", repair["policy_status"])
        self.assertIn("tmlr-acceptance-criteria", repair["source_refs"])

    def test_future_effective_policy_is_not_applied_early(self) -> None:
        future = json.loads(FUTURE_FIXTURE.read_text(encoding="utf-8"))
        before = self.resolve(
            "Example Future Journal",
            as_of="2026-12-31",
            contracts=[future],
            fallback_profile_id="rigor-first",
        )
        active = self.resolve(
            "Example Future Journal",
            as_of="2027-01-01",
            contracts=[future],
            fallback_profile_id="rigor-first",
        )

        self.assertEqual("fallback_with_live_resolution_required", before["resolution_mode"])
        self.assertIn(future["contract_id"], before["not_yet_effective_contract_ids"])
        self.assertTrue(before["live_official_resolution_required"])
        self.assertEqual("exact_contract_snapshot", active["resolution_mode"])
        self.assertEqual(future["contract_id"], active["contract"]["contract_id"])

    def test_unknown_journal_fallback_never_certifies_exact_policy(self) -> None:
        result = self.resolve(
            "Journal Not Maintained Here",
            fallback_profile_id="rigor-first",
        )
        self.assertEqual("fallback_with_live_resolution_required", result["resolution_mode"])
        self.assertTrue(result["live_official_resolution_required"])
        self.assertTrue(result["fallback"]["profile_is_not_venue_policy"])
        self.assertEqual("fallback_not_exact", result["resolution_certification"]["level"])

    def test_legacy_pre_submission_stage_alias_still_resolves(self) -> None:
        legacy = self.resolve("PLOS ONE", stage="pre_submission")
        canonical = self.resolve("PLOS ONE", stage="initial_submission")
        self.assertEqual("exact_contract_snapshot", legacy["resolution_mode"])
        self.assertEqual(canonical["contract"]["contract_id"], legacy["contract"]["contract_id"])

    def test_live_official_contract_supersedes_local_snapshot_for_same_tuple(self) -> None:
        local = self.resolve("TMLR")["contract"]
        live = json.loads(json.dumps(local))
        live["contract_id"] = "tmlr-research-article-live-2026-08-28"
        live["provenance"]["resolution_mode"] = "live_official_resolution"
        result = self.resolve("TMLR", contracts=self.contracts + [live])
        self.assertEqual("exact_live_official", result["resolution_mode"])
        self.assertEqual(live["contract_id"], result["contract"]["contract_id"])
        self.assertEqual("live_official", result["resolution_certification"]["level"])


if __name__ == "__main__":
    unittest.main()
