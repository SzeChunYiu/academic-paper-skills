---
name: academic-paper-pipeline
description: >-
  Orchestrate an academic manuscript through repeated research, evidence/claim
  planning, academic writing, statistics, figure/diagram design, independent
  reviewer simulation, editor synthesis, revision, and targeted re-review until
  a simulated editor judges it publication-ready for the resolved target or a
  real blocker remains. Use for end-to-end paper workflows, repeated review and
  revision, publishability hardening, reviewer-driven iteration, or self-research
  when a paper type or venue is not already covered. The pipeline is journal-
  agnostic; Nature is only one optional target adapter. It never fabricates
  results or treats reviewer votes as acceptance.
---

# Academic Paper Pipeline

This is the canonical **orchestration skill** for end-to-end manuscript development.

It does not replace specialist capabilities. It coordinates them as one stateful editorial loop.

## Always load

Read `manifest.yaml`, then every file in `always_load`.

The core lifecycle is defined by:

- `../nature-shared/core/academic-paper-iteration-pipeline.md`;
- `../nature-shared/core/atomic-claim-verification.md`;
- `../nature-shared/core/editor-reviewer-decision-engine.md`;
- `../nature-shared/core/paper-archetype-atlas.md`;
- `../nature-shared/core/unknown-paper-research-protocol.md`;
- `../nature-shared/core/sentence-logic-and-cohesion.md`;
- `../nature-shared/core/manuscript-surface-qa.md`.

## Canonical role map

Use the installed specialist capabilities as roles in one pipeline:

- **research/literature** — academic search + citation verification;
- **academic writing** — canonical `$academic-writing` capability (legacy repository directory: `skills/nature-writing`);
- **statistics/analysis** — statistical design, analysis and reporting capability;
- **figures/diagrams** — scientific figure capability, including data plots and diagram-specific backends;
- **review** — independent editor/reviewer simulation;
- **revision response** — editor/reviewer concern closure and response-package logic.

Do not expose internal skill-routing mechanics inside manuscript prose.

## Start state

Resolve or infer conservatively:

```text
target journal/venue
article/content type
submission stage
policy as-of/effective date
dominant paper archetype
secondary archetypes
intended reader
available manuscript/data/figures/sources
real-world constraints on new experiments/analysis
```

If a target/archetype is unclear but the current task can proceed safely, build a generic rigorous profile and research the uncertainty instead of repeatedly asking the user.

## Exact venue decision contract

When a target-specific readiness or revision decision matters, resolve:

`exact venue × article type × stage × effective date`

Load `../nature-shared/journal-formats/venue-decision-contract.md`. There is no universal acceptance objective. Keep scientific assurance, target-objective
fit, real journal decision state, and any certification layer as separate state
objects.

The resolution order is live official-source contract, active maintained exact
snapshot, then an explicitly non-exact fallback. A fallback never becomes the
journal's policy. Future-effective rules do not apply early, and an observed
snapshot cannot be back-cast before its observation date.

The contract must expose scientific gates; novelty/impact/breadth/audience
interest gates; burden-of-doubt rules; allowed repair routes; review model;
AI/confidentiality policy; acceptance states; certification layer; and source
plus effective-date provenance. Journal certification is separate from acceptance:
neither a journal annotation nor a resolver/source certification predicts the
real editorial outcome.

## Self-research rule

If the current paper type, writing convention, reporting standard, figure grammar, or target criterion is materially uncertain, **research before guessing**.

Use the unknown-paper protocol to inspect:

1. current official target guidance;
2. relevant reporting/methodological standards;
3. roughly 8–15 comparable recent papers for a quick profile when useful;
4. 3–6 nearest-neighbor papers for deep reasoning;
5. counterexamples to any apparent convention.

Create a temporary manuscript-specific archetype profile.

Do not copy wording or layouts.

## Study protocol and conduct contract

Before manuscript-state claims are treated as scientific evidence, materialize
the shared **study protocol/conduct decision contract** from
`../nature-shared/core/study-protocol-conduct-contract.md`.

Resolve the study archetype and applicable obligations, then bind:

`protocol version -> analysis-plan version -> conduct receipt -> deviation ledger -> analysis/result -> claim`.

Keep planned, executed, verified, unknown, not done, and not applicable distinct.
A protocol/conduct blocker is a manuscript-state blocker when it affects an
in-scope claim. Valid repairs preserve history: reconcile authoritative records,
append a dated deviation, rerun from a valid snapshot/split, add a versioned
sensitivity analysis, reclassify exploratory/post-hoc work, narrow the claim, or
request a new prospective study. Never backdate, overwrite adverse/null evidence,
or infer ethics/randomization/blinding execution from prose.

Schema/registration/reporting completion, protocol/conduct traceability,
scientific validity, and journal acceptance remain separate state layers.

## Iterative loop

Run these stages in order.

### 1. Intake and evidence freeze

Separate:

- author results/data;
- manuscript claims;
- external literature;
- project/repository artifacts;
- missing evidence;
- constraints.

Never invent new study results.

### 2. Materialize protocol and conduct state

For each in-scope study, resolve the maintained adapter or an explicit unresolved
domain research requirement. Evaluate protocol/SAP timing, registration
applicability, executed assignment/blinding/fidelity, outcomes, stopping,
exclusions/attrition, harms, raw-data/analysis lineage, deviations, and
ethics/governance before licensing confirmatory or causal claim status.

### 3. Research and positioning

Research enough to establish:

- strongest relevant prior work;
- novelty/contribution boundary;
- methodological/reporting norms;
- nearest paper archetype;
- local evidence/figure expectations;
- target criteria when known.

Resolve the exact venue decision contract from current official sources or an
active maintained snapshot. If only a fallback is available, keep target-policy
status unresolved while useful science and drafting work continues.

### 4. Build manuscript state

Maintain one row per atomic content item in the atomic-claim ledger, together
with evidence, figure, source and concern ledgers. Split every
scientific assertion while preserving scope, qualifiers, negation, comparators,
quantifiers, and conditions. Verify whether the located warrant actually entails
the assertion.

Build:

`question/tension -> bounded contribution -> evidence progression -> alternatives/boundaries -> meaning`

Check content richness and explanatory sufficiency.

### 5. Plan figures/statistics/diagrams

For every headline claim determine:

```text
reader question
-> unit/estimand/object
-> evidence/data
-> uncertainty/alternative
-> representation
-> main/support/omit
```

Then materialize the shared scientific display decision contract for every
evidence-bearing figure, plot, table, image plate, diagram, or mixed display.
Record the reader task, estimand, statistical unit, candidate representation,
allowed/prohibited inferences, data snapshot, analysis receipt, render receipt,
source-data object, caption denominator, uncertainty meaning, transformations,
group coverage, accessibility, and placement. There is no universal best chart.

A display-contract blocker is a manuscript-state blocker when the display is
required for a headline claim. Repair it by reconciling/re-rendering from real
evidence, changing representation, adding a traceable companion display, or
narrowing the claim—not by inventing evidence.

Use scientific diagram backends for workflows/mechanisms/flowcharts rather than forcing everything through a plotting grammar.

### 6. Draft/rewrite

Use academic-writing logic in this order:

```text
scientific relation
-> paragraph dependency
-> sentence dependency
-> explanation sufficiency
-> identity/information chains
-> stance
-> natural author voice
-> exact target adaptation
-> surface QA
```

### 7. Pre-review QA

Before simulated review, check:

- claim/evidence consistency;
- protocol/conduct/deviation/claim-status consistency;
- complete atomic-claim coverage and definition/proof/source entailment;
- statistics/reporting;
- figure adequacy;
- explanation depth;
- sentence/paragraph logic;
- citations/prior work;
- main/support allocation;
- artifact leakage;
- punctuation/typography;
- exact target compliance.

### 8. Editorial triage

The simulated editor decides whether the manuscript should proceed to review or whether a target/science/readiness blocker should be repaired first.

### 9. Independent review

Run mutually blind initial reviewer contexts.

Default lenses:

- reviewer 1 — validity/methods/data/inference;
- reviewer 2 — contribution/prior work/target-specific significance or utility;
- reviewer 3 — reproducibility/reporting/clarity/boundaries/readership.

Every Major Concern requires a stable concern ID and a resolution test.

### 10. Editor synthesis

The editor weighs **arguments and expertise, not reviewer votes**.

Mark each concern as:

- must address;
- claim recalibration;
- clarity/explanation/reporting;
- surface copyedit;
- optional enrichment.

### 11. Execute minimum-sufficient revision

Do every valid repair possible with available material/tools:

- research literature;
- add/replace citations;
- reanalyse supplied data;
- calculate/check statistics;
- add/rebuild plots;
- create/redesign diagrams;
- restructure evidence;
- expand missing explanation;
- repair sentence logic;
- correct reporting/punctuation;
- relocate project artifacts;
- narrow/remove unsupported claims;
- recommend retargeting when fit is the issue.

If a real new experiment/data collection is required, mark it blocked and state the minimum resolution test. Do not fabricate it.

### 12. Freeze revision delta

Update ledgers and current manuscript version. Verify every claimed closure exists in the manuscript/evidence state.

### 13. Targeted re-review

For major revisions, send the relevant changed claims/evidence back to the original concern owner by default.

For minor clarity/surface issues, allow editor-only closure when target practice permits.

Do not re-open the whole paper from zero unnecessarily.

### 14. Moving-goalpost protection

A new blocking concern after round 1 needs a reason such as:

- revision created a new issue;
- new evidence revealed it;
- previously unassessable material became visible;
- expertise gap was discovered;
- original concern was incompletely scoped.

Otherwise treat it as late optional enrichment unless the editor independently determines it is essential to scientific validity/publication criteria.

### 15. Editor closure

Repeat revision/re-review only while a real must-address concern remains and there is a concrete resolution test.

Do **not** keep iterating just to make every reviewer maximally happy.

## Success state

The only successful terminal label is:

`simulated_publication_ready_for_target`

Use it only when:

- no integrity/compliance blocker;
- no unresolved publication-criteria blocker;
- the exact target tuple/date is resolved by a supported contract, not a
  fallback presented as policy;
- no unresolved technical blocker to a headline claim;
- headline claims are established or appropriately narrowed;
- every in-scope atomic assertion has an allowed release status and zero
  `SUPPORTED_INTERNAL`, `UNRESOLVED`, `CONTRADICTED`, `BLOCKED`, or in-scope
  `NOT_ASSESSABLE` manuscript assertions remain;
- central alternatives/boundaries are visible;
- methods/statistics/reporting are adequate;
- figures/diagrams expose the needed evidence;
- every required display contract is bound to the current data/analysis/render/source-data objects and has no display-contract blocker;
- contents are rich enough to understand without filler;
- sentence-to-sentence and paragraph logic are coherent;
- author voice is natural rather than generic/AI-like;
- citations/prior work are fair and sufficiently verified;
- main/support allocation is appropriate;
- every standalone surface is locally intelligible, every display in the abstract
  has a target-resolved disposition, and no unexplained private term/symbol or
  unresolved surface-review item remains;
- no release placeholder remains in manuscript-facing text;
- rendered artifacts, when present, pass every-page layout, metadata,
  accessibility, and final-page/spill review;
- manuscript surfaces are free of project leakage and punctuation defects;
- remaining requests are optional enrichment or production copyedit.

This is a **simulation of readiness**, not a promise of real acceptance.

## Blocked states

Return one of these instead of pretending readiness:

- `blocked_on_author_evidence`;
- `scientifically_sound_but_target_mismatch`;
- `current_claims_not_established`;
- `blocked_by_integrity_or_compliance`.

For every block, specify the cheapest valid path forward.

## Round reporting

Keep the user-facing update compact:

```text
Round/version
Editor posture
Must-address concerns open
Closed this round
Research/analysis/figures/writing added
Claims narrowed/removed
Surface QA
Next revision action
```

The final paper/deliverables remain primary. Do not bury the user under internal ledgers unless they ask.

## Red lines

Never:

- count reviewer votes as an editorial decision;
- fabricate data/experiments;
- manipulate reviewer selection/citations;
- hide negative evidence;
- add cosmetic experiments;
- optimize an acceptance probability score;
- copy peer-paper prose/visual identity;
- expose project filenames/paths inside the paper;
- call prose-only rebuttal a scientific closure when the manuscript remains unchanged;
- keep iterating after only optional enrichment remains.
