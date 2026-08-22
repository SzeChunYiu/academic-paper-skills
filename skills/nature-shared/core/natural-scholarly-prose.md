# Natural scholarly prose

> Shared contract for producing academic prose that is precise, reader-aware, authorial, and logically continuous without collapsing into generic machine-like academic English. Last reviewed: 2026-08-22.
>
> This is a writing-quality contract. It is **not** an AI-detector evasion guide.

## Contents

- [Purpose](#purpose)
- [What natural scholarly writing means](#what-natural-scholarly-writing-means)
- [Research-backed failure patterns](#research-backed-failure-patterns)
- [The sentence-flow hierarchy](#the-sentence-flow-hierarchy)
- [The why-this-sentence-now test](#the-why-this-sentence-now-test)
- [Information progression](#information-progression)
- [Lexical and referential continuity](#lexical-and-referential-continuity)
- [Sentence relations](#sentence-relations)
- [Topic, stress, and emphasis](#topic-stress-and-emphasis)
- [Functional syntactic variation](#functional-syntactic-variation)
- [Natural academic lexis](#natural-academic-lexis)
- [Stance, engagement, and author presence](#stance-engagement-and-author-presence)
- [Paragraph choreography](#paragraph-choreography)
- [Connectives and signposting](#connectives-and-signposting)
- [Cadence and the read-aloud audit](#cadence-and-the-read-aloud-audit)
- [Anti-template audit](#anti-template-audit)
- [Revision workflow](#revision-workflow)
- [Interaction with author voice and analogue papers](#interaction-with-author-voice-and-analogue-papers)
- [Boundaries](#boundaries)
- [Research basis](#research-basis)

## Purpose

The target is not prose that merely *looks human*. The target is prose in which a qualified reader can follow the author's reasoning with minimal backtracking and can hear a stable scholarly voice behind the claims.

Use this contract when:

- drafting or substantially rewriting academic prose;
- polishing text that feels generic, formulaic, over-smoothed, repetitive, or machine-like;
- restoring authorial voice after large structural edits;
- repairing sentence-to-sentence or paragraph-to-paragraph flow;
- adapting prose to a journal without turning the manuscript into journal cosplay;
- studying analogue papers without copying their wording.

The quality objective is:

`scientific relation -> information flow -> lexical/reference continuity -> stance -> syntax -> connective -> cadence`

Do not reverse this order by polishing vocabulary before the reasoning relation is clear.

## What natural scholarly writing means

Natural scholarly writing is **not** conversational filler, deliberate imperfection, random sentence-length variation, or avoidance of words associated with language models.

It is writing with:

- a recoverable line of reasoning;
- concrete scientific subjects and actions where possible;
- stable terminology for stable concepts;
- purposeful variation in sentence form because rhetorical functions vary;
- stance calibrated locally to the evidence;
- visible authorial decisions when agency matters;
- enough lexical and referential overlap for the reader to track entities;
- transitions that encode real relations rather than decorate jumps;
- paragraph endings that complete an inference or create a useful next question;
- a recognizable author voice that survives editing.

A technically dense paper may still sound natural. A highly formal paper may still sound natural. Naturalness is **context-sensitive control**, not informality.

## Research-backed failure patterns

Recent comparative research on human and LLM-produced academic writing suggests several recurring risks. Treat them as diagnostic hypotheses, not universal machine fingerprints.

### 1. Narrow and repetitive stance / engagement

LLM-produced academic writing can rely on a narrower and more repetitive set of stance and engagement devices than human writing, even when the prose is superficially coherent.

Diagnostic questions:

- Does every limitation use the same hedge?
- Does every paragraph use the same confidence level?
- Does the text repeatedly use the same engagement frame (`it is important to note`, `it should be noted`, etc.) regardless of function?
- Are claims either uniformly cautious or uniformly assertive instead of locally calibrated?

Repair: decide the epistemic status of each proposition first, then choose language.

### 2. Standardized cadence with low meaningful variability

Recent corpus work reports more standardized expression and less stylistic variability in AI-generated academic text than in human-authored text.

Diagnostic questions:

- Do several consecutive sentences have the same clause pattern?
- Do paragraphs repeatedly have the same opening and closing shape?
- Does every result sentence use `X showed that Y`, even when the rhetorical relation differs?
- Does every paragraph sound equally polished, detached, and rhythmically uniform?

Repair: vary syntax only when the **function** changes. Do not inject random short sentences for artificial `burstiness`.

### 3. Ornamental or unnecessarily rare academic vocabulary

Corpus comparisons have found overuse of infrequent academic vocabulary and flowery language in some ChatGPT-generated academic prose.

Repair rule:

> Prefer the most precise conventional term the field would naturally use, even when it is ordinary.

Do not replace `use` with `utilize`, `show` with an ornate synonym, or a stable technical term with rotating near-synonyms merely to sound scholarly.

### 4. Synonym substitution inside repeated syntactic templates

Changing nouns and verbs while preserving the same sentence frame does not create genuine rhetorical variety.

Repair: change sentence architecture only when the relation, topic, agency, evidence status, or emphasis changes.

### 5. Depersonalized or over-deterministic argumentation

Research on AI-assisted academic writing has raised concerns about homogenized stance and weakened authorial identity. A manuscript can become impersonal not because passive voice is intrinsically bad, but because authorial decisions disappear.

Repair:

- use `we` when the authors' decision, analysis, interpretation, or contribution is the relevant subject and the field/target permits it;
- use passive or process-centered syntax when the procedure/object should remain foregrounded;
- do not hide interpretive responsibility behind `it is believed`, `it is evident`, or other agentless constructions unless the source of evaluation is genuinely communal or irrelevant.

### 6. Connector stuffing

More connectives do not guarantee more coherence. Academic corpora show section- and discipline-specific cohesion patterns, and L2 writing can overuse additive linking adverbials.

Repair: state the underlying relation first. Add an explicit connective only when the relation would otherwise be difficult to recover.

### 7. Generic prestige phrasing

Phrases such as `underscores the critical importance`, `paves the way for`, `offers valuable insights into`, or `represents a significant advancement` often carry less information than a concrete consequence.

Do not ban phrases mechanically. Ask instead:

> What exactly changes for knowledge, inference, capability, measurement, theory, practice, or future work?

Write that consequence.

## The sentence-flow hierarchy

For every difficult passage, repair in this order:

1. **Proposition** — what does each sentence actually assert?
2. **Relation** — why does sentence B follow sentence A?
3. **Information state** — what is already active for the reader, and what is new?
4. **Entity chain** — which objects/terms/referents must remain trackable?
5. **Topic and emphasis** — what should the reader recognize first, and what should receive stress?
6. **Stance** — how strongly is this proposition warranted?
7. **Syntax** — what clause structure best realizes that function?
8. **Connective** — is an explicit relation marker needed?
9. **Cadence** — does the sequence sound monotonous or overloaded after logic is fixed?

A passage that fails steps 1–4 cannot be repaired by vocabulary or punctuation alone.

## The why-this-sentence-now test

For every sentence after the first in a paragraph, answer four questions:

1. **Inheritance** — what word, concept, result, contrast, question, or assumption does this sentence inherit from the preceding context?
2. **Relation** — is it evidence, explanation, consequence, contrast, concession, specification, comparison, qualification, inference, or a bridge?
3. **Advance** — what genuinely new information does it add?
4. **Enablement** — what becomes possible for the next sentence because this sentence exists?

Compact representation:

`inherits X -> performs relation R -> adds Y -> enables Z`

If no meaningful `inherits` or `relation` can be written, the sentence may be misplaced or the missing bridge may be conceptual rather than linguistic.

### Dependency-graph test

Before rewriting a dense paragraph, map sentence dependencies:

```text
S1 establishes phenomenon A
S2 qualifies A using condition B
S3 explains why B matters for interpretation C
S4 tests C against alternative D
S5 closes with bounded inference E
```

Then write prose that makes those dependencies easy to recover. Do not preserve the original sentence order merely because the grammar is correct.

## Information progression

A useful default is **given -> new**:

```text
S1: A -> B
S2: B -> C
S3: C -> D
```

The reader meets familiar material near the beginning and receives the important advance later. The new information can then serve as the next sentence's point of departure.

But given->new is a **default reader-management principle**, not a compulsory template.

Use other patterns when the reasoning calls for them:

- **constant topic**: A -> B; A -> C; A -> D;
- **derived themes**: A -> A1, then A2, then A3;
- **contrast pair**: A -> property X; B -> contrasting property Y;
- **question-answer**: unresolved Q -> evidence -> answer;
- **claim-evidence-qualification**: claim A -> support B -> boundary C.

Ask whether the chosen progression reduces working-memory burden and keeps the argument's center visible.

## Lexical and referential continuity

Natural flow often depends on controlled repetition.

### Repeat central technical terms when the referent is unchanged

In technical prose, stylistic synonym rotation can damage precision. If `model`, `framework`, `system`, and `approach` do not mean exactly the same thing, do not alternate them merely to avoid repetition.

A useful rule from scientific-writing pedagogy is that exact repetition of a technical term is often safer than changing names for stylistic variety.

### Build identity chains

Track the same entity or concept across adjacent sentences using:

- exact term repetition;
- stable abbreviation;
- unambiguous pronoun;
- precise demonstrative noun phrase (`this discrepancy`, `this assumption`, `these estimates`);
- clearly marked subtype or supertype.

Recent coherence research suggests that stronger writers develop more effective identity chains rather than merely inserting more cohesive devices.

### Demonstrative test

For every `this`, `these`, `it`, `they`, or `such`, ask whether a reader could reasonably identify two possible antecedents. If yes, name the noun.

Bad:

`This may explain the difference.`

Better when ambiguity exists:

`This sampling imbalance may explain the difference.`

## Sentence relations

Label adjacent-sentence relations before inserting connectives.

Core relations:

- evidence / support;
- explanation / mechanism;
- cause;
- consequence;
- contrast;
- concession;
- comparison;
- specification;
- example;
- sequence;
- inference;
- qualification / boundary;
- problem -> response;
- result -> next question.

### Relation test

Read two adjacent sentences and complete:

`Sentence B exists because Sentence A ______.`

If the blank cannot be filled with a meaningful relation, investigate structure before style.

## Topic, stress, and emphasis

Readers use sentence openings and endings as interpretive cues.

### Opening position

The beginning often works best when it provides:

- the active topic;
- familiar context;
- a stable entity;
- the condition under which the sentence should be read.

Avoid long abstract subjects that delay the main relation when a more concrete subject is available.

### Stress position

The end of a sentence often receives natural emphasis. Use it for important new information when that ordering remains grammatical and accurate.

Do not mechanically force every claim to sentence-final position. The point is to align information placement with rhetorical hierarchy.

### Subject-action test

Ask:

- Who or what performs the important action?
- Is that subject visible early enough?
- Is the main verb carrying the scientific action, or has it been diluted into a noun (`an evaluation of X was conducted`)?

Prefer a concrete clause when it improves precision:

`We evaluated X` or `The analysis evaluated X`

over
`An evaluation of X was conducted`

unless the nominal form has a genuine discourse function.

## Functional syntactic variation

Human-sounding scholarly prose does not require random variation. It requires **functionally motivated variation**.

### Useful correspondences

- **Decisive local result** — often benefits from a direct finite clause.
- **Qualification** — may require a dependent clause because the condition is logically subordinate.
- **Comparison** — parallel syntax can make the comparison visible.
- **Procedure** — chronological syntax helps when order matters.
- **Cause/mechanism** — explicit clauses usually outperform dense noun stacks when the relation is new.
- **Established technical concept** — compact nominalization can be efficient once readers know the concept.
- **Contrast** — balanced clauses can make the opposition easy to compare.
- **Definition** — keep term and defining property close together.

### Clause-shape audit

Flag runs of three or more sentences with near-identical architecture **only when the repeated form no longer reflects repeated function**.

Do not rewrite parallel evidence sentences merely to create surface variety. Parallel content can legitimately use parallel form.

## Natural academic lexis

### Prefer precision to impressive vocabulary

Choose words by:

1. field meaning;
2. claim strength;
3. collocational naturalness;
4. reader familiarity;
5. economy.

Do not choose by rarity.

### Prefer verbs that expose the relation

Examples:

- data `show`, `indicate`, `suggest`, `are consistent with`;
- a model `predicts`, `estimates`, `classifies`;
- an analysis `tests`, `compares`, `quantifies`;
- a theorem `establishes` under stated assumptions;
- a qualitative analysis `identifies`, `interprets`, `characterizes` themes/patterns as appropriate.

Use the strongest verb justified by the evidence, not the strongest available verb.

### Avoid noun-stack inflation

Unpack long sequences of abstract nouns when the underlying relation is difficult to see.

Instead of asking whether a sentence is `academic enough`, ask whether the reader can identify:

`actor/object -> relation/action -> evidence/status -> consequence`

## Stance, engagement, and author presence

Academic writing is not neutral text without a writer. Authors make choices about evidence, interpretation, scope, comparison, and uncertainty.

### Calibrate stance proposition by proposition

Distinguish:

- directly observed;
- estimated;
- associated;
- experimentally manipulated;
- causally identified;
- simulated;
- inferred;
- hypothesized;
- proved under assumptions;
- interpreted from qualitative/source evidence.

Then choose stance language.

Do not apply one hedge level to an entire manuscript.

### Use author presence where it clarifies responsibility

First person can be appropriate for:

- study decisions;
- contribution statements;
- analytical choices;
- interpretation (`we interpret...`) when ownership matters;
- paper organization where the discipline permits it.

Do not insert `we` everywhere to sound human. Agency must serve the sentence.

### Engagement should be purposeful

Reader-directed language, questions, directives, shared-knowledge appeals, and signposts vary strongly across disciplines. Learn them from close analogue papers and the target genre rather than forcing a universal engagement style.

## Paragraph choreography

A paragraph should behave like a small reasoning episode, not a bag of grammatically related sentences.

### Start with the nucleus or orient toward it

The paragraph nucleus is the proposition/question/result that makes the paragraph necessary. It need not always be sentence 1, but readers should be able to identify it without reconstructing the paragraph afterward.

### Arrange satellites by reasoning dependency

Possible satellites:

- evidence;
- explanation;
- comparison;
- qualification;
- counterevidence;
- implication;
- bridge.

Order them according to what the reader needs next.

### Evidence and interpretation boundary

Do not merge observation and interpretation when doing so increases the apparent certainty of the evidence. Conversely, do not force them into separate sentences when a single carefully subordinated sentence makes the evidence-status relation clearer.

### End with consequence, boundary, or handoff

A useful ending often tells the reader one of three things:

- what can now be concluded;
- what remains uncertain;
- why the next analysis/paragraph is necessary.

Avoid ending every paragraph with a generic `These findings highlight...` sentence when the scientific consequence can be stated directly.

## Connectives and signposting

Connectives are labels for relations already present in the reasoning.

### Use explicit connectives when

- the relation could otherwise be misread;
- a contrast or concession changes interpretation;
- the inferential step is important;
- the reader must distinguish sequence from causality;
- the text changes scale, population, condition, or evidence class.

### Omit them when

- lexical/reference continuity already makes the relation obvious;
- syntax encodes the relation;
- the connective merely announces addition (`moreover`) without explaining why the evidence belongs together.

### Connector-density audit

Do not target a preferred number of `however`, `therefore`, `moreover`, `furthermore`, or `additionally` tokens. Corpus research shows that cohesion and connective use vary by section, discipline, and writer population.

## Cadence and the read-aloud audit

Cadence is a **late** editing layer.

After logic, terminology, stance, and syntax are correct, read the paragraph aloud or simulate an oral read.

Listen for:

- repeated sentence openings;
- several sentences with identical length and clause rhythm;
- long runs with no natural emphasis point;
- abrupt short sentences that break a relation that should be integrated;
- sentences that require a second reading because the subject/verb relation arrives too late;
- monotonous repeated paragraph closings.

Repair only when cadence interferes with comprehension or author voice.

Never introduce grammatical errors, random fragments, arbitrary punctuation, or random sentence lengths to manufacture `human` variation.

## Anti-template audit

Flag repeated frames when they become functionally empty:

- `This study ...` at the start of many adjacent sentences;
- `It is important to note that ...` without a reason the note is important;
- `Furthermore/Moreover/Additionally` used as default paragraph glue;
- identical three-part lists across paragraphs;
- repeated `not only ... but also ...` constructions;
- generic `These findings underscore/highlight ...` closings;
- repeated `X plays a crucial role in Y` abstractions;
- repeated prestige claims (`novel`, `groundbreaking`, `significant advancement`) without a measurable distinction.

These are **diagnostics, not banned strings**. A phrase is acceptable when it is the clearest accurate realization of the intended relation.

### No AI-word blacklist

Do not maintain a list of words to remove simply because they have been associated with LLMs. Research on human-LLM coevolution shows that lexical signatures change as writers and models adapt, making word-level avoidance a poor quality criterion.

Judge the sentence by function, specificity, collocation, evidence, and voice.

## Revision workflow

For a paragraph that feels `AI-written`, generic, or unnatural:

### Pass 1 — strip to propositions

Write one plain line per scientific proposition. Remove rhetorical decoration temporarily.

### Pass 2 — map dependency

Record why each proposition follows the previous one.

### Pass 3 — choose information progression

Select linear given->new, constant topic, derived themes, contrast, question-answer, or another defensible progression.

### Pass 4 — stabilize entity chains

Restore canonical technical terms and explicit referents.

### Pass 5 — calibrate stance

Set local claim strength from evidence.

### Pass 6 — realize syntax by function

Choose clause structure, agency, and sentence boundaries.

### Pass 7 — add only necessary connectives

Make implicit relations explicit only where readers need help.

### Pass 8 — restore author voice

Load `author-voice-profile.md`. Restore the project's cadence, agency habits, technical density, and signposting without reintroducing defects.

### Pass 9 — cadence audit

Read the paragraph as continuous prose. Remove mechanical repetition or needless ornament.

### Pass 10 — scientific drift audit

Confirm that naturalization did not strengthen causality, certainty, generality, novelty, or importance.

## Interaction with author voice and analogue papers

Use four constraints independently:

`author evidence = truth constraint`

`journal / reporting rules = compliance constraint`

`analogue papers = structural and local-convention priors`

`author voice = expression prior`

Natural scholarly prose mediates **expression**, not truth.

A close analogue can show that a field often uses direct first-person contribution statements or compact Discussion paragraphs. That does not authorize copying its phrases. The author's own voice determines how the valid rhetorical move is realized.

If analogue practice and author voice conflict:

1. obey scientific validity;
2. obey required journal/reporting rules;
3. preserve enough local convention for intelligibility;
4. preserve author voice everywhere else.

## Boundaries

Never use this contract to:

- evade AI-detection systems;
- optimize an `AI probability` score;
- insert deliberate mistakes or awkwardness;
- randomly vary sentence length, punctuation, vocabulary, or spelling;
- conceal AI assistance when disclosure is required;
- imitate a named living author's distinctive style;
- copy sentences, paragraph structures, or distinctive rhetorical flourishes from analogue papers;
- make unsupported claims sound more convincing.

The system should be able to explain every revision in terms of **logic, readability, disciplinary convention, evidence calibration, or the author's established voice**.

## Research basis

Use this evidence as guidance, not as a universal style template.

### AI-assisted / AI-generated academic prose

- Mo, Z. & Crosthwaite, P. (2025). *Exploring the affordances of generative AI large language models for stance and engagement in academic writing*. Journal of English for Academic Purposes, 75, 101499. https://doi.org/10.1016/j.jeap.2025.101499
  - Compared three LLMs with human academic writers on matched topics; LLMs used a narrower and more repetitive range of stance/engagement resources.
- *A corpus-driven comparative analysis of AI in academic discourse: Investigating ChatGPT-generated academic texts in social sciences* (2024). Lingua, 312, 103838. https://doi.org/10.1016/j.lingua.2024.103838
  - Reported overuse of infrequent academic vocabulary/flowery language, lower human-like syntactic variation, and synonym substitution inside similar structures.
- Zhao, N. & Lei, L. (2026). *Informality features in AI-generated academic writing: A corpus-based comparison between human and AI*. Journal of English for Academic Purposes, 79, 101629. https://doi.org/10.1016/j.jeap.2026.101629
  - Found AI-generated academic abstracts more standardized and less variable in style than human-authored abstracts.
- *Reconstructing stance in EFL doctoral thesis writing through generative artificial intelligence* (2025). Humanities and Social Sciences Communications, 12, 1963. https://doi.org/10.1057/s41599-025-06249-x
  - Examined changes in authorial stance in doctoral writing in the GenAI era and discusses homogenization/depersonalization risks.
- Geng, M. & Trotta, R. (2025). *Human-LLM Coevolution: Evidence from Academic Writing*. Findings of ACL 2025, 12689–12696. https://aclanthology.org/2025.findings-acl.657/
  - Shows why static word-frequency signatures are unstable quality/detection criteria as humans and models co-evolve.

### Cohesion and sentence flow

- Golparvar, S. E., Crosthwaite, P. & Ziaeian, E. (2024). *Mapping cohesion in research articles of applied linguistics: A close look at rhetorical sections*. Journal of English for Academic Purposes, 67, 101316. https://doi.org/10.1016/j.jeap.2023.101316
  - Cohesion patterns differ by rhetorical section at sentence, paragraph, and text levels.
- Golparvar, S. E., Hu, G. & Seyedi, S. E. (2025). *Cohesion in the discussion section of research articles: A cross-disciplinary investigation*. English for Specific Purposes, 77, 1–19. https://doi.org/10.1016/j.esp.2024.08.004
  - Found substantial cross-disciplinary variation in local/global/text cohesion across applied linguistics, chemistry, and economics.
- *Assessing the effects of explicit coherence instruction on EFL students' integrated writing performance* (2026). Assessing Writing, 67, 101019. https://doi.org/10.1016/j.asw.2026.101019
  - In a mixed-methods study of 64 EFL students, explicit coherence instruction improved performance; stronger writers showed better identity-chain development.

### Scientific-paper structure and writing process

- Mensh, B. & Kording, K. (2017). *Ten simple rules for structuring papers*. PLOS Computational Biology, 13(9), e1005619. https://doi.org/10.1371/journal.pcbi.1005619
  - Useful reader-oriented structural heuristics across sentence, paragraph, section, and document scales. Treat its C-C-C model as a heuristic, not a universal skeleton.
- Weinberger, C. J., Evans, J. A. & Allesina, S. (2015). *Ten Simple (Empirical) Rules for Writing Science*. PLOS Computational Biology, 11(4), e1004205. https://doi.org/10.1371/journal.pcbi.1004205
  - Analyzed more than one million abstracts across eight disciplines and cautions that common style advice does not uniformly predict citation outcomes; journal context matters.

### Pedagogic information-flow references

- Harvard College Writing Center, *Transitions*: https://writingcenter.fas.harvard.edu/transitions
- Purdue OWL, *Tips for Writing in North American Colleges: The Basics*: https://owl.purdue.edu/

Use pedagogic sources for reader-management heuristics and empirical corpus studies to calibrate how strongly those heuristics should be generalized.
