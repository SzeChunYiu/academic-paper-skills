# `nature-shared/` - shared support package for academic-paper skills

This is an installable support package, not a standalone user workflow. It keeps the shared definitions and references used by the canonical academic-paper and compatible `nature-*` skills in one place so those sources stay consistent and update together. A complete `npx skills` installation discovers and manages it alongside the user-facing skills.

Sibling skills reference these files through relative paths such as:

```yaml
always_load:
  - ../nature-shared/core/reader-workflow.md
```

## Contents

| File | Consumers |
|---|---|
| `core/reader-workflow.md` | `nature-polishing`, `nature-writing` |
| `core/paper-type-taxonomy.md` | `nature-polishing`, `nature-writing` |
| `core/ethics.md` | `nature-polishing`, `nature-writing` |
| `core/research-compliance.md` | `nature-writing` and skills needing Nature Portfolio specialist compliance checks |
| `core/atomic-claim-verification.md` | `academic-writing`, `academic-paper-pipeline`, `nature-writing`, `nature-reviewer`, `nature-polishing`, `nature-response` |
| `core/study-protocol-conduct-contract.md` | `academic-writing`, `academic-paper-pipeline` |
| `core/data-integrity-stewardship-contract.md` | `academic-writing`, `academic-paper-pipeline`, and downstream data/figure/review workflows |
| `data-contracts/` + `scripts/resolve_data_integrity.py` | machine-readable data lifecycle, non-universal adapters, evidence provenance, and bounded evaluation |
| `core/statistical-inference-uncertainty-contract.md` | `academic-writing`, `academic-paper-pipeline`, `nature-statistics`, and downstream display/review workflows |
| `analysis-contracts/` + `scripts/resolve_statistical_inference.py` | machine-readable estimand/execution/uncertainty/surface lifecycle, composable non-universal adapters, time-versioned evidence, and bounded evaluation |
| `core/terminology-ledger.md` | `nature-polishing`, `nature-writing`, `nature-reader`, `nature-paper2ppt` |
| `core/consistency-sweep.md` | `nature-polishing`, `nature-reviewer`, `nature-response`, `nature-statistics` |
| `core/main-text-discipline.md` | `nature-writing`, `nature-polishing`, `nature-response` |
| `journal-formats/nat-comms.md` | `nature-polishing`, `nature-writing` |
| `journal-formats/nature.md` | `nature-writing` and skills needing exact flagship `Nature Article` submission rules |
| `journal-formats/nature-machine-intelligence.md` | Writing, polishing, figure, data, and statistics workflows for NMI submissions |

`core/atomic-claim-verification.md` is the fail-closed scientific-content contract. Full-manuscript, formal-claim, and readiness workflows must inventory every atomic content item, verify that its cited warrant actually entails it, and block verification-complete readiness while any item is merely internally supported, unresolved, contradicted, blocked, or unassessable.

`core/data-integrity-stewardship-contract.md` preserves the authority chain from
source/acquisition record through immutable raw or exact external-reference
origins, validated, and analysis-ready
snapshots, QC and transformation receipts, analysis/display inputs, governance,
and release. Its maintained adapters are explicitly non-universal. Unmatched
modalities and exact institutional, legal, funder, repository, licence, consent,
or community policies require live competent-source resolution. Passing bounded
checks does not certify accuracy, completeness, representativeness, privacy,
legal compliance, reproducibility, scientific truth, or acceptance.

`core/statistical-inference-uncertainty-contract.md` preserves the chain from
question and estimand through independent unit/dependence, analysis population,
plan, immutable input, execution, diagnostics/sensitivity, typed uncertainty,
and every table/display/caption/prose binding to a bounded claim. Its maintained
adapters return applicable obligations, never a universal best test, model,
prior, interval, threshold, or frequentist template. Unmatched domains and
exact regulator/venue rules require live, date-aware source resolution. Passing
does not certify model adequacy, causal identification, adequate precision,
external validity, scientific truth, or acceptance.

`scripts/check_consistency.py` provides a mechanical first pass for terminology variants, equal values reported at different precision, and equivalent lengths expressed in different units. `scripts/audit_manuscript_surface.py` adds target-aware abstract, terminology, placeholder, and rendered-surface diagnostics. Script output is triage evidence for contextual review, never a substitute for the atomic verification ledger.

## When to Put Files Here

Only place a file here when two or more skills need to reuse the same content. If the content serves only one skill, keep it in that skill's own `static/` or `references/` directory.

## When to Keep Content Local

The shared layer should hold definitions and references only, such as paper-type classifications, reader workflows, ethics rules, or terminology ledgers. Skill-specific diagnosis, drafting, modification, and output logic should remain in each skill's own files.

## Relationship With Other Skills

`nature-shared/` is not a standalone workflow. It is a shared dependency package that canonical and compatible academic-paper skills read on demand.
