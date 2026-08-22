# `nature-polishing` Skill

[中文说明](README.md)

`nature-polishing` rewrites, restructures, shortens, expands when needed, or translates academic prose while preserving scientific meaning, evidence boundaries, terminology, citation intent, and author voice. It is journal-aware rather than Nature-only, and it treats “less AI-written” as a writing-quality problem — logic, information flow, explanatory sufficiency, stance, syntax, cadence, and authentic voice — not an AI-detector-evasion problem.

## What To Use It For

- Translate Chinese academic prose into publication-ready English without changing the science.
- Repair sentence-to-sentence logic before polishing vocabulary.
- Rewrite paragraphs using proposition dependencies and the `inherits -> relation -> adds -> enables` test.
- Detect **under-explanation** when a polished short passage omits the rationale, hidden premise, mechanism/logic, comparison meaning, or boundary needed for readers to understand it.
- Expand only the missing explanation, while keeping routine or already-sufficient material concise.
- Make prose more natural when it feels generic, over-smoothed, formulaic, repetitive, connector-heavy, or machine-like.
- Preserve useful technical repetition and authorial agency instead of rotating synonyms or deleting `we` mechanically.
- Study a few close analogue papers before a substantial rewrite to learn local rhetorical/evidence/explanation conventions without copying phrases.
- Build a compact author-voice profile and run a re-voice pass after structural edits.
- Detect prose that contains codebase/repository debris and relocate operational details through the shared manuscript-content-selection logic when doing full-manuscript work.
- Shorten Results and allocate core evidence versus robustness/support to main text, captions, Methods, Extended Data/SI, and availability/artifact layers.
- Adapt the final prose to the exact target journal/article type/stage only after the scientific/logical edit is stable.
- Sweep full or repeatedly revised manuscripts for terminology, units, numeric precision, claim drift, redundant evidence, and explanation gaps.

## Workflow

For a substantial rewrite, the editor conceptually works in this order:

```text
scientific meaning / claims
-> paragraph and sentence dependency
-> explanatory sufficiency / hidden-premise audit
-> information flow + identity chains
-> stance and evidence strength
-> functional syntax and precise vocabulary
-> necessary connectives
-> natural cadence
-> author re-voice
-> exact journal adaptation
-> consistency / claim-drift audit
```

For a central idea, the skill checks whether the intended reader can reconstruct, as needed:

`what -> why -> how/logic -> evidence/comparison -> boundary -> what follows`

It does not force every element into every paragraph. Explanation expands with centrality, unfamiliarity, and inferential dependence, and contracts for routine knowledge or already-sufficient material.

When useful, a pre-pass studies 3–6 close analogue papers for **structural/evidence priors**, while the author's own prose supplies the **expression prior**.

“Humanizing” never means adding errors, random sentence lengths, odd punctuation, slang, or a blacklist of words associated with LLMs.

## Method Sources

- [`docs/academic-writing-research_EN.md`](../../docs/academic-writing-research_EN.md): cross-disciplinary writing, cohesion, stance, and human/LLM academic-writing evidence.
- [`docs/natural-scholarly-writing_EN.md`](../../docs/natural-scholarly-writing_EN.md): practical sentence-to-sentence flow and natural academic prose.
- [`docs/explanatory-sufficiency_EN.md`](../../docs/explanatory-sufficiency_EN.md): minimum-sufficient explanation, hidden premises, and adaptive elaboration.
- [`docs/manuscript-content-and-figures_EN.md`](../../docs/manuscript-content-and-figures_EN.md): content allocation and repository-to-manuscript leakage.
- `../nature-shared/core/explanatory-sufficiency.md`: reader-reconstruction and explanation-depth contract.
- `../nature-shared/core/natural-scholarly-prose.md`: research-backed natural-prose contract.
- `../nature-shared/core/author-voice-profile.md`: manuscript voice preservation.
- `../nature-shared/core/analogue-paper-calibration.md`: close-paper structural calibration.
- `../nature-shared/core/main-text-discipline.md`: Results compression and evidence allocation.

## Typical Requests

- "Translate this Chinese Results paragraph into clear academic English; don't make it sound like generic AI prose."
- "This explanation is too short for readers to follow. Identify the missing reasoning and expand only what is necessary."
- "This paragraph is grammatically correct but the sentences don't flow. Rebuild the dependencies first."
- "Preserve my author voice after restructuring this Discussion."
- "Read a few similar papers before polishing this section, but don't copy their wording."
- "Remove implementation/repository details that do not belong in the manuscript and move them to the right layer."
- "Adapt this scientifically stable draft from Journal A to Journal B without changing claim strength."

## What You Need To Provide

- Source text and section context.
- Facts, data, citations, terminology, uncertainty, and claims that must not change.
- Representative author prose when preserving voice matters.
- Target journal/venue and article type when journal-specific adaptation is requested.
- Desired output: rewrite only, paired original/rewrite, or rewrite plus reasoning/risk notes.

## Outputs

- Ready-to-paste English rewrite or Chinese-English paired version.
- Key change notes covering logic, explanation depth, sentence dependency, stance, terminology, and claim boundaries.
- Optional explanation diagnostics: hidden premise, missing `what/why/how/evidence/boundary/connection`, and `sufficient / under-explained / over-explained` status.
- Optional author-voice profile / voice-drift notes for large edits.
- Optional natural-prose diagnostics: orphan sentences, vague referents, connector stuffing, repeated templates, generic prestige language, and nonfunctional syntactic repetition.
- Main-text allocation/deletion records for Results/full-manuscript compression.
- Consistency-risk list for terminology/unit/precision/claim drift.
- Facts or citation intent requiring author confirmation.

## Boundaries

- The skill does not invent results, mechanisms, statistical significance, citations, unsupported interpretation, or unsupported rationale.
- It does not equate longer prose with better explanation or turn routine field knowledge into textbook exposition.
- It does not make prose more causal, general, certain, novel, or important merely to sound prestigious.
- It does not optimize AI-detector scores, maintain `AI-word` blacklists, deliberately add mistakes, or create random `burstiness`.
- It does not copy distinctive prose from analogue papers or imitate a named living author's style.
- Layout-only LaTeX work skips prose, analogue, explanation-depth, naturalization, and re-voice passes.
- For writing a section from scratch or planning evidence/figures, use `nature-writing`; for final figure rendering, use `nature-figure`.

## Related Skills

- `nature-writing`: argument architecture, explanatory sufficiency, content selection, plot/figure suggestions, and section drafting.
- `nature-figure`: claim-driven figure rendering and visual QA.
- `nature-response`: reviewer response and revision correspondence.
- `nature-statistics`: statistical text, estimands, uncertainty, and figure statistics.
- `nature-reviewer`: pre-submission editor/reviewer stress testing, including explanation-depth issues.
