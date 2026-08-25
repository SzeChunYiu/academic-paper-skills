---
name: nature-writing
description: Draft, restructure, or plan journal-aware academic manuscripts from author-provided claims, results, figures, notes, sources, or Chinese drafts. The legacy skill name is retained for compatibility, but core writing is evidence-first, rhetorical-move-based, cross-disciplinary, and independent of Nature style. Use for titles, abstracts, introductions, related work, Methods, Results/experiments, Discussions, Conclusions, full-paper argument architecture, paragraph/sentence logic, natural scholarly prose, target-journal corpus calibration, analogue-paper study, author-voice preservation, editor/reviewer preflight, acceptance-readiness engineering, journal transfer, and initial-submission packages. For substantial rewrites, study a few genuinely comparable papers to learn how similar work frames the problem, sequences evidence, chooses main figures/data displays, plots key comparisons, and allocates material between main text and SI, while preserving a separate author-voice profile so the final manuscript remains recognizably the author's own writing. Also use to repair prose that feels generic, formulaic, over-smoothed, machine-like, repetitive, connector-heavy, or difficult to follow sentence by sentence by reconstructing proposition dependencies, given/new progression, identity chains, local stance, functional syntax, and cadence. Never optimize prose for AI-detector evasion. Supports Nature Portfolio, Science/AAAS, Cell Press, IEEE, ACM, PLOS, Springer/BMC, Elsevier, Wiley, society journals, discipline-specific venues, and unknown targets through the journal resolver. Trigger on academic writing, paper drafting, manuscript structure/logic, natural writing, sentence flow, human-sounding academic prose, similar papers, reference papers, editor perspective, reviewer perspective, acceptance readiness, 学术写作、科研写作、论文写作、自然学术表达、句间逻辑、段落逻辑、论文结构、参考相似论文、期刊写作、投稿写作、编辑视角、审稿人视角.
---

# Journal-Aware Academic Writing — Router

`nature-writing` is a legacy entry-point name. It does **not** define the target journal, discipline, evidence standard, rhetorical skeleton, editorial objective, or prose style.

The writing system has six layers:

- **core reasoning** under `static/core/`: evidence/claim stance, rhetorical engine, writing workflow, output contract;
- **selective fragments/references**: paper type, section, language, journal routing, cross-disciplinary move atlas, empirical corpus evidence, examples;
- **analogue-paper + author-voice calibration**: close-read a few similar papers for structural/evidence/figure priors while separately preserving the author's own expression profile;
- **natural scholarly prose**: realize the scientific reasoning sentence by sentence with recoverable dependencies, information flow, identity chains, calibrated stance, functional syntax, and non-mechanical cadence;
- **dynamic corpus calibration**: when broader target-style inference matters, study a larger comparable recent corpus without copying prose;
- **decision preflight**: before submission, model exact target criteria, editorial triage, reviewer objections, and minimum-sufficient repair routes.

Shared exact-journal resolution, analogue calibration, author voice, natural scholarly prose, and decision logic live under `../nature-shared/`. Exact live author/editor/reviewer instructions outrank local profiles for submission-critical requirements.

Do not draft from remembered prestige style. Do not try to make text `look human` by adding noise. Load the routed files.

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

If the user asks how to improve acceptance-readiness, desk-review survival, editor/reviewer perception, or likely rejection risk, also load:

- `../nature-shared/core/editor-reviewer-decision-engine.md`;
- `../nature-shared/journal-formats/editorial-decision-profiles.md` when the exact publication objective needs fallback calibration;
- `references/editor-reviewer-preflight.md`.

If the user says the prose feels `AI-written`, generic, unnatural, over-smoothed, repetitive, choppy, connector-heavy, or difficult to follow sentence by sentence, load:

- `../nature-shared/core/natural-scholarly-prose.md`;
- `references/paragraph-flow.md` when local coherence is part of the problem;
- `../nature-shared/core/author-voice-profile.md` when author-provided prose is available for voice recovery.

### 4. Plan and draft in this priority order

#### A. Evidence and claim integrity

Use `static/core/stance.md` and author-provided material. Never invent results, mechanisms, references, uncertainty, novelty, or limitations.

For full manuscripts, theory/proof sections, public-posting/submission readiness,
or decision-relevant rewrites, load
`../nature-shared/core/atomic-claim-verification.md`. Atomize every scientific
assertion, verify the actual warrant rather than the presence of a pointer, and
fail closed on unresolved or contradicted content.

#### B. Rhetorical engine

Use `static/core/rhetorical-engine.md` to build:

`question/tension -> answer/contribution -> evidence chain -> boundary -> meaning`

Classify contribution/evidence type. Do not force unrelated contributions into one inflated novelty sentence.

#### C. Discipline and paper type

Apply the paper-type fragment and research paradigm. A theorem paper, clinical cohort, qualitative interview study, benchmark paper, materials experiment, and historical argument need different evidence/rhetoric even in the same publisher family.

#### D. Analogue-paper study + author voice for substantial rewrites

When rewriting/restructuring more than a tiny local passage and the field, contribution class, or target is known, load `../nature-shared/core/analogue-paper-calibration.md`.

Study a few **near-neighbor papers** matched by research question/contribution class, study design, data/evidence type, article type, subfield/audience, and target venue when possible. Comparability outranks prestige.

Extract:

- research-need construction and contribution placement;
- section and paragraph move patterns;
- why one evidence block leads to the next;
- what data/evidence are visible in main text;
- what the main figures are *for*;
- how similar papers display controls, uncertainty, raw observations, validation, generalization, mechanism, and failure boundaries;
- what is moved to Methods/SI/Extended Data;
- local expectations for background depth, signposting, citations, and interpretation.

For figure/plot questions, route to `nature-figure` and its `references/analogue-figure-calibration.md`; writing may still use the analogue study to plan the figure's **scientific role and evidence dependency**.

Do not copy wording, distinctive paragraph architecture, figure layouts, visual identity, normalization/statistical choices, or production dimensions.

If the user supplied representative prose or asks to keep their style, also load `../nature-shared/core/author-voice-profile.md`. Build a compact profile from the author's own material, separating:

- **voice invariants** — cadence, agency, technical directness, signposting level, terminology, epistemic rhythm;
- **flexible traits** — sentence/paragraph length, transitions, heading form, context amount, local compression.

Then use this hierarchy:

`author evidence = truth constraint`

`journal rules = compliance constraint`

`analogue papers = structural/evidence priors`

`author voice = expression prior`

Skip or bound the analogue pass for tiny edits, layout-only work, or when no reliable comparable papers are available.

#### E. Section move map

Apply the selected section fragment. If the material does not fit its local default or cross-disciplinary calibration matters, load `references/section-move-atlas.md`.

Plan sections as move graphs. Moves can recur or embed; they are not a one-use checklist.

#### F. Paragraph and sentence logic

Use one paragraph **nucleus** plus necessary satellites (evidence, explanation, comparison, qualification, counterargument, implication, bridge). Do not require every paragraph to perform exactly one rhetorical function.

For flow problems, load `references/paragraph-flow.md` and repair in order:

`section structure -> paragraph nucleus -> sentence dependency -> relation -> information progression -> identity chain -> topic/emphasis -> syntax -> connectives -> cadence`

For every non-initial sentence in a difficult paragraph, run:

`inherits X -> relation R -> adds Y -> enables Z`

If the sentence inherits nothing and its only link is a generic connector, investigate structure rather than polishing the connector.

#### G. Natural scholarly prose realization

Before final language polish, load `../nature-shared/core/natural-scholarly-prose.md` for substantial drafting/rewrite jobs or whenever prose has become generic/machine-like.

The quality hierarchy is:

`scientific relation -> information flow -> lexical/reference continuity -> stance -> syntax -> connective -> cadence`

Operational rules:

1. Strip difficult passages to proposition-level content before rephrasing.
2. Label why each sentence follows the previous one.
3. Use given->new progression as a useful default, not a rigid template; choose constant-topic, derived-theme, contrast, question-answer, or claim-evidence-boundary progression when the reasoning requires it.
4. Build lexical/reference **identity chains** so central entities remain trackable.
5. Repeat canonical technical terms when the referent is unchanged; do not rotate synonyms merely to avoid repetition.
6. Calibrate stance proposition by proposition from the evidence.
7. Vary sentence structure **because rhetorical function varies**, not to manufacture human-like randomness.
8. Use first-person, passive, or process-centered syntax according to agency/focus and discipline—not according to a global preference.
9. Add connectives only when a real relation needs to be made explicit.
10. Run a cadence/read-aloud pass only after the reasoning is correct.
11. Re-voice after structural/natural-prose repairs so the manuscript remains recognizably the author's.
12. Recheck scientific drift after every naturalization pass.

### What `avoid AI writing` means in this skill

It means avoid **generic machine-like failure modes** documented in academic-writing research:

- narrow/repetitive stance and engagement;
- standardized cadence without functionally meaningful variation;
- ornamental/rare academic vocabulary chosen for prestige rather than precision;
- synonym substitution inside repeated syntactic frames;
- depersonalized prose that erases consequential authorial decisions;
- connector stuffing;
- generic prestige claims that replace concrete scientific consequences;
- repeated paragraph templates and generic closings.

It does **not** mean:

- maintain an `AI word` blacklist;
- optimize an AI-detector score;
- deliberately add grammar mistakes, fragments, odd punctuation, slang, or typos;
- randomize sentence length or vocabulary to create `burstiness`;
- conceal required AI-use disclosure.

Research on human-LLM coevolution shows why static word signatures are unstable. Judge prose by relation, specificity, collocation, evidence, reader path, and authentic author voice.

#### H. Results evidence allocation

For Results/full manuscript compression, load `../nature-shared/core/main-text-discipline.md`. Build the shortest sufficient evidence chain while keeping conclusion-changing qualifications visible.

Sequence evidence by reasoning dependency — why analysis B becomes necessary after A — not merely chronological experiment order.

Use analogue papers as a **placement prior**, not a placement rule. Final main-text/SI allocation follows the function of the evidence in this paper and exact target requirements.

#### I. Editor/reviewer decision preflight before final submission polish

When acceptance-readiness or rejection-risk matters, do this **before** target-style polishing.

1. Resolve the exact publication model and verified decision criteria.
2. Build the compact editor decision brief: question, answer, decisive evidence, target-specific value, boundary, intended community.
3. Build a decision proof for every headline claim.
4. Run the atomic verification contract across definitions, claims, proofs,
   numbers, sources, availability statements, and cross-section restatements.
5. Simulate editorial triage separately from external reviewers.
6. Stress-test the manuscript with independent validity, positioning/significance, and reproducibility/boundary lenses.
7. Classify risks as target-fit blockers, technical blockers, major repairable, claim recalibration, clarity/reporting, or optional enrichment.
8. Select the minimum scientifically sufficient repair:
   - add decisive evidence;
   - reanalyse existing evidence;
   - correct an error;
   - clarify/restructure existing evidence;
   - narrow the claim;
   - remove the claim;
   - change target/article type when the science is sound but the editorial objective is mismatched.

Do not assume more experiments are always the correct answer. A target-fit problem may require transfer; an over-broad secondary claim may be better removed; a missed existing control may require restructuring rather than new data.

#### J. Larger target-corpus calibration when requested/useful

If the user asks to characterize current writing patterns across a target field/venue beyond a few close analogues, load `references/target-corpus-calibration.md`.

Use the **analogue pass** for close reading of a handful of nearest neighbors and the **target-corpus pass** for broader distributions/tendencies. Do not confuse them.

For a broader profile, stratify by article type/study design. Learn:

- argument and evidence sequence;
- section moves;
- paragraph nuclei/satellites;
- sentence information structure and stance;
- where interpretation, limitations, citations and figure calls occur.

Never create reusable full-sentence templates from copyrighted papers. Learn **moves and relations, not wording**.

For dozens/hundreds of extracted `.md`/`.txt` papers, use `scripts/corpus_structure_stats.py` for descriptive surface statistics, then add semantic move annotation. Corpus frequency is not a writing-quality score.

#### K. Reporting and journal compliance

Apply research-reporting obligations and exact journal/content-type/stage rules. Family profiles are fallbacks, not exact contracts.

#### L. Final language polish

Only after logic, evidence, natural-prose realization, voice restoration, and decision-readiness are sound, apply language-specific sentence/paragraph guidance. Do not make prose more causal, general, important, novel, or certain to sound prestigious.

### 5. Reach for evidence/reference layers on demand

Use the manifest's `references.on_demand` table. Important routes include:

- natural scholarly expression / machine-like prose repair -> `../nature-shared/core/natural-scholarly-prose.md`;
- close analogue-paper study -> `../nature-shared/core/analogue-paper-calibration.md`;
- author voice preservation/re-voicing -> `../nature-shared/core/author-voice-profile.md`;
- editor/reviewer decision logic -> `../nature-shared/core/editor-reviewer-decision-engine.md`;
- publication-model differences -> `../nature-shared/journal-formats/editorial-decision-profiles.md`;
- author-facing acceptance-readiness preflight -> `references/editor-reviewer-preflight.md`;
- cross-disciplinary section logic -> `references/section-move-atlas.md`;
- empirical basis behind writing rules -> `references/cross-disciplinary-writing-evidence.md`;
- broader target-paper corpus learning -> `references/target-corpus-calibration.md`;
- whole-paper architecture -> `references/article-architecture.md`;
- Introduction logic -> `references/introduction.md`;
- Methods credibility/reproducibility -> `references/method.md`;
- paragraph/sentence coherence -> `references/paragraph-flow.md`;
- local 2025 Nature Communications CS/AI calibration -> `references/nat-comms-2025-corpus.md` (local profile only, never universal);
- concrete examples -> `references/examples/index.md`;
- self-review/claim-evidence audit -> `references/paper-review.md`;
- fail-closed full-manuscript/formal-claim verification -> `../nature-shared/core/atomic-claim-verification.md`;
- main-text versus captions/SI -> `../nature-shared/core/main-text-discipline.md`.

## Dynamic learning rule

Published papers are evidence about **how writers solved rhetorical, evidentiary, linguistic, and visual problems under particular conditions**. They are not text/figure templates and not automatic best practice.

When learning from papers:

1. sample comparable papers, not only famous ones;
2. annotate complete rhetorical/evidence units, not isolated attractive sentences or plots;
3. distinguish scientific necessity from discipline/journal/author tendencies;
4. record legitimate counterexamples;
5. separate frequency from effectiveness;
6. choose final figures/plots from the user's data and claim, not popularity;
7. validate a proposed core rule outside the corpus that generated it;
8. keep exact journal mechanics separate from observed published practice;
9. distinguish **survivorship** from evidence of causality — published-paper patterns show what survived one publication ecology, not what independently caused acceptance;
10. preserve an independent author/project voice after structural calibration;
11. learn sentence-level naturalness from information flow, stance, lexical chains, and rhetorical function rather than copying recognizable phrases.

## Submission boundary

- `nature-writing` owns manuscript drafting, analogue-paper structural calibration, natural scholarly prose, author-voice restoration, pre-submission decision engineering, and **initial submission** materials before peer review.
- `nature-figure` owns detailed visual analogue calibration, plot choice, figure building, and graphical abstracts.
- `nature-reviewer` owns isolated pre-submission editor/reviewer simulation when the user wants full mock reports.
- `nature-response` owns post-decision rebuttals, revision cover letters, marked manuscripts and appeals.

## Acceptance-engineering red lines

- Optimize scientific credibility and decisionability, not reviewer manipulation.
- Never hide adverse/contradictory evidence or a close competitor.
- Never recommend strategic citations to likely reviewers or selection of friendly reviewers.
- Never manufacture broad interest or novelty with wording that the evidence cannot support.
- Never bury a limitation in SI if it changes the headline interpretation.
- Do not add cosmetic experiments that fail to discriminate between plausible interpretations.
- Do not use cover-letter rhetoric to create a stronger scientific story than the manuscript establishes.

## Natural-writing red lines

- Do not optimize for AI-detector evasion.
- Do not deliberately introduce errors or random variability.
- Do not maintain a machine-associated word blacklist.
- Do not convert `human voice` into forced informality.
- Do not imitate a named living author's distinctive prose style.
- Do not replace precise technical repetition with unstable synonym variation.
- Do not use connectives as substitutes for reasoning.

## Non-negotiable writing rules

- Evidence quality and study design determine claim strength; journal prestige does not.
- A research need need not be a manufactured `gap`.
- Strong prior work should be represented fairly.
- Do not hide incrementality to make a contribution appear larger.
- Do not copy distinctive prose or figure design from analogue papers.
- Do not erase the author's coherent voice merely to resemble a target corpus.
- Do not force IMRaD, conclusion-first Results, pipeline Methods, a fixed abstract funnel, one-function paragraphs, or one sentence-flow pattern across disciplines.
- Do not equate more connectives, shorter sentences, denser noun phrases, rarer vocabulary, or more assertive verbs with better academic writing.
- Exact live journal requirements outrank local formatting profiles; scientific validity outranks all house style.

## Why this architecture

- The core stores rules that survived cross-disciplinary testing.
- A close analogue set supplies paper-class-specific structural/evidence priors; broader corpora remain separate evidence layers.
- Natural scholarly prose operates on reader-facing reasoning rather than detector-facing surface statistics.
- Author voice is modeled separately so structural and linguistic repair do not become generic-academic flattening.
- Dynamic calibration lets the skill learn current practice without hard-coding thousands of journals.
- The decision preflight separates `scientifically weak`, `scientifically sound but hard to evaluate`, and `scientifically sound but target-mismatched` manuscripts.
- Regression tests protect the distinction between scientific/rhetorical logic, author identity, surface imitation, detector gaming, and review-system gaming.
