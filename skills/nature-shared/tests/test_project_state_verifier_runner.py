from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

SHARED = Path(__file__).parents[1]
ROOT = SHARED.parents[1]
RUNNER_PATH = SHARED / "scripts" / "run_project_state_verifiers.py"
SCHEMA_PATH = SHARED / "project-contracts" / "academic-paper-project-state.schema.json"
TEMPLATE_PATH = ROOT / "docs" / "academic-paper-project-state.template.yaml"


def run_runner(argv: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(RUNNER_PATH), *[str(a) for a in argv]],
        capture_output=True,
        text=True,
    )


def result_of(proc: subprocess.CompletedProcess[str]) -> dict:
    return json.loads(proc.stdout)


def status_of(report: dict, check: str) -> str:
    return next(item["status"] for item in report["results"] if item["check"] == check)


class ProjectStateVerifierRunnerTests(unittest.TestCase):
    def setUp(self) -> None:
        required = [RUNNER_PATH, SCHEMA_PATH, TEMPLATE_PATH]
        if self._testMethodName != "test_required_runner_artifacts_exist" and not all(
            path.exists() for path in required
        ):
            self.skipTest("project-state runner artifacts not present yet")
        self.tmp = tempfile.TemporaryDirectory()
        self.state = Path(self.tmp.name) / "project-state.yaml"
        if TEMPLATE_PATH.exists():
            self.state.write_text(TEMPLATE_PATH.read_text(encoding="utf-8"), encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_required_runner_artifacts_exist(self) -> None:
        for path in (RUNNER_PATH, SCHEMA_PATH, TEMPLATE_PATH):
            self.assertTrue(path.exists(), path)

    def test_registry_lists_six_checks(self) -> None:
        proc = run_runner(["--list"])
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        for check in ("schema", "placeholder_census", "id_integrity", "ledger", "consistency", "release_manifest"):
            self.assertIn(check, proc.stdout)

    def test_untouched_template_passes_and_records_ledger_events(self) -> None:
        proc = run_runner(["--state", self.state, "--json"])
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = result_of(proc)
        self.assertEqual(report["summary"]["FAIL"], 0)
        self.assertEqual(report["summary"]["CANNOT_CHECK"], 0)
        self.assertEqual(status_of(report, "schema"), "PASS")
        self.assertEqual(status_of(report, "id_integrity"), "PASS")
        self.assertEqual(status_of(report, "ledger"), "SKIPPED")
        # auto-init: state_initialized + verifier_run recorded beside the state
        self.assertTrue(report["ledger"]["ledger_recorded"])
        self.assertEqual(report["ledger"]["event_seq"], 2)
        events = [
            json.loads(line)
            for line in Path(report["ledger"]["ledger_path"]).read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        self.assertEqual([event["type"] for event in events], ["state_initialized", "verifier_run"])
        self.assertEqual(events[1]["payload"]["summary"], report["summary"])
        self.assertTrue(events[1]["payload"]["state_sha256"])

    def test_planning_stage_skips_drafting_checks(self) -> None:
        report = result_of(run_runner(["--state", self.state, "--json"]))
        self.assertEqual(report["stage"], "planning")
        self.assertEqual(status_of(report, "consistency"), "SKIPPED")
        self.assertEqual(status_of(report, "release_manifest"), "SKIPPED")

    def test_drafting_stage_enforces_id_integrity_and_runs_artifact_checks(self) -> None:
        doc = yaml.safe_load(TEMPLATE_PATH.read_text(encoding="utf-8"))
        doc["project"]["target"]["stage"] = "drafting"
        self.state.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")
        proc = run_runner(["--state", self.state, "--json"])
        self.assertEqual(proc.returncode, 1, proc.stdout + proc.stderr)
        report = result_of(proc)
        self.assertEqual(status_of(report, "id_integrity"), "FAIL")
        self.assertIn("referenced id(s) never declared", next(
            item for item in report["results"] if item["check"] == "id_integrity"
        )["reason"])
        # drafting checks now run but their inputs are absent, so they SKIP with reasons
        self.assertEqual(status_of(report, "consistency"), "SKIPPED")
        self.assertEqual(status_of(report, "release_manifest"), "SKIPPED")

    def test_tampered_ledger_fails_and_append_is_refused(self) -> None:
        run_runner(["--state", self.state, "--json"])
        ledger = self.state.parent / (self.state.name + ".events.jsonl")
        lines = ledger.read_text(encoding="utf-8").splitlines()
        event = json.loads(lines[0])
        event["payload"]["smuggled"] = True
        lines[0] = json.dumps(event, sort_keys=True, separators=(",", ":"))
        ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
        proc = run_runner(["--state", self.state, "--json"])
        self.assertEqual(proc.returncode, 1, proc.stdout + proc.stderr)
        report = result_of(proc)
        self.assertEqual(status_of(report, "ledger"), "FAIL")
        self.assertFalse(report["ledger"]["ledger_recorded"])
        self.assertEqual(report["ledger"]["reason"], "refused_append_onto_broken_chain")
        # nothing was appended onto the tampered chain
        self.assertEqual(
            len(ledger.read_text(encoding="utf-8").splitlines()), 2
        )

    def test_missing_state_file_is_cannot_check_exit_two(self) -> None:
        proc = run_runner(["--state", Path(self.tmp.name) / "absent.yaml"])
        self.assertEqual(proc.returncode, 2, proc.stdout + proc.stderr)
        self.assertIn("CANNOT-CHECK", proc.stdout)

    def test_yaml_parse_error_is_defect_exit_one(self) -> None:
        (Path(self.tmp.name) / "broken.yaml").write_text("a: [unclosed\n", encoding="utf-8")
        proc = run_runner(["--state", Path(self.tmp.name) / "broken.yaml"])
        self.assertEqual(proc.returncode, 1, proc.stdout + proc.stderr)
        self.assertIn("FAIL", proc.stdout)


if __name__ == "__main__":
    unittest.main()
