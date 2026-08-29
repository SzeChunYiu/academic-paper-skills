from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
SCRIPT = SHARED / "scripts" / "validate_editorial_routing_profile.py"
SCHEMA = SHARED / "editorial-contracts" / "editorial-routing-profile.schema.json"
ACCEPTANCE = SHARED / "core" / "journal-acceptance-readiness.md"
ROUTING = SHARED / "core" / "editor-expertise-routing.md"
ENGINE = SHARED / "core" / "editor-reviewer-decision-engine.md"
RESEARCH = SHARED / "research" / "journal-acceptance-editorial-decision-research-2026-08-29.md"

spec = importlib.util.spec_from_file_location("validate_editorial_routing_profile", SCRIPT)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def valid_profile() -> dict:
    policy_url = "https://journals.plos.org/plosone/s/submit-now"
    board_url = "https://journals.plos.org/plosone/static/editorial-board"
    return {
        "schema_version": "1.0.0",
        "exact_venue": "PLOS ONE",
        "article_type": "Research Article",
        "as_of_date": "2026-08-29",
        "manuscript": {
            "domain_tags": ["computational biology"],
            "method_tags": ["machine learning", "external validation"],
            "contribution_class": "empirical method evaluation",
            "reviewer_expertise_needed": ["domain biology", "prediction modeling", "statistics"],
        },
        "suggestion_policy": {
            "state": "permitted",
            "source_url": policy_url,
            "notes": "Current workflow asks for qualified Academic Editor recommendations.",
        },
        "exclusion_policy": {
            "state": "permitted",
            "source_url": policy_url,
            "notes": "Current workflow permits opposed Editors/reviewers with reasons.",
        },
        "editor_sources": [
            {
                "url": policy_url,
                "source_type": "official_submission_policy",
                "official": True,
                "accessed_at": "2026-08-29",
            },
            {
                "url": board_url,
                "source_type": "official_board_page",
                "official": True,
                "accessed_at": "2026-08-29",
            },
        ],
        "candidates": [
            {
                "name": "Example Editor",
                "role": "Academic Editor",
                "section_or_team": "Computational Biology",
                "expertise_evidence": ["official board subject coverage"],
                "source_urls": [board_url],
                "conflict_status": "clear",
                "routing_fit": "strong",
                "intended_use": "suggest_if_permitted",
                "notes": "Synthetic test fixture; not a real recommendation.",
            }
        ],
        "routing_state": "strong_coverage",
        "routing_ambiguity": [],
        "submission_metadata_repairs": [],
    }


class JournalAcceptanceReadinessTests(unittest.TestCase):
    def test_acceptance_is_gate_based_not_probability(self) -> None:
        text = read(ACCEPTANCE).lower()
        self.assertIn("there is no single \"key\" to journal acceptance", text)
        self.assertIn("do not output a numeric acceptance probability", text)
        for marker in (
            "editorial triage",
            "editor/expertise routing",
            "external technical review",
            "editorial synthesis",
            "revision closure",
            "retargeting is an acceptance tool",
        ):
            self.assertIn(marker, text)

    def test_irreducible_editorial_uncertainty_is_separate_from_repairable_state(self) -> None:
        text = read(ACCEPTANCE).lower().replace("**", "")
        self.assertIn("uncontrollable editorial context", text)
        self.assertIn("simultaneous or just-accepted overlapping work", text)
        self.assertIn("competition among multiple strong submissions", text)
        self.assertIn("should not automatically trigger more experiments", text)

    def test_multi_editor_preflight_is_independent_and_not_vote_counting(self) -> None:
        text = read(ACCEPTANCE).lower()
        engine = read(ENGINE).lower()
        self.assertIn("multi-editor preflight", text)
        self.assertIn("freeze each assessment independently", text)
        self.assertIn("do not count editor-lens votes", text)
        self.assertIn("multi-editor desk preflight", engine)
        self.assertIn("do not count lens votes", engine)

    def test_editor_identity_is_routing_metadata_not_persuasion_target(self) -> None:
        text = read(ROUTING).lower()
        self.assertIn("professional routing metadata", text)
        self.assertIn("not as psychological targets", text)
        for marker in (
            "leniency/harshness labels",
            "acceptance propensity",
            "citation preferences",
            "political/religious beliefs",
            "do not search for personal information",
        ):
            self.assertIn(marker, text)
        self.assertIn("do not insert editor names into the manuscript", text)

    def test_editor_suggestion_requires_exact_target_permission(self) -> None:
        profile = valid_profile()
        self.assertEqual(mod.validate_profile(profile, SCHEMA), [])

        profile["suggestion_policy"]["state"] = "not_permitted"
        errors = mod.validate_profile(profile, SCHEMA)
        self.assertTrue(any("editor suggestion is not permitted" in error for error in errors))

    def test_resolved_permission_requires_source(self) -> None:
        profile = valid_profile()
        profile["suggestion_policy"]["source_url"] = None
        errors = mod.validate_profile(profile, SCHEMA)
        self.assertTrue(any("resolved permission state requires a current policy source" in error for error in errors))

    def test_permission_source_must_be_registered_official_submission_policy(self) -> None:
        profile = valid_profile()
        profile["suggestion_policy"]["source_url"] = "https://example.org/unregistered"
        errors = mod.validate_profile(profile, SCHEMA)
        self.assertTrue(any("policy source must be registered" in error for error in errors))

        profile = valid_profile()
        policy_url = profile["suggestion_policy"]["source_url"]
        policy_source = next(source for source in profile["editor_sources"] if source["url"] == policy_url)
        policy_source["official"] = False
        policy_source["source_type"] = "publication_record"
        errors = mod.validate_profile(profile, SCHEMA)
        self.assertTrue(any("resolved permission requires an official source" in error for error in errors))
        self.assertTrue(any("official_submission_policy" in error for error in errors))

    def test_conflicted_editor_cannot_be_suggested(self) -> None:
        profile = valid_profile()
        profile["candidates"][0]["conflict_status"] = "conflict"
        profile["candidates"][0]["routing_fit"] = "conflict"
        errors = mod.validate_profile(profile, SCHEMA)
        self.assertTrue(any("only conflict-clear candidates" in error for error in errors))
        self.assertTrue(any("conflicted editor cannot" in error for error in errors))

    def test_prohibited_editor_targeting_fields_fail_closed(self) -> None:
        profile = valid_profile()
        profile["acceptance_probability"] = 0.8
        profile["candidates"][0]["leniency_score"] = 9
        errors = mod.validate_profile(profile, SCHEMA)
        self.assertTrue(any("prohibited editor-targeting field" in error for error in errors))
        self.assertTrue(any("additional properties" in error.lower() for error in errors))

    def test_named_candidate_must_directly_cite_official_editor_or_board_source(self) -> None:
        profile = valid_profile()
        secondary_url = "https://orcid.org/0000-0000-0000-0000"
        profile["editor_sources"].append(
            {
                "url": secondary_url,
                "source_type": "orcid",
                "official": False,
                "accessed_at": "2026-08-29",
            }
        )
        profile["candidates"][0]["source_urls"] = [secondary_url]
        errors = mod.validate_profile(profile, SCHEMA)
        self.assertTrue(any("must cite an official editor or editorial-board source directly" in error for error in errors))

    def test_candidate_source_must_be_registered(self) -> None:
        profile = valid_profile()
        profile["candidates"][0]["source_urls"] = ["https://example.org/unregistered"]
        errors = mod.validate_profile(profile, SCHEMA)
        self.assertTrue(any("sources not present in editor_sources" in error for error in errors))

    def test_editor_source_requires_access_date(self) -> None:
        profile = valid_profile()
        profile["editor_sources"][0].pop("accessed_at")
        errors = mod.validate_profile(profile, SCHEMA)
        self.assertTrue(any("accessed_at" in error for error in errors))

    def test_exclusion_requires_permission_and_conflict_rationale(self) -> None:
        profile = valid_profile()
        profile["candidates"][0]["intended_use"] = "exclude_if_permitted"
        profile["candidates"][0]["conflict_status"] = "clear"
        profile["exclusion_policy"]["state"] = "not_permitted"
        errors = mod.validate_profile(profile, SCHEMA)
        self.assertTrue(any("editor exclusion is not permitted" in error for error in errors))
        self.assertTrue(any("exclusion needs a conflict-based rationale" in error for error in errors))

    def test_research_basis_includes_current_editorial_and_meta_research(self) -> None:
        text = read(RESEARCH).lower()
        for marker in (
            "nature communications",
            "plos one",
            "nature geoscience",
            "reviewer disagreement",
            "desk-rejection judgments can differ",
            "novelty",
            "author-suggested reviewers",
            "2026-08-29",
        ):
            self.assertIn(marker, text)
        self.assertIn("not a recipe for manipulating editors", text)

    def test_top_level_skills_route_acceptance_and_editor_expertise(self) -> None:
        manifests = (
            SKILLS / "academic-writing" / "manifest.yaml",
            SKILLS / "academic-paper-pipeline" / "manifest.yaml",
            SKILLS / "nature-reviewer" / "manifest.yaml",
            SHARED / "manifest.yaml",
        )
        for path in manifests:
            text = read(path)
            self.assertIn("journal-acceptance-readiness.md", text, path)
            self.assertIn("editor-expertise-routing.md", text, path)
            self.assertIn("journal-acceptance-editorial-decision-research-2026-08-29.md", text, path)


if __name__ == "__main__":
    unittest.main()
