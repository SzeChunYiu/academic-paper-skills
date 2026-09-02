# Project-state execution spine evidence ledger — 2026-09-02

**Purpose:** research basis for the executable project-state JSON Schema, the
hash-chained project event ledger, and the chained verification-pipeline
runner. This ledger records the absence evidence that motivates the spine,
the interface survey it builds on, and the design decisions with their
rejected alternatives. It is not a universal checklist and does not certify
scientific truth, absence of bias, or journal acceptance.

**Frozen analysis date:** 2026-09-02
**Baseline commit:** `d5b61b5` (merge of PR #34)
**Tracking issue:** GitHub issue #35

Shipped artifacts (this P0 scope):

| Artifact | Path (relative to `skills/nature-shared/`) |
|---|---|
| Structural schema (JSON Schema draft 2020-12) | `project-contracts/academic-paper-project-state.schema.json` |
| Structural validator CLI | `scripts/validate_project_state.py` |
| Hash-chained event ledger CLI | `scripts/project_state_ledger.py` |
| Chained verifier runner (check registry in code) | `scripts/run_project_state_verifiers.py` |
| Invalid-mutation corpus manifest | `tests/fixtures/project-state/invalid-mutations.json` |
| Regression tests | `tests/test_project_state_schema.py`, `tests/test_project_state_ledger.py`, `tests/test_project_state_verifier_runner.py` |

## Absence evidence (recorded before implementation)

Three independent probes, each run at the repository root at `d5b61b5`:

1. `find . -name "*.jsonl" -not -path "./.git/*" | wc -l` → `0`.
   The repository defines append-only, hash-chained ledgers as its core
   integrity pattern (research-integrity, manuscript-element-justification,
   terminology) yet no project-state ledger instance exists anywhere.
2. `ls skills/nature-shared/scripts/ | wc -l` → `22`. Every entry is a
   per-artifact verifier, resolver, or auditor. No script chains the others;
   orchestration exists only as prose in
   `skills/academic-paper-pipeline/SKILL.md` (20-stage lifecycle) and
   `core/academic-paper-iteration-pipeline.md`.
3. `find skills/nature-shared/tests/fixtures -type f` → one valid fixture per
   contract family (study-protocols, data-integrity, statistical-inference,
   display-contracts, venue-contracts) and zero fixtures designed to fail.
   Happy-path-only testing cannot detect a verifier that accepts invalid
   input.

## Interface survey (what the runner chains)

Verified by reading each script's argparse block at `d5b61b5`:

| Script | CLI shape | Network |
|---|---|---|
| `resolve_study_protocol.py` | `contract PATH [--adapters PATH]` | no |
| `resolve_data_integrity.py` | `contract PATH [--adapters PATH]` | no |
| `resolve_statistical_inference.py` | `contract PATH [--adapters PATH]` | no |
| `verify_research_integrity.py` | `ledger PATH [--report PATH]` | yes (Crossref) |
| `resolve_venue_contract.py` | `--venue --article-type --stage --as-of` | no |
| `verify_publication_release.py` | `manifest PATH [--report PATH]` | no |
| `check_consistency.py` | `paths... [--json]` | no |
| surface auditors (`audit_*.py`) | artifact PATH | no |

The shipped runner registry (`REGISTRY` in `scripts/run_project_state_verifiers.py`)
chains the checks whose inputs are discoverable from the project state itself:
schema validation, placeholder census, id integrity, and ledger verification
at every stage, plus `check_consistency.py` over manuscript version files that
exist on disk and `verify_publication_release.py` over an explicitly provided
release manifest from drafting onward. The per-contract resolvers
(`resolve_study_protocol.py`, `resolve_data_integrity.py`,
`resolve_statistical_inference.py`, `verify_research_integrity.py`,
`resolve_venue_contract.py`) are **not** chained in this P0: their inputs are
standalone contract files the project state does not yet locate, so chaining
them now would guess paths. They join the registry incrementally as contract
artifacts gain explicit routing in the project state; the `Check` dataclass is
the extension point.

## Design decisions

1. **Schema validates structure, not semantics.** The shipped template
   (`docs/academic-paper-project-state.template.yaml`) contains `REPLACE_ME`
   placeholders by design. The schema therefore constrains types, enums
   (exactly the values the template documents in inline comments), id
   prefixes, and date patterns — it must accept the untouched template as a
   structural instance. Placeholder semantics belong to per-contract
   resolvers, not to the structural schema.
   *Rejected:* requiring non-placeholder content (would make the template
   itself invalid and duplicate resolver responsibilities).
2. **Ledger is a hash chain, not a database.** Each event carries
   `prev_event_sha256` and `event_sha256` (sha256 over the canonical JSON of
   the event with `event_sha256` removed). `verify-ledger` recomputes the
   full chain; any byte edit breaks the chain at a named sequence number.
   *Rejected:* signed entries (no key infrastructure in this repository's
   threat model; hash chaining matches the research-integrity ledger
   precedent).
3. **Runner is artifact-driven and stage-gated.** Checks run when their input
   artifacts exist (discovered from the project state), and applicability is
   gated by `project.target.stage` so a planning-stage project is not failed
   for lacking a manuscript. A check whose optional input is absent reports
   `SKIPPED` with a named reason (visible in the report and in the recorded
   ledger event), never a silent pass; `id_integrity` is a census at planning
   (the untouched template legitimately carries exemplar forward references)
   and enforced from drafting onward.
   *Rejected:* failing on every missing optional artifact (produces noise
   fails that train users to ignore the runner) and silently passing missing
   inputs (unfalsifiable green).
4. **Exit codes are three-valued and fail-closed.** `0` = verified clean,
   `1` = defect found (invalid state, broken chain, failed check),
   `2` = cannot check (unreadable input, absent ledger). "Could not check"
   is never reported as "checked and fine".
5. **Network checks are opt-in.** Every registry entry declares
   `network: true|false`; the runner skips network checks unless
   `--allow-network` is passed, keeping CI and offline audits deterministic.
   No P0 registry entry uses the network — `verify_research_integrity.py`
   (live Crossref) is the first future consumer and joins only when its
   ledger artifact gains routing.
6. **Ledger lives beside the state file** (`<state>.events.jsonl` by
   default) so a project directory is self-contained and portable.

## Regression requirements

`tests/test_project_state_schema.py`, `tests/test_project_state_ledger.py`,
and `tests/test_project_state_verifier_runner.py` must keep asserting: the
untouched template validates with zero errors; every entry of the
invalid-mutation corpus fails with the expected error at the expected
pointer; payload tampering and event removal break the ledger chain with a
named sequence number; appending onto a broken chain is refused; the runner
exits 0 with the untouched planning-stage template (auto-initializing the
ledger with `state_initialized` + `verifier_run` events), exits 1 when
`id_integrity` is enforced at drafting stage or the ledger chain is broken
(append refused, chain length unchanged), and exits 2 for a missing state
file.

## Boundaries

The spine enforces structure and chain-of-custody only. It does not certify
measurement accuracy, absence of bias, analytic reproducibility, scientific
truth, or journal acceptance — those certifications remain with the
per-contract resolvers and their `does_not_certify_*` fields.
