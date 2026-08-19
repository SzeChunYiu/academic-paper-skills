---
name: nature-writing
description: Draft, restructure, or plan journal-aware academic manuscripts from author-provided claims, results, figures, notes, sources, or Chinese drafts. The legacy skill name is retained for compatibility, but core writing is evidence-first, rhetorical-move-based, cross-disciplinary, and independent of Nature style. Use for titles, abstracts, introductions, related work, Methods, Results/experiments, Discussions, Conclusions, full-paper argument architecture, paragraph/sentence logic, target-journal corpus calibration, journal transfer, and initial-submission packages. Also use to map claim-to-evidence logic, sequence analyses, diagnose flow, distinguish observation from interpretation, preserve uncertainty and contribution boundaries, learn current rhetorical patterns from comparable published papers without copying wording, allocate material across main text/captions/Methods/SI, and prevent revision accretion. Supports Nature Portfolio, Science/AAAS, Cell Press, IEEE, ACM, PLOS, Springer/BMC, Elsevier, Wiley, society journals, discipline-specific venues, and unknown targets through the journal resolver. Trigger on academic writing, paper drafting, manuscript structure/logic, 学术写作、科研写作、论文写作、论文逻辑、段落逻辑、论文结构、期刊写作、投稿写作.
---

# Journal-Aware Academic Writing — Router

`nature-writing` is a legacy entry-point name. It does **not** define the target journal, discipline, evidence standard, or rhetorical skeleton.

The writing system has three layers:

- **core reasoning** under `static/core/`: evidence/claim stance, rhetorical engine, writing workflow, output contract;
- **selective fragments/references**: paper type, section, language, journal routing, cross-disciplinary move atlas, empirical corpus evidence, examples;
- **dynamic calibration**: when target style matters, study a comparable recent paper corpus and derive a temporary rhetorical profile without copying published prose.

Shared exact-journal resolution lives under `../nature-shared/journal-formats/`. Exact live author instructions outrank local profiles for submission-critical requirements.

Do not draft from remembered prestige style. Load the routed files.

## Routing protocol

### 1. Load manifest and core

Read [manifest.yaml](manifest.yaml), then every file under `always_load`.

The rhetorical engine is core: plan the paper as reader-facing moves before choosing sentence forms.

### 2. Resolve task axes

Detect:

- `task` — manuscript / submission-package;
- `paper_type` — research / methods / hypothesis / algorithmic / review;
- `section` — abstract / intro / related-work / method / experiments / discussion / conclusion / title; may be multiple;
- `language` — en / zh-to-en;
- `journal` — nature / nature-family / nat-comms / nat-mach-intell / profiled / generic.

For the journal axis:

- `nature` = flagship **Nature** only;
- `nat-comms` = **Nature Communications** only;
- `nat-mach-intell` = **Nature Machine Intelligence** only;
- `nature-family` = another Nature Portfolio title or unresolved Nature-family request;
- `profiled` = any named non-Nature journal/venue/family or journal transfer;
- `generic` = no useful target known.

Ask only when ambiguity would materially change the scientific argument or compliance result. Otherwise choose the safest generic route and state important assumptions.

### 3. Load only relevant fragments

Read each selected axis fragment. Do not preload the entire reference library.

For `journal=profiled`, resolve as needed:

`exact journal -> article/content type -> submission stage -> component`

using `../nature-shared/journal-formats/journal-resolution.md` and current official instructions when exact compliance matters.

### 4. Plan and draft in this priority order

#### A. Evidence and claim integrity

Use `static/core/stance.md` and author-provided material. Never invent results, mechanisms, references, uncertainty, novelty, or limitations.

#### B. Rhetorical engine

Use `static/core/rhetorical-engine.md` to build:

`question/tension -> answer/contribution -> evidence chain -> boundary -> meaning`

Classify contribution/evidence type. Do not force unrelated contributions into one inflated novelty sentence.

#### C. Discipline and paper type

Apply the paper-type fragment and research paradigm. A theorem paper, clinical cohort, qualitative interview study, benchmark paper, materials experiment, and historical argument need different evidence/rhetoric even in the same publisher family.

#### D. Section move map

Apply the selected section fragment. If the material does not fit its local default or cross-disciplinary calibration matters, load `references/section-move-atlas.md`.

Plan sections as move graphs. Moves can recur or embed; they are not a one-use checklist.

#### E. Paragraph and sentence logic

Use one paragraph **nucleus** plus necessary satellites (evidence, explanation, comparison, qualification, counterargument, implication, bridge). Do not require every paragraph to perform exactly one rhetorical function.

For flow problems, load `references/paragraph-flow.md` and repair in order:

`structure -> relation -> given/new information -> lexical/reference continuity -> sentence form -> connectives`

Do not use transition words to mask a missing logical relation.

#### F. Results evidence allocation

For Results/full manuscript compression, load `../nature-shared/core/main-text-discipline.md`. Build the shortest sufficient evidence chain while keeping conclusion-changing qualifications visible.

Sequence evidence by reasoning dependency—why analysis B becomes necessary after A—not merely chronological experiment order.

#### G. Target-corpus calibration when requested/useful

If the user asks to write like current papers in a named venue/field, or the target has no reliable local profile, load `references/target-corpus-calibration.md`.

For a quick profile, inspect a comparable recent sample rather than one showcase paper. Stratify by article type/study design. Learn:

- argument and evidence sequence;
- section moves;
- paragraph nuclei/satellites;
- sentence information structure and stance;
- where interpretation, limitations, citations and figure calls occur.

Never create reusable full-sentence templates from copyrighted papers. Learn **moves and relations, not wording**.

For dozens/hundreds of extracted `.md`/`.txt` papers, use `scripts/corpus_structure_stats.py` for descriptive surface statistics, then add semantic move annotation. Corpus frequency is not a writing-quality score.

#### H. Reporting and journal compliance

Apply research-reporting obligations and exact journal/content-type/stage rules. Family profiles are fallbacks, not exact contracts.

#### I. Language polish last

Only after logic is sound, apply language-specific sentence/paragraph guidance. Do not make prose more causal, general, or certain to sound prestigious.

### 5. Reach for evidence/reference layers on demand

Use the manifest's `references.on_demand` table. Important routes include:

- cross-disciplinary section logic -> `references/section-move-atlas.md`;
- empirical basis behind writing rules -> `references/cross-disciplinary-writing-evidence.md`;
- current target-paper corpus learning -> `references/target-corpus-calibration.md`;
- whole-paper architecture -> `references/article-architecture.md`;
- Introduction logic -> `references/introduction.md`;
- Methods credibility/reproducibility -> `references/method.md`;
- paragraph/sentence coherence -> `references/paragraph-flow.md`;
- local 2025 Nature Communications CS/AI calibration -> `references/nat-comms-2025-corpus.md` (local profile only, never universal);
- concrete examples -> `references/examples/index.md`;
- self-review/claim-evidence audit -> `references/paper-review.md`;
- main-text versus captions/SI -> `../nature-shared/core/main-text-discipline.md`.

## Dynamic learning rule

Published papers are evidence about **how writers solved rhetorical problems under particular conditions**. They are not text templates and not automatic best practice.

When learning from papers:

1. sample comparable papers, not only famous ones;
2. annotate complete rhetorical units, not isolated attractive sentences;
3. distinguish cross-disciplinary invariants from discipline/journal/author tendencies;
4. record legitimate counterexamples;
5. separate frequency from effectiveness;
6. validate a proposed core rule outside the corpus that generated it;
7. keep exact journal mechanics separate from observed writing practice.

## Submission boundary

- `nature-writing` owns manuscript drafting and **initial submission** materials before peer review.
- `nature-response` owns post-decision rebuttals, revision cover letters, marked manuscripts and appeals.
- graphical abstracts/TOC graphics -> `nature-figure`;
- simulated pre-submission peer review -> `nature-reviewer`.

## Non-negotiable writing rules

- Evidence quality and study design determine claim strength; journal prestige does not.
- A research need need not be a manufactured `gap`.
- Strong prior work should be represented fairly.
- Do not hide incrementality to make a contribution appear larger.
- Do not force IMRaD, conclusion-first Results, pipeline Methods, a fixed abstract funnel, or one-function paragraphs across disciplines.
- Do not equate more connectives, shorter sentences, denser noun phrases, or more assertive verbs with better academic writing.
- Exact live journal requirements outrank local formatting profiles; scientific validity outranks all house style.

## Why this architecture

- The core stores rules that survived cross-disciplinary testing.
- Discipline/journal corpora remain local evidence layers rather than contaminating the universal engine.
- Dynamic calibration lets the skill learn current practice without hard-coding thousands of journals.
- Regression tests protect the distinction between rhetorical logic and surface imitation.
