from __future__ import annotations

import hashlib
import importlib.util
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path


SHARED = Path(__file__).parents[1]
SCHEMA = SHARED / "release-contracts" / "publication-release-manifest.schema.json"
CONTRACT = SHARED / "core" / "publication-release-integrity.md"
SCRIPT = SHARED / "scripts" / "verify_publication_release.py"
INTEGRITY = SHARED / "core" / "research-integrity-verification.md"
ACADEMIC_WRITING = SHARED.parent / "academic-writing" / "SKILL.md"
ACADEMIC_WRITING_MANIFEST = SHARED.parent / "academic-writing" / "manifest.yaml"
PIPELINE_MANIFEST = SHARED.parent / "academic-paper-pipeline" / "manifest.yaml"
PIPELINE_SKILL = SHARED.parent / "academic-paper-pipeline" / "SKILL.md"
SHARED_MANIFEST = SHARED / "manifest.yaml"


def _sha(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def _load_verifier():
    assert SCRIPT.exists(), "publication release verifier is missing"
    spec = importlib.util.spec_from_file_location("verify_publication_release", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write_release(tmp_path: Path) -> tuple[dict, Path]:
    manuscript = b"final reader-facing manuscript bytes\n"
    cover = b"final cover letter bytes\n"
    (tmp_path / "paper.pdf").write_bytes(manuscript)
    (tmp_path / "cover.pdf").write_bytes(cover)

    now = datetime.now(timezone.utc).isoformat()
    ledger = {
        "schema_version": "1.0",
        "manuscript_id": "manuscript:orion-01-final",
        "manuscript_fingerprint": _sha(manuscript),
        "authoring_agent_id": "writer-agent",
        "verification_scope": "full_manuscript",
        "coverage_check": {
            "status": "PASS",
            "verifier_id": "coverage-reviewer",
            "verification_method": "independent_model_with_retrieved_source",
            "checked_at": now,
        },
        "sources": [
            {
                "source_id": "S1",
                "source_type": "test_fixture",
                "identifiers": [
                    {"scheme": "url", "value": "https://example.invalid/test-fixture"}
                ],
                "bibliographic": {
                    "title": "Publication release verifier test fixture",
                    "authors": ["Test Author"],
                    "year": 2026,
                    "venue": "Local test fixture",
                },
                "declared_publication_status": "ACTIVE",
                "identity_checks": [
                    {
                        "provider": "local-test",
                        "status": "MATCH",
                        "checked_at": now,
                        "verification_method": "authoritative_project_record",
                        "verifier_id": "fixture-verifier",
                    }
                ],
                "status_checks": [
                    {
                        "provider": "local-test",
                        "status": "ACTIVE",
                        "checked_at": now,
                        "verification_method": "authoritative_project_record",
                        "verifier_id": "fixture-verifier",
                    }
                ],
            }
        ],
        "claims": [
            {
                "claim_id": "C1",
                "location": "paper.pdf:1",
                "text": "The reader-facing test manuscript contains the declared text.",
                "claim_class": "literature_fact",
                "risk": "normal",
                "release_status": "VERIFIED",
                "independent_check": {
                    "status": "PASS",
                    "verifier_id": "claim-reviewer",
                },
            }
        ],
        "evidence_receipts": [
            {
                "receipt_id": "E1",
                "claim_id": "C1",
                "warrant_type": "source",
                "source_id": "S1",
                "locator": "Complete local test fixture",
                "evidence_fingerprint": "sha256:" + "0" * 64,
                "verification_method": "human_review",
                "support_status": "ENTAILS",
                "scope_match": "MATCH",
                "verifier_id": "claim-reviewer",
            }
        ],
        "citation_usages": [
            {
                "citation_id": "R1",
                "source_id": "S1",
                "location": "paper.pdf:1",
                "claim_ids": ["C1"],
            }
        ],
        "release": {"requested_state": "submission_ready"},
    }
    ledger_bytes = (json.dumps(ledger, sort_keys=True) + "\n").encode()
    (tmp_path / "claim-ledger.json").write_bytes(ledger_bytes)

    archive_path = tmp_path / "submission.zip"
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_STORED) as archive:
        archive.writestr("paper.pdf", manuscript)
        archive.writestr("cover.pdf", cover)
    archive_bytes = archive_path.read_bytes()

    manifest = {
        "schema_version": "1.0",
        "release_id": "release:orion-01-final",
        "canonical_paper_id": "ORION-01",
        "requested_state": "submission_ready",
        "authority": {
            "manuscript_id": "manuscript:orion-01-final",
            "manuscript_artifact_id": "artifact:paper",
            "claim_ledger_artifact_id": "artifact:claim-ledger",
        },
        "manuscript_candidates": [
            {
                "manuscript_id": "manuscript:orion-01-final",
                "artifact_id": "artifact:paper",
                "sha256": _sha(manuscript),
                "disposition": "authoritative",
                "reason": "Current journal-facing manuscript selected for this release.",
            },
            {
                "manuscript_id": "manuscript:orion-01-old",
                "sha256": "sha256:" + "1" * 64,
                "disposition": "superseded",
                "superseded_by": "manuscript:orion-01-final",
                "reason": "Earlier manuscript retained only as provenance.",
            },
        ],
        "artifacts": [
            {
                "artifact_id": "artifact:paper",
                "role": "reader_manuscript",
                "path": "paper.pdf",
                "sha256": _sha(manuscript),
                "byte_count": len(manuscript),
            },
            {
                "artifact_id": "artifact:cover",
                "role": "submission_component",
                "path": "cover.pdf",
                "sha256": _sha(cover),
                "byte_count": len(cover),
            },
            {
                "artifact_id": "artifact:claim-ledger",
                "role": "claim_ledger",
                "path": "claim-ledger.json",
                "sha256": _sha(ledger_bytes),
                "byte_count": len(ledger_bytes),
            },
        ],
        "package": {
            "path": "submission.zip",
            "format": "zip",
            "sha256": _sha(archive_bytes),
            "byte_count": len(archive_bytes),
            "members": [
                {"member_path": "paper.pdf", "artifact_id": "artifact:paper"},
                {"member_path": "cover.pdf", "artifact_id": "artifact:cover"},
            ],
        },
    }
    manifest_path = tmp_path / "release-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest, manifest_path


def _validate(manifest: dict, manifest_path: Path) -> dict:
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return _load_verifier().validate_release(manifest, manifest_path=manifest_path)


def test_valid_release_binds_authority_ledger_artifacts_and_exact_zip(
    tmp_path: Path,
) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    report = _validate(manifest, manifest_path)
    assert report["decision"] == "PASS", report
    assert report["verified_artifact_count"] == 3
    assert report["verified_package_member_count"] == 2
    assert report["research_integrity_decision"] == "PASS"
    assert report["release_manifest_sha256"] == _sha(manifest_path.read_bytes())
    assert report["release_manifest_byte_count"] == len(manifest_path.read_bytes())


def test_competing_manuscripts_require_exactly_one_authority(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    manifest["manuscript_candidates"][1]["disposition"] = "authoritative"
    report = _validate(manifest, manifest_path)
    assert any("exactly one authoritative" in error for error in report["errors"])


def test_superseded_candidate_requires_reason_and_successor(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    old = manifest["manuscript_candidates"][1]
    old.pop("reason")
    old.pop("superseded_by")
    report = _validate(manifest, manifest_path)
    assert any(
        "superseded candidate" in error and "reason" in error
        for error in report["errors"]
    )
    assert any(
        "superseded candidate" in error and "superseded_by" in error
        for error in report["errors"]
    )


def test_superseded_candidate_successor_must_exist_in_inventory(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    manifest["manuscript_candidates"][1]["superseded_by"] = "manuscript:missing"
    report = _validate(manifest, manifest_path)
    assert report["decision"] == "BLOCKED"
    assert any("unknown superseded_by" in error for error in report["errors"])


def test_claim_ledger_must_fingerprint_canonical_reader_manuscript(
    tmp_path: Path,
) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    ledger_path = tmp_path / "claim-ledger.json"
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    ledger["manuscript_fingerprint"] = "sha256:" + "0" * 64
    ledger_bytes = (json.dumps(ledger, sort_keys=True) + "\n").encode()
    ledger_path.write_bytes(ledger_bytes)
    claim_artifact = next(
        x for x in manifest["artifacts"] if x["artifact_id"] == "artifact:claim-ledger"
    )
    claim_artifact["sha256"] = _sha(ledger_bytes)
    claim_artifact["byte_count"] = len(ledger_bytes)
    report = _validate(manifest, manifest_path)
    assert any(
        "claim-ledger manuscript_fingerprint" in error for error in report["errors"]
    )


def test_final_artifact_mutation_blocks_release(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    (tmp_path / "paper.pdf").write_bytes(b"mutated after verification\n")
    report = _validate(manifest, manifest_path)
    assert any(
        "artifact:paper" in error and "sha256 mismatch" in error
        for error in report["errors"]
    )


def test_exact_archive_byte_mutation_blocks_release(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    with (tmp_path / "submission.zip").open("ab") as handle:
        handle.write(b"post-verification bytes")
    report = _validate(manifest, manifest_path)
    assert any("package sha256 mismatch" in error for error in report["errors"])
    assert any("package byte_count mismatch" in error for error in report["errors"])


def test_stale_or_extra_package_member_blocks_release(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    with zipfile.ZipFile(
        tmp_path / "submission.zip", "w", compression=zipfile.ZIP_STORED
    ) as archive:
        archive.writestr("paper.pdf", b"stale manuscript")
        archive.writestr("cover.pdf", (tmp_path / "cover.pdf").read_bytes())
        archive.writestr("old-paper.pdf", b"obsolete competing manuscript")
    package_bytes = (tmp_path / "submission.zip").read_bytes()
    manifest["package"]["sha256"] = _sha(package_bytes)
    manifest["package"]["byte_count"] = len(package_bytes)
    report = _validate(manifest, manifest_path)
    assert any("unexpected package member" in error for error in report["errors"])
    assert any(
        "paper.pdf" in error and "sha256 mismatch" in error
        for error in report["errors"]
    )


def test_extra_directory_named_zip_member_with_payload_blocks_release(
    tmp_path: Path,
) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    with zipfile.ZipFile(
        tmp_path / "submission.zip", "a", compression=zipfile.ZIP_STORED
    ) as archive:
        archive.writestr("undeclared/", b"payload hidden behind directory syntax")
    package_bytes = (tmp_path / "submission.zip").read_bytes()
    manifest["package"]["sha256"] = _sha(package_bytes)
    manifest["package"]["byte_count"] = len(package_bytes)
    report = _validate(manifest, manifest_path)
    assert report["decision"] == "BLOCKED", report
    assert any(
        "unexpected package member undeclared/" in error for error in report["errors"]
    )


def test_empty_zip_directory_entries_are_metadata_not_package_members(
    tmp_path: Path,
) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    with zipfile.ZipFile(
        tmp_path / "submission.zip", "a", compression=zipfile.ZIP_STORED
    ) as archive:
        archive.writestr("supplement/", b"")
    package_bytes = (tmp_path / "submission.zip").read_bytes()
    manifest["package"]["sha256"] = _sha(package_bytes)
    manifest["package"]["byte_count"] = len(package_bytes)
    report = _validate(manifest, manifest_path)
    assert report["decision"] == "PASS", report
    assert report["verified_package_member_count"] == 2


def test_paths_cannot_escape_release_root(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    manifest["artifacts"][0]["path"] = "../paper.pdf"
    report = _validate(manifest, manifest_path)
    assert any("safe relative path" in error for error in report["errors"])


def test_independent_file_upload_set_is_verified_without_forcing_a_zip(
    tmp_path: Path,
) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    manifest["package"] = {
        "format": "file_set",
        "members": [
            {"member_path": "paper.pdf", "artifact_id": "artifact:paper"},
            {"member_path": "cover.pdf", "artifact_id": "artifact:cover"},
        ],
    }
    report = _validate(manifest, manifest_path)
    assert report["decision"] == "PASS", report
    assert report["verified_package_member_count"] == 2


def test_malformed_package_is_blocked_instead_of_crashing(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    manifest["package"] = None
    report = _validate(manifest, manifest_path)
    assert report["decision"] == "BLOCKED"
    assert any("package must be an object" in error for error in report["errors"])


def test_malformed_authority_is_blocked_instead_of_crashing(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    manifest["authority"] = []
    report = _validate(manifest, manifest_path)
    assert report["decision"] == "BLOCKED"
    assert any("authority must be an object" in error for error in report["errors"])


def test_top_level_non_object_is_blocked_instead_of_crashing(tmp_path: Path) -> None:
    _, manifest_path = _write_release(tmp_path)
    manifest_path.write_text("[]\n", encoding="utf-8")
    report = _load_verifier().validate_release([], manifest_path=manifest_path)
    assert report["decision"] == "BLOCKED"
    assert any(
        "top-level JSON value must be an object" in error for error in report["errors"]
    )


def test_nonclosing_claim_ledger_blocks_release_even_when_hashes_match(
    tmp_path: Path,
) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    ledger_path = tmp_path / "claim-ledger.json"
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    ledger["claims"][0]["release_status"] = "SUPPORTED_INTERNAL"
    ledger_bytes = (json.dumps(ledger, sort_keys=True) + "\n").encode()
    ledger_path.write_bytes(ledger_bytes)
    claim_artifact = next(
        x for x in manifest["artifacts"] if x["artifact_id"] == "artifact:claim-ledger"
    )
    claim_artifact["sha256"] = _sha(ledger_bytes)
    claim_artifact["byte_count"] = len(ledger_bytes)
    report = _validate(manifest, manifest_path)
    assert report["research_integrity_decision"] == "BLOCKED"
    assert any("non-closing release_status" in error for error in report["errors"])


def test_unknown_schema_fields_fail_closed(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    manifest["looks_final"] = True
    manifest["artifacts"][0]["unbound_note"] = "ignore me"
    report = _validate(manifest, manifest_path)
    assert any(
        "manifest: unsupported field looks_final" in error for error in report["errors"]
    )
    assert any("unsupported field unbound_note" in error for error in report["errors"])


def test_symlink_cannot_escape_release_root(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    outside = tmp_path.parent / "outside-paper.pdf"
    outside.write_bytes((tmp_path / "paper.pdf").read_bytes())
    (tmp_path / "paper-link.pdf").symlink_to(outside)
    manuscript_artifact = next(
        x for x in manifest["artifacts"] if x["artifact_id"] == "artifact:paper"
    )
    manuscript_artifact["path"] = "paper-link.pdf"
    report = _validate(manifest, manifest_path)
    assert any(
        "resolved path escapes the release root" in error for error in report["errors"]
    )


def test_public_posting_ready_uses_the_same_integrity_gate(tmp_path: Path) -> None:
    manifest, manifest_path = _write_release(tmp_path)
    manifest["requested_state"] = "public_posting_ready"
    ledger_path = tmp_path / "claim-ledger.json"
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    ledger["release"]["requested_state"] = "public_posting_ready"
    ledger_bytes = (json.dumps(ledger, sort_keys=True) + "\n").encode()
    ledger_path.write_bytes(ledger_bytes)
    claim_artifact = next(
        x for x in manifest["artifacts"] if x["artifact_id"] == "artifact:claim-ledger"
    )
    claim_artifact["sha256"] = _sha(ledger_bytes)
    claim_artifact["byte_count"] = len(ledger_bytes)
    report = _validate(manifest, manifest_path)
    assert report["decision"] == "PASS", report
    assert report["research_integrity_decision"] == "PASS"


def test_contract_schema_and_transitive_pipeline_route_are_present() -> None:
    assert SCHEMA.exists()
    assert CONTRACT.exists()
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert schema["title"] == "Publication Release Integrity Manifest"
    contract = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "multiple manuscript/package authority",
        "final-byte binding",
        "claim-ledger -> canonical manuscript -> submission package",
        "exactly one authoritative",
        "sha-256 and byte count",
        "unexpected package member",
        "not a reproducible-build certificate",
    ):
        assert marker in contract, marker
    integrity = INTEGRITY.read_text(encoding="utf-8")
    assert "publication-release-integrity.md" in integrity
    assert "verify_publication_release.py" in integrity
    assert "publication-release-integrity.md" in ACADEMIC_WRITING.read_text(
        encoding="utf-8"
    )
    pipeline_skill = PIPELINE_SKILL.read_text(encoding="utf-8")
    assert "verify_publication_release.py" in pipeline_skill
    assert "exact mirror" in pipeline_skill
    for path in (ACADEMIC_WRITING_MANIFEST, PIPELINE_MANIFEST, SHARED_MANIFEST):
        text = path.read_text(encoding="utf-8")
        assert "publication-release-integrity.md" in text, path
    for path in (ACADEMIC_WRITING_MANIFEST, PIPELINE_MANIFEST):
        text = path.read_text(encoding="utf-8")
        assert "publication-release-manifest.schema.json" in text, path
        assert "verify_publication_release.py" in text, path
