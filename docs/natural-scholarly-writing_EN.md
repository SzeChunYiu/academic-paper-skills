# Natural Scholarly Writing: A Practical Sentence-to-Sentence Guide

[中文](natural-scholarly-writing.md)

This guide turns the repository's writing research into an operational editing method. It is designed for academic prose that is scientifically correct but sounds generic, formulaic, over-smoothed, choppy, or machine-like.

It is **not** an AI-detector evasion manual. Do not add errors, random sentence lengths, unusual punctuation, or replace words solely because they appear on internet lists of `AI words`.

## The central idea

A paragraph feels natural when the reader can understand **why each sentence is here now**.

For every sentence after the first, ask:

`inherits X -> relation R -> adds Y -> enables Z`

If you cannot fill in those four fields, do not start with vocabulary polishing.

## 1. Start with propositions, not sentences

Take a paragraph that feels awkward and strip it down:

```text
P1. Performance improves on the internal test set.
P2. The improvement disappears in the external cohort.
P3. The two cohorts differ strongly in age distribution.
P4. Age-stratified analysis reduces the discrepancy.
P5. Therefore, the original generalization claim is too broad.
```

This proposition list exposes the scientific dependency better than polished prose.

Now map:

```text
P1 creates generalization expectation
P2 contradicts that expectation
P3 proposes a plausible source of the discrepancy
P4 tests that explanation
P5 narrows the claim using P2–P4
```

Only then rewrite.

## 2. Give every sentence a dependency

### Bad flow pattern

```text
The model achieved high accuracy on the internal cohort.
Furthermore, external validation is important for clinical models.
The external cohort contained older participants.
Moreover, age is an important clinical factor.
The model performed less well externally.
```

Every sentence is grammatical. The paragraph is still weak because sentence order follows generic topical association rather than reasoning.

### Better reasoning order

```text
The model achieved high accuracy on the internal cohort, but performance declined in the external cohort. The external cohort contained substantially older participants, raising the possibility that age-dependent case mix contributed to the discrepancy. Consistent with this explanation, age-stratified analysis reduced the performance gap, although it did not eliminate it. The model therefore generalizes less uniformly across populations than the internal evaluation alone suggests.
```

Why it flows:

- internal result -> external contradiction;
- contradiction -> candidate explanation;
- explanation -> discriminating analysis;
- analysis -> bounded conclusion.

The improvement comes from **dependency**, not from using more transitions.

## 3. Use given -> new as a default, not a formula

A useful progression is:

```text
Sentence 1: A -> B
Sentence 2: B -> C
Sentence 3: C -> D
```

This reduces the number of new entities the reader must activate at once.

But different reasoning needs different patterns.

### Constant topic

```text
The intervention increased response rate.
It also shortened recovery time.
It did not alter adverse-event frequency.
```

Useful when several parallel properties of one object are being reported.

### Contrast

```text
The internal cohort showed a strong effect.
The external cohort showed little evidence of the same effect.
```

Useful when symmetry makes the difference easier to see.

### Question -> evidence -> answer

```text
We next asked whether the effect depended on baseline severity. Stratified estimates increased monotonically across severity groups. This pattern suggests that the average treatment effect masks clinically relevant heterogeneity.
```

Do not rewrite every passage into one progression pattern.

## 4. Build identity chains

Readers need to know which object is still being discussed.

### Technical repetition is often good

If the paper calls something the `calibration model`, keep calling it the `calibration model` unless a defined abbreviation or category relation is needed.

Avoid:

```text
the model -> the framework -> the approach -> the system -> the technique
```

when all five expressions mean the same object.

That kind of synonym rotation can sound artificially polished and creates ambiguity.

### Make demonstratives explicit

Weak:

```text
This may explain the difference.
```

Stronger when several antecedents are possible:

```text
This age imbalance may explain the difference.
```

### Track conceptual chains, not just repeated words

```text
sampling bias -> differential recruitment -> cohort composition -> external-validity boundary
```

The chain can evolve as the argument evolves, but each step should be explicit.

## 5. Name the relation before choosing the transition

Between two sentences, choose the scientific relation first:

- evidence;
- explanation;
- cause;
- consequence;
- contrast;
- concession;
- comparison;
- specification;
- example;
- inference;
- qualification;
- next question.

Then decide whether the relation needs a connective.

### Connective not necessary

```text
The mutation increased receptor abundance. Surface-binding capacity increased in parallel.
```

If the relation is obvious from context, an extra `Furthermore` may add nothing.

### Connective useful

```text
The mutation increased receptor abundance. However, ligand affinity was unchanged.
```

Here `however` encodes a real contrast that affects interpretation.

## 6. Put topic and new information where readers expect them

Sentence openings often work best when they connect to active context.

Sentence endings often naturally receive emphasis.

Compare:

```text
A reduction in prediction error of 18% was observed after recalibration of the model using site-specific prevalence estimates.
```

with:

```text
Recalibrating the model with site-specific prevalence estimates reduced prediction error by 18%.
```

The second version exposes actor/action/result more directly.

This does not mean active voice is always superior. Use passive or process-centered syntax when the procedure/object, rather than the researcher, is the relevant topic.

## 7. Vary syntax because the rhetorical job changes

Do not try to make prose human by alternating long-short-long-short sentences.

Useful functional variation:

### Direct result

```text
The intervention reduced mortality.
```

### Result with important condition

```text
The intervention reduced mortality only among participants with severe baseline disease.
```

### Qualification

```text
Although the association remained after covariate adjustment, residual confounding cannot be excluded.
```

### Comparison

```text
Model A improved sensitivity, whereas Model B mainly improved calibration.
```

### Mechanism

```text
Because the mutation prevents receptor internalization, surface abundance remains elevated after stimulation.
```

Different functions naturally create different sentence forms.

## 8. Prefer ordinary precision to ornamental academic vocabulary

Do not make a sentence more academic by making its vocabulary rarer.

Prefer:

- `use` when `use` is exact;
- `show` when evidence directly shows something;
- `suggest` when evidence is indirect;
- `compare`, `test`, `estimate`, `measure`, `predict`, `identify` when those verbs describe the actual scientific operation.

Be skeptical of empty prestige phrases:

- `paves the way for`;
- `underscores the critical importance of`;
- `provides valuable insights into`;
- `represents a significant advancement`;
- `plays a crucial role in`.

These phrases are not forbidden. Replace them when they hide the actual consequence.

Instead of:

```text
These findings provide valuable insights into treatment heterogeneity.
```

write the insight:

```text
The average treatment effect masks a subgroup in which the intervention provides little benefit.
```

## 9. Calibrate stance locally

Natural academic writing has variation in confidence because the **evidence varies**, not because the writer is trying to vary style.

### Direct observation

`We observed...`

### Estimate

`The estimated difference was...`

### Association

`X was associated with Y.`

### Indirect interpretation

`This pattern suggests...`

### Plausible explanation

`One possibility is...`

### Formal result

`Under assumptions A–C, the theorem establishes...`

Do not use `demonstrates` merely because it sounds strong.

## 10. Keep authorial agency when it matters

A paper becomes generic when every decision is described as if nobody made it.

Use first person where permitted and useful:

```text
We chose the external cohort before inspecting outcome labels.
We interpret this discrepancy as evidence of population-specific calibration drift.
```

Use process-centered syntax when the process is the real topic:

```text
Samples were randomized before imaging.
```

The question is not active versus passive. It is **what should be foregrounded here?**

## 11. Make paragraph endings do scientific work

Weak generic close:

```text
Taken together, these findings highlight the importance of robust validation.
```

Possible stronger closes:

### Bounded conclusion

```text
The model therefore transfers across sites only after prevalence recalibration.
```

### Remaining uncertainty

```text
Whether the residual performance gap reflects unmeasured case mix remains unresolved.
```

### Handoff

```text
We therefore tested whether site-specific feature distributions accounted for the remaining gap.
```

The next paragraph should pick up that consequence/question.

## 12. Audit machine-like standardization

After a major rewrite, scan for:

- several sentences beginning with the same frame;
- every paragraph ending with a generic implication;
- repeated `Moreover/Furthermore/Additionally`;
- repeated `This study...` sentences;
- the same hedge in every interpretive sentence;
- many rare synonyms but few stable technical terms;
- repeated syntactic frames with only word substitution;
- all authorial decisions rewritten as agentless passive constructions;
- smooth prose with weak evidence dependencies.

Do not fix these mechanically. Ask what rhetorical function each sentence actually needs.

## 13. Run a read-aloud cadence audit

Only after logic is stable, read the paragraph aloud.

Listen for:

- long subjects that delay the verb;
- repeated rhythms;
- too many consecutive sentences with the same opening;
- an important conclusion buried in the middle;
- sentence breaks that interrupt one logical relation;
- paragraphs with no natural point of emphasis.

Fix cadence when it interferes with comprehension or the author's established voice.

Do not introduce errors or random variation.

## 14. Re-voice after restructuring

The correct order is:

1. repair scientific logic;
2. repair sentence/paragraph dependencies;
3. repair information flow and stance;
4. realize clear natural prose;
5. restore the author's recognizable voice.

Preserve:

- cadence;
- preferred agency;
- technical directness;
- signposting level;
- stable terminology;
- epistemic rhythm.

Do not restore ambiguity, awkward calques, unsupported certainty, or redundant prose merely because they appeared in the original.

## 15. A compact paragraph checklist

Before finalizing a paragraph:

- **Nucleus:** Why does this paragraph exist?
- **Dependency:** Why does each sentence occur in this order?
- **Inheritance:** What does each sentence pick up?
- **Relation:** How does it relate to the previous sentence?
- **Advance:** What new information does it add?
- **Enablement:** What does it make possible next?
- **Identity:** Can the reader track the central entities?
- **Stance:** Is every claim calibrated to evidence?
- **Syntax:** Does sentence form match rhetorical function?
- **Connective:** Is every explicit transition doing real work?
- **Cadence:** Does the paragraph have purposeful rather than mechanical rhythm?
- **Voice:** Does it sound like this manuscript's author?
- **Drift:** Did any rewrite increase causality, generality, certainty, novelty, or importance?

## 16. What not to do

Do not:

- optimize an AI-detector probability;
- remove words because they appear on a viral `AI vocabulary` list;
- insert deliberate errors;
- randomize sentence length;
- add unnecessary contractions/slang;
- rotate synonyms for central technical terms;
- copy the style of a named living author;
- copy distinctive sentences from analogue papers;
- add transitions before establishing the relation;
- use `humanization` to disguise unsupported claims.

The goal is not to hide how the text was produced. The goal is to make the scientific reasoning genuinely readable and recognizably authored.
