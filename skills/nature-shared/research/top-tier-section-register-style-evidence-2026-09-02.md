# Top-tier section-register and scholarly-style evidence — 2026-09-02

**Purpose:** evidence ledger for section- and archetype-specific scholarly language. The goal is to learn how expert authors realize different intellectual jobs without copying prose, treating prestige as causal evidence, or flattening all disciplines into one `top-journal style`.

This ledger complements:

- `../core/section-register-and-human-scholarly-style.md`;
- `../core/natural-scholarly-prose.md`;
- `../core/manuscript-section-craftsmanship.md`;
- `../core/analogue-paper-calibration.md`;
- `stratified-paper-reading-2025-2026.md`.

## Research design

Three evidence classes were kept separate because they answer different questions.

### E1 — large genre / corpus evidence

Use this to infer recurrent rhetorical and linguistic distributions across disciplines and sections. It can show variation, common moves, phraseology, stance, agency, and section-specific linguistic behavior. It cannot prove that a frequent pattern is better or caused publication success.

### E2 — official editorial / venue evidence

Use this to resolve actual article-type mechanics and editor-facing writing expectations: structured versus unstructured abstracts, Key Points/Highlights, section labels, word/display budgets, legend roles, and target-specific expectations. Venue rules do not become universal scientific-writing laws.

### E3 — deep reading of real papers

Use this to reconstruct how a successful paper converts a reader question into paragraphs, evidence, formal objects, displays, and transitions. Extract functions and habits, not sentences.

The research model is therefore:

```text
large corpus distributions
+ current venue/editorial rules
+ stratified close reading
-> conditional scholarly-register priors
```

not:

```text
prestigious paper phrase frequency
-> imitate phrase
```

## 1. Large corpus / genre evidence

### 1.1 Introductions vary by discipline at both move and phrase level

**Source:** Lu, Yoon, Kisselev, Casal, Liu, Deng & Nie (2021), *System*, `Rhetorical and phraseological features of research article introductions: Variation among five social science disciplines`, DOI 10.1016/j.system.2021.102543.

**Corpus:** 500 published Research Article Introductions from Anthropology, Applied Linguistics, Political Science, Psychology, and Sociology; manually annotated for rhetorical moves/steps.

**Support:** substantial disciplinary variation occurred both in move/step distributions and in the phraseological realizations associated with those moves.

**Engineering consequence:** CARS-like functions are useful abstractions, but the skill must not force one Introduction paragraph count, one `however`-based gap sentence, or one phrase frame across disciplines.

**Transfer limit:** this is five social-science disciplines, not all science.

### 1.2 Syntactic complexity is linked to rhetorical move and discipline

**Source:** Lu et al. (2021), *Journal of English for Academic Purposes*, `The relationship between syntactic complexity and rhetorical move-steps in research article introductions: Variation among four social science and engineering disciplines`, DOI 10.1016/j.jeap.2021.100971.

**Support:** linguistic form is not independent of rhetorical function; different moves and disciplines show different complexity profiles.

**Engineering consequence:** do not optimize sentence length/complexity globally. A contribution statement, background synthesis, definition, and limitation can legitimately require different syntax.

### 1.3 Methods sections are rhetorical credibility work, not only procedure

**Source:** Cotos, Huffman & Link (2017), *English for Specific Purposes*, `A move/step model for methods sections: Demonstrating Rigour and Credibility`, DOI 10.1016/j.esp.2017.01.001.

**Corpus:** 900 Methods sections from 30 academic fields.

**Support:** Methods contain recurring rhetorical work that demonstrates rigour and credibility, with cross-disciplinary variation.

**Engineering consequence:** a good Methods section may explain or justify consequential design choices rather than mechanically list operations. Procedural density is legitimate; arbitrary `humanizing` variation is not.

### 1.4 Abstract phraseology depends on rhetorical move and discipline

**Source:** Omidian, Shahriari & Siyanova-Chanturia (2018), *Journal of English for Academic Purposes*, `A cross-disciplinary investigation of multi-word expressions in the moves of research article abstracts`, DOI 10.1016/j.jeap.2018.08.002.

**Corpus:** 5,910 abstracts from six disciplines.

**Support:** recurrent word combinations differ by rhetorical move and between hard/soft science disciplines.

**Engineering consequence:** abstract language should be generated from its scientific moves and field, not from one generic `Background—gap—Here we—results—implications` phrase template.

### 1.5 First-person agency is section- and discipline-dependent

**Source:** Gao (2017), cross-disciplinary study of first-person pronouns in research articles across Physics, Computer Science, Linguistics and Management.

**Stable conclusion used here:** first-person frequency and rhetorical function vary materially across disciplines and sections; even traditionally `hard` disciplines can use substantial author agency.

**Engineering consequence:** neither `avoid we` nor `use we to sound human` is defensible as a global rule. Agency follows responsibility, discourse topic, discipline, and target.

### 1.6 Discussion/Conclusion language is especially rhetorically flexible

**Evidence family:** recent cross-disciplinary move/appraisal studies of Research Article Discussion and Discussion/Conclusion sections, including studies sampling hundreds of sections across multiple disciplines.

**Stable conclusion:** Discussion tends to combine evaluation, interpretation, prior-work comparison, explanation, qualification, and implication more recursively than simple result reporting, with substantial disciplinary variation.

**Engineering consequence:** Discussion should not be written as Results plus extra hedges. Its wider stance range and recursive synthesis are legitimate.

### 1.7 No one whole-paper move sequence transfers across engineering fields

**Evidence family:** cross-disciplinary move analyses of full research articles in multiple engineering fields.

**Stable conclusion:** local rhetorical similarities exist, but no single full-paper move pattern captures all fields.

**Engineering consequence:** section registers and archetype overlays should be conditional priors, not compulsory templates.

## 2. AI-versus-human academic-language evidence

### 2.1 LLM stance and engagement can be narrower and more repetitive

**Source:** Mo & Crosthwaite (2025), *Journal of English for Academic Purposes*, `Exploring the affordances of generative AI large language models for stance and engagement in academic writing`, DOI 10.1016/j.jeap.2025.101499.

**Design:** essays generated by three LLMs were compared with human writing on identical topics and annotated using a stance/engagement taxonomy.

**Support:** LLMs generally used a narrower and more repetitive range of stance and engagement resources, with model and discipline variation.

**Engineering consequence:** vary stance because propositions have different epistemic status and rhetorical jobs, not to manufacture surface diversity.

**Transfer limit:** academic essays are not identical to published research articles; this is a diagnostic warning, not an authorship detector.

### 2.2 ChatGPT academic prose can overuse rare/ornamental vocabulary and repeated syntactic frames

**Source:** 2024 *Lingua*, `A corpus-driven comparative analysis of AI in academic discourse: Investigating ChatGPT-generated academic texts in social sciences`, DOI 10.1016/j.lingua.2024.103838.

**Support:** the study reported overuse of infrequent academic vocabulary/flowery language, less human-like formulaic use, greater human syntactic subordination, and synonym substitution inside equivalent syntactic structures.

**Engineering consequence:** remove `prestige vocabulary` optimization and synonym rotation. Functional syntactic variation and conventional field terms are preferable.

**Transfer limit:** one model/time period and social-science corpus; not a universal machine fingerprint.

## 3. Official editorial / venue evidence

### 3.1 Nature Methods: sections have different writing jobs

**Source:** Nature Methods editorial, `So you're writing a paper`, DOI 10.1038/nmeth.4532.

Key support:

- a paper is a selection of data + interpretation for a particular audience, not a chronological record;
- Results and figures are the core evidence surface;
- Results should focus on experimental rationale, observations, and direct interpretation;
- detailed methods normally belong in Methods, with methods papers as an explicit exception;
- Discussion can be more reflective, integrating other work, caveats and future directions;
- legends should describe what is shown rather than become Methods/Discussion;
- direct, simple language is preferred;
- every word should do useful work.

**Engineering consequence:** the same prose register should not be applied to Results, Discussion, Methods and legends.

### 3.2 JAMA: top-tier clinical writing can be highly structured and point-like

**Source:** current JAMA Instructions for Authors, accessed 2026-09-02.

Current Research Article behavior includes:

- structured abstracts for reports of original data;
- a separate Key Points surface organized as `Question`, `Findings`, `Meaning`;
- explicit instruction that parts of structured abstracts may be phrases rather than complete sentences;
- controlled main-text and display budgets;
- reporting-guideline integration.

**Engineering consequence:** fragments, labels and point-like structure are not intrinsically `unhuman` or `AI-like`. If the publication surface is designed for scanability/reporting, terse structured prose can be the expert register.

### 3.3 Cell Press: Highlights are a distinct bullet genre, not a miniature abstract

**Source:** Cell Press/Crosstalk, `Two oft-forgotten items every paper needs`.

Cell Highlights are described as 3–4 result-oriented points, each no more than 85 characters, intended for fast online scanning; the In Brief paragraph instead describes context/significance for a broader audience.

**Engineering consequence:** point form is justified by a distinct reader task and publication surface. Do not generalize Highlights-style bullets into Introduction/Results/Discussion prose.

### 3.4 Nature Physics explicitly rejects generic section/conclusion habits

**Sources:** current `Nature Physics — Content Types`; Nature Physics editorial `Elements of style`.

Current Article guidance:

- up to 3,000 main-text words and six display items;
- generic headings such as `Introduction`, `Results`, `Discussion` should be avoided;
- concluding paragraphs that merely summarize conclusions presented elsewhere are not permitted.

The editorial separately argues that a conclusion should add perspective rather than restate the paper.

**Engineering consequence:** even familiar IMRaD labels and recap Conclusions are not universal markers of professional writing.

## 4. Deep recent-paper reading: section-register cases

The goal of these cases is not to infer a ranking of prose quality. They provide counterexamples and reusable functional observations from strong recent publications.

### 4.1 Nature Cell Biology 2025 — mechanistic experimental narrative

**Paper:** Rawal et al., `Edge curvature drives endoplasmic reticulum reorganization and dictates epithelial migration mode`, Nature Cell Biology 27, 1660–1675 (2025), DOI 10.1038/s41556-025-01729-3.

**Abstract observation:** opens with a biological phenomenon across scales, identifies the unknown mechanism, then progresses through intracellular observation -> force dependence -> mathematical model -> functional migration consequence -> synthesis. The register is narrative but not suspenseful.

**Introduction/Main observation:** field/problem language gives way to a direct `Here, we...` present-paper move and a bounded claim.

**Results observation:** the first subsection begins with a scientific rationale (`to reveal...`), then active experimental actions and observations tied immediately to figures. `We` is frequent because experimental choices are relevant actors. The result narrative is not simply chronological; the rationale tells the reader why the operation exists.

**Discussion observation:** the language changes to present-tense interpretation and mechanism synthesis, integrating prior biological knowledge and caveats.

**Transferable lesson:** mechanism papers can legitimately sound like an increasingly discriminating sequence of questions. Results and Discussion should not have the same rhetorical temperature.

### 4.2 Nature Machine Intelligence 2025 — computational explanation paper

**Paper:** Ursu et al., `Training data composition determines machine learning generalization and biological rule discovery`, Nature Machine Intelligence 7, 1206–1219 (2025), DOI 10.1038/s42256-025-01089-5.

**Abstract observation:** background/problem -> explicit `we examined` question -> synthetic-structure approach -> OOD/ID finding -> ground-truth rule-discovery finding -> experimental validation -> one bounded takeaway. The abstract does not enumerate every benchmark metric.

**Figure-title observation:** main figures use message-like scientific titles: training-data composition determines generalization/rule discovery; classification performance varies with task and data similarity; negative-dataset choice changes learned rules.

**Transferable lesson:** computational papers can read as scientific explanation rather than `architecture -> leaderboard -> ablation`. Display titles and prose organize around scientific questions.

### 4.3 Nature Machine Intelligence 2025 — data-bias/generalization paper

**Paper:** Graber et al., `Resolving data bias improves generalization in binding affinity prediction`, Nature Machine Intelligence 7, 1713–1725 (2025), DOI 10.1038/s42256-025-01124-5.

**Abstract observation:** field need -> specific leakage problem -> proposed curated split -> retraining intervention -> performance drop -> interpretation that prior apparent performance was driven substantially by leakage.

**Transferable lesson:** when dataset construction/bias is the explanation, the prose foregrounds the data-design problem before model details. This is a useful counterexample to architecture-first ML writing.

### 4.4 Scientific Data 2026 — resource/data-descriptor register

**Paper:** Koscova et al., `The Harvard-Emory ECG Database`, Scientific Data 13, 516 (2026), DOI 10.1038/s41597-026-06861-9.

**Abstract/Background & Summary observation:** database identity, scale, population/source, recording format, metadata and use potential are central. Large counts and acquisition details are warranted because **coverage is the scientific object**.

**Technical Validation observation:** the prose becomes procedural/quality-oriented and directly tells users what was checked and what quality control they remain responsible for.

**Important exception:** file/directory names such as metadata files can legitimately appear because the resource organization itself is part of reuse. Generic repository-leakage rules must not delete them automatically.

**Transferable lesson:** resource papers answer trust/reuse questions and can be denser in schemas/files than ordinary empirical Results.

### 4.5 JMLR 2025 — long theory + numerics register

**Paper:** Brugiapaglia, Dexter, Karam & Wang, `Physics-Informed Deep Learning and Compressive Collocation for High-Dimensional Diffusion-Reaction Equations: Practical Existence Theory and Numerics`, JMLR 26(275):1–51 (2025).

**Abstract observation:** historical/problem context -> numerical-analysis gap -> method -> theoretical/numerical comparison -> practical existence theorem and dimension/sample-complexity implication.

**Body observation:** a 51-page formal paper uses explicit roadmaps, Problem Setting, Definitions, Theorems, section cross-references and phrases such as `we start by...` to manage a long dependency chain. These are not defects merely because they are systematic.

**Numerics observation:** theory/proof status and numerical evidence are kept epistemically separate.

**Transferable lesson:** theory writing may require more explicit navigation than short experimental prose. Removing roadmaps/signposts merely to appear `less mechanical` can reduce comprehension.

### 4.6 Nature Physics — structure itself can be topic-led

**Evidence:** current Article format explicitly discourages generic `Introduction`, `Results`, `Discussion` headings and recap-only conclusions.

**Transferable lesson:** a topic-led narrative with integrated interpretation can be fully conventional at an elite venue. Do not treat visible IMRaD labels as a universal quality marker.

### 4.7 JAMA — reporting-oriented clinical surface

**Evidence:** current JAMA original-data instructions plus recent Research Article structure.

**Observed register:** Key Points and abstract are strongly structured; Results emphasize participant denominators, effect estimates, intervals and primary outcomes; Discussion opens directly with the primary finding before interpretation/prior evidence.

**Transferable lesson:** `mechanical precision` can be the correct human scholarly register when the scientific job is transparent clinical reporting. Do not smooth mandatory reporting into a literary narrative.

### 4.8 Cell Press — multiple summary surfaces have different voices

**Evidence:** Cell Press Highlights and In Brief guidance.

**Observed design:** the same paper can legitimately have:

- terse result-only bullets;
- a short context/significance blurb;
- a conventional abstract;
- a graphical abstract.

**Transferable lesson:** human scholarly communication is already multi-register even before entering the main text.

## 5. Stable cross-source conclusions

### A. There is no universal `top-journal voice`

The strongest stable conclusion is conditionality:

```text
section function
x paper archetype
x discipline
x target/article type
x evidence status
x author voice
-> local register
```

### B. `Storytelling` means intellectual dependency

Strong papers often make one scientific operation create the need for the next. This can coexist with highly restrained language.

Do not equate story with drama, promotional language, suspense, or chronological narration.

### C. Human prose varies because intellectual functions vary

Sentence architecture, stance, agency, tense, citation use and density should change for real rhetorical reasons. Random `burstiness`, rare vocabulary, arbitrary synonyms and connector variation are poor substitutes.

### D. Abstract, Results and Discussion should not sound interchangeable

- Abstract: minimum sufficient scientific case.
- Results: evidence-led progression with local inference.
- Discussion: wider interpretive/stance range and prior-work synthesis.

If the same generic paragraph template works in all three, the language model is probably flattening section function.

### E. Formal/procedural writing can legitimately be systematic

Roadmaps, numbered definitions, structured abstract labels, checklists, dense parameter definitions and repeated canonical terminology can all be expert writing when they solve navigation/reporting/reproducibility problems.

### F. Point form is a publication-surface decision

Bullets are appropriate in JAMA Key Points, Cell Highlights, formal assumption lists, algorithmic steps, resource schemas and some review boxes. They are usually inferior when they replace connected causal/inferential reasoning in ordinary Introduction/Results/Discussion prose.

### G. Figures and tables change how much prose is needed

Display-rich empirical papers can use concise prose around inspectable evidence. Theory papers may have few displays but extensive formal exposition. Resource papers often need tables/workflows. Qualitative work may need no figures.

Do not infer a global `figures per 1,000 words` target.

### H. First person is not a humanization toggle

Use author agency when responsibility/choice/interpretation is the rhetorical subject. Use object/process-centered syntax when that better serves the reader. Frequency must be locally calibrated.

### I. A manuscript should change register without changing identity

The same author can be terse in a caption, procedural in Methods, direct in Results and reflective in Discussion. `Author voice` is the stable identity layer above these legitimate register shifts.

## 6. Transfer limits and anti-copy safeguards

1. Publication in a prestigious journal does not prove every stylistic choice is optimal.
2. Corpus frequency is descriptive, not causal evidence for acceptance or readability.
3. Editorial advice from one journal is not automatically a scientific law.
4. The same phraseological move can be appropriate in one field and artificial in another.
5. Deep-reading observations should be generalized to rhetorical functions; do not store reusable sentences, sentence templates, or distinctive phrase strings.
6. Open-access resource papers and reporting-guideline-driven clinical papers are deliberate counterexamples to generic `remove details` and `avoid structured prose` rules.
7. A good style profile must preserve genuine author voice when supplied; analogue papers calibrate community expectations, not identity.
8. No AI detector, perplexity score, sentence-length variance, `burstiness` metric, or word blacklist establishes human authorship or scholarly quality.
9. Copyright-safe extraction records functions and high-level habits, not expressive wording.
10. Exact current target instructions override generic format defaults.

## 7. Engineering consequences for the skill

This research supports:

- `section-register-and-human-scholarly-style.md` as the section/archetype register layer;
- a machine-readable scholarly-register observation profile for long projects;
- progressive disclosure rather than loading all style evidence during every sentence edit;
- one compact always-active invariant: **one author, multiple scholarly registers**;
- section-specific anti-monotone review rather than global sentence-variation scoring;
- explicit exceptions for structured clinical abstracts/Key Points, theory navigation, resource schemas/files and supplementary procedural detail;
- analogue reading that records opening moves, paragraph nuclei, agency, stance, syntax, citation integration, numerical/formal density, list use, display interaction, transitions and closure behavior;
- no copied phrase bank.

## 8. Primary public sources used in this tranche

- Nature Methods, `So you're writing a paper`: https://www.nature.com/articles/nmeth.4532
- Nature Physics, Article content/format: https://www.nature.com/nphys/content
- Nature Physics, `Elements of style`: https://www.nature.com/articles/nphys724
- JAMA, Instructions for Authors: https://jamanetwork.com/journals/jama/pages/instructions-for-authors
- Cell Press/Crosstalk, `Two oft-forgotten items every paper needs`: https://crosstalk.cell.com/blog/two-oft-forgotten-items-every-paper-needs
- Lu et al. (2021), *System*: https://doi.org/10.1016/j.system.2021.102543
- Cotos et al. (2017), *English for Specific Purposes*: https://doi.org/10.1016/j.esp.2017.01.001
- Omidian et al. (2018), *Journal of English for Academic Purposes*: https://doi.org/10.1016/j.jeap.2018.08.002
- Mo & Crosthwaite (2025), *Journal of English for Academic Purposes*: https://doi.org/10.1016/j.jeap.2025.101499
- *Lingua* (2024) ChatGPT/human corpus comparison: https://doi.org/10.1016/j.lingua.2024.103838
- Rawal et al. (2025), Nature Cell Biology: https://doi.org/10.1038/s41556-025-01729-3
- Ursu et al. (2025), Nature Machine Intelligence: https://doi.org/10.1038/s42256-025-01089-5
- Graber et al. (2025), Nature Machine Intelligence: https://doi.org/10.1038/s42256-025-01124-5
- Koscova et al. (2026), Scientific Data: https://doi.org/10.1038/s41597-026-06861-9
- Brugiapaglia et al. (2025), JMLR: https://www.jmlr.org/papers/v26/24-0884.html

This is a living evidence tranche. Future expansion should add counterexamples by field/archetype, not merely more papers from the same prestigious publication ecology.
