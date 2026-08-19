# Editor–Reviewer Decision Architecture

> Research and implementation note. Last reviewed: 2026-08-19.

## Contents

- [Problem](#problem)
- [Research team lenses](#research-team-lenses)
- [Central finding](#central-finding)
- [Decision lifecycle](#decision-lifecycle)
- [Cross-journal publication models](#cross-journal-publication-models)
- [Claim decision proofs](#claim-decision-proofs)
- [Reviewer simulation](#reviewer-simulation)
- [Editor synthesis](#editor-synthesis)
- [Revision closure](#revision-closure)
- [Acceptance engineering and anti-gaming](#acceptance-engineering-and-anti-gaming)
- [Implementation map](#implementation-map)
- [Current source basis](#current-source-basis)

## Problem

A manuscript can fail at several distinct stages for different reasons:

- not in scope or wrong article type;
- scientifically interesting but not a priority for a selective target;
- editor cannot recover the contribution/evidence quickly enough to justify review;
- technically invalid or under-supported central claim;
- sound central case but over-broad secondary claims;
- reviewer requests that are useful but not publication-critical;
- revisions that answer letters without changing the manuscript/evidence state;
- scientifically sound work sent to a publication model whose objective is mismatched.

A single `acceptance score` hides these failure modes and makes revision strategy worse.

## Research team lenses

The implementation was designed from four complementary perspectives:

1. **Handling editor / triage lens** — scope, article type, priority, readership, maturity and decision cost.
2. **Methods / reproducibility reviewer lens** — design, evidence, inference, reproducibility and technical blockers.
3. **Domain reviewer / argument lens** — contribution, prior work, significance, alternatives and boundaries.
4. **Meta-review / decision-engineering lens** — how multiple reports become an editorial decision and how a revision closes decision-relevant concerns.

The roles are analytical lenses, not invented real reviewer identities.

## Central finding

There is no universal publication objective.

Current official guidance contains deliberately different models:

- **Nature** adds editorial gates for outstanding importance and interdisciplinary interest to a technically credible case.
- **PLOS ONE** explicitly evaluates technical rigor and scientific/ethical eligibility rather than a perceived-importance threshold.
- **IEEE** exposes scope, novelty, validity, data, clarity, compliance and advancement as separate review dimensions.
- **PLOS Medicine / selective clinical models** add importance of the question and possible care/policy/research implications.
- **eLife's current Reviewed Preprint model** separates significance of findings from strength of evidence rather than using conventional post-review accept/reject gatekeeping.
- **Conference selection** can make current-version completeness decisive because a long journal-style revision cycle may not exist.

Therefore:

> `scientifically strong` and `good fit for this exact publication model` are separate states.

## Decision lifecycle

The shared engine models:

```text
Stage 0  Integrity / compliance
   ↓
Stage 1  Editorial triage
   ↓
Stage 2  Independent external review
   ↓
Stage 3  Editor synthesis
   ↓
Stage 4  Revision closure / transfer / stop
```

### Stage 0

Authorship, ethics, registration, data/image integrity, duplicate publication and required reporting can independently block publication. Do not treat these as rhetoric problems.

### Stage 1

The editor simulation asks whether the manuscript fits the exact target, has a recoverable contribution, satisfies target-specific priority criteria, and is mature enough to justify external review.

### Stage 2

Independent reviewers stress-test the scientific case using universal axes plus only those target-conditional criteria the journal actually uses.

### Stage 3

The editor synthesis weighs concern reasoning and relevant review lenses rather than counting recommendations.

### Stage 4

The author closes decision-relevant issues using the minimum scientifically sufficient route.

## Cross-journal publication models

Implemented fallback profiles:

- selective broad-interest;
- selective field-advancement;
- rigor-first scholarly record;
- clinical / policy priority;
- evidence-assessment without conventional post-review gatekeeping;
- deadline-constrained conference selection.

Exact current journal guidance always overrides a fallback profile.

## Claim decision proofs

Every headline claim should be auditable as:

```text
Claim
Why it matters under the target criteria
Evidence type
Decisive evidence
Strongest plausible alternative explanation
Discriminating test / analysis
Uncertainty and boundary
Location
Status
```

This changes experiment planning. Instead of asking `What else can we add?`, ask:

> `What is the cheapest convincing evidence that distinguishes the headline interpretation from the strongest plausible alternative?`

Sometimes that is a new experiment. Sometimes it is a sensitivity analysis, negative control, external validation, counterexample, clearer source evidence, or narrower claim.

## Reviewer simulation

Three default independent lenses are used without invented biographies:

- validity / methods / evidence;
- contribution / prior work / target-specific significance;
- reproducibility / clarity / boundaries / readership.

Article-type-specific lenses can replace them.

Every major concern must have a **resolution test**. This prevents vague preference from being treated as a blocking scientific objection.

Reviewer packets do not receive the editorial-triage conclusion. Reports are frozen before synthesis.

## Editor synthesis

Post-review issues are classified as:

- publication-criteria blocker;
- technical blocker;
- major repairable;
- claim recalibration;
- clarity/reporting;
- optional enrichment.

The synthesis does not average review scores. Consensus is useful evidence but not a voting rule. A single technically decisive concern can remain blocking; multiple optional requests do not become mandatory merely through repetition.

## Revision closure

Closure routes:

1. add decisive evidence;
2. reanalyse existing evidence;
3. correct an error;
4. clarify/restructure existing evidence;
5. narrow the claim;
6. remove the claim;
7. change journal/article type when target mismatch is the real problem.

This supports an important rule:

> Do not perform an experiment merely because a reviewer requested it. Perform it when it is needed to distinguish interpretations or satisfy a real publication criterion.

A response letter does not close a concern unless the evidentiary/manuscript state now satisfies the resolution test.

## Acceptance engineering and anti-gaming

The term **acceptance engineering** is used narrowly:

- improve exact-target fit;
- improve decisionability;
- strengthen or correctly bound evidence;
- surface limitations before reviewers discover them;
- make methods and analyses auditable;
- close real objections efficiently.

It does **not** include:

- friendly-reviewer selection;
- strategic citation of likely reviewers;
- hiding adverse evidence;
- omitting strong competitors;
- inflated novelty/significance language;
- fake reviewer consensus;
- cosmetic experiments;
- burying decision-changing limitations.

Empirical peer-review research showing more favorable recommendations from author-suggested reviewers and associations between reviewer citation requests and recommendations is treated as an anti-gaming warning, not as a strategy.

### Survivorship warning

Published papers and accepted-manuscript patterns are useful evidence about how arguments were presented under a publication ecology. They do **not** establish that a phrase, structure, figure count, or rhetorical style caused acceptance.

The system therefore separates:

- official decision criteria;
- scientific reasoning about evidence;
- observed published-paper conventions;
- empirical peer-review associations;
- unsupported causal claims about acceptance.

## Implementation map

### Shared

- `skills/nature-shared/core/editor-reviewer-decision-engine.md`
- `skills/nature-shared/journal-formats/editorial-decision-profiles.md`

### Writing

- `skills/nature-writing/references/editor-reviewer-preflight.md`
- routed from `nature-writing/manifest.yaml` and `nature-writing/SKILL.md`

### Mock review

- `nature-reviewer` now runs target resolution, editorial triage, mutually blind reviewers, editor synthesis, and author-facing decision engineering.

### Real revision

- `skills/nature-response/references/editor-decision-closure.md`
- classifies must-address versus optional requests and chooses the minimum valid closure route.

### Tests

Focused contracts protect:

- journal-specific decision profiles;
- no universal weighted acceptance score;
- no vote counting;
- no reviewer contamination by editorial triage;
- claim narrowing/removal as valid closure routes;
- anti-gaming rules;
- editor conditions outranking optional reviewer preferences.

## Current source basis

Public guidance reviewed 2026-08-19 includes:

- Nature editorial criteria/process and peer-review policy;
- IEEE Author Center peer-review and reviewer guidance;
- PLOS ONE Reviewer Guidelines and Academic Editor philosophy;
- PLOS Biology and PLOS Medicine selective criteria;
- PLOS editor decision guidance;
- JAMA Network peer-reviewer guidance;
- eLife Assessment definitions and current Reviewed Preprint model;
- venue-specific ACM review criteria as examples of conference/community variation;
- empirical JAMA/eLife peer-review studies relevant to reviewer-suggestion/citation anti-gaming safeguards.

Exact URLs are recorded in the shared source/decision files. Re-verify current official criteria whenever a real target journal decision is being modeled.