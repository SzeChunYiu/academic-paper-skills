---
name: nature-writing
description: Draft, restructure, or plan journal-aware academic manuscript sections and initial-submission materials from author-provided claims, results, figures, notes, or Chinese drafts. The legacy skill name is retained for compatibility, but the workflow supports Nature Portfolio, Science/AAAS, Cell Press, IEEE, ACM, PLOS, Springer/BMC, Elsevier, Wiley, society journals, discipline-specific venues, and unknown targets through an extensible journal resolver. Use for abstracts, introductions, related work, methods, Results or experiments, discussions, conclusions, titles, full manuscript arguments, journal transfer, and first-submission packages such as cover letters, title pages, highlights, author contributions, availability or declaration text, and reviewer suggestions. Also use to classify Results evidence, decide what belongs in main text, captions, Methods or source data, or Supplementary Information, compress Results to the shortest sufficient evidence chain, prevent revision accretion, and audit paragraph necessity or claim repetition. Trigger on drafting a paper or section, structuring a manuscript, academic writing, first submission, journal transfer, 投稿材料、首次投稿、投稿信、标题页、亮点、作者贡献、数据可用性声明、推荐审稿人.
---

# Journal-Aware Scientific Writing — Router

`nature-writing` is a legacy entry-point name. Do not infer the target journal from the skill name. Resolve the target from the user's request and manuscript context.

This skill is split into two layers:

- A **static layer** under `static/` that holds versioned, reusable content fragments (core stance + workflow, paper-type playbooks, per-section drafting guidance, initial-submission guidance, language-specific rules, and journal routing fragments).
- A **dynamic layer** (this file plus `manifest.yaml`) that detects the request's axes and loads only the fragments needed for the current job.

Shared journal resolution lives under `../nature-shared/journal-formats/`. Exact live journal instructions outrank local profiles for submission-critical requirements.

Do not try to apply the drafting logic from memory or from this router. Always load fragments from disk as described below.

## Routing protocol

Follow these five steps every time the skill is invoked.

### 1. Load the manifest and the core layer

Read [manifest.yaml](manifest.yaml). It declares the axes (`task`, `paper_type`, `section`, `language`, `journal`), the allowed values, and the file paths each value maps to.

Also read every file listed under `always_load`. These hold the default stance, writing workflow, ethics, terminology, and output format that apply to every drafting job.

### 2. Detect the axis values for this request

For each axis in the manifest, decide the value using the manifest's `detect:` hint and the user's input:

- `task` — manuscript / submission-package. Use `submission-package` for first-submission materials, never for revision correspondence.
- `paper_type` — research / methods / hypothesis / algorithmic / review. Default: research.
- `section` — abstract / intro / related-work / method / experiments / discussion / conclusion / title. May be multiple. Ask only if ambiguity materially blocks a correct draft; otherwise make the safest generic choice and mark unresolved assumptions.
- `language` — en or zh-to-en. Detect from the user's notes themselves.
- `journal` — nature / nature-family / nat-comms / nat-mach-intell / profiled / generic.
  - `nature`: flagship **Nature** only.
  - `nat-comms`: **Nature Communications** only.
  - `nat-mach-intell`: **Nature Machine Intelligence** only.
  - `nature-family`: another Nature Portfolio title or an unresolved Nature-family request.
  - `profiled`: any named non-Nature journal, publisher/venue family, discipline family, or journal-transfer request. This includes Science/AAAS, Cell Press, IEEE, ACM, PLOS, Springer/BMC, Elsevier, Wiley, society journals, APA-style targets, biomedical/clinical venues, and humanities/law journals.
  - `generic`: no target or useful family is known.

State the detected axis values in one short line before drafting when doing so helps the user correct a material misclassification.

For `profiled`, the skill name must never bias the result toward Nature style.

### 3. Load the matching fragments

For each axis value, read the file mapped in the manifest. Skip the `section` axis when the task is `submission-package` or when the user explicitly asks for a free-floating argument paragraph with no section context.

For `journal=profiled`, also follow the fragment's instruction to load:

- `../nature-shared/journal-formats/journal-resolution.md`
- `../nature-shared/journal-formats/journal-family-profiles.md`

Then resolve, as far as the task requires:

`exact journal -> article/content type -> stage -> component`

If exact compliance matters, check the current official author instructions for that exact journal/content type/stage. Family profiles are fallbacks, not submission contracts.

Do **not** read every fragment in `static/`.

### 4. Draft using the loaded material

Apply the loaded fragments in this priority order:

1. Core stance + intake (`core/stance.md`) — surface missing claim / evidence / boundary before drafting.
2. Paper-type playbook — argument chain, drafting order.
3. Section-specific drafting rules and structure.
4. Research-reporting obligations and discipline conventions where relevant.
5. Task-specific submission rules when `task=submission-package`.
6. Exact journal/content-type/stage requirements when verified.
7. Journal-family guidance only as a non-numeric fallback.
8. Language-specific sentence and paragraph rules (apply last).

For `task=manuscript`, run the workflow in `core/workflow.md` end-to-end. Do not skip planning just because the user asked for prose immediately.

When drafting or restructuring Results, or compressing a full manuscript's main text, also load `../nature-shared/core/main-text-discipline.md` before building the paragraph map. Classify every result by function, allocate it across main text, captions, Methods/source data, and SI, then draft the shortest sufficient evidence chain. Do not equate a complete analysis record with a complete main text.

For `task=submission-package`, follow `static/fragments/task/submission-package.md` and `references/submission-package.md`. For a named non-Nature journal, treat any Nature-specific examples in those references as examples only and verify the exact target's current required package.

If essential evidence or boundary is missing, write a placeholder and list it under `Assumptions or missing inputs:` instead of inventing content.

For a journal transfer, preserve target-independent scientific edits, remove old-journal house style, resolve the new target, and rebuild only target-dependent structure, front/back matter, citation rendering, and mechanics.

### 5. Reach for references only when needed

The files under `references/` are deep references and the example library, not defaults. Open them on demand per the `references.on_demand` table in the manifest. Typical triggers:

- Any named non-Nature target, publisher/venue family, or journal transfer -> `../nature-shared/journal-formats/journal-resolution.md` and, if useful, `journal-family-profiles.md`.
- A concrete example/template -> `references/examples/index.md`.
- A section has structural problems -> the matching `references/<section>.md`.
- A broad-audience flagship Nature abstract opening or summary paragraph -> `references/nature-summary-paragraph.md`.
- Paragraph-flow audit -> `references/paragraph-flow.md`.
- Self-review/rejection-risk audit -> `references/paper-review.md`.
- Main-text/caption/SI allocation or reviewer-driven accretion -> `../nature-shared/core/main-text-discipline.md`.
- Complete first-submission package or readiness audit -> `references/submission-package.md`, interpreted through the exact target journal when non-Nature.
- Flagship Nature exact rules -> `../nature-shared/journal-formats/nature.md`.
- Nature Machine Intelligence exact rules -> `../nature-shared/journal-formats/nature-machine-intelligence.md`.
- Regulated or specialist research compliance -> `../nature-shared/core/research-compliance.md`.

## Submission boundary

- `nature-writing` owns **initial submission** materials prepared before peer review, regardless of journal family.
- `nature-response` owns revision cover letters, rebuttals, point-by-point responses, marked manuscripts, appeals, and other post-decision correspondence.
- Route graphical abstracts and TOC graphics to `nature-figure`; route simulated pre-submission peer review to `nature-reviewer`.

## Safety and generalization rules

- Never equate journal prestige with evidence quality.
- Never copy a numeric or mechanical requirement from a sister journal without verifying the exact target.
- Never force IMRaD onto a genre or discipline that does not use it.
- Never strengthen causality, novelty, generality, or certainty merely to imitate a selective journal.
- Exact live author instructions outrank local profiles; exact local profiles outrank family profiles; family profiles outrank generic defaults only for non-submission-critical guidance.

## Why this split

- The static layer is versioned and reviewable. Adding another exact journal profile is one file plus one manifest route, while thousands of unprofiled journals still work through the resolver.
- The dynamic layer keeps each invocation cheap: only relevant fragments enter context.
- Existing `nature-*` entry points remain usable, avoiding a breaking rename while behavior becomes journal-agnostic.
- Journal-specific formatting is separated from scientific structure, reporting obligations, evidence selection, and submission mechanics.
