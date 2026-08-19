# Cross-disciplinary section move atlas

Use this reference when a manuscript needs section-level logic beyond a journal template. These are **move inventories**, not mandatory sequences. Select and order moves according to the paper's argument, study design, discipline, and target venue.

## Contents

- [How to use the atlas](#how-to-use-the-atlas)
- [Abstract](#abstract)
- [Introduction](#introduction)
- [Related work / literature review](#related-work--literature-review)
- [Methods](#methods)
- [Results](#results)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [Title](#title)
- [Discipline and paper-type calibration](#discipline-and-paper-type-calibration)
- [Anti-patterns](#anti-patterns)

## How to use the atlas

1. Identify the paper's dominant contribution type and evidence type.
2. List the reader questions the section must answer.
3. Select the minimum moves needed to answer them.
4. Decide which moves deserve separate paragraphs and which are supporting submoves.
5. Order moves so each creates the reason for the next.
6. Apply the target journal's exact structural constraints only after the logical map works.

A move can recur. For example, a Discussion may cycle through `result -> interpretation -> prior work -> qualification` several times, once for each major finding.

## Abstract

Possible moves:

- establish problem / context
- identify tension, need, or opportunity
- state objective / question
- identify study design / method
- present main result(s)
- present mechanism / explanation
- state conclusion / implication
- state boundary / population / condition
- identify resource availability when central to reuse

### Empirical default

In empirical science, **results are usually the highest-value move**. Do not spend so much abstract space on motivation that the reader cannot tell what was found.

Do not force a complete `Introduction -> Purpose -> Method -> Results -> Conclusion` sequence. Published abstract corpora show frequent omission and reordering of moves across fields.

### Variants

- **formal/theoretical**: problem -> result/theorem -> consequence; method detail may be minimal
- **clinical/quantitative**: objective/question -> design/population -> effect/result with uncertainty -> conclusion/boundary
- **algorithmic/benchmark**: task/bottleneck -> method/resource -> comparative result -> capability/boundary
- **qualitative/social science**: phenomenon/problem -> framing/question -> data/approach -> interpretive finding -> implication
- **review/synthesis**: scope/problem -> synthesis approach or organizing lens -> major synthesis -> implications/gaps

## Introduction

Core move families:

### A. Establish the research territory

- define the phenomenon/problem only if readers need it
- establish importance, practical consequence, theoretical significance, or unresolved uncertainty
- summarize what is already known at the level needed for this paper

### B. Create a research need

A legitimate research need is broader than a generic literature `gap`. Common forms:

- unanswered question
- contradiction between findings
- unexplained observation
- weak or indirect evidence
- missing mechanism
- measurement limitation
- methodological bottleneck
- unrealistic assumption
- missing population / condition / scale
- lack of external validation
- absent benchmark / standard / resource
- theory-data mismatch
- emerging opportunity enabled by new data/instrumentation
- replication or robustness need

State the need faithfully. Do not manufacture scarcity with `few studies` when the actual contribution is a better explanation, measurement, comparison, or test.

### C. Position prior work

- synthesize approaches by idea, assumption, mechanism, evidence class, or trade-off
- show what each line of work makes possible
- identify the exact point at which the present question remains live
- distinguish limitation of evidence from limitation of method

Prior work can be revisited later in the Introduction if the argument has multiple tensions. A single funnel is not mandatory.

### D. Occupy the research space

- state the question / hypothesis / objective
- state the contribution or study response
- explain the key design choice or conceptual move when needed
- preview evidence classes, not every result
- state scope/boundary when misunderstanding is likely

### Introduction variants

- **problem-led**: consequence -> current knowledge -> unresolved cause/need -> study
- **theory-led**: theoretical tension -> competing accounts -> discriminating test -> study
- **method-led**: capability need -> current technical trade-off -> design principle -> method
- **observation-led**: surprising phenomenon -> why existing explanations are insufficient -> analysis/test
- **resource/benchmark-led**: fragmented practice -> missing common resource/standard -> design requirements -> resource
- **replication/validation-led**: influential prior claim -> uncertainty/generalizability concern -> replication/extension design

## Related work / literature review

The section should build a **map of the intellectual decision space**, not a bibliography tour.

Possible organizing dimensions:

- competing explanations
- method families
- assumptions
- datasets/populations/settings
- historical development when chronology changes interpretation
- evidence strength
- unresolved trade-offs
- points of agreement and disagreement

Paragraph moves:

1. topic claim about a body of work
2. synthesis of representative evidence
3. comparison or distinction
4. consequence for the present study

Use author-by-author chronology only when who-did-what-first is itself analytically important.

## Methods

Methods do more than report procedure. Their rhetorical job is to demonstrate **rigour, credibility, interpretability, and reproducibility**.

Possible moves:

- study/design overview
- setting / population / material / dataset definition
- inclusion/exclusion / sampling / recruitment
- variables / constructs / outcomes / labels
- apparatus / materials / preprocessing
- procedure / intervention / experimental sequence
- model / algorithm / mathematical formulation
- parameter / hyperparameter choices
- analysis / statistical model / inference procedure
- controls / baselines / validation
- sensitivity / robustness / uncertainty procedure
- ethics / registration / consent
- reproducibility / code / data / software environment

### Rationale submoves

Explain *why* a methodological choice was made when alternatives would materially change interpretation. Do not justify every routine action.

Useful rationale targets:

- sampling strategy
- outcome choice
- exclusion rule
- model class
- baseline
- threshold
- preprocessing transformation
- statistical test
- validation design

### Algorithmic pipeline subtype

For a computational pipeline, use:

`problem representation -> components -> information/data flow -> objective/training/inference -> complexity/resources -> implementation -> validation`

A module's `motivation -> design -> consequence` can be useful, but technical advantages should be supported by analysis or experiments rather than asserted inside Methods.

## Results

The obligatory core is **evidence reporting**. Commentary, interpretation, and methodological reminders vary by field and journal.

A robust result block often contains:

1. **question / local purpose** — what is being tested or established?
2. **setup reminder** — only information needed to read the result
3. **observation / estimate** — what happened?
4. **evidence** — numbers, uncertainty, comparison, figure/table, qualitative material, proof step
5. **local inference** — the narrow conclusion justified by this result
6. **bridge** — why the next analysis follows

Not every paragraph needs all six.

### Common sequencing strategies

- causal/mechanistic ladder
- baseline -> primary comparison -> ablation/diagnosis -> robustness/generalization
- descriptive -> inferential -> explanatory
- simple condition -> complex condition
- discovery -> validation -> external validation
- theorem/lemma -> main result -> corollary/application
- theme/finding 1 -> theme/finding 2 -> integrative pattern

### Commentary boundary

Some fields integrate interpretation into Results; others reserve most interpretation for Discussion. Match the target discipline and journal. Never force `conclusion-first` if the field expects neutral reporting before interpretation.

## Discussion

Discussion is usually **recursive**, not a single one-way widening paragraph sequence.

For each major finding, select from:

- restate the finding at the level needed for interpretation
- interpret mechanism / meaning
- compare with prior studies or theory
- explain agreement/disagreement
- consider alternative explanations
- state practical/theoretical implication
- qualify by design, uncertainty, population, model, or measurement

Then add paper-level moves as needed:

- integrate findings into one answer
- distinguish what changed from what remains uncertain
- limitations with consequences for interpretation
- strengths that affect confidence or transferability
- generalizability / external validity
- future work that follows from a real unresolved question
- clinical/policy/design implications when supported

Do not make a separate generic `limitations` paragraph the only place where boundaries appear. Put important qualifications near the claims they constrain, then summarize major limitations globally if the genre expects it.

## Conclusion

A conclusion can contain:

- answer to the central question
- decisive evidence basis
- contribution relative to prior knowledge
- bounded implication
- unresolved issue / next step when useful

Do not mechanically repeat the abstract. The conclusion should represent what remains defensible after the Discussion's qualifications.

Some journals/paper types do not need a separate Conclusion; a Discussion ending may perform the same move.

## Title

Title form varies strongly by discipline and genre. Choose based on what readers search for and what the paper can truthfully claim.

Common forms:

- descriptive noun phrase
- method/resource + target/problem
- declarative finding
- question title
- two-part `topic: specification` title
- population/design/outcome title in clinical or social science contexts

Check:

- core searchable entities are present
- the title distinguishes the paper from neighboring work
- causal wording matches causal evidence
- evaluative adjectives are earned
- abbreviations are recognizable enough for the target audience
- title syntax matches the target journal/content type

Do not impose a universal title formula; corpus studies show strong disciplinary variation.

## Discipline and paper-type calibration

### Experimental natural science

Often favors compact background, evidence-heavy Results, and phrasally dense technical prose. Methods credibility depends on materials, conditions, controls, replicates, uncertainty, and instrumentation.

### Engineering / computer science

Conference and journal papers may foreground task definition, system design, benchmark protocol, baselines, ablations, runtime/complexity, and failure analysis. Related work may be a separate section. Do not assume a biomedical IMRaD rhythm.

### Clinical / epidemiological

Population, design, outcomes, effect sizes, uncertainty, confounding, adverse outcomes, registration/reporting standards, and generalizability drive structure. Avoid translating statistical association into treatment recommendation without the needed evidence.

### Social science / psychology

Theory, constructs, competing accounts, measurement validity, sampling, and interpretation may require more clausal reasoning and literature integration than a short technical funnel.

### Qualitative research

Researcher positioning, sampling rationale, analytic process, theme/evidence presentation, interpretation, and reflexivity may be central. Do not force quantitative result syntax.

### Humanities

Argument and source architecture may replace IMRaD entirely. Sections can be conceptual, chronological, textual, historiographic, or case-based. A `gap -> method -> result` template may be actively harmful.

### Theory / mathematics

Problem definition, assumptions, formal statements, proof architecture, counterexamples, and consequences determine the paper. An abstract or introduction may move rapidly from context to theorem/result.

### Review / perspective

The contribution is synthesis, framework, interpretation, or agenda-setting rather than a new experiment. Organize around concepts/questions, not Results-shaped prose.

## Anti-patterns

Never treat the following as universal rules:

- every Introduction must have four paragraphs
- every abstract must contain all five IMRaD-like moves
- every Results paragraph must begin with the conclusion
- every paragraph must perform only one rhetorical function
- every Methods section is a computational pipeline
- every Discussion should postpone all interpretation until the end
- every title should be `system + capability + application`
- shorter sentences are always clearer
- more transitions automatically create better flow
- journal prestige determines how strongly a claim should be written

Use empirical patterns as priors, then let the paper's evidence and disciplinary conventions decide.