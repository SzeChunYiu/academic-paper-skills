# Editor–Reviewer Decision Architecture

> Research and implementation note. Last reviewed: 2026-08-22.

## Contents

- [Problem](#problem)
- [Central finding](#central-finding)
- [Decision lifecycle](#decision-lifecycle)
- [Pre-review manuscript intelligence](#pre-review-manuscript-intelligence)
- [Cross-journal publication models](#cross-journal-publication-models)
- [Claim decision proofs](#claim-decision-proofs)
- [Reviewer simulation](#reviewer-simulation)
- [Editor synthesis](#editor-synthesis)
- [Revision closure](#revision-closure)
- [Acceptance engineering and anti-gaming](#acceptance-engineering-and-anti-gaming)
- [Implementation map](#implementation-map)
- [Current source basis](#current-source-basis)

## Problem

A manuscript can fail for very different reasons:

- wrong scope/article type;
- valid science but wrong publication objective;
- contribution/evidence too difficult for an editor to recover quickly;
- central claim under-supported or invalid;
- sound central case with over-broad secondary claims;
- decisive negative/boundary evidence buried in support material;
- figures show headline metrics but not the variation/generalization/calibration needed to evaluate the claim;
- main narrative is cluttered with implementation/repository details while the scientific logic remains implicit;
- reviewer requests are useful but not publication-critical;
- revision letters answer comments without changing the evidence/manuscript state.

A single `acceptance score` hides these failure modes.

## Central finding

There is no universal publication objective.

Examples of deliberately different models include:

- selective broad-interest journals, where scope/priority/readership add gates beyond technical validity;
- selective field-advancement journals, where contribution to a specialist field matters;
- rigor-first scholarly-record models such as PLOS ONE, where perceived importance is not the publication threshold;
- clinical/policy-priority models;
- evidence-assessment models such as current eLife Reviewed Preprints;
- deadline-constrained conferences.

Therefore:

> `scientifically strong`, `easy to evaluate`, and `good fit for this publication model` are different states.

## Decision lifecycle

The shared system models:

```text
Stage -1  Manuscript intelligence / decisionability
   ↓
Stage 0   Integrity / reporting / compliance
   ↓
Stage 1   Editorial triage
   ↓
Stage 2   Independent external review
   ↓
Stage 3   Editor synthesis
   ↓
Stage 4   Revision closure / transfer / stop
```

### Stage -1 — manuscript intelligence

Before simulating acceptance/rejection risk, the writing system can repair the manuscript so reviewers are testing the **science**, not avoidable presentation failures.

This includes:

- argument spine;
- manuscript-content selection;
- close analogue-paper study;
- evidence/figure planning;
- sentence/paragraph dependency and natural scholarly prose;
- author-voice restoration;
- exact journal/reporting resolution.

This stage must never manufacture broader significance or stronger evidence.

### Stage 0 — integrity/compliance

Authorship, ethics, registration, data/image integrity, duplicate publication, reporting checklists, and required data/code/material availability can independently block publication. They are not rhetoric problems.

### Stage 1 — editorial triage

Ask whether the paper:

- fits scope/content type;
- has a recoverable bounded contribution;
- satisfies target-specific priority criteria;
- presents evidence mature enough to justify external review;
- exposes the central evidence rather than forcing editors to excavate it from SI/code/project docs.

### Stage 2 — independent review

Independent reviewers stress-test design, evidence, inference, positioning, reproducibility, clarity, and claim boundaries. They do not receive the simulated triage conclusion.

### Stage 3 — editor synthesis

The simulated editor weighs the **reasoning and relevance** of concerns. It does not count votes or average incompatible scores.

### Stage 4 — revision closure

A concern closes only when the scientific/manuscript state satisfies a resolution test.

## Pre-review manuscript intelligence

### 1. Content selection

`skills/nature-shared/core/manuscript-content-selection.md` asks whether every candidate detail is:

- inference-critical;
- interpretation-critical;
- reproducibility-critical;
- compliance/provenance-critical;
- orientation-critical;
- or none.

Then it assigns the detail to main text, figure, legend, Methods, Extended Data/SI, availability, repository docs, or omit.

This prevents **repository-to-manuscript leakage**: file paths, helper names, setup commands, internal modules, configs, CI/tests, repeated project links, and developer workflow appearing in scientific narrative without a scientific function.

### 2. Figure/evidence planning

`skills/nature-shared/core/figure-evidence-planning.md` maps:

`claim -> reader question -> statistical unit -> estimand -> data structure -> alternative explanation/uncertainty -> visual evidence -> placement`

A reviewer-ready generalization claim may need site/task/population-level evidence, not one pooled metric. A calibration claim needs calibration evidence, not discrimination alone. A paired effect should preserve pairing. A negative result needs effect/uncertainty logic rather than `P > 0.05` alone.

### 3. Natural scholarly prose

`skills/nature-shared/core/natural-scholarly-prose.md` reduces interpretive friction through:

`proposition/dependency -> information progression -> identity chains -> stance -> syntax -> connectives -> cadence`

For difficult paragraphs:

`inherits X -> relation R -> adds Y -> enables Z`

This is a decisionability tool, not AI-detector evasion.

### 4. Analogue papers

Close analogue papers can inform local evidence/figure expectations and rhetorical architecture, but **never become publication policy**. Published patterns contain survivorship bias.

### 5. Author voice

After structural/natural-prose repair, restore the manuscript's recognizable cadence, agency, terminology, technical density, and stance. Clearer does not need to mean generic.

## Cross-journal publication models

Fallback profiles implemented in the shared layer include:

- selective broad-interest;
- selective field-advancement;
- rigor-first scholarly record;
- clinical/policy priority;
- evidence-assessment without conventional post-review gatekeeping;
- deadline-constrained conference selection.

Exact current target guidance overrides fallback profiles.

## Claim decision proofs

Every headline claim should be auditable as:

```text
Claim
Why it matters for this target
Evidence type
Decisive evidence
Strongest plausible alternative explanation
Discriminating test / analysis
Uncertainty and boundary
Manuscript/figure location
Status
```

This changes experiment planning. Instead of asking:

`What else can we add?`

ask:

> `What is the minimum convincing evidence that distinguishes the headline interpretation from the strongest plausible alternative?`

That may be a new experiment, reanalysis, sensitivity analysis, negative control, external validation, counterexample, clearer presentation of existing evidence, narrower claim, or removal of a secondary claim.

## Reviewer simulation

Default mutually blind lenses:

- validity / methods / evidence;
- contribution / prior work / target-specific significance;
- reproducibility / clarity / boundaries / readership.

Article-type-specific lenses can replace these.

Every Major Concern requires a **resolution test**. This prevents reviewer preference from automatically becoming a blocking scientific requirement.

Analogue papers may inform whether evidence architecture is unusual for the claim class, but they are context only.

## Editor synthesis

Concerns are classified as:

- `publication_criteria_blocker`;
- `technical_blocker`;
- `major_repairable`;
- `claim_recalibration`;
- `clarity_or_reporting`;
- `optional_enrichment`.

A single technically decisive concern may remain blocking. Many optional requests do not become mandatory through repetition.

The synthesis also distinguishes:

- weak science;
- sound science that is difficult to evaluate;
- sound science with poor target fit.

## Revision closure

Valid closure routes include:

1. add decisive evidence;
2. reanalyse existing evidence;
3. correct an error;
4. clarify/restructure/reallocate existing evidence;
5. narrow the claim;
6. remove the claim;
7. explain justified nonimplementation;
8. change journal/article type when fit is the real problem.

Important rule:

> Do not perform an experiment merely because a reviewer requested it. Perform it when it is needed to distinguish interpretations or satisfy a real publication criterion.

Similarly, do not add a paragraph/panel simply because a reviewer asked. If the requested content is important but operational/supporting, place it in the scientifically correct location.

## Acceptance engineering and anti-gaming

`Acceptance engineering` means:

- improve exact-target fit;
- improve decisionability;
- strengthen or correctly bound evidence;
- expose decisive negative/alternative evidence;
- make Methods/figures/data/code auditable;
- close real objections efficiently.

It does **not** mean:

- friendly-reviewer selection;
- strategic citation of likely reviewers;
- hiding adverse evidence or strong competitors;
- inflated novelty/significance wording;
- fake reviewer consensus;
- cosmetic experiments;
- burying conclusion-changing limitations;
- cargo-cult imitation of accepted papers;
- AI-detector manipulation.

### Survivorship warning

Published papers show what survived one publication ecology. They do not prove that a phrase, structure, plot, figure count, or visual style caused acceptance.

## Implementation map

### Shared

- `skills/nature-shared/core/editor-reviewer-decision-engine.md`
- `skills/nature-shared/journal-formats/editorial-decision-profiles.md`
- `skills/nature-shared/core/manuscript-content-selection.md`
- `skills/nature-shared/core/figure-evidence-planning.md`
- `skills/nature-shared/core/natural-scholarly-prose.md`
- `skills/nature-shared/core/analogue-paper-calibration.md`
- `skills/nature-shared/core/author-voice-profile.md`

### Writing

- `skills/nature-writing/references/editor-reviewer-preflight.md`
- `skills/nature-writing/static/core/workflow.md`

### Mock review

- `nature-reviewer`: target resolution -> editorial triage -> mutually blind reviewers -> editor synthesis -> author-facing decision map.

### Real revision

- `skills/nature-response/references/editor-decision-closure.md`
- `nature-response`: editor conditions -> blocking concerns -> closure routes -> concise manuscript changes + full reviewer-facing responses.

### Research docs

- `docs/academic-writing-research_EN.md`
- `docs/natural-scholarly-writing_EN.md`
- `docs/manuscript-content-and-figures_EN.md`

## Current source basis

The architecture has been calibrated against current official/editorial/reviewer guidance and direct-reading examples across Nature Portfolio (including Nature, Nature Methods, Nature Computational Science, Nature Medicine, Nature Cell Biology), PLOS, IEEE, ACM, JAMA and eLife publication models, plus empirical peer-review and academic-writing research.

For exact submission decisions, re-verify current official criteria for the real target journal/content type/stage. Local profiles and published-paper patterns are reasoning aids, not permanent substitutes for live target guidance.
