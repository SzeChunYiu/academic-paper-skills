# Author voice profile

> Shared contract for preserving a recognizable authorial style while improving scientific logic, clarity, and journal fit.

## Contents

- [Purpose](#purpose)
- [When to build a voice profile](#when-to-build-a-voice-profile)
- [Source hierarchy](#source-hierarchy)
- [Voice dimensions](#voice-dimensions)
- [Invariants versus flexible traits](#invariants-versus-flexible-traits)
- [Rewrite workflow](#rewrite-workflow)
- [Interaction with analogue papers](#interaction-with-analogue-papers)
- [Voice drift audit](#voice-drift-audit)
- [Failure modes](#failure-modes)
- [Output contract](#output-contract)

## Purpose

A strong rewrite should sound like a clearer, more rigorous version of the author, not like a generic journal imitation or an average of several published papers.

The voice profile records **how this author tends to communicate scientific reasoning** while separating those preferences from errors, ambiguity, unsupported claims, and journal mechanics.

The profile does not freeze weak prose. It preserves identity where doing so does not conflict with scientific accuracy, clarity, accessibility, or target requirements.

## When to build a voice profile

Build one when:

- the user asks to rewrite/polish existing prose while keeping their style;
- multiple sections or a full manuscript are being rewritten;
- analogue papers are being studied for style/structure calibration;
- a journal transfer risks making the manuscript sound like several different authors;
- repeated AI editing has flattened the manuscript into generic academic English.

For a tiny one-sentence correction, a formal profile is usually unnecessary.

## Source hierarchy

Learn the author's voice from, in order:

1. the current manuscript passages the author considers representative;
2. other supplied writing by the same author/project;
3. stable patterns repeated across several sections;
4. explicit user preferences about tone/style.

Do not infer voice from analogue papers, publisher marketing text, reviewer comments, or generated prose.

If the supplied manuscript already contains heavy multi-author/editor drift, identify the conflict instead of pretending it has one stable voice.

## Voice dimensions

Record only dimensions that are actually observable.

### Argument tempo

- direct claim-first versus gradual setup;
- compact versus explanatory reasoning;
- frequency of explicit reader signposts;
- tendency to preview versus reveal conclusions locally.

### Sentence cadence

- typical sentence length/rhythm;
- preference for simple clauses versus controlled multi-clause sentences;
- degree of phrasal compression;
- use of parallel structures.

### Agency and voice

- first-person `we` frequency;
- passive voice where method/process is foregrounded;
- explicit versus implicit author agency.

### Technical density

- abbreviation density;
- equation/notation narration;
- terminology repetition versus synonym use;
- amount of background explanation before specialist detail.

### Epistemic stance

- direct versus cautious claim style;
- preferred hedge forms;
- how limitations are introduced;
- how uncertainty is integrated with results.

Claim strength itself is **not** a style preference. Evidence controls it.

### Paragraph rhythm

- typical paragraph scale;
- location of paragraph nucleus;
- use of closing synthesis/bridge sentences;
- preference for examples or comparisons inside the paragraph.

### Citation integration

- parenthetical versus narrative citation placement where the target permits both;
- dense synthesis versus spaced evidence discussion;
- how prior work is introduced and contrasted.

### Lexical character

- recurring neutral verbs and transition habits;
- preference for concrete versus abstract nouns;
- amount of evaluative language;
- stable project-specific terminology.

Do not deliberately preserve grammatical mistakes, awkward calques, filler, or imprecise terminology merely because they recur.

## Invariants versus flexible traits

Divide the profile into two groups.

### Voice invariants

Preserve unless they conflict with accuracy/clarity/requirements.

Examples:

- preferred level of technical directness;
- recognizable sentence cadence;
- consistent use of `we` versus impersonal method narration;
- degree of explicit signposting;
- terminology choices;
- restrained versus more interpretive Discussion voice.

### Flexible traits

May change freely to solve a rhetorical or journal problem.

Examples:

- paragraph length;
- transition wording;
- heading form;
- amount of contextual explanation;
- citation placement;
- sentence length at a difficult reasoning point;
- title/abstract compression.

## Rewrite workflow

### 1. Diagnose before editing

Separate:

- scientific/logic defects;
- clarity defects;
- journal/genre requirements;
- voice characteristics.

Do not call a logic defect `style`.

### 2. Preserve the author's reasoning stance

Where the author's original reasoning is clear and defensible, keep its conceptual order unless there is a stronger structural reason to change it.

### 3. Repair at the smallest useful level

Prefer:

- stronger paragraph ordering before wholesale voice replacement;
- precise sentence restructuring before generic paraphrase;
- terminology repair before synonym variation;
- explicit logical relations before decorative connectors.

### 4. Re-voice after structural rewriting

If a section required major restructuring, run a second pass specifically to restore the author's cadence, agency, terminology, and level of explicitness.

### 5. Check cross-section consistency

A rewritten Abstract, Introduction, Results, and Discussion should sound like the same author while preserving each section's different rhetorical job.

## Interaction with analogue papers

Analogue papers can teach:

- what moves readers expect;
- evidence/figure sequence;
- background depth;
- common local reporting patterns;
- where claims and limitations usually appear.

They should **not** determine:

- the author's favorite transition words;
- sentence cadence;
- characteristic phrasing;
- voice/person choices unless required by the target;
- distinctive rhetorical flourishes.

Use this conceptual split:

`analogue papers = structural priors`

`author voice = expression prior`

`user's evidence = truth constraint`

`journal rules = compliance constraint`

## Voice drift audit

After rewriting, compare representative before/after passages.

Ask:

1. Does the revised text still use the author's stable terminology?
2. Is the degree of directness recognizable?
3. Has every paragraph acquired the same AI-like cadence?
4. Did first-person/passive use change without a rhetorical reason?
5. Did the rewrite add generic prestige phrases absent from the author's voice?
6. Did analogue-paper wording leak into the manuscript?
7. Are hedges/boosters now stronger because of style imitation rather than evidence?
8. Does each section sound like the same author but still perform its own function?

If the answer reveals flattening, re-voice without undoing the scientific repairs.

## Failure modes

### Generic-academic flattening

Symptom: every sentence has the same length and polished neutral cadence.

Repair: restore observed author rhythm and agency.

### Journal cosplay

Symptom: manuscript starts sounding like a caricature of Nature/Science/IEEE/etc.

Repair: retain only verified target constraints and useful rhetorical architecture.

### Analogue cloning

Symptom: characteristic phrases/layout logic from one comparison paper appear repeatedly.

Repair: abstract the move, then rewrite from the author's own reasoning.

### Error preservation

Symptom: awkward or ambiguous structures are retained in the name of voice.

Repair: preserve identity, not defects.

### Multi-author inconsistency

Symptom: different sections contain incompatible voice profiles.

Repair: define one manuscript-level voice target, then preserve section-specific variation within it.

## Output contract

A working author voice profile should be concise:

```text
Voice invariants
- ...

Flexible traits
- ...

Terminology/agency rules
- ...

Patterns to remove
- ...

Rewrite target
- clearer/more rigorous version of this author, not imitation of analogue papers
```

Do not expose a long psycholinguistic profile unless the user asks for it. The profile is primarily an editing control.