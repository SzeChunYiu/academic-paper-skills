from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SHARED = Path(__file__).parents[1]
LEDGER_PATH = SHARED / "scripts" / "project_state_ledger.py"


def load_ledger():
    spec = importlib.util.spec_from_file_location("project_state_ledger", LEDGER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import ledger module from {LEDGER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def run_cli(argv: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(LEDGER_PATH), *[str(a) for a in argv]],
        capture_output=True,
        text=True,
    )


class ProjectStateLedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        if not LEDGER_PATH.exists():
            self.skipTest("project-state ledger tool not present yet")
        self.ledger = load_ledger()
        self.tmp = tempfile.TemporaryDirectory()
        self.state = Path(self.tmp.name) / "project-state.yaml"
        self.state.write_text("schema_version: '0.5.0'\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def events_file(self) -> Path:
        return self.ledger.ledger_path(self.state)

    def init_ledger(self) -> list[dict]:
        self.ledger.append_event(
            self.events_file(),
            self.ledger.make_event(
                seq=1,
                event_type="state_initialized",
                actor="test",
                payload={"state_file": self.state.name},
                prev_sha256=self.ledger.GENESIS_PREV,
                timestamp=self.ledger.utc_now_iso(),
            ),
        )
        return self.ledger.read_events(self.events_file())

    def test_init_creates_genesis_chained_event(self) -> None:
        events = self.init_ledger()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["type"], "state_initialized")
        self.assertEqual(events[0]["prev_event_sha256"], self.ledger.GENESIS_PREV)
        self.assertEqual(self.ledger.verify_chain(events), [])

    def test_append_extends_chain_and_recomputes_digest(self) -> None:
        self.init_ledger()
        tail = self.ledger.last_event(self.ledger.read_events(self.events_file()))
        self.ledger.append_event(
            self.events_file(),
            self.ledger.make_event(
                seq=2,
                event_type="status_transition",
                actor="test",
                payload={"from": "planning", "to": "drafting"},
                prev_sha256=tail["event_sha256"],
                timestamp=self.ledger.utc_now_iso(),
            ),
        )
        events = self.ledger.read_events(self.events_file())
        self.assertEqual(len(events), 2)
        self.assertEqual(self.ledger.verify_chain(events), [])

    def test_payload_tamper_breaks_chain_detectably(self) -> None:
        self.init_ledger()
        lines = self.events_file().read_text(encoding="utf-8").splitlines()
        event = json.loads(lines[0])
        event["payload"]["smuggled"] = True
        lines[0] = json.dumps(event, sort_keys=True, separators=(",", ":"))
        self.events_file().write_text("\n".join(lines) + "\n", encoding="utf-8")
        defects = self.ledger.verify_chain(self.ledger.read_events(self.events_file()))
        self.assertTrue(any("event_sha256 does not match" in d for d in defects), defects)

    def test_event_removal_breaks_seq_and_prev_links(self) -> None:
        for seq in (1, 2, 3):
            events = self.ledger.read_events(self.events_file()) or []
            tail = self.ledger.last_event(events)
            self.ledger.append_event(
                self.events_file(),
                self.ledger.make_event(
                    seq=seq,
                    event_type="state_saved" if seq > 1 else "state_initialized",
                    actor="test",
                    payload={"n": seq},
                    prev_sha256=tail["event_sha256"] if tail else self.ledger.GENESIS_PREV,
                    timestamp=self.ledger.utc_now_iso(),
                ),
            )
        lines = self.events_file().read_text(encoding="utf-8").splitlines()
        del lines[1]
        self.events_file().write_text("\n".join(lines) + "\n", encoding="utf-8")
        defects = self.ledger.verify_chain(self.ledger.read_events(self.events_file()))
        self.assertTrue(defects)
        self.assertTrue(any("seq is" in d for d in defects), defects)

    def test_unknown_event_type_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.ledger.make_event(
                seq=1,
                event_type="certified",
                actor="test",
                payload={},
                prev_sha256=self.ledger.GENESIS_PREV,
                timestamp=self.ledger.utc_now_iso(),
            )

    def test_cli_lifecycle_init_append_verify(self) -> None:
        self.assertEqual(run_cli(["init", self.state]).returncode, 0)
        append = run_cli(
            [
                "append",
                self.state,
                "--type",
                "status_transition",
                "--payload",
                '{"from": "planning", "to": "drafting"}',
            ]
        )
        self.assertEqual(append.returncode, 0, append.stdout + append.stderr)
        verify = run_cli(["verify", self.state])
        self.assertEqual(verify.returncode, 0, verify.stdout + verify.stderr)
        self.assertIn("intact", verify.stdout)

    def test_cli_append_onto_broken_chain_refused(self) -> None:
        run_cli(["init", self.state])
        path = self.events_file()
        path.write_text('{"seq": 1, "bogus": true}\n', encoding="utf-8")
        append = run_cli(
            ["append", self.state, "--type", "state_saved", "--payload", "{}"]
        )
        self.assertEqual(append.returncode, 1, append.stdout + append.stderr)
        self.assertIn("refusing to append", append.stdout)

    def test_cli_verify_missing_ledger_is_cannot_check(self) -> None:
        verify = run_cli(["verify", self.state])
        self.assertEqual(verify.returncode, 2, verify.stdout + verify.stderr)
        self.assertIn("CANNOT-CHECK", verify.stdout)


if __name__ == "__main__":
    unittest.main()
