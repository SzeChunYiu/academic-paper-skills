---
name: nature-polishing
description: Polish, restructure, shorten, or translate academic prose into journal-aware scholarly English while preserving facts, evidence boundaries, terminology, uncertainty, citation intent, and a recognizable author voice. The legacy skill name is retained for compatibility, but the workflow supports Nature Portfolio, Science/AAAS, Cell Press, IEEE, ACM, PLOS, Springer/BMC, Elsevier, Wiley, society journals, discipline-specific venues, journal transfer, and unknown targets through an extensible journal resolver. For substantial rewrites, study a few genuinely comparable papers to learn rhetorical moves, evidence/figure expectations, data presentation, and current field conventions without copying wording; separately build an author-voice profile so the result sounds like a clearer version of the author rather than a synthetic target-journal imitation. Also use a research-backed natural-scholarly-prose pass when text feels generic, formulaic, over-smoothed, machine-like, repetitive, connector-heavy, or difficult to follow sentence by sentence. Repair proposition dependencies, given/new progression, identity chains, stance, syntax, connectives, and cadence without optimizing for AI-detector evasion. Use for manuscript paragraphs, abstracts, introductions, Results, discussions, conclusions, titles, Methods, Chinese drafts, proofreading, language editing, and general academic or scientific writing. Also use to shorten bloated Results, allocate evidence across main text, captions, Methods/source data, and Supplementary Information, prevent reviewer-driven revision accretion, reduce repeated statistics or claims, and apply paragraph-necessity checks. Covers LaTeX layout or typesetting fixes such as sparse pages, stranded headings, oversized or split figures, float errors, multi-panel arrangement, and sparse Supplementary Information via references/latex-layout.md. Trigger on 学术写作、科研写作、论文润色、SCI写作、英文论文润色、自然学术表达、AI味、句间逻辑、语言润色、润色、改写、学术英语、期刊转换、排版.
---

# Journal-Aware Academic Polishing — Router

`nature-polishing` is a legacy entry-point name. Do not infer the target journal or desired prose style from the skill name.

This skill is split into two layers:

- A **static layer** under `static/` that holds versioned, reusable content fragments (core principles, paper-type playbooks, per-section guidance, language-specific rules, and journal routing fragments).
- A **dynamic layer** (this file plus `manifest.yaml`) that detects the request's axes and loads only the fragments needed for the current job.

Shared journal resolution, analogue calibration, author voice, and natural scholarly prose live under `../nature-shared/`. Exact live journal instructions outrank local profiles for submission-critical requirements.

Do not try to apply the polishing logic from memory or from this router. Always load fragments from disk as described below.

## Routing protocol

Follow these five steps every time the skill is invoked.

### 1. Load the manifest and the core layer

Read [manifest.yaml](manifest.yaml). It declares the axes (`paper_type`, `section`, `language`, `journal`), the allowed values, and the file paths each value maps to.

Also read every file listed under `always_load`. These hold the default stance, failure-mode diagnosis, ethics, terminology discipline, and output format that apply to every polish job.

### 2. Detect the axis values for this request

For each axis in the manifest, decide the value using the manifest's `detect:` hint and the user's input:

- `paper_type` — research / methods / hypothesis / algorithmic / review. Default: research.
- `section` — abstract / intro / results / discussion / conclusion / title / methods. May be multiple. Infer conservatively when possible; ask only if the ambiguity materially changes the edit.
- `language` — en or zh-to-en. Detect from the draft itself.
- `journal` — nature / nat-comms / nat-mach-intell / profiled / generic.
  - `nature`: flagship **Nature** only.
  - `nat-comms`: **Nature Communications** only.
  - `nat-mach-intell`: **Nature Machine Intelligence** only.
  - `profiled`: any other named journal, journal/publisher/venue/discipline family, or journal-transfer target. This includes other Nature Portfolio titles, Science/AAAS, Cell Press, IEEE, ACM, PLOS, Springer/BMC, Elsevier, Wiley, society journals, APA-style targets, biomedical/clinical venues, and humanities/law journals.
  - `generic`: no target or useful family is known.

State the detected axis values in one short line when doing so helps the user cheaply correct a material misclassification.

### 3. Load the matching fragments

For each axis value, read the file mapped in the manifest. Skip the `section` axis only for truly free-floating prose with no section context.

For `journal=profiled`, also load:

- `../nature-shared/journal-formats/journal-resolution.md`
- `../nature-shared/journal-formats/journal-family-profiles.md`

Then resolve, as far as the task requires:

`exact journal -> article/content type -> stage -> component`

If exact compliance matters, check the current official author instructions for the exact journal/content type/stage. Family profiles are fallbacks, not submission contracts.

When the user says the prose feels `AI-written`, generic, unnatural, formulaic, over-polished, monotonous, connector-heavy, or choppy, load `../nature-shared/core/natural-scholarly-prose.md`. If representative author prose exists, also load `../nature-shared/core/author-voice-profile.md`.

Do **not** read every fragment in `static/`.

### 4. Polish using the loaded material

Use three conceptual passes when naturalness/voice matters, even if the final output is delivered once.

#### Pre-pass — analogue papers and author voice for substantial rewrites

When rewriting more than a small local passage and the field/contribution class or target is known, load `../nature-shared/core/analogue-paper-calibration.md` and inspect a few close analogue papers when reliable access is available.

Learn only transferable functions:

- how comparable papers build the research need;
- how evidence blocks are ordered;
- what data/figures normally carry claims of this type;
- where validation, robustness, generalization, negative cases, and limitations appear;
- how much context and signposting this audience appears to need;
- what is commonly kept in main text versus SI.

Do not copy phrases, distinctive paragraph forms, figure layouts, visual identity, or unverified analysis choices.

If the user supplied representative prose or asks to keep their style, also load `../nature-shared/core/author-voice-profile.md`. Record a compact voice profile before rewriting: cadence, agency, technical density, signposting, terminology, epistemic stance, paragraph rhythm, and citation integration. Separate **voice invariants** from flexible traits.

Use this conceptual split:

`analogue papers = structural/evidence priors`

`author voice = expression prior`

`author evidence = truth constraint`

`journal rules = compliance constraint`

For a tiny correction, layout-only job, or missing/reliably incomparable analogue set, skip or bound this pre-pass rather than inventing a corpus.

#### Pass A — target-independent scientific and logical edit

Apply:

1. Paper-type playbook (architecture, writing order).
2. Section-specific job and failure modes.
3. Paragraph logic and claim/evidence/boundary discipline.
4. Terminology, units, numbers, tense, and cross-manuscript consistency.
5. Analogue-derived structural/evidence lessons only where they solve a real reader/reviewer problem.
6. Author-voice invariants where they remain compatible with clarity and scientific accuracy.
7. Language-specific sentence and paragraph repair.

Fix clarity without changing facts, uncertainty, causal strength, novelty boundaries, or limitations.

For a paragraph that reads fluently but does not flow logically, repair **dependencies before diction**:

`paragraph nucleus -> sentence propositions -> sentence relations -> information progression -> identity/reference chain -> topic/emphasis`

For each sentence after the first, ask:

`inherits X -> relation R -> adds Y -> enables Z`

A sentence connected only by `moreover`, `furthermore`, or another generic additive marker may still be structurally orphaned.

#### Pass A2 — natural scholarly prose + re-voice

When naturalness is part of the job, load `../nature-shared/core/natural-scholarly-prose.md` after the core logic is stable.

Use the quality hierarchy:

`scientific relation -> information flow -> lexical/reference continuity -> stance -> syntax -> connective -> cadence`

Key rules:

- use given->new as a useful default, not a universal template;
- choose constant-topic, contrast, derived-theme, question-answer, or other progression when the reasoning requires it;
- repeat canonical technical terms when they refer to the same thing rather than rotating synonyms for elegance;
- choose vocabulary for precision and collocational naturalness, not rarity;
- calibrate hedge/booster strength proposition by proposition;
- choose `we`, passive, or process-centered syntax according to agency/focus and disciplinary convention;
- vary syntax because rhetorical function varies, not to manufacture `human` randomness;
- add connectives only when the underlying relation needs explicit encoding;
- run cadence/read-aloud checks only after reasoning is correct.

If major restructuring was required, finish with a **re-voice pass** using the author profile so the result does not collapse into generic academic prose.

### What `make it less AI-written` means here

Treat the request as a quality problem, not a detector-evasion problem.

Look for:

- repeated sentence/paragraph templates;
- standardized neutral cadence with little functionally motivated variation;
- narrow/repetitive stance or engagement choices;
- ornamental or unnecessarily rare academic words;
- synonym substitution while sentence architecture stays identical;
- agentless/depersonalized claims that hide authorial responsibility;
- excessive additive connectives;
- generic prestige language where a concrete scientific consequence should appear.

Do **not**:

- optimize an AI-detector score;
- maintain a blacklist of `AI words`;
- add intentional grammar mistakes, fragments, slang, typos, or odd punctuation;
- randomize sentence length or vocabulary to create `burstiness`;
- hide required disclosure of AI assistance.

#### Pass B — target-dependent adaptation

Only after the target is resolved, adapt:

1. Audience breadth and assumed background.
2. Title/abstract compression and framing.
3. Section architecture and heading conventions.
4. Terminology/abbreviation density.
5. Main-text versus Methods/Supplementary allocation.
6. Reference/display economy.
7. Required front/back matter wording and other verified house-style requirements.

Exact journal requirements outrank family-profile guidance. Never import another journal's numeric limit, punctuation, legend rule, or submission mechanic because it shares a publisher.

For Results, full-main-text compression, main-versus-SI allocation, or prose added during revision, load `../nature-shared/core/main-text-discipline.md` before sentence polishing. Classify each result, retain the shortest sufficient evidence chain, and require every addition to trigger a deletion or replacement check across the affected paragraph.

When the job is a whole manuscript rather than a passage, or the text has already been through more than one round of editing, also load `../nature-shared/core/consistency-sweep.md`. Sweep for accumulated terminology/unit/number drift, claims contradicted by displays, repeated evidence, and tense/label inconsistencies before polishing sentences, and repeat until a pass finds nothing new.

For a journal transfer, preserve target-independent edits and the manuscript-level author voice, remove the old journal's house style and boilerplate, resolve the new journal/content type/stage, then re-apply only verified target-dependent constraints.

If a structural problem cannot be fixed without inventing content, flag it instead of papering over it.

### 5. Reach for references only when needed

The files under `references/` are deep references, not defaults. Open them on demand per the `references.on_demand` table in the manifest.

- Natural scholarly prose / machine-like generic writing -> `../nature-shared/core/natural-scholarly-prose.md`.
- Substantial rewrite with similar-paper study -> `../nature-shared/core/analogue-paper-calibration.md`.
- Preserve author's recognizable style -> `../nature-shared/core/author-voice-profile.md`.
- Any named non-Nature target, family, or journal transfer -> shared `journal-resolution.md` and `journal-family-profiles.md`.
- Nature/Nature Communications published-pattern examples -> `references/published-article-patterns.md`; do not apply them automatically to non-Nature targets.
- Section moves/phrase alternatives/style mechanics -> the relevant local references.
- Whole-manuscript consistency -> `../nature-shared/core/consistency-sweep.md`.
- Nature Machine Intelligence exact requirements -> `../nature-shared/journal-formats/nature-machine-intelligence.md`.

**Layout/typesetting requests are different.** If the user asks to fix placement rather than wording — loose/sparse pages, stranded headings, figures that do not fill the page or split across pages, `Float too large`, multi-panel arrangement, sparse Supplementary Information — load `references/latex-layout.md` directly for diagnosis and layout repair. Do not run prose rewriting, analogue-style calibration, natural-prose rewriting, or author-voice rewriting for a placement-only request. If a named target journal is involved, also resolve that journal's current template and stage-specific mechanics; never assume Nature layout rules. Always compile and visually inspect rendered pages before and after when execution tools are available.

## Safety and generalization rules

- Never equate prestigious wording with scientific quality.
- Never make a claim more causal, general, certain, or novel to match a journal's perceived tone.
- Never copy distinctive wording or visual identity from analogue papers.
- Never force IMRaD, Nature summary-paragraph logic, STAR Methods, IEEE/ACM layout, or another family convention onto an incompatible paper type.
- Never erase a coherent author voice merely to resemble target papers; preserve voice after logic/evidence repair unless clarity or exact requirements require change.
- Never treat `humanizing` as detector evasion, deliberate imperfection, or random stylistic noise.
- Exact live author instructions outrank local profiles; exact local profiles outrank family profiles; family profiles outrank generic defaults only for non-submission-critical guidance.

## Why this split

- The static layer is versioned and reviewable. Adding an exact journal style remains one file plus one manifest line, while unprofiled journals work through the shared resolver.
- The dynamic layer keeps each invocation cheap: only fragments relevant to this draft enter context.
- Existing `nature-*` names remain backward-compatible while behavior becomes journal-agnostic.
- Scientific editing is separated from journal-specific house style and submission mechanics.
- Analogue papers inform architecture/evidence expectations while a separate author-voice layer preserves manuscript identity.
- Natural scholarly prose protects against polished-but-generic machine-like output without relying on unstable detector heuristics.
