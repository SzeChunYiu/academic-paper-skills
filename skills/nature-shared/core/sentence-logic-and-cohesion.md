# Sentence logic and cohesion

> Shared contract for making academic prose logically connected from one sentence to the next while preserving disciplinary variation and author voice. Last reviewed: 2026-08-25.

## Purpose

A paragraph can contain individually grammatical sentences and still be difficult to follow because the reader cannot recover **why sentence B comes after sentence A**.

This contract treats sentence flow as a reasoning problem first, a cohesion problem second, and a style problem last.

Use it for:

- choppy or list-like academic prose;
- paragraphs that read like separate AI-generated mini-summaries;
- abrupt evidence-to-interpretation jumps;
- weak handoffs between analyses;
- excessive connective words without real logic;
- unclear pronouns/demonstratives;
- repeated topic resets;
- buried subjects/verbs or misplaced emphasis.

## Research basis

Reader-expectation work in scientific writing emphasizes several useful tendencies in English academic prose:

- readers use early sentence material to establish context/topic;
- long interruptions between a grammatical subject and its verb increase processing burden;
- sentence-final/stress positions naturally receive emphasis and are often useful for important new information;
- backward linkage to material already active in the discourse helps readers connect sentences;
- given-before-new organization can improve continuity, but it is a reader-management principle rather than a mandatory template.

A 2026 mixed-methods study of explicit coherence instruction reported improved writing coherence and found stronger writers showed better **identity-chain development**. Recent research-article cohesion studies also show that cohesion patterns vary by rhetorical section and discipline, so no single connective density or thematic-progression pattern should be enforced universally.

## Core hierarchy

Repair in this order:

```text
proposition
-> dependency/relation
-> topic/context
-> entity/identity chain
-> information progression
-> emphasis/stress
-> syntax
-> connective
-> cadence
```

Do not begin with `add however/furthermore`.

## Sentence dependency contract

For every sentence after the first in a difficult paragraph, write:

```text
inherits X
-> relation R
-> adds Y
-> enables Z
```

### Inherits

What does the sentence take as active from previous context?

Possible inheritance:

- same entity/object;
- previous result;
- contrast set;
- open question;
- assumption;
- method condition;
- causal candidate;
- quantity/estimate;
- limitation.

### Relation

Why is this sentence here?

Common relations:

- evidence/support;
- explanation/mechanism;
- cause;
- consequence;
- comparison;
- contrast;
- concession;
- specification;
- example;
- qualification/boundary;
- inference;
- alternative explanation;
- result -> next question;
- problem -> response;
- method choice -> interpretation.

### Adds

What genuinely new information enters the reader's model?

If it merely restates the prior sentence, compress/remove it.

### Enables

What can the reader now understand, test, compare, or ask next?

A strong sentence often creates the reason for the next one.

## Orphan-sentence test

A sentence is suspicious when:

- it inherits no identifiable concept/question;
- its relation to adjacent sentences cannot be named;
- it could be moved almost anywhere in the section without changing the logic;
- the only apparent connection is `Moreover`, `Furthermore`, `Additionally`, or `Notably`;
- it summarizes generically rather than advancing the argument.

Repair by moving, merging, deleting, or adding the missing conceptual bridge.

## Given-new chain

Useful default:

```text
S1: A -> B
S2: B -> C
S3: C -> D
```

The important new material near the end of one sentence becomes available context near the start of the next.

But do not enforce this mechanically.

Legitimate alternatives include:

### Constant topic

```text
A -> B
A -> C
A -> D
```

Useful when several properties of the same object are being compared.

### Contrast

```text
A -> X
B -> Y
comparison -> implication
```

### Question-answer

```text
unresolved question
-> test/evidence
-> answer
```

### Claim-evidence-boundary

```text
claim
-> support
-> qualification
```

### Derived themes

```text
general A
-> A1
-> A2
-> synthesis
```

### Procedure/sequence

Chronology can dominate when order is scientifically meaningful.

The reader should feel a **controlled progression**, not a sentence template.

## Identity-chain audit

Track central entities across adjacent sentences.

Use:

- exact canonical technical term;
- stable abbreviation;
- unambiguous pronoun;
- precise demonstrative noun phrase (`this reduction`, `this discrepancy`, `these estimates`);
- clearly signaled subtype/supertype relationship.

### Avoid synonym drift

If `model`, `framework`, `system`, `method`, and `approach` are not exactly interchangeable, do not rotate them merely to sound varied.

Precise repetition can improve coherence.

### Demonstrative+noun preference

When `this` could refer to multiple ideas, name the referent.

Weak:

`This explains the discrepancy.`

Stronger:

`This sampling imbalance explains the discrepancy.`

Do not expand when the pronoun is already unambiguous.

## Topic-position audit

Ask what story the sentence is telling.

Whenever possible, place a recognizable topic/context early enough that readers know how to interpret what follows.

Common failures:

- opening with a long abstract nominalization;
- switching to a new subject without a bridge;
- starting every sentence with `This study` or `We` even when the discourse topic differs;
- burying the actual scientific object behind meta-discourse.

Topic continuity matters more than surface variation.

## Subject-verb distance audit

Long subject-to-verb interruptions can increase cognitive load.

Flag sentences where:

- the main subject is followed by several embedded prepositional/relative clauses before the main verb;
- the reader must retain a long noun phrase before learning the action;
- important content is trapped inside an interruption that reads as secondary.

Repair options:

- move background/qualification after the main clause;
- split the sentence if the qualification deserves its own proposition;
- convert a noun-heavy construction into an explicit clause;
- keep the subject and main scientific action closer.

Do not force short sentences when a complex relationship is clearer in one well-structured sentence.

## Stress/emphasis audit

Sentence endings naturally attract emphasis.

Ask:

- what should the reader remember from this sentence?
- is that material located in a natural emphasis position?
- did a parenthetical, citation, method detail, or secondary qualifier accidentally occupy the final stress position?

Useful pattern:

```text
known context -> relation -> important new result
```

Then use that new result as the next sentence's context if appropriate.

Do not move every number to the sentence end mechanically.

## Evidence-to-interpretation handoff

AI prose often compresses:

`observation -> interpretation`

without exposing the warrant.

For consequential inference, use:

```text
observation
-> comparison/expected alternative
-> inference
-> boundary
```

or another structure that makes the warrant visible.

Use `explanatory-sufficiency.md` when the missing link is conceptual rather than merely linguistic.

## Analysis-to-analysis handoff

A Results section should not feel like a list of experiments.

Before analysis B, state or make recoverable **why A makes B necessary**.

Common dependencies:

- A establishes phenomenon -> B asks mechanism;
- A shows benchmark gain -> B tests generalization;
- A shows heterogeneity -> B investigates moderator/subgroup;
- A suggests mechanism -> B discriminates alternative mechanism;
- A proves theorem -> B tests practical consequence;
- A finds qualitative theme -> B explores negative/contrasting case;
- A exposes failure -> B tests whether a modification repairs it.

This relation may need only a phrase/sentence, but it must exist in the reader's model.

## Connective gate

A connective labels a relation; it does not create one.

Before adding `however`, `therefore`, `moreover`, `in contrast`, `consequently`, or similar markers:

1. name the underlying relation;
2. verify both propositions actually support that relation;
3. add the connective only if the relation would otherwise be difficult to recover.

### Remove connective stuffing

If several consecutive sentences start with transition adverbs, check whether the paragraph's dependency structure is weak.

Lexical/identity continuity can often provide smoother connection than repeated adverbs.

## Paragraph dependency graph

For difficult paragraphs, write a minimal graph before rewriting prose:

```text
S1 establish A
└─ S2 quantify A under B
   ├─ S3 contrast with expected C
   └─ S4 infer D, bounded by E
      └─ S5 motivate next test F
```

The graph can branch. Sentence order should follow reader dependency, not original drafting chronology.

## Cross-paragraph handoff

The same principle applies across paragraphs.

At paragraph end, identify one of:

- bounded conclusion;
- unresolved question;
- contrast requiring next paragraph;
- new scale/population/regime;
- mechanism question;
- validation need;
- implication.

The next paragraph should pick up that handoff or clearly signal a justified section shift.

## Local coherence versus global logic

A paragraph can be cohesive yet globally misplaced.

After local sentence repair, ask:

- does this paragraph answer the section's current reader question?
- does its nucleus belong here?
- is the whole paragraph a digression?

Do not use smooth transitions to hide a wrong argument order.

## Human/natural tone interaction

Logical continuity helps prose feel human because sentences react to each other rather than arriving as independent polished outputs.

But natural tone also requires:

- locally calibrated stance;
- meaningful syntactic variation;
- authorial agency when decisions/interpretations matter;
- precise technical vocabulary;
- no generic prestige filler.

Use `natural-scholarly-prose.md` and `author-voice-profile.md` after logic is correct.

## Section-specific caution

Cohesion strategies vary by section.

### Introduction

Topic chains often follow field/problem/need/contribution progression.

### Methods

Procedure/object continuity and chronological/dependency relations can dominate.

### Results

Question/evidence/inference chains dominate; figure calls should attach to the evidence sentence they support.

### Discussion

Finding/interpretation/prior evidence/alternative/boundary chains are common.

Do not impose one connective or pronoun pattern across all sections.

## Sentence-flow QA checklist

For each difficult paragraph:

1. Can every non-initial sentence name what it inherits?
2. Can every adjacent pair name a real relation?
3. Are central entities stable across identity chains?
4. Does new information become usable context when appropriate?
5. Are topic shifts signaled?
6. Is the main subject/action unnecessarily separated?
7. Does important new information receive appropriate emphasis?
8. Are evidence-to-inference warrants visible?
9. Does each analysis create a reason for the next?
10. Are connectives labeling real logic rather than decorating jumps?
11. Does the paragraph still serve the section's global reader question?

## Non-negotiable boundary

Never improve apparent flow by inventing a causal or logical relation that the evidence does not support.

If two sentences do not logically connect because the science is missing, expose the gap.