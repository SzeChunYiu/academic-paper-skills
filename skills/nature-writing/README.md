# `nature-writing` 技能

[English](README_EN.md)

`nature-writing` 用于根据作者提供的证据起草、重构和规划 journal-aware 学术论文。它已经不再是一个“Nature 风格模板写手”：先建立科学论证，再在需要时精读 close analogue papers，决定哪些内容和图件真正应该进入论文，检查重要想法是否解释充分，修复句间逻辑与自然学术表达，保留作者自己的 voice，最后才应用具体期刊规则。

## 适合用它做什么

- 起草标题、摘要、引言、related work、Methods、Results、Discussion、Conclusion 或整篇论文 argument。
- 在写 prose 之前建立 `question/tension -> contribution -> evidence chain -> boundary -> meaning`。
- 精读几篇真正可比的论文，学习当前 evidence architecture、figure role、main-text/SI allocation、解释深度与本领域 rhetorical convention，而不是复制句子。
- 检查 **explanatory sufficiency**：核心概念、方法、机制、结果、公式或 implication 是否给出了足够的 identity、rationale、logic、evidence、boundary 和 connection，让目标读者不需要猜就能理解。
- 检测 hidden premise 与 conceptual jump，避免一个看起来很干净的短句把关键推理步骤压缩掉。
- 决定哪些内容应该放在 main text、figure、legend、Methods、Extended Data/SI、Data/Code/Resource Availability、repository docs，或者直接删除。
- 检测并移除 **repository-to-manuscript leakage**：例如文件路径、script/helper 名、setup command、config、internal module、developer workflow 和反复出现的 project link，如果它们没有执行科学功能。
- 根据 claim、reader question、estimand、data structure、uncertainty 和 competing explanation 主动建议论文需要哪些 figure/plot，再由 `nature-figure` 负责渲染。
- 修复“每句话单独看都对，但段落连不起来”的文本：对每句建立 `inherits -> relation -> adds -> enables`。
- 让 academic prose 更自然，但不做 detector gaming：保留精准的技术术语重复，用有功能理由的 syntax variation，逐 proposition 校准 stance，避免 connector stuffing 与 generic prestige language，最后恢复作者自己的 cadence 与 agency。
- 把 Results 压缩成最短充分 evidence chain，同时保持会改变结论的 negative/boundary evidence 在主文可见。
- 从 editor/reviewer 视角做 preflight，并选择最低成本但科学上有效的修复：补解释/重构、补证据、reanalysis、纠错、收窄/删除 claim，或改变 target/article type。
- 准备首次投稿材料并检查 exact journal / article type / stage 要求。

## 工作方式

对于 substantial manuscript work，整体流程大致是：

```text
evidence/claims
-> argument spine
-> content triage
-> close analogue study
-> author-voice profile
-> evidence + figure/plot planning
-> section move graph
-> paragraph nuclei + satellites
-> sentence dependency / information flow
-> explanatory sufficiency / hidden-premise audit
-> natural scholarly prose
-> editor/reviewer preflight
-> exact journal adaptation
-> final consistency and claim-drift audit
```

对重要想法，解释深度检查会让读者能够恢复出（按需要选择）：

```text
是什么
-> 为什么在这里
-> 如何工作 / 为什么这个推断成立
-> 什么 evidence 或 comparison 支撑它
-> 哪个 assumption/boundary 适用
-> 它让下一步什么成为可能
```

技能不会强迫每个段落都包含六个元素。解释量随 `中心性 × 陌生度 × 推理依赖程度` 增加；对领域常识、已经解释充分或只属于 artifact 的内容则保持简洁。

核心分离是：

```text
author evidence = truth constraint
journal/reporting rules = compliance constraint
analogue papers = structural/evidence priors
author voice = expression prior
```

Natural scholarly prose 是 quality floor；author voice 是其上的 identity layer。

## 典型请求

- “按真正 evidence 和 research need 重建这个 Introduction，不要套 Nature 模板。”
- “这个解释太压缩了。检查读者到底能不能理解，只展开缺失的推理部分。”
- “先读 4–6 篇真正相似的论文，再重写这些 Results，并告诉我哪些内容应该留在主文、哪些去 SI。”
- “这一段很有 AI 味。修复句子之间的逻辑，让它自然一点并保留我的写作 voice，但不要优化 AI detector。”
- “源材料包含代码和 repository docs。论文只保留科学上真正有用的内容，把 operational details 放到正确的位置。”
- “根据这些 claims 和 data，在写 Results 之前先帮我规划 main figures 和具体 plot type。”
- “从 editor 和 reviewers 的视角做 submission preflight，找出最便宜但科学上有效的修改。”

## 你需要提供

- 核心 claims/questions、figures、data/results、Methods facts、limitations，以及任何不能被改变的 evidence。
- 如果需要保留可辨认的 author voice，提供有代表性的作者原文。
- 已知的话，提供 target field、paper type、study design 和 exact journal/venue。
- 如果你已经有 preferred analogue papers 可以直接提供；否则 workflow 会先定义需要找什么样的 comparator。
- 只有当 method/resource/reproducibility 相关时才需要提供 code/repository/project materials；技能不会自动把它们抄进论文正文。

## 产出

根据任务不同，可以产出：

- 可直接粘贴的 manuscript prose；
- argument spine 与 section move map；
- **explanation ledger**：`concept/inference -> reader baseline -> 缺失解释元素 -> recommended expansion -> destination -> sufficient/under-explained/over-explained`；
- content-allocation ledger：`main / figure / legend / Methods / Extended Data/SI / availability / repository / omit`；
- repository-leakage list：指出哪些 artifact detail 被移除，以及正确 scientific abstraction / destination；
- shortest sufficient evidence chain；
- figure/plot suggestion ledger：`claim/question -> statistical unit -> estimand -> plot -> uncertainty/comparator -> main/support`；
- analogue-paper `adopt / adapt / reject / unresolved` decisions；
- compact author-voice profile 与 re-voice notes；
- sentence/paragraph dependency repair；
- editor/reviewer blocker map 与 resolution tests；
- 首次投稿材料和需要时的 `ready / ready_with_author_checks / blocked` 状态。

## 方法来源

写作规则来自 empirical research 和 direct reading，而不是一个 prestige-journal style。

- [`docs/academic-writing-research.md`](../../docs/academic-writing-research.md)：跨学科 rhetorical moves、cohesion、stance、human/LLM academic writing、section structure 与 writing process 研究综述。
- [`docs/natural-scholarly-writing.md`](../../docs/natural-scholarly-writing.md)：句子到句子的逻辑流与自然学术表达实操指南。
- [`docs/explanatory-sufficiency.md`](../../docs/explanatory-sufficiency.md)：如何发现解释不足、hidden premise，以及什么时候该展开或压缩。
- [`docs/manuscript-content-and-figures.md`](../../docs/manuscript-content-and-figures.md)：论文该写什么、repository-to-manuscript leakage、evidence allocation 与 figure/plot planning。
- `references/cross-disciplinary-writing-evidence.md`：skill 内置的 empirical corpus evidence。
- `references/direct-reading-notes-2025-2026.md`：跨 publication ecology 的 direct reading。
- `../nature-shared/core/analogue-paper-calibration.md`：focused 3–6-paper near-neighbor study。
- `../nature-shared/core/explanatory-sufficiency.md`：minimum-sufficient explanation 与 reader-reconstruction contract。
- `../nature-shared/core/natural-scholarly-prose.md`：research-backed natural scholarly prose contract。
- `../nature-shared/core/manuscript-content-selection.md`：content admission 与 destination model。
- `../nature-shared/core/figure-evidence-planning.md`：claim-driven figure/plot planning。

## 边界

- 不会虚构 results、mechanisms、statistical significance、references、uncertainty、limitations、novelty，也不会补作者没有证据支持的 rationale。
- 不会把“写得更长”当成“解释更好”；领域常识和已经充分解释的内容继续保持简洁。
- 不会把“humanize”理解成 AI-detector evasion、故意加错误、AI-word blacklist、随机长短句或强行口语化。
- 不会从 analogue papers 复制 sentence、distinctive paragraph structure、figure layout 或 visual identity。
- 不会假设“多做实验”永远是正确答案；补解释/重构、收窄/删除 claim 或换 target 也可能是最正确修复。
- 不会把所有 reproducibility detail 塞进主文：Methods、SI、availability statements 与 repositories 有不同工作。
- Exact current target-journal instructions 与 reporting standards 高于 generic/local placement defaults。
- 最终 figure rendering/export 由 `nature-figure` 负责；真实 editor decision 之后的 rebuttal/revision correspondence 使用 `nature-response`。

## 相关技能

- `nature-polishing`：用同一套 explanatory-sufficiency、natural-prose 与 author-voice 原则润色/重构已有文本。
- `nature-figure`：把 claim-driven figure plan 转成 publication figures 并做 visual QA。
- `nature-reviewer`：独立 editor/reviewer simulation，同时检查 under-explanation 和 decisionability。
- `nature-response`：真实返修后关闭 editor/reviewer concerns。
- `nature-citation`：默认 best-evidence citation discovery，也保留显式 CNS/Nature scope。
- `nature-academic-search`：更广泛的 literature discovery 与 verification。
- `nature-statistics`：统计设计、reporting、estimand、uncertainty 与 figure statistics。
