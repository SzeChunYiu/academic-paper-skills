# Scientific rhetorical act and result-state contract

> Fine-grained writing contract for turning scientific evidence states into reader-facing prose without collapsing distinct results into `positive`, `negative`, or `null` templates.
>
> Last reviewed: 2026-09-02.

## Core invariant

A result sentence should be written from its **scientific state**, not from whether a P value crossed a threshold and not from whether the authors like the outcome.

Use:

```text
scientific question
-> target quantity / proposition
-> observed pattern
-> uncertainty / diagnostic state
-> inferential class
-> analysis role
-> claim-changing consequence
-> rhetorical act
-> wording
```

The same numerical direction can support different prose under different designs. Conversely, the same phrase (`no effect`) can be valid in one analysis and invalid in another.

Do not treat these as synonyms:

```text
non-significant
!= no effect
!= evidence of absence
!= equivalence
!= non-inferiority
!= failed hypothesis
!= inconclusive
!= negative control
!= adverse result
```

Likewise:

```text
statistically significant
!= important
!= causal
!= robust
!= generalizable
!= primary
!= confirmatory
```

## 1. Atomic representation

For each claim-bearing result block, resolve a state vector before drafting:

```text
Q = local scientific question
T = target quantity / relation / proposition
O = observed pattern or estimate
U = uncertainty / compatibility / diagnostic state
D = inferential decision class
R = role in the study (primary, secondary, validation, control, exploratory, etc.)
P = prespecification status
C = scientific consequence for the current argument
```

The manuscript wording is a realization of `(Q,T,O,U,D,R,P,C)`, not of `P < 0.05` alone.

When any field is unresolved and could change the wording materially, do not draft a stronger claim from intuition.

## 2. Result polarity is not enough

Avoid using `positive result` and `negative result` as the primary internal categories because they are ambiguous.

`Positive` can mean:

- estimate above zero;
- desired outcome;
- statistically significant;
- evidence supporting a hypothesis;
- successful control;
- harmful event that is positively detected.

`Negative` can mean:

- estimate below zero;
- adverse/harmful outcome;
- non-significant test;
- evidence against a hypothesis;
- failed control;
- evidence of absence.

Prefer explicit state labels below.

## 3. Evidence-state taxonomy

### A. Descriptive observation

Use when reporting what was observed without a population-level inferential claim.

Typical act:

```text
object/population -> observed pattern -> denominator/unit -> local meaning
```

Good prose identifies the scientific object, not the software operation that produced the summary.

Do not convert descriptive separation into population certainty merely because the difference is visually large.

### B. Directional estimate with compatible uncertainty

Use when the estimate has a direction and the analysis supports an inferential contrast.

Write:

```text
comparison + direction/magnitude + uncertainty + bounded consequence
```

Lead with the scientific relation when it is the paragraph's message. Dense arrays belong in the display/table.

### C. Supported superiority / directional effect

Use only when the design and analysis support that decision.

State the effect and uncertainty before celebrating statistical significance.

Avoid:

- `highly significant` as a substitute for magnitude;
- implying practical importance from a small P value;
- promoting a secondary significant result over a non-significant primary result.

### D. Ordinary non-significant result / failure to reject

This state means the analysis did not establish the tested directional difference under the stated framework.

It does **not** establish absence or equivalence.

Prefer language such as:

```text
the estimated difference was X (interval ...), and the analysis did not provide clear evidence of a difference under this design
```

or, when the exact target/style calls for it:

```text
there was no statistically significant difference ...
```

Then use the interval/design to explain what effects remain compatible with the data.

Do not write:

- `there was no effect`;
- `the groups were the same`;
- `the hypothesis was proven false`;
- `the methods were equivalent`;
- `the treatment was ineffective`;

unless a different inferential framework actually supports those claims.

### E. Inconclusive / imprecise result

Use when the evidence is too imprecise to distinguish scientifically important possibilities.

The key rhetorical act is **preserve the live alternatives**.

Write the estimate/interval and say what competing interpretations remain compatible.

An inconclusive result should not be cosmetically reframed as either a weak positive or a reassuring negative.

### F. Evidence of absence / practically negligible effect

Use only when the analysis can support an absence claim at a stated scale, for example with an appropriately designed equivalence analysis, Bayes-factor framework, posterior decision, or another justified method.

State:

- what effect magnitude counts as meaningfully absent/negligible;
- the inferential method;
- the evidence/interval relative to that region;
- the bounded absence claim.

Prefer:

```text
the data provide evidence against effects of at least [scientifically meaningful magnitude] under [conditions]
```

rather than metaphysical claims that an effect is exactly zero.

### G. Equivalence

Equivalence is a positive inferential conclusion about a **bounded difference region**, not a synonym for non-significance.

Report the prespecified or otherwise justified equivalence margin and show how the interval/test relates to it.

If the margin was selected post hoc, disclose that and lower the inferential status accordingly.

### H. Non-inferiority

State:

- direction of benefit/harm;
- non-inferiority margin;
- effect scale;
- relevant confidence bound;
- whether the bound satisfies the decision criterion.

Do not translate non-inferiority into superiority unless superiority is separately established under the appropriate hierarchy.

### I. Supported adverse / harmful effect

Harm is not rhetorically secondary merely because the intervention's intended effect is beneficial.

Write harms with the same discipline used for benefits:

```text
harm outcome + denominator/exposure + absolute/relative estimate when appropriate + uncertainty + consequence
```

Do not euphemize adverse evidence, bury it after favorable secondary outcomes, or omit zero-event prespecified harms when reporting standards require them.

Distinguish:

```text
zero events observed
!= harm not assessed
!= harm not reported
```

### J. Failed prespecified hypothesis

A failed hypothesis is a relation between a prespecified prediction and the observed evidence.

State:

```text
prespecified prediction -> observed result -> what part of the prediction was not supported -> consequence for the argument
```

Do **not** automatically infer the stronger competing explanation.

Example of the distinction:

```text
The prespecified monotone-scaling prediction was not supported: performance did not increase detectably across the tested model sizes. Because the analysis was not designed to establish equivalence across sizes, this result leaves small or heterogeneous scale effects unresolved.
```

If an absence-capable analysis does exclude effects above a meaningful magnitude, that stronger conclusion can be stated separately.

### K. Failed replication / non-replication

Distinguish:

- failure to reproduce a direction;
- estimate incompatible with the original estimate;
- estimate compatible with both the original effect and zero because of imprecision;
- successful replication of the effect size within a justified tolerance;
- conceptual versus direct replication.

Do not write `failed to replicate` when the new study is simply underpowered or the interval remains compatible with the prior estimate.

### L. Contradictory evidence

When two analyses or datasets support materially different conclusions, surface the contradiction rather than averaging it away linguistically.

Write:

```text
result A under condition A
contrasts with
result B under condition B
-> candidate explanations / boundary / unresolved discriminator
```

Contradiction can be scientifically central even when one result is inconvenient.

### M. Heterogeneous / interaction result

The rhetorical object is the **difference in effects**, not whether one subgroup is significant and another is not.

Use an interaction/heterogeneity estimate or another design-appropriate comparison.

Do not infer subgroup differences from:

```text
P < 0.05 in subgroup A
and
P > 0.05 in subgroup B
```

alone.

State the heterogeneity evidence, then describe subgroup estimates as context.

### N. Robustness / sensitivity result

First say what was changed:

- model specification;
- exclusion rule;
- prior;
- transformation;
- missing-data assumption;
- outcome definition;
- data subset;
- estimator;
- representation;
- preprocessing choice.

Then say whether the **same scientific conclusion** persisted.

Do not call an analysis `robustness` when it targets a different estimand or scientific question.

If a sensitivity analysis changes the conclusion, that is not a nuisance to hide. It reveals an assumption-dependent claim.

### O. Positive control

A positive control asks whether the system can detect an effect that should be detectable.

Its rhetorical consequence is typically local:

```text
positive control succeeded -> assay/model/procedure had relevant sensitivity under this condition
```

It does not automatically validate every causal assumption, exclusion restriction, endpoint, or generalization claim in the study.

### P. Negative control

A negative control tests whether a signal appears where it should not under the target interpretation.

State:

```text
control purpose -> expected null/negative pattern -> observed evidence -> what artifact/confound is made less plausible
```

A negative control that is merely non-significant may itself be inconclusive unless the design supports the absence claim needed for the control.

### Q. Unexpected / anomalous result

Do not rewrite an unexpected observation as though it had been the original hypothesis.

Separate:

```text
prespecified question
from
post hoc observation
from
new explanatory hypothesis
```

Use direct language such as `unexpectedly`, `in an exploratory analysis`, or `this observation motivated...` when accurate.

Avoid retrospective inevitability.

### R. Exploratory / post hoc result

Exploratory evidence can be important. Its inferential status must remain visible.

State what was exploratory and avoid borrowing confirmatory language from prespecified results.

Exploratory findings can motivate a new discriminator or study; they do not become confirmatory because they are mechanistically attractive.

### S. Threshold / criterion result

When a decision depends on a prespecified threshold, report:

- the quantity;
- threshold;
- uncertainty/tolerance as appropriate;
- which side of the criterion the result lies on;
- how close it is to the boundary when that affects interpretation.

Do not round away the criterion crossing.

### T. Boundary / failure-mode result

A failure case can be a main scientific result when it defines where the method, theory, or phenomenon stops working.

Write it as a boundary:

```text
under condition X, the expected relation breaks / reverses / becomes unstable
-> therefore the headline claim is limited to Y
```

Do not hide the failure in supplementary material if it materially changes the main claim.

## 4. Rhetorical acts beyond result polarity

A manuscript sentence or paragraph can perform one or more of the following acts. Use the act to choose syntax and placement.

### Orientation

Activate the object, context, or reader state needed for what follows.

### Definition

Bind a term/symbol/object to its scientific meaning.

### Motivation

Explain why the next scientific operation is necessary.

### Gap / unresolved tension

Identify exactly what current evidence/theory does not resolve.

### Objective / question

State what the present analysis/paper asks.

### Observation

Report what was measured or found.

### Estimate

Quantify a target relation with uncertainty.

### Comparison / contrast

Put two quantities, mechanisms, theories, or studies into a common comparison.

### Explanation / mechanism

Propose or test how/why the observed result arises.

### Discriminator

Use evidence that separates competing explanations.

### Validation

Test whether a result/model/procedure behaves as required under an independent or orthogonal criterion.

### Generalization

Test or argue transfer beyond the immediate training/sample/domain setting.

### Qualification / boundary

Restrict the claim where the evidence requires it.

### Limitation

Identify an unresolved property of the design/evidence and state which inference it weakens.

### Interpretation

State what the result means scientifically.

### Prior-work relation

State whether the current result agrees, conflicts, extends, narrows, or addresses a different question from previous evidence.

### Implication

State what becomes possible, likely, or worth reconsidering because of the finding.

### Speculation / hypothesis generation

Propose an explanation or next hypothesis whose evidential status is explicitly lower than an established result.

### Handoff

Create the reason for the next paragraph/analysis/section.

If a paragraph has no identifiable act beyond `more information`, its inclusion is suspect.

## 5. Atomic Results paragraph patterns

Do not force one template, but make the dependency recoverable.

### Confirmatory directional result

```text
question/rationale
-> estimate/pattern
-> uncertainty/decision
-> bounded inference
-> next unresolved question
```

### Inconclusive result

```text
question
-> estimate + interval/diagnostic
-> scientifically important possibilities still compatible
-> what cannot be concluded
-> what discriminator would resolve it
```

### Evidence-of-absence result

```text
absence question + meaningful effect region
-> method capable of addressing absence
-> evidence relative to that region
-> bounded absence conclusion
```

### Heterogeneity result

```text
why a common effect may be misleading
-> interaction/heterogeneity evidence
-> subgroup/condition pattern
-> boundary or mechanism implication
```

### Robustness result

```text
assumption/choice challenged
-> alternative analysis
-> whether claim survives
-> if not, which assumption now limits the claim
```

### Failure-mode result

```text
headline expectation
-> condition where it breaks
-> evidence
-> revised scope of claim
```

## 6. Positive and adverse findings should receive symmetric scientific treatment

Do not let rhetorical enthusiasm determine evidential detail.

For both favorable and unfavorable results, preserve:

- target quantity;
- comparison;
- denominator/unit;
- magnitude;
- uncertainty;
- role (primary/secondary/exploratory/control);
- prespecification status;
- scientific consequence.

A favorable secondary result does not rescue a failed primary endpoint without changing the claim hierarchy.

An adverse result does not become optional because it complicates the narrative.

## 7. Anti-spin rules

Flag the following patterns for repair:

### Secondary-outcome rescue

A non-significant/inconclusive primary result is followed by emphasis on significant secondary/subgroup/within-group results as though the primary claim succeeded.

### Trend laundering

`trend toward significance`, `approached significance`, or equivalent wording is used to imply a positive result from an unestablished threshold crossing.

Describe the estimate and uncertainty instead.

### Null-to-equivalence laundering

`P > alpha` becomes `no difference`, `same`, `equivalent`, `unchanged`, or `ineffective` without an absence-capable design.

### Significance-to-importance laundering

A small P value becomes `large`, `important`, `meaningful`, `substantial`, or `transformative` without magnitude/context supporting that evaluation.

### Causal laundering

Association/observational evidence is written with causal verbs unsupported by the design.

### Abstract optimism drift

The abstract/title/conclusion is more favorable, certain, or general than the Results evidence.

### Harm minimization

Adverse findings are omitted, linguistically softened, or presented only in relative/absolute terms chosen to reduce apparent importance without scientific justification.

### Selective robustness

Only sensitivity analyses preserving the preferred result are described while claim-changing sensitivities are hidden.

### Post hoc confirmation

An exploratory result is narrated as a predicted/confirmatory finding.

### Boundary deletion

A failure case that changes the claim is omitted from the main scientific synthesis.

## 8. What distinguishes a well-written scientific article from a poorly written one

Writing quality is not grammatical smoothness alone.

A **well-written** article lets a qualified clean reader reconstruct, with low unnecessary effort:

```text
question
-> target scientific object
-> design / formal assumptions
-> decisive evidence
-> uncertainty
-> competing explanation
-> bounded answer
-> consequence
```

and correctly distinguish which propositions are observed, estimated, proved, exploratory, null/inconclusive, adverse, equivalent, speculative, or generalizable.

A **poorly written** article may be grammatically polished but still fail because it makes the reader infer one or more of those relations.

### Dimension 1 — Evidence-state fidelity

Well written:

- each result's wording matches its inferential state;
- absence claims have absence-capable evidence;
- exploratory findings remain exploratory;
- negative/adverse results are visible.

Poorly written:

- significance threshold determines rhetoric;
- null results become no-effect claims;
- post hoc results are retrofitted as hypotheses;
- inconvenient results disappear.

### Dimension 2 — Message hierarchy

Well written:

- the reader can identify the central result of each paragraph/section;
- quantitative detail supports rather than buries the message;
- primary evidence is not displaced by secondary trivia.

Poorly written:

- the result is discoverable only after reading a number dump;
- every result has equal rhetorical weight;
- the paper's strongest claim is unclear.

### Dimension 3 — Logical dependency

Well written:

- each experiment/formal step exists because the previous state leaves a specific question open;
- paragraph order reflects scientific dependency.

Poorly written:

- experiment chronology substitutes for reasoning;
- `next`, `additionally`, and `furthermore` hide missing logic;
- sections could be permuted without changing apparent meaning.

### Dimension 4 — Reader-state control

Well written:

- terminology is active before claim-bearing use;
- prerequisites arrive before they are needed;
- paragraphs have identifiable nuclei and handoffs.

Poorly written:

- models, datasets, metrics, symbols, or hypotheses appear first in tables/Results;
- definitions arrive after use;
- paragraph openings assume project knowledge.

### Dimension 5 — Uncertainty as scientific content

Well written:

- uncertainty changes the claim where it should;
- intervals/diagnostics are interpreted for scientific compatibility;
- imprecision is distinguished from absence.

Poorly written:

- uncertainty is decorative notation after a point estimate;
- P values replace effect interpretation;
- wide intervals are verbally collapsed to a binary conclusion.

### Dimension 6 — Positive/negative symmetry

Well written:

- favorable, adverse, failed, and null findings are reported according to scientific role;
- primary/secondary status remains visible regardless of direction.

Poorly written:

- positive findings receive mechanism and implication paragraphs while negative findings receive one apologetic clause;
- adverse outcomes are buried;
- a failed primary outcome is rescued rhetorically by secondary signals.

### Dimension 7 — Section/register fitness

Well written:

- Abstract compresses;
- Methods makes procedure recoverable;
- Results exposes evidence progression;
- Discussion interprets;
- captions decode;
- supplement supports scrutiny.

Poorly written:

- every section sounds like the same generic academic paragraph;
- Results contains mini-Discussion essays;
- Discussion merely repeats Results;
- Methods contains promotional interpretation.

### Dimension 8 — Element economy

Well written:

- every retained paragraph/display/citation/formal object performs a necessary reader/scientific function;
- scarce venue space deepens central science before broadening trivia.

Poorly written:

- material survives because it was generated, analyzed, cited, or already written;
- closest-work inventories, caveats, robustness dumps, or implementation chronology crowd out explanation.

### Dimension 9 — Display/prose complementarity

Well written:

- prose states the pattern/meaning;
- figures expose inspectable structure;
- tables preserve exact lookup;
- captions make displays locally interpretable.

Poorly written:

- prose recites table cells;
- plots hide heterogeneity/pairing/uncertainty;
- figures are decorative or dashboard-like.

### Dimension 10 — Authorial judgment without performance

Well written:

- authors take responsibility for choices and interpretations;
- stance changes with evidence state;
- prose is direct when the evidence is direct.

Poorly written:

- agentless phrases hide consequential choices;
- every paragraph uses the same hedge/booster sequence;
- prestige adjectives substitute for scientific consequence.

### Dimension 11 — Literature relation

Well written:

- prior work is synthesized where it helps define, compare, or interpret the current result;
- conflicting literature is confronted directly.

Poorly written:

- citations are wallpaper;
- one-paper-per-sentence catalogues replace synthesis;
- novelty is claimed by adjective rather than exact residual difference.

### Dimension 12 — Cross-surface consistency

Well written:

- abstract, Results, figure, table, Discussion, and conclusion preserve the same result identity, magnitude, uncertainty, and bounded claim.

Poorly written:

- confidence increases as the paper moves toward the abstract/conclusion;
- rounded values imply different decisions;
- a null primary outcome becomes a positive headline.

## 9. Clean-reader result test

For every headline result, a reader who has not seen the project history should be able to answer:

1. What scientific question was being tested?
2. What target quantity/relation answers it?
3. What was observed/estimated?
4. How uncertain is that result?
5. What inferential state does the evidence support?
6. Was this primary/confirmatory, secondary, control, validation, or exploratory?
7. What can now be concluded?
8. What important alternative remains?
9. Why does the next paragraph/analysis exist?

If the reader cannot answer because the prose only says `significant`, `non-significant`, `passed`, `failed`, or lists numbers, the writing is incomplete.

## 10. Interaction with other contracts

Use with:

- `statistical-inference-uncertainty-contract.md` for analysis semantics;
- `epistemic-rhetoric-and-qualification.md` for claim strength and caveat placement;
- `section-register-and-human-scholarly-style.md` for section/archetype realization;
- `manuscript-element-justification.md` for why a result paragraph belongs;
- `figure-purpose-representation-optimization.md` for visual representation;
- `abstract-information-budget.md` for which result states deserve abstract space;
- `manuscript-narrative-architecture.md` for result ordering and handoffs.

Statistics decides what the evidence licenses. This contract decides how that licensed state should be communicated.

## 11. Anti-bureaucracy boundary

Do not create a heavy ledger for every ordinary descriptive sentence.

Use explicit state records for:

- headline/claim-bearing results;
- null/inconclusive/equivalence/non-inferiority results;
- adverse/harm outcomes;
- failed hypotheses/replications;
- subgroup/heterogeneity claims;
- robustness/sensitivity results that affect scope;
- exploratory findings elevated to main-text interpretation;
- contradictions/failure modes;
- abstract/conclusion statements.

For routine prose, the atomic state can remain an internal reasoning step.

## 12. Release checks

Before publication-ready status:

- no non-significant result is silently written as absence/equivalence;
- every supported absence/equivalence claim states the meaningful region/margin or equivalent inferential basis;
- primary, secondary, exploratory, control, and post hoc roles remain visible when they affect interpretation;
- failed hypotheses state what failed without automatically proving the alternative;
- subgroup differences are supported by interaction/heterogeneity evidence when required;
- adverse/harms and zero-event outcomes are not selectively omitted;
- sensitivity analyses that change the claim are visible;
- no `trend toward significance` language is used to manufacture a positive result;
- effect magnitude and uncertainty carry more scientific weight than threshold labels;
- abstract/title/conclusion do not become more favorable or certain than the Results;
- each headline result has a clean-reader recoverable evidence state and scientific consequence.

Operating principle:

> **Write the evidence state you actually have—not the result polarity you hoped for.**
