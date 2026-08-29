from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
SCRIPT = SHARED / "scripts" / "validate_acceptance_optimization_plan.py"
SCHEMA = SHARED / "acceptance-contracts" / "acceptance-optimization-plan.schema.json"
PROTOCOL = SHARED / "core" / "acceptance-optimization-protocol.md"
HISTORY = SHARED / "core" / "public-review-history-calibration.md"
RESEARCH = SHARED / "research" / "acceptance-optimization-evidence-ledger-2026-08-29.md"

spec = importlib.util.spec_from_file_location("validate_acceptance_optimization_plan", SCRIPT)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def valid_plan() -> dict:
    plos_criteria = "https://journals.plos.org/plosone/s/criteria-for-publication"
    public_history = "https://elifesciences.org/articles/108399/peer-reviews"
    return {
        "schema_version": "1.0.0",
        "objective": "fixed_target_decision_readiness",
        "study_state": "pre_submission",
        "target": {
            "exact_venue": "PLOS ONE",
            "article_type": "Research Article",
            "stage": "initial_submission",
            "as_of_date": "2026-08-29",
            "route": "standard_article",
            "policy_state": "resolved_current",
            "official_policy_urls": [plos_criteria],
        },
        "registered_report": {
            "availability": "not_applicable",
            "eligibility": "not_applicable",
            "official_policy_url": None,
            "stage1_quality_controls_defined": None,
            "notes": "Study is already complete.",
        },
        "levers": [
            {
                "id": "science.claim_alignment",
                "stage": "evidence_maturation",
                "decision_axis": "evidence_maturity",
                "action": "Verify every headline claim is supported by current evidence.",
                "evidence_grade": "MANUSCRIPT_INTERNAL",
                "source_urls": [],
                "enforcement": "hard_gate",
                "scientific_effect": "strengthens_evidence",
                "status": "satisfied",
                "closure_test": "All headline claims have decisive evidence and explicit boundaries.",
            },
            {
                "id": "target.plos_support",
                "stage": "target_fit",
                "decision_axis": "scope",
                "action": "Check exact PLOS ONE publication criteria.",
                "evidence_grade": "D",
                "source_urls": [plos_criteria],
                "enforcement": "hard_gate",
                "scientific_effect": "improves_target_fit",
                "status": "satisfied",
                "closure_test": "The manuscript meets all applicable current target criteria.",
            },
            {
                "id": "history.claim_narrowing",
                "stage": "review",
                "decision_axis": "revision_closure",
                "action": "Use close public histories to compare evidence addition versus claim narrowing.",
                "evidence_grade": "H",
                "source_urls": [public_history],
                "enforcement": "heuristic",
                "scientific_effect": "context_only",
                "status": "satisfied",
                "closure_test": "History pattern is used only as context and checked against our evidence.",
                "transfer_limit": "Public histories are selected and do not prove causal acceptance effects.",
            },
        ],
        "blockers": [
            {
                "id": "B1",
                "class": "manuscript_visibility",
                "status": "closed",
                "resolution_test": "Editor-facing contribution and decisive evidence are recoverable from abstract/main figures.",
            }
        ],
        "target_ladder": [],
        "public_review_history": {
            "used": True,
            "accepted_case_count": 3,
            "rejected_or_rejection_evidence_count": 2,
            "survivorship_warning_recorded": True,
            "notes": "Accepted histories paired with rejection-report evidence.",
        },
        "uncontrollable_context": [
            {
                "factor": "unknown competing submissions",
                "state": "unknown",
                "source_url": None,
                "notes": "Kept separate from repairable manuscript state.",
            }
        ],
        "release_state": "acceptance_optimized_decision_ready_for_target",
    }


class AcceptanceOptimizationProtocolTests(unittest.TestCase):
    def test_valid_plan_passes(self) -> None:
        self.assertEqual(mod.validate_plan(valid_plan(), SCHEMA), [])

    def test_probability_and_person_targeting_fields_fail_closed(self) -> None:
        plan = valid_plan()
        plan["acceptance_probability"] = 0.84
        plan["editor_leniency"] = "high"
        errors = mod.validate_plan(plan, SCHEMA)
        self.assertTrue(any("prohibited acceptance-targeting field" in error for error in errors))
        self.assertTrue(any("additional properties" in error.lower() for error in errors))

    def test_public_history_cannot_be_a_hard_gate(self) -> None:
        plan = valid_plan()
        plan["levers"][2]["enforcement"] = "hard_gate"
        errors = mod.validate_plan(plan, SCHEMA)
        self.assertTrue(any("public review-history heuristics cannot become hard gates" in error for error in errors))

    def test_public_history_requires_rejection_balance_and_survivorship_warning(self) -> None:
        plan = valid_plan()
        plan["public_review_history"]["rejected_or_rejection_evidence_count"] = 0
        plan["public_review_history"]["survivorship_warning_recorded"] = False
        errors = mod.validate_plan(plan, SCHEMA)
        self.assertTrue(any("pair accepted-case learning with rejection evidence" in error for error in errors))
        self.assertTrue(any("survivorship warning" in error for error in errors))

    def test_target_specific_official_gate_must_cite_registered_target_policy(self) -> None:
        plan = valid_plan()
        plan["levers"][1]["source_urls"] = ["https://example.org/editorial-opinion"]
        errors = mod.validate_plan(plan, SCHEMA)
        self.assertTrue(any("registered exact target policy source" in error for error in errors))

    def test_ready_state_fails_with_open_repairable_blocker(self) -> None:
        plan = valid_plan()
        plan["blockers"][0]["status"] = "open"
        errors = mod.validate_plan(plan, SCHEMA)
        self.assertTrue(any("repairable blockers must be closed" in error for error in errors))

    def test_ready_state_fails_with_unsatisfied_hard_gate(self) -> None:
        plan = valid_plan()
        plan["levers"][0]["status"] = "uncertain"
        errors = mod.validate_plan(plan, SCHEMA)
        self.assertTrue(any("every hard gate must be satisfied" in error for error in errors))

    def test_registered_report_route_requires_current_eligibility_and_policy(self) -> None:
        plan = valid_plan()
        plan["objective"] = "registered_report_stage1"
        plan["target"]["route"] = "registered_report_stage1"
        plan["registered_report"] = {
            "availability": "unknown",
            "eligibility": "unknown",
            "official_policy_url": None,
            "stage1_quality_controls_defined": None,
            "notes": "Unresolved.",
        }
        errors = mod.validate_plan(plan, SCHEMA)
        self.assertTrue(any("requires current availability" in error for error in errors))
        self.assertTrue(any("requires confirmed eligibility" in error for error in errors))
        self.assertTrue(any("exact current policy source is required" in error for error in errors))

    def test_successful_publication_objective_requires_fit_first_target_ladder(self) -> None:
        plan = valid_plan()
        plan["objective"] = "successful_publication"
        errors = mod.validate_plan(plan, SCHEMA)
        self.assertTrue(any("fit-first target ladder" in error for error in errors))

    def test_decision_ready_requires_current_policy_and_known_route(self) -> None:
        plan = valid_plan()
        plan["target"]["policy_state"] = "requires_live_research"
        plan["target"]["route"] = "unknown"
        errors = mod.validate_plan(plan, SCHEMA)
        self.assertTrue(any("resolved current target policy" in error for error in errors))
        self.assertTrue(any("cannot use an unknown publication route" in error for error in errors))

    def test_editorial_outcome_uncertain_state_requires_context_bucket(self) -> None:
        plan = valid_plan()
        plan["release_state"] = "decision_ready_but_editorial_outcome_uncertain"
        plan["uncontrollable_context"] = []
        errors = mod.validate_plan(plan, SCHEMA)
        self.assertTrue(any("requires at least one explicit uncontrollable-context item" in error for error in errors))

    def test_protocol_starts_before_writing_and_is_evidence_graded(self) -> None:
        text = read(PROTOCOL).lower()
        for marker in (
            "evidence grades for acceptance levers",
            "earliest-fix principle",
            "registered report check",
            "fit-first target ladder",
            "desk-rejection stress test",
            "multi-editor preflight",
            "revision delta",
            "public review-history calibration",
            "acceptance_optimized_decision_ready_for_target",
        ):
            self.assertIn(marker, text)
        self.assertIn("never output a manuscript-specific numeric acceptance probability", text)

    def test_history_protocol_is_survivorship_aware_and_learns_repairs_not_phrases(self) -> None:
        text = read(HISTORY).lower()
        for marker in (
            "strong selection effects",
            "survivorship/selection warning",
            "repair grammar",
            "reviewer_requested",
            "editor_required",
            "scientifically_required",
            "learn dependencies, not phrases",
            "pair accepted histories with rejection evidence",
        ):
            self.assertIn(marker, text)
        self.assertIn("never infer that a visible revision caused acceptance", text)

    def test_evidence_ledger_preserves_causal_boundaries(self) -> None:
        text = read(RESEARCH).lower()
        for marker in (
            "randomized trial",
            "multi-journal",
            "desk rejection",
            "registered reports",
            "reviewer disagreement",
            "public review histories",
            "claim narrowing",
        ):
            self.assertIn(marker, text)
        self.assertIn("does not justify numeric acceptance probabilities", text)
        self.assertIn("improved overall manuscript quality", text)
        self.assertIn("not a clean causal increase in acceptance probability", text)

    def test_top_level_skills_route_acceptance_optimization_layers(self) -> None:
        manifests = (
            SKILLS / "academic-writing" / "manifest.yaml",
            SKILLS / "academic-paper-pipeline" / "manifest.yaml",
            SKILLS / "nature-reviewer" / "manifest.yaml",
            SHARED / "manifest.yaml",
        )
        for path in manifests:
            text = read(path)
            self.assertIn("acceptance-optimization-protocol.md", text, path)
            self.assertIn("public-review-history-calibration.md", text, path)
            self.assertIn("acceptance-optimization-evidence-ledger-2026-08-29.md", text, path)


if __name__ == "__main__":
    unittest.main()
