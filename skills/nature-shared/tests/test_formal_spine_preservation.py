from __future__ import annotations

from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
CONTRACT = SHARED / "core" / "formal-spine-preservation.md"
WRITING_MANIFEST = SKILLS / "academic-writing" / "manifest.yaml"
PIPELINE_MANIFEST = SKILLS / "academic-paper-pipeline" / "manifest.yaml"
ARCHETYPE = SHARED / "core" / "paper-archetype-atlas.md"


def test_formal_spine_contract_covers_overcompression_regression() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()

    required_markers = (
        "formal-spine inventory",
        "main_text_requirement: required",
        "minimum formal core for framework papers",
        "the scientific object",
        "the scientific transition or operator",
        "the context or competence boundary",
        "the decisive implication or non-implication",
        "candidate laws are not established axioms",
        "compression order",
        "formal-spine delta audit",
        "reader recovery test",
        "perspective and review articles",
        "anti-overformalization safeguards",
        "ideas retained; formal scientific object deleted",
    )
    for marker in required_markers:
        assert marker in text, marker


def test_contract_preserves_nonimplication_and_context_relative_formalism() -> None:
    text = CONTRACT.read_text(encoding="utf-8")
    assert r"\not\Rightarrow" in text
    assert "successful execution" in text
    assert "warranted scientific transition" in text
    assert "context-relative" in text
    assert "candidate/hypothesis status" in text


def test_contract_does_not_reward_equation_density() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "never invent formalism",
        "minimum sufficient formal core",
        "manufacture equations",
        "notation density with scientific depth",
    ):
        assert marker in text, marker


def test_academic_writing_always_loads_formal_spine_contract() -> None:
    manifest = WRITING_MANIFEST.read_text(encoding="utf-8")
    assert "version: 1.10.0" in manifest
    assert "../nature-shared/core/formal-spine-preservation.md" in manifest
    assert "formal-spine preservation" in manifest


def test_iteration_pipeline_always_loads_formal_spine_contract() -> None:
    manifest = PIPELINE_MANIFEST.read_text(encoding="utf-8")
    assert "version: 1.11.0" in manifest
    assert "../nature-shared/core/formal-spine-preservation.md" in manifest
    assert "formal-spine preservation" in manifest


def test_existing_archetype_atlas_covers_theory_and_perspective_use_cases() -> None:
    text = ARCHETYPE.read_text(encoding="utf-8").lower()
    assert "theory / proof / mathematical paper" in text
    assert "review / systematic review / perspective / synthesis paper" in text
