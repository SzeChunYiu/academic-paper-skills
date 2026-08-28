# `academic-paper-pipeline` Skill

[中文说明](README.md)

`academic-paper-pipeline` is the end-to-end orchestration layer for developing a manuscript through repeated **research → writing → figures/statistics → independent review → editor synthesis → revision → re-review** until the simulated editor judges the paper publication-ready for the resolved target or a real blocker remains.

It is journal-agnostic. Nature is one optional target, not the default identity of the system.

## What It Solves

The repository has specialist capabilities for writing, figures, statistics, research, review and revision. Without an orchestrator, those can become disconnected one-off prompts.

The pipeline keeps one persistent manuscript state across rounds:

- claim/evidence ledger;
- figure ledger;
- source/research ledger;
- stable reviewer-concern IDs;
- editor must-address conditions;
- revision delta;
- current publication-readiness posture.

## Exact Venue Decision State

The persistent state now resolves **exact venue × article type × stage ×
effective date** and records the policy sources behind each decision field.
Scientific assurance remains independent from target-objective fit. Novelty,
impact, breadth, audience interest, burden of doubt, allowed repair routes,
review model, AI/confidentiality rules, acceptance states, and journal
certifications are not collapsed into one acceptance score.

Live official-source contracts outrank maintained exact snapshots. A generic
or publication-model fallback can guide planning, but cannot close exact target
readiness or be attributed to the journal.

## Iteration Model

```text
target + paper archetype
-> evidence/source intake
-> research calibration
-> argument + claim/evidence architecture
-> content/figure/statistics planning
-> academic writing
-> technical/reporting/surface QA
-> editor triage
-> independent reviewers
-> editor synthesis
-> minimum-sufficient revision
-> targeted re-review
-> editor closure
   ↳ repeat while a real blocker remains
-> simulated_publication_ready_for_target
   OR explicit blocked/retarget state
```

The editor, not reviewer vote count, controls convergence.

## Realistic Review Behavior

- Initial reviewer reports are mutually blind.
- Every Major Concern gets a stable ID and resolution test.
- The editor marks must-address versus non-essential requests.
- Major technical revisions normally return to the relevant original reviewer(s).
- Minor clarity/surface issues can be editor-closed when the target process permits.
- New blocking concerns after round 1 need a documented reason such as a revision regression or newly visible evidence problem; otherwise the pipeline resists moving-goalpost review churn.
- Reviewer disagreement is resolved by evidence/expertise/editor judgment, not score averaging.

## What The Session Can Do During Revision

When tools/data are available, the pipeline can actively:

- research current literature and nearest papers;
- verify/replace citations;
- clarify novelty/prior-work boundaries;
- reanalyse supplied data;
- check statistics/reporting;
- propose/build new plots from existing data;
- redesign figure sequences;
- create workflows/mechanism diagrams/flowcharts;
- expand under-explained scientific reasoning;
- repair sentence-to-sentence logic;
- humanize academic tone while preserving author voice;
- relocate Methods/SI/availability content;
- remove file/script/repository leakage;
- fix punctuation and scientific typography;
- narrow/remove unsupported claims;
- recommend target/article-type transfer.

It **cannot invent a new experimental result**. If a real experiment/data collection is required, the pipeline ends that concern as `blocked_on_author_evidence` and gives the minimum resolution test.

## Self-Research For Uncovered Papers

If a paper class is not covered confidently, the session must research rather than force an existing template.

It should inspect:

1. current official target guidance;
2. applicable reporting/methodological standards;
3. about 8–15 comparable recent papers for a quick profile when useful;
4. 3–6 nearest-neighbor papers for deep reading;
5. counterexamples to apparent conventions.

It then builds a **temporary manuscript-specific archetype profile** covering evidence dependencies, section moves, explanation depth, figure/table roles, support allocation and unresolved uncertainties.

## Writing Quality Gate

Sentence flow is checked as:

```text
inherits X
-> relation R
-> adds Y
-> enables Z
```

The pipeline also checks:

- topic/context continuity;
- identity/reference chains;
- given/new progression when appropriate;
- subject–verb separation;
- stress/emphasis position;
- evidence-to-interpretation warrants;
- analysis-to-analysis handoffs;
- connective use only when a real relation exists.

The aim is rich, coherent scholarly reasoning, not short AI summaries and not verbose filler.

## Content Richness

For central ideas/results, the pipeline checks whether the reader has the necessary subset of:

- identity/definition;
- motivation;
- mechanism/inferential logic;
- decisive evidence;
- comparator/baseline;
- uncertainty;
- alternative explanation;
- boundary/assumption;
- prior-work relationship;
- scientific consequence;
- visual evidence when useful.

`Rich` means enough scientific reasoning/evidence to understand and evaluate the claim — **not more words for their own sake**.

## Figure And Diagram Learning

The pipeline resolves paper archetype before figure sequence.

It can learn from:

- broad stratified paper corpora;
- close analogues;
- recent cross-archetype direct-reading notes;
- mature diagram backends such as Graphviz, Schemdraw and Mermaid for appropriate topology/layout tasks.

It borrows capabilities and design principles, never copyrighted figure layouts or visual identity.

## Publication-Ready State

The successful terminal label is:

`simulated_publication_ready_for_target`

It requires no unresolved integrity, target-criteria or central technical blockers; adequate evidence/statistics/reporting/figures; sufficient explanation and logical flow; fair prior-work treatment; clean main/support allocation; natural authorial prose; and a final artifact-leakage/punctuation pass.

This means **the simulation considers the manuscript ready to submit/finalize**. It is not a guarantee of real acceptance.

## Other Terminal States

- `blocked_on_author_evidence`
- `scientifically_sound_but_target_mismatch`
- `current_claims_not_established`
- `blocked_by_integrity_or_compliance`

Each state must include the cheapest valid path forward.

## Typical Requests

- "Keep reviewing and revising this paper until the editor thinks it is ready to submit."
- "Run a realistic Nature Methods revision loop with the same reviewers until all blocking issues are closed."
- "This paper type is unusual. Research how comparable papers are written first, then build the review/revision loop."
- "Use our existing data to add any analyses/plots needed by reviewers, but never invent experiments."
- "Iterate the manuscript, figures and response until only optional reviewer comments remain."

## Boundary

The pipeline does not game reviewers, count votes, optimize an acceptance score, fabricate data, hide negative results, or add cosmetic experiments.

The goal is a stronger scientific manuscript, not simulated reviewer obedience.
