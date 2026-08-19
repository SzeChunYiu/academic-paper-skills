# Related Work / Literature Synthesis Guide

The purpose of literature writing is to reconstruct the **decision space of prior knowledge** so the reader can see what is established, contested, assumed, missing, and relevant to the present question.

## Contents

- [Start with the research question](#start-with-the-research-question)
- [Build a literature matrix](#build-a-literature-matrix)
- [Choose an organizing dimension](#choose-an-organizing-dimension)
- [Synthesis paragraph moves](#synthesis-paragraph-moves)
- [Citation roles](#citation-roles)
- [Contradictions and disagreements](#contradictions-and-disagreements)
- [Positioning the present work](#positioning-the-present-work)
- [Discipline variants](#discipline-variants)
- [Audit](#audit)

## Start with the research question

Do not begin by collecting `recent papers` and then inventing a story around them.

Write:

1. the exact live question/tension;
2. which parts of that question require prior knowledge;
3. what kinds of sources can establish those parts;
4. which directly competing/alternative explanations or approaches matter.

Literature belongs when it helps the reader reason toward the present study, interpret its design, or evaluate its contribution.

## Build a literature matrix

Before prose, summarize important sources in a matrix such as:

| Source | Question | Approach/design | Data/population | Main finding | Assumption | Strength | Boundary | Relation to present question |
|---|---|---|---|---|---|---|---|---|

Add field-specific columns when useful:

- theory/mechanism;
- benchmark;
- effect/uncertainty;
- causal identification;
- external validation;
- source/corpus;
- historical context;
- replication status.

The matrix prevents citation-by-citation summaries from becoming the section structure.

## Choose an organizing dimension

Organize by the dimension that exposes the intellectual structure.

### Explanation/theory

Useful when the key issue is competing accounts of the same phenomenon.

### Method/design family

Useful when approaches differ in representation, assumptions, trade-offs, measurement, or inferential strategy.

### Evidence class

Useful when evidence strength varies: observational vs randomized, simulation vs experiment, lab vs field, single-dataset vs external validation, primary vs secondary source.

### Population/setting/regime

Useful when generalizability is the live problem.

### Trade-off

Useful in engineering/computing: accuracy-cost, resolution-scale, interpretability-performance, flexibility-robustness.

### Historical/chronological

Use chronology when development itself explains why concepts/claims changed. Do not use it as the default simply because publication dates are easy to sort.

### Historiographic/source tradition

Useful in humanities when schools of interpretation, source bases, editions, or conceptual traditions organize the dispute.

## Synthesis paragraph moves

A strong paragraph may contain:

1. **nucleus** — a claim about a body of literature;
2. **evidence** — representative sources, not necessarily every source;
3. **comparison** — how approaches/findings relate;
4. **qualification** — limits, scope, conflicting evidence;
5. **consequence** — what the synthesis means for the live question.

Example abstract pattern:

```text
Several studies support explanation A under condition X. [evidence]
Evidence under Y is less consistent, partly because ... [contrast/explanation]
Thus the open issue is not whether A occurs, but whether it generalizes when ... [consequence]
```

This is stronger than `Author 1 did X. Author 2 did Y. Author 3 did Z.` because it gives the reader a proposition to evaluate.

## Citation roles

Annotate citations by role before drafting:

### Background/factual support

Supports a descriptive field statement.

### Attribution/origin

Credits an idea, method, dataset, concept, theorem, measure, or source.

### Representative example

Shows a class of work; do not imply exhaustiveness.

### Consensus evidence

Multiple sources genuinely support the same proposition.

### Contradictory/limiting evidence

Shows disagreement or narrows a claim.

### Methodological precedent

Supports use/adaptation of a design or procedure.

### Comparison/baseline

A direct alternative against which the present work is evaluated.

### Theory/framework

Provides the conceptual model used to interpret the current study.

### Provenance

Establishes source/data/software/material origin.

A cluster of citations can contain different roles. If so, split the proposition rather than presenting them as interchangeable support.

## Contradictions and disagreements

Do not resolve conflicts rhetorically before analyzing why they differ.

Compare:

- population/system;
- measurement/operationalization;
- intervention/exposure;
- sample size/power;
- data quality;
- model/specification;
- assumptions;
- time period;
- external conditions;
- publication/source context;
- interpretation rather than observation.

Then distinguish:

- **true contradiction** — comparable evidence supports opposing conclusions;
- **boundary difference** — both results can be true under different conditions;
- **measurement difference** — constructs/outcomes differ;
- **method difference** — estimator/design changes what can be inferred;
- **evidence-strength difference** — one claim has stronger warrant;
- **apparent contradiction** — authors use different language for compatible results.

The present study may be motivated by discriminating among these possibilities.

## Positioning the present work

A literature section should enable accurate positioning, not create a sales funnel.

Legitimate relationships include:

- extends prior result to a new condition;
- tests a proposed mechanism;
- resolves a contradiction;
- provides stronger identification/measurement;
- independently validates/replicates;
- removes an assumption;
- creates a common benchmark/resource;
- integrates previously separate ideas;
- contradicts a prior expectation;
- synthesizes a fragmented literature;
- applies a known approach where the application itself answers a substantive question.

Say which relationship applies.

### Incremental work

If the work is incremental, make the increment **auditable**:

`previous capability/claim -> exact change -> evidence that the change matters -> boundary`

Do not obscure the predecessor.

### Novel terminology

Do not rename an established idea to imply novelty. If terminology differs across fields, define the correspondence.

## Discipline variants

### Engineering / computer science

Often includes a separate Related Work section and direct technical comparisons. Cover strongest baselines and assumptions. Conference papers may be primary literature.

### Natural/biomedical science

Literature is often integrated into Introduction and Discussion. Primary studies should support specific experimental claims; reviews are useful for broad context.

### Clinical / epidemiological

Study design, population, effect uncertainty and guideline/evidence hierarchy matter. Do not synthesize heterogeneous observational/RCT evidence as if equally causal.

### Social science

Theoretical frameworks, constructs, measurement traditions and competing explanations can require deeper conceptual synthesis before the empirical gap becomes clear.

### Humanities

Monographs, chapters, primary texts, archives, editions and historiography may be central. `Recent papers + technical gap` is often the wrong model.

### Review/meta-analysis

The literature itself is the data. Search/inclusion/risk-of-bias/synthesis methods belong to Methods, while the narrative should reflect systematic evidence rather than selective exemplars.

## Audit

1. Can every paragraph nucleus be stated without author names?
2. Are strongest relevant alternatives represented fairly?
3. Does each citation have a clear role?
4. Are primary sources used where a specific primary claim matters?
5. Are reviews used appropriately for synthesis/background rather than misrepresented as primary evidence?
6. Are contradictions analyzed rather than merely listed?
7. Is `not studied` distinguished from `does not work`?
8. Is a method limitation distinguished from weak evidence or narrow scope?
9. Does the section explain why the present question remains live without devaluing successful prior work?
10. Is the present contribution's relationship to predecessors explicit enough for a reviewer to verify?

If the literature story collapses when one `however` sentence is removed, the synthesis may not yet be real.