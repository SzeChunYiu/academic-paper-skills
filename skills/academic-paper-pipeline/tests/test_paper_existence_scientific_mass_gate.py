from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


PIPELINE = Path(__file__).parents[1]
SHARED = PIPELINE.parent / "nature-shared"
VERIFIER_PATH = SHARED / "scripts" / "verify_paper_existence_scientific_mass.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_verifier():
    spec = importlib.util.spec_from_file_location("paper_existence_verifier", VERIFIER_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def base_ledger() -> dict:
    return {
        "schema_version": "1.0.0",
        "paper_id": "TEST-1",
        "surviving_claim": {
            "plain_language": "A real bounded result changes what the reader should believe.",
            "claim_type": "empirical",
            "posterior_change": "The tested intervention distinguishes the stated alternatives on independent units.",
            "status": "established",
        },
        "hostile_panel": [
            {"lens": "field_editor", "fatal_objection": "", "severity": "none", "closure_test": "n/a"},
            {"lens": "methods_benchmark_statistics", "fatal_objection": "", "severity": "none", "closure_test": "n/a"},
            {"lens": "theory", "fatal_objection": "", "severity": "none", "closure_test": "n/a"},
            {"lens": "systems_reproducibility", "fatal_objection": "", "severity": "none", "closure_test": "n/a"},
            {"lens": "literature_portfolio", "fatal_objection": "", "severity": "none", "closure_test": "n/a"},
        ],
        "scientific_mass": {
            "raw_rows_or_cases": 30,
            "independent_unit_type": "independent task family",
            "independent_unit_count": 12,
            "dependence_notes": "Rows within a family are not counted as independent science.",
            "failure_opportunities": "Both positive and negative outcomes are possible on each family.",
            "adverse_or_null_results": ["one retained null"],
        },
        "novelty": {
            "nearest_external_works": ["Neighbour A", "Neighbour B", "Neighbour C"],
            "component_novelty": "none claimed",
            "composition_novelty": "bounded",
            "emergent_result": "the coupled intervention identifies a new failure boundary",
            "theory_lineage": "no theorem novelty claimed",
        },
        "comparisons": {
            "minimum_mechanism": "simple heuristic baseline is included and loses on the stated estimand",
            "baseline_roles": ["trivial", "strong conventional", "oracle"],
            "interface_parity": "matched",
            "scorer_latitude": "low",
            "designer_advantage": "low",
        },
        "external_validity": {
            "level": "L5",
            "description": "multi-domain prospective units",
            "claim_scope_matches_level": True,
        },
        "integrity_vs_validity": {
            "integrity_evidence": ["replay"],
            "scientific_validity_evidence": ["independent units", "strong controls"],
            "integrity_substituted_for_validity": False,
        },
        "sibling_overlap": {
            "siblings": [],
            "reader_visible_separation": "not_applicable",
            "merge_test": "No sibling shares the scientific question/evidence object.",
        },
        "next_discriminator": {
            "task": "external replication",
            "why_it_changes_decision": "would raise external validity but is not required for the bounded present claim",
            "closure_test": "independent replication reports the same directional result",
            "blocks_further_polish": False,
        },
        "decision": {
            "disposition": "WRITE_FULL_PAPER",
            "top_tier_status": "candidate",
            "second_tier_status": "candidate",
            "reason": "bounded full-paper contribution survives the hostile panel",
        },
    }


class PaperExistenceScientificMassGateTests(unittest.TestCase):
    def test_manifest_always_loads_gate(self) -> None:
        manifest = read(PIPELINE / "manifest.yaml")
        self.assertIn("paper-existence-scientific-mass-gate.md", manifest)
        self.assertIn("paper-existence-scientific-mass.schema.json", manifest)
        self.assertIn("verify_paper_existence_scientific_mass.py", manifest)

    def test_contract_has_nonwriting_terminals_and_claim_narrowing_rerun(self) -> None:
        text = read(SHARED / "core" / "paper-existence-scientific-mass-gate.md")
        for marker in (
            "WAIT_FOR_EVIDENCE",
            "MERGE_WITH_SIBLING",
            "RECLASSIFY_AS_NOTE",
            "KILL_CLAIM",
            "Re-run after claim narrowing",
            "Minimum-mechanism / trivial-baseline attack",
            "Portfolio anti-fragmentation / merge attack",
            "Integrity versus scientific-validity gate",
        ):
            self.assertIn(marker, text)

    def test_full_paper_with_supported_state_passes(self) -> None:
        verifier = load_verifier()
        result = verifier.validate(base_ledger())
        self.assertEqual(result["verdict"], "PASS")

    def test_full_paper_is_blocked_after_claim_collapses(self) -> None:
        verifier = load_verifier()
        ledger = base_ledger()
        ledger["surviving_claim"]["status"] = "unsupported"
        result = verifier.validate(ledger)
        self.assertEqual(result["verdict"], "BLOCKED")
        self.assertTrue(any(item["code"] == "full_paper_without_surviving_claim" for item in result["findings"]))

    def test_wait_for_evidence_must_stop_noninformative_polish(self) -> None:
        verifier = load_verifier()
        ledger = base_ledger()
        ledger["decision"]["disposition"] = "WAIT_FOR_EVIDENCE"
        ledger["decision"]["top_tier_status"] = "not_yet"
        ledger["next_discriminator"]["blocks_further_polish"] = False
        result = verifier.validate(ledger)
        self.assertEqual(result["verdict"], "BLOCKED")
        self.assertTrue(any(item["code"] == "wait_without_polish_block" for item in result["findings"]))

    def test_integrity_cannot_substitute_for_scientific_validity(self) -> None:
        verifier = load_verifier()
        ledger = base_ledger()
        ledger["integrity_vs_validity"]["integrity_substituted_for_validity"] = True
        result = verifier.validate(ledger)
        self.assertEqual(result["verdict"], "BLOCKED")
        self.assertTrue(any(item["code"] == "integrity_substituted_for_validity" for item in result["findings"]))


if __name__ == "__main__":
    unittest.main()
