# Empirical evidence base for academic writing

This file records the research basis behind the writing skill. It is not a phrase bank. Use it to decide which writing rules are robust, which are discipline-conditioned, and which are only local observations from a small journal corpus.

## Contents

- [Why this evidence layer exists](#why-this-evidence-layer-exists)
- [Large corpus evidence](#large-corpus-evidence)
- [Direct-reading layer](#direct-reading-layer)
- [What the evidence changes in this skill](#what-the-evidence-changes-in-this-skill)
- [Section-specific findings](#section-specific-findings)
- [Sentence and paragraph findings](#sentence-and-paragraph-findings)
- [What not to infer](#what-not-to-infer)
- [Research protocol for future updates](#research-protocol-for-future-updates)
- [Key sources](#key-sources)

## Why this evidence layer exists

A writing skill can fail in two opposite ways:

1. **generic advice** — correct but too vague to help construct a paper;
2. **overfit templates** — concrete but learned from one journal, discipline, or paper type and then incorrectly generalized.

The solution is a layered evidence model:

- large cross-disciplinary corpora establish robust patterns and variation;
- direct reading of recent published papers shows how those moves work in real arguments;
- exact journal guidance controls submission mechanics and house style;
- the author's evidence controls what can actually be claimed.

## Large corpus evidence

### Research article introductions

Lu, Yoon, Kisselev, Casal, Liu, Deng & Nie (2021), *System*, analyzed **500 research-article introductions** across Anthropology, Applied Linguistics, Political Science, Psychology, and Sociology, manually annotating rhetorical move-steps. The main result for this skill is not a universal sequence; it is **substantial disciplinary variation in move distribution and phraseological realization**.

Lu, Casal, Liu, Kisselev & Yoon (2021), *Journal of English for Academic Purposes*, analyzed **400 introductions** from social-science and engineering disciplines and found that syntactic complexity varies by both rhetorical move and discipline. Function and form therefore need to be routed together rather than polishing all sentences toward one generic notion of sophistication.

Zhou, Li & Lu (2023) analyzed **300 science introductions across six disciplines**, again finding that syntactic choices vary systematically by rhetorical move.

### Methods

Cotos, Huffman & Link (2017), *English for Specific Purposes*, developed the **Demonstrating Rigour and Credibility (DRaC)** model from **900 Methods sections across 30 academic fields**. The critical lesson is that Methods are not merely procedural descriptions: their rhetorical purpose includes establishing methodological credibility, and the moves used to do this vary across disciplines.

This evidence directly contradicts treating every Methods section as a computational pipeline of `module -> motivation -> technical advantage`.

### Abstracts

Omidian, Shahriari & Siyanova-Chanturia (2018) analyzed recurrent expressions across rhetorical moves in a corpus of **5,910 research/conference abstracts from six disciplines**, showing that phrase choices and move priorities differ by discipline.

A PLOS ONE discourse study analyzed **500 abstracts across five science domains**. Only **2.4%** used the full five-move Introduction–Purpose–Method–Results–Conclusion sequence. Results were present in **493/500** abstracts, while Purpose was explicit in only **46/500**. The lesson is: results are often central, but a complete five-move abstract is not a universal norm.

Atanassova, Bertin & Larivière analyzed **more than 85,000 PLOS research articles** to study how abstracts relate to full-paper sections. Abstracts draw disproportionately on information appearing near the beginning of Introductions and the end of papers, reinforcing the idea that the abstract is a compressed argument rather than a checklist of every section.

RAAMove (2024) provides **33,988 move-annotated abstract instances**, further supporting move-based rather than sentence-template-based abstraction.

### Whole-paper structure and headings

Thelwall's multidisciplinary heading study analyzed **more than one million research articles** across broad and narrow fields. No heading structure was close to universal across broad disciplines, and humanities papers often diverged substantially from IMRaD-like organization.

This is a direct warning against assuming that `Introduction / Methods / Results / Discussion` or any fixed subsection list is the underlying logical structure of scholarship.

### Titles

Nagano (2015) analyzed **3,200 research-article titles across eight disciplines** and found clear disciplinary conventions. Title form therefore belongs to the discipline/journal/article-type layer, not to a universal formula such as `object + capability + application`.

### Syntactic complexity across sections and disciplines

Casal, Lu and colleagues analyzed syntactic complexity across **240 published social-science research articles** and found significant part-genre and disciplinary variation. Introductions and Discussions, which perform more synthesis and argumentation, often use different complexity resources from Methods and Results.

Additional corpus work comparing professional hard- and soft-discipline articles finds a continuum rather than a single hard/soft binary: phrasal compression is especially prominent in many hard-science texts, while clausal elaboration is more productive in many soft disciplines.

The writing implication is important: **do not blindly shorten sentences** and do not equate longer or denser syntax with poor writing. Diagnose whether the syntax makes the rhetorical relation easier or harder to recover.

### Discussion sections

Move studies of Discussion sections repeatedly show recursive patterns involving result reporting/restatement, interpretation, comparison with literature, explanation, implication, limitation and future direction. Recent work also finds differences between qualitative and quantitative research in how these moves and metadiscourse are realized.

A 2025 corpus of **200 applied-linguistics Discussions** found move-specific syntactic differences and differences between Chinese and native-English published writing. The useful conclusion is not to imitate a nationality-specific surface style; it is to connect sentence form to rhetorical function and to avoid over-compressed nominal syntax when it obscures interpretation.

### Cohesion and information flow

Corpus and discourse research treats cohesion at sentence, paragraph, section and whole-text levels. Useful mechanisms include:

- given-to-new information progression;
- lexical chains that keep central entities trackable;
- clear reference/pronoun chains;
- explicit logical relations where readers cannot infer them safely;
- paragraph-to-paragraph chain links.

Importantly, more local connectives do **not** automatically mean better writing. Mature prose can have strong global coherence with relatively few overt transition words because topic progression, lexical continuity and argument structure already make the relation clear.

## Direct-reading layer

Large corpora tell us what varies; direct reading shows how expert authors execute the logic.

The repository already contains a manually curated 2025 reading set of **20 open-access Nature Communications CS/AI papers** in `nat-comms-2025-corpus.md`. That corpus is useful as a **local journal/field profile**, not a universal writing law.

The broader direct-reading layer now includes representative recent papers across different publication ecologies, for example:

- *Nature Machine Intelligence*: multimodal materials-LLM work in which the Results repeatedly move from evaluation to ablation, external generalization and interpretability, while the Discussion re-integrates those evidence strands rather than simply repeating figures.
- *npj Computational Materials*: an AI-accelerated superconductor-discovery paper whose Results interleave computational prediction, disorder analysis, synthesis, diffraction and low-temperature measurements; its Discussion re-opens the field problem and then reconstructs the contribution around progressive filtering and experimental confirmation.
- *PLOS ONE*: a clinical-ML proof-of-principle paper whose Introduction spends substantial space defining clinical phenotype, motivating personalized treatment, giving real clinical examples, establishing the limitations of conventional analysis, and only then stating the simulated-RCT study. Its Results use a sequential inferential narrative rather than a short conclusion-first Nature-style paragraph template; the Discussion cycles through main finding, contrast, qualification and recommendation.
- recent open materials, psychology, behavioral-health and public-health papers used to check how theory, population, methods and interpretation change the writing rhythm.

These readings reinforce three principles:

1. **good papers create local reasons for the next analysis**;
2. **Results sequencing follows the evidence-generating logic**, not one journal's preferred paragraph opening;
3. **Discussion often revisits findings recursively**, with interpretation and qualification attached to each major claim.

## What the evidence changes in this skill

### Previous rule: one paragraph = exactly one job

Replaced by:

> one paragraph = one **nucleus** plus supporting submoves.

Published paragraphs commonly combine a main claim with evidence, explanation, comparison, qualification and a bridge. Split only when there are two independent nuclei.

### Previous rule: default four-paragraph Introduction funnel

Replaced by a move inventory. Introductions can create a research need through an unanswered question, contradiction, missing mechanism, weak evidence, methodological bottleneck, missing population/scale, replication need, theory-data mismatch or new opportunity. A generic `few studies / however / gap` formula is not required.

### Previous rule: Methods = pipeline modules

Restricted to algorithmic/method-heavy subtypes. General Methods planning now focuses on design, materials/data/population, procedure, analysis, controls, validation, uncertainty, ethics and reproducibility, with rationale attached to consequential choices.

### Previous rule: Results should be conclusion-first

Downgraded from universal rule to a venue/field option. The robust unit is:

`question -> setup if needed -> observation/estimate -> evidence -> bounded local inference -> bridge`

Different disciplines decide whether interpretation belongs locally in Results or mainly in Discussion.

### Previous rule: Discussion widens once from result to meaning

Replaced by recursive finding-centered cycles plus paper-level integration and limitations.

### Previous rule: a good abstract should contain a fixed six-move funnel

Replaced by genre/field-aware move selection. The abstract must communicate the paper's highest-value information under the target word budget; full five-move coverage is uncommon in some corpora.

## Section-specific findings

### Introductions

Robust across many fields:

- readers need enough territory/context to understand why the question matters;
- a live research need must be created;
- prior work must be synthesized to position the present response;
- the paper must eventually state what it does.

Variable:

- how early the paper states the research question;
- whether the need is framed as a `gap`;
- number of literature paragraphs;
- how much theory is developed;
- whether results/contributions are previewed;
- degree of explicit self-reference (`we`, `this study`).

### Methods

Robust:

- enough information to understand how evidence was generated;
- credibility/rigour of consequential design choices;
- reproducibility appropriate to the field.

Variable:

- chronological versus conceptual organization;
- amount of rationale;
- whether implementation details sit in main text, appendix, supplement or repository;
- role of equations, protocols, coding frameworks, apparatus descriptions or participant procedures.

### Results

Robust:

- actual evidence must be recoverable;
- the reader should know what question each result answers;
- comparisons must have a clear reference/baseline;
- uncertainty and sample definitions belong near the quantitative claim when relevant.

Variable:

- degree of commentary;
- claim-first versus observation-first paragraphs;
- whether Methods reminders are embedded;
- whether Results and Discussion are combined.

### Discussion

Robust:

- interpretation;
- relation to prior knowledge or alternatives;
- bounded claims;
- implications proportional to evidence.

Variable:

- whether limitations have a dedicated subsection;
- how often previous results are restated;
- how much future work is included;
- stance/metadiscourse conventions.

## Sentence and paragraph findings

The evidence supports a functional approach:

- sentence complexity should match the rhetorical move;
- keep old/given information sufficiently early when it helps readers attach the sentence;
- use stable lexical chains for core concepts;
- reserve the strongest emphasis for the sentence's real new contribution;
- choose active/passive voice for information structure and agency, not because one sounds more academic;
- use connectives to expose non-obvious logic, not as decoration;
- avoid noun-stack compression when readers must unpack a new causal or conceptual relation.

## What not to infer

Do not conclude that:

- frequent patterns are mandatory;
- high-impact journals are automatically better writing models for every field;
- corpus frequency proves a sentence is rhetorically effective in the user's paper;
- native-English published writing provides a moral or intellectual quality standard;
- a disciplinary norm should override accuracy, ethics, reporting standards or accessibility;
- one year's corpus permanently defines a journal.

Corpus patterns are priors. The exact paper and evidence remain the final test.

## Research protocol for future updates

When extending the writing skill:

1. **Stratify the corpus** by discipline, paper type, journal/venue and year.
2. **Read complete rhetorical units**, not isolated sentences.
3. Annotate at least: section, move, submove, paragraph nucleus, sentence relation, evidence type, stance, and section-to-section handoff.
4. Separate **frequency** from **effectiveness**. A common phrase may be conventional but weak.
5. Record counterexamples and legitimate alternative structures.
6. Never copy published prose into reusable templates; abstract the function and structure.
7. Validate a proposed rule against papers outside the corpus that generated it.
8. Promote a rule to the core only if it survives cross-disciplinary testing; otherwise keep it in a journal/discipline profile.
9. Re-check recent papers because house style and publication practices evolve.
10. Add regression tests when a research finding changes a router or core contract.

## Key sources

- Lu, X. et al. (2021). *Rhetorical and phraseological features of research article introductions: Variation among five social science disciplines*. **System 100**, 102543. DOI: `10.1016/j.system.2021.102543`.
- Lu, X. et al. (2021). *The relationship between syntactic complexity and rhetorical move-steps in research article introductions: Variation among four social science and engineering disciplines*. **Journal of English for Academic Purposes 52**, 101006.
- Zhou, W., Li, Z. & Lu, X. (2023). *Syntactic complexity features of science research article introductions: Rhetorical-functional and disciplinary variation perspectives*. **Journal of English for Academic Purposes 61**, 101212.
- Cotos, E., Huffman, S. & Link, S. (2017). *A move/step model for methods sections: Demonstrating Rigour and Credibility*. **English for Specific Purposes**. DOI: `10.1016/j.esp.2017.01.001`.
- Omidian, T., Shahriari, H. & Siyanova-Chanturia, A. (2018). *A cross-disciplinary investigation of multi-word expressions in the moves of research article abstracts*. **Journal of English for Academic Purposes 36**, 1–14. DOI: `10.1016/j.jeap.2018.08.002`.
- *A discourse analysis of the macro-structure, metadiscoursal and microdiscoursal features in the abstracts of research articles across multiple science disciplines*. **PLOS ONE 13(10)**, e0205417. DOI: `10.1371/journal.pone.0205417`.
- Atanassova, I., Bertin, M. & Larivière, V. (2016). *On the Composition of Scientific Abstracts*. corpus of more than 85,000 PLOS articles.
- Thelwall, M. (2019). *The rhetorical structure of science? A multidisciplinary analysis of article headings*. analysis of more than one million PMC Open Access research articles.
- Nagano, R. L. (2015). *Research Article Titles and Disciplinary Conventions: A Corpus Study of Eight Disciplines*. **Journal of Academic Writing 5(1)**, 133–144. DOI: `10.18552/joaw.v5i1.168`.
- Casal, J. E., Lu, X. et al. (2021). *Syntactic complexity across academic research article part-genres: A cross-disciplinary perspective*. **Journal of English for Academic Purposes 52**, 100996. DOI: `10.1016/j.jeap.2021.100996`.
- Golparvar et al. (2024). *Mapping cohesion in research articles of applied linguistics: A close look at rhetorical sections*. **Journal of English for Academic Purposes 67**, 101316. DOI: `10.1016/j.jeap.2023.101316`.
- *Creating Logical Flow When Writing Scientific Articles*. **Journal of Korean Medical Science 36**, e275 (2021).
- *Strategic Paragraphing 2.0: Techniques for Enhancing Inter-Paragraph Coherence* (given-new and chain-link paragraph progression).

Treat this bibliography as a research trail, not a closed canon. New evidence should update the skill when it changes the operational writing rules.