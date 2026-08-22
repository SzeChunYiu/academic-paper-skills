# Explanatory sufficiency

> Shared contract for deciding whether an academic manuscript explains an idea deeply enough for its intended reader without turning the paper into a textbook or implementation manual. Last reviewed: 2026-08-23.

## Purpose

A paper can be concise and still be under-explained.

A common failure in machine-assisted academic writing is **explanatory underspecification**: the text names a concept, method, mechanism, result, or implication in polished compressed prose but leaves out one or more reasoning steps the reader needs to actually understand it.

Typical symptoms:

- a new idea is introduced and summarized in one sentence before the reader knows what it is;
- a method is named but its scientific purpose is not explained;
- a result is reported without explaining what comparison or pattern makes it meaningful;
- an interpretation jumps directly from observation to conclusion;
- an equation is presented without an intuitive explanation of its role;
- a figure is cited without telling the reader what to notice and why it matters;
- a central technical concept is defined once but never connected to the problem it solves;
- a paragraph is short and grammatically clean but assumes several unstated premises;
- a citation is used as a substitute for local explanation of a concept the reader must understand now.

The goal is **minimum sufficient explanation**, not maximum detail.

Use this contract to decide:

> Has the intended reader been given enough context, reasoning, and interpretation to reconstruct the idea without guessing?

## Core principle

Do not optimize simultaneously for `shorter` and `more complete` by deleting reasoning.

Use adaptive elaboration:

`reader model -> novelty/cognitive load -> explanation need -> minimum sufficient explanation -> placement`

The amount of explanation should rise when material is:

- central to the paper's contribution;
- novel or unfamiliar to the intended audience;
- conceptually dense;
- cross-disciplinary;
- necessary to interpret a headline result;
- a consequential methodological decision;
- a non-obvious causal/mechanistic inference;
- a surprising result;
- a boundary or exception that changes the claim;
- difficult to infer from a figure/table alone.

The amount can fall when material is:

- routine and genuinely standard for the intended audience;
- already explained adequately nearby;
- operational artifact detail better placed in Methods/SI/repository documentation;
- a secondary robustness check that does not change interpretation;
- a repeated explanation that no longer serves a new reader task.

## Audience model first

Before judging explanation depth, define the intended reader.

Ask:

1. What background can reasonably be assumed from the target field/article type?
2. Is the venue broad-disciplinary or specialist?
3. Is this section read by a broader audience than the rest of the paper?
4. Is the concept native to the target field or borrowed from another discipline?
5. Is the concept established, emerging, or introduced by this paper?
6. What information has this manuscript already made active for the reader?

Do not use `experts know this` as a blanket excuse for compression.

Flag an assumption as unsafe when a competent target reader could follow the field generally but still need a local explanation to interpret this paper's specific claim.

For broad journals, titles/abstracts/summary paragraphs usually require a lower assumed-knowledge baseline than specialist Methods.

## The explanation packet

For every important new idea, choose the **minimum subset** of the following elements needed by the reader.

### E1 — identity: what is it?

Provide enough definition or characterization to distinguish the concept from nearby alternatives.

Possible forms:

- direct definition;
- short appositive;
- operational definition;
- conceptual contrast;
- equation plus plain-language meaning;
- schematic/figure support.

Do not define common specialist terms merely to satisfy a template.

### E2 — purpose: why is it here?

Explain why the idea/method/analysis is necessary for the paper's problem.

Useful questions:

- What uncertainty does it resolve?
- What limitation of the previous approach does it address?
- What reader question makes this step necessary now?
- Why this method/quantity rather than an obvious alternative?

### E3 — mechanism or logic: how does it work?

When the relationship is not obvious, expose the intermediate logic.

This can be:

- causal/mechanistic reasoning;
- mathematical intuition;
- algorithmic scientific logic at the method level, not code internals;
- experimental dependency;
- conceptual relationship among variables;
- inferential bridge from evidence to claim.

### E4 — evidence/observable consequence: how would we know?

Show what evidence makes the idea testable or interpretable.

Possible forms:

- predicted pattern;
- comparison/control;
- measurable quantity;
- representative observation plus quantification;
- theorem implication;
- source/case evidence;
- figure/table cue.

### E5 — boundary/assumption: when does it hold?

State assumptions or limits when they materially change interpretation.

Do not bury a claim-changing assumption in SI merely to keep the main text smooth.

### E6 — connection: what does this enable next?

Make clear what changes in the reader's model because this explanation was provided.

Examples:

- why the next experiment is necessary;
- what a result now means;
- what comparison is now interpretable;
- why the contribution matters;
- what uncertainty remains.

Not every idea needs all six elements. The contract is **selective**.

## Reader reconstruction test

After an important explanatory unit, ask whether the intended reader can answer the relevant questions without external reconstruction:

- **What** is the object/idea/result?
- **Why** is it relevant here?
- **How** does it work or connect logically, when non-obvious?
- **What evidence** supports or operationalizes it?
- **What comparison/baseline** gives the result meaning?
- **What assumptions or boundaries** matter?
- **What follows** from it?

If several answers require guessing, the unit is under-explained even if every sentence is grammatical.

## Hidden-premise / conceptual-jump audit

For adjacent propositions A -> B, ask:

> What must the reader believe or know for B to follow from A?

Write the missing premise explicitly during diagnosis.

Then classify it:

- safe shared knowledge -> can remain implicit;
- already established locally -> no expansion needed;
- specialist but essential -> explain briefly;
- paper-specific assumption -> state explicitly;
- disputed inference -> justify or weaken the claim;
- unsupported leap -> add evidence/reasoning or remove the inference.

This audit is especially important for phrases such as:

- `therefore`;
- `thus`;
- `suggesting that`;
- `indicating that`;
- `which enables`;
- `this demonstrates`;
- `we therefore propose`;
- `consistent with a mechanism in which...`.

A connective does not supply the missing premise.

## Compression-risk signals

Treat these as prompts to inspect explanation depth, not automatic errors.

### New concept + immediate conclusion

Pattern:

`We introduce X, which enables Y.`

Question:

Does the reader know what X changes, why that produces Y, and how Y is observed?

### Named method without scientific rationale

Pattern:

`We use X to analyse the data.`

Question:

Why is X appropriate for the estimand/design/problem, especially if the choice affects interpretation?

### Result without comparison meaning

Pattern:

`Performance reached 0.84.`

Question:

Relative to what baseline, uncertainty, practical scale, or competing method is 0.84 meaningful?

### Mechanism claim without discriminating evidence

Pattern:

`These results reveal mechanism M.`

Question:

Which observation distinguishes M from the strongest plausible alternative?

### Figure reference without visual interpretation

Pattern:

`The results are shown in Fig. 3.`

Question:

What pattern should the reader see, and what narrow inference does it support?

### Equation without semantic interpretation

Pattern:

`We define L = ...`

Question:

What does L measure/control/penalize, how do its terms behave, and why is that relevant to the method?

### Citation as explanation substitute

Pattern:

`We use X [12].`

Question:

Does the current reader need a one-sentence explanation of X's role here even if the method is cited?

### Dense noun stack

Pattern:

`cross-domain representation alignment uncertainty regularization`

Question:

Have relationships among the concepts been compressed into nouns that should instead be expressed as clauses?

### One-sentence novelty packet

Pattern:

problem + new method + mechanism + benchmark + implication all appear in one sentence.

Question:

Would two or three reasoning steps make the contribution easier to understand without becoming verbose?

## Section-specific sufficiency

### Abstract

The abstract is compressed, but a competent target reader should still recover:

- the problem/context;
- what was done or introduced;
- the main result;
- the bounded implication.

For broad audiences, avoid assuming specialist context merely to save words.

### Introduction

Elaborate enough that the reader can understand:

- the scientific problem/tension;
- why existing knowledge/approaches do not settle it;
- the question this paper addresses;
- what kind of contribution is made;
- why the contribution could resolve the stated problem.

Do not expand into a textbook history when that material does not change the paper's research need.

### Methods

For consequential choices, explain:

`what was done -> how -> why this choice -> assumptions/parameters that affect interpretation`

A Methods section should not merely list software, libraries, commands, model names, or analysis labels.

Operational repository details remain in artifact documentation unless scientifically consequential.

### Results

Each major result block should give the reader enough to understand:

- the local question;
- essential setup/comparison;
- what was observed/estimated;
- the uncertainty or evidence needed to judge it;
- the bounded local inference;
- why the next analysis follows, when relevant.

Do not force repeated Methods detail into Results; include only the setup necessary to interpret the evidence.

### Discussion

For important findings, elaborate enough to separate:

- finding;
- interpretation;
- relation to prior evidence or alternatives;
- boundary/limitation;
- implication.

Do not jump from `we observed X` directly to broad field/societal significance without the intermediate scientific meaning.

### Figure callouts and legends

Main text should tell the reader **what to notice and why it matters**.

Legend should tell the reader **what is shown and how to read it**, including definitions/statistics required for interpretation.

Do not make the main text a duplicate legend or make the legend carry the entire scientific explanation.

### Equations and formal models

When a formula is central to the paper, define variables and give enough conceptual interpretation for the intended reader to understand the role of the expression.

For specialist formal work, do not over-explain standard notation. For cross-disciplinary work, lower the assumed baseline.

## Elaboration budget

Use an **importance × unfamiliarity × inferential-dependence** heuristic.

### High elaboration priority

- central new concept;
- mechanism required for headline interpretation;
- unfamiliar cross-disciplinary method;
- consequential analytical choice;
- new metric/quantity whose scale is not intuitive;
- surprising/contradictory result;
- failure boundary that changes the claim;
- abstraction necessary to interpret a main figure;
- assumption on which a major conclusion depends.

### Medium priority

- supporting method choice;
- important but familiar background concept;
- secondary validation;
- non-central interpretation;
- transition between evidence blocks.

### Low priority

- standard field procedure;
- repeated definition;
- implementation detail with no scientific consequence;
- secondary robustness that does not change interpretation;
- obvious figure-reading instruction.

Do not allocate explanation by word-count quotas.

## Audience-switch audit

A paper often has multiple reader baselines.

For each section, ask whether the reader is:

- broad scientist;
- field specialist;
- method specialist;
- reviewer/editor;
- practitioner/clinician;
- data/resource reuser.

The same concept may need a plain-language orientation in the abstract/introduction, a precise operational definition in Methods, and no redefinition in Results.

This is controlled repetition with different functions, not redundancy.

## Analogue-paper calibration for explanation depth

Close analogue papers can help estimate local explanation depth.

When studying them, annotate:

- which concepts are defined locally versus assumed;
- how many reasoning steps separate question from conclusion;
- what is explained in main text versus Methods/SI;
- whether the main text includes brief method rationale;
- how figures are narrated;
- where mechanism/interpretation is expanded;
- what background is considered obvious to the community.

Learn the **depth and function**, not the wording.

Do not infer that an under-explained published paper is good practice merely because it was accepted.

## Reviewer/editor comprehension audit

A reviewer may be technically capable of reconstructing a missing step and still judge the paper as unclear or unconvincing.

For each headline claim ask:

1. Can a domain reviewer recover the evidence-to-claim chain without supplying an unstated premise?
2. Can an editor/non-specialist recover the paper's problem, contribution, and meaning at the appropriate level?
3. Is the method rationale visible enough to judge why the analysis is credible?
4. Does the paper explain why a displayed difference matters, not only that it exists?
5. Are claim-changing boundaries explained where the claim is made?

If the answer is no, classify the issue as **explanatory insufficiency**, not automatically as missing science.

The cheapest repair may be explanation/restructuring rather than new evidence.

## Explanation ledger

For substantial rewrites, maintain a compact ledger when useful:

```text
Concept / inference
- reader baseline:
- centrality:
- current explanation:
- missing element(s): E1/E2/E3/E4/E5/E6
- hidden premise:
- recommended expansion:
- destination: main text / Methods / legend / SI / other
- status: sufficient / under-explained / over-explained / misplaced
```

Do not show the full ledger unless the user wants it.

## Over-explanation guard

Explanatory sufficiency is not a license for repetitive exposition.

Flag over-explanation when:

- a definition is repeated without a new rhetorical function;
- routine specialist knowledge receives textbook treatment;
- the same rationale is restated in Introduction, Results, and Discussion without adaptation;
- Methods contain a tutorial rather than reproducibility-relevant explanation;
- Results repeat extended background before every analysis;
- the manuscript explains code/repository operations instead of scientific abstractions;
- a figure pattern is described exhaustively when the visual already makes it obvious;
- every sentence receives an explanatory parenthesis.

Repair by keeping the **first sufficient explanation** and using later references/brief reminders.

## Final sufficiency test

Before release, select each central idea/result/mechanism/method choice and ask:

> If the intended reader encountered this paper without access to our internal notes/code and without us in the room, could they explain back what this means, why it is here, how the claim follows, and what its important limits are?

If not, identify exactly which explanation element is missing.

Do not solve under-explanation by adding generic filler. Add the **specific missing reasoning**.

## Boundaries

Never use this contract to:

- add unsupported mechanisms, rationales, or implications;
- invent motivations the authors did not have;
- turn Results into a Methods tutorial;
- expose private/internal repository detail merely to appear thorough;
- repeat material already sufficient in a different form;
- lower the technical level so far that scientific precision is lost;
- force one explanation template across disciplines;
- equate longer prose with better prose.

## Research basis

Use these sources as guidance rather than universal templates.

### Current journal/editorial guidance

- Nature Portfolio, *How to write your paper*: warns authors not to assume every reader has the necessary specialist background, recommends defining technical terms/abbreviations where needed, and emphasizes clear direct communication.
- Nature, *Formatting guide*: requires readability across disciplines and explanation of unavoidable jargon.
- Nature, *Editorial criteria and processes*: notes that editors pay special attention to readability and may encourage highly technical authors to use a slightly longer summary paragraph so nonspecialists can understand the background and how the results affect the field.
- Nature Computational Science (2025), *On writing accessible computational science papers*: recommends logical Results order and inclusion of only the methodological detail necessary for readers to understand results, with deeper technical detail moved to Methods.
- Nature Climate Change (2025), *Making the most of the Methods*: states that Methods should explain what was done, how, and why, while brief method descriptions in main text can help readers interpret the approach and results.

### Comprehension and reader-processing evidence

- Gopen, G. D. & Swan, J. A. (1990). *The Science of Scientific Writing*. American Scientist 78, 550–558. Reader-centered organization: context before new information, visible action, topic/stress positions, and sentence connectivity.
- Bullock, O. M. et al. (2019). *Jargon as a barrier to effective science communication: Evidence from metacognition*. Public Understanding of Science 28, 845–853. https://doi.org/10.1177/0963662519865687 — jargon reduced processing fluency in an experiment with 650 participants.
- Shulman, H. C. et al. (2020). *The Effects of Jargon on Processing Fluency, Self-Perceptions, and Scientific Engagement*. Journal of Language and Social Psychology 39, 579–597. https://doi.org/10.1177/0261927X20902177 — jargon disrupted processing fluency even when definitions were supplied.
- Vidal-Abarca, E. et al. (1998). *Levels of comprehension of scientific prose: the role of text variables*. Learning and Instruction 8, 215–233. https://doi.org/10.1016/S0959-4752(97)00020-0 — improving relationships among text ideas and links to reader knowledge supported different levels of comprehension, with problem solving improving when both were present.

The operational lesson is not `explain everything`. It is:

> explanation depth should be matched to what the intended reader must understand to evaluate and reuse the paper's scientific reasoning.
