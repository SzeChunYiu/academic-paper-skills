#!/usr/bin/env python3
"""Conservative manuscript-independence and reader-context audit.

This scanner detects high-confidence repository/project leakage and review-worthy
opaque project vocabulary. It does not decide whether an identifier is
scientifically necessary; contextual review remains authoritative.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


MACHINE_TERMINAL_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+){2,}\b")
OPAQUE_ID_RE = re.compile(r"\b(?:D|M|A|V|P|H)\d+(?:[-.][A-Z0-9]+)*\b")
PATH_RE = re.compile(
    r"(?<![\w.-])(?:src|protocol|evidence|development|research|papers|host|gold|figures|reproducibility|literature)/"
    r"[A-Za-z0-9_./-]+"
)
CLI_RE = re.compile(r"^\s*(?:python(?:3)?|make|pytest|git|pip|conda|poetry|uv)\s+\S+", re.MULTILINE)
SHA_RE = re.compile(r"\b[0-9a-f]{40}\b|\b[0-9a-f]{64}\b", re.IGNORECASE)
PAPER_SERIES_RE = re.compile(r"\bPaper\s+(?:[IVX]+|\d+)\b", re.IGNORECASE)
ARXIV_RE = re.compile(r"\barXiv\s+(?:preprint|:)", re.IGNORECASE)
REFERENCE_START_RE = re.compile(r"^\s*(?:References|Bibliography)\s*$", re.IGNORECASE | re.MULTILINE)

PRIVATE_PHRASES = (
    "claim subtraction",
    "donor family",
    "donor families",
    "donor-owned",
    "donor-complete",
    "strongest parent",
    "nearest-work audit",
    "nearest work audit",
    "post-saturation successor",
    "microgate",
    "programme terminal",
    "program terminal",
    "exact terminal is",
    "retained terminal is",
)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def excerpt(text: str, start: int, end: int, limit: int = 180) -> str:
    left = text.rfind("\n", 0, start) + 1
    right = text.find("\n", end)
    if right < 0:
        right = len(text)
    value = " ".join(text[left:right].split())
    return value[:limit]


def add_finding(
    findings: list[dict[str, Any]],
    *,
    code: str,
    severity: str,
    message: str,
    text: str,
    start: int,
    end: int,
    token: str | None = None,
) -> None:
    findings.append(
        {
            "code": code,
            "severity": severity,
            "line": line_number(text, start),
            "token": token,
            "message": message,
            "excerpt": excerpt(text, start, end),
        }
    )


def audit(text: str) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []

    for match in MACHINE_TERMINAL_RE.finditer(text):
        token = match.group(0)
        if len(token) < 24:
            continue
        add_finding(
            findings,
            code="machine_terminal_leak",
            severity="error",
            message=(
                "Long upper-snake machine/audit terminal appears in manuscript-facing text. "
                "Translate to a reader-facing scientific outcome and keep the exact terminal in the artifact record unless it is itself the study object."
            ),
            text=text,
            start=match.start(),
            end=match.end(),
            token=token,
        )

    for match in PATH_RE.finditer(text):
        add_finding(
            findings,
            code="repository_path_leak",
            severity="review",
            message=(
                "Repository/file path appears in manuscript-facing text. Prefer one persistent access location plus an external machine-readable manifest unless this exact path is required by the venue or claim."
            ),
            text=text,
            start=match.start(),
            end=match.end(),
            token=match.group(0),
        )

    for match in CLI_RE.finditer(text):
        add_finding(
            findings,
            code="cli_leak",
            severity="review",
            message="CLI/reproduction command is usually artifact documentation rather than scientific narrative.",
            text=text,
            start=match.start(),
            end=match.end(),
            token=match.group(0).strip(),
        )

    for phrase in PRIVATE_PHRASES:
        for match in re.finditer(re.escape(phrase), text, re.IGNORECASE):
            add_finding(
                findings,
                code="private_authoring_vocabulary",
                severity="review",
                message=(
                    "Private research-management vocabulary appears in the manuscript. Replace it with ordinary scholarly positioning or define it only if it is genuinely a scientific object."
                ),
                text=text,
                start=match.start(),
                end=match.end(),
                token=match.group(0),
            )

    for match in PAPER_SERIES_RE.finditer(text):
        add_finding(
            findings,
            code="paper_series_dependency",
            severity="review",
            message=(
                "Paper-series shorthand may assume prior programme context. Ensure the current manuscript restates the minimum scientific identity needed to stand alone."
            ),
            text=text,
            start=match.start(),
            end=match.end(),
            token=match.group(0),
        )

    opaque_counts: Counter[str] = Counter(match.group(0) for match in OPAQUE_ID_RE.finditer(text))
    first_seen: set[str] = set()
    for match in OPAQUE_ID_RE.finditer(text):
        token = match.group(0)
        if token in first_seen:
            continue
        first_seen.add(token)
        add_finding(
            findings,
            code="opaque_project_id_first_use",
            severity="review",
            message=(
                f"First occurrence of opaque identifier {token}. Confirm that a reader-facing scientific name/definition appears before or at this use; the ID should normally be secondary shorthand."
            ),
            text=text,
            start=match.start(),
            end=match.end(),
            token=token,
        )

    if len(opaque_counts) >= 6 or sum(opaque_counts.values()) >= 20:
        findings.append(
            {
                "code": "opaque_id_density",
                "severity": "review",
                "line": None,
                "token": None,
                "message": (
                    "High density of project-like experiment/version identifiers. Check whether the manuscript is narrating project genealogy rather than the smallest set of scientifically distinct studies."
                ),
                "excerpt": ", ".join(f"{key}×{value}" for key, value in opaque_counts.most_common(12)),
            }
        )

    sha_matches = list(SHA_RE.finditer(text))
    if len(sha_matches) >= 3:
        findings.append(
            {
                "code": "hash_manifest_density",
                "severity": "review",
                "line": line_number(text, sha_matches[0].start()),
                "token": None,
                "message": (
                    "Multiple raw commit/SHA-256 identifiers appear in the manuscript. Prefer a persistent archive plus machine-readable manifest unless individual hashes are scientifically consequential."
                ),
                "excerpt": f"{len(sha_matches)} raw 40/64-hex identifiers detected",
            }
        )

    ref_match = REFERENCE_START_RE.search(text)
    reference_text = text[ref_match.end() :] if ref_match else text
    preprint_count = len(ARXIV_RE.findall(reference_text))
    if preprint_count >= 5:
        findings.append(
            {
                "code": "preprint_concentration",
                "severity": "review",
                "line": line_number(text, ref_match.start()) if ref_match else None,
                "token": None,
                "message": (
                    "Reference set contains many explicit arXiv/preprint entries. Run a version-of-record audit and confirm that mature background claims are not being supported by preprints merely from search convenience."
                ),
                "excerpt": f"{preprint_count} explicit arXiv/preprint reference markers detected",
            }
        )

    counts = Counter(item["severity"] for item in findings)
    return {
        "decision": "BLOCKED" if counts["error"] else ("REVIEW" if counts["review"] else "PASS"),
        "counts": {"error": counts["error"], "review": counts["review"]},
        "findings": findings,
        "notes": [
            "Opaque IDs and preprint concentration are review signals, not automatic scientific errors.",
            "A contextual zero-reader audit must decide whether each identifier or source is necessary and adequately defined.",
        ],
    }


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Audit manuscript text for project-context and reader-independence failures.")
    p.add_argument("manuscript", type=Path)
    p.add_argument("--pretty", action="store_true")
    p.add_argument("--strict", action="store_true", help="Return nonzero when high-confidence errors are present.")
    p.add_argument("--fail-on-review", action="store_true", help="Return nonzero for review findings as well as errors.")
    p.add_argument("--report", type=Path)
    return p


def main() -> int:
    args = parser().parse_args()
    text = args.manuscript.read_text(encoding="utf-8")
    payload = audit(text)
    rendered = json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if args.fail_on_review and payload["decision"] != "PASS":
        return 1
    if args.strict and payload["counts"]["error"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
