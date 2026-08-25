<div align="center">
  <p>
    <img src="assets/readme-banner-cn.png" alt="Academic Paper Skills：面向学者的可复用科研与论文工作流" width="100%">
  </p>
  <p>
    <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-2ea44f"></a>
    <a href="#5-安装"><img alt="Install" src="https://img.shields.io/badge/install-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw%20%7C%20OpenCode%20%7C%20Hermes-111827"></a>
    <a href="#6-技能索引"><img alt="Skills" src="https://img.shields.io/badge/skills-20-0ea5e9"></a>
    <a href="README_EN.md"><img alt="Language" src="https://img.shields.io/badge/language-中文%20%7C%20English-1f6feb"></a>
  </p>
  <p>
    <a href="https://yuan1z0825.github.io/nature-skills/">在线网站</a>
    · <a href="#4-快速开始">快速开始</a>
    · <a href="#5-安装">安装</a>
    · <a href="#6-技能索引">技能索引</a>
    · <a href="docs/deep-paper-calibration.md">论文深度校准</a>
    · <a href="docs/academic-writing-research.md">学术写作研究</a>
    · <a href="README_EN.md">English</a>
  </p>
</div>

---

这是一个面向 AI agents 的可复用 **academic research + academic paper skill system**。项目最初围绕 Nature 工作流构建，所以很多历史目录仍保留 `nature-*` 名称；但论文系统现在已经是 **journal-agnostic、paper-archetype-aware** 的。

Canonical writing entry point 是 **`academic-writing`**；整篇论文持续迭代的 orchestration entry point 是 **`academic-paper-pipeline`**。Nature 现在只是一个可选 target adapter。

当前 manuscript lifecycle：

```text
target + paper archetype
-> evidence/source intake
-> literature + comparable-paper research
-> argument + claim/evidence architecture
-> content + statistics + figure/diagram planning
-> academic writing
-> sentence/explanation/author-voice repair
-> technical/reporting/surface QA
-> editor triage
-> independent reviewers
-> editor synthesis
-> revision + targeted re-review
   ↳ 真实 blocker 仍存在时继续
-> simulated publication readiness 或 explicit blocker/retarget state
```

目标不是让所有论文“像顶刊”，而是让 science **清楚、内容足够丰富、可辩护、可复现、边界合适、视觉证据可检查，并让目标 reader/editor/reviewer 容易评估**。

## 目录

- [1. 仓库现在是什么](#1-仓库现在是什么)
- [2. Academic Writing、Review 与 Paper Engineering](#2-academic-writingreview-与-paper-engineering)
- [3. 架构与设计原则](#3-架构与设计原则)
- [4. 快速开始](#4-快速开始)
- [5. 安装](#5-安装)
- [6. 技能索引](#6-技能索引)
- [7. 贡献与开发](#7-贡献与开发)
- [8. 项目与社区](#8-项目与社区)

## 1. 仓库现在是什么

### Canonical academic writing，不再是 Nature writing

`academic-writing` 是新的公开 manuscript-writing skill。旧 `nature-writing` 目录只作为 compatibility/reference implementation layer 保留成熟 section fragments、examples 与 corpus scripts，并关闭 implicit invocation。

写作会独立解析：

`paper archetype -> study design/evidence -> intended reader -> article type -> exact target/stage`

不会从一个 Nature 命名推导写作风格。

### Closed-loop manuscript iteration

`academic-paper-pipeline` 在所有轮次维护同一个 manuscript state，并协调：

`research -> writing -> statistics -> figures/diagrams -> review -> editor synthesis -> revision -> re-review`

决定收敛的是 simulated editor，不是 reviewer 票数。Major concerns 有稳定 ID 与 resolution test；major revision 可回到对应 original reviewer，minor clarity/surface issue 在 target process 允许时可以由 editor closure。

成功 terminal state 是 `simulated_publication_ready_for_target`。这是 readiness simulation，不保证真实期刊 accept。

### 不认识的 paper，先 research 再写

如果 paper type、target venue、reporting standard、writing convention 或 figure grammar 无法可靠覆盖，AI session 应先研究：

1. current official target guidance；
2. applicable reporting/methodological standards；
3. 需要时的 comparable recent-paper quick profile；
4. 3–6 篇 nearest-neighbor papers deep reading；
5. 对 apparent convention 的 counterexamples。

然后建立 temporary manuscript-specific archetype profile，而不是硬套 nearest template。

### Paper archetype 高于 journal aesthetics

Shared system 至少区分：

- experimental discovery/mechanism；
- randomized intervention/trial；
- observational/epidemiological/clinical association；
- computational/ML empirical；
- method/tool/software/instrument；
- dataset/resource；
- theory/proof；
- qualitative/interpretive；
- review/systematic review/perspective/synthesis；
- hybrid papers。

Clinical trial、ML benchmark、qualitative interview、mechanism paper、theorem paper 不应该因为都投 selective journal 就共享同一 evidence/figure sequence。

### Evidence before prestige

Citation discovery 默认 best evidence，不默认 CNS/Nature filter。Exact current journal/article-type/stage instructions 高于 publisher-family assumption。

## 2. Academic Writing、Review 与 Paper Engineering

### 2.1 Sentence-to-sentence logical flow

Academic flow 首先是 reasoning problem。

困难段落中，每个非首句检查：

```text
inherits X
-> relation R
-> adds Y
-> enables Z
```

同时检查 topic/context continuity、identity/reference chains、合适时的 given/new progression、subject–verb distance、stress/emphasis、evidence-to-interpretation warrant、analysis-to-analysis handoff，以及 connective 是否真的对应 relation。

Connective 不能替代缺失的 scientific logic。

### 2.2 Rich content without bloat

论文可以很短、语法也正确，但仍然 under-explained。对 central idea/result，系统检查读者是否获得必要的：

- identity/definition；
- motivation；
- mechanism/inferential logic；
- decisive evidence；
- comparator/baseline；
- uncertainty；
- strongest alternative explanation；
- assumption/boundary；
- prior-work relationship；
- scientific consequence；
- prose 不够高效时的 visual evidence。

目标是 **minimum sufficient scientific explanation**，不是最大压缩，也不是最大字数。

### 2.3 Natural scholarly prose + author voice

当 prose 很 generic / AI-like，系统会修：

`scientific relation -> information flow -> identity chain -> stance -> syntax -> connective -> cadence`

它允许必要 technical repetition，按 rhetorical function 变化 syntax，在逻辑/evidence 修好后恢复 author voice。

不做 AI-word blacklist、fake burstiness、deliberate errors 或 detector optimization。

### 2.4 学很多 papers，但不复制

使用两层：

- **broad stratified corpus**：几十/几百篇 comparable papers 的 descriptive tendencies；
- **3–6 close analogues**：深入研究 claim/evidence dependency、explanation depth、figure roles、uncertainty、terminology 与 reader assumptions。

Corpus frequency 不是 quality score，也不是 acceptance predictor。

### 2.5 什么内容应该进入 paper？

Content-selection layer 防止 **implementation-detail / repository-to-manuscript leakage**。

内容先分类为 inference-critical、interpretation-critical、reproducibility-critical、compliance/provenance-critical、orientation-critical 或 none，再分配到：

`main text / main figure / legend / Methods / Extended Data-SI / availability / artifact docs / omit`

File path、script/notebook、helper/function、config/output filename、CLI、branch/PR/CI/test、raw project URL 不会因为 AI 看得到就自动进入 manuscript。

### 2.6 Final manuscript-surface QA

Content planning 还不够，因为后续 rewrite 或 caption generation 仍可能把 project detail 带回来。所有 manuscript-facing surfaces 最终再做一次独立 scrub。

核心规则：

> **Audit trail 可以知道 artifact 名字；manuscript 应该写 science。**

同时检查 punctuation spacing、doubled punctuation、bracket balance、Fig. reference、range/minus/hyphen、units、target-aware citation/equation/legend typography，并保护 scientific identifiers。

### 2.7 Figures、plots 与 scientific diagrams

Figure planning：

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

没有 universal ideal figure count。

Scientific-figure skill 还提供独立 diagram route，可处理 flowchart、mechanism diagram、state diagram、timeline、system schematic 与 conceptual illustration；按需使用 Graphviz、Schemdraw、Mermaid、custom Matplotlib/SVG 或 TikZ 的能力，同时保持 scientific semantics 与最终 visual identity 原创。

### 2.8 更真实的 editor/reviewer iteration

Review loop：

`editorial triage -> independent review -> editor synthesis -> revision closure -> targeted re-review`

Editor 区分 publication/technical blocker、explanation/reporting、surface copyedit、claim recalibration 与 optional enrichment。

Round 1 之后新的 blocker 需要真实理由，例如 revision regression 或 new evidence 暴露新问题，避免 reviewer 不断 moving goalposts。

可做的 repair 包括 research、reanalysis、已有 data 的新 plots、diagram redesign、writing/explanation repair、citation work、claim narrowing/removal 与 retargeting。真实 new experiment/data requirement 会成为 explicit author-evidence blocker，不会被虚构。

### 2.9 研究文档

- [学术写作研究](docs/academic-writing-research.md)
- [深度论文校准](docs/deep-paper-calibration.md)
- [自然学术写作](docs/natural-scholarly-writing.md)
- [解释充分性](docs/explanatory-sufficiency.md)
- [论文内容与图件](docs/manuscript-content-and-figures.md)
- [All-journals architecture](docs/all-journals-architecture.md)
- [Editor–Reviewer Decision Architecture](docs/editor-reviewer-decision-architecture.md)

## 3. 架构与设计原则

### 3.1 Constraint hierarchy

```text
author evidence = truth constraint
paper archetype = evidence/reader-dependency prior
reporting + exact target rules = compliance constraint
broad corpus = descriptive tendency layer
close analogues = manuscript-specific structural/evidence priors
author voice = expression prior
```

Scientific validity 高于所有 surface style rule。

### 3.2 Published papers 是 priors，不是 acceptance hacks

Published papers 有 survivorship bias。它们能告诉我们某个 publication ecology 下哪些解决方案活了下来，但不能证明某种 phrase、plot、figure count 或 layout 导致了 acceptance。

### 3.3 Review convergence 是 concern-led

只有真实 must-address concern 仍存在、且下一轮有 concrete resolution test 时才继续迭代。只剩 optional enrichment / production copyedit 时应停止。

### 3.4 Anti-gaming

不做 friendly-reviewer selection、strategic reviewer citation、隐藏 adverse evidence/competitor、inflated novelty、cosmetic experiment、AI-detector evasion 或 acceptance-probability optimization。

## 4. 快速开始

安装后直接提供 manuscript、data、figures、reviewer letter、sources、repository context 或任务描述。

| 目标 | Prompt |
| --- | --- |
| End-to-end iterative hardening | `使用 academic-paper-pipeline：持续 research、write、review、revise、re-review，直到 simulated editor 判断 publication-ready 或遇到真实 blocker。` |
| Draft/rebuild manuscript | `使用 academic-writing，根据这些 claims/data/figures 重建论文；先解析 paper archetype 与 target，不要假设 Nature style。` |
| Learn from similar papers | `先研究 broad comparable corpus，再精读 4–6 篇 nearest papers，告诉我 evidence、figures、section logic 哪些 adopt/adapt/reject。` |
| Naturalize academic prose | `修复 sentence dependencies 和自然 scholarly flow，保留我的 author voice，不要优化 AI detector。` |
| 检查内容是否足够丰富 | `逐个 central idea 检查 rationale、mechanism/inference、evidence、comparator、uncertainty、boundary、consequence，只展开真正缺失部分。` |
| Decide what belongs | `把每个 source/project item 分配到 main、figure、legend、Methods、SI、availability、artifact docs 或 omit，最后再做 leakage scrub。` |
| Plan figures/plots | `对每个 headline claim 先确定 reader question、estimand、uncertainty，再选最合适 representation，不按 journal popularity 选 plot。` |
| Scientific diagram | `先建立 mechanism/flow topology 和 arrow semantics，再选合适 vector diagram backend。` |
| Pre-submission review | `解析 target decision model，做 editor triage + independent reviewers，再综合 must-address blockers 与 minimum valid repairs。` |
| Real reviewer response | `解析这个 decision letter，先处理 editor conditions 和 blocking concerns，再起草 revision/response package。` |
| Find citations | `拆分 claims 并找 best supporting evidence，除非我指定，不按 prestige filter。` |
| Deep-read paper | `做 source-grounded Paper Card：method logic、evidence chain、boundaries、weaknesses、testable ideas。` |

知道 skill name 可以直接指定，否则自然描述任务即可。

## 5. 安装

Skills 以完整目录放在 `skills/`。很多 academic-paper skills 依赖 `skills/nature-shared/`，因此应复制完整 skill directory，而不是只拷 `SKILL.md`。

### 5.1 `npx skills`

列出 skills：

```bash
npx skills add Yuan1z0825/nature-skills --list
```

为 Codex 全量安装：

```bash
npx skills add Yuan1z0825/nature-skills --global --agent codex --skill '*' --yes --copy
```

安装 canonical academic writing + shared：

```bash
npx skills add Yuan1z0825/nature-skills --global --agent codex \
  --skill academic-writing --skill nature-shared --yes --copy
```

需要完整闭环时，再安装 `academic-paper-pipeline` 与你的 agent 环境中需要调用的 specialist skills。

更新：

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

### 5.3 Claude Code 与其他 agents

Claude Code、OpenClaw、OpenCode、Hermes 等请保持 complete skill directories + shared dependencies 一起安装。参见 [integration guide](docs/open-source-agent-frameworks.md)。

Optional Python/R/browser/MCP/diagram dependencies 只按需要安装。不要提交 API keys/provider credentials。

## 6. 技能索引

当前仓库公开 **20 个 triggerable skills**。`nature-shared` 与 legacy `nature-writing` 是 support/reference layer，不计入。

| Skill | Status | Purpose | Example Triggers | Details |
|---|---|---|---|---|
| [`academic-paper-pipeline`](skills/academic-paper-pipeline/README.md) | Beta | Closed-loop research、writing、figure/statistics、independent review、editor synthesis、revision、targeted re-review，直到 simulated publication readiness 或 explicit blocker | "iterate until publishable", "反复 review/revise", "publication-ready pipeline" | [详情](skills/academic-paper-pipeline/README.md) |
| [`academic-writing`](skills/academic-writing/README.md) | Beta | Canonical journal-agnostic manuscript writing：archetype resolution、self-research fallback、rich explanation、sentence logic、corpus/analogue learning、author voice、figure planning、surface QA | "academic writing", "论文写作", "rewrite Results", "句间逻辑" | [详情](skills/academic-writing/README.md) |
| [`nature-academic-search`](skills/nature-academic-search/README.md) | Beta | Multi-source literature search、citation verification、metrics 与 reference management | "search papers", "文献检索", "verify DOI" | [详情](skills/nature-academic-search/README.md) |
| [`nature-citation`](skills/nature-citation/README.md) | Beta | Claim segmentation + best-evidence citation discovery，保留显式 journal/prestige scope 与 RIS/ENW/Zotero export | "find citations", "supporting evidence", "RIS export" | [详情](skills/nature-citation/README.md) |
| [`nature-data`](skills/nature-data/README.md) | Draft | Data Availability、repository plan 与 FAIR checks | "Data Availability", "FAIR metadata" | [详情](skills/nature-data/README.md) |
| [`nature-downloader`](skills/nature-downloader/README.md) | Beta | 通过 library/open-access 合法获取 academic full text/PDF | "download papers", "library PDF" | [详情](skills/nature-downloader/README.md) |
| [`nature-experiment-log`](skills/nature-experiment-log/README.md) | Draft | 将实验 image/voice/text 转成 standardized Obsidian experiment logs | "experiment log", "实验记录" | [详情](skills/nature-experiment-log/README.md) |
| [`nature-figure`](skills/nature-figure/README.md) | Stable | Archetype/claim-driven figure planning、data plots、scientific diagrams、analogue calibration、target adaptation、legend/surface QA 与 export | "what plots", "科研作图", "机制图", "flowchart" | [详情](skills/nature-figure/README.md) |
| [`nature-image2ppt`](skills/nature-image2ppt/README.md) | Beta | 将 slide image/scanned PDF/image-only PPTX 重建为 editable PowerPoint | "image to editable PowerPoint" | [详情](skills/nature-image2ppt/README.md) |
| [`nature-literature-pipeline`](skills/nature-literature-pipeline/README.md) | Stable | 自动 literature discovery、retrieval、scoring、deep-reading delivery、local archive | "literature pipeline", "daily literature" | [详情](skills/nature-literature-pipeline/README.md) |
| [`nature-paper-card`](skills/nature-paper-card/README.md) | Beta | Source-grounded deep reading：method logic、evidence chains、boundaries、critical analysis、research ideas | "Paper Card", "deep-read paper" | [详情](skills/nature-paper-card/README.md) |
| [`nature-paper-to-patent`](skills/nature-paper-to-patent/README.md) | Beta | Evidence-constrained Chinese patent drafting、patent-point mining、prior-art search | "paper to patent", "claims drafting" | [详情](skills/nature-paper-to-patent/README.md) |
| [`nature-paper2ppt`](skills/nature-paper2ppt/README.md) | Beta | 从 research paper 生成中文 journal-club/paper-presentation PPTX | "paper PPT", "journal club" | [详情](skills/nature-paper2ppt/README.md) |
| [`nature-polishing`](skills/nature-polishing/README.md) | Stable | Journal-aware academic rewriting/translation：explanation、sentence logic、natural prose、author voice、archetype calibration、surface QA | "polish", "AI-like prose", "sentence flow" | [详情](skills/nature-polishing/README.md) |
| [`nature-proposal-writer`](skills/nature-proposal-writer/README.md) | Beta | Proposal-first research-writing state machine：draft/review 前先建立 evidence/argument/section contracts | "researchwrite", "proposal", "research plan" | [详情](skills/nature-proposal-writer/README.md) |
| [`nature-reader`](skills/nature-reader/README.md) | Beta | Full-paper Markdown reader：source anchors、figure-text alignment、equations、中英翻译 | "paper reader", "full Markdown" | [详情](skills/nature-reader/README.md) |
| [`nature-ref-verifier`](skills/nature-ref-verifier/README.md) | Stable | Reference identity/metadata verification，与 target rendering/cross-links 分离 | "verify refs", "metadata check" | [详情](skills/nature-ref-verifier/README.md) |
| [`nature-response`](skills/nature-response/README.md) | Beta | 真实 editor/reviewer decision 的 closure-oriented response、cover letter、marked manuscript、revision-package checks | "response to reviewers", "major revision", "rebuttal" | [详情](skills/nature-response/README.md) |
| [`nature-reviewer`](skills/nature-reviewer/README.md) | Draft | Journal-aware editor triage、mutually blind reviewers、editor synthesis、archetype/evidence/figure/explanation audit | "pre-submission review", "reviewer reports" | [详情](skills/nature-reviewer/README.md) |
| [`nature-statistics`](skills/nature-statistics/README.md) | Draft | Statistical design/reporting：units、estimands、p values、multiplicity、effect sizes、intervals、figure stats | "statistics review", "p value", "figure statistics" | [详情](skills/nature-statistics/README.md) |

## 7. 贡献与开发

### 7.1 Shared principles

1. Scientific validity first。
2. Canonical public paper writing 是 `academic-writing`；Nature-named legacy directory 只做 compatibility，除非 target 真的是 Nature。
3. 先解析 paper archetype，再借鉴 writing/figure convention。
4. 不熟悉的 paper/venue 先 research，不猜规则。
5. Broad corpus 学 tendency，close analogues 学 deep reasoning；frequency 不是 quality。
6. Preserve author evidence 与 claim boundaries。
7. 内容要足够理解，但不加 filler。
8. Figures 必须回答 reader questions 并暴露关键 uncertainty/alternatives。
9. Project/repository implementation detail 不得泄漏到 manuscript surface。
10. Punctuation/scientific typography 是 final QA，不是装饰。
11. Editor/reviewer simulation concern-led、anti-gaming。
12. Shared behavior 改动必须加 regression tests。

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
├── academic-writing-research.md
├── deep-paper-calibration.md
├── natural-scholarly-writing.md
├── explanatory-sufficiency.md
├── manuscript-content-and-figures.md
├── all-journals-architecture.md
└── editor-reviewer-decision-architecture.md
```

### 7.3 提交前

运行 README mirror/count、skill metadata/index validation、focused academic-paper contracts、specialist tests 与 repository tooling。新 pipeline/writing/figure behavior 应由 regression tests 保护，而不是只写文档。

## 8. 项目与社区

Founder / maintainer: **Yizhe Yuan（袁一哲）**。项目也包含 core developers 与 community contributors 的贡献。

- Website: https://yuan1z0825.github.io/nature-skills/
- 商务合作: [natureskills2026@outlook.com](mailto:natureskills2026@outlook.com)
- Nature AI service/store: https://apiciyuan.top/
- Open-source agent integration: [docs/open-source-agent-frameworks.md](docs/open-source-agent-frameworks.md)

更广泛的理念保持不变：research workflows 可以被显式化、检查、复用并持续通过 research 校准，但不能把 science 变成 rigid template。

### Star History

[![Star History Chart](assets/star-history-20260819T024318Z.svg)](https://star-history.com/#Yuan1z0825/nature-skills&Date)
