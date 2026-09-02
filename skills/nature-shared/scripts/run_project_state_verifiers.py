#!/usr/bin/env python3
"""Run the registered verifier chain over an academic-paper project state.

The runner is registry-driven and artifact-driven: each registered check
declares the project stages it applies to, whether it needs the network, and
which artifact it consumes. Checks report PASS / FAIL / SKIPPED / CANNOT_CHECK
— a missing optional input is SKIPPED with its reason, never a silent PASS.
The run appends a ``verifier_run`` event to the project-state hash-chained
ledger (creating the ledger if none exists) and exits 0 only when no check
FAILed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

SCRIPTS_DIR = Path(__file__).resolve().parent
SHARED_DIR = SCRIPTS_DIR.parent
DEFAULT_STATE = SHARED_DIR.parents[2] / "docs" / "academic-paper-project-state.template.yaml"

RUNNER_VERSION = "1.0.0"
STAGES = ("planning", "drafting", "pre_submission", "revision", "post_publication")
ALL_STAGES = frozenset(STAGES)
LATER_STAGES = frozenset({"drafting", "pre_submission", "revision", "post_publication"})

KNOWN_ID_PREFIXES = (
    "project:", "agent:", "hypothesis:", "claim:", "study:", "result-type:",
    "reporting:", "adapter:", "contract:", "study-contract:", "data-contract:",
    "stat-contract:", "protocol:", "analysis-plan:", "analysis:", "result:",
    "data:", "data-source:", "data-snapshot:", "data-transform:", "data-qc:",
    "data-decision:", "question:", "estimand:", "population:", "sensitivity:",
    "surface:", "search:", "source:", "passage:", "validation:",
    "figure:", "table:", "display-contract:", "manuscript:", "declaration:",
    "review-packet:", "concern:", "target-projection:", "deviation:",
)

EXIT_OK = 0
EXIT_DEFECT = 1
EXIT_CANNOT_CHECK = 2


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {name} from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_module("validate_project_state", SCRIPTS_DIR / "validate_project_state.py")
LEDGER = load_module("project_state_ledger", SCRIPTS_DIR / "project_state_ledger.py")


@dataclass
class CheckResult:
    check: str
    status: str  # PASS | FAIL | SKIPPED | CANNOT_CHECK
    reason: str | None = None
    details: dict[str, Any] = field(default_factory=dict)


@dataclass
class Check:
    name: str
    description: str
    stages: frozenset[str]
    network: bool
    run: Callable[[dict[str, Any], argparse.Namespace], CheckResult]


def is_known_id(value: Any) -> bool:
    return isinstance(value, str) and any(value.startswith(prefix) for prefix in KNOWN_ID_PREFIXES)


def walk_id_bindings(doc: Any) -> tuple[set[str], set[str], int]:
    """Collect declared ids (under key ``id``) and referenced ids (under
    ``*_id`` / ``*_ids`` / ``intended_headline_claims`` keys).

    Returns (declared, referenced, placeholder_reference_count). Reference
    strings containing ``REPLACE_ME`` are counted but not treated as bindings,
    because placeholder elimination belongs to the per-contract resolvers.
    """
    declared: set[str] = set()
    referenced: set[str] = set()
    placeholders = 0

    def visit(node: Any, binding: str | None) -> None:
        nonlocal placeholders
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "id":
                    visit(value, "declare")
                elif key.endswith("_id") or key.endswith("_ids") or key == "intended_headline_claims":
                    visit(value, "reference")
                else:
                    visit(value, None)
        elif isinstance(node, list):
            for item in node:
                visit(item, binding)
        elif isinstance(node, str) and is_known_id(node):
            if binding == "declare":
                declared.add(node)
            elif binding == "reference":
                if "REPLACE_ME" in node:
                    placeholders += 1
                else:
                    referenced.add(node)

    visit(doc, None)
    return declared, referenced, placeholders


def run_schema_check(doc: dict, args: argparse.Namespace) -> CheckResult:
    errors = VALIDATOR.iter_validation_errors(doc, args.schema_doc)
    if errors:
        return CheckResult(
            "schema",
            "FAIL",
            reason=f"{len(errors)} structural error(s)",
            details={"errors": errors[:10], "error_count": len(errors)},
        )
    return CheckResult("schema", "PASS", details={"error_count": 0})


def run_placeholder_census(doc: dict, args: argparse.Namespace) -> CheckResult:
    counts = {"REPLACE_ME": 0, "date_placeholders": 0}
    text = json.dumps(doc, ensure_ascii=False)
    counts["REPLACE_ME"] = text.count("REPLACE_ME")
    counts["date_placeholders"] = text.count("YYYY-MM-DD")
    return CheckResult(
        "placeholder_census",
        "PASS",
        details={"counts": counts, "note": "placeholder elimination is owned by the per-contract resolvers"},
    )


def run_id_integrity(doc: dict, args: argparse.Namespace) -> CheckResult:
    declared, referenced, placeholders = walk_id_bindings(doc)
    missing = sorted(referenced - declared)
    details = {
        "declared_count": len(declared),
        "bound_reference_count": len(referenced),
        "placeholder_reference_count": placeholders,
    }
    if stage_of(doc) == "planning":
        # The planning-stage template legitimately carries exemplar forward
        # references (e.g. data-source:, display-contract:, surface:) that get
        # bound as the contracts are filled in. Report them as a census; from
        # drafting onward every reference must resolve.
        details["dangling"] = missing[:20]
        details["dangling_count"] = len(missing)
        details["note"] = "census only at planning; enforced from drafting onward"
        return CheckResult("id_integrity", "PASS", details=details)
    if missing:
        return CheckResult(
            "id_integrity",
            "FAIL",
            reason=f"{len(missing)} referenced id(s) never declared",
            details={**details, "missing": missing[:20], "missing_count": len(missing)},
        )
    return CheckResult("id_integrity", "PASS", details=details)


def run_ledger_check(doc: dict, args: argparse.Namespace) -> CheckResult:
    path = LEDGER.ledger_path(args.state)
    try:
        events = LEDGER.read_events(path)
    except OSError as exc:
        return CheckResult("ledger", "CANNOT_CHECK", reason=str(exc))
    if events is None:
        return CheckResult("ledger", "SKIPPED", reason="ledger_not_initialized")
    if not events:
        return CheckResult("ledger", "FAIL", reason="ledger_empty")
    defects = LEDGER.verify_chain(events)
    if defects:
        return CheckResult(
            "ledger",
            "FAIL",
            reason=f"chain broken: {len(defects)} defect(s)",
            details={"defects": defects[:10]},
        )
    return CheckResult("ledger", "PASS", details={"event_count": len(events)})


def discover_manuscript_files(doc: dict, base_dir: Path) -> list[Path]:
    files: list[Path] = []
    versions = doc.get("manuscript", {}).get("versions", [])
    for version in versions:
        if not isinstance(version, dict):
            continue
        location = version.get("location")
        if isinstance(location, str) and location.strip() and "REPLACE_ME" not in location:
            candidate = Path(location)
            if not candidate.is_absolute():
                candidate = base_dir / candidate
            if candidate.is_file():
                files.append(candidate)
    return files


def run_consistency_check(doc: dict, args: argparse.Namespace) -> CheckResult:
    files = discover_manuscript_files(doc, args.state.resolve().parent)
    if not files:
        return CheckResult("consistency", "SKIPPED", reason="no manuscript file exists on disk")
    proc = subprocess.run(
        [
            sys.executable,
            str(SCRIPTS_DIR / "check_consistency.py"),
            "--json",
            "--fail-on-findings",
            *[str(f) for f in files],
        ],
        capture_output=True,
        text=True,
    )
    findings_count = None
    try:
        findings_count = len(json.loads(proc.stdout))
    except json.JSONDecodeError:
        pass
    if proc.returncode == 0:
        return CheckResult(
            "consistency",
            "PASS",
            details={"files": [str(f) for f in files], "finding_count": findings_count or 0},
        )
    if proc.returncode == 1:
        return CheckResult(
            "consistency",
            "FAIL",
            reason="mechanical consistency findings",
            details={"files": [str(f) for f in files], "finding_count": findings_count, "stdout": proc.stdout[-2000:]},
        )
    return CheckResult("consistency", "CANNOT_CHECK", reason=f"exit {proc.returncode}", details={"stderr": proc.stderr[-1000:]})


def run_release_manifest_check(doc: dict, args: argparse.Namespace) -> CheckResult:
    if args.release_manifest is None:
        return CheckResult("release_manifest", "SKIPPED", reason="no release manifest provided")
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "verify_publication_release.py"), str(args.release_manifest)],
        capture_output=True,
        text=True,
    )
    if proc.returncode == 0:
        return CheckResult("release_manifest", "PASS", details={"manifest": str(args.release_manifest)})
    if proc.returncode == 1:
        return CheckResult("release_manifest", "FAIL", reason="release verification failed", details={"stdout": proc.stdout[-2000:]})
    return CheckResult("release_manifest", "CANNOT_CHECK", reason=f"exit {proc.returncode}", details={"stderr": proc.stderr[-1000:]})


REGISTRY: tuple[Check, ...] = (
    Check("schema", "structural schema validation of the state document", ALL_STAGES, False, run_schema_check),
    Check("placeholder_census", "count unresolved REPLACE_ME / date placeholders", ALL_STAGES, False, run_placeholder_census),
    Check("id_integrity", "every referenced known-prefix id is declared in the document", ALL_STAGES, False, run_id_integrity),
    Check("ledger", "hash-chain verification of the project-state event ledger", ALL_STAGES, False, run_ledger_check),
    Check("consistency", "check_consistency.py over manuscript files that exist on disk", LATER_STAGES, False, run_consistency_check),
    Check("release_manifest", "verify_publication_release.py over the release manifest", LATER_STAGES, False, run_release_manifest_check),
)


def stage_of(doc: dict) -> str:
    target = doc.get("project", {}).get("target", {})
    stage = target.get("stage")
    return stage if isinstance(stage, str) and stage in STAGES else "planning"


def run_all(doc: dict, args: argparse.Namespace) -> dict:
    stage = stage_of(doc)
    results: list[CheckResult] = []
    for check in REGISTRY:
        if stage not in check.stages:
            results.append(CheckResult(check.name, "SKIPPED", reason=f"stage_not_applicable:{stage}"))
            continue
        if check.network and not args.allow_network:
            results.append(CheckResult(check.name, "SKIPPED", reason="network_disabled"))
            continue
        results.append(check.run(doc, args))
    summary = {
        status: sum(1 for result in results if result.status == status)
        for status in ("PASS", "FAIL", "SKIPPED", "CANNOT_CHECK")
    }
    return {
        "runner_version": RUNNER_VERSION,
        "state": str(args.state),
        "stage": stage,
        "network_allowed": args.allow_network,
        "results": [result.__dict__ for result in results],
        "summary": summary,
    }


def record_run(doc: dict | None, args: argparse.Namespace, report: dict) -> dict:
    """Append a verifier_run event, creating the ledger if needed.

    Refuses (and reports refusal) when the existing chain is broken — appending
    onto a tampered ledger would launder it.
    """
    if doc is None:
        return {"ledger_recorded": False, "reason": "state_unreadable"}
    path = LEDGER.ledger_path(args.state)
    state_sha = hashlib.sha256(args.state.read_bytes()).hexdigest()
    payload = {
        "runner_version": RUNNER_VERSION,
        "stage": report["stage"],
        "summary": report["summary"],
        "results": [
            {"check": result["check"], "status": result["status"], "reason": result["reason"]}
            for result in report["results"]
        ],
        "state_sha256": state_sha,
        "network_allowed": report["network_allowed"],
    }
    actor = getattr(args, "actor", "run_project_state_verifiers")
    if not path.exists():
        try:
            LEDGER.append_event(path, LEDGER.make_event(
                seq=1,
                event_type="state_initialized",
                actor=actor,
                payload={"state_file": args.state.name, "created_by": "run_project_state_verifiers"},
                prev_sha256=LEDGER.GENESIS_PREV,
                timestamp=LEDGER.utc_now_iso(),
            ))
        except OSError as exc:
            return {"ledger_recorded": False, "reason": f"ledger_init_failed: {exc}"}
    events = LEDGER.read_events(path)
    if events is None:
        return {"ledger_recorded": False, "reason": "ledger_missing_after_init"}
    if LEDGER.verify_chain(events):
        return {"ledger_recorded": False, "reason": "refused_append_onto_broken_chain"}
    tail = LEDGER.last_event(events)
    seq = (tail.get("seq", 0) if tail else 0) + 1
    prev = tail.get("event_sha256", LEDGER.GENESIS_PREV) if tail else LEDGER.GENESIS_PREV
    actor = getattr(args, "actor", "run_project_state_verifiers")
    try:
        LEDGER.append_event(path, LEDGER.make_event(
            seq=seq,
            event_type="verifier_run",
            actor=actor,
            payload=payload,
            prev_sha256=prev,
            timestamp=LEDGER.utc_now_iso(),
        ))
    except OSError as exc:
        return {"ledger_recorded": False, "reason": f"append_failed: {exc}"}
    return {"ledger_recorded": True, "ledger_path": str(path), "event_seq": seq}


def human_report(report: dict, ledger_info: dict) -> None:
    print(f"project-state verifier run (runner {report['runner_version']})")
    print(f"state: {report['state']}  stage: {report['stage']}  network: {report['network_allowed']}")
    for result in report["results"]:
        line = f"  {result['status']:<12} {result['check']}"
        if result["reason"]:
            line += f" — {result['reason']}"
        print(line)
    summary = report["summary"]
    print(
        f"summary: {summary['PASS']} PASS, {summary['FAIL']} FAIL, "
        f"{summary['SKIPPED']} SKIPPED, {summary['CANNOT_CHECK']} CANNOT_CHECK"
    )
    if ledger_info.get("ledger_recorded"):
        print(f"ledger: verifier_run recorded at event {ledger_info['event_seq']} ({ledger_info['ledger_path']})")
    else:
        print(f"ledger: NOT recorded — {ledger_info.get('reason', 'unknown')}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE, help="project-state YAML file")
    parser.add_argument("--schema", type=Path, default=VALIDATOR.DEFAULT_SCHEMA, help="structural schema path")
    parser.add_argument("--release-manifest", type=Path, default=None, help="release manifest for the release_manifest check")
    parser.add_argument("--allow-network", action="store_true", help="permit checks that contact external services (none registered yet)")
    parser.add_argument("--actor", default="run_project_state_verifiers", help="actor id recorded on the verifier_run ledger event")
    parser.add_argument("--json", action="store_true", help="emit a machine-readable result object")
    parser.add_argument("--list", action="store_true", help="print the check registry and exit")
    args = parser.parse_args()

    if args.list:
        for check in REGISTRY:
            stages = "all" if check.stages == ALL_STAGES else ",".join(sorted(check.stages))
            print(f"{check.name:<18} stages={stages:<40} network={check.network}  {check.description}")
        return EXIT_OK

    if not args.state.is_file():
        print(f"CANNOT-CHECK state file not found: {args.state}")
        return EXIT_CANNOT_CHECK

    doc, load_error = VALIDATOR.load_state(args.state)
    if doc is None:
        if load_error and load_error.startswith("cannot read"):
            print(f"CANNOT-CHECK {load_error}")
            return EXIT_CANNOT_CHECK
        print(f"FAIL state unparseable: {load_error}")
        return EXIT_DEFECT

    try:
        args.schema_doc = VALIDATOR.load_schema(args.schema)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"CANNOT-CHECK schema unreadable: {args.schema}: {exc}")
        return EXIT_CANNOT_CHECK

    report = run_all(doc, args)
    ledger_info = record_run(doc, args, report)
    report["ledger"] = ledger_info

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        human_report(report, ledger_info)

    if report["summary"]["FAIL"]:
        return EXIT_DEFECT
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
