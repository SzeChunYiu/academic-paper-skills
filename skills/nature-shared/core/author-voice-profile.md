# Author voice profile

> Shared contract for preserving a recognizable authorial style while improving scientific logic, clarity, natural scholarly expression, and journal fit.

## Contents

- [Purpose](#purpose)
- [When to build a voice profile](#when-to-build-a-voice-profile)
- [Source hierarchy](#source-hierarchy)
- [Voice dimensions](#voice-dimensions)
- [Invariants versus flexible traits](#invariants-versus-flexible-traits)
- [Rewrite workflow](#rewrite-workflow)
- [Interaction with natural scholarly prose](#interaction-with-natural-scholarly-prose)
- [Interaction with analogue papers](#interaction-with-analogue-papers)
- [Voice drift audit](#voice-drift-audit)
- [Failure modes](#failure-modes)
- [Output contract](#output-contract)

## Purpose

A strong rewrite should sound like a clearer, more rigorous version of the author, not like a generic journal imitation, an average of several published papers, or a standardized language-model register.

The voice profile records **how this author tends to communicate scientific reasoning** while separating those preferences from errors, ambiguity, unsupported claims, and journal mechanics.

The profile does not freeze weak prose. It preserves identity where doing so does not conflict with scientific accuracy, clarity, accessibility, or target requirements. Do not flatten a manuscript into **generic academic prose** merely because that prose is grammatically clean.

Naturalness is not measured by an AI detector. Never change wording merely to reduce an `AI probability`, avoid a rumored machine-associated word, create artificial `burstiness`, or insert human-like mistakes. The target is authentic, reader-aware scholarly expression.

## When to build a voice profile

Build one when:

- the user asks to rewrite/polish existing prose while keeping their style;
- multiple sections or a full manuscript are being rewritten;
- analogue papers are being studied for style/structure calibration;
- a journal transfer risks making the manuscript sound like several different authors;
- repeated AI editing has flattened the manuscript into generic academic English;
- the manuscript has become uniformly polished but no longer sounds authored.

For a tiny one-sentence correction, a formal profile is usually unnecessary.

## Source hierarchy

Learn the author's voice from, in order:

1. the current manuscript passages the author considers representative;
2. other supplied writing by the same author/project;
3. stable patterns repeated across several sections;
4. explicit user preferences about tone/style.

Do not infer voice from analogue papers, publisher marketing text, reviewer comments, generated prose, or an AI detector's preferred features.

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
- use of parallel structures;
- where the author naturally places emphasis.

Cadence should never be reduced to a target variance in sentence length.

### Agency and voice

- first-person `we` frequency;
- passive voice where method/process is foregrounded;
- explicit versus implicit author agency;
- how interpretive responsibility is expressed.

### Technical density

- abbreviation density;
- equation/notation narration;
- terminology repetition versus synonym use;
- amount of background explanation before specialist detail.

Technical term repetition can be part of good scientific voice. Do not replace stable terms with synonyms merely to create lexical variety.

### Epistemic stance

- direct versus cautious claim style;
- preferred hedge forms;
- how limitations are introduced;
- how uncertainty is integrated with results;
- how clearly observation is separated from interpretation.

Claim strength itself is **not** a style preference. Evidence controls it.

### Paragraph rhythm

- typical paragraph scale;
- location of paragraph nucleus;
- use of closing synthesis/bridge sentences;
- preference for examples or comparisons inside the paragraph;
- how often a paragraph closes a local inference versus opens the next question.

### Citation integration

- parenthetical versus narrative citation placement where the target permits both;
- dense synthesis versus spaced evidence discussion;
- how prior work is introduced and contrasted.

### Lexical character

- recurring neutral verbs and transition habits;
- preference for concrete versus abstract nouns;
- amount of evaluative language;
- stable project-specific terminology;
- characteristic level of formality.

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
- restrained versus more interpretive Discussion voice;
- typical relationship between evidence statements and interpretive statements.

### Flexible traits

May change freely to solve a rhetorical or journal problem.

Examples:

- paragraph length;
- transition wording;
- heading form;
- amount of contextual explanation;
- citation placement;
- sentence length at a difficult reasoning point;
- title/abstract compression;
- exact syntactic form when the underlying function stays intact.

## Rewrite workflow

### 1. Diagnose before editing

Separate:

- scientific/logic defects;
- clarity/cohesion defects;
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
- explicit logical relations before decorative connectors;
- restoration of a missing subject/action before adding prestigious vocabulary.

### 4. Re-voice after structural rewriting

If a section required major restructuring, run a second pass specifically to restore the author's cadence, agency, terminology, level of explicitness, and characteristic argument tempo.

### 5. Check cross-section consistency

A rewritten Abstract, Introduction, Results, and Discussion should sound like the same author while preserving each section's different rhetorical job.

## Interaction with natural scholarly prose

Load `natural-scholarly-prose.md` when a passage feels generic, over-smoothed, repetitive, connector-heavy, difficult to follow sentence by sentence, or suspiciously standardized after editing.

The division of labor is:

- `natural-scholarly-prose.md` controls **reader-facing reasoning realization**: sentence relation, given/new progression, lexical/reference chains, topic/emphasis, local stance, functional syntax, connectives, cadence;
- this file controls **manuscript identity**: the author's stable cadence, agency, technical density, terminology, and preferred degree of explicitness.

Run the natural-prose repair first when the reasoning is hard to follow, then re-voice. Do not preserve an author habit that forces readers to reconstruct the logic.

A useful principle is:

`natural scholarly prose = quality floor`

`author voice = identity layer above that floor`

### No detector-oriented voice engineering

Do not define author voice through features such as:

- high or low AI-detector probability;
- arbitrary sentence-length variance;
- deliberate fragments or errors;
- a blacklist of words associated with LLMs;
- forced contractions, slang, or idiosyncratic punctuation;
- random replacements designed to look less predictable.

Those techniques do not establish authentic authorship and may reduce scientific clarity.

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
9. Are consecutive sentences varied for real rhetorical reasons, or merely because an editor tried to make them look less machine-like?
10. Can every substantive wording change be explained by logic, clarity, disciplinary convention, evidence calibration, or an observed author preference?

If the answer reveals flattening, re-voice without undoing the scientific repairs.

## Failure modes

### Generic-academic flattening

Symptom: every sentence has the same length and polished neutral cadence.

Repair: restore observed author rhythm and agency after verifying sentence dependencies.

### Detector cosplay

Symptom: prose contains random short sentences, unusual punctuation, arbitrary synonyms, or deliberate roughness introduced only to appear human.

Repair: remove detector-oriented edits and return to scientific relation + author voice.

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

Natural-prose risks
- ...

Rewrite target
- clearer/more rigorous version of this author, not imitation of analogue papers or detector-oriented prose
```

Do not expose a long psycholinguistic profile unless the user asks for it. The profile is primarily an editing control.
