<div align="center">
  <p>
    <img src="assets/readme-banner-en.png" alt="Academic Paper Skills: reusable research and manuscript workflows for AI scholars" width="100%">
  </p>
  <p>
    <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-2ea44f"></a>
    <a href="#5-installation"><img alt="Install" src="https://img.shields.io/badge/install-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw%20%7C%20OpenCode%20%7C%20Hermes-111827"></a>
    <a href="#6-skill-index"><img alt="Skills" src="https://img.shields.io/badge/skills-20-0ea5e9"></a>
    <a href="README.md"><img alt="Language" src="https://img.shields.io/badge/language-English%20%7C%20中文-1f6feb"></a>
  </p>
  <p>
    <a href="https://yuan1z0825.github.io/nature-skills/">Website</a>
    · <a href="#4-quick-start">Quick Start</a>
    · <a href="#5-installation">Install</a>
    · <a href="#6-skill-index">Skill Index</a>
    · <a href="docs/deep-paper-calibration_EN.md">Paper Calibration</a>
    · <a href="docs/academic-writing-research_EN.md">Writing Research</a>
    · <a href="README.md">中文</a>
  </p>
</div>

---

This repository is a reusable **academic-research and academic-paper skill system** for AI agents. It began with Nature-oriented workflows, which is why many historical directories still use `nature-*` names, but the paper system is now **journal-agnostic and archetype-aware**.

The canonical writing entry point is **`academic-writing`**. The end-to-end iterative orchestration entry point is **`academic-paper-pipeline`**. Nature is now only one possible target adapter.

The current manuscript lifecycle is:

```text
target + paper archetype
-> evidence/source intake
-> literature and comparable-paper research
-> argument + claim/evidence architecture
-> content + statistics + figure/diagram planning
-> academic writing
-> sentence/explanation/author-voice repair
-> technical/reporting/surface QA
-> editor triage
-> independent reviewers
-> editor synthesis
-> revision + targeted re-review
   ↳ repeat while a real blocker remains
-> simulated publication readiness OR explicit blocker/retarget state
```

The goal is not to make every paper sound prestigious. The goal is to make the science **clear, rich enough to understand, defensible, reproducible, appropriately scoped, visually inspectable, and easy for the intended reader/editor/reviewer to evaluate**.

## Table of Contents

- [1. What This Repository Has Become](#1-what-this-repository-has-become)
- [2. Academic Writing, Review, and Paper Engineering](#2-academic-writing-review-and-paper-engineering)
- [3. Architecture and Design Principles](#3-architecture-and-design-principles)
- [4. Quick Start](#4-quick-start)
- [5. Installation](#5-installation)
- [6. Skill Index](#6-skill-index)
- [7. Contribution and Development](#7-contribution-and-development)
- [8. Project and Community](#8-project-and-community)

## 1. What This Repository Has Become

### Canonical academic writing, not Nature writing

`academic-writing` is the public manuscript-writing skill. The old `nature-writing` directory is retained only as a compatibility/reference implementation layer for mature section fragments, examples, and corpus scripts; implicit invocation is disabled.

Writing resolves:

`paper archetype -> study design/evidence -> intended reader -> article type -> exact target/stage`

rather than inferring a Nature style from the skill name.

### Closed-loop manuscript iteration

`academic-paper-pipeline` keeps one manuscript state across rounds and coordinates:

`research -> writing -> statistics -> figures/diagrams -> review -> editor synthesis -> revision -> re-review`

The simulated editor controls convergence. Reviewer votes are not counted as an acceptance decision. Major concerns keep stable IDs and resolution tests; major revisions can return to the relevant original reviewer, while minor clarity/surface fixes may be editor-closed when the target process permits.

The successful internal terminal label is `simulated_publication_ready_for_target`; it is a readiness simulation, not a promise of real-world acceptance.

### Self-research when the paper is unfamiliar

If a paper type, target venue, reporting standard, writing convention, or figure grammar is not confidently covered, the AI session should **research before guessing**:

1. current official target guidance;
2. applicable reporting/methodological standards;
3. a quick profile of comparable recent papers when useful;
4. 3–6 nearest-neighbor papers for deep reading;
5. counterexamples to apparent conventions.

It then builds a temporary manuscript-specific archetype profile instead of forcing the nearest template.

### Paper archetypes before journal aesthetics

The shared system distinguishes at least:

- experimental discovery/mechanism;
- randomized intervention/trial;
- observational/epidemiological/clinical association;
- computational/ML empirical;
- method/tool/software/instrument;
- dataset/resource;
- theory/proof;
- qualitative/interpretive;
- review/systematic review/perspective/synthesis;
- hybrid papers.

A clinical trial, ML benchmark, qualitative interview study, mechanism paper, and theorem paper should not share one evidence or figure sequence merely because they target selective journals.

### Evidence before prestige

Citation discovery defaults to best evidence rather than Nature/Science/Cell filtering. Explicit prestige/journal scopes remain available when the user actually requests them.

Exact current journal/article-type/stage instructions outrank publisher-family assumptions.

## 2. Academic Writing, Review, and Paper Engineering

### 2.1 Sentence-to-sentence logical flow

Academic flow is treated as a reasoning problem first.

For every difficult non-initial sentence:

```text
inherits X
-> relation R
-> adds Y
-> enables Z
```

The system also checks:

- topic/context continuity;
- identity/reference chains;
- given/new progression when appropriate;
- subject–verb distance;
- stress/emphasis position;
- evidence-to-interpretation warrants;
- analysis-to-analysis handoffs;
- connectives only when they label a real relation.

A connective cannot manufacture a missing scientific relationship.

### 2.2 Rich content without bloat

A concise manuscript can still be under-explained. For central ideas/results, the system checks whether the intended reader has the necessary subset of:

- identity/definition;
- motivation;
- mechanism/inferential logic;
- decisive evidence;
- comparator/baseline;
- uncertainty;
- strongest alternative explanation;
- assumption/boundary;
- relationship to prior work;
- scientific consequence;
- visual evidence when prose is inefficient.

The target is **minimum sufficient scientific explanation**, not maximal brevity or maximal word count.

### 2.3 Natural scholarly prose and author voice

When prose feels generic or AI-like, the system does not use detector tricks. It repairs:

`scientific relation -> information flow -> identity chain -> stance -> syntax -> connective -> cadence`

It preserves precise technical repetition where appropriate, uses syntactic variation because rhetorical functions vary, restores meaningful author agency, and runs a separate re-voice pass when representative author prose is available.

No AI-word blacklist. No fake `burstiness`. No deliberate errors.

### 2.4 Learning from many papers without copying

Two complementary layers are used:

- **broad stratified corpus** — dozens/hundreds of papers for descriptive tendencies;
- **3–6 close analogues** — deep reading of claim/evidence dependencies, explanation depth, figure roles, uncertainty, local terminology, and reader assumptions.

Corpus frequencies are not quality scores or acceptance predictors.

Recent cross-archetype reading notes and scalable figure/caption inventory tooling help prevent one local journal pattern from becoming a universal rule.

### 2.5 What belongs in the paper?

The content-selection system prevents **implementation-detail / repository-to-manuscript leakage**.

Candidate content is classified as inference-critical, interpretation-critical, reproducibility-critical, compliance/provenance-critical, orientation-critical, or none, then allocated to:

`main text / main figure / legend / Methods / Extended Data-SI / availability / artifact docs / omit`

File paths, scripts, notebooks, helper functions, config names, output filenames, CLI commands, branches/PRs/CI/tests, and raw project URLs do not earn manuscript space merely because the AI can see them.

### 2.6 Hard final manuscript-surface QA

Content planning alone is not enough because project details can re-enter during later rewrites or caption generation. A final independent gate scans manuscript-facing surfaces for artifact leakage and high-confidence punctuation defects.

Core rule:

> **The audit trail may name the artifact; the manuscript should name the science.**

The final pass also checks punctuation spacing, doubled punctuation, bracket balance, figure-reference formatting, range/minus/hyphen distinctions, units, and target-aware citation/equation/legend typography without blindly altering scientific identifiers.

### 2.7 Figures, plots, and scientific diagrams

Figure planning starts from:

```text
claim
-> reader question
-> scientific/statistical unit
-> estimand / visual object
-> data structure
-> uncertainty / alternative explanation
-> representation
-> main/support/omit
```

There is no universal ideal figure count.

The figure system now has a separate scientific-diagram route for flowcharts, mechanism diagrams, state diagrams, timelines, system schematics, and conceptual illustrations. It can draw on mature vector-layout capabilities such as Graphviz, Schemdraw, Mermaid, custom Matplotlib/SVG, or TikZ when appropriate, while keeping scientific semantics and final visual identity original.

### 2.8 Realistic editor/reviewer iteration

The review loop separates:

`editorial triage -> independent review -> editor synthesis -> revision closure -> targeted re-review`

The editor distinguishes publication/technical blockers from explanation/reporting issues, surface copyediting, claim recalibration, and optional enrichment.

Late new blockers need a real reason, such as revision-introduced regression or newly visible evidence, so the simulation does not create endless moving-goalpost review churn.

Research, reanalysis, new plots from existing data, diagram redesign, writing repair, explanation expansion, citation work, claim narrowing/removal, and retargeting can all be valid repairs. A required real new experiment remains an explicit author-evidence blocker; it is never fabricated.

### 2.9 Research documentation

- [Academic Writing Research: What Strong Papers Actually Do](docs/academic-writing-research_EN.md)
- [Deep Paper Calibration: Learn the Scientific Job, Not the Prestige Surface](docs/deep-paper-calibration_EN.md)
- [Natural Scholarly Writing](docs/natural-scholarly-writing_EN.md)
- [Explanatory Sufficiency](docs/explanatory-sufficiency_EN.md)
- [What Belongs in a Paper — and What Figures Should It Show?](docs/manuscript-content-and-figures_EN.md)
- [All-journals architecture](docs/all-journals-architecture.md)
- [Editor–Reviewer Decision Architecture](docs/editor-reviewer-decision-architecture.md)

## 3. Architecture and Design Principles

### 3.1 Constraint hierarchy

```text
author evidence = truth constraint
paper archetype = evidence/reader-dependency prior
reporting + exact target rules = compliance constraint
broad corpus = descriptive tendency layer
close analogues = manuscript-specific structural/evidence priors
author voice = expression prior
```

Scientific validity outranks every surface style rule.

### 3.2 Published papers are priors, not acceptance hacks

Published papers contain survivorship bias. They show solutions that survived a publication ecology, not which phrase, plot, figure count, or layout caused acceptance.

### 3.3 Review convergence is concern-led

The pipeline continues only while a real must-address concern remains and there is a concrete resolution test. It stops when remaining requests are non-essential enrichment or production copyediting.

### 3.4 Anti-gaming

The system does not recommend friendly-reviewer selection, strategic citation of likely reviewers, hiding adverse evidence/competitors, inflated novelty language, cosmetic experiments, AI-detector evasion, or acceptance-probability optimization.

## 4. Quick Start

After installation, provide the manuscript, data, figures, reviewer letter, sources, repository context, or task description directly.

| Goal | Prompt |
| --- | --- |
| End-to-end iterative paper hardening | `Use academic-paper-pipeline: research, write, review, revise and re-review until the simulated editor says this is publication-ready or a real blocker remains.` |
| Draft/rebuild a manuscript | `Use academic-writing on these claims, data and figures. Resolve the paper archetype and target separately; do not assume Nature style.` |
| Learn from similar papers | `Study a broad comparable corpus for tendencies, then deeply read 4–6 nearest papers and tell me what evidence, figures and section logic we should adopt/adapt/reject.` |
| Naturalize academic prose | `Repair sentence dependencies and natural scholarly flow while preserving my author voice; do not optimize an AI detector.` |
| Check whether content is rich enough | `Audit every central idea for missing rationale, mechanism/inference, evidence, comparator, uncertainty, boundary and consequence. Expand only what readers need.` |
| Decide what belongs in the paper | `Put each source/project item in main text, figure, legend, Methods, SI, availability, artifact docs, or omit; then run the final leakage scrub.` |
| Plan figures/plots | `For each headline claim, choose the reader question, estimand, uncertainty and best representation. Do not choose plots by journal popularity.` |
| Design a scientific diagram | `Build the mechanism/flow topology first, define arrow semantics, then choose an appropriate vector diagram backend and make it publication-ready.` |
| Pre-submission review | `Resolve the target decision model, simulate editor triage and independent reviewers, then synthesize must-address blockers and minimum valid repairs.` |
| Respond to real reviewers | `Parse this decision letter, prioritize editor conditions and blocking concerns, then draft the revision/response package.` |
| Find citations | `Segment these claims and find the best supporting evidence; do not filter by prestige unless I specify a scope.` |
| Deep-read a paper | `Build a source-grounded Paper Card with method logic, experiment-to-claim evidence, boundaries, weaknesses and testable ideas.` |

If you know the skill name, request it explicitly; otherwise describe the task naturally.

## 5. Installation

Skills are complete directories under `skills/`. Many academic-paper skills depend on `skills/nature-shared/`, so install/copy complete directories rather than only `SKILL.md`.

### 5.1 `npx skills`

List skills:

```bash
npx skills add Yuan1z0825/nature-skills --list
```

Install all globally for Codex:

```bash
npx skills add Yuan1z0825/nature-skills --global --agent codex --skill '*' --yes --copy
```

Install canonical academic writing with the shared package:

```bash
npx skills add Yuan1z0825/nature-skills --global --agent codex \
  --skill academic-writing --skill nature-shared --yes --copy
```

For the end-to-end loop also install `academic-paper-pipeline` plus the specialist skills it will call in your agent environment.

Update later:

```bash
npx skills update --global --yes
```

### 5.2 Repository installer

```bash
git clone https://github.com/Yuan1z0825/nature-skills.git
cd nature-skills
scripts/update-codex-skills.sh --pull
scripts/update-codex-skills.sh --check
```

### 5.3 Claude Code and other agents

For Claude Code, OpenClaw, OpenCode, Hermes, and similar frameworks, keep complete skill directories and shared dependencies together. See [the integration guide](docs/open-source-agent-frameworks_EN.md).

Optional Python/R/browser/MCP/diagram dependencies are installed only for skills that require them. Do not commit API keys or provider credentials.

## 6. Skill Index

The current repository exposes **20 triggerable skills**. `nature-shared` and the legacy `nature-writing` implementation are support/reference layers and are not counted here.

| Skill | Status | Purpose | Example Triggers | Details |
|---|---|---|---|---|
| [`academic-paper-pipeline`](skills/academic-paper-pipeline/README_EN.md) | Beta | Closed-loop research, writing, figure/statistics, independent review, editor synthesis, revision and targeted re-review until simulated publication readiness or an explicit blocker | "iterate until publishable", "review and revise repeatedly", "publication-ready pipeline" | [Details](skills/academic-paper-pipeline/README_EN.md) |
| [`academic-writing`](skills/academic-writing/README_EN.md) | Beta | Canonical journal-agnostic manuscript architecture/writing with archetype resolution, self-research fallback, rich explanation, sentence logic, analogue/corpus learning, author voice, figure planning, and final surface QA | "academic writing", "paper drafting", "rewrite Results", "sentence logic" | [Details](skills/academic-writing/README_EN.md) |
| [`nature-academic-search`](skills/nature-academic-search/README_EN.md) | Beta | Multi-source literature search, citation verification, citation metrics, influential-citer profiling, and reference management | "search papers", "literature search", "verify DOI" | [Details](skills/nature-academic-search/README_EN.md) |
| [`nature-citation`](skills/nature-citation/README_EN.md) | Beta | Claim segmentation and best-evidence citation discovery, with explicit journal/prestige scopes and RIS/ENW/Zotero export | "find citations", "supporting evidence", "RIS export" | [Details](skills/nature-citation/README_EN.md) |
| [`nature-data`](skills/nature-data/README_EN.md) | Draft | Data Availability statements, repository plans, FAIR checks | "Data Availability", "FAIR metadata" | [Details](skills/nature-data/README_EN.md) |
| [`nature-downloader`](skills/nature-downloader/README_EN.md) | Beta | Legally obtain academic full text/PDFs through library/open-access routes | "download papers", "library PDF" | [Details](skills/nature-downloader/README_EN.md) |
| [`nature-experiment-log`](skills/nature-experiment-log/README_EN.md) | Draft | Convert experiment images, voice, and text into standardized Obsidian experiment logs | "experiment log", "record experiment" | [Details](skills/nature-experiment-log/README_EN.md) |
| [`nature-figure`](skills/nature-figure/README_EN.md) | Stable | Archetype/claim-driven figure planning, data plots, scientific diagrams, analogue calibration, target adaptation, legend/surface QA, and vector/raster export | "what plots", "scientific figure", "mechanism diagram", "flowchart" | [Details](skills/nature-figure/README_EN.md) |
| [`nature-image2ppt`](skills/nature-image2ppt/README_EN.md) | Beta | Reconstruct slide images/scanned PDFs/image-only PPTX as editable PowerPoint with rendered QA | "image to editable PowerPoint" | [Details](skills/nature-image2ppt/README_EN.md) |
| [`nature-literature-pipeline`](skills/nature-literature-pipeline/README_EN.md) | Stable | Automated literature discovery with retrieval, scoring, deep-reading delivery and local archiving | "literature pipeline", "daily literature" | [Details](skills/nature-literature-pipeline/README_EN.md) |
| [`nature-paper-card`](skills/nature-paper-card/README_EN.md) | Beta | Source-grounded deep reading: method logic, evidence chains, boundaries, critical analysis and research ideas | "Paper Card", "deep-read paper" | [Details](skills/nature-paper-card/README_EN.md) |
| [`nature-paper-to-patent`](skills/nature-paper-to-patent/README_EN.md) | Beta | Evidence-constrained Chinese invention-patent drafting, patent-point mining and prior-art search | "paper to patent", "claims drafting" | [Details](skills/nature-paper-to-patent/README_EN.md) |
| [`nature-paper2ppt`](skills/nature-paper2ppt/README_EN.md) | Beta | Generate Chinese PPTX journal-club/paper-presentation decks from research papers | "paper PPT", "journal club" | [Details](skills/nature-paper2ppt/README_EN.md) |
| [`nature-polishing`](skills/nature-polishing/README_EN.md) | Stable | Journal-aware academic rewriting/translation with explanation, sentence logic, natural prose, author voice, archetype calibration and final surface QA | "polish", "AI-like prose", "sentence flow" | [Details](skills/nature-polishing/README_EN.md) |
| [`nature-proposal-writer`](skills/nature-proposal-writer/README_EN.md) | Beta | Proposal-first research-writing state machine: evidence, argument and section contracts before drafting/review | "researchwrite", "proposal", "research plan" | [Details](skills/nature-proposal-writer/README_EN.md) |
| [`nature-reader`](skills/nature-reader/README_EN.md) | Beta | Full-paper Markdown readers with source anchors, figure-text alignment, rendered equations and Chinese-English translation | "paper reader", "full Markdown" | [Details](skills/nature-reader/README_EN.md) |
| [`nature-ref-verifier`](skills/nature-ref-verifier/README_EN.md) | Stable | Verify reference identity/metadata separately from target-journal rendering and manuscript cross-links | "verify refs", "metadata check" | [Details](skills/nature-ref-verifier/README_EN.md) |
| [`nature-response`](skills/nature-response/README_EN.md) | Beta | Closure-oriented real editor/reviewer response, revision cover letters, marked manuscripts and revision-package checks | "response to reviewers", "major revision", "rebuttal" | [Details](skills/nature-response/README_EN.md) |
| [`nature-reviewer`](skills/nature-reviewer/README_EN.md) | Draft | Journal-aware editor triage, mutually blind reviewer simulation, editor synthesis, archetype/evidence/figure/explanation audit and repair map | "pre-submission review", "reviewer reports" | [Details](skills/nature-reviewer/README_EN.md) |
| [`nature-statistics`](skills/nature-statistics/README_EN.md) | Draft | Statistical design/reporting: units, estimands, p values, multiplicity, effect sizes, intervals, figure statistics and numeric consistency | "statistics review", "p value", "figure statistics" | [Details](skills/nature-statistics/README_EN.md) |

## 7. Contribution and Development

### 7.1 Shared principles

1. Scientific validity first.
2. Canonical public paper writing is `academic-writing`; historical Nature-named directories are compatibility layers unless the target is actually Nature.
3. Resolve paper archetype before borrowing writing/figure conventions.
4. Research unfamiliar paper types/venues instead of guessing.
5. Use broad corpora for tendencies and close analogues for deep reasoning; frequency is not quality.
6. Preserve author evidence and claim boundaries.
7. Make content rich enough to understand without adding filler.
8. Make figures answer reader questions and expose relevant uncertainty/alternatives.
9. Keep project/repository implementation details out of manuscript surfaces.
10. Treat punctuation/scientific typography as final QA, not decorative style.
11. Keep editor/reviewer simulation concern-led and anti-gaming.
12. Add regression tests whenever a shared behavioral contract changes.

### 7.2 Repository layout

```text
skills/
├── academic-paper-pipeline/      # canonical closed-loop orchestration
├── academic-writing/             # canonical manuscript writing router
├── nature-shared/                # shared reasoning/research/journal contracts
├── nature-writing/               # legacy compatibility/reference implementation
├── nature-figure/
├── nature-polishing/
├── nature-reviewer/
├── nature-response/
└── nature-<topic>/...

docs/
├── academic-writing-research_EN.md
├── deep-paper-calibration_EN.md
├── natural-scholarly-writing_EN.md
├── explanatory-sufficiency_EN.md
├── manuscript-content-and-figures_EN.md
├── all-journals-architecture.md
└── editor-reviewer-decision-architecture.md
```

### 7.3 Before submitting changes

Run README mirror/count checks, skill metadata/index validation, the focused academic-paper contracts, specialist tests, and repository tooling. New pipeline/writing/figure behaviors should be regression-tested rather than documented only in prose.

## 8. Project and Community

Founder / maintainer: **Yizhe Yuan (袁一哲)**. The project also includes contributions from core developers and community contributors.

- Website: https://yuan1z0825.github.io/nature-skills/
- Business cooperation: [natureskills2026@outlook.com](mailto:natureskills2026@outlook.com)
- Nature AI service/store: https://apiciyuan.top/
- Open-source agent integration: [docs/open-source-agent-frameworks_EN.md](docs/open-source-agent-frameworks_EN.md)

The broader philosophy remains: research workflows can be made explicit, inspectable, reusable, and continuously research-calibrated — without turning science into a rigid template.

### Star History

[![Star History Chart](assets/star-history-20260819T024318Z.svg)](https://star-history.com/#Yuan1z0825/nature-skills&Date)
