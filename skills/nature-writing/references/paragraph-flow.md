# Paragraph and sentence flow

Use this reference when prose is logically correct but feels choppy, dense, repetitive, hard to follow, over-transitioned, generic, or disconnected from the section argument.

For a broader natural-scholarly-expression audit, also load `../../nature-shared/core/natural-scholarly-prose.md`.

## Contents

- [Core model](#core-model)
- [Paragraph nucleus and satellites](#paragraph-nucleus-and-satellites)
- [Sentence dependency graph](#sentence-dependency-graph)
- [Sentence relations](#sentence-relations)
- [The why-this-sentence-now test](#the-why-this-sentence-now-test)
- [Given-to-new progression](#given-to-new-progression)
- [Lexical and referential chains](#lexical-and-referential-chains)
- [Topic and emphasis](#topic-and-emphasis)
- [Paragraph-to-paragraph handoffs](#paragraph-to-paragraph-handoffs)
- [Transitions](#transitions)
- [Cadence without artificial variation](#cadence-without-artificial-variation)
- [Reverse outlining](#reverse-outlining)
- [Repair workflow](#repair-workflow)
- [Cross-disciplinary caution](#cross-disciplinary-caution)

## Core model

Flow is not the presence of words such as `however`, `therefore`, or `moreover`.

A reader experiences flow when they can recover:

`what this unit is about -> how the next statement relates -> what new information changed -> why the next unit follows`

Diagnose flow at five levels:

1. whole-section argument;
2. paragraph nuclei;
3. sentence dependency/relations;
4. information progression;
5. lexical/reference continuity.

Do not fix a level-1 structural problem by adding level-3 transitions.

Research on academic cohesion shows that local, global, and text-level cohesion differ across rhetorical sections and disciplines. Therefore this file supplies **diagnostic operations**, not a target number of connectives, lexical overlaps, or sentence shapes.

## Paragraph nucleus and satellites

Each paragraph has one **nucleus**: the claim, question, result, contrast, problem, interpretive point, or reader task that makes the paragraph necessary.

Supporting satellites can include:

- evidence;
- mechanism/explanation;
- example;
- comparison;
- qualification;
- counterargument;
- implication;
- methodological context;
- bridge.

A paragraph is coherent when the satellites clearly serve the nucleus.

### Split test

Split when:

- two propositions could each be the main reason the paragraph exists;
- evidence begins supporting a different claim;
- the paragraph switches time scale/population/system without an integrating point;
- a qualification grows into an independent argument;
- the reader must remember too many unresolved relations.

Do not split merely because the paragraph contains both evidence and interpretation; that combination is often exactly what makes it coherent.

### Paragraph choreography

Before prose editing, write:

`nucleus -> support/explanation -> qualification/alternative if needed -> local inference -> next-reader question`

Not every paragraph needs every element. The point is to know why each element exists.

## Sentence dependency graph

Before revising a difficult paragraph, strip it down to proposition-level dependencies.

Example:

```text
S1 establishes phenomenon A
S2 restricts A to condition B
S3 explains why B changes interpretation C
S4 tests C against alternative D
S5 concludes E within boundary B
```

Then ask whether the prose order exposes that graph.

A grammatically correct order can still be rhetorically wrong. If S4 is necessary to trust S3, placing it after an unrelated implication forces the reader to hold unresolved doubt.

### Dependency edge types

Useful edges include:

- `supports`;
- `explains`;
- `qualifies`;
- `contrasts-with`;
- `specifies`;
- `tests-alternative-to`;
- `motivates`;
- `follows-from`;
- `defines-boundary-of`;
- `creates-question-for`.

If two adjacent sentences have no defensible edge, either reorder them or supply the missing reasoning step.

## Sentence relations

Label the relation between adjacent sentences before rewriting:

- evidence/support;
- explanation/cause;
- consequence;
- contrast;
- concession;
- specification;
- example;
- sequence;
- comparison;
- inference;
- qualification;
- bridge/new question.

If no relation can be named, the sequence may be accidental.

If the relation is important and not inferable, make it explicit through syntax or a connective. If the relation is obvious, an extra transition may add clutter.

### Relation completion test

Complete:

`Sentence B exists here because Sentence A ______.`

A useful completion is more informative than `comes before it`.

## The why-this-sentence-now test

For every sentence after the first, write four fields:

- **inherits** — which active concept/result/question/condition from prior context does it pick up?
- **relation** — what rhetorical relation does it perform?
- **adds** — what new proposition becomes available?
- **enables** — why does that proposition make the next step possible?

Compact form:

`inherits X -> relation R -> adds Y -> enables Z`

This catches a common source of machine-like prose: every sentence is locally polished, but each behaves like an independent mini-summary rather than a dependent step in reasoning.

### Orphan-sentence test

A sentence is suspicious when:

- it could be moved almost anywhere in the paragraph without changing meaning;
- it repeats the paragraph topic without advancing it;
- it introduces a broad implication before the evidence chain is closed;
- its only connection is a generic additive connective;
- it changes topic with no inherited entity or explicit reset.

Not every independent sentence is wrong, but every one should have a reason for its position.

## Given-to-new progression

A useful default is to connect new sentences to information already active in the reader's mind, then advance to the new point.

Example logic:

```text
Sentence 1: A -> B
Sentence 2: B -> C
Sentence 3: C -> D
```

This is a **progression principle**, not a command that every sentence start with repeated words.

### Diagnose broken progression

Ask:

- What noun/concept is active at the end of the previous sentence?
- What does the next sentence assume is active?
- Did the prose jump to a new entity before establishing the relation?
- Does a pronoun refer to the intended entity?
- Is important context delayed until after the reader needs it?

### Useful progression patterns

- **linear**: A -> B, B -> C, C -> D;
- **constant topic**: A -> B, A -> C, A -> D;
- **derived themes**: general A -> A1, A2, A3;
- **contrast pair**: A -> property X; B -> contrasting property Y;
- **question-answer**: Q -> evidence -> answer;
- **claim-evidence-boundary**: A -> B -> bounded A'.

Choose the progression that matches the reasoning. Do not enforce old-before-new when a deliberate topic reset, parallel comparison, or formal proof structure calls for another pattern.

## Lexical and referential chains

Keep core entities trackable across sentences and paragraphs.

A lexical/identity chain can include:

- canonical term -> exact repeated term;
- full name -> stable abbreviation;
- category -> clearly named subtype;
- phenomenon -> same phenomenon with a controlled descriptor;
- explicit noun -> unambiguous pronoun;
- result -> precise demonstrative phrase (`this increase`, `this discrepancy`).

Recent coherence research suggests that stronger writers develop better **identity chains**, not merely more cohesive markers.

### Repeat technical terms on purpose

Avoid unnecessary synonym rotation for central technical concepts. In literary prose, repetition may feel inelegant; in research logic, changing `model`, `framework`, `system`, and `approach` as if they are interchangeable can create ambiguity.

If the referent is the same and the technical term is conventional, exact repetition can be the more natural scholarly choice.

### Demonstrative test

Pronouns and demonstratives (`this`, `these`, `it`, `they`, `such`) need recoverable referents. Replace vague `this` with `this increase`, `this assumption`, or `this discrepancy` when several candidates exist.

## Topic and emphasis

A sentence often becomes hard to read because the reader does not know what to treat as the topic or where the main new information sits.

Check:

- Does the opening connect to the current topic/context?
- Is the main new claim buried inside a subordinate clause?
- Is a long abstract subject delaying the verb and relation?
- Does the sentence end on information that deserves emphasis, or on routine detail?
- Is the scientific actor/action visible, or hidden inside nominalizations?

Do not mechanically move every important word to the end. Use information placement to make the rhetorical hierarchy visible.

### Subject-action repair

When a sentence feels abstract, recover:

`who/what -> does/is related to what -> under what condition -> with what evidence/status`

Then decide whether a more compact nominal form is actually helpful.

## Paragraph-to-paragraph handoffs

A strong paragraph ending either:

- completes a local inference;
- reveals a limitation/tension;
- creates the next question;
- names the object examined next.

The next paragraph should pick up that handoff directly or deliberately reset the topic with enough orientation.

### Chain-link test

Write only:

```text
P1 nucleus -> P1 consequence/question
P2 nucleus -> P2 consequence/question
P3 nucleus -> ...
```

If `P1 consequence/question` does not make `P2 nucleus` feel useful, reconsider order or add the missing reasoning step.

## Transitions

Transitions encode relations; they do not create them.

### Use when needed

- `however` / `by contrast`: real opposition or exception;
- `therefore` / `thus`: warranted inference/consequence;
- `for example`: instance of a prior general statement;
- `specifically`: narrower specification;
- `in addition`: genuinely parallel evidence;
- `despite` / `although`: concession that affects interpretation.

### Common misuse

- adding `moreover` between unrelated ideas;
- using `therefore` when only chronology is shown;
- starting every paragraph with an adverbial connective;
- using `however` to introduce novelty rather than contrast;
- repeating a connective because a target corpus uses it frequently;
- using a transition to disguise a topic jump.

If removing a transition makes the argument collapse, check whether the underlying relation is sufficiently stated.

### Do not optimize connector density

More transitions are not more academic. Empirical work shows cohesion features differ by section and discipline, and some L2 corpora overuse linking adverbials. Use the relation the paragraph needs.

## Cadence without artificial variation

Natural scholarly rhythm emerges because different propositions perform different jobs.

Use syntax accordingly:

- direct clause for a decisive local result;
- subordinate clause for a real condition/qualification;
- balanced parallel clauses for a comparison;
- chronological construction for procedure;
- longer controlled sentence when several relations genuinely belong together;
- short sentence when a conclusion needs isolated emphasis and the field/section tolerates it.

Do **not** randomize sentence lengths or punctuation to look human.

### Repetition audit

Flag three or more consecutive sentences with nearly identical structure only when their functions differ. If they present genuinely parallel evidence, parallel syntax may be the clearest choice.

### Read-aloud audit

After logic is fixed, read the paragraph continuously and listen for:

- repeated sentence openings;
- identical clause rhythms;
- buried verbs;
- unnatural pauses caused by noun stacks;
- repeated generic paragraph closings;
- abrupt sentence boundaries that split one logical relation.

## Reverse outlining

For a section-level flow check:

1. State the section's reader question.
2. Write each paragraph nucleus in one sentence.
3. List the evidence/reasoning attached to each nucleus.
4. Write the handoff question/consequence after each paragraph.
5. Check `evidence -> nucleus`.
6. Check `nucleus -> section answer`.
7. Check `handoff -> next nucleus`.
8. For difficult paragraphs, add the sentence dependency graph.

A clean sequence of topic sentences is not enough if the evidence does not warrant them.

## Repair workflow

Repair in this order:

### 1. Structural

- remove paragraphs that do not serve the section question;
- reorder evidence to reflect reasoning dependencies;
- split competing nuclei;
- merge tiny paragraphs that are really satellites of the same nucleus.

### 2. Proposition/dependency

- strip ornate wording and state each proposition plainly;
- map why each sentence exists now;
- move orphan sentences or add missing conceptual bridges.

### 3. Relational

- state missing causal/contrast/inference relations;
- move qualifications next to the claims they bound;
- create explicit handoffs between evidence blocks.

### 4. Information flow

- restore given-to-new continuity where appropriate;
- choose a different progression pattern when reasoning requires it;
- stabilize terminology/identity chains;
- resolve vague pronouns;
- put definitions before dependent reasoning.

### 5. Sentence realization

- reduce overloaded noun stacks;
- break genuinely multi-claim sentences;
- combine repetitive short sentences when one relation is clearer in a single sentence;
- move the main claim out of a buried subordinate clause;
- choose active/passive based on what should be foregrounded.

### 6. Stance

- distinguish observed, estimated, inferred, associated, causal, simulated, proved, and hypothesized claims;
- adjust local hedge/booster strength from evidence.

### 7. Connectives

Only now add or remove explicit transitions.

### 8. Cadence and author voice

Load `../../nature-shared/core/natural-scholarly-prose.md` and `../../nature-shared/core/author-voice-profile.md` when needed. Remove mechanical repetition while preserving terminology and a recognizable authorial rhythm.

The goal is not prose that feels artificially smooth. The goal is prose whose reasoning can be reconstructed with minimal reader backtracking.

## Cross-disciplinary caution

Do not turn any one cohesion pattern into a universal house style.

Research shows:

- local/global/text cohesion varies by rhetorical section;
- Discussion cohesion differs across applied linguistics, chemistry, and economics;
- stance, engagement, first person, connectives, nominalization, and syntactic complexity vary by discipline and rhetorical move.

Therefore:

1. preserve the universal diagnostic question `can the reader recover the relation?`;
2. learn local realization from close analogue papers;
3. preserve the author's voice where it does not obstruct clarity;
4. apply exact target requirements last.
