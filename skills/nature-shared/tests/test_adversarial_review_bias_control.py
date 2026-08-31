from __future__ import annotations

from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
CONTRACT = SHARED / "core" / "adversarial-review-bias-control.md"
REVIEWER_MANIFEST = SKILLS / "nature-reviewer" / "manifest.yaml"
PIPELINE_MANIFEST = SKILLS / "academic-paper-pipeline" / "manifest.yaml"


def _version(text: str) -> tuple[int, ...]:
    for line in text.splitlines():
        if line.startswith("version:"):
            return tuple(int(part) for part in line.split(":", 1)[1].strip().split("."))
    raise AssertionError("manifest version missing")


def test_contract_requires_active_falsification_not_just_blind_reviewers() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "reviewer independence is necessary but not sufficient",
        "not_yet_established",
        "reconstruct the case independently",
        "mandatory adversarial attack log",
        "counterexample / boundary attack",
        "alternative-explanation attack",
        "prior-art / novelty attack",
        "negative-evidence attack",
        "definition / type attack",
        "cross-surface contradiction attack",
        "reproducibility / provenance attack",
    ):
        assert marker in text, marker


def test_contract_controls_framing_and_revision_anchoring() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "interpretation-blind evidence pass when feasible",
        "best rejection / non-closure case",
        "best survival / acceptance-readiness case",
        "reviewer continuity does not substitute for a cold review",
        "final clean-room closure review",
        "no positivity momentum",
    ):
        assert marker in text, marker


def test_contract_does_not_reward_performative_harshness() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "there is no concern quota",
        "failure-seeking is not performative harshness",
        "do not manufacture flaws",
        "no blocking concern survived the attempted falsification passes",
    ):
        assert marker in text, marker


def test_terminal_state_requires_adversarial_and_clean_room_closure() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "headline claims have adversarial attack logs",
        "strongest rejection/non-closure case",
        "major central revisions received a cold review",
        "final clean-room closure review passed",
        "confirmation-bias protection is incomplete",
    ):
        assert marker in text, marker


def test_reviewer_and_pipeline_always_load_bias_control() -> None:
    reviewer = REVIEWER_MANIFEST.read_text(encoding="utf-8")
    pipeline = PIPELINE_MANIFEST.read_text(encoding="utf-8")
    path = "../nature-shared/core/adversarial-review-bias-control.md"
    assert path in reviewer
    assert path in pipeline
    # The path is the normative routing invariant. Descriptions may wrap or become
    # more specific over time, so only require the semantic concepts to remain.
    assert "adversarial" in reviewer.lower()
    assert "confirmation-bias" in reviewer.lower()
    assert "adversarial" in pipeline.lower()
    assert "confirmation-bias" in pipeline.lower()
    assert _version(reviewer) >= (2, 8, 0)
    assert _version(pipeline) >= (1, 13, 0)
