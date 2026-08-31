from __future__ import annotations

import argparse
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
SCRIPT = SHARED / "scripts" / "verify_research_integrity.py"
SCHEMA = SHARED / "analysis-contracts" / "research-integrity-ledger.schema.json"
CONTRACT = SHARED / "core" / "research-integrity-verification.md"
EMPTY_SHA = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

spec = importlib.util.spec_from_file_location("verify_research_integrity", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def args(manuscript: Path | None = None) -> argparse.Namespace:
    return argparse.Namespace(
        timeout=1.0,
        user_agent="test",
        mailto=None,
        manuscript=manuscript,
        max_status_age_days=30,
    )


def valid_ledger(requested_state: str = "review") -> dict:
    now = datetime.now(timezone.utc).isoformat()
    return {
        "schema_version": "1.0",
        "manuscript_id": "paper-1",
        "manuscript_fingerprint": EMPTY_SHA,
        "authoring_agent_id": "writer-agent",
        "verification_scope": "full_manuscript",
        "coverage_check": {
            "status": "PASS",
            "verifier_id": "coverage-agent",
            "verification_method": "independent_model_with_retrieved_source",
            "checked_at": now,
            "reviewed_manuscript_fingerprint": EMPTY_SHA,
        },
        "sources": [
            {
                "source_id": "S1",
                "source_type": "journal_article",
                "identifiers": [{"scheme": "doi", "value": "10.0000/example"}],
                "bibliographic": {
                    "title": "Verified example",
                    "authors": ["Ada Smith"],
                    "year": 2024,
                    "venue": "Journal",
                },
                "declared_publication_status": "ACTIVE",
                "identity_checks": [
                    {
                        "provider": "crossref",
                        "status": "MATCH",
                        "checked_at": now,
                        "verification_method": "registry_lookup",
                        "verifier_id": "registry-tool",
                    }
                ],
                "status_checks": [
                    {
                        "provider": "crossref",
                        "status": "ACTIVE",
                        "checked_at": now,
                        "verification_method": "registry_lookup",
                        "verifier_id": "registry-tool",
                    }
                ],
            }
        ],
        "claims": [
            {
                "claim_id": "C1",
                "location": "Introduction:1",
                "text": "The verified example reports the stated result.",
                "claim_class": "literature_fact",
                "risk": "normal",
                "release_status": "VERIFIED",
                "independent_check": {"status": "PASS", "verifier_id": "reviewer-agent"},
            }
        ],
        "evidence_receipts": [
            {
                "receipt_id": "E1",
                "claim_id": "C1",
                "warrant_type": "source",
                "source_id": "S1",
                "locator": "Results, paragraph 2",
                "evidence_fingerprint": "sha256:" + "0" * 64,
                "verification_method": "fulltext_span_check",
                "support_status": "ENTAILS",
                "scope_match": "MATCH",
                "verifier_id": "evidence-reader",
            }
        ],
        "citation_usages": [
            {
                "citation_id": "R1",
                "source_id": "S1",
                "location": "Introduction:1",
                "claim_ids": ["C1"],
            }
        ],
        "release": {"requested_state": requested_state},
    }


def validate(ledger: dict, manuscript: Path | None = None) -> dict:
    return module.validate_ledger(ledger, live=False, args=args(manuscript))


def test_valid_release_ledger_passes(tmp_path: Path) -> None:
    manuscript = tmp_path / "paper.md"
    manuscript.write_bytes(b"")
    report = validate(valid_ledger("submission_ready"), manuscript)
    assert report["decision"] == "PASS", report
    assert report["error_count"] == 0


def test_public_posting_is_a_fail_closed_release_state(tmp_path: Path) -> None:
    manuscript = tmp_path / "paper.md"
    manuscript.write_bytes(b"")
    ledger = valid_ledger("public_posting_ready")
    ledger["claims"][0]["release_status"] = "SUPPORTED_INTERNAL"
    report = validate(ledger, manuscript)
    assert report["decision"] == "BLOCKED"
    assert any("non-closing release_status" in x for x in report["errors"])


def test_release_is_bound_to_exact_manuscript(tmp_path: Path) -> None:
    manuscript = tmp_path / "paper.md"
    manuscript.write_text("changed", encoding="utf-8")
    report = validate(valid_ledger("submission_ready"), manuscript)
    assert any("fingerprint does not match" in x for x in report["errors"])


def test_release_requires_coverage_fingerprint_for_exact_reviewed_manuscript(
    tmp_path: Path,
) -> None:
    manuscript = tmp_path / "paper.md"
    manuscript.write_bytes(b"")
    ledger = valid_ledger("submission_ready")
    ledger["coverage_check"].pop("reviewed_manuscript_fingerprint")
    report = validate(ledger, manuscript)
    assert report["decision"] == "BLOCKED"
    assert any(
        "coverage_check reviewed_manuscript_fingerprint" in x
        for x in report["errors"]
    )


def test_release_blocks_review_receipt_from_an_older_candidate(tmp_path: Path) -> None:
    manuscript = tmp_path / "paper.md"
    manuscript.write_bytes(b"")
    ledger = valid_ledger("submission_ready")
    ledger["coverage_check"]["reviewed_manuscript_fingerprint"] = (
        "sha256:" + "1" * 64
    )
    report = validate(ledger, manuscript)
    assert report["decision"] == "BLOCKED"
    assert any(
        "coverage_check reviewed_manuscript_fingerprint does not match" in x
        for x in report["errors"]
    )


def test_release_requires_full_manuscript_verification_scope(tmp_path: Path) -> None:
    manuscript = tmp_path / "paper.md"
    manuscript.write_bytes(b"")
    ledger = valid_ledger("submission_ready")
    ledger["verification_scope"] = "partial"
    report = validate(ledger, manuscript)
    assert report["decision"] == "BLOCKED"
    assert any("full_manuscript verification_scope" in x for x in report["errors"])


def test_release_requires_the_supported_ledger_schema_version(
    tmp_path: Path,
) -> None:
    manuscript = tmp_path / "paper.md"
    manuscript.write_bytes(b"")
    ledger = valid_ledger("submission_ready")
    ledger["schema_version"] = "0.0"
    report = validate(ledger, manuscript)
    assert report["decision"] == "BLOCKED"
    assert any("schema_version must be 1.0" in x for x in report["errors"])


def test_release_support_must_match_the_claim_scope(tmp_path: Path) -> None:
    manuscript = tmp_path / "paper.md"
    manuscript.write_bytes(b"")
    ledger = valid_ledger("submission_ready")
    ledger["evidence_receipts"][0]["scope_match"] = "NARROWER"
    report = validate(ledger, manuscript)
    assert report["decision"] == "BLOCKED"
    assert any("scope-matched receipt" in x for x in report["errors"])


def test_model_self_report_is_not_verification() -> None:
    ledger = valid_ledger()
    ledger["evidence_receipts"][0]["verification_method"] = "model_self_report"
    report = validate(ledger)
    assert report["decision"] == "BLOCKED"
    assert any("untrusted verification_method" in x for x in report["errors"])


def test_authoring_agent_cannot_self_certify_independent_check() -> None:
    ledger = valid_ledger()
    ledger["claims"][0]["independent_check"]["verifier_id"] = "writer-agent"
    report = validate(ledger)
    assert any("independent verifier must differ" in x for x in report["errors"])


def test_authoring_agent_cannot_self_certify_coverage() -> None:
    ledger = valid_ledger()
    ledger["coverage_check"]["verifier_id"] = "writer-agent"
    report = validate(ledger)
    assert any("coverage verifier must differ" in x for x in report["errors"])


def test_release_requires_identity_and_status_receipts(tmp_path: Path) -> None:
    manuscript = tmp_path / "paper.md"
    manuscript.write_bytes(b"")
    ledger = valid_ledger("submission_ready")
    ledger["sources"][0].pop("identity_checks")
    ledger["sources"][0].pop("status_checks")
    report = validate(ledger, manuscript)
    assert any("release requires a resolved identity check" in x for x in report["errors"])
    assert any("release requires a current publication-status check" in x for x in report["errors"])


def test_stale_publication_status_receipt_blocks_release(tmp_path: Path) -> None:
    manuscript = tmp_path / "paper.md"
    manuscript.write_bytes(b"")
    ledger = valid_ledger("submission_ready")
    ledger["sources"][0]["status_checks"][0]["checked_at"] = "2000-01-01T00:00:00Z"
    report = validate(ledger, manuscript)
    assert any("older than 30 days" in x for x in report["errors"])


def test_retracted_source_blocks_release() -> None:
    ledger = valid_ledger()
    ledger["sources"][0]["declared_publication_status"] = "RETRACTED"
    ledger["sources"][0]["status_checks"][0]["status"] = "RETRACTED"
    report = validate(ledger)
    assert any("publication status is RETRACTED" in x for x in report["errors"])


def test_citation_must_map_to_source_receipt_for_same_claim() -> None:
    ledger = valid_ledger()
    ledger["evidence_receipts"][0]["source_id"] = "S_OTHER"
    report = validate(ledger)
    assert any("no evidence receipt for claim C1" in x for x in report["errors"])


def test_high_risk_claim_requires_counterevidence_search() -> None:
    ledger = valid_ledger()
    ledger["claims"][0]["claim_class"] = "causal"
    ledger["claims"][0]["risk"] = "high"
    report = validate(ledger)
    assert any("requires counterevidence_search" in x for x in report["errors"])


def test_metadata_identity_comparison_rejects_wrong_source() -> None:
    source = valid_ledger()["sources"][0]
    ok, problems = module.compare_identity(
        source,
        {"title": "Completely unrelated paper", "authors": ["Other Person"], "year": 2020},
    )
    assert not ok
    assert any("title mismatch" in x for x in problems)
    assert any("year mismatch" in x for x in problems)
    assert any("first-author mismatch" in x for x in problems)


def test_contract_schema_and_pipeline_routing_are_present() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert schema["title"] == "Research Integrity Verification Ledger"
    assert "verification_scope" in schema["required"]
    coverage_schema = schema["$defs"]["coverageCheck"]
    assert "reviewed_manuscript_fingerprint" in coverage_schema["properties"]
    assert any(
        item.get("then", {}).get("required")
        == ["reviewed_manuscript_fingerprint"]
        for item in coverage_schema["allOf"]
    )
    for marker in ("manuscript_fingerprint", "coverage_check", "evidence_fingerprint"):
        assert marker in SCHEMA.read_text(encoding="utf-8")

    contract = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "phantom source",
        "semantic citation hallucination",
        "retrieval prompt injection",
        "evidence fingerprint",
        "independent verifier",
        "counterevidence",
        "verification_scope == full_manuscript",
        "scope_match == match",
    ):
        assert marker in contract

    for path in (
        SKILLS / "academic-paper-pipeline" / "manifest.yaml",
        SKILLS / "nature-citation" / "manifest.yaml",
    ):
        assert "research-integrity-verification.md" in path.read_text(encoding="utf-8"), str(path)
