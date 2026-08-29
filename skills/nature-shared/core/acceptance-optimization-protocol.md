# Acceptance optimization protocol

> Journal-agnostic, evidence-graded protocol for maximizing **legitimate publication opportunity** by reducing preventable rejection, strengthening the scientific case, choosing a compatible publication route, and closing decision-relevant concerns. It does **not** predict acceptance, manipulate editors/reviewers, or convert correlation into a guarantee.
>
> Last reviewed: 2026-08-29.

## 1. Objective

The goal is not to make a paper look more publishable than the science warrants.

The goal is to make the **best defensible version of the scientific object** reach the **most compatible decision process** with the fewest preventable failure points.

Operationally:

```text
important / useful scientific question
-> design capable of answering it
-> evidence mature enough for the claims
-> transparent analysis and reporting
-> figures/tables that expose the evidence
-> exact target/article-type fit
-> clear editorial routing
-> expert review coverage
-> real concern closure
-> retarget/transfer when fit, not science, is the blocker
```

For a fixed target journal, optimize decision readiness under that journal's public criteria.

For a broader goal of successful publication, optimize the **target ladder** rather than prestige alone.

Never output a manuscript-specific numeric acceptance probability.

## 2. Evidence grades for acceptance levers

Every proposed acceptance lever must carry an evidence grade.

### Grade A — direct experimental / quasi-experimental evidence

Examples:

- randomized trials of statistical review or reporting-guideline review that measure manuscript quality;
- intervention studies that directly test a publication-process change.

A Grade A finding may support the measured outcome only. If a study improves manuscript quality but does not test acceptance, do not rewrite it as "increases acceptance".

### Grade B — multi-journal / large-scale observational meta-research

Examples:

- acceptance associations across many journals;
- large manuscript-level analyses of novelty, review disagreement, or editorial outcomes.

Use as a strong prior, not causal proof.

### Grade C — single-journal or narrow-domain observational evidence

Examples:

- content analysis of rejection reports;
- one-journal desk-triage studies;
- one-journal revision histories.

Use to define recurring failure modes and stress tests. Do not universalize frequencies.

### Grade D — official current venue policy or editor/reviewer instructions

Official policy is authoritative for **what the target says it evaluates or requires**, even when it is not causal evidence about acceptance across journals.

Use for exact target gates, article-type rules, reviewer criteria, Registered Report eligibility, cover-letter requirements, and submission mechanics.

### Grade E — expert editorial guidance / practice commentary

Useful for workflow ideas, especially when consistent with stronger evidence, but not a causal acceptance claim.

### Grade H — public review-history heuristic

Accepted/revised public peer-review files can reveal:

- what concerns arose;
- what authors changed;
- what evidence/claim/figure/text changes closed those concerns;
- what remained disputed.

Because these are usually selected on publication or public review availability, they are **survivorship-biased**. Learn repair patterns, never acceptance probabilities.

### Grade X — prohibited / invalid optimization

Never use:

- editor leniency or harshness profiling;
- reviewer friendliness scores;
- acceptance-propensity ranking by individual;
- strategic citation of a likely editor/reviewer;
- personal/demographic/political/religious profiling;
- hiding negative evidence;
- inflated novelty or unsupported significance;
- fabricated experiments/results;
- selective omission of competitors;
- cosmetic experiments performed only to impress a reviewer;
- gaming AI detectors or manuscript-screening systems.

## 3. Acceptance is a lifecycle, not a submission trick

A paper can lose publication opportunity at multiple stages.

```text
research-question stage
-> protocol/design stage
-> data/analysis stage
-> evidence-maturation stage
-> manuscript stage
-> journal-selection stage
-> editorial triage
-> peer review
-> editor synthesis
-> revision
-> final compliance / production
```

The later the stage, the fewer scientific variables remain safely changeable.

Therefore, the protocol uses the **earliest-fix principle**:

> If a preventable acceptance blocker can be resolved before data collection, do not postpone it to manuscript revision.

## 4. Stage -2 — acceptance by research-question design

Before running a study, ask:

1. What exact scientific question will this study answer?
2. Who should care if the answer is positive, null, negative, heterogeneous, or conditional?
3. Which publication models consider that question valuable?
4. What would make the answer informative regardless of direction?
5. What is already conventional knowledge that anchors the question?
6. What is genuinely novel rather than merely renamed or recombined?
7. What evidence would make the contribution interpretable rather than surprising but fragile?

### Novelty plus scientific grounding

Large multi-journal observational evidence suggests that novelty and conventional grounding can both be positively associated with acceptance.

Engineering consequence:

- do not maximize novelty by disconnecting the paper from established literature;
- do not maximize conventionality by removing the actual new contribution;
- build a contribution that is new **and** scientifically legible in relation to known work.

Use close analogue papers to determine what is truly nearby, but do not imitate their claims or prose.

## 5. Stage -1 — choose the publication route before the study when possible

The standard post-results article is not the only route.

### Registered Report check

For prospective studies, ask whether an exact suitable target currently offers Registered Reports.

A Registered Report may be especially appropriate when:

- the question is valuable independent of outcome direction;
- the design and analysis can be specified before outcome access;
- outcome-neutral quality controls can be defined;
- the authors want early methodological review;
- publication bias against null/negative results is a meaningful concern.

At eligible venues, Stage 1 peer review can lead to in-principle acceptance before results are known, conditional on following the approved design and providing a defensible interpretation.

Do not call Registered Reports a universal acceptance shortcut. Stage 1 can still be rejected, and some fields/journals do not support the format.

Record:

```text
RR eligible? yes / no / unknown
exact target source
Stage 1 novelty/significance criterion
methodological criterion
sampling/power requirement
outcome-neutral quality checks
allowed deviations
Stage 2 publication conditions
```

## 6. Stage 0 — design the study to survive the claims

For every headline claim, work backward from the inference.

```text
claim
-> estimand / scientific object
-> independent unit
-> design / identification
-> measurement validity
-> comparator / control
-> sample / information size
-> uncertainty
-> strongest alternative explanation
-> discriminating evidence
-> robustness / sensitivity
-> failure boundary
```

Do not rely on manuscript rhetoric to compensate for design mismatch.

Examples:

- causal wording requires a design/identification strategy capable of supporting causality;
- generalization claims require evidence beyond one convenient dataset/site/population when the claim is broad;
- mechanism claims require discriminating evidence, not only correlation/ablation;
- benchmark superiority should expose task/site/seed heterogeneity rather than a grand mean only;
- clinical prediction claims should distinguish discrimination, calibration, operating thresholds, and utility;
- null/absence claims require appropriate equivalence/non-inferiority/precision logic rather than `p > 0.05`.

## 7. Stage 1 — pre-specified evidence maturity

Before the manuscript exists, define what would count as a mature evidence package.

For each central claim record:

```text
minimum decisive evidence
required positive controls
required negative controls
required comparator/baseline
required uncertainty
required robustness/sensitivity
required external/orthogonal validation if any
outcome-neutral quality checks
claim-changing adverse/null evidence
stopping / escalation condition
```

The objective is not "more experiments".

The objective is the **shortest evidence set that discriminates the central claim from plausible alternatives**.

## 8. Stage 2 — evidence maturation before submission

Run internal red-team review before journal submission.

### 8.1 Domain-science review

Ask:

- Is the question important/useful under the target's actual objective?
- Is the nearest prior work represented fairly?
- Does the contribution survive a skeptical expert reading?
- Are boundary conditions and negative cases visible?

### 8.2 Methods/design review

Ask:

- Can the design support the inference?
- Are controls/comparators informative?
- Are measurements valid for the construct?
- Are exclusions/attrition/missingness traceable?
- Are protocol deviations visible?

### 8.3 Statistical review

Where quantitative analysis is central, run a statistical/methodological red team before submission.

Randomized peer-review experiments show that specialist statistical review can improve manuscript reporting quality. Treat that as evidence for **quality improvement**, not proof of a causal acceptance increase.

Check:

- estimands;
- independent units and dependence;
- analysis population;
- multiplicity;
- missingness;
- convergence/diagnostics;
- effect size and typed uncertainty;
- sensitivity;
- cross-surface number consistency;
- calibration/utility when claimed.

### 8.4 Reporting-standard review

Resolve the current applicable reporting guideline(s) before submission.

Use them as transparency/completeness requirements, not as substitutes for good study design.

Evidence from randomized review interventions supports possible manuscript-quality improvement from guideline-based review, but the effect is not a universal acceptance guarantee.

### 8.5 Figure/table review

For every headline claim, verify that the decisive evidence is inspectable.

Ask whether the evidence belongs in:

- text;
- a table;
- a figure;
- a mixed figure/table package;
- Methods/SI;
- nowhere.

Do not hide claim-changing limitations or heterogeneity in SI.

## 9. Stage 3 — publication-objective fit

Resolve:

`exact venue × article/content type × stage × as-of date`.

Then separate:

```text
scientific validity
journal eligibility/scope
novelty criterion
importance/significance/utility criterion
readership criterion
evidence-strength criterion
reporting/compliance criterion
publication model
review model
```

Do not average these into one prestige score.

### 9.1 Fit-first target ladder

When the goal is successful publication rather than one fixed journal, maintain a target ladder:

```text
stretch_but_compatible
best_fit
robust_fit
specialist_fallback
alternative_article_type
registered_report_route_if_prospective
```

Each target must be justified by explicit fit, not impact factor alone.

Record for every target:

- scope compatibility;
- contribution class compatibility;
- required evidence maturity;
- readership;
- article type;
- open/transparent review options;
- Registered Report availability when relevant;
- transfer/resubmission options;
- unresolved policy questions.

## 10. Stage 4 — desk-rejection stress test

Content analyses of rejection reports repeatedly surface several preventable classes.

Run a dedicated pre-submission desk test for:

### D1 — wrong target / article type

- out of scope;
- wrong article/content type;
- contribution class mismatched to venue objective.

### D2 — weak or unclear question/rationale

- research question not recoverable;
- rationale generic or circular;
- contribution depends on manufactured gap language;
- significance/utility claimed but not demonstrated under target criteria.

### D3 — design cannot support the claim

- causal overreach;
- inadequate comparator/control;
- invalid measurement/tool;
- insufficient validation;
- sample/information structure incompatible with the claim.

### D4 — methods/analysis under-described or weak

- necessary methodological decisions omitted;
- analysis rationale unclear;
- uncertainty or independent unit unclear;
- reproducibility-critical detail missing.

### D5 — evidence presentation weak

- decisive result buried;
- figure/table hides pairing/heterogeneity/uncertainty;
- exact primary values unavailable where needed;
- results and discussion repeat rather than interpret.

### D6 — writing blocks evaluation

- contribution cannot be recovered quickly;
- sentence/paragraph dependencies are broken;
- explanation is too compressed;
- terminology drifts;
- manuscript contains repository/artifact residue.

### D7 — policy/compliance failure

- ethics/registration/data/code/reporting requirement unresolved;
- template/format or anonymization violation when rejection-without-review is possible;
- related work/dual-submission policy violated.

A desk stress test is not complete until each identified blocker has a concrete resolution test.

## 11. Stage 5 — multi-editor preflight

Because editorial triage can vary, use multiple independent role-based lenses.

At minimum:

1. scope/article type;
2. contribution/positioning;
3. evidence maturity;
4. readership/target objective;
5. routing clarity.

Freeze each assessment independently.

Do not vote-count. A single valid desk-rejection argument remains a risk item even if other simulated editors would proceed.

## 12. Stage 6 — submission packaging

### 12.1 Title

The title should help the correct editor identify:

- scientific object;
- contribution class;
- population/system when relevant;
- major design feature when decision-relevant.

Do not overclaim causality, generality, mechanism, or clinical utility.

### 12.2 Abstract

The abstract should expose:

- problem/question;
- design/data;
- decisive result with appropriate quantitative context;
- bounded conclusion;
- why the result matters for the target readership.

It should not require the cover letter to explain what the paper is actually about.

### 12.3 Keywords / subject routing

Use accurate scientific/method terms that help routing.

Do not insert editor names or strategic citations.

### 12.4 Cover letter

Use current exact target instructions.

Where a cover letter is appropriate, make it a short evidence-bound routing brief:

```text
what the study establishes
why it fits this exact venue/article type
what is genuinely new/important/useful under the venue's criteria
important concurrent/related-submission information
conflicts/exclusions or required confidential handling information
```

Do not use author prestige, flattery, or unsupported "breakthrough" language.

## 13. Stage 7 — reviewer expertise coverage

For each central claim, identify expertise needed to review it fairly.

Possible dimensions:

- domain science;
- causal/design expertise;
- statistics;
- computation/ML;
- measurement/instrumentation;
- clinical/translation;
- qualitative methodology;
- resource/data stewardship;
- specialized experimental technique.

If the exact journal permits reviewer/editor suggestions, use expertise and independence only.

Never optimize suggestions for expected favorability.

## 14. Stage 8 — reviewer-proof manuscript architecture

The paper should make the skeptical path easy to follow.

For each central claim:

```text
claim
why it matters
nearest prior work
scientific unit / estimand
decisive evidence
comparator/control
uncertainty
alternative explanation
result that discriminates the alternative
boundary / limitation
figure/table/source
```

The reviewer should not have to reconstruct this chain across six sections and three supplements.

## 15. Stage 9 — review and editor synthesis

Reviewer disagreement is normal.

Therefore:

- do not optimize for unanimous enthusiasm;
- do not count reviewer votes;
- identify the strongest valid technical or publication-criteria objection;
- keep reviewer recommendation separate from argument quality;
- let the simulated editor decide which concerns are must-address.

For every major concern assign:

```text
stable concern id
challenged claim
reasoning
visible evidence
missing/ambiguous evidence
severity
publication criterion affected
resolution test
owner
status
```

## 16. Stage 10 — revision optimization

Optimize the **revision delta**, not response-letter length.

Valid closure routes:

1. add decisive evidence;
2. reanalyse existing data;
3. correct an error;
4. expose evidence already present but hidden;
5. expand missing explanation;
6. improve figure/table representation;
7. narrow the claim;
8. remove the claim;
9. change article type/target.

A reply saying "we thank the reviewer" is not closure.

### Evidence-strength lesson from revision histories

Large eLife revision data show that evidence-strength assessments often improve during revision, whereas significance assessments change less often.

Engineering consequence:

- revision is a high-value phase for strengthening evidence and calibrating claims;
- do not assume a fundamentally low-fit research question can be repaired by endless experiments;
- retarget when the scientific case is sound but the venue objective remains mismatched.

Do not impose a universal number of revision rounds. Use concrete unresolved blockers as the stopping criterion.

## 17. Stage 11 — public review-history calibration

Load `public-review-history-calibration.md` when the paper class or revision problem is unfamiliar.

Use transparent histories to learn:

- concern classes;
- evidence additions;
- reanalysis patterns;
- claim narrowing;
- figure/table redesign;
- explanation changes;
- which concerns persisted after revision.

Do not infer that a change caused acceptance merely because it appears in an accepted paper.

Pair accepted-case learning with rejection-report evidence to reduce survivorship bias.

## 18. Stage 12 — rejection triage

Classify the rejection before reacting.

### R1 — scientific blocker

The design/evidence cannot establish the headline claim.

Repair with new evidence, reanalysis, claim narrowing/removal, or a new study.

### R2 — target mismatch

The science may be sound but does not meet scope, readership, article type, significance/utility, or contribution model.

Repair by retargeting or article-type change.

### R3 — manuscript/evidence visibility failure

The evidence exists but is hard to locate, interpret, or audit.

Repair writing, figures, tables, methods, explanation, or allocation.

### R4 — policy/compliance failure

Repair the exact requirement if legitimately possible; otherwise the current target may be unavailable.

### R5 — review disagreement / unresolved technical argument

Reassess the strongest concern and evidence. Do not assume the negative reviewer is wrong or that more reviewer votes solve it.

### R6 — uncontrollable editorial context

Examples:

- overlapping work;
- competition among strong submissions;
- reviewer availability;
- legitimate soft-criterion disagreement;
- confidential information;
- editorial discretion not reducible to public criteria.

Do not respond with automatic extra experiments or personalized editor targeting.

### R7 — appeal candidate

Use only when the exact target has an appeal process and there is a specific factual/procedural/scientific basis.

An appeal is not a second cover letter.

## 19. Stage 13 — transfer and retargeting strategy

If the scientific case is mature, preserve useful review work.

Check whether the publisher/venue supports:

- manuscript transfer;
- review transfer;
- author response transfer;
- direct resubmission after revision;
- public-review reuse.

When previous review is transferable, map every concern to its current closure state before resubmission.

Do not restart the paper rhetorically from zero if the science and prior review work remain valid.

## 20. Acceptance opportunity matrix

For every serious target maintain:

| Axis | State |
|---|---|
| exact venue/article type/date resolved | satisfied / uncertain / blocked |
| scientific integrity | satisfied / uncertain / blocked |
| scope | satisfied / uncertain / blocked |
| contribution / novelty | satisfied / uncertain / blocked |
| significance / utility / readership, if applicable | satisfied / uncertain / blocked / N/A |
| evidence maturity | satisfied / uncertain / blocked |
| design/statistics/reporting | satisfied / uncertain / blocked |
| visual evidence | satisfied / uncertain / blocked |
| editorial routing | strong / mixed / weak / unknown |
| reviewer expertise coverage | strong / mixed / weak / unknown |
| Registered Report route | available / unavailable / not applicable / unknown |
| revision closure | closed / open / not yet reviewed |
| policy/compliance | satisfied / uncertain / blocked |
| uncontrollable context | unknown / known contextual risk |
| cheapest valid next action | text |

Do not collapse the table to one acceptance score.

## 21. Cost-aware repair ordering

When multiple valid repairs exist, prioritize by:

```text
scientific necessity
× decision consequence
× claim centrality
× feasibility with current evidence
× reversibility
```

Do **not** prioritize by what seems most impressive.

A cheap clarification that exposes already-existing decisive evidence can dominate an expensive experiment that adds no discrimination.

Conversely, no amount of writing should substitute for missing evidence required by the central claim.

## 22. Stop rules

Stop adding work when:

- no integrity/compliance blocker remains;
- central claims are supported or narrowed;
- exact target criteria are satisfied or explicitly uncertain rather than guessed;
- the strongest plausible desk-rejection arguments are closed;
- required reviewer expertise is identifiable;
- no publication-criteria or technical blocker remains;
- remaining changes are optional enrichment or production polish.

Do not keep extending the study merely to maximize an imagined acceptance score.

## 23. Unknown-domain fallback

If the field, journal, article type, or publication model is unfamiliar:

1. resolve current official target policy;
2. identify reporting/methodological standards;
3. inspect rejection/desk-triage evidence where available;
4. inspect 8–15 comparable recent papers for descriptive calibration;
5. inspect 3–6 close public review histories if available;
6. include counterexamples and rejected-case evidence;
7. create a temporary manuscript-specific acceptance profile;
8. label every learned pattern by evidence grade.

No unsupported local pattern becomes a permanent universal rule.

## 24. Release state

The strongest pre-submission label allowed by this protocol is:

`acceptance_optimized_decision_ready_for_target`

It means:

- preventable decision blockers have been systematically attacked;
- the scientific case is mature for the claims made;
- the target and publication model are compatible;
- the paper is easy to route and review;
- remaining real-world editorial uncertainty is not being misrepresented as controllable.

It does **not** mean likely accepted or guaranteed acceptance.
