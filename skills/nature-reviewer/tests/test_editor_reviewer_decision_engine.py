from __future__ import annotations

import unittest
from pathlib import Path


REVIEWER = Path(__file__).parents[1]
SHARED = REVIEWER.parent / "nature-shared"


def read(base: Path, relative: str) -> str:
    return (base / relative).read_text(encoding="utf-8")


class EditorReviewerDecisionEngineTests(unittest.TestCase):
    def test_router_has_separate_editor_and_reviewer_stages(self) -> None:
        router = read(REVIEWER, "SKILL.md")
        self.assertIn("Editorial triage simulation", router)
        self.assertIn("Editor synthesis (post-review; simulated)", router)
        self.assertIn("Decision engineering map", router)
        self.assertIn("Do not let one reviewer read", router)
        self.assertIn("Do not claim the real editor's final decision or numeric acceptance probability", router)

    def test_publication_models_are_not_one_universal_score(self) -> None:
        profiles = read(SHARED, "journal-formats/editorial-decision-profiles.md")
        self.assertIn("selective broad-interest", profiles)
        self.assertIn("rigor-first scholarly record", profiles)
        self.assertIn("evidence-assessment without post-review gatekeeping", profiles)
        self.assertIn("Do not average incompatible profiles", profiles)
        self.assertIn("validity may be a hard gate while impact is not a gate", profiles)

    def test_resolution_routes_include_claim_narrowing_and_target_change(self) -> None:
        engine = read(SHARED, "core/editor-reviewer-decision-engine.md")
        self.assertIn("Route 5 — narrow the claim", engine)
        self.assertIn("Route 6 — remove the claim", engine)
        self.assertIn("change target/article type", engine)
        self.assertIn("No vote counting", engine)
        self.assertIn("Do not add experiments solely to appease a reviewer", engine)

    def test_rigor_first_review_does_not_force_importance(self) -> None:
        axes = read(REVIEWER, "references/review-axes.md")
        self.assertIn("Rigor-first profile", axes)
        self.assertIn("do **not** manufacture those bars", axes)
        self.assertIn("PLOS ONE", axes)

    def test_reviewer_packet_excludes_editorial_triage_conclusion(self) -> None:
        workflow = read(REVIEWER, "references/reviewer-workflow.md")
        self.assertIn("Do **not** include", workflow)
        self.assertIn("editorial triage conclusions", workflow)
        self.assertIn("weight arguments, not votes", workflow)
        self.assertIn("optional_enrichment", workflow)

    def test_anti_gaming_is_explicit(self) -> None:
        engine = read(SHARED, "core/editor-reviewer-decision-engine.md")
        for marker in (
            "suggesting reviewers because they are expected to be favorable",
            "citing a potential reviewer merely to influence them",
            "hiding limitations",
        ):
            self.assertIn(marker, engine)


if __name__ == "__main__":
    unittest.main()
