# Article architecture

Use this reference to design the **logic of a whole paper**. For detailed section move options, use `section-move-atlas.md`. For empirical justification, use `cross-disciplinary-writing-evidence.md`.

## Contents

- [Architecture is an argument, not a section template](#architecture-is-an-argument-not-a-section-template)
- [The argument spine](#the-argument-spine)
- [Contribution branches](#contribution-branches)
- [Evidence architecture](#evidence-architecture)
- [Section handoffs](#section-handoffs)
- [Common whole-paper architectures](#common-whole-paper-architectures)
- [Paragraph architecture](#paragraph-architecture)
- [Claim architecture](#claim-architecture)
- [Compression and emphasis](#compression-and-emphasis)
- [Architecture audit](#architecture-audit)

## Architecture is an argument, not a section template

A strong paper allows a reader to reconstruct:

`why this question -> what this paper answers -> why the evidence warrants that answer -> where the answer stops -> why the bounded answer matters`

That chain can be realized through IMRaD, combined Results/Discussion, theorem-proof sections, case-based chapters, conceptual sections, or another field-appropriate structure.

Do not judge architecture by whether the headings resemble a familiar journal. Judge whether the evidence and reasoning answer the paper's live questions in a recoverable order.

## The argument spine

Write five statements before designing sections:

1. **Research tension/question** — the live problem, contradiction, uncertainty, bottleneck, missing test, unexplained phenomenon, or opportunity.
2. **Answer/contribution** — the narrowest statement that captures what the paper establishes or provides.
3. **Decisive warrant** — the evidence/reasoning without which the answer would not be convincing.
4. **Boundary** — population, system, assumptions, scale, conditions, uncertainty, alternative interpretation, or scope limit.
5. **Meaning** — what changes in knowledge, capability, practice, theory, or future investigation.

The paper should make the dependency between these five objects visible.

## Contribution branches

Many papers have more than one contribution. Do not flatten them into a grandiose single claim.

Represent them as:

```text
central question
  -> dominant answer
      -> evidence chain A
      -> evidence chain B
  -> secondary contribution 1
      -> supporting evidence
  -> secondary contribution 2
      -> supporting evidence
  -> integrated meaning + boundaries
```

A secondary contribution earns main-text space when it changes interpretation, credibility, reuse, generalizability, or practical value. Otherwise move it to a subordinate section or supplement.

## Evidence architecture

Results/analysis order should follow a **reasoning dependency**, not simply the order experiments were performed.

Useful dependencies include:

- establish measurement validity -> report main effect -> test mechanism;
- baseline -> primary comparison -> ablation/diagnosis -> robustness/generalization;
- discovery -> independent validation -> external validation;
- descriptive pattern -> inferential test -> explanatory analysis;
- contradiction -> discriminating experiment -> revised explanation;
- method capability -> benchmark -> stress test -> failure analysis;
- theorem/lemma -> main theorem -> corollary/application;
- theme -> contrasting theme -> negative case -> integrated interpretation;
- archival/source claim -> counterevidence -> contextual reconstruction -> argument.

For every evidence block ask: **Why does the reader need this now? What earlier result made this the next useful question?**

## Section handoffs

A section ending should change the reader's question.

### Introduction handoff

Reader should know:

- the live question/need;
- why existing knowledge does not settle it;
- the study's response and scope;
- what evidence would count as an answer.

The next question is usually: **How was that answer obtained or tested?**

### Methods handoff

Reader should know enough to evaluate how evidence was generated and what inferential assumptions matter.

The next question is: **What did the evidence show?**

### Results/analysis handoff

Reader should know the empirical/formal/source-based answer and major qualifications.

The next question is: **How should that answer be understood relative to alternatives and prior knowledge?**

### Discussion handoff

Reader should know what the findings mean, what they do not establish, and what remains unresolved.

The final question is: **What is the most durable bounded contribution?**

These handoffs are conceptual. They do not require those exact section names.

## Common whole-paper architectures

### Mechanism/discovery

`phenomenon -> unresolved explanation -> discriminating evidence -> mechanism -> boundary -> implication`

### Method/algorithm

`capability need -> current trade-off/bottleneck -> design principle -> method -> fair evaluation -> diagnostic/ablation -> generalization/failure modes -> implication`

### Resource/benchmark

`fragmented/inadequate evaluation -> design requirements -> resource construction -> validation/coverage -> benchmark findings -> reuse/governance/boundaries`

### Clinical/epidemiological

`clinical/population question -> evidence/design limitation -> study design -> effect/association with uncertainty -> sensitivity/subgroup/adverse outcomes -> interpretation/generalizability -> implication`

### Theory

`formal problem -> assumptions/definitions -> main result -> proof architecture -> consequences/counterexamples -> limitations/applicability`

### Qualitative

`phenomenon/context -> research question/lens -> sampling/data/analytic process -> themes/findings with evidence -> contrasts/negative cases -> interpretation/reflexivity -> transferability/boundaries`

### Humanities/historical

`interpretive/historiographic problem -> source/conceptual framing -> evidence sequence/cases -> counterreading/counterevidence -> synthesis -> bounded argument`

### Review/synthesis

`field problem -> organizing question/lens -> evidence landscape -> synthesis/tensions -> framework/taxonomy -> gaps/agenda -> bounded conclusion`

### Replication/validation

`important prior claim -> uncertainty about robustness/generalizability -> replication/extension design -> comparison to original expectation -> discrepancy/consistency analysis -> consequences for claim scope`

### Negative/null result

`important expected relationship -> adequate test/power/sensitivity -> null/negative evidence -> alternative explanations/limits -> revised boundary of the original claim`

No architecture is automatically superior. Choose the one that makes evidentiary dependency easiest to follow.

## Paragraph architecture

A paragraph is a local argument unit with one **nucleus** and any number of necessary supporting satellites.

Example structures:

```text
nucleus claim
  -> evidence
  -> interpretation
  -> qualification
```

```text
problem/tension nucleus
  -> example/evidence
  -> consequence
  -> bridge to solution
```

```text
prior-work synthesis nucleus
  -> representative evidence
  -> contrast
  -> consequence for present study
```

The first sentence need not always state the conclusion. It should orient the reader efficiently to the nucleus. Observation-first, question-first, context-first, or contrast-first openings may be better depending on genre and information flow.

## Claim architecture

For every major claim maintain a traceable tuple:

`claim -> evidence/reasoning -> uncertainty -> boundary -> competing interpretation`

Not every sentence states all five, but the manuscript should make them recoverable.

Watch for **claim drift**:

- Results: association
- Discussion: mechanism
- Abstract: causal effect
- Title: universal capability

If claim strength grows as text becomes shorter, fix the compression rather than the data.

## Compression and emphasis

Main text is not the complete lab record. Allocate space by argumentative importance:

- more space for the decisive warrant, unexpected qualification, or reasoning readers need to trust;
- less space for routine procedures, repeated statistics, and evidence already legible in a display;
- enough context to interpret each display without retelling every cell;
- important limitations near the claims they constrain, not hidden only in a final limitations paragraph.

Use `../../../nature-shared/core/main-text-discipline.md` for detailed evidence allocation.

## Architecture audit

Before polishing, answer:

1. Can the whole paper be reduced to one dominant question and bounded answer?
2. Does every main section have a reader question?
3. Does every major evidence block answer a question created earlier?
4. Does the next block follow because of what was learned in the previous one?
5. Are major alternatives/qualifications placed before broad generalization?
6. Can each paragraph's nucleus be stated in one line?
7. Do those nucleus lines reconstruct the section argument?
8. Does each major claim have visible warrant and boundary?
9. Are secondary contributions subordinate to the dominant spine rather than competing with it?
10. If headings were removed, would the logical progression still be recoverable?

Fix failed architecture tests before sentence polishing.