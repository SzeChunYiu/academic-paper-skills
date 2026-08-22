<div align="center">
  <p>
    <img src="assets/readme-banner-cn.png" alt="Nature Skills：面向全球学者的科研 Skill 库" width="100%">
  </p>
  <p>
    <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-2ea44f"></a>
    <a href="#5-安装"><img alt="Install" src="https://img.shields.io/badge/install-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw%20%7C%20OpenCode%20%7C%20Hermes-111827"></a>
    <a href="#6-技能索引"><img alt="Skills" src="https://img.shields.io/badge/skills-19-0ea5e9"></a>
    <a href="README_EN.md"><img alt="Language" src="https://img.shields.io/badge/language-中文%20%7C%20English-1f6feb"></a>
  </p>
  <p>
    <a href="https://yuan1z0825.github.io/nature-skills/">在线网站</a>
    · <a href="#4-快速开始">快速开始</a>
    · <a href="#5-安装">安装</a>
    · <a href="#6-技能索引">技能索引</a>
    · <a href="docs/academic-writing-research.md">学术写作研究</a>
    · <a href="docs/manuscript-content-and-figures.md">论文内容与图件</a>
    · <a href="README_EN.md">English</a>
  </p>
</div>

---

`nature-skills` 是面向 AI Agent 的可复用科研 Skill 系统。历史上的 `nature-*` 名称继续保留以保证兼容，但**学术论文工作流已经不再是 Nature-only**：target journal、article type、discipline、study design、evidence standard、writing style、editorial objective 和 submission stage 都会独立解析。

当前 paper workflow 是 evidence-first：

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

目标不是让每篇论文都“像顶刊”，而是让 science **清楚、可辩护、可复现、边界准确，并让目标 editor/reviewer/reader 容易评价**。

## 目录

- [1. 这个仓库现在是什么](#1-这个仓库现在是什么)
- [2. 学术写作与论文工程](#2-学术写作与论文工程)
- [3. 架构与设计原则](#3-架构与设计原则)
- [4. 快速开始](#4-快速开始)
- [5. 安装](#5-安装)
- [6. 技能索引](#6-技能索引)
- [7. 贡献与开发](#7-贡献与开发)
- [8. 项目与社区](#8-项目与社区)

## 1. 这个仓库现在是什么

项目最初围绕 Nature-oriented research workflow 建设，现在已经扩展成更一般的 academic-paper architecture，同时保留原目录名避免已有安装失效。

### Journal-aware，而不是 hard-coded journal style

共享 journal resolver 使用：

`exact journal -> article/content type -> submission stage -> output component`

当前 exact official instruction 高于本地 profile；publisher-family profile 只是 fallback，不是 submission contract。

### Evidence 优先于 prestige

Citation discovery 默认使用 **best evidence**，不再自动筛 Nature/Science/Cell。只有明确要求时才启用 `nature`、`science`、`cell`、`cns`、`flagship` scope。

### Writing 是 research engine

写作系统基于跨学科 rhetorical/corpus research、真实论文 direct reading、close analogue-paper study 和 exact target requirement，不会把一种 Introduction、Results、Discussion 或 sentence template 强行推广到所有学科。

### Editor/reviewer decision engineering

评审系统区分：

`editorial triage -> independent reviewers -> editor synthesis -> revision closure`

不会用 universal acceptance score，也不会数 reviewer votes。Concern 可以通过 evidence、reanalysis、correction、restructuring、claim narrowing/removal 或更合适的 target/article type 关闭。

### Figures 是 evidence units

Figure planning 从：

`claim -> reader question -> estimand -> data structure -> uncertainty/alternative explanation -> plot`

开始，而不是“顶刊通常画什么”。Main figures 放最短充分 visual evidence chain；supporting diagnostics/robustness 在适合时进入 Extended Data/SI。

## 2. 学术写作与论文工程

写作层已经做了大幅重构。

### 2.1 Natural scholarly prose，而不是 AI-detector evasion

文本有“AI 味”时，系统不会维护 `AI-word` blacklist，也不会随机化句长，而是修 reader-facing reasoning：

`proposition -> dependency -> information progression -> identity/reference chain -> stance -> syntax -> connective -> cadence`

对困难段落中第一句之后的每一句：

`inherits X -> relation R -> adds Y -> enables Z`

它能抓住一种常见问题：每句话单独都很“漂亮”，但彼此没有真正 dependency。

系统还会允许在 referent 不变时精准重复 technical term，只在 rhetorical function 改变时做 syntax variation，并在大重构后恢复作者自己的 voice。

### 2.2 Analogue-paper calibration

对于 substantial rewrite，系统可以在可用时精读大约 **3–6 篇真正可比的论文**，按 question/contribution type、study design、evidence/data type、article type、subfield 与 target venue 匹配。

学习：

- research need 如何创建；
- evidence sequence；
- figure roles；
- data/control/uncertainty 如何展示；
- main text vs Methods/SI；
- local stance/signposting/background convention。

学习的是 function 和 relation，不是句子或 visual identity。

### 2.3 论文到底应该写什么？

新增 content-selection layer 防止 **implementation-detail leakage / repository-to-manuscript leakage**。

每个候选信息先分类：

- inference-critical；
- interpretation-critical；
- reproducibility-critical；
- compliance/provenance-critical；
- orientation-critical；
- 或 none。

然后再分配到：

`main text / main figure / legend / Methods / Extended Data/SI / Data-Code-Resource Availability / repository docs / omit`

文件路径、helper 名、setup command、config、internal module、CI/unit-test 细节和反复出现的 repository URL 不会再自动进入 prose。

一个很有用的判断：

> 如果把 implementation 从头重写，但 scientific method/results 完全不变，这个细节还会影响论文吗？

### 2.4 在真正画图之前先给 plot suggestions

系统可以根据 scientific question 推荐可视化：

- distribution -> raw points/distribution-aware display；
- paired effect -> paired changes/differences；
- time/dose -> meaningful trajectory；
- association -> scatter/hexbin + justified model；
- classification -> ROC/precision–recall/operating point；
- calibration -> reliability/calibration display；
- survival -> censoring-aware curve；
- heterogeneity -> forest/stratified effect；
- benchmark -> task/site/run-level comparison；
- robustness -> sensitivity curve/interval/small multiples；
- imaging -> representative image + quantitative evidence；
- null result -> effect estimate + uncertainty/equivalence logic；
- qualitative/theory -> 不强行 quantitative plot。

详细指南：[论文到底应该写什么、哪些内容不该进正文，以及应该画什么图？](docs/manuscript-content-and-figures.md)

### 2.5 研究文档

- [学术写作研究综述：强论文究竟是怎样写出来的](docs/academic-writing-research.md)
- [自然学术写作：句子到句子的逻辑与表达指南](docs/natural-scholarly-writing.md)
- [论文到底应该写什么、哪些内容不该进正文，以及应该画什么图？](docs/manuscript-content-and-figures.md)
- [All-journals architecture](docs/all-journals-architecture.md)
- [Editor–Reviewer Decision Architecture](docs/editor-reviewer-decision-architecture.md)

## 3. 架构与设计原则

### 3.1 Truth、compliance、structure、voice 分开

```text
author evidence = truth constraint
journal/reporting rules = compliance constraint
analogue papers = structural/evidence priors
author voice = expression prior
```

Scientific validity 高于所有 surface style rule。

### 3.2 Evidence completeness 不等于 main-text completeness

完整 evidence/reproducibility record 可以分布在 manuscript、Methods、figures/tables、Extended Data/SI、source data、availability statement 和 repository 中。

Main text 应该保留**最短充分 reader-facing evidence chain**，同时所有会改变 headline interpretation 的 negative/boundary evidence 必须可见。

### 3.3 Contribution type 会改变 evidence architecture

Mechanism paper、clinical cohort、ML benchmark、method/tool paper、dataset/resource、theory、qualitative study 与 review 的 evidence/figure architecture 不应相同。

例如 methods paper 可能需要 performance validation、ground truth/gold standard、benchmarking、reproducibility、general applicability 和 distinct applications；clinical generalization claim 可能需要 site/population-stratified performance、calibration、absolute clinical quantity 或 time-to-event evidence，而不是一个 pooled metric。

### 3.4 Published papers 是 priors，不是 acceptance hacks

Published-paper patterns 有 survivorship bias。它们可以告诉我们在某 publication ecology 下别人怎么解决 rhetorical/evidentiary problem，但不能证明某个 phrase、figure count 或 layout 导致 acceptance。

### 3.5 Anti-gaming

系统不会建议：

- 挑 friendly reviewers；
- 战略性引用潜在 reviewer；
- 隐藏 close competitor/adverse evidence；
- 用 inflated novelty/significance wording；
- 加 cosmetic experiments；
- 把 conclusion-changing limitation 埋进 SI；
- 做 AI-detector evasion tricks。

## 4. 快速开始

安装后可以直接交给 Agent manuscript、paper、figures、reviewer letter、code/project context 或 task description。

| 想做什么 | 直接这样说 |
|---|---|
| 读论文 / 中英文 reader | `把这篇 PDF 做成带 source anchors、图文对应的中英文 Markdown reader。` |
| 深度精读 | `做一份 Paper Card：方法逻辑、evidence-to-claim chain、结论边界、弱点和可检验研究想法。` |
| 起草/重建 manuscript | `根据这些 claims、data 和 figures 重建整篇 paper argument。不要默认 Nature style，target journal 单独解析。` |
| 先学 similar papers | `先找/读 4–6 篇真正可比论文，再告诉我哪些 evidence、figures 和 section logic 应 adopt/adapt/reject。` |
| 降低 AI 味 | `这段太 generic/像 AI。修 sentence dependency 和 natural scholarly flow，同时保留我的 author voice；不要优化 AI detector。` |
| 决定什么该进论文 | `审查这些 notes/code/repository materials，把每项分到 main text、figure、legend、Methods、SI、availability、repository docs 或 omit。` |
| 规划 figures/plots | `针对每个 headline claim，判断是否需要 figure，并根据 estimand/data structure/uncertainty 推荐 plot，不要按期刊流行度选。` |
| 投稿前评审 | `解析这个 journal 的 decision model，先 editor triage，再独立 reviewers，最后综合 blockers 和 minimum valid repairs。` |
| 回复 reviewers | `解析 decision letter，先按 editor conditions 和 blocking concerns 排序，再写 point-by-point response 与 manuscript changes。` |
| 查引用 | `拆分这些 claims，找最强 supporting evidence；除非我指定，不按 prestige 过滤。` |
| 生成文献汇报 PPT | `把这篇论文做成中文 journal-club PPT，保留关键图件和来源标注。` |

如果已经知道 skill 名，可以直接指定；否则自然描述任务即可。

## 5. 安装

`nature-skills` 以 `skills/` 下的完整 skill directory 组织。许多 router-style skills 依赖 `skills/nature-shared/`，所以**请安装/复制完整目录，不要只复制 `SKILL.md`**。

### 5.1 `npx skills`

查看技能：

```bash
npx skills add Yuan1z0825/nature-skills --list
```

给 Codex 全局安装全部 skills：

```bash
npx skills add Yuan1z0825/nature-skills --global --agent codex --skill '*' --yes --copy
```

只装某个 skill 时，把需要的 shared package 一起装：

```bash
npx skills add Yuan1z0825/nature-skills --global --agent codex \
  --skill nature-writing --skill nature-shared --yes --copy
```

后续更新：

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

脚本会同步完整 top-level skill directories 并验证复制结果。

### 5.3 Claude Code

保留稳定 clone，然后用 subagent/slash-command wrapper 指向真实 `skills/*/SKILL.md`，或用 `scripts/autoupdate-skills.sh` 同步完整技能到 `~/.claude/skills/`。

示例：

```bash
git clone https://github.com/Yuan1z0825/nature-skills.git ~/ai-skills/nature-skills
~/ai-skills/nature-skills/scripts/autoupdate-skills.sh --force
```

### 5.4 其他 Agent 与可选 runtime

OpenClaw、OpenCode、Hermes 等见 [接入指南](docs/open-source-agent-frameworks.md)。

Python/R/browser/MCP 依赖只在相关 skill 需要时安装；不要把 API key/provider credential 提交到仓库。

## 6. 技能索引

当前 `skills/` 下有 19 个可触发 skill；`nature-shared` 是内部支持包，不计入这里。

| 技能 | 状态 | 用途 | 触发词 | 详情页 |
|---|---|---|---|---|
| [`nature-figure`](skills/nature-figure/README.md) | Stable | Claim-driven figure planning + Python/R rendering、analogue calibration、main/support allocation、journal adaptation 与 visual/source-data QA | “该画什么图”, “scientific figure”, “Figure 1”, “publication plot”, “graphical abstract” | [详情](skills/nature-figure/README.md) |
| [`nature-polishing`](skills/nature-polishing/README.md) | Stable | Journal-aware academic rewrite/translation，包含 sentence dependency、natural scholarly prose、analogue calibration、author voice 与 consistency | “润色”, “自然学术表达”, “AI味”, “句间逻辑”, “journal transfer” | [详情](skills/nature-polishing/README.md) |
| [`nature-writing`](skills/nature-writing/README.md) | Draft | Evidence-first manuscript architecture、content selection、analogue study、plot suggestions、natural prose/voice、editor-reviewer preflight 与首次投稿 | “论文写作”, “重写 Results”, “什么该进论文”, “相似论文”, “编辑视角” | [详情](skills/nature-writing/README.md) |
| [`nature-reviewer`](skills/nature-reviewer/README.md) | Draft | Journal-aware editor triage + 互盲 reviewer simulation + editor synthesis + decision-relevant repair map | “预投稿评审”, “editor perspective”, “reviewer report”, “拒稿风险” | [详情](skills/nature-reviewer/README.md) |
| [`nature-citation`](skills/nature-citation/README.md) | Beta | 默认 best-evidence claim citation discovery，同时保留显式 Nature/CNS/flagship scope 与 RIS/ENW/Zotero export | “找引用”, “supporting evidence”, “CNS citation”, “RIS export” | [详情](skills/nature-citation/README.md) |
| [`nature-data`](skills/nature-data/README.md) | Draft | Data Availability statement、repository plan 与 FAIR checks | “Data Availability”, “数据可用性”, “FAIR” | [详情](skills/nature-data/README.md) |
| [`nature-statistics`](skills/nature-statistics/README.md) | Draft | 统计设计/reporting：experimental units、estimands、p values、multiplicity、effect sizes、intervals、figure stats 与 numeric consistency | “统计审查”, “p value”, “sample size”, “figure statistics” | [详情](skills/nature-statistics/README.md) |
| [`nature-reader`](skills/nature-reader/README.md) | Beta | 带 source anchors、图文对应、公式渲染和中英文翻译的全文 Markdown reader | “论文 reader”, “全文 Markdown”, “图文对应”, “翻译” | [详情](skills/nature-reader/README.md) |
| [`nature-paper-card`](skills/nature-paper-card/README.md) | Beta | Source-grounded 深度精读：method logic、experiment-to-claim evidence、结论边界、批判分析与 research ideas | “Paper Card”, “论文精读”, “evidence chain” | [详情](skills/nature-paper-card/README.md) |
| [`nature-response`](skills/nature-response/README.md) | Beta | 解析 editor/reviewer decision，构建 closure-oriented rebuttal、cover letter、标红稿与 revision-package checks | “response to reviewers”, “major revision”, “rebuttal”, “返修” | [详情](skills/nature-response/README.md) |
| [`nature-paper2ppt`](skills/nature-paper2ppt/README.md) | Beta | 从科研论文生成中文 PPTX journal-club/paper-presentation deck | “paper PPT”, “journal club”, “论文汇报” | [详情](skills/nature-paper2ppt/README.md) |
| [`nature-image2ppt`](skills/nature-image2ppt/README.md) | Beta | 将 slide image、scanned PDF、image-only PPTX 重建为对象级可编辑 PowerPoint 并做 QA | “图片转可编辑PPT”, “扫描PDF转PPTX” | [详情](skills/nature-image2ppt/README.md) |
| [`nature-paper-to-patent`](skills/nature-paper-to-patent/README.md) | Beta | Evidence-constrained 中国发明专利起草、专利点挖掘、prior-art search 与技术交底迭代 | “论文转专利”, “Chinese patent”, “权利要求” | [详情](skills/nature-paper-to-patent/README.md) |
| [`nature-ref-verifier`](skills/nature-ref-verifier/README.md) | Stable | 分开校验 reference identity/metadata、target-journal rendering 与 manuscript cross-links | “校验文献”, “reference verification”, “metadata check” | [详情](skills/nature-ref-verifier/README.md) |
| [`nature-academic-search`](skills/nature-academic-search/README.md) | Beta | Multi-source literature search、citation verification、citation metrics、influential citer profiling 与 reference management | “查文献”, “literature search”, “verify DOI”, “citation table” | [详情](skills/nature-academic-search/README.md) |
| [`nature-downloader`](skills/nature-downloader/README.md) | Beta | 通过 library access、browser login state 与 OA route 合法获取 academic PDF/full text | “download papers”, “图书馆PDF”, “CARSI” | [详情](skills/nature-downloader/README.md) |
| [`nature-literature-pipeline`](skills/nature-literature-pipeline/README.md) | Stable | 自动化 literature discovery：retrieval、scoring、deep-reading delivery 与 local archiving | “literature pipeline”, “每日文献”, “cron” | [详情](skills/nature-literature-pipeline/README.md) |
| [`nature-experiment-log`](skills/nature-experiment-log/README.md) | Draft | 把 experiment image/voice/text 标准化为 Obsidian experiment log 并归档 source | “实验日志”, “record experiment”, “Obsidian” | [详情](skills/nature-experiment-log/README.md) |
| [`nature-proposal-writer`](skills/nature-proposal-writer/README.md) | Beta | Proposal-first research writing state machine：先建立 evidence、argument 与 section contract 再写作/评审 | “researchwrite”, “proposal”, “研究方案”, “写作QA” | [详情](skills/nature-proposal-writer/README.md) |

## 7. 贡献与开发

### 7.1 共享设计原则

1. **Scientific validity first。** Journal prestige、style 和 aesthetic 都不能覆盖 evidence。
2. **规则优先用 current primary source。** Exact journal requirement 应来自目标期刊，而不是同 publisher 的其他期刊。
3. **分离不同 function。** Evidence selection、writing logic、author voice、figures、reporting、house style 与 artifact docs 是不同层。
4. **写作规则要 research。** 优先 cross-disciplinary corpus evidence、direct reading 和 counterexamples，而不是单一作者直觉。
5. **从 analogues 学 function，不克隆。** 提取 relation/evidence architecture，不复制 sentence/visual identity。
6. **阻止 repository leakage。** Code/project artifact 必须翻译成 scientific abstraction 并放到正确 publication layer。
7. **Figure 必须回答问题。** Plot choice 跟着 estimand/data structure/uncertainty，不跟 journal fashion。
8. **修完后保留 author voice。** Natural scholarly prose 是 quality floor，author voice 是 identity layer。
9. **不做 detector/reviewer gaming。** 不优化 AI-detector score，也不操纵 peer-review system。
10. **Contract 要有 regression tests。** 新 shared behavior 应被 focused tests 与 repository validators 保护。

### 7.2 仓库结构

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
├── academic-writing-research.md
├── natural-scholarly-writing.md
└── manuscript-content-and-figures.md
```

每个 triggerable skill 保留 human-facing `README.md` / `README_EN.md`、governing `SKILL.md` 与 `manifest.yaml`；复杂技能按需 route 到 modular `references/`、`static/`、scripts 与 shared contracts。

### 7.3 提交前检查

至少运行仓库 validators 与 focused tests，包括 README count/mirror、skill metadata/index、journal-generalization contracts、writing/figure/shared tests 和 `git diff --check`。

## 8. 项目与社区

创始人 / 维护者：**袁一哲（Yizhe Yuan）**。项目也包含核心开发者和社区贡献者的工作。

项目现有公开资源继续保留：

- 在线网站：https://yuan1z0825.github.io/nature-skills/
- 商务合作：[natureskills2026@outlook.com](mailto:natureskills2026@outlook.com)
- Nature AI 服务/充值卡网：https://apiciyuan.top/
- Open-source agent 接入：[docs/open-source-agent-frameworks.md](docs/open-source-agent-frameworks.md)

项目的核心理念仍然是：科研 workflow 可以被显式化、可检查化并封装成 reusable agent skill；但这些 workflow 必须继续服从 science，而不能变成僵硬 template。

### Star History

[![Star History Chart](assets/star-history-20260819T024318Z.svg)](https://star-history.com/#Yuan1z0825/nature-skills&Date)
