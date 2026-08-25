---
name: nature-shared
description: Internal shared-reference support package for installed academic-paper skills, including nature-writing, nature-polishing, nature-reviewer, nature-response, nature-figure, nature-reader, and nature-paper2ppt. Do not invoke it as a standalone user workflow. Load only the specific core or journal-format file requested by another skill.
---

# Academic Paper Shared References

Use this package only as a dependency of another installed academic-paper skill.

- Load the exact referenced file; do not preload the whole package.
- Treat `core/`, `research/`, and `journal-formats/` as shared definitions/evidence layers, not standalone user workflows.
- Use `core/paper-archetype-atlas.md` before generalizing paper/figure structure across very different scientific jobs. Calibrate mechanism/discovery, randomized intervention, observational, computational/ML, method/tool/software, resource/dataset, theory/proof, qualitative, review/synthesis, and hybrid papers by their evidence dependencies rather than prestige-journal surface patterns.
- Use `research/stratified-paper-reading-2025-2026.md` when recent cross-archetype direct-reading counterexamples are needed. It is descriptive calibration, not causal acceptance evidence.
- Use `core/analogue-paper-calibration.md` when writing/figure/review work should study a few close comparable papers for argument, evidence, figure, data-display, explanation-depth, and main-text-versus-SI priors without copying wording or visual identity.
- Use `core/author-voice-profile.md` when substantial rewriting/polishing should preserve a recognizable authorial cadence, agency, terminology, technical density, and stance after structural repairs.
- Use `core/natural-scholarly-prose.md` when drafting or polishing prose that feels generic, over-smoothed, formulaic, choppy, repetitive, connector-heavy, or weakly authorial. Repair scientific relations, information progression, lexical/reference chains, local stance, functional syntax, and cadence. Never use it for AI-detector evasion, random `burstiness`, deliberate errors, or word blacklists.
- Use `core/explanatory-sufficiency.md` when prose is concise but readers may not actually understand the idea. Audit hidden premises, missing rationale, mechanism/logic, operational evidence, interpretation boundaries, unfamiliar concepts, equations, figure meaning, and whether the intended reader can reconstruct `what / why / how / evidence / boundary / what follows`. Expand only the specific missing reasoning; do not equate longer prose with better prose.
- Use `core/manuscript-content-selection.md` when deciding what belongs in main text, figures, legends, Methods, Extended Data/SI, availability statements, repository documentation, or nowhere. In particular, use it to prevent **implementation-detail / repository-to-manuscript leakage** such as file paths, helper names, setup commands, project links, internal modules, configs, and developer workflow from contaminating scientific narrative.
- Use `core/figure-evidence-planning.md` when deciding what figures or plots a paper needs before rendering. Map `claim -> reader question -> estimand -> data structure -> uncertainty/alternative explanation -> visual representation -> main/support placement`; do not select plots because analogue/top-journal papers happen to use them.
- Use `core/manuscript-surface-qa.md` as the **last manuscript-facing release gate** after drafting/polishing/legend writing. Scrub filenames, paths, scripts/helpers, CLI/developer residue, raw project links and output names; then audit punctuation/spacing/brackets/ranges/minus/hyphen/units and target-aware copy-editing. Use `scripts/audit_manuscript_surface.py` only as a conservative warning tool, never an automatic semantic rewriter.
- Use `core/editor-reviewer-decision-engine.md` for target-aware editorial triage, reviewer decision proof, synthesis, and revision-closure logic.
- Use `journal-formats/journal-resolution.md` before exact journal/article-type/stage compliance work.
- Use `journal-formats/nature.md` only for the flagship journal Nature and `core/research-compliance.md` only when its specialist applicability gate is triggered.
- Use `journal-formats/nature-machine-intelligence.md` for exact NMI article types, limits, initial-submission files, data/code duties and production requirements; do not import flagship Nature or Nature Communications limits.
- Use `core/main-text-discipline.md` for result placement, main-text compression, revision accretion, caption/SI allocation, and claim-repetition checks; combine it with `core/manuscript-content-selection.md` when the problem is broader than Results compression.
- Return to the requesting skill for task logic, output format, and final QA.
