from __future__ import annotations

import importlib.util
from pathlib import Path


SHARED = Path(__file__).parents[1]
CONTRACT = SHARED / "core" / "manuscript-element-justification.md"
KERNEL = SHARED / "core" / "ai-session-execution-kernel.md"
SCHEMA = SHARED / "analysis-contracts" / "manuscript-element-justification-ledger.schema.json"
VERIFIER = SHARED / "scripts" / "verify_manuscript_element_justification.py"


def _load_verifier():
    spec = importlib.util.spec_from_file_location("verify_manuscript_element_justification", VERIFIER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _element(eid: str, parent: str | None, *, function: str, contribution: str, importance: str = "central") -> dict:
    return {
        "element_id": eid,
        "element_type": "paragraph" if parent else "section",
        "parent_id": parent,
        "importance": importance,
        "location": eid,
        "reader_question": f"What job does {eid} perform?",
        "functions": [function],
        "incoming_dependency": "the paper question" if parent is None else "the preceding scientific state",
        "contribution": contribution,
        "outgoing_dependency": "enables the next scientific decision",
        "deletion_consequence": "the reader loses a necessary part of the argument",
        "reader_state": {
            "before": f"before {eid}",
            "after": f"after {eid}",
            "remaining_uncertainty": "the next question remains open",
        },
        "claim_ids": ["C1"],
        "evidence_ids": ["E1"] if function == "evidence" else [],
        "placement": "main_text",
        "placement_reason": "the first-pass reader needs it here",
        "representation_reason": "prose is the lowest-friction representation for this job",
        "redundancy": {"status": "unique", "reason": "no other audited element performs the same job"},
        "protected_by": [],
        "status": "keep",
    }


def _ledger(release: str = "PASS") -> dict:
    return {
        "schema_version": "1.0.0",
        "manuscript_id": "demo",
        "stage": "final",
        "scope": {"surface": "full manuscript", "coverage": "all_paragraphs", "notes": "sentence audit escalated where needed"},
        "elements": [
            _element("sec-results", None, function="orient", contribution="defines the Results reader job"),
            _element("p1", "sec-results", function="evidence", contribution="establishes the decisive observation"),
            _element("p2", "sec-results", function="interpret", contribution="explains the bounded scientific meaning"),
        ],
        "release": {"decision": release, "notes": []},
    }


def test_contract_generalizes_justification_to_every_manuscript_element() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "every retained element must perform a justified",
        "hierarchical justification tree",
        "deletion test",
        "placement test",
        "representation test",
        "paragraph contract",
        "sentence and clause discipline",
        "citation justification",
        "equation, definition, theorem and formal-element justification",
        "adaptive audit granularity",
        "if an element cannot explain why it exists",
    ):
        assert marker in text, marker


def test_kernel_keeps_compact_element_justification_invariant_ambient() -> None:
    text = KERNEL.read_text(encoding="utf-8").lower()
    assert "every retained manuscript element must earn its place" in text
    assert "manuscript-element-justification.md" in text


def test_schema_and_verifier_exist() -> None:
    assert SCHEMA.exists()
    assert VERIFIER.exists()


def test_valid_all_paragraph_final_ledger_passes() -> None:
    verifier = _load_verifier()
    result = verifier.validate(_ledger())
    assert result["decision"] == "PASS"


def test_retained_element_without_function_blocks() -> None:
    verifier = _load_verifier()
    ledger = _ledger(release="BLOCKED")
    ledger["elements"][1]["functions"] = []
    result = verifier.validate(ledger)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "retained_without_function" for item in result["findings"])


def test_redundant_element_kept_triggers_review_not_fake_deletion_quota() -> None:
    verifier = _load_verifier()
    ledger = _ledger(release="REVIEW")
    ledger["elements"][2]["redundancy"] = {"status": "redundant", "reason": "duplicates the prior paragraph's interpretation"}
    result = verifier.validate(ledger)
    assert result["decision"] == "REVIEW"
    assert any(item["code"] == "redundant_element_kept" for item in result["findings"])


def test_final_targeted_only_audit_is_unresolved_for_universal_release_claim() -> None:
    verifier = _load_verifier()
    ledger = _ledger(release="UNRESOLVED")
    ledger["scope"]["coverage"] = "targeted"
    result = verifier.validate(ledger)
    assert result["decision"] == "UNRESOLVED"
    assert any(item["code"] == "final_paragraph_coverage_incomplete" for item in result["findings"])


def test_protected_element_cannot_be_deleted_for_concision() -> None:
    verifier = _load_verifier()
    ledger = _ledger(release="BLOCKED")
    item = ledger["elements"][1]
    item["status"] = "delete"
    item["placement"] = "omit"
    item["protected_by"] = ["reporting_standard_requires_primary_outcome"]
    result = verifier.validate(ledger)
    assert result["decision"] == "BLOCKED"
    assert any(entry["code"] == "protected_element_deleted" for entry in result["findings"])


def test_missing_parent_blocks_hierarchy() -> None:
    verifier = _load_verifier()
    ledger = _ledger(release="BLOCKED")
    ledger["elements"][1]["parent_id"] = "missing-section"
    result = verifier.validate(ledger)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "parent_missing" for item in result["findings"])


def test_no_reader_state_change_without_scaffolding_function_is_review_signal() -> None:
    verifier = _load_verifier()
    ledger = _ledger(release="REVIEW")
    item = ledger["elements"][1]
    item["reader_state"]["after"] = item["reader_state"]["before"]
    result = verifier.validate(ledger)
    assert result["decision"] == "REVIEW"
    assert any(entry["code"] == "no_reader_state_change" for entry in result["findings"])
