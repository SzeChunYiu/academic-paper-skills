from __future__ import annotations

import importlib.util
from pathlib import Path

import yaml


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
KERNEL = SHARED / "core" / "ai-session-execution-kernel.md"
ROUTER = SHARED / "core" / "ai-session-context-routing.md"
SCHEMA = SHARED / "analysis-contracts" / "ai-session-checkpoint.schema.json"
VERIFIER = SHARED / "scripts" / "verify_ai_session_checkpoint.py"
EVIDENCE = SHARED / "research" / "ai-session-context-engineering-evidence-2026-08-31.md"
WRITING = SKILLS / "academic-writing" / "manifest.yaml"
PIPELINE = SKILLS / "academic-paper-pipeline" / "manifest.yaml"
REVIEWER = SKILLS / "nature-reviewer" / "manifest.yaml"


def _load_verifier():
    spec = importlib.util.spec_from_file_location("verify_ai_session_checkpoint", VERIFIER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _manifest(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _base_checkpoint() -> dict:
    return {
        "schema_version": "1.0.0",
        "manuscript_id": "paper-demo",
        "session_mode": "COMPOSE",
        "primary_operation": "Draft the Results opening for claim C1",
        "target": {
            "venue": "Example Journal",
            "article_type": "Article",
            "stage": "drafting",
            "rules_verified_as_of": "2026-08-31",
        },
        "paper": {
            "intended_reader": "field-competent reader with no project context",
            "dominant_archetype": "computational / ML paper",
            "central_question": "Does the representation preserve the decision-relevant distinction?",
            "bounded_answer": "It does on the controlled benchmark under the declared conditions.",
        },
        "active_scope": {
            "surface": "Results / controlled benchmark",
            "claim_ids": ["C1"],
            "evidence_ids": ["E1"],
        },
        "hard_constraints": ["Do not invent missing data"],
        "open_blockers": [],
        "reader_state": {
            "terms_active": ["representation"],
            "terms_pending": ["prospective adequacy"],
        },
        "context": {
            "required_contracts": ["manuscript-section-craftsmanship.md"],
            "loaded_contracts": ["manuscript-section-craftsmanship.md"],
        },
        "budget_snapshot": "Results block soft allocation remains available.",
        "deliberately_not_done": ["No global reviewer simulation during composition."],
        "next_action": "Write one evidence-led Results block.",
        "stop_condition": "Stop when the local question is answered and the next handoff is explicit.",
        "updated_at": "2026-08-31T00:00:00Z",
    }


def test_kernel_preserves_hard_invariants_while_reducing_context() -> None:
    text = KERNEL.read_text(encoding="utf-8").lower()
    for marker in (
        "context as a scarce execution resource",
        "truth before fluency",
        "fail closed on unresolved scientific support",
        "the paper is standalone",
        "scientific identity is preserved",
        "publication space is finite",
        "review is adversarial, not confirmatory",
        "release is different from drafting",
        "one primary operation at a time",
        "no compose-plus-global-review collision",
        "minimum sufficient context packet",
        "progressive disclosure is mandatory",
        "stable session checkpoint",
        "evidence cards instead of source dumps",
        "deterministic work goes to deterministic tools",
        "delta-first revision",
        "full-manuscript passes are deliberate",
        "parallel work only when independence is real",
        "stop rules",
    ):
        assert marker in text, marker


def test_router_has_stage_and_task_bundles() -> None:
    text = ROUTER.read_text(encoding="utf-8").lower()
    for marker in (
        "bootstrap bundle",
        "research bundle",
        "architect bundle",
        "compose bundle",
        "audit bundle",
        "revise bundle",
        "review bundle",
        "release bundle",
        "formal task",
        "quantitative task",
        "figure/table task",
        "source/citation task",
        "target task",
        "context eviction rule",
        "full manuscript policy",
        "resume protocol",
        "anti-overengineering boundary",
    ):
        assert marker in text, marker


def test_public_manifests_use_small_always_loaded_working_sets() -> None:
    writing = _manifest(WRITING)
    pipeline = _manifest(PIPELINE)
    reviewer = _manifest(REVIEWER)

    assert writing["version"] == "1.16.0"
    assert pipeline["version"] == "1.18.0"
    assert reviewer["version"] == "3.3.0"

    assert writing["always_load"] == [
        "../nature-shared/core/ai-session-execution-kernel.md",
        "../nature-shared/core/ai-session-context-routing.md",
        "../nature-shared/core/ethics.md",
    ]
    assert pipeline["always_load"] == [
        "../nature-shared/core/ai-session-execution-kernel.md",
        "../nature-shared/core/ai-session-context-routing.md",
        "../nature-shared/core/academic-paper-iteration-pipeline.md",
        "../nature-shared/core/ethics.md",
    ]
    assert reviewer["always_load"] == [
        "../nature-shared/core/ai-session-execution-kernel.md",
        "../nature-shared/core/ai-session-context-routing.md",
        "references/source-basis.md",
        "../nature-shared/core/editor-reviewer-decision-engine.md",
        "../nature-shared/core/adversarial-review-bias-control.md",
    ]


def test_detailed_safeguards_remain_discoverable_not_deleted() -> None:
    combined = "\n".join(
        path.read_text(encoding="utf-8") for path in (WRITING, PIPELINE, REVIEWER, ROUTER)
    )
    for path in (
        "manuscript-excellence-release-gate.md",
        "abstract-information-budget.md",
        "manuscript-section-craftsmanship.md",
        "manuscript-narrative-architecture.md",
        "research-integrity-verification.md",
        "atomic-claim-verification.md",
        "formal-spine-preservation.md",
        "statistical-inference-uncertainty-contract.md",
        "figure-evidence-planning.md",
        "standalone-manuscript-reader-contract.md",
        "scholarly-surface-semantics.md",
        "publication-release-integrity.md",
    ):
        assert path in combined, path


def test_checkpoint_schema_and_verifier_are_present() -> None:
    assert '"const": "1.0.0"' in SCHEMA.read_text(encoding="utf-8")
    evidence = EVIDENCE.read_text(encoding="utf-8").lower()
    for marker in (
        "lost in the middle",
        "leaner prompts",
        "give the agent a map",
        "progressive disclosure",
        "stable checkpoints",
        "delta-first revision",
    ):
        assert marker in evidence, marker


def test_valid_compose_checkpoint_passes() -> None:
    verifier = _load_verifier()
    result = verifier.validate(_base_checkpoint())
    assert result["decision"] == "PASS"
    assert result["counts"] == {"error": 0, "unresolved": 0, "review": 0}


def test_missing_required_contract_blocks_checkpoint() -> None:
    verifier = _load_verifier()
    payload = _base_checkpoint()
    payload["context"]["loaded_contracts"] = []
    result = verifier.validate(payload)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "required_contract_not_loaded" for item in result["findings"])


def test_compose_without_active_surface_blocks_checkpoint() -> None:
    verifier = _load_verifier()
    payload = _base_checkpoint()
    payload["active_scope"]["surface"] = None
    result = verifier.validate(payload)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "active_surface_required" for item in result["findings"])


def test_release_without_target_blocks_checkpoint() -> None:
    verifier = _load_verifier()
    payload = _base_checkpoint()
    payload["session_mode"] = "RELEASE"
    payload["primary_operation"] = "Run final release verification"
    payload["target"] = None
    result = verifier.validate(payload)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "release_target_unresolved" for item in result["findings"])


def test_review_without_concern_state_is_only_a_review_signal() -> None:
    verifier = _load_verifier()
    payload = _base_checkpoint()
    payload["session_mode"] = "REVIEW"
    payload["primary_operation"] = "Initial independent reviewer pass"
    payload["active_scope"]["surface"] = None
    result = verifier.validate(payload)
    assert result["decision"] == "REVIEW"
    assert any(item["code"] == "review_scope_check" for item in result["findings"])
