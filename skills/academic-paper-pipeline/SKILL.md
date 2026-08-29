---
name: academic-paper-pipeline
description: >-
  Orchestrate an academic paper from research-question and publication-route
  design through evidence maturation, manuscript writing, statistics,
  figures/tables/diagrams, evidence-graded acceptance optimization, journal
  acceptance-readiness, independent reviewer simulation, editor synthesis,
  revision, rejection triage, transfer/retargeting, and targeted re-review until
  the paper is decision-ready for the resolved target or a real blocker remains.
  Use for end-to-end paper workflows, maximum legitimate publication opportunity,
  repeated review and revision, publishability hardening, Registered Report
  planning, target/editorial triage, or self-research when a paper type or venue
  is not already covered. The pipeline is journal-agnostic; Nature is only one
  optional target adapter. It never fabricates results, predicts acceptance
  probability, profiles editor/reviewer favorability, or treats reviewer votes
  as acceptance.
---

# Academic Paper Pipeline

This is the canonical **orchestration skill** for end-to-end manuscript development.

It does not replace specialist capabilities. It coordinates them as one stateful scientific and editorial loop.

## Always load

Read `manifest.yaml`, then every file in `always_load`.

The core lifecycle is defined by:

- `../nature-shared/core/academic-paper-iteration-pipeline.md`;
- `../nature-shared/core/atomic-claim-verification.md`;
- `../nature-shared/core/editor-reviewer-decision-engine.md`;
- `../nature-shared/core/journal-acceptance-readiness.md`;
- `../nature-shared/core/acceptance-optimization-protocol.md`;
- `../nature-shared/core/paper-archetype-atlas.md`;
- `../nature-shared/core/unknown-paper-research-protocol.md`;
- `../nature-shared/core/sentence-logic-and-cohesion.md`;
- `../nature-shared/core/explanatory-sufficiency.md`;
- `../nature-shared/core/manuscript-content-selection.md`;
- `../nature-shared/core/study-protocol-conduct-contract.md`;
- `../nature-shared/core/data-integrity-stewardship-contract.md`;
- `../nature-shared/core/statistical-inference-uncertainty-contract.md`;
- `../nature-shared/core/figure-evidence-planning.md`;
- `../nature-shared/core/scientific-display-decision-contract.md`;
- `../nature-shared/core/manuscript-surface-qa.md`.

## Canonical role map

Use the installed specialist capabilities as roles in one pipeline:

- **research/literature** — strongest prior work, close analogues, reporting/methodological standards and citation verification;
- **acceptance optimization** — evidence-graded question/design/publication-route planning, Registered Report screening, evidence maturation, fit-first target ladder, desk-rejection stress tests, public-review-history calibration, rejection triage and retargeting;
- **academic writing** — canonical `$academic-writing` capability (legacy repository directory: `skills/nature-writing`);
- **statistics/analysis** — statistical design, analysis, uncertainty and reporting capability;
- **figures/diagrams** — scientific figure capability, including plots, tables, image evidence and diagram-specific backends;
- **acceptance readiness** — exact target, editorial triage, expertise routing, reviewer coverage, cover-letter/submission metadata and retargeting;
- **review** — independent editor/reviewer simulation;
- **revision response** — editor/reviewer concern closure and response-package logic.

Do not expose internal skill-routing mechanics inside manuscript prose.

## Start state

Resolve or infer conservatively:

```text
publication objective: fixed target vs successful publication vs revision/retargeting
project phase: question design / protocol / data collection / analysis / manuscript / submitted / revision / rejected
target journal/venue, if fixed
article/content type
submission stage
policy as-of/effective date
dominant paper archetype
secondary archetypes
intended reader
available manuscript/data/figures/sources
whether outcome/result data have already been accessed
real-world constraints on new experiments/analysis
Registered Report or other prospective publication-route relevance
editor/team routing relevance
submission-system editor/reviewer suggestion or exclusion rules
practical target-ladder constraints
```

If a target/archetype is unclear but the current task can proceed safely, build a generic rigorous profile and research the uncertainty instead of repeatedly asking the user.

## Evidence-graded acceptance optimization

For any substantial publication-oriented project, apply `../nature-shared/core/acceptance-optimization-protocol.md`.

The goal is not an acceptance score. It is to reduce preventable rejection and strengthen legitimate publication opportunity using the earliest scientifically valid intervention.

Use this authority distinction:

```text
A = direct experimental / quasi-experimental process evidence
B = multi-journal or large-scale observational meta-research
C = single-journal / narrow-domain observational evidence
D = current official target policy or reviewer criteria
E = expert editorial/practice guidance
H = public peer-review-history heuristic
MANUSCRIPT_INTERNAL = the project's own scientific evidence/state
```

Rules:

- `D` and `MANUSCRIPT_INTERNAL` may define hard gates when they genuinely have authority;
- `A` can justify the outcome actually tested, not an unmeasured acceptance effect;
- `B/C/E` inform priors and stress tests with transfer limits;
- `H` can teach concern-to-repair patterns but can **never** become a hard acceptance gate by itself;
- public accepted/revised histories must be paired with rejection/rejection-report evidence and an explicit survivorship warning;
- never transform any grade into a manuscript-specific numeric acceptance probability.

When the task is a serious target/submission plan, materialize an acceptance-optimization plan conforming to:

`../nature-shared/acceptance-contracts/acceptance-optimization-plan.schema.json`

and validate it with:

`../nature-shared/scripts/validate_acceptance_optimization_plan.py`.

## Exact venue decision contract

When a target-specific readiness or revision decision matters, resolve:

`exact venue × article type × stage × effective date`

Load `../nature-shared/journal-formats/venue-decision-contract.md`. There is **no universal acceptance objective**. Keep scientific assurance, target-objective fit, real journal decision state, and any certification layer as separate state objects; certification is separate from acceptance.

The resolution order is live official-source contract, active maintained exact snapshot, then an explicitly non-exact fallback. A fallback never becomes the journal's policy. Future-effective rules do not apply early, and an observed snapshot cannot be back-cast before its observation date.

The contract must expose scientific gates; novelty/impact/breadth/audience-interest gates; burden-of-doubt rules; allowed repair routes; review model; AI/confidentiality policy; acceptance states; certification layer; and source plus effective-date provenance. Neither a journal annotation nor a resolver/source certification predicts the real editorial outcome.

## Journal acceptance-readiness and editor routing

Always apply `../nature-shared/core/journal-acceptance-readiness.md` when the user is preparing a target submission or asking how to improve publication prospects.

Model the real decision path as separate gates:

```text
science/integrity
-> exact target scope/article type
-> editorial triage
-> editor/expertise routing
-> reviewer coverage
-> evidence maturity
-> editor synthesis
-> revision closure
-> final compliance
```

Run several independent non-biographical editorial lenses before submission: scope/article type, contribution/positioning, evidence maturity, readership/objective, and routing clarity. Freeze each assessment before synthesis; do not count votes. A plausible desk-rejection argument remains a risk item until its underlying reason is repaired or shown not to apply.

When public editor identities, teams or sections matter, load `../nature-shared/core/editor-expertise-routing.md`. Use official professional information only for subject/expertise coverage, conflict checks, section routing, or an editor suggestion explicitly permitted by the exact submission workflow. Never infer leniency, personality, ideology, citation preferences or acceptance propensity, and never simulate a real named editor's psychology.

Maintain uncontrollable editorial context separately from manuscript state: simultaneous overlapping work, competition among strong submissions, reviewer availability, legitimate editor disagreement and confidential information may affect a real decision without creating a valid manuscript repair.

## Prospective publication-route gate

If the project is still prospective, check the publication route **before** outcome/results access where possible.

In particular, determine whether a scientifically compatible target currently offers a Registered Report.

If considering a Registered Report, resolve current official policy and record:

```text
availability
eligibility
Stage 1 criteria
sampling / information-size obligations
outcome-neutral quality checks
allowed deviations
in-principle-acceptance conditions
Stage 2 publication conditions
```

Do not call a Registered Report a shortcut or guarantee. It is a different review architecture that can move methodological peer review before results and, at eligible venues, make final publication less dependent on outcome direction when the approved protocol is followed.

If result/outcome access already makes Stage 1 ineligible, record that fact and continue with the appropriate route rather than backdating prospective status.

## Fit-first target ladder

When the user's objective is successful publication rather than one immovable journal, do not optimize only one target.

Maintain a target ladder such as:

```text
stretch_but_compatible
best_fit
robust_fit
specialist_fallback
alternative_article_type
Registered Report route when prospective and eligible
```

For each target, resolve or research:

- scope;
- article type;
- contribution class;
- novelty/importance/utility/readership requirements;
- evidence maturity;
- reporting/method compatibility;
- review model;
- editorial expertise coverage;
- transfer/resubmission options;
- unresolved policy questions.

Never rank the ladder solely by prestige or impact factor.

## Self-research rule

If the current paper type, writing convention, reporting standard, figure grammar, target criterion, editorial routing rule, acceptance lever or review-closure convention is materially uncertain, **research before guessing**.

Use the unknown-paper protocol to inspect:

1. current official target guidance;
2. relevant reporting/methodological standards;
3. official editor/team/section and submission-routing information when useful;
4. rejection/desk-triage evidence where available;
5. roughly 8–15 comparable recent papers for descriptive calibration when useful;
6. 3–6 nearest-neighbor papers for deep scientific/writing/figure reasoning;
7. roughly 3–6 close public review histories when a review/closure problem is unfamiliar;
8. counterexamples and rejected-case evidence.

For public review histories, load `../nature-shared/core/public-review-history-calibration.md`. Learn scientific concern-to-repair dependencies, not wording, reviewer personalities, or accepted-paper tricks.

Create a temporary manuscript-specific profile with evidence grades and transfer limits. Do not copy wording, layouts, palettes or rebuttal language.

## Study protocol and conduct contract

Before manuscript-state claims are treated as scientific evidence, materialize the shared **study protocol/conduct decision contract** from `../nature-shared/core/study-protocol-conduct-contract.md`.

Resolve the study archetype and applicable obligations, then bind:

`protocol version -> analysis-plan version -> conduct receipt -> deviation ledger -> analysis/result -> claim`.

Keep planned, executed, verified, unknown, not done, and not applicable distinct. A **protocol/conduct blocker** is a manuscript-state blocker when it affects an in-scope claim. Valid repairs preserve history: reconcile authoritative records, append a dated deviation, rerun from a valid snapshot/split, add a versioned sensitivity analysis, reclassify exploratory/post-hoc work, narrow the claim, or request a real new prospective study. Never backdate, overwrite adverse/null evidence, or infer ethics/randomization/blinding execution from prose.

Schema/registration/reporting completion, protocol/conduct traceability, scientific validity, and journal acceptance remain separate state layers.

## Data integrity and stewardship contract

After protocol/conduct resolution and before analysis, display, claim, availability, or readiness work, materialize `../nature-shared/core/data-integrity-stewardship-contract.md`.

Bind:

`source/acquisition record -> immutable raw or exact external-reference origin -> validation/QC receipts -> versioned transformations -> immutable analysis-ready snapshot -> analysis/display inputs -> governed release -> bounded claim`.

Resolve maintained modality/governance adapters without treating them as universal or exact local policy. Preserve unmatched domains and exact institutional, legal, funder, repository, licence, consent and community obligations as live official-source research requirements.

A mutable raw snapshot, broken lineage, unreceipted transformation/QC/calibration, analysis hash mismatch, hidden adverse/null exclusion, count or unit drift, undisclosed missingness change, absent authority/rights, unauthorized release, or false repository/version statement blocks every dependent state object. Repairs must preserve history and rerun downstream work where necessary. Claim narrowing can repair an evidence-scope mismatch, but cannot create consent, rights, privacy, observations, calibration, execution, or release evidence.

## Statistical inference and uncertainty contract

After the analysis-ready data snapshot is fixed and before quantitative Results, displays, captions, claims, review, or readiness work, materialize `../nature-shared/core/statistical-inference-uncertainty-contract.md`.

Bind:

`question/claim -> estimand -> independent unit/dependence -> analysis population -> missingness/multiplicity/decision plan -> immutable input -> executed analysis + diagnostics/sensitivity -> estimate + typed uncertainty -> table/display/caption/prose bindings -> bounded claim`.

Never force a universal best test, model, interval, prior, threshold, or frequentist template. Preserve Bayesian, descriptive, exploratory, non-quantitative, adverse, harmful, null, failed and deviating routes.

Block recorded pseudoreplication, unhandled dependence, plan/execution drift, missing-data drift, unresolved confirmatory multiplicity, post-result observed power as evidence, nonconvergence, unreceipted diagnostics, invalid significance/absence/equivalence shortcuts, stale or semantically changed surface bindings, omitted planned results, and claims that outrun available calibration, prediction, or same-estimand sensitivity evidence. Claim narrowing can repair overreach but cannot create execution, independent observations, convergence, prespecification, a margin, missing-data work, or policy authority.

## Iterative lifecycle

Run the following lifecycle. Enter at the earliest stage that still applies to the real project; never pretend an earlier prospective state exists after data/results access.

### 0. Acceptance-by-design and publication-route check

If the study is not yet complete:

- test whether the scientific question is valuable/useful under plausible publication models independent of outcome direction;
- map intended claims backward to design, identification, measurements, independent units, controls, information size, uncertainty, alternatives and discriminating evidence;
- define outcome-neutral quality checks and minimum decisive evidence;
- check Registered Report eligibility before result access;
- build a fit-first target ladder when the objective is successful publication.

If the project is already complete, record which early-stage decisions are immutable and optimize only legitimate downstream levers.

### 1. Intake and evidence freeze

Separate:

- author results/data;
- manuscript claims;
- external literature;
- project/repository artifacts;
- missing evidence;
- constraints;
- publication objective and target constraints.

Never invent new study results.

### 2. Materialize protocol and conduct state

For each in-scope study, evaluate protocol/SAP timing, registration applicability, executed assignment/blinding/fidelity, outcomes, stopping, exclusions/attrition, harms, raw-data/analysis lineage, deviations and ethics/governance before licensing confirmatory or causal claim status.

### 3. Resolve the data lifecycle

Evaluate source/acquisition identity, raw/validated/analysis-ready snapshots, hashes and counts, QC/calibration, transformations, decisions/deviations, missingness, analysis/display bindings, authority/rights, sensitivity, access, retention and release. Never substitute an availability sentence for a verified release object.

### 4. Resolve statistical inference and uncertainty

Evaluate estimand/population bindings, independent unit/dependence, plan/input/execution identity, missingness, multiplicity, sample-size/information rationale, diagnostics, convergence, typed uncertainty, sensitivity, deviations, adverse/null/failed-result visibility and every table/display/caption/prose numeric binding.

### 5. Evidence-maturation red team

Before manuscript rhetoric becomes fixed, attack each headline claim from independent scientific lenses:

- domain science / nearest prior work;
- design and identification;
- measurement and controls;
- statistics/uncertainty;
- reporting-standard completeness;
- figures/tables/data visibility;
- strongest alternative explanation and failure boundary.

For each claim define the shortest evidence set that discriminates it from plausible alternatives. Do not equate maturity with experiment count.

### 6. Research, positioning and publication ecology

Research enough to establish:

- strongest relevant prior work;
- novelty/contribution boundary;
- methodological/reporting norms;
- nearest paper archetype;
- local evidence/figure expectations;
- exact target criteria;
- desk-rejection/rejection patterns where evidence exists;
- editor/team expertise coverage and submission-routing rules when relevant;
- transfer/resubmission options when relevant.

If accepted public review histories are used, pair them with rejection evidence and record survivorship bias.

### 7. Build manuscript state

Maintain **one row per atomic content item** in the atomic-claim ledger, together with evidence, figure, source, acceptance-lever and concern ledgers. Split every scientific assertion while preserving scope, qualifiers, negation, comparators, quantifiers and conditions. Verify whether the located warrant actually entails the assertion.

Build:

`question/tension -> bounded contribution -> evidence progression -> alternatives/boundaries -> meaning`

Check content richness and explanatory sufficiency.

### 8. Plan figures, tables, statistics and diagrams

For every headline claim determine:

```text
reader question
-> unit / estimand / scientific object
-> evidence/data
-> uncertainty / heterogeneity / alternative
-> text vs table vs figure vs mixed display
-> candidate representation
-> main / support / omit
```

Then materialize the shared **display contract** for every evidence-bearing figure, plot, table, image plate, diagram or mixed display. Record reader task, estimand, statistical unit, candidate representation, allowed/prohibited inferences, data snapshot, analysis receipt, render receipt, source-data object, caption denominator, uncertainty meaning, transformations, group coverage, accessibility and placement.

A **display-contract blocker** is a manuscript-state blocker when the display is required for a headline claim. Repair it by reconciling/re-rendering from real evidence, changing representation, adding a traceable companion display, or narrowing the claim—not by inventing evidence.

### 9. Draft/rewrite

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

### 10. Acceptance optimization and desk-rejection stress test

Materialize/update the acceptance-optimization plan.

Stress-test at least:

- `D1` wrong scope/article type;
- `D2` weak/unclear question, rationale or contribution;
- `D3` design cannot support the headline claim;
- `D4` methods/analysis under-described or weak;
- `D5` decisive evidence poorly presented;
- `D6` writing/explanation blocks evaluation;
- `D7` policy/compliance failure.

Every blocker needs a concrete closure test. Do not strengthen adjectives where the correct repair is evidence, claim narrowing or retargeting.

### 11. Pre-review QA

Before simulated review, check:

- claim/evidence consistency;
- protocol/conduct/deviation/claim-status consistency;
- statistical-inference contract status, typed uncertainty and current result-to-surface bindings;
- complete atomic-claim coverage and definition/proof/source entailment;
- acceptance-optimization plan schema/semantic validity;
- all hard acceptance gates satisfied or explicitly open;
- no Grade H/C/E heuristic promoted into a hard journal criterion;
- reporting/statistics;
- figure/table adequacy;
- explanation depth;
- sentence/paragraph logic;
- citations/prior work;
- main/support allocation;
- artifact leakage;
- punctuation/typography;
- exact target compliance;
- journal acceptance-readiness across scope, triage, routing and reviewer coverage.

### 12. Multi-editor editorial triage

Run independent non-biographical lenses for scope/article type, contribution/positioning, evidence maturity, readership/objective and routing clarity. Freeze each assessment before synthesis.

The simulated editor decides whether the manuscript should proceed to review or whether a target/science/readiness blocker should be repaired first. Do not simulate the psychology of a named real editor and do not count editor-lens votes.

### 13. Independent review

Run mutually blind initial reviewer contexts.

Default lenses:

- reviewer 1 — validity/methods/data/inference;
- reviewer 2 — contribution/prior work/target-specific significance or utility;
- reviewer 3 — reproducibility/reporting/clarity/boundaries/readership.

Every Major Concern requires a stable concern ID and a resolution test.

### 14. Editor synthesis

The editor weighs **arguments and expertise, not reviewer votes**.

Mark each concern as:

- must address;
- claim recalibration;
- clarity/explanation/reporting;
- surface copyedit;
- optional enrichment.

### 15. Execute minimum-sufficient revision

Do every valid repair possible with available material/tools:

- research literature;
- add/replace citations based on evidence relevance;
- reanalyse supplied data;
- calculate/check statistics;
- add/rebuild plots/tables;
- create/redesign diagrams;
- restructure evidence;
- expand missing explanation;
- repair sentence logic;
- correct reporting/punctuation;
- relocate project artifacts;
- narrow/remove unsupported claims;
- repair title/abstract/keywords/routing clarity;
- recommend target/article-type change when fit is the issue.

If the repair route is unclear, public review histories may supply Grade H concern-to-repair examples, but they do not determine the repair and cannot create new evidence.

If a real new experiment/data collection is required, mark it blocked and state the minimum resolution test. Do not fabricate it.

### 16. Freeze revision delta

Update all ledgers and the current manuscript version. Verify every claimed closure exists in the manuscript/evidence state.

Record whether each change was:

```text
new evidence
reanalysis
correction
figure/table redesign
explanation/structure repair
reporting repair
limitation added
claim narrowed
claim removed
target/article type changed
```

### 17. Targeted re-review

For major revisions, send relevant changed claims/evidence back to the original concern owner by default.

For minor clarity/surface issues, allow editor-only closure when target practice permits.

Do not re-open the whole paper from zero unnecessarily.

### 18. Moving-goalpost protection

A new blocking concern after round 1 needs a reason such as:

- revision created a new issue;
- new evidence revealed it;
- previously unassessable material became visible;
- expertise gap was discovered;
- original concern was incompletely scoped.

Otherwise treat it as late optional enrichment unless the editor independently determines it is essential to scientific validity/publication criteria.

### 19. Editor closure

Repeat revision/re-review only while a real must-address concern remains and there is a concrete resolution test.

Do **not** keep iterating just to make every reviewer maximally happy.

### 20. Rejection / transfer / retargeting loop

If a real or simulated rejection occurs, classify it before adding work:

- `R1 scientific_blocker`;
- `R2 target_mismatch`;
- `R3 manuscript_or_evidence_visibility`;
- `R4 policy_or_compliance`;
- `R5 review_disagreement_or_unresolved_argument`;
- `R6 uncontrollable_editorial_context`;
- `R7 appeal_candidate` under an exact appeal policy.

Then choose the cheapest valid route: scientific repair, reanalysis, writing/visual repair, claim narrowing/removal, appeal where justified, transfer, or retargeting.

If publisher/venue review transfer is available, preserve valid prior review and concern-closure work rather than restarting rhetorically from zero.

## Success states

### Acceptance-optimized target readiness

The acceptance optimization layer may return:

`acceptance_optimized_decision_ready_for_target`

only when preventable decision blockers have been systematically attacked, hard gates are satisfied, the scientific case is mature for the claims made, and remaining real-world uncertainty is explicitly outside the manuscript-repair state.

### Full pipeline readiness

The strongest full-pipeline success label remains:

`simulated_publication_ready_for_target`

Use it only when:

- no integrity/compliance blocker;
- no unresolved publication-criteria blocker;
- the exact target tuple/date is resolved by a supported contract, not a fallback presented as policy;
- the acceptance-optimization plan has no unresolved hard gate or repairable blocker;
- journal acceptance-readiness has no known repairable blocker across scope, contribution/readership, evidence maturity, editorial routing, reviewer coverage, editor synthesis, revision closure or compliance;
- public review histories, if used, remain survivorship-bounded context rather than causal acceptance rules;
- public editor information, if used, is bounded to professional routing and exact submission permissions rather than preference targeting;
- no unresolved technical blocker to a headline claim;
- every required statistical-inference contract passes bounded checks, exact required analysis policy is resolved for the as-of date, and all reported numbers/interval semantics bind to current analysis receipts;
- headline claims are established or appropriately narrowed;
- every in-scope atomic assertion has an allowed release status and zero `SUPPORTED_INTERNAL`, `UNRESOLVED`, `CONTRADICTED`, `BLOCKED`, or in-scope `NOT_ASSESSABLE` manuscript assertions remain;
- central alternatives/boundaries are visible;
- methods/statistics/reporting are adequate;
- figures/tables/diagrams expose the needed evidence;
- every required display contract is bound to the current data/analysis/render/source-data objects and has no display-contract blocker;
- contents are rich enough to understand without filler;
- sentence-to-sentence and paragraph logic are coherent;
- author voice is natural rather than generic/AI-like;
- citations/prior work are fair and sufficiently verified;
- main/support allocation is appropriate;
- every standalone surface is locally intelligible, every display in the abstract has a target-resolved disposition, and no unexplained private term/symbol or unresolved surface-review item remains;
- no release placeholder remains in manuscript-facing text;
- rendered artifacts, when present, pass every-page layout, metadata, accessibility and final-page/spill review;
- manuscript surfaces are free of project leakage and punctuation defects;
- remaining requests are optional enrichment or production copyedit.

This is a **simulation of readiness**, not a promise of real acceptance. Uncontrollable editorial context remains outside the certification.

## Blocked states

Return one of these instead of pretending readiness:

- `blocked_on_author_evidence`;
- `scientifically_sound_but_target_mismatch`;
- `current_claims_not_established`;
- `blocked_by_integrity_or_compliance`;
- `decision_ready_but_editorial_outcome_uncertain` when no repairable blocker remains but the real outcome is inherently unknowable.

For every block, specify the cheapest valid path forward.

## Round reporting

Keep the user-facing update compact:

```text
Round/version
Project/publication stage
Publication route / target ladder
Acceptance-optimization state
Editor posture
Must-address concerns open
Closed this round
Research/analysis/figures/writing added
Claims narrowed/removed
Acceptance-readiness/routing state
Surface QA
Next valid action
```

The final paper/deliverables remain primary. Do not bury the user under internal ledgers unless they ask.

## Red lines

Never:

- count reviewer votes as an editorial decision;
- fabricate data/experiments;
- manipulate editor/reviewer selection or citations;
- profile named editors/reviewers for personality, ideology, leniency, friendliness or acceptance propensity;
- strategically cite likely decision-makers;
- hide negative/adverse/contradictory evidence;
- add cosmetic experiments merely to look more impressive;
- optimize or report an acceptance-probability score;
- rank targets solely by prestige or impact factor;
- promote accepted public review histories into causal acceptance rules;
- copy peer-paper prose, reviewer language, rebuttal wording, figure layouts or visual identity;
- expose project filenames/paths inside the paper;
- call prose-only rebuttal a scientific closure when the manuscript/evidence remains unchanged;
- backdate Registered Report/prespecification status;
- keep extending the study after only optional enrichment remains.
