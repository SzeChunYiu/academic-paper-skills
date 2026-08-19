---
name: nature-polishing
description: Polish, restructure, shorten, or translate academic prose into journal-aware scholarly English while preserving facts, evidence boundaries, terminology, uncertainty, and citation intent. The legacy skill name is retained for compatibility, but the workflow supports Nature Portfolio, Science/AAAS, Cell Press, IEEE, ACM, PLOS, Springer/BMC, Elsevier, Wiley, society journals, discipline-specific venues, journal transfer, and unknown targets through an extensible journal resolver. Use for manuscript paragraphs, abstracts, introductions, Results, discussions, conclusions, titles, Methods, Chinese drafts, proofreading, language editing, and general academic or scientific writing. Also use to shorten bloated Results, allocate evidence across main text, captions, Methods/source data, and Supplementary Information, prevent reviewer-driven revision accretion, reduce repeated statistics or claims, and apply paragraph-necessity checks. Covers LaTeX layout or typesetting fixes such as sparse pages, stranded headings, oversized or split figures, float errors, multi-panel arrangement, and sparse Supplementary Information via references/latex-layout.md. Trigger on 学术写作、科研写作、论文润色、SCI写作、英文论文润色、语言润色、润色、改写、学术英语、期刊转换、排版.
---

# Journal-Aware Academic Polishing — Router

`nature-polishing` is a legacy entry-point name. Do not infer the target journal from the skill name.

This skill is split into two layers:

- A **static layer** under `static/` that holds versioned, reusable content fragments (core principles, paper-type playbooks, per-section guidance, language-specific rules, and journal routing fragments).
- A **dynamic layer** (this file plus `manifest.yaml`) that detects the request's axes and loads only the fragments needed for the current job.

Shared journal resolution lives under `../nature-shared/journal-formats/`. Exact live journal instructions outrank local profiles for submission-critical requirements.

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

Do **not** read every fragment in `static/`.

### 4. Polish using the loaded material

Use two conceptual passes even if the final output is delivered once.

#### Pass A — target-independent scientific edit

Apply:

1. Paper-type playbook (architecture, writing order).
2. Section-specific job and failure modes.
3. Paragraph logic and claim/evidence/boundary discipline.
4. Terminology, units, numbers, tense, and cross-manuscript consistency.
5. Language-specific sentence and paragraph repair.

Fix clarity without changing facts, uncertainty, causal strength, novelty boundaries, or limitations.

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

For a journal transfer, preserve target-independent edits, remove the old journal's house style and boilerplate, resolve the new journal/content type/stage, then re-apply only verified target-dependent constraints.

If a structural problem cannot be fixed without inventing content, flag it instead of papering over it.

### 5. Reach for references only when needed

The files under `references/` are deep references, not defaults. Open them on demand per the `references.on_demand` table in the manifest.

- Any named non-Nature target, family, or journal transfer -> shared `journal-resolution.md` and `journal-family-profiles.md`.
- Nature/Nature Communications published-pattern examples -> `references/published-article-patterns.md`; do not apply them automatically to non-Nature targets.
- Section moves/phrase alternatives/style mechanics -> the relevant local references.
- Whole-manuscript consistency -> `../nature-shared/core/consistency-sweep.md`.
- Nature Machine Intelligence exact requirements -> `../nature-shared/journal-formats/nature-machine-intelligence.md`.

**Layout/typesetting requests are different.** If the user asks to fix placement rather than wording — loose/sparse pages, stranded headings, figures that do not fill the page or split across pages, `Float too large`, multi-panel arrangement, sparse Supplementary Information — load `references/latex-layout.md` directly for diagnosis and layout repair. If a named target journal is involved, also resolve that journal's current template and stage-specific mechanics; never assume Nature layout rules. Always compile and visually inspect rendered pages before and after when execution tools are available.

## Safety and generalization rules

- Never equate prestigious wording with scientific quality.
- Never make a claim more causal, general, certain, or novel to match a journal's perceived tone.
- Never force IMRaD, Nature summary-paragraph logic, STAR Methods, IEEE/ACM layout, or another family convention onto an incompatible paper type.
- Exact live author instructions outrank local profiles; exact local profiles outrank family profiles; family profiles outrank generic defaults only for non-submission-critical guidance.

## Why this split

- The static layer is versioned and reviewable. Adding an exact journal style remains one file plus one manifest line, while unprofiled journals work through the shared resolver.
- The dynamic layer keeps each invocation cheap: only fragments relevant to this draft enter context.
- Existing `nature-*` names remain backward-compatible while behavior becomes journal-agnostic.
- Scientific editing is separated from journal-specific house style and submission mechanics.
