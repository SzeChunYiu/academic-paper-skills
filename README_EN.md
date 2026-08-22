<div align="center">
  <p>
    <img src="assets/readme-banner-en.png" alt="Nature Skills: Reusable Research Skills for AI Scholars" width="100%">
  </p>
  <p>
    <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-2ea44f"></a>
    <a href="#5-installation"><img alt="Install" src="https://img.shields.io/badge/install-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw%20%7C%20OpenCode%20%7C%20Hermes-111827"></a>
    <a href="#6-skill-index"><img alt="Skills" src="https://img.shields.io/badge/skills-19-0ea5e9"></a>
    <a href="README.md"><img alt="Language" src="https://img.shields.io/badge/language-English%20%7C%20中文-1f6feb"></a>
  </p>
  <p>
    <a href="https://yuan1z0825.github.io/nature-skills/">Website</a>
    · <a href="#4-quick-start">Quick Start</a>
    · <a href="#5-installation">Install</a>
    · <a href="#6-skill-index">Skill Index</a>
    · <a href="docs/academic-writing-research_EN.md">Writing Research</a>
    · <a href="docs/manuscript-content-and-figures_EN.md">Content & Figures</a>
    · <a href="README.md">中文</a>
  </p>
</div>

---

`nature-skills` is a reusable academic-research skill system for AI agents. The historical `nature-*` names remain for compatibility, but **the academic-paper workflows are no longer Nature-only**: journal choice, article type, discipline, study design, evidence standard, writing style, editorial objective, and submission stage are resolved independently.

The current paper workflow is evidence-first:

```text
best evidence
-> scientific argument
-> manuscript content selection
-> close analogue-paper study
-> figure/evidence planning
-> natural scholarly prose + author voice
-> exact journal/reporting adaptation
-> editor/reviewer preflight
-> revision closure
```

The goal is not to make every paper sound prestigious. The goal is to make the science **clear, defensible, reproducible, appropriately scoped, and easy for the intended editor/reviewer/reader to evaluate**.

## Table of Contents

- [1. What This Repository Has Become](#1-what-this-repository-has-become)
- [2. Academic Writing and Paper Engineering](#2-academic-writing-and-paper-engineering)
- [3. Architecture and Design Principles](#3-architecture-and-design-principles)
- [4. Quick Start](#4-quick-start)
- [5. Installation](#5-installation)
- [6. Skill Index](#6-skill-index)
- [7. Contribution and Development](#7-contribution-and-development)
- [8. Project and Community](#8-project-and-community)

## 1. What This Repository Has Become

The repository started around Nature-oriented research workflows. It now provides a broader academic-paper architecture while keeping the old names so existing installations do not break.

### Journal-aware, not journal-hard-coded

Shared journal resolution uses:

`exact journal -> article/content type -> submission stage -> output component`

Current exact official instructions outrank local profiles. Publisher-family profiles are fallbacks, not submission contracts.

### Evidence before prestige

Citation discovery defaults to **best evidence**, not Nature/Science/Cell filtering. Explicit `nature`, `science`, `cell`, `cns`, and `flagship` scopes remain available when requested.

### Writing is a research engine

The writing system is grounded in cross-disciplinary rhetorical/corpus research, direct reading of published papers, close analogue-paper study, and exact target requirements. It does not enforce one Introduction template, one Results style, one Discussion ladder, or one sentence pattern across disciplines.

### Editor/reviewer decision engineering

The review system separates:

`editorial triage -> independent reviewers -> editor synthesis -> revision closure`

It does not average a universal acceptance score or count reviewer votes. A concern can be closed by evidence, reanalysis, correction, restructuring, claim narrowing/removal, or a better target/article type.

### Figures are evidence units

Figure planning starts with:

`claim -> reader question -> estimand -> data structure -> uncertainty/alternative explanation -> plot`

A plot is not chosen because it is common in a top journal. Main figures contain the shortest sufficient visual evidence chain; supporting diagnostics/robustness go to Extended Data/SI when appropriate.

## 2. Academic Writing and Paper Engineering

The writing layer has been substantially rebuilt.

### 2.1 Natural scholarly prose, not AI-detector evasion

When prose feels machine-like, the system does **not** maintain an `AI-word` blacklist or randomize sentence lengths. It repairs the reasoning path:

`proposition -> dependency -> information progression -> identity/reference chain -> stance -> syntax -> connective -> cadence`

For each difficult non-initial sentence:

`inherits X -> relation R -> adds Y -> enables Z`

This detects a common failure where every sentence is individually polished but the paragraph has no real dependency.

The system also preserves controlled repetition of technical terms when the referent is unchanged, uses syntactic variation only when rhetorical function changes, and restores the author's own voice after major restructuring.

### 2.2 Analogue-paper calibration

For substantial rewrites, the system can close-read roughly **3–6 genuinely comparable papers** when available, matched by question/contribution type, study design, evidence/data type, article type, subfield, and target venue.

It learns:

- how the research need is created;
- evidence sequence;
- figure roles;
- what data/controls/uncertainty are visible;
- what belongs in main text versus Methods/SI;
- local stance/signposting/background conventions.

It learns functions and relations, not sentences or visual identity.

### 2.3 What belongs in the paper?

A new content-selection layer prevents **implementation-detail leakage / repository-to-manuscript leakage**.

Before content enters the manuscript it is classified as:

- inference-critical;
- interpretation-critical;
- reproducibility-critical;
- compliance/provenance-critical;
- orientation-critical;
- or none.

Then it is assigned to:

`main text / main figure / legend / Methods / Extended Data/SI / Data-Code-Resource Availability / repository docs / omit`

File paths, helper names, setup commands, configs, internal modules, CI/unit-test details, and repeated repository URLs no longer automatically leak into prose.

A useful test is:

> If the implementation were rewritten from scratch but the scientific method/results stayed the same, would this detail still matter to the paper?

### 2.4 Plot suggestions before rendering

The system can suggest plots from the actual scientific question:

- distributions -> raw points/distribution-aware displays;
- paired effects -> paired changes/differences;
- time/dose -> meaningful trajectories;
- association -> scatter/hexbin with justified model if needed;
- classification -> ROC/precision–recall/operating points as appropriate;
- calibration -> reliability/calibration displays;
- survival -> censoring-aware curves;
- heterogeneity -> forest/stratified effect displays;
- benchmark -> task/site/run-level comparisons when variation matters;
- robustness -> sensitivity curves/intervals/small multiples;
- imaging -> representative image plus quantitative evidence when making population-level claims;
- null results -> effect estimates + uncertainty/equivalence logic;
- qualitative/theory -> no forced quantitative plot.

Detailed guide: [What Belongs in a Paper — and What Figures Should It Show?](docs/manuscript-content-and-figures_EN.md)

### 2.5 Research documentation

- [Academic Writing Research: What Strong Papers Actually Do](docs/academic-writing-research_EN.md)
- [Natural Scholarly Writing: A Practical Sentence-to-Sentence Guide](docs/natural-scholarly-writing_EN.md)
- [What Belongs in a Paper — and What Figures Should It Show?](docs/manuscript-content-and-figures_EN.md)
- [All-journals architecture](docs/all-journals-architecture.md)
- [Editor–Reviewer Decision Architecture](docs/editor-reviewer-decision-architecture.md)

## 3. Architecture and Design Principles

### 3.1 Truth, compliance, structure, voice

The writing architecture keeps different constraints separate:

```text
author evidence = truth constraint
journal/reporting rules = compliance constraint
analogue papers = structural/evidence priors
author voice = expression prior
```

Scientific validity outranks every surface style rule.

### 3.2 Evidence completeness is not main-text completeness

The complete evidential/reproducibility record can live across the manuscript, Methods, figures/tables, Extended Data/SI, source data, availability statements, and repositories.

The main text should contain the **minimum sufficient reader-facing evidence chain**, including any negative/boundary evidence that changes the headline interpretation.

### 3.3 Contribution type matters

A mechanism paper, clinical cohort, machine-learning benchmark, method/tool paper, dataset/resource, theory paper, qualitative study, and review need different evidence/figure architectures.

For example, a strong methods paper may need performance validation, ground truth/gold standard where available, benchmarking, reproducibility, general applicability, and distinct applications. A clinical generalization claim may need site/population-stratified performance, calibration, absolute clinical quantities, or time-to-event evidence rather than a single pooled metric.

### 3.4 Published papers are priors, not causal acceptance hacks

Published-paper patterns have survivorship bias. They can show how authors solved rhetorical/evidentiary problems under a publication ecology, but they do not prove that a phrase, figure count, or layout caused acceptance.

### 3.5 Anti-gaming

The system does not recommend:

- friendly-reviewer selection;
- strategic citation of likely reviewers;
- hiding close competitors/adverse evidence;
- inflated novelty/significance wording;
- cosmetic experiments;
- burying conclusion-changing limitations in SI;
- AI-detector evasion tricks.

## 4. Quick Start

After installation, give the agent the manuscript, paper, figures, reviewer letter, code/project context, or task description directly.

| Goal | Prompt |
| --- | --- |
| Read a paper / bilingual reader | `Turn this PDF into a figure-aware Chinese-English Markdown reader with source anchors.` |
| Deep-read a paper | `Build a Paper Card: method logic, evidence-to-claim chain, boundaries, weaknesses, and testable ideas.` |
| Draft/rebuild a manuscript | `Use these claims, data and figures to rebuild the paper argument. Do not assume Nature style; resolve the target separately.` |
| Learn from similar papers | `Find/read 4–6 genuinely comparable papers first, then tell me what evidence, figures and section logic our paper should adopt/adapt/reject.` |
| Naturalize academic prose | `This paragraph sounds generic/AI-written. Repair sentence dependencies and natural scholarly flow while preserving my author voice; do not optimize an AI detector.` |
| Decide what belongs in the paper | `Audit these notes/code/repository materials. Put each item in main text, figure, legend, Methods, SI, availability, repository docs, or omit.` |
| Plan figures/plots | `For each headline claim, propose whether a figure is needed and the best plot from the estimand/data structure/uncertainty. Don't choose plots by journal popularity.` |
| Pre-submission review | `Resolve this journal's decision model, simulate editor triage, run independent reviewers, then synthesize blockers and minimum valid repairs.` |
| Respond to reviewers | `Parse this decision letter, prioritize editor conditions and blocking concerns, then draft point-by-point responses and manuscript changes.` |
| Find citations | `Segment these claims and find the best supporting evidence. Do not filter by prestige unless I specify a scope.` |
| Generate paper presentation | `Create a Chinese journal-club PPT from this paper, keeping key figures and source labels.` |

If you already know the skill name, explicitly request it; otherwise describe the task naturally.

## 5. Installation

`nature-skills` is organized as complete skill directories under `skills/`. Many router-style skills depend on `skills/nature-shared/`, so **install/copy complete directories rather than only `SKILL.md`**.

### 5.1 `npx skills`

List available skills:

```bash
npx skills add Yuan1z0825/nature-skills --list
```

Install all skills globally for Codex:

```bash
npx skills add Yuan1z0825/nature-skills --global --agent codex --skill '*' --yes --copy
```

Install one skill plus the shared package when needed:

```bash
npx skills add Yuan1z0825/nature-skills --global --agent codex \
  --skill nature-writing --skill nature-shared --yes --copy
```

Update later:

```bash
npx skills update --global --yes
```

### 5.2 Codex repository installer

```bash
git clone https://github.com/Yuan1z0825/nature-skills.git
cd nature-skills
scripts/update-codex-skills.sh --pull
scripts/update-codex-skills.sh --check
```

The installer syncs complete top-level skill directories into Codex and verifies the copied contents.

### 5.3 Claude Code

Keep a stable clone and either point subagent/slash-command wrappers to the real `skills/*/SKILL.md` files or use `scripts/autoupdate-skills.sh` to sync complete skills into `~/.claude/skills/`.

Example sync:

```bash
git clone https://github.com/Yuan1z0825/nature-skills.git ~/ai-skills/nature-skills
~/ai-skills/nature-skills/scripts/autoupdate-skills.sh --force
```

### 5.4 Other agents and optional runtimes

For OpenClaw, OpenCode, Hermes, and similar frameworks, see [the integration guide](docs/open-source-agent-frameworks_EN.md).

Optional Python/R/browser/MCP dependencies are installed only for the skills that require them. Do not commit API keys or provider credentials.

## 6. Skill Index

The current `skills/` directory contains 19 triggerable skills. `nature-shared` is an internal support package and is not counted here.

| Skill | Status | Purpose | Example Triggers | Details |
|---|---|---|---|---|
| [`nature-figure`](skills/nature-figure/README_EN.md) | Stable | Claim-driven scientific figure planning + Python/R rendering, analogue-figure calibration, main/support allocation, journal adaptation, and visual/source-data QA | "what plots should I make", "scientific figure", "publication plot", "Figure 1", "graphical abstract" | [Details](skills/nature-figure/README_EN.md) |
| [`nature-polishing`](skills/nature-polishing/README_EN.md) | Stable | Journal-aware academic rewriting/translation with sentence-dependency repair, natural scholarly prose, analogue calibration, author-voice preservation, and manuscript consistency checks | "polish", "natural academic writing", "AI-like prose", "sentence flow", "journal transfer" | [Details](skills/nature-polishing/README_EN.md) |
| [`nature-writing`](skills/nature-writing/README_EN.md) | Draft | Evidence-first manuscript architecture, content selection, analogue-paper study, plot suggestions, natural prose/author voice, editor-reviewer preflight, and first-submission planning | "paper writing", "rewrite Results", "what belongs in paper", "similar papers", "editor perspective" | [Details](skills/nature-writing/README_EN.md) |
| [`nature-reviewer`](skills/nature-reviewer/README_EN.md) | Draft | Journal-aware editor-triage + mutually blind reviewer simulation + editor synthesis + decision-relevant repair map | "pre-submission review", "editor perspective", "reviewer reports", "rejection risk" | [Details](skills/nature-reviewer/README_EN.md) |
| [`nature-citation`](skills/nature-citation/README_EN.md) | Beta | Claim segmentation and best-evidence citation discovery by default, with explicit Nature/CNS/flagship scopes and RIS/ENW/Zotero export | "find citations", "supporting evidence", "CNS citation", "RIS export" | [Details](skills/nature-citation/README_EN.md) |
| [`nature-data`](skills/nature-data/README_EN.md) | Draft | Prepare Data Availability statements, repository plans, and FAIR checks | "Data Availability", "repository", "FAIR metadata" | [Details](skills/nature-data/README_EN.md) |
| [`nature-statistics`](skills/nature-statistics/README_EN.md) | Draft | Audit/draft statistical design and reporting: experimental units, estimands, p values, multiplicity, effect sizes, intervals, figure stats, numeric consistency | "statistics review", "p value", "sample size", "figure statistics" | [Details](skills/nature-statistics/README_EN.md) |
| [`nature-reader`](skills/nature-reader/README_EN.md) | Beta | Full-paper Markdown readers with source anchors, figure-text alignment, rendered equations, and Chinese-English translation | "paper reader", "full Markdown", "figure-text alignment", "translation" | [Details](skills/nature-reader/README_EN.md) |
| [`nature-paper-card`](skills/nature-paper-card/README_EN.md) | Beta | Source-grounded deep reading: method logic, experiment-to-claim evidence, conclusion boundaries, critical analysis, and research ideas | "Paper Card", "deep-read paper", "evidence chain" | [Details](skills/nature-paper-card/README_EN.md) |
| [`nature-response`](skills/nature-response/README_EN.md) | Beta | Parse editor/reviewer decisions and build closure-oriented rebuttals, cover letters, marked manuscripts, and revision-package checks | "response to reviewers", "major revision", "rebuttal", "revision letter" | [Details](skills/nature-response/README_EN.md) |
| [`nature-paper2ppt`](skills/nature-paper2ppt/README_EN.md) | Beta | Generate Chinese PPTX journal-club/paper-presentation decks from research papers | "paper PPT", "journal club", "paper to slides" | [Details](skills/nature-paper2ppt/README_EN.md) |
| [`nature-image2ppt`](skills/nature-image2ppt/README_EN.md) | Beta | Reconstruct slide images, scanned PDFs, and image-only PPTX as object-level editable PowerPoint with rendered QA | "image to editable PowerPoint", "scanned PDF to PPTX" | [Details](skills/nature-image2ppt/README_EN.md) |
| [`nature-paper-to-patent`](skills/nature-paper-to-patent/README_EN.md) | Beta | Evidence-constrained Chinese invention-patent drafting, patent-point mining, prior-art search, and technical-disclosure iteration | "paper to patent", "Chinese patent", "claims drafting" | [Details](skills/nature-paper-to-patent/README_EN.md) |
| [`nature-ref-verifier`](skills/nature-ref-verifier/README_EN.md) | Stable | Verify reference identity/metadata separately from target-journal rendering and manuscript cross-links | "verify refs", "reference verification", "metadata check" | [Details](skills/nature-ref-verifier/README_EN.md) |
| [`nature-academic-search`](skills/nature-academic-search/README_EN.md) | Beta | Multi-source literature search, citation verification, citation metrics, influential-citer profiling, and reference management | "search papers", "literature search", "verify DOI", "citation table" | [Details](skills/nature-academic-search/README_EN.md) |
| [`nature-downloader`](skills/nature-downloader/README_EN.md) | Beta | Legally obtain academic full text/PDFs through library access, browser login state, and open-access routes | "download papers", "library PDF", "CARSI" | [Details](skills/nature-downloader/README_EN.md) |
| [`nature-literature-pipeline`](skills/nature-literature-pipeline/README_EN.md) | Stable | Automated literature discovery pipeline with retrieval, scoring, deep-reading delivery, and local archiving | "literature pipeline", "daily literature", "cron" | [Details](skills/nature-literature-pipeline/README_EN.md) |
| [`nature-experiment-log`](skills/nature-experiment-log/README_EN.md) | Draft | Convert experiment images, voice, and text into standardized Obsidian experiment logs with archived sources | "experiment log", "record experiment", "Obsidian" | [Details](skills/nature-experiment-log/README_EN.md) |
| [`nature-proposal-writer`](skills/nature-proposal-writer/README_EN.md) | Beta | Proposal-first research-writing state machine: establish evidence, argument, and section contracts before drafting/review | "researchwrite", "proposal", "research plan", "writing QA" | [Details](skills/nature-proposal-writer/README_EN.md) |

## 7. Contribution and Development

### 7.1 Shared design principles

1. **Scientific validity first.** Journal prestige, style, and aesthetics never override evidence.
2. **Use primary/current sources for rules.** Exact journal requirements should come from the current target, not another journal in the same publisher family.
3. **Separate functions.** Evidence selection, writing logic, author voice, figures, reporting, house style, and artifact documentation are different layers.
4. **Research writing rules empirically.** Prefer cross-disciplinary corpus evidence, direct reading, and explicit counterexamples over one-author intuition.
5. **Learn from analogues without cloning.** Extract functions/relations/evidence architecture, not sentences or visual identity.
6. **Prevent repository leakage.** Code/project artifacts must be translated to scientific abstractions and allocated to the correct publication layer.
7. **Make figures answer questions.** Plot choice follows estimand/data structure/uncertainty, not journal fashion.
8. **Preserve author voice after repair.** Natural scholarly prose is the quality floor; author voice is the identity layer.
9. **No detector/reviewer gaming.** Do not optimize AI-detector scores or manipulate peer-review systems.
10. **Regression-test contracts.** New shared behavior should be protected by focused tests and repository validators.

### 7.2 Repository layout

```text
skills/
├── nature-shared/                # shared reasoning/journal contracts
├── nature-writing/
├── nature-polishing/
├── nature-figure/
├── nature-reviewer/
├── nature-response/
└── nature-<topic>/...

docs/
├── all-journals-architecture.md
├── editor-reviewer-decision-architecture.md
├── academic-writing-research_EN.md
├── natural-scholarly-writing_EN.md
└── manuscript-content-and-figures_EN.md
```

Each triggerable skill keeps human-facing `README.md` / `README_EN.md`, a governing `SKILL.md`, and `manifest.yaml`; complex skills route to modular `references/`, `static/`, scripts, and shared contracts.

### 7.3 Before submitting changes

At minimum run the repository validators and focused tests, including README mirror/count checks, skill metadata/index validation, journal-generalization contracts, writing/figure/shared tests, and `git diff --check`.

## 8. Project and Community

Founder / maintainer: **Yizhe Yuan (袁一哲)**. The project also includes contributions from core developers and community contributors.

Public community/resources retained from the project:

- Website: https://yuan1z0825.github.io/nature-skills/
- Business cooperation: [natureskills2026@outlook.com](mailto:natureskills2026@outlook.com)
- Nature AI service/store: https://apiciyuan.top/
- Open-source agent integration: [docs/open-source-agent-frameworks_EN.md](docs/open-source-agent-frameworks_EN.md)

The project's broader philosophy remains: research workflows can be made explicit, inspectable, and reusable as agent skills — but the workflows should remain grounded in the science rather than becoming rigid templates.

### Star History

[![Star History Chart](assets/star-history-20260819T024318Z.svg)](https://star-history.com/#Yuan1z0825/nature-skills&Date)
