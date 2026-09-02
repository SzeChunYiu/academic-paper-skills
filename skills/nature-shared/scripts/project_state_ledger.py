#!/usr/bin/env python3
"""Append and verify a tamper-evident hash-chained JSONL event ledger for a project state.

The ledger lives beside the state file as ``<state>.events.jsonl``. Every event
carries ``prev_event_sha256`` and its own ``event_sha256`` computed over the
canonical JSON of the event with ``event_sha256`` removed, so any edit, removal,
insertion, or reordering of a historical event breaks the chain detectably.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

GENESIS_PREV = "0" * 64
EVENT_TYPES = ("state_initialized", "state_saved", "status_transition", "verifier_run")

EXIT_OK = 0
EXIT_DEFECT = 1
EXIT_CANNOT_CHECK = 2


def ledger_path(state_path: Path) -> Path:
    return state_path.parent / (state_path.name + ".events.jsonl")


def canonical_json(payload: Any) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def utc_now_iso() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def event_digest(event: dict) -> str:
    body = {key: value for key, value in event.items() if key != "event_sha256"}
    return hashlib.sha256(canonical_json(body).encode("utf-8")).hexdigest()


def make_event(seq: int, event_type: str, actor: str, payload: dict, prev_sha256: str, timestamp: str) -> dict:
    if event_type not in EVENT_TYPES:
        raise ValueError(f"unknown event type: {event_type}")
    event = {
        "seq": seq,
        "timestamp": timestamp,
        "type": event_type,
        "actor": actor,
        "payload": payload,
        "prev_event_sha256": prev_sha256,
    }
    event["event_sha256"] = event_digest(event)
    return event


def read_events(path: Path) -> list[dict | None] | None:
    """Parse ledger lines. Returns None when the ledger does not exist.

    A malformed JSON line is preserved as None so the defect is attributed to
    its exact line rather than aborting the whole read.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    except OSError as exc:
        raise OSError(f"cannot read ledger: {exc}") from exc
    events: list[dict | None] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            events.append(None)
    return events


def verify_chain(events: list[dict | None]) -> list[str]:
    """Return human-readable defects; empty list means the chain is intact."""
    defects: list[str] = []
    prev = GENESIS_PREV
    for index, event in enumerate(events):
        position = index + 1
        if not isinstance(event, dict):
            defects.append(f"event {position}: not a JSON object")
            prev = None
            continue
        if event.get("seq") != position:
            defects.append(f"event {position}: seq is {event.get('seq')!r}, expected {position}")
        if event.get("type") not in EVENT_TYPES:
            defects.append(f"event {position}: unknown type {event.get('type')!r}")
        if event.get("prev_event_sha256") != prev:
            defects.append(
                f"event {position}: prev_event_sha256 is {event.get('prev_event_sha256')!r}, "
                f"expected {prev!r}"
            )
        recorded = event.get("event_sha256")
        recomputed = event_digest(event)
        if not isinstance(recorded, str) or recorded != recomputed:
            defects.append(f"event {position}: event_sha256 does not match recomputed digest")
        prev = event.get("event_sha256")
    return defects


def append_event(path: Path, event: dict) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(canonical_json(event) + "\n")


def last_event(events: list[dict | None]) -> dict | None:
    for event in reversed(events):
        if isinstance(event, dict):
            return event
    return None


def cmd_init(args: argparse.Namespace) -> int:
    path = ledger_path(args.state)
    if path.exists():
        if not args.force:
            print(f"DEFECT ledger already exists: {path} (use --force to restart)")
            return EXIT_DEFECT
        path.unlink()
    event = make_event(
        seq=1,
        event_type="state_initialized",
        actor=args.actor,
        payload={"state_file": args.state.name},
        prev_sha256=GENESIS_PREV,
        timestamp=utc_now_iso(),
    )
    append_event(path, event)
    print(f"OK initialized {path} (event 1 sha256={event['event_sha256'][:12]}…)")
    return EXIT_OK


def cmd_append(args: argparse.Namespace) -> int:
    path = ledger_path(args.state)
    events = read_events(path)
    if events is None:
        print(f"CANNOT-CHECK no ledger at {path}; run init first")
        return EXIT_CANNOT_CHECK
    defects = verify_chain(events)
    if defects:
        print(f"DEFECT refusing to append onto a broken chain ({len(defects)} defect(s)):")
        for defect in defects:
            print(f"  {defect}")
        return EXIT_DEFECT
    try:
        payload = json.loads(args.payload)
    except json.JSONDecodeError as exc:
        print(f"DEFECT --payload is not valid JSON: {exc}")
        return EXIT_DEFECT
    tail = last_event(events)
    seq = (tail.get("seq", 0) if tail else 0) + 1
    prev = tail.get("event_sha256", GENESIS_PREV) if tail else GENESIS_PREV
    event = make_event(
        seq=seq,
        event_type=args.type,
        actor=args.actor,
        payload=payload,
        prev_sha256=prev,
        timestamp=utc_now_iso(),
    )
    append_event(path, event)
    print(f"OK appended event {seq} ({args.type}) sha256={event['event_sha256'][:12]}…")
    return EXIT_OK


def cmd_verify(args: argparse.Namespace) -> int:
    path = ledger_path(args.state)
    try:
        events = read_events(path)
    except OSError as exc:
        print(f"CANNOT-CHECK {exc}")
        return EXIT_CANNOT_CHECK
    if events is None:
        print(f"CANNOT-CHECK no ledger at {path}")
        return EXIT_CANNOT_CHECK
    if not events:
        print(f"DEFECT ledger {path} is empty")
        return EXIT_DEFECT
    defects = verify_chain(events)
    if defects:
        print(f"DEFECT ledger chain broken ({len(defects)} defect(s) in {len(events)} event(s)):")
        for defect in defects:
            print(f"  {defect}")
        return EXIT_DEFECT
    print(f"OK ledger chain intact: {len(events)} event(s), head sha256={last_event(events)['event_sha256'][:12]}…")
    return EXIT_OK


def cmd_events(args: argparse.Namespace) -> int:
    path = ledger_path(args.state)
    try:
        events = read_events(path)
    except OSError as exc:
        print(f"CANNOT-CHECK {exc}")
        return EXIT_CANNOT_CHECK
    if events is None:
        print(f"CANNOT-CHECK no ledger at {path}")
        return EXIT_CANNOT_CHECK
    for event in events:
        print(json.dumps(event, sort_keys=True))
    return EXIT_OK


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="create the ledger with a state_initialized event")
    init.add_argument("state", type=Path, help="project-state YAML file the ledger belongs to")
    init.add_argument("--actor", default="operator", help="actor id recorded on the event")
    init.add_argument("--force", action="store_true", help="delete and recreate an existing ledger")
    init.set_defaults(fn=cmd_init)

    append = sub.add_parser("append", help="append one event to the chain")
    append.add_argument("state", type=Path, help="project-state YAML file the ledger belongs to")
    append.add_argument("--type", required=True, choices=EVENT_TYPES, help="event type")
    append.add_argument("--payload", required=True, help="JSON payload for the event")
    append.add_argument("--actor", default="operator", help="actor id recorded on the event")
    append.set_defaults(fn=cmd_append)

    verify = sub.add_parser("verify", help="verify the hash chain end to end")
    verify.add_argument("state", type=Path, help="project-state YAML file the ledger belongs to")
    verify.set_defaults(fn=cmd_verify)

    events = sub.add_parser("events", help="print the raw event stream")
    events.add_argument("state", type=Path, help="project-state YAML file the ledger belongs to")
    events.set_defaults(fn=cmd_events)

    return root


def main() -> int:
    args = parser().parse_args()
    try:
        return args.fn(args)
    except OSError as exc:
        print(f"CANNOT-CHECK {exc}")
        return EXIT_CANNOT_CHECK


if __name__ == "__main__":
    sys.exit(main())
