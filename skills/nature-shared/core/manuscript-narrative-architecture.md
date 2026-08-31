# Manuscript narrative architecture and reader-state contract

> Shared release contract for making a scientific paper read as one argument rather than as a sequence of locally correct sections, experiments, audit events, or repository-derived summaries.
>
> The target is not a universal IMRaD template. The target is **dependency-complete scientific narration for the intended reader**.

## Core principle

A manuscript is not coherent merely because adjacent sentences connect.

The reader must be able to recover, in order:

```text
scientific problem
-> why existing knowledge leaves it open
-> exact question / object / estimand
-> what must be defined before the question can be tested
-> evidence sequence
-> answer
-> interpretation relative to alternatives and prior work
-> boundary / implication
```

Every substantial paper must therefore be audited at three scales:

1. **manuscript argument architecture**;
2. **section and subsection function**;
3. **reader-state activation in reading order**.

A paper can pass sentence-level cohesion and still fail all three.

## 1. Build the manuscript argument graph before polishing

For each central paper, freeze a compact argument graph:

```text
Q0  scientific problem or unresolved tension
G0  knowledge gap / decision gap
O1  central scientific object or estimand
C1  headline claim / bounded answer
E1  first necessary evidence or theorem
E2  discriminator / mechanism / validation / generalization
A1  strongest alternative or failure explanation
B1  claim-changing boundary
M1  scientific meaning / consequence
```

Use only the nodes the paper actually needs. Do not invent a rigid number of claims or experiments.

For every edge, name the dependency:

- motivates;
- defines;
- makes identifiable;
- tests;
- discriminates;
- validates;
- generalizes;
- qualifies;
- contradicts;
- interprets;
- enables.

If two neighboring major sections have no meaningful dependency edge, investigate whether the paper is narrating execution chronology rather than scientific reasoning.

## 2. Section-function contract

Every section or substantive subsection must have a reader-facing function record:

```text
section:
reader question:
prerequisites already active:
new object/evidence introduced:
claim or uncertainty discharged:
what later section depends on this:
handoff:
```

A section heading is not evidence that the function was performed.

### Functional sufficiency, not word-count sufficiency

Do **not** impose universal minimum word counts.

A short section is sufficient when it discharges every downstream dependency with minimal explanation.

A short section is **underdeveloped** when later text relies on:

- an undefined object;
- an unstated research question;
- an unexplained design choice;
- an unintroduced comparator/model/dataset;
- an unstated assumption;
- an uninterpreted metric;
- an experimental label whose scientific identity is not yet known;
- a distinction that exists only in internal notes or code.

A long section can fail for the same reason if it contains background but not the needed definitions or logic.

## 3. Problem-formulation / theory-opening gate

When a paper contains a section such as `Problem formulation`, `Framework`, `Theory`, `Model`, `Task definition`, or `Formal setup`, the section must leave the reader able to answer all applicable questions before Results/Experiments rely on them:

1. What is the scientific problem being formalized?
2. What is the unit/object/world/sample/system under study?
3. What is observable to the method and what is protected/latent/held out?
4. What is the target quantity, state, label, action, or estimand?
5. What are the central variables/symbols and their domains?
6. What assumptions or restrictions make the object well-defined?
7. What comparison or failure would answer the research question?
8. What terminology is paper-specific rather than field-standard?
9. How does the formal object connect to the experiment that follows?

The section does not need to contain implementation details, long proofs, or every later hyperparameter.

It must contain the **conceptual prerequisites** later claims depend on.

### Formal-object handoff

Before the first empirical subsection, provide a short bridge of the form:

```text
formal distinction / quantity
-> observable experimental consequence
-> design that tests it
```

The exact wording is free. The dependency is not.

## 4. Reader-state activation law

Treat the reader's active knowledge as a state that grows in reading order.

For every nonstandard term, model name, dataset, hypothesis label, experiment ID, comparator, metric, symbol, acronym, status, and paper-specific distinction, record:

```text
reader-facing identity
category
first claim-bearing occurrence
activation location
minimum definition/description needed
later shorthand allowed?
```

### Meaning before use

At first claim-bearing use, the reader must already know enough to identify the object and understand its role.

Bad ordering:

```text
D1 improves transfer ...
...
Section 4.5: D1 is the whole-domain transfer experiment.
```

Better ordering:

```text
We next test whole-domain procedural transfer (experiment D1) ...
```

The ID can then be used sparingly.

### Scientific name before project label

Default order:

```text
reader-facing scientific name -> optional internal/compact label
```

not

```text
project label -> definition several pages later
```

This applies to labels such as `D0`, `D1`, `M1`, `V3`, `P4-X`, `H2`, `A5`, task-family IDs, version names, and similar paper-private shorthand.

## 5. No surprise-entity rule

A central entity must not appear for the first time as if it had already been part of the study.

Examples:

- a model family suddenly appearing in Results (`Qwen`, `GPT-*`, a new classifier, a new comparator);
- a dataset first appearing in a table row;
- a hypothesis first appearing only when declared passed/failed;
- a metric first appearing as a table column without semantic interpretation;
- a baseline first appearing in a figure legend;
- a formal symbol first appearing inside a theorem consequence.

Before the first result about an entity, the paper must normally establish:

```text
what it is
+ why it is included
+ what role it plays in the comparison
+ any constraint needed to interpret its result
```

The explanation may be one phrase when the object is standard and obvious to the target reader.

## 6. Tables and figures do not get a terminology exemption

Tables and figures are reader-facing scientific surfaces.

Before or at a table/figure's first appearance:

- every central row/column category must be understandable;
- abbreviations and paper-private labels must be expanded locally when needed;
- the main text should orient the reader to the comparison the display performs;
- a table must not become the first place where a central experiment/model/hypothesis is silently introduced.

A legend can locally define display-specific notation, but it should not carry the entire conceptual definition of a headline object that the prose already reasons about.

## 7. Results must be a question chain, not a run log

For each major Results block, use this dependency structure when applicable:

```text
local question
-> why this analysis is needed now
-> essential setup/comparator
-> observation / estimate
-> uncertainty / discriminator
-> bounded local answer
-> next unresolved question
```

Do not force all seven into seven sentences. Combine them naturally.

### Analysis-to-analysis necessity

For every major analysis after the first, answer:

> What did the previous result leave unresolved that makes this analysis necessary?

Legitimate answers include:

- mechanism;
- alternative explanation;
- robustness;
- external validity;
- subgroup/heterogeneity;
- computational sufficiency;
- calibration;
- causal identification;
- boundary/failure mode;
- practical usefulness.

`We next evaluate...` is not itself a scientific dependency.

### Chronology scrub

Experiment/version chronology belongs in Results only when chronology changes scientific interpretation, for example:

- prospective versus outcome-informed design;
- a repair creates a materially different estimand;
- independent replication;
- a predeclared hypothesis genuinely failed and the failure is scientifically relevant.

Parser fixes, dependency repairs, smoke tests, version numbers, artifact recovery, and administrative sequence normally belong in Methods, provenance records, or repository documentation.

## 8. Paragraph-to-section and section-to-section handoff

At the end of each major block, identify one useful handoff:

- answer now established;
- uncertainty now localized;
- alternative remains;
- generalization now testable;
- assumption now exposed;
- next scale/domain now relevant;
- implication now interpretable.

The next block should inherit that state.

If the next block changes topic entirely, signal why the change is necessary for the paper's central case.

## 9. Introduction architecture

An effective Introduction normally lets the reader reconstruct:

```text
field/problem
-> unresolved scientific tension or limitation
-> why the closest existing approaches do not settle this exact question
-> bounded research question
-> approach/contribution preview
-> main result/meaning preview at target-appropriate detail
```

Do not turn the Introduction into:

- a catalogue of everything the field has done;
- a novelty-defence ledger;
- a sequence of disclaimers about what the paper does not own;
- repository/project history.

The closest prior work should sharpen the research need rather than interrupt it.

## 10. Discussion architecture

A Discussion is not a longer limitations section and not a repetition of Results.

For every headline finding, decide which of these interpretive functions are genuinely needed:

### D1 — scientific meaning

What changed in our understanding because of the result?

### D2 — mechanism / explanation

What mechanism, mathematical relation, or process is consistent with the finding? What is demonstrated versus merely plausible?

### D3 — strongest alternative

What other explanation could produce the pattern, and what evidence does or does not discriminate it?

### D4 — relation to prior work

Does the result agree, extend, qualify, reconcile, or conflict with the closest literature?

Do not repeat the whole Related Work section. Discuss only literature that changes interpretation.

### D5 — boundary / generalizability

Where should the claim stop? Which population, regime, dataset, interface, assumption, or scale remains untested?

### D6 — practical / methodological implication

What would a researcher, method designer, practitioner, or theorist do differently if the result is correct?

### D7 — next discriminator

What unresolved question is now scientifically sharper than before this study?

Not every finding needs D1–D7. A Discussion is deep when it contains the **minimum sufficient interpretive chain**, not when it is long.

### Discussion-depth failure

Flag a Discussion as underdeveloped when it mainly contains:

- summary of Results;
- lists of what is not established;
- generic future work;
- audit/provenance chronology;
- repeated caution without interpretation;
- literature names without explaining agreement/disagreement;
- implications asserted without a reasoning bridge.

## 11. Results–Discussion separation

Results owns:

- what was tested;
- what was observed/estimated;
- uncertainty and primary local inference;
- immediate conclusion-changing qualification.

Discussion owns:

- interpretation;
- relation to strongest prior evidence;
- alternatives;
- generalization;
- broader methodological/scientific consequence;
- unresolved questions.

Some venues merge Results and Discussion. The functional distinction still applies even when the sections are physically combined.

## 12. Content-proportion audit

Do not allocate space according to project effort.

A six-week debugging sequence may deserve one Methods sentence. A central definition that took one hour may deserve half a page because every result depends on it.

Allocate explanatory space by:

```text
claim centrality
× reader unfamiliarity
× dependency burden
× interpretive consequence
```

not by development duration or number of archived artifacts.

## 13. Reverse-outline audit

After drafting, produce a one-line reverse outline for every paragraph:

```text
P1 function -> claim/question
P2 function -> claim/question
...
```

Then ask:

- Does each paragraph advance the central argument?
- Are two paragraphs performing the same function?
- Is any necessary step missing?
- Is an entire section mostly provenance, defence, or chronology?
- Does a paragraph depend on a concept introduced later?
- Does the order minimize reader backtracking?

Reorder by dependency before polishing sentence style.

## 14. Zero-context reconstruction test

Give the current manuscript, without repository/programme notes, to a clean reviewer.

After the Introduction + setup/formulation, they should be able to explain:

- the question;
- why it matters;
- the central scientific objects;
- the main comparison logic;
- what each major experiment is for.

After Results, they should be able to explain:

- the evidence sequence;
- which result answers which question;
- the strongest surviving claim;
- the strongest unresolved alternative/boundary.

After Discussion, they should be able to explain:

- what the findings mean relative to prior knowledge;
- where the claim stops;
- why the next question is scientifically different from the one just answered.

If they cannot, the manuscript is not release-ready even when every sentence is factually correct.

## 15. Release blockers

Block full-manuscript readiness when any central claim depends on:

- an object defined only after use;
- an entity appearing first in a result/table without adequate activation;
- a missing argument edge between major evidence blocks;
- a section whose title exists but whose downstream prerequisites remain undefined;
- a Discussion that provides no adequate interpretation of headline findings;
- project chronology substituted for scientific narrative;
- a central comparison whose inclusion/rationale is never explained.

## Boundaries

Do not use this contract to:

- impose one universal section order;
- require a separate Related Work or Discussion section when the venue/genre does not use one;
- inflate every short section;
- explain genuinely standard specialist terms unnecessarily;
- invent motivations or mechanisms;
- hide adverse results for narrative smoothness;
- convert a clean formal paper into tutorial prose.

The goal is dependency-complete reader logic, not maximal explanation.
