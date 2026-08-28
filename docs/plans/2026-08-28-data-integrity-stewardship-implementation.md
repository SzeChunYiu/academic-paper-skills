# Data Integrity and Stewardship Contract Implementation Plan

> **For Codex:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add an evidence-backed, non-universal data integrity and stewardship decision contract to the canonical paper-writing lifecycle.

**Architecture:** A JSON Schema and Python evaluator enforce only bounded lifecycle invariants. Maintained modality/governance adapters supply applicable obligations and official-source provenance; unmatched exact-domain requirements remain explicit live-research obligations.

**Tech Stack:** JSON Schema 2020-12, Python 3.11 plus `jsonschema`, JSON/YAML/Markdown, `unittest`.

---

### Task 1: Freeze and reconcile the research base

**Files:**
- Create: `skills/nature-shared/research/data-integrity-stewardship-search-log-2026-08-28.json`
- Create: `skills/nature-shared/research/data-integrity-stewardship-evidence-ledger-2026-08.md`
- Create: `skills/nature-shared/data-contracts/data-integrity-evidence-registry.json`

1. Execute and freeze at least ten broad bibliographic queries.
2. Read primary full text or official standards for lifecycle invariants and use
   abstracts only for bounded empirical support.
3. Record read depth, supported decisions, contradictions, transfer limits,
   effective dates, and update triggers.
4. Validate JSON and manually reconcile every adapter source reference.

### Task 2: Specify behavior before implementation

**Files:**
- Create: `skills/nature-shared/tests/test_data_integrity_contracts.py`
- Create: `skills/nature-shared/tests/fixtures/data-integrity/valid-tabular.json`

1. Write tests for required artifacts, evidence depth, non-universal resolution,
   certification limits, and each bounded blocker.
2. Run the test module and verify failure because the schema/catalog/resolver do
   not exist.
3. Keep every behavioral test focused on an observable decision, not an internal
   helper.

### Task 3: Implement schema and maintained adapters

**Files:**
- Create: `skills/nature-shared/data-contracts/data-integrity-stewardship-contract.schema.json`
- Create: `skills/nature-shared/data-contracts/maintained-data-adapters.json`

1. Define strict object shapes, state enums, hashes, dates, lineage edges,
   governance, release, deviations, and claims.
2. Define common adapters with at least two reconciled sources and explicit
   transfer limits each.
3. Run the behavior tests and verify they still fail only because evaluation is
   absent.

### Task 4: Implement resolver and evaluator test-first

**Files:**
- Create: `skills/nature-shared/scripts/resolve_data_integrity.py`
- Modify: `skills/nature-shared/tests/test_data_integrity_contracts.py`

For each behavior: run the single failing test, add the minimum check and repair
route, rerun the test, then run the complete module. Structural schema failure
must return before arithmetic or set operations. The result must separate
blockers, warnings, unresolved policy research, repair routes, visible
deviations, and bounded certification.

### Task 5: Document and integrate the contract

**Files:**
- Create: `skills/nature-shared/core/data-integrity-stewardship-contract.md`
- Modify: `skills/academic-writing/SKILL.md`
- Modify: `skills/academic-writing/README.md`
- Modify: `skills/academic-writing/README_EN.md`
- Modify: `skills/academic-writing/manifest.yaml`
- Modify: `skills/academic-paper-pipeline/SKILL.md`
- Modify: `skills/academic-paper-pipeline/README.md`
- Modify: `skills/academic-paper-pipeline/README_EN.md`
- Modify: `skills/academic-paper-pipeline/manifest.yaml`
- Modify: `skills/nature-shared/manifest.yaml`
- Modify: `skills/nature-shared/README.md`
- Modify: `skills/nature-shared/README_EN.md`
- Modify: `docs/academic-paper-project-state.template.yaml`

1. Insert data-lifecycle resolution after study conduct and before analysis,
   displays, claims, or availability projection.
2. Add on-demand evidence-ledger routing and bump affected skill versions.
3. Add an additive project-state section and assurance fields; do not remove or
   rename existing fields.
4. Add integration tests showing both canonical skills load the shared layer.

### Task 6: Verify, review, and integrate

1. Run the data-contract module and the complete focused journal/writing/pipeline
   suites with `python -B`.
2. Parse every Python file with `ast` and every JSON artifact with `json`.
3. Run repository, README mirror, skill-index, metadata, and workflow validators.
4. Run `git diff --check`; inspect status and `origin/main...HEAD` diff.
5. Commit, push, open a dedicated PR, and inspect every hosted check and inline
   review finding.
6. Fix valid findings test-first and repeat verification.
7. Squash-merge only when the PR reports a clean merge state and all required
   checks are complete.
