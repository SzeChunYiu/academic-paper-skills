# Study Protocol and Conduct Contracts Implementation Plan

> **For Codex:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add evidence-backed, study-type-aware protocol and conduct decision contracts that preserve prospective timing, deviations, execution provenance, and claim boundaries before manuscript drafting and journal evaluation.

**Architecture:** A shared JSON Schema is evaluated by a Python resolver against maintained study-type adapters and a versioned evidence registry. The canonical writing and pipeline skills consume the bounded result; the project-state template stores authoritative object references without breaking existing fields.

**Tech Stack:** JSON Schema 2020-12, Python 3.11 standard library plus `jsonschema`, JSON/YAML/Markdown, `unittest`.

---

### Task 1: Freeze the research basis

**Files:**
- Create: `skills/nature-shared/research/study-protocol-conduct-search-log-2026-08-28.json`
- Create: `skills/nature-shared/study-contracts/study-protocol-evidence-registry.json`
- Create: `skills/nature-shared/research/study-protocol-conduct-evidence-ledger-2026-08.md`

1. Freeze 12 broad OpenAlex queries and 84 metadata-screening records.
2. Reconcile included-source metadata through DOI/official pages.
3. Record read depth, supported fields, contradictions, and transfer limits.
4. Require at least two relevant sources per maintained adapter.

### Task 2: Specify behavior before implementation

**Files:**
- Create: `skills/nature-shared/tests/test_study_protocol_contracts.py`
- Create: `skills/nature-shared/tests/fixtures/study-protocols/randomized-valid.json`

1. Write tests for catalog provenance and non-universal resolution.
2. Write tests for false prospective status and outcome switching.
3. Write tests for randomized execution, blinding, stopping, exclusion, harms,
   computational leakage, ethics, and claim reclassification repairs.
4. Run the test file and verify failure because schema/resolver/catalog files do
   not yet exist.

### Task 3: Implement the schema, adapters, and evaluator

**Files:**
- Create: `skills/nature-shared/study-contracts/study-protocol-conduct-contract.schema.json`
- Create: `skills/nature-shared/study-contracts/maintained-study-adapters.json`
- Create: `skills/nature-shared/scripts/resolve_study_protocol.py`
- Create: `skills/nature-shared/core/study-protocol-conduct-contract.md`

1. Add the minimum schema needed by the behavioral tests.
2. Add maintained adapters for randomized intervention, observational causal,
   observational association, computational/ML, animal/preclinical, systematic
   review, qualitative, experimental, resource, and exploratory work.
3. Implement adapter loading, provenance validation, resolution, and evaluation.
4. Run the focused test after each behavior becomes green.
5. Document certification boundaries and allowed repairs.

### Task 4: Integrate canonical skills and state

**Files:**
- Modify: `skills/academic-writing/SKILL.md`
- Modify: `skills/academic-writing/README.md`
- Modify: `skills/academic-writing/README_EN.md`
- Modify: `skills/academic-writing/manifest.yaml`
- Modify: `skills/academic-paper-pipeline/SKILL.md`
- Modify: `skills/academic-paper-pipeline/README.md`
- Modify: `skills/academic-paper-pipeline/README_EN.md`
- Modify: `skills/academic-paper-pipeline/manifest.yaml`
- Modify: `skills/nature-shared/manifest.yaml`
- Modify: `docs/academic-paper-project-state.template.yaml`
- Modify: canonical integration tests.

1. Write failing route/state tests.
2. Load the protocol/conduct contract before Methods, Results, claims, displays,
   or venue acceptance checks when a study record is in scope.
3. Extend state additively and preserve the existing protocol/analysis/deviation
   fields.
4. Run integration tests until green.

### Task 5: Verify, review, and integrate

1. Run the complete focused journal/writing/pipeline/figure/shared suite without
   Python bytecode generation.
2. Run repository, README, mirror, index, metadata, and workflow validators.
3. Run `git diff --check`; inspect status and the full PR file boundary.
4. Commit, push, open a dedicated PR, inspect hosted checks and review comments,
   repair test-first if needed, and merge only when clean.

