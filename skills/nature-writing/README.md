# `nature-writing` 技能

[English](README_EN.md)

`nature-writing` 用于根据作者提供的证据起草、重构和规划 journal-aware 学术论文。它已经不再是“Nature 风格模板写手”：先识别 paper 的 scientific archetype，建立 argument/evidence dependency，再按需研究 broad corpus 与 close analogue papers，决定哪些内容和图件真正应该进入论文，检查 explanation depth 与句间逻辑，保留 author voice，最后对所有 manuscript-facing surface 做 file/script leakage 与 punctuation scrub，再应用 exact journal rule。

## 适合用它做什么

- 起草标题、摘要、引言、related work、Methods、Results、Discussion、Conclusion 或整篇论文 argument。
- 先解析 dominant **paper archetype**：mechanism/discovery、randomized intervention、observational、computational/ML、method/tool/software、resource/dataset、theory/proof、qualitative、review/synthesis 或 hybrid，再决定 evidence 和 figure 需求。
- 在写 prose 之前建立 `question/tension -> contribution -> evidence chain -> boundary -> meaning`。
- 用 broad stratified corpus 学习 tendency，用 3–6 篇 close analogues 深挖当前 manuscript 的 claim/evidence/explanation/figure dependency，而不是复制 wording/layout。
- 检查 **explanatory sufficiency**：核心概念、方法、机制、结果、公式或 implication 是否给出了足够 identity、rationale、logic、evidence、boundary 与 connection，让目标读者不用猜就能理解。
- 检测 hidden premise 与 conceptual jump，避免一个漂亮短句压掉必要推理。
- 决定内容应该放在 main text、figure、legend、Methods、Extended Data/SI、Data/Code/Resource Availability、repository docs，还是删除。
- 检测并移除 **repository-to-manuscript leakage**：文件/目录路径、script/notebook/config/output filename、helper/class/function name、CLI command、internal module、developer workflow 和无必要的 project link。
- 根据 claim、reader question、estimand、data structure、uncertainty、alternative explanation 与 paper archetype 主动建议 figure/plot，再由 `nature-figure` 渲染。
- 修复“每句话单独看都对，但段落连不起来”的文本：对每句建立 `inherits -> relation -> adds -> enables`。
- 让 academic prose 更自然但不做 detector gaming：保留精准 technical repetition，用 functionally motivated syntax，逐 proposition 校准 stance，避免 connector stuffing/generic prestige language，再恢复作者自己的 cadence 与 agency。
- 把 Results 压缩成 shortest sufficient evidence chain，同时保持会改变结论的 negative/failure/boundary evidence 在主文可见。
- 对 title/abstract/body/legends/table notes/Methods/equations/availability 执行最终 **manuscript-surface QA**，检查 artifact leakage、punctuation spacing、bracket balance、broken Fig. reference、range/minus/hyphen、units 和 target-aware copy-editing。
- 从 editor/reviewer 视角做 preflight，并选择 minimum valid repair：补解释/重构、补证据、reanalysis、纠错、收窄/删除 claim，或改变 target/article type。
- 准备首次投稿材料并检查 exact journal / article type / stage 要求。

## 工作方式

对于 substantial manuscript work，整体流程大致是：

```text
evidence/claims
-> paper archetype
-> argument spine
-> content triage
-> broad corpus / close analogue calibration（需要时）
-> author-voice profile
-> evidence + figure/plot planning
-> section move graph
-> paragraph nuclei + satellites
-> sentence dependency / information flow
-> explanatory sufficiency / hidden-premise audit
-> natural scholarly prose
-> editor/reviewer preflight
-> exact journal adaptation
-> final consistency + manuscript-surface leakage/punctuation release gate
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

技能不会强迫每个段落包含六个元素。解释量随 `中心性 × 陌生度 × 推理依赖程度` 增加；领域常识、已解释充分或 artifact-only 内容保持简洁。

Research hierarchy 是：

```text
author evidence = truth constraint
paper archetype = evidence/reader-dependency prior
journal/reporting rules = compliance constraint
broad corpus = descriptive tendency layer
close analogues = manuscript-specific structural/evidence priors
author voice = expression prior
```

Frequency 永远不是 writing-quality score。

## 学习大量论文

当有几十/几百篇已经提取成 `.md` / `.txt` 的论文时，可以结合：

```bash
python scripts/corpus_structure_stats.py CORPUS_DIR --pretty --output corpus-structure.json
python scripts/corpus_figure_inventory.py CORPUS_DIR --json corpus-figures.json --csv corpus-displays.csv
```

前者描述 section/paragraph/sentence surface statistics；后者 inventory figures/tables/captions，并给出透明的 **candidate** evidence role，例如 orientation、mechanism、validation、OOD/generalization、robustness、failure/limitation、heterogeneity、calibration、resource coverage、theory/model、qualitative synthesis。

这些 label 只是 triage heuristic，不是 semantic truth、acceptance predictor，也不是“哪个 plot 出现最多就照抄哪个”。任何 rule 改动前仍必须 semantic close reading。

## 典型请求

- “按真正 evidence 和 research need 重建这个 Introduction，不要套 Nature 模板。”
- “先判断这究竟是哪类 paper，再告诉我这种 archetype 的 evidence sequence 和 main figures 应该是什么。”
- “这个解释太压缩了。检查读者到底能不能理解，只展开缺失推理。”
- “先研究 50 篇 recent papers 的 broad tendency，再精读 4–6 篇真正近邻后重写 Results。”
- “这一段很有 AI 味。修复句子逻辑、保留我的 voice，但不要优化 AI detector。”
- “源材料包含代码/repository docs。论文只保留科学上真正有用的内容，并在最终交付前再做 filename/script leakage scrub。”
- “检查我们的 figure captions：删除 plotting-pipeline filename/helper name，并修 punctuation，但保留必要 scientific identifiers。”
- “根据这些 claims/data，在写 Results 前先规划 main figures 和具体 plot type。”
- “从 editor/reviewers 视角做 submission preflight，找最便宜但科学上有效的修改。”

## 你需要提供

- 核心 claims/questions、figures、data/results、Methods facts、limitations，以及不能改变的 evidence。
- 需要保留 author voice 时提供代表性作者原文。
- 已知的话提供 target field、paper type、study design 和 exact journal/venue。
- 有 preferred analogues 可以直接给；否则 workflow 会定义 comparator profile。
- 只有 method/resource/reproducibility 相关时才需要 code/repository/project materials；技能不会自动把它们抄进 paper。
- 需要 broad empirical calibration 时，可提供 extracted paper corpus。

## 产出

根据任务不同，可以产出：

- 通过 final surface QA 的可粘贴 manuscript prose；
- dominant/secondary paper-archetype plan；
- argument spine 与 section move map；
- **explanation ledger**：`concept/inference -> reader baseline -> 缺失解释元素 -> recommended expansion -> destination -> sufficient/under-explained/over-explained`；
- content-allocation ledger：`main / figure / legend / Methods / Extended Data/SI / availability / repository / omit`；
- repository-leakage list：artifact detail -> scientific abstraction/correct destination；
- final manuscript-surface QA findings 与 resolution；
- shortest sufficient evidence chain；
- figure/plot suggestion ledger：`claim/question -> statistical unit -> estimand -> plot -> uncertainty/comparator -> main/support`；
- broad-corpus descriptive profile 与 close-analogue `adopt / adapt / reject / unresolved` decisions；
- compact author-voice profile 与 re-voice notes；
- sentence/paragraph dependency repair；
- editor/reviewer blocker map 与 resolution tests；
- 首次投稿材料和需要时的 `ready / ready_with_author_checks / blocked` 状态。

## 方法来源

写作规则来自 empirical research 和 stratified direct reading，而不是一个 prestige-journal style。

- [`docs/academic-writing-research.md`](../../docs/academic-writing-research.md)：跨学科 rhetorical moves、cohesion、stance、human/LLM academic writing、section structure 与 writing process。
- [`docs/deep-paper-calibration.md`](../../docs/deep-paper-calibration.md)：paper archetypes、recent stratified reading、broad-corpus/close-analogue calibration、figure inventory、leakage 与 punctuation QA。
- [`docs/natural-scholarly-writing.md`](../../docs/natural-scholarly-writing.md)：句子到句子的逻辑流与自然 academic prose。
- [`docs/explanatory-sufficiency.md`](../../docs/explanatory-sufficiency.md)：解释不足、hidden premise，以及什么时候该展开/压缩。
- [`docs/manuscript-content-and-figures.md`](../../docs/manuscript-content-and-figures.md)：paper content、repository-to-manuscript leakage、evidence allocation 与 figure/plot planning。
- `../nature-shared/core/paper-archetype-atlas.md`：archetype-specific evidence/writing/figure priors。
- `../nature-shared/research/stratified-paper-reading-2025-2026.md`：recent cross-archetype direct reading。
- `../nature-shared/core/analogue-paper-calibration.md`：focused 3–6-paper near-neighbor study。
- `../nature-shared/core/explanatory-sufficiency.md`：minimum-sufficient explanation 与 reader reconstruction。
- `../nature-shared/core/natural-scholarly-prose.md`：natural scholarly expression。
- `../nature-shared/core/manuscript-content-selection.md`：content admission/destination model。
- `../nature-shared/core/figure-evidence-planning.md`：claim-driven figure/plot planning。
- `../nature-shared/core/manuscript-surface-qa.md`：final artifact-leakage 与 punctuation/typography release gate。

## 边界

- 不会虚构 results、mechanisms、statistical significance、references、uncertainty、limitations、novelty 或 unsupported rationale。
- 不会把“写得更长”当成“解释更好”；routine/已充分解释内容继续简洁。
- 不会把 humanize 理解成 AI-detector evasion、故意错误、word blacklist、随机长短句或强行口语化。
- 不会复制 analogue papers 的 sentence、distinctive paragraph structure、figure layout 或 visual identity。
- 不会把 broad-corpus frequency 或 keyword role label 当作 quality/acceptance score。
- 不会假设多做实验永远是正确答案；补解释/重构、收窄/删除 claim 或换 target 都可能正确。
- 不会把所有 reproducibility detail 塞进 main narrative：Methods、SI、availability 与 repository 有不同工作。
- 不会因为 project files 里存在内部 filename/script/helper 就把它们暴露在 manuscript-facing prose。
- Exact current target-journal instructions/reporting standards 高于 generic/local formatting/punctuation defaults。
- 最终 figure rendering/export 用 `nature-figure`；真实 editor decision 后的 rebuttal/revision correspondence 用 `nature-response`。

## 相关技能

- `nature-polishing`：用同一套 explanation、archetype、surface-QA、natural-prose 与 author-voice 原则润色/重构已有文本。
- `nature-figure`：把 claim/archetype-driven figure plan 转成 publication figures，并做 visual + legend/caption QA。
- `nature-reviewer`：独立 editor/reviewer simulation，检查 archetype fit、under-explanation、figure adequacy 与 surface hygiene。
- `nature-response`：真实返修后关闭 editor/reviewer concerns。
- `nature-citation`：默认 best-evidence citation discovery，也保留显式 CNS/Nature scope。
- `nature-academic-search`：更广泛的 literature discovery 与 verification。
- `nature-statistics`：统计设计、reporting、estimand、uncertainty 与 figure statistics。
