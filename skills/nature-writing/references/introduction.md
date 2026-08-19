# Introduction writing guide

Use this reference to build the **reasoning that makes the study necessary**. Do not start from a four-paragraph template or from the desire to manufacture a dramatic literature gap.

## Contents

- [The Introduction's job](#the-introductions-job)
- [Build the backward logic first](#build-the-backward-logic-first)
- [Move families](#move-families)
- [Research-need types](#research-need-types)
- [Prior-work positioning](#prior-work-positioning)
- [Contribution positioning](#contribution-positioning)
- [Common architectures](#common-architectures)
- [Method/algorithm subtype](#methodalgorithm-subtype)
- [Theory subtype](#theory-subtype)
- [Clinical/social-science subtype](#clinicalsocial-science-subtype)
- [Humanities/qualitative subtype](#humanitiesqualitative-subtype)
- [Paragraph logic](#paragraph-logic)
- [Ending the Introduction](#ending-the-introduction)
- [Audit](#audit)

## The Introduction's job

By the end of an Introduction, the intended reader should be able to answer:

1. What phenomenon/problem/question is this paper about?
2. Why is it worth resolving for this research community?
3. What does existing knowledge already establish?
4. What exactly remains live or uncertain?
5. Why is the present study an appropriate response?
6. What will the paper attempt to establish, and within what scope?

Not every answer needs its own paragraph, and not every field answers them in that order.

## Build the backward logic first

Start from the paper's evidence, then reason backward.

### A. What does the paper truly establish?

Write the bounded answer without prestige language.

### B. What evidence is decisive?

Identify which experiment, comparison, analysis, proof, source set, or observation makes the answer credible.

### C. What question would make that evidence necessary?

The research question should create a legitimate reason for the decisive evidence to exist.

### D. What prior knowledge makes that question understandable but still unresolved?

This determines what belongs in the Introduction. Background that does not help the reader reach the live question is expendable.

Then write forward from context/knowledge to need to study response.

## Move families

### Move A — establish territory/context

Possible functions:

- define a phenomenon only if readers need the definition;
- establish theoretical importance;
- establish practical/clinical/engineering consequence;
- state a robust known relationship;
- identify an emerging capability or dataset that changes what can now be studied.

Avoid generic importance openings that could introduce hundreds of papers.

### Move B — synthesize current knowledge

Explain the state of knowledge at the level needed to create the present question.

- group studies by explanation, method family, assumption, evidence class, population, or trade-off;
- distinguish established findings from contested ones;
- identify where evidence is direct versus indirect;
- name important constraints fairly.

### Move C — create the research need

A research need can be a gap, but often it is something more precise. See the types below.

### Move D — sharpen the question or design requirement

Translate the broad need into a question that can be answered by the paper's evidence.

### Move E — state the present response

State the objective, hypothesis, design, contribution, or organizing lens. Explain a key design choice if readers would otherwise misunderstand why this approach can answer the question.

### Move F — preview scope/evidence/contributions

Preview enough for orientation. Do not turn the Introduction ending into a compressed Results section unless the journal/genre expects it.

Moves may recur. A complex Introduction can establish one line of work, expose a limitation, introduce a second line that partly solves it, then reveal a more precise unresolved tension.

## Research-need types

Use the type that matches the science instead of forcing `few studies have...`.

### Unanswered question

A meaningful variable, mechanism, population, regime, or consequence is genuinely unknown.

### Contradictory evidence

Credible studies support different conclusions. The Introduction should identify what differs among them and what evidence could discriminate.

### Missing mechanism/explanation

The phenomenon is established but the mechanism, causal pathway, or conceptual explanation is not.

### Weak or indirect evidence

A claim is widely repeated but rests on surrogate outcomes, observational evidence, small samples, simulations, one dataset, or another limited basis.

### Measurement/identification limitation

The field cannot currently distinguish entities, quantify a process, isolate causality, or observe the needed scale/resolution.

### Methodological trade-off/bottleneck

Existing methods trade accuracy for cost, resolution for scale, interpretability for performance, flexibility for robustness, etc. State the trade-off rather than labeling all prior work inadequate.

### Missing condition/population/scale

A result is known in one regime but transferability is uncertain elsewhere.

### External-validation/robustness need

A promising result exists but has not survived independent data, laboratories, populations, devices, time periods, or perturbations.

### Replication need

An influential claim needs an adequately powered or independently designed replication. Replication is a substantive contribution; do not disguise it as novelty.

### Resource/standardization need

Progress is hard to compare because datasets, benchmarks, taxonomies, reporting standards, or common protocols are missing or fragmented.

### Theory–data mismatch

Observed behavior conflicts with a prevailing prediction or framework.

### New opportunity

New instrumentation, data, computation, policy change, or natural experiment makes a previously inaccessible question testable. The opportunity itself can motivate the study without attacking prior work.

## Prior-work positioning

### Synthesize, do not parade citations

A useful prior-work paragraph usually has:

`claim about a body of work -> representative evidence -> comparison/limitation -> consequence for present question`

The citation list is support for the synthesis, not the paragraph's organizing principle.

### Separate limitation types

Be precise about what is limited:

- **method limitation** — the approach cannot represent/measure/do X;
- **evidence limitation** — the claim has not been tested under X;
- **scope limitation** — evidence is valid but only for X;
- **reporting limitation** — needed detail/data is unavailable;
- **conceptual limitation** — the model does not explain X;
- **practical limitation** — cost, latency, safety, scalability, etc.

Do not call a method deficient merely because it was designed for a different question.

### Treat strong prior work fairly

The strongest motivation often comes from showing exactly what prior work accomplished and why a more specific question now becomes possible. A contribution does not become weaker because it has intellectual ancestry.

## Contribution positioning

State contribution magnitude accurately.

### Incremental extension

Say what changes relative to the previous method/claim and why the difference matters. Examples of legitimate value include wider regime, reduced cost, stronger validation, improved uncertainty, new mechanism, better measurement, or removal of an assumption.

Do **not** hide the baseline or historical relationship to make an incremental contribution appear discontinuous.

### New method/resource

Explain the design principle and what capability it enables. Avoid claiming the pipeline components themselves are novel when the contribution is their integration or a new use.

### New finding/mechanism

State the question and evidence class; reserve causal/mechanistic wording for evidence that can support it.

### Negative/replication result

Explain why the original claim was important enough to retest and what the new evidence changes about its scope.

## Common architectures

### Problem-led

`consequence/importance -> current knowledge -> unresolved question -> present study`

### Theory-led

`theoretical issue -> competing accounts -> evidence that would discriminate -> present test`

### Contradiction-led

`established expectation -> conflicting observations -> source of uncertainty -> discriminating study`

### Method-led

`needed capability -> current trade-off -> design requirement -> proposed principle/method -> evaluation scope`

### Observation-led

`surprising phenomenon -> current explanations -> why they do not settle it -> analysis/test`

### Resource/benchmark-led

`fragmented practice -> comparability/reuse problem -> requirements for a common resource -> present resource/benchmark`

### Replication/validation-led

`important prior result -> uncertainty about robustness/generalization -> why independent test matters -> replication/extension design`

### Opportunity-led

`new capability/data/event -> previously inaccessible question -> present study`

Architecture is selected from the paper, not from prestige.

## Method/algorithm subtype

The previous version of this guide was largely a computational-pipeline guide. Keep those patterns only for the papers that need them.

A useful algorithmic Introduction may move:

`task/capability -> technical bottleneck/trade-off -> prior method families -> design principle -> proposed approach -> evaluation questions`

### Useful questions

- What exact failure/trade-off does the method address?
- Is that failure empirically demonstrated or merely asserted?
- What design principle connects problem to method?
- Which contribution is conceptual versus implementation-level?
- What evidence will test the claimed advantage: baselines, ablations, complexity, stress test, external benchmark, failure analysis?

The existing local examples under `references/examples/introduction/` can still be used for computational papers, but they are examples of one publication ecology rather than universal structures.

## Theory subtype

A theory/formal Introduction may prioritize:

- formal problem and importance;
- relationship to known results;
- unresolved mathematical/conceptual obstacle;
- assumptions;
- main theorem/result and why it matters;
- proof idea or implications.

It may state the main result early because the novelty is the formal result itself rather than an empirical reveal.

## Clinical/social-science subtype

These introductions often need more room for:

- population/context;
- construct/outcome definition;
- competing explanations/confounding;
- prior effect estimates and uncertainty;
- measurement validity;
- treatment/policy/practice stakes;
- study design needed to support the intended inference.

A short technical `gap -> solution` funnel can erase the inferential problem the study is actually solving.

## Humanities/qualitative subtype

Do not force a technical-challenge narrative.

The Introduction may instead:

- establish an interpretive/historiographic problem;
- position a conceptual lens;
- identify a neglected source, reading, voice, context, or contradiction;
- explain the corpus/case and analytic stance;
- state an argument rather than a testable hypothesis.

For qualitative research, the phenomenon, research question, participant/context rationale, and analytic perspective may be central.

## Paragraph logic

Plan paragraphs as nucleus + satellites.

Possible Introduction nuclei:

- why phenomenon X matters;
- what is known about mechanism Y;
- why explanation A is insufficient under condition B;
- why two literatures create a contradiction;
- what design requirement follows;
- what this study tests/provides.

A paragraph can contain evidence, comparison and qualification as satellites. Do not split solely because multiple rhetorical functions appear.

Use `paragraph-flow.md` to check handoffs. A good sequence makes the next paragraph feel like the question created by the previous one.

## Ending the Introduction

The ending should make the paper's response legible.

Depending on genre, include some combination of:

- research question/objective/hypothesis;
- core contribution;
- study design/approach;
- evidence classes;
- scope/boundary;
- contribution list for engineering/CS when conventionally useful.

Avoid laundry-list contributions whose items mix methods, routine experiments, and broad claims at the same level.

## Audit

Before drafting prose, test:

1. Can the live research need be named more precisely than `a gap exists`?
2. Does every literature paragraph help create or sharpen that need?
3. Is prior work represented fairly, including what it succeeds at?
4. Does the study response actually address the stated need?
5. Is the contribution type accurately named?
6. Does the Introduction promise only what the Results/analysis can support?
7. Are causal/mechanistic claims compatible with study design?
8. Is the final paragraph orienting rather than marketing?
9. Could a skeptical field expert explain why the study is necessary after reading only the paragraph nuclei?
10. Does the target journal require a different article-type-specific opening/summary structure?

If #4 fails, the problem is the paper argument, not the prose.