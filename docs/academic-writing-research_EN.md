# Academic Writing Research: What Strong Papers Actually Do

[中文](academic-writing-research.md)

This document summarizes the research basis behind the repository's writing system. It is not a universal style manual and it is not a list of prestigious-journal tricks. The goal is to identify what can be generalized across academic writing, what varies by discipline/genre, and what should remain a local calibration learned from comparable papers.

Last reviewed: 2026-08-22.

## Contents

- [1. The central conclusion](#1-the-central-conclusion)
- [2. Academic writing is a reasoning system before it is a language style](#2-academic-writing-is-a-reasoning-system-before-it-is-a-language-style)
- [3. Why fixed templates fail across disciplines](#3-why-fixed-templates-fail-across-disciplines)
- [4. The argument spine](#4-the-argument-spine)
- [5. Paragraphs as reasoning episodes](#5-paragraphs-as-reasoning-episodes)
- [6. Sentence-to-sentence flow](#6-sentence-to-sentence-flow)
- [7. Cohesion is more than transitions](#7-cohesion-is-more-than-transitions)
- [8. Syntax should follow rhetorical function](#8-syntax-should-follow-rhetorical-function)
- [9. Stance, uncertainty, and author presence](#9-stance-uncertainty-and-author-presence)
- [10. What current research suggests about AI-like academic prose](#10-what-current-research-suggests-about-ai-like-academic-prose)
- [11. Why word blacklists and detector-oriented rewriting are the wrong goal](#11-why-word-blacklists-and-detector-oriented-rewriting-are-the-wrong-goal)
- [12. Reading analogue papers](#12-reading-analogue-papers)
- [13. Figures and data are part of the argument](#13-figures-and-data-are-part-of-the-argument)
- [14. Section-specific writing](#14-section-specific-writing)
- [15. A research-backed manuscript workflow](#15-a-research-backed-manuscript-workflow)
- [16. What should remain local rather than universal](#16-what-should-remain-local-rather-than-universal)
- [17. Research sources](#17-research-sources)

## 1. The central conclusion

Strong academic writing is not produced by adding academic words to correct grammar. It emerges when the manuscript lets readers reconstruct:

`question/tension -> contribution -> evidence/reasoning -> boundary -> meaning`

At smaller scales, the same principle recurs:

- a section answers a reader question;
- a paragraph develops one necessary reasoning nucleus with supporting moves;
- a sentence inherits something from the current context, performs a relation, adds new information, and enables what comes next.

This is why the repository treats writing as **scientific/rhetorical engineering**, then language realization, rather than template completion.

## 2. Academic writing is a reasoning system before it is a language style

Mensh and Kording's *Ten simple rules for structuring papers* is useful because it explicitly connects writing quality with how readers consume information at several scales: sentence, paragraph, section, and whole document. Its particular Context-Content-Conclusion framework is a heuristic rather than a universal skeleton, but the broader reader-oriented principle transfers well.

The critical writing question is not:

> What sounds academic here?

It is:

> What must the reader understand now for the next scientific move to be justified?

This reframes common editing problems:

- a `transition problem` may actually be a missing logical relation;
- a `wordiness problem` may actually be a hidden multi-step inference;
- a `weak paragraph` may have two competing nuclei;
- a `boring Results section` may follow experiment chronology rather than uncertainty reduction;
- a `generic Discussion` may summarize results without comparing interpretations or boundaries.

## 3. Why fixed templates fail across disciplines

Large cross-disciplinary studies provide strong evidence against one universal paper template.

### Introductions

Lu et al. studied **500 published research-article introductions across five social-science disciplines** and found substantial disciplinary variation in rhetorical move/step distribution and phraseology.

Implication: a fixed four-paragraph Introduction or one mandatory `gap` sentence should not be universalized.

### Methods

Cotos, Huffman, and Link developed the Demonstrating Rigour and Credibility model from **900 Methods texts across 30 academic fields**.

Implication: Methods does more than list procedures. Its rhetorical function is to make the evidence credible and evaluable, but how that is achieved varies by field.

### Abstracts

Omidian and colleagues analyzed **5,910 abstracts across six disciplines** and showed that recurrent expressions vary with rhetorical moves and disciplinary context.

Weinberger, Evans, and Allesina analyzed **more than one million abstracts across eight disciplines**. Their results are especially useful as a warning against uncritically applying popular writing advice: several conventional style recommendations did not show the expected association with citations, and journal context mattered.

Implication: abstract structure and style must be calibrated to article type, discipline, and exact venue rather than one prestige-journal funnel.

### Headings / macrostructure

Large-scale research on section headings has shown substantial field variation and no single broad-field heading set that should be assumed universal.

Implication: IMRaD is common but not a law of academic reasoning.

## 4. The argument spine

Before writing prose, construct five objects:

1. **Question / tension** — what is unresolved, disputed, weakly evidenced, unmeasured, unexplained, unvalidated, or newly possible?
2. **Answer / contribution** — what does this paper establish, provide, clarify, test, synthesize, delimit, or falsify?
3. **Evidence chain** — which observations, analyses, proofs, sources, cases, comparisons, or experiments make the answer credible?
4. **Boundary** — where does the answer hold and where does it stop?
5. **Meaning** — what changes for the intended research community if the bounded answer is true?

Contribution types include more than `novel method`:

- empirical finding;
- mechanism/explanation;
- method/algorithm/instrument;
- dataset/resource/benchmark;
- theory/proof/model;
- replication/validation/robustness;
- negative/null result;
- synthesis/review/taxonomy;
- clinical/practical/policy implication;
- historical/interpretive argument.

A useful manuscript should not disguise an incremental contribution as discontinuous novelty. It should make the increment auditable and explain why it matters.

## 5. Paragraphs as reasoning episodes

A paragraph is more useful to model as **one nucleus plus satellites** than as `exactly one rhetorical function`.

### Nucleus

The proposition, question, result, contrast, problem, or interpretation that makes the paragraph necessary.

### Satellites

Possible supporting moves:

- evidence;
- explanation;
- comparison;
- example;
- qualification;
- counterargument/counterevidence;
- implication;
- methodological reminder;
- bridge.

A paragraph may legitimately contain result + evidence + qualification + implication if they all serve one nucleus.

### Paragraph choreography

A practical representation is:

`nucleus -> support/reasoning -> qualification/alternative if needed -> local inference -> next-reader question`

Not every paragraph needs every slot.

### Paragraph split test

Split a paragraph when:

- two propositions could each independently justify the paragraph's existence;
- evidence starts supporting a different claim;
- scale/population/system changes without an integrating point;
- a qualification becomes an independent argument;
- the reader must retain too many unresolved dependencies.

## 6. Sentence-to-sentence flow

Sentence flow is one of the most important areas for natural scholarly prose.

### The dependency principle

Before polishing a difficult paragraph, reduce it to proposition dependencies:

```text
S1 establishes phenomenon A
S2 restricts A to condition B
S3 explains why B changes interpretation C
S4 tests C against alternative D
S5 closes with bounded inference E
```

Then ask whether sentence order exposes that dependency graph.

### The why-this-sentence-now test

For every sentence after the first:

`inherits X -> relation R -> adds Y -> enables Z`

- **inherits**: what active concept/result/question/condition does the sentence pick up?
- **relation**: evidence, explanation, contrast, consequence, qualification, comparison, inference, etc.?
- **adds**: what new proposition becomes available?
- **enables**: why does this proposition make the next step possible?

A polished sentence that has no meaningful dependency can still make a paragraph feel synthetic.

### Given -> new information

A useful default is:

`A -> B; B -> C; C -> D`

The sentence begins from something sufficiently active for the reader and advances to new information. That new information then becomes available to launch the next sentence.

But given->new is not a mandatory template. Other valid patterns include:

- constant topic: `A -> B; A -> C; A -> D`;
- derived themes: `A -> A1/A2/A3`;
- contrast pair;
- question -> evidence -> answer;
- claim -> evidence -> boundary.

The invariant question is whether the reader can recover why the sequence is ordered this way.

## 7. Cohesion is more than transitions

Empirical cohesion research is especially useful here.

Golparvar, Crosthwaite, and Ziaeian analyzed **100 applied-linguistics research articles** using local, global, and text-level cohesion indices and found significant differences across rhetorical sections.

A later cross-disciplinary study of **300 Discussion sections** across applied linguistics, chemistry, and economics found substantial disciplinary differences in cohesion patterns.

A 2026 mixed-methods study of **64 Chinese EFL students** found that explicit coherence instruction improved writing performance and that higher-performing writers showed stronger **identity-chain development**.

### Identity chains

Readers need stable objects to track:

- exact technical term repetition;
- stable abbreviations;
- explicit noun phrases;
- unambiguous pronouns;
- controlled category/subtype relations;
- precise demonstratives such as `this discrepancy` rather than a vague `this`.

### Why exact repetition can be good

Scientific writing often values referential precision more than literary synonym variation. If `model`, `system`, `framework`, and `approach` are not semantically identical, rotating them to avoid repetition can make the argument harder to track.

Mensh and Kording explicitly recommend consistent word choice for scientific concepts. This aligns with the repository's terminology-ledger and identity-chain approach.

### Transitions

Transitions should encode real relations; they do not create those relations.

`therefore` is only useful if the inference is warranted.

`however` is only useful if there is a real contrast/concession.

`moreover` cannot make unrelated facts part of one argument.

The repository therefore never optimizes connector density.

## 8. Syntax should follow rhetorical function

Good natural scholarly prose is not a random mixture of short and long sentences.

Sentence form should change when the **job** changes.

Examples:

- decisive local result -> direct finite clause;
- qualification -> dependent/subordinate clause when the condition is logically subordinate;
- comparison -> parallel clauses can expose the comparison;
- procedure -> chronological syntax when order matters;
- new cause/mechanism -> explicit clauses often outperform compressed noun stacks;
- established technical concept -> compact nominalization can be efficient;
- contrast -> balanced syntax can expose opposition;
- definition -> keep term and defining property close.

This is **functional syntactic variation**.

Random sentence-length variation is not a writing principle.

## 9. Stance, uncertainty, and author presence

Academic writing is not authorless language. Authors choose methods, interpret results, delimit claims, compare alternatives, and take responsibility for inference.

### Evidence-status categories

Distinguish:

- observed;
- estimated;
- associated;
- experimentally manipulated;
- causally identified;
- simulated;
- inferred;
- hypothesized;
- proved under assumptions;
- interpreted from qualitative/source evidence.

Stance should be calibrated proposition by proposition.

### Human versus LLM stance research

Mo and Crosthwaite compared three LLMs with human academic writers on matched topics and found that the LLMs used a **narrower and more repetitive range of stance and engagement features** than human writers.

The implication is not `add more hedge words`. It is:

> decide what the proposition warrants and what rhetorical relationship with the reader is appropriate here.

### First person

First person is not inherently unacademic. It can clarify responsibility for:

- study decisions;
- analytical choices;
- contribution statements;
- interpretations;
- paper organization.

Its appropriateness is discipline- and genre-sensitive.

Passive/process-centered syntax remains useful when procedure/object should be foregrounded.

## 10. What current research suggests about AI-like academic prose

`AI-like` should be treated as a **quality diagnosis**, not as a detector category.

### Narrow/repetitive stance and engagement

Mo & Crosthwaite (2025) found less varied stance/engagement resources in LLM writing than in matched human writing.

### Standardized expression

Zhao & Lei (2026) found that AI-generated academic abstracts showed more consistent/standardized expression and less variability than human-authored abstracts.

### Flowery or unnecessarily rare academic vocabulary

A 2024 Lingua comparison of ChatGPT-generated and human social-science academic texts reported overuse of infrequent academic vocabulary and excessively flowery language in ChatGPT texts.

### Syntactic template repetition

The same study reported that ChatGPT sometimes produced variation through synonym substitution inside syntactically equivalent structures, while human-authored texts showed greater syntactic complexity through subordination.

The lesson is not `use more subordinate clauses`. The lesson is that **lexical substitution is not rhetorical/syntactic variety**.

### Authorial stance and depersonalization

Recent doctoral-writing research discusses concerns about homogenized stance and weakened authorial identity in AI-assisted academic writing.

Again, the repair is not `use we everywhere`. It is to make consequential authorship/interpretive responsibility visible where it genuinely belongs.

### Repeated machine-like paragraph patterns

A common practical symptom is a manuscript in which each paragraph independently follows:

`generic topic sentence -> broad explanation -> generic implication`

without local evidence dependencies.

The repository attacks this by reconstructing sentence/paragraph dependency first.

## 11. Why word blacklists and detector-oriented rewriting are the wrong goal

Geng and Trotta's 2025 ACL paper on **human-LLM coevolution** documents how the frequency of some words publicly associated with ChatGPT changed after those associations became widely discussed.

This illustrates a fundamental problem with static `AI word` lists: language use changes as humans and models react to one another.

Therefore the repository explicitly rejects:

- AI-word blacklists;
- detector-score optimization;
- deliberate grammar mistakes;
- random short sentences;
- arbitrary punctuation variation;
- random synonym replacement;
- artificial `burstiness`;
- hiding required AI-use disclosure.

The writing-quality criterion is whether every important choice can be explained through:

- logic;
- readability;
- evidence calibration;
- disciplinary convention;
- author voice;
- exact journal/reporting requirements.

## 12. Reading analogue papers

A few near-neighbor papers are extremely valuable, but only if they are read at the right abstraction level.

### Match on

1. research question/contribution class;
2. study design;
3. evidence/data type;
4. article type;
5. subfield/community;
6. exact venue and recent period when available.

Comparability outranks prestige.

### Extract

- how the research need is created;
- contribution positioning;
- evidence dependency sequence;
- what each main figure is supposed to prove;
- what data/controls/uncertainty are visible;
- main text versus Methods/SI placement;
- paragraph/section moves;
- background depth;
- stance/signposting tendencies;
- legitimate counterexamples.

### Do not copy

- sentences;
- distinctive paragraph patterns;
- distinctive figure layouts/palettes;
- normalization/statistical decisions without scientific justification;
- production settings inferred from PDFs.

Analogue papers are **structural/evidence priors**. The author voice remains an independent **expression prior**.

## 13. Figures and data are part of the argument

Scientific figures should be planned as evidence units rather than decorations.

For each major figure ask:

- What question does this figure answer?
- What claim does it support or delimit?
- What is the statistical/sample unit?
- What comparator/control is visible?
- Is uncertainty visible?
- Are individual/raw observations important for interpretation?
- What alternative interpretation does the figure discriminate from?
- Why is this main text rather than SI?

Comparable papers can reveal common **figure roles**—phenomenon, mechanism, validation, generalization, failure boundary—but the final chart type must follow the user's data and estimand.

Do not use a bar chart, heatmap, or UMAP merely because it is common in the venue.

## 14. Section-specific writing

### Title

Encode the durable contribution at the strength the evidence supports. Do not use novelty adjectives as compensation for a vague contribution.

### Abstract

The exact move inventory depends on discipline/article type. The core task is to let the reader recover the question, contribution, decisive evidence, and bounded meaning under the target's structural constraints.

### Introduction

Create a **real research need**, which may be:

- unanswered question;
- contradiction/tension;
- missing mechanism;
- weak/inconclusive evidence;
- measurement/identification problem;
- trade-off/bottleneck;
- missing regime/population;
- replication/robustness need;
- benchmark/resource need;
- theory-data mismatch;
- new opportunity.

Do not manufacture a gap by misrepresenting prior work.

### Methods

Methods demonstrates why the evidence deserves trust. Depending on design, this can involve provenance, sampling, procedure, measurement, controls, analysis, uncertainty, reproducibility, ethics, and assumptions.

### Results

Order evidence by **reasoning dependency / uncertainty reduction**, not necessarily experiment chronology.

For each block:

`question -> evidence -> bounded local inference -> next uncertainty`

### Discussion

A useful repeated cycle is:

`finding -> interpretation -> relation to prior knowledge/alternatives -> qualification -> implication`

Not every finding needs every move.

### Conclusion

Return the post-qualification durable answer. Avoid generic impact language disconnected from the evidence.

## 15. A research-backed manuscript workflow

1. Inventory claims, data, figures, methods, known limitations, and verified literature.
2. Build the argument spine.
3. Classify contribution/evidence type.
4. Study 3–6 close analogues when useful.
5. Build an author-voice profile from representative author prose.
6. Select section move graphs.
7. Build paragraph nuclei + satellites.
8. Allocate evidence across main text/figures/Methods/SI.
9. Build sentence dependency graphs for difficult passages.
10. Repair information progression and identity chains.
11. Calibrate stance to evidence.
12. Realize syntax according to rhetorical function.
13. Add only necessary connectives.
14. Run cadence/read-aloud audit.
15. Re-voice after major structural edits.
16. Run editor/reviewer decision preflight.
17. Apply exact journal/reporting requirements.
18. Run final claim-drift and consistency audit.

## 16. What should remain local rather than universal

Do not universalize:

- exact number/order of Introduction paragraphs;
- structured versus unstructured abstract;
- conclusion-first Results paragraphs;
- amount of first person;
- connector frequency;
- sentence length;
- nominalization density;
- heading structure;
- Discussion sequencing;
- title form;
- number/type of figures;
- graphical style;
- citation density;
- amount of background explanation.

Calibrate these through:

`exact journal/article type + discipline/study design + close analogue papers + author voice`

while preserving scientific validity.

## 17. Research sources

### Cross-disciplinary research-article rhetoric

- Lu, X., Casal, J. E., & Liu, Y. (2021). *Rhetorical and phraseological features of research article introductions: Variation among five social science disciplines*. System. Study corpus: 500 published introductions.
- Cotos, E., Huffman, S., & Link, S. (2017). *A move/step model for methods sections: Demonstrating Rigour and Credibility*. English for Specific Purposes. Study corpus: 900 Methods texts across 30 fields.
- Omidian, T., Shahriari, H., & Siyanova-Chanturia, A. (2018). Research on rhetorical moves/recurrent expressions in 5,910 research abstracts across six disciplines.

### Cohesion / coherence

- Golparvar, S. E., Crosthwaite, P., & Ziaeian, E. (2024). *Mapping cohesion in research articles of applied linguistics: A close look at rhetorical sections*. Journal of English for Academic Purposes, 67, 101316. https://doi.org/10.1016/j.jeap.2023.101316
- Golparvar, S. E., Hu, G., & Seyedi, S. E. (2025). *Cohesion in the discussion section of research articles: A cross-disciplinary investigation*. English for Specific Purposes, 77, 1–19. https://doi.org/10.1016/j.esp.2024.08.004
- *Assessing the effects of explicit coherence instruction on EFL students' integrated writing performance* (2026). Assessing Writing, 67, 101019. https://doi.org/10.1016/j.asw.2026.101019

### AI-generated / AI-assisted academic writing

- Mo, Z., & Crosthwaite, P. (2025). *Exploring the affordances of generative AI large language models for stance and engagement in academic writing*. Journal of English for Academic Purposes, 75, 101499. https://doi.org/10.1016/j.jeap.2025.101499
- *A corpus-driven comparative analysis of AI in academic discourse: Investigating ChatGPT-generated academic texts in social sciences* (2024). Lingua, 312, 103838. https://doi.org/10.1016/j.lingua.2024.103838
- Zhao, N., & Lei, L. (2026). *Informality features in AI-generated academic writing: A corpus-based comparison between human and AI*. Journal of English for Academic Purposes, 79, 101629. https://doi.org/10.1016/j.jeap.2026.101629
- *Reconstructing stance in EFL doctoral thesis writing through generative artificial intelligence* (2025). Humanities and Social Sciences Communications, 12, 1963. https://doi.org/10.1057/s41599-025-06249-x
- Geng, M., & Trotta, R. (2025). *Human-LLM Coevolution: Evidence from Academic Writing*. Findings of ACL 2025, 12689–12696. https://aclanthology.org/2025.findings-acl.657/

### Scientific writing / structure

- Mensh, B., & Kording, K. (2017). *Ten simple rules for structuring papers*. PLOS Computational Biology, 13(9), e1005619. https://doi.org/10.1371/journal.pcbi.1005619
- Weinberger, C. J., Evans, J. A., & Allesina, S. (2015). *Ten Simple (Empirical) Rules for Writing Science*. PLOS Computational Biology, 11(4), e1004205. https://doi.org/10.1371/journal.pcbi.1004205

### Pedagogic reader-flow references

- Harvard College Writing Center, *Transitions*: https://writingcenter.fas.harvard.edu/transitions
- Purdue OWL academic-writing resources: https://owl.purdue.edu/

Use this bibliography as a starting point. The writing system should continue to be updated through new corpus research and direct reading of comparable current papers.
