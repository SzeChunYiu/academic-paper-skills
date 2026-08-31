#!/usr/bin/env python3
"""Verify canonical publication authority and exact release-package bytes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any


SHA256_RE = re.compile(r"^sha256:[0-9a-fA-F]{64}$")
RELEASE_STATES = {"submission_ready", "publication_ready", "public_posting_ready"}
CANDIDATE_DISPOSITIONS = {
    "authoritative",
    "superseded",
    "historical_provenance",
    "excluded_incompatible",
    "withdrawn",
    "quarantined",
}


def _sha256(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def _safe_relative_path(value: object) -> str | None:
    raw = str(value or "")
    if not raw or "\\" in raw or re.match(r"^[A-Za-z]:", raw):
        return None
    path = PurePosixPath(raw)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        return None
    return path.as_posix()


def _require(item: dict[str, Any], keys: tuple[str, ...], label: str, errors: list[str]) -> None:
    for key in keys:
        if key not in item or item[key] in (None, "", []):
            errors.append(f"{label}: missing required field {key}")


def _check_digest(value: object, label: str, errors: list[str]) -> None:
    if not SHA256_RE.fullmatch(str(value or "")):
        errors.append(f"{label}: sha256 must be sha256:<64 hex>")


def _read_artifact(
    artifact: dict[str, Any], root: Path, errors: list[str]
) -> tuple[Path | None, bytes | None]:
    artifact_id = str(artifact.get("artifact_id", "<missing>"))
    safe = _safe_relative_path(artifact.get("path"))
    if safe is None:
        errors.append(f"{artifact_id}: path must be a safe relative path")
        return None, None
    path = root / safe
    try:
        data = path.read_bytes()
    except OSError as exc:
        errors.append(f"{artifact_id}: cannot read artifact {safe}: {exc}")
        return path, None
    expected_sha = str(artifact.get("sha256", ""))
    expected_bytes = artifact.get("byte_count")
    if _sha256(data).casefold() != expected_sha.casefold():
        errors.append(f"{artifact_id}: sha256 mismatch")
    if not isinstance(expected_bytes, int) or isinstance(expected_bytes, bool) or expected_bytes < 0:
        errors.append(f"{artifact_id}: byte_count must be a non-negative integer")
    elif len(data) != expected_bytes:
        errors.append(f"{artifact_id}: byte_count mismatch ({len(data)} != {expected_bytes})")
    return path, data


def _validate_authority(
    manifest: dict[str, Any], artifacts: dict[str, dict[str, Any]], errors: list[str]
) -> None:
    authority = manifest.get("authority")
    if not isinstance(authority, dict):
        errors.append("manifest: authority must be an object")
        return
    _require(
        authority,
        ("manuscript_id", "manuscript_artifact_id", "claim_ledger_artifact_id"),
        "authority",
        errors,
    )
    candidates = manifest.get("manuscript_candidates")
    if not isinstance(candidates, list) or not candidates:
        errors.append("manifest: manuscript_candidates must be a non-empty array")
        return

    ids = [str(item.get("manuscript_id", "")) for item in candidates if isinstance(item, dict)]
    for candidate_id, count in Counter(ids).items():
        if not candidate_id:
            errors.append("manuscript candidate: missing required field manuscript_id")
        elif count > 1:
            errors.append(f"manuscript candidate: duplicate manuscript_id {candidate_id}")

    authoritative = []
    for index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            errors.append(f"manuscript_candidates[{index}]: must be an object")
            continue
        disposition = str(candidate.get("disposition", ""))
        label = f"{disposition or 'manuscript'} candidate {candidate.get('manuscript_id', index)}"
        _require(candidate, ("manuscript_id", "sha256", "disposition", "reason"), label, errors)
        _check_digest(candidate.get("sha256"), label, errors)
        if disposition not in CANDIDATE_DISPOSITIONS:
            errors.append(f"{label}: unsupported disposition {disposition!r}")
        if disposition == "authoritative":
            authoritative.append(candidate)
        elif disposition == "superseded" and not candidate.get("superseded_by"):
            errors.append(f"{label}: superseded candidate requires superseded_by")

    if len(authoritative) != 1:
        errors.append(
            f"manifest: exactly one authoritative manuscript candidate is required; found {len(authoritative)}"
        )
        return

    selected = authoritative[0]
    manuscript_id = str(authority.get("manuscript_id", ""))
    artifact_id = str(authority.get("manuscript_artifact_id", ""))
    if selected.get("manuscript_id") != manuscript_id:
        errors.append("authority: manuscript_id does not match the authoritative candidate")
    if selected.get("artifact_id") != artifact_id:
        errors.append("authority: manuscript_artifact_id does not match the authoritative candidate")
    artifact = artifacts.get(artifact_id)
    if artifact is None:
        errors.append(f"authority: unknown manuscript_artifact_id {artifact_id!r}")
    else:
        if artifact.get("role") != "reader_manuscript":
            errors.append("authority: canonical manuscript artifact must have role reader_manuscript")
        if str(selected.get("sha256", "")).casefold() != str(artifact.get("sha256", "")).casefold():
            errors.append("authority: authoritative candidate sha256 does not match manuscript artifact")
    ledger_id = str(authority.get("claim_ledger_artifact_id", ""))
    ledger_artifact = artifacts.get(ledger_id)
    if ledger_artifact is None:
        errors.append(f"authority: unknown claim_ledger_artifact_id {ledger_id!r}")
    elif ledger_artifact.get("role") != "claim_ledger":
        errors.append("authority: claim-ledger artifact must have role claim_ledger")


def _validate_claim_ledger_binding(
    manifest: dict[str, Any],
    artifacts: dict[str, dict[str, Any]],
    artifact_data: dict[str, bytes],
    errors: list[str],
) -> None:
    authority = manifest.get("authority")
    if not isinstance(authority, dict):
        return
    manuscript_id = str(authority.get("manuscript_id", ""))
    manuscript_artifact = artifacts.get(str(authority.get("manuscript_artifact_id", "")))
    ledger_id = str(authority.get("claim_ledger_artifact_id", ""))
    ledger_bytes = artifact_data.get(ledger_id)
    if manuscript_artifact is None or ledger_bytes is None:
        return
    try:
        ledger = json.loads(ledger_bytes)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        errors.append(f"{ledger_id}: claim ledger is not valid UTF-8 JSON: {exc}")
        return
    if ledger.get("manuscript_id") != manuscript_id:
        errors.append("claim-ledger manuscript_id does not match canonical authority")
    if str(ledger.get("manuscript_fingerprint", "")).casefold() != str(
        manuscript_artifact.get("sha256", "")
    ).casefold():
        errors.append("claim-ledger manuscript_fingerprint does not match canonical reader manuscript")
    ledger_state = str(ledger.get("release", {}).get("requested_state", ""))
    if ledger_state != str(manifest.get("requested_state", "")):
        errors.append("claim-ledger requested_state does not match publication release manifest")


def _validate_zip_package(
    package: dict[str, Any],
    root: Path,
    artifacts: dict[str, dict[str, Any]],
    errors: list[str],
) -> int:
    safe = _safe_relative_path(package.get("path"))
    if safe is None:
        errors.append("package: path must be a safe relative path")
        return 0
    path = root / safe
    try:
        package_bytes = path.read_bytes()
    except OSError as exc:
        errors.append(f"package: cannot read {safe}: {exc}")
        return 0
    if _sha256(package_bytes).casefold() != str(package.get("sha256", "")).casefold():
        errors.append("package sha256 mismatch")
    expected_size = package.get("byte_count")
    if not isinstance(expected_size, int) or isinstance(expected_size, bool) or expected_size < 0:
        errors.append("package: byte_count must be a non-negative integer")
    elif len(package_bytes) != expected_size:
        errors.append(f"package byte_count mismatch ({len(package_bytes)} != {expected_size})")

    declared_members = package.get("members")
    if not isinstance(declared_members, list) or not declared_members:
        errors.append("package: members must be a non-empty array")
        return 0
    expected: dict[str, str] = {}
    for index, member in enumerate(declared_members):
        if not isinstance(member, dict):
            errors.append(f"package.members[{index}]: must be an object")
            continue
        member_path = _safe_relative_path(member.get("member_path"))
        if member_path is None:
            errors.append(f"package.members[{index}]: member_path must be a safe relative path")
            continue
        if member_path in expected:
            errors.append(f"package: duplicate declared member {member_path}")
        expected[member_path] = str(member.get("artifact_id", ""))
        if expected[member_path] not in artifacts:
            errors.append(f"package member {member_path}: unknown artifact_id {expected[member_path]!r}")

    try:
        with zipfile.ZipFile(path) as archive:
            infos = [info for info in archive.infolist() if not info.is_dir()]
            actual_names = [info.filename for info in infos]
            for name, count in Counter(actual_names).items():
                if count > 1:
                    errors.append(f"package: duplicate archive member {name}")
            actual = set(actual_names)
            for extra in sorted(actual - set(expected)):
                errors.append(f"unexpected package member {extra}")
            for missing in sorted(set(expected) - actual):
                errors.append(f"missing package member {missing}")
            for member_path in sorted(actual & set(expected)):
                artifact = artifacts.get(expected[member_path])
                if artifact is None:
                    continue
                data = archive.read(member_path)
                if _sha256(data).casefold() != str(artifact.get("sha256", "")).casefold():
                    errors.append(f"package member {member_path}: sha256 mismatch")
                if len(data) != artifact.get("byte_count"):
                    errors.append(f"package member {member_path}: byte_count mismatch")
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        errors.append(f"package: invalid or unreadable zip: {exc}")
        return 0
    return len(expected)


def _validate_file_set(
    package: dict[str, Any], artifacts: dict[str, dict[str, Any]], errors: list[str]
) -> int:
    members = package.get("members")
    if not isinstance(members, list) or not members:
        errors.append("package: members must be a non-empty array")
        return 0
    seen: set[str] = set()
    for index, member in enumerate(members):
        if not isinstance(member, dict):
            errors.append(f"package.members[{index}]: must be an object")
            continue
        member_path = _safe_relative_path(member.get("member_path"))
        artifact_id = str(member.get("artifact_id", ""))
        if member_path is None:
            errors.append(f"package.members[{index}]: member_path must be a safe relative path")
        elif member_path in seen:
            errors.append(f"package: duplicate declared member {member_path}")
        else:
            seen.add(member_path)
        artifact = artifacts.get(artifact_id)
        if artifact is None:
            errors.append(f"package member {member_path}: unknown artifact_id {artifact_id!r}")
        elif member_path != _safe_relative_path(artifact.get("path")):
            errors.append(f"package member {member_path}: file_set path does not match artifact path")
    return len(seen)


def validate_release(manifest: dict[str, Any], *, manifest_path: Path) -> dict[str, Any]:
    """Return a fail-closed report for one publication release manifest."""
    errors: list[str] = []
    try:
        manifest_bytes = manifest_path.read_bytes()
    except OSError as exc:
        errors.append(f"manifest: cannot read release manifest bytes: {exc}")
        manifest_bytes = b""
    _require(
        manifest,
        (
            "schema_version",
            "release_id",
            "canonical_paper_id",
            "requested_state",
            "authority",
            "manuscript_candidates",
            "artifacts",
            "package",
        ),
        "manifest",
        errors,
    )
    if manifest.get("schema_version") != "1.0":
        errors.append("manifest: schema_version must be 1.0")
    if manifest.get("requested_state") not in RELEASE_STATES:
        errors.append(f"manifest: unsupported requested_state {manifest.get('requested_state')!r}")

    root = manifest_path.resolve().parent
    items = manifest.get("artifacts")
    if not isinstance(items, list) or not items:
        errors.append("manifest: artifacts must be a non-empty array")
        items = []
    artifacts: dict[str, dict[str, Any]] = {}
    artifact_data: dict[str, bytes] = {}
    seen_paths: set[str] = set()
    for index, artifact in enumerate(items):
        if not isinstance(artifact, dict):
            errors.append(f"artifacts[{index}]: must be an object")
            continue
        label = f"artifact {artifact.get('artifact_id', index)}"
        _require(artifact, ("artifact_id", "role", "path", "sha256", "byte_count"), label, errors)
        artifact_id = str(artifact.get("artifact_id", ""))
        if artifact_id in artifacts:
            errors.append(f"manifest: duplicate artifact_id {artifact_id}")
            continue
        artifacts[artifact_id] = artifact
        _check_digest(artifact.get("sha256"), artifact_id, errors)
        safe = _safe_relative_path(artifact.get("path"))
        if safe and safe in seen_paths:
            errors.append(f"manifest: duplicate artifact path {safe}")
        elif safe:
            seen_paths.add(safe)
        _, data = _read_artifact(artifact, root, errors)
        if data is not None:
            artifact_data[artifact_id] = data

    _validate_authority(manifest, artifacts, errors)
    _validate_claim_ledger_binding(manifest, artifacts, artifact_data, errors)

    package = manifest.get("package")
    member_count = 0
    if not isinstance(package, dict):
        errors.append("manifest: package must be an object")
    else:
        package_format = package.get("format")
        if package_format == "zip":
            _require(package, ("path", "sha256", "byte_count", "members"), "package", errors)
            _check_digest(package.get("sha256"), "package", errors)
            member_count = _validate_zip_package(package, root, artifacts, errors)
        elif package_format == "file_set":
            member_count = _validate_file_set(package, artifacts, errors)
        else:
            errors.append(f"package: unsupported format {package_format!r}; use zip or file_set")

    authority = manifest.get("authority")
    if not isinstance(authority, dict):
        authority = {}
    canonical_artifact_id = str(authority.get("manuscript_artifact_id", ""))
    declared_members = package.get("members", []) if isinstance(package, dict) else []
    member_artifact_ids = {
        str(member.get("artifact_id", "")) for member in declared_members if isinstance(member, dict)
    }
    if canonical_artifact_id and canonical_artifact_id not in member_artifact_ids:
        errors.append("package: canonical reader manuscript is not included in the declared submission package")

    return {
        "decision": "BLOCKED" if errors else "PASS",
        "error_count": len(errors),
        "errors": errors,
        "verified_artifact_count": len(artifact_data),
        "verified_package_member_count": member_count,
        "release_id": manifest.get("release_id"),
        "canonical_paper_id": manifest.get("canonical_paper_id"),
        "release_manifest_sha256": _sha256(manifest_bytes) if manifest_bytes else None,
        "release_manifest_byte_count": len(manifest_bytes) if manifest_bytes else None,
        "notes": [
            "PASS binds the recorded authority, claim ledger, artifact bytes and declared package only.",
            "PASS does not certify scientific truth, reproducible rebuilding, journal compliance, repository custody or acceptance.",
        ],
    }


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("manifest", type=Path)
    p.add_argument("--pretty", action="store_true")
    p.add_argument("--report", type=Path)
    return p


def main() -> int:
    args = parser().parse_args()
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"decision": "BLOCKED", "errors": [f"cannot read manifest: {exc}"]}))
        return 1
    report = validate_release(manifest, manifest_path=args.manifest)
    rendered = json.dumps(report, ensure_ascii=False, indent=2 if args.pretty else None)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["decision"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
