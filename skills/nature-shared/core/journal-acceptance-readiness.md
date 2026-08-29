# Journal acceptance readiness

> Shared, journal-agnostic contract for making a scientifically valid manuscript easier for the correct journal to evaluate, route, review, revise, and publish. This contract does **not** predict acceptance and does not authorize manipulation of editors or reviewers.
>
> Last reviewed: 2026-08-29.

## Principle

There is no single "key" to journal acceptance and no universal acceptance score.

A useful operational model is:

```text
scientific validity and integrity
-> exact target eligibility/scope
-> editorial triage/readership/contribution
-> editor/expertise routing
-> external technical review
-> editorial synthesis
-> revision closure
-> final reporting/compliance
```

The package should improve the manuscript at every stage that can be improved without changing the truth of the work.

The goal is **decision readiness**:

> a qualified editor and reviewer should be able to identify the contribution, see why it fits the target, locate the decisive evidence, understand the boundaries, and determine what—if anything—still blocks publication.

## What the system may optimize

The system may improve:

- target-journal and article-type fit;
- scope and readership alignment;
- contribution clarity;
- novelty/context positioning supported by literature;
- claim–evidence alignment;
- evidence completeness and visible limitations;
- figure/table/data presentation;
- explanatory sufficiency and sentence logic;
- methods/statistics/reporting transparency;
- editor/reviewer routeability;
- cover-letter clarity;
- permitted editor/reviewer suggestions based on expertise and independence;
- revision plans and concern closure;
- retargeting when a sound paper is mismatched to the current venue.

It may **not** optimize acceptance by flattering individuals, exploiting perceived leniency, strategically citing an editor/reviewer, hiding competing work, withholding adverse evidence, or profiling personal characteristics.

## Acceptance-readiness object

Maintain a journal-specific record with these independent axes:

```text
Target identity
Article/content type
Submission stage
As-of date

Science/integrity state
Scope eligibility
Contribution/novelty state
Readership/importance state
Evidence maturity
Methods/statistics/reporting state
Visual evidence state
Editorial routing state
Peer-review risk state
Revision closure state
Compliance/production state

Blocked criteria
Uncertain criteria
Best valid repair
Retargeting option
```

Use categorical states such as:

- `satisfied`;
- `uncertain`;
- `blocked`;
- `not_applicable`;
- `requires_live_research`.

Do not output a numeric acceptance probability.

## Gate 0 — science, integrity, eligibility

Before optimizing presentation, confirm that the manuscript has no unresolved blocker involving:

- ethics/consent/registration;
- authorship/conflicts;
- duplicate publication;
- data/image integrity;
- fabrication/falsification/plagiarism;
- unsupported statistical inference;
- missing required data/code/material availability;
- article-type eligibility.

A rhetorical repair cannot close these blockers.

## Gate 1 — exact target and article-type fit

Resolve the exact target tuple:

`venue × article/content type × stage × as-of date`.

Use current official sources. Then ask:

1. Is this topic actually within scope?
2. Is this contribution class publishable in this article type?
3. Does the journal require novelty, field advance, broad interest, clinical importance, methodological utility, rigor only, or another explicit objective?
4. Is the manuscript asking the journal to value something the journal does not claim to value?
5. Would claim narrowing preserve target fit or reveal that another venue is more appropriate?

Do not repair target mismatch with stronger adjectives.

## Gate 2 — editorial triage

The first editorial question is often not "is every analysis perfect?" but:

> Is there a sufficiently clear, relevant, mature and target-appropriate scientific case here to justify external review?

Build an editor-facing decision brief:

```text
Question / unresolved problem
Bounded contribution / answer
Decisive evidence
Why this matters under this journal's explicit objective
Why this audience should care
Most important boundary / limitation
What distinguishes it from the nearest prior work
```

The editor should be able to recover the case quickly **without relying on the cover letter to rescue a weak manuscript**.

### Multi-editor preflight

Because desk-triage judgments can vary, run several independent editorial lenses before submission:

1. **scope/article-type lens** — is this the right journal and content type?
2. **contribution/positioning lens** — is the actual advance recoverable and fairly situated?
3. **evidence-maturity lens** — is the paper mature enough to justify reviewer time?
4. **readership/objective lens** — does the work meet the target's explicit interest/importance/utility standard?
5. **clarity/routeability lens** — can an editor identify the field, methods, evidence class and reviewer expertise needed without reconstructing the project?

Freeze each assessment independently before synthesis.

A plausible desk-rejection argument becomes a risk item even when another lens would proceed to review.

Do not count editor-lens votes. Resolve the strongest valid blocker.

## Gate 3 — editorial routing and expertise coverage

Load `editor-expertise-routing.md`.

Public editor identities may be used only for bounded professional purposes:

- confirm the journal has credible expertise coverage for the manuscript;
- identify the most appropriate subject section/team;
- support an editor suggestion **only when the exact submission system permits it**;
- avoid conflicts of interest;
- clarify which technical reviewer expertise the paper will require.

Do not infer or exploit an individual editor's personality, leniency, citation preferences, social/political views, demographic identity, or presumed acceptance tendency.

Weak routing clarity can be repaired by a more precise title/abstract/keywords, a clearer contribution class, explicit methods/evidence tags, or a better target—not by naming an editor inside the manuscript.

## Gate 4 — reviewer coverage

Reviewers are selected for expertise. Before submission, create a **reviewer expertise coverage map** rather than a list of friendly people.

For each central claim identify what expertise is required to evaluate:

- study design/identification;
- domain science;
- statistics/computation;
- measurement/instrumentation;
- clinical/translation/context;
- data/resource/reproducibility;
- any specialized technique.

If the journal permits reviewer suggestions, suggest independent experts who collectively cover the manuscript's technical surface.

Never select reviewers because they are expected to be favorable.

## Gate 5 — reviewer-proof evidence architecture

For every headline claim maintain:

```text
Claim
Why it matters
Evidence
Scientific/statistical unit
Comparator/control
Uncertainty
Strongest alternative explanation
Discriminating test/analysis
Boundary
Figure/table/source
Target criterion
```

The strongest acceptance improvement is often not more prose but making the decisive evidence and the strongest plausible alternative easy to inspect.

## Gate 6 — editor synthesis after review

Editors adjudicate reviewer arguments; they do not simply count recommendations.

Classify each concern into:

- publication-criteria blocker;
- technical blocker;
- major repairable concern;
- claim recalibration;
- clarity/reporting issue;
- surface issue;
- optional enrichment.

A single decisive technical concern can block publication. Multiple negative reviewer recommendations do not create a blocker if their reasoning is not valid under the journal's criteria and evidence.

## Gate 7 — revision closure

Optimize the **revision delta**, not the length of the response letter.

Valid closure routes include:

- add decisive evidence;
- reanalyse existing evidence;
- correct an error;
- expose evidence already present but hard to find;
- expand missing reasoning/explanation;
- redesign a misleading or weak figure/table;
- narrow a claim;
- remove a claim;
- change target/article type.

After revision, re-review the changed scientific object against the original concern ID and resolution test.

## Cover letter as routing aid, not sales copy

A cover letter may help an editor understand:

- what the manuscript establishes;
- why it fits the exact journal;
- what is novel or important under that journal's public criteria;
- relevant related/concurrent submissions;
- conflicts, reviewer/editor exclusions, or other confidential handling information where appropriate.

Keep it short and evidence-bound.

Do not use:

- flattery of the editor/journal;
- author prestige/CV arguments;
- unsupported claims of "breakthrough" or "first ever";
- strategic citations to named editors;
- claims not recoverable from the manuscript.

The manuscript itself must carry the scientific case.

## Presubmission enquiry

Use only when the exact journal currently offers one and when the information requested can be supplied accurately.

A positive response is not acceptance and may not guarantee peer review; a negative response does not prove the science is weak.

## Retargeting is an acceptance tool

A sound manuscript can be unpublishable at one target because its contribution is too specialized, not broad enough, the wrong article type, or outside scope.

Retargeting is not failure. It is often the highest-value repair when the scientific case is already mature but the target objective is mismatched.

Maintain a target ladder based on:

```text
scientific scope
contribution class
article type
required novelty/importance/utility
readership
methods/reporting compatibility
editorial expertise coverage
practical constraints
```

Do not rank journals solely by prestige or impact factor.

## What public editor identities can and cannot tell us

### Legitimate signals

- official role/team/section;
- publicly stated subject coverage;
- public professional research expertise;
- whether the journal's editorial structure appears to cover the manuscript;
- whether an exact journal permits authors to request/suggest an editor;
- conflicts of interest that make assignment inappropriate.

### Non-legitimate or unreliable signals

- inferred personal taste;
- whether the editor is "easy" or "hard";
- acceptance/rejection propensity from a small public sample;
- citation preferences;
- political/personality profiling;
- presumed reviewer network friendliness;
- private editorial discussions;
- attempts to predict a specific individual's decision.

Treat editor identity as **routing metadata**, never as a persuasion target.

## Acceptance-readiness exit state

A manuscript may be labelled:

`decision_ready_for_submission_to_target`

only when:

- scientific/integrity blockers are closed;
- exact target/article type/stage is resolved;
- scope and target objective are satisfied or explicitly uncertain rather than guessed;
- contribution and nearest-prior-work distinction are recoverable;
- decisive evidence and boundaries are visible;
- the figure/table package exposes the scientific case;
- methods/statistics/reporting are adequate;
- editorial routing is clear;
- reviewer expertise coverage is identifiable;
- cover letter/submission metadata are accurate and non-manipulative;
- no known publication-criteria blocker remains.

This state means **ready for a fair editorial decision**, not "likely accepted".

## Research basis

Current official/editorial and meta-research reviewed 2026-08-29 includes:

- Nature Communications editorial process and peer-review criteria;
- Nature publication criteria and reviewer/editor decision policies;
- Nature Geoscience cover-letter editorial guidance;
- PLOS editor assignment and PLOS ONE editor-request workflow;
- Nature Communications public editor-team/expertise pages;
- 2026 meta-research on reviewer recommendation disagreement and editorial outcomes;
- 2026 research on desk-rejection disagreement among co-editors;
- multi-journal research on novelty and acceptance;
- rejection-report analyses identifying scope, novelty, methodology, rationale and writing as recurring failure classes.

Exact current target guidance always overrides this shared model.
