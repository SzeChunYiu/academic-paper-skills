from __future__ import annotations

import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class NaturalScholarlyProseTests(unittest.TestCase):
    def test_shared_manifest_routes_natural_prose(self) -> None:
        manifest = read(SHARED / "manifest.yaml")
        self.assertIn("core/natural-scholarly-prose.md", manifest)

    def test_quality_model_is_not_detector_evasion(self) -> None:
        text = read(SHARED / "core" / "natural-scholarly-prose.md")
        self.assertIn("writing-quality contract", text)
        self.assertIn("It is **not** an AI-detector evasion guide.", text)
        self.assertIn("No AI-word blacklist", text)
        self.assertIn("Never introduce grammatical errors", text)
        self.assertIn("random sentence lengths", text)
        self.assertIn("function, specificity, collocation, evidence, and voice", text)

    def test_sentence_flow_has_dependency_and_why_now_contract(self) -> None:
        natural = read(SHARED / "core" / "natural-scholarly-prose.md")
        flow = read(SKILLS / "nature-writing" / "references" / "paragraph-flow.md")
        for text in (natural, flow):
            self.assertIn("inherits", text)
            self.assertIn("relation", text)
            self.assertIn("adds", text)
            self.assertIn("enables", text)
        self.assertIn("Sentence dependency graph", flow)
        self.assertIn("identity chains", flow)

    def test_given_new_is_default_not_universal_template(self) -> None:
        natural = read(SHARED / "core" / "natural-scholarly-prose.md")
        flow = read(SKILLS / "nature-writing" / "references" / "paragraph-flow.md")
        self.assertIn("not a compulsory template", natural)
        self.assertIn("Do not enforce old-before-new", flow)

    def test_precise_technical_repetition_is_allowed(self) -> None:
        natural = read(SHARED / "core" / "natural-scholarly-prose.md")
        flow = read(SKILLS / "nature-writing" / "references" / "paragraph-flow.md")
        self.assertIn("Repeat central technical terms", natural)
        self.assertIn("exact repetition can be the more natural scholarly choice", flow)

    def test_syntactic_variation_is_functional_not_random(self) -> None:
        natural = read(SHARED / "core" / "natural-scholarly-prose.md")
        writing = read(SKILLS / "nature-writing" / "SKILL.md")
        self.assertIn("functionally motivated variation", natural)
        self.assertIn("Vary sentence structure **because rhetorical function varies**", writing)
        self.assertIn("Do not optimize for AI-detector evasion", writing)

    def test_author_voice_is_quality_layer_not_error_preservation(self) -> None:
        voice = read(SHARED / "core" / "author-voice-profile.md")
        self.assertIn("natural scholarly prose = quality floor", voice)
        self.assertIn("author voice = identity layer", voice)
        self.assertIn("Detector cosplay", voice)
        self.assertIn("Do not infer voice", voice)

    def test_polishing_routes_natural_prose(self) -> None:
        manifest = read(SKILLS / "nature-polishing" / "manifest.yaml")
        self.assertIn("natural-scholarly-prose.md", manifest)
        self.assertIn("detector evasion", manifest)


if __name__ == "__main__":
    unittest.main()
