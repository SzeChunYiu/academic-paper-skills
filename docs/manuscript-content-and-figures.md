# 论文到底应该写什么、哪些内容不该进正文，以及应该画什么图？

[English](manuscript-content-and-figures_EN.md)

强论文不是把整个项目压缩进 PDF。真正成熟的 publication package 会把信息放到最合适的位置：主文承担最短充分科学论证，主图让决定性证据可直接检查，Methods 保证解释与复现，Extended Data/SI 支持更深审查，Data/Code/Resource Availability 负责访问入口，repository 则承担安装、运行和开发文档。

这份指南说明仓库现在如何判断：**什么该写、写在哪里、什么应该删掉，以及该建议什么图。**

最后复核日期：2026-08-22。

## 1. 一个常见问题：repository-to-manuscript leakage

AI 从代码库写论文时，很容易把 implementation artifact 直接抄进正文：

- 文件名和目录路径；
- helper function / class 名称；
- CLI command；
- config 文件；
- 安装命令；
- branch / PR / issue 历史；
- unit test 名；
- internal module；
- 反复出现的 GitHub 链接；
- developer workflow。

我们把它叫做 **implementation-detail leakage** 或 **repository-to-manuscript leakage**。

问题不是这些信息“错”，而是它们在当前位置通常没有执行科学功能。

### Scientific-abstraction test

问：

> 如果明天整套代码被重新实现，但 scientific method 与 results 完全不变，这个细节还会影响论文吗？

如果答案是否定的，它大概率属于 artifact/documentation，而不是 scientific narrative。

例如：

| 源材料 | 更合理的 publication 位置 |
|---|---|
| `scripts/preprocess.py` | 在 Methods 描述真正影响科学结果的 preprocessing；文件名留在 repository。 |
| `src/model.py::fit()` | 写模型/算法 fitting 的科学过程，不写 function path。 |
| YAML config | Methods/SI 报告真正 consequential 的参数；完整 config 留在代码包。 |
| GitHub URL | 在 Code/Resource Availability 给一个 authoritative access point。 |
| install command | repository README / artifact appendix。 |
| unit tests / CI | repository QA；除非 software reliability 本身就是论文评估对象。 |
| internal module hierarchy | 通常是 developer docs；只有 architecture 本身就是 contribution 才进入论文。 |

## 2. 五个 content admission function

每个候选信息至少应该执行一种功能。

### F1 — inference-critical

没有它，读者无法相信/评估一个科学 claim。

### F2 — interpretation-critical

没有它，读者会误解 meaning、scope、alternative explanation 或 boundary。

### F3 — reproducibility-critical

复现/验证实验或分析必须知道。

### F4 — compliance/provenance-critical

伦理、reporting、注册、data/code/material access、attribution、audit 所要求。

### F5 — orientation-critical

显著降低理解复杂 design、system、cohort、workflow 或 evidence sequence 的 cognitive cost。

如果五类都不是，这个信息通常不值得占 publication space。

即使属于 F1–F5，也不代表一定进主文。下一步是分配位置。

## 3. 主文、Methods、SI、repository，到底怎么分？

### Main text

放 reader 在第一次阅读论证时必须看到的：

- research question / tension；
- bounded contribution；
- central findings；
- decisive comparison/control；
- primary uncertainty；
- 若声明 mechanism，则必要的 mechanism evidence；
- 若声明 generalization，则必要的 validation/generalization；
- 会改变 interpretation 的 negative/failure evidence；
- 防止 overgeneralization 的 boundary/limitation。

### Main figures / tables

当证据的 **pattern** 应由读者直接检查，而不是由 prose 代述时使用：

- distribution；
- pairing；
- heterogeneity；
- relationship；
- uncertainty；
- comparative performance；
- mechanism/sequence；
- generalization/failure boundary；
- high-dimensional/spatial/network structure。

每个 display 都要“赚到”自己的位置。

### Figure legend

负责解码：

- panel 展示什么；
- groups/conditions；
- axes 与 units；
- `n` 是什么 statistical/experimental unit；
- error/interval 含义；
- tests/annotation；
- scale bars；
- 必要 panel-specific 条件。

不要把 legend 写成重复 Results + 完整 Methods。

### Methods

负责 interpretation 和 reproducibility：

- design；
- provenance/sampling；
- procedure；
- measurement；
- preprocessing；
- algorithms/models；
- fitting/training；
- statistics；
- controls；
- consequential software/hardware；
- ethics/registration；
- reproducibility details。

计算类论文中，长 derivation、training strategy、exhaustive architecture description，如果会打断 Results，通常应放 Methods。

### Extended Data / Supplementary Information

放“重要，但第一次阅读中心论证时不是必须”的 support：

- secondary controls；
- robustness/sensitivity；
- alternative specification；
- parameter sweep；
- full benchmark table；
- extended diagnostics；
- secondary endpoints；
- large derivations/calculations；
- specialist details；
- non-central edge cases。

但是：failed external validation、subgroup reversal、adverse effect、重要 failure boundary 如果会改变 headline interpretation，就不能埋进 SI。

### Data / Code / Resource Availability

作为 artifact access 的 authoritative one-stop shop：

- persistent repository / DOI / accession；
- release/version/commit（需要时）；
- license；
- access restriction；
- archived code/data/material identifier；
- central protocol。

GitHub 链接通常应该在这里集中出现，而不是 Results 每段都贴一次。

### Repository / artifact documentation

放：

- installation；
- dependencies；
- CLI usage；
- file structure；
- configs；
- APIs；
- scripts；
- reproduction commands；
- developer info；
- unit tests/CI；
- extensive operational examples。

### Omit

如果既不帮助 inference、interpretation、reproducibility、compliance/provenance，也不帮助 orientation，就删。

`我们做过这个 analysis` 本身不是发表理由。

## 4. 顶刊 editorial guidance 实际上支持“主文选择性 + publication package 完整性”

Nature Portfolio 的作者指南反复强调 focused/concise message，并要求每个 figure 真正 support main message。

Nature Computational Science 明确建议 Results 按 **logical narrative** 排，而不是 lab chronology；main text 只放最重要结果。详细 mathematical derivation、training strategy、exhaustive model architecture/construction 如果会干扰 Results，就移到 Methods。

与此同时，Nature Methods 又要求 method paper 有足够详细的 algorithm/code/user guide 以便 reuse。

这两条并不矛盾：

> **主文不需要成为 artifact manual；但整个 publication package 必须足够透明和可复现。**

Nature Methods 对 methods paper 真正关心的是 validation、benchmarking、reproducibility、general applicability、useful application，而不是 Results 中 implementation prose 越多越好。

## 5. 决定“论文应该画什么图”，不要从 chart type 开始

正确顺序：

`claim -> reader question -> estimand -> data structure -> uncertainty / alternative explanation -> plot -> placement`

对每个 headline claim 问：

1. skeptical reader 为判断这个 claim 必须看到什么？
2. experimental/statistical unit 是什么？
3. 真正 estimand/quantity of interest 是什么？
4. 哪种 variation 会改变解释？
5. 哪个 alternative explanation 应该被 visual 直接检验？
6. 哪种 uncertainty 必须可见？
7. prose/table 是否比 figure 更合适？
8. 这是否值得占 main display？

## 6. Figure role atlas：图到底在论文里做什么工作？

可用角色包括：

- **orientation/system** — design、cohort flow、workflow、apparatus、method concept；
- **primary finding** — 核心 observation/effect；
- **mechanism** — 区分 proposed mechanism 与 alternative；
- **validation/replication** — independent evidence；
- **generalization** — sites/populations/tasks/regimes；
- **robustness/sensitivity** — 对 analysis/parameter choice 的依赖；
- **heterogeneity** — average 隐藏的 variation；
- **failure/negative boundary** — claim 在哪里停止；
- **benchmark/comparison** — meaningful baseline/alternative；
- **resource/quality/coverage** — dataset/resource 的组成、质量和 utility；
- **model/process interpretation** — scientifically relevant internal relationship；
- **synthesis/conceptual model** — 有边界地整合 findings。

一篇 paper 不需要把所有角色都填满。

## 7. 按 scientific question 选 plot

以下只是 starting point，不是 universal template。

### 小样本 continuous groups

尽量让 individual observations / distribution 可见，而不是只有 mean ± error bar。

可考虑：

- dot/strip/swarm；
- box/violin + points；
- ECDF；
- estimation/effect-size plot。

Weissgerber 等的系统研究说明，bar/line summary 会隐藏 outlier、bimodality、overlap 与 paired structure。Nature/PLOS 的可视化指导也越来越倾向于在样本数允许时显示 individual points。

### Paired / matched data

把 pairing 画出来：

- connected pairs；
- paired-difference distribution；
- slopegraph；
- repeated-measure trajectories。

不要用两个独立 bar 抹掉真实 estimand。

### Time / dose / ordered parameter

只有 order/continuity 有意义时才用 line/trajectory，并在需要时保留 individual trajectory 或 uncertainty。

### Association

scatter / hexbin / density，根据数据规模选择。只有在 model 合理时才加 fitted relationship。图上的 association 不是 causality。

### Measurement agreement

correlation 不是 agreement。

可使用 correspondence + difference-vs-average 等 agreement diagnostic。

### Classification

根据 decision problem：

- ROC：sensitivity/specificity trade-off；
- precision–recall：class imbalance 与 positive retrieval 更关键时；
- operating point：deployment threshold 真正重要时。

如果 calibration/threshold behavior 影响实际使用，AUC 不能代表完整评价。

### Calibration

画 calibration/reliability curve，并配合适当 quantitative calibration metric。Discrimination 与 calibration 是不同问题。

### Survival / time-to-event

用 censoring-aware survival/cumulative-incidence display 与 effect interval，而不是普通时间线。

### Heterogeneity / subgroup effect

forest/interval plot 或 stratified raw-data display。声明 subgroup difference 时，要比较 effect difference，而不是“一个显著一个不显著”。

### Robustness / sensitivity

sensitivity curve、interval plot、small multiples、parameter surface。通常放 support，除非 sensitivity 本身定义了 central boundary。

### ML / algorithm benchmark

如果 task/site/run heterogeneity 重要，就画 per-unit performance 或 paired difference，不要只有 grand mean。

可考虑：

- per-task/site paired comparison；
- interval plot；
- performance-vs-compute frontier；
- exact-value table（many metrics 时）。

只有 rank 本身是 decision target 时才以 rank 为核心。

### Ablation

Ablation 通常能说明“去掉/改变 component 后 output/performance 如何变”，但它本身不自动证明 biological/causal mechanism。

应该画实际 component effect、interaction 或 across-task variation。

### Imaging / microscopy

如果是 population-level claim，representative image 通常要和正确 experimental unit 上的 quantitative evidence 配套。

### High-dimensional / single-cell / omics

Heatmap/embedding 适合展示 matrix/manifold pattern，但漂亮 UMAP/t-SNE 不能独立承担 quantitative separation 或 mechanism claim。

### Null / negative result

应展示 effect estimate + uncertainty / equivalence / non-inferiority logic（视问题而定）。`P > 0.05` + 看起来没差的 bar 不能证明“没有 effect”。

### Qualitative / theory / humanities

不要强行数字化。Conceptual framework、evidence matrix、source map、process diagram，甚至不画图，都可能更忠实。

## 8. Contribution type 会改变“应该写什么、应该画什么”

### Experimental discovery / mechanism

高优先证据可能是：

- phenomenon；
- decisive controls；
- perturbation/dependency；
- competing mechanism discrimination；
- rescue/orthogonal evidence；
- generalization/boundary。

### Clinical / epidemiological

可能是：

- cohort/design orientation；
- primary outcome/effect；
- uncertainty；
- confounding/identification logic；
- clinically meaningful absolute quantity；
- central heterogeneity/safety/generalization。

### Computational / ML

可能是：

- task/data regime；
- fair baseline comparison；
- primary benchmark；
- across-task/site/run variation；
- ablation（只有 component dependence 是 claim 时）；
- external/OOD validation（只有 generalization 是 claim 时）；
- failure/calibration/efficiency trade-off（如果 central）。

Implementation plumbing 应进入 Methods/repository。

### Methods / tools

Nature Methods 提供了很清晰的 evidence checklist：

- method 可复用的详细 description；
- strong performance validation；
- ground truth/gold standard（如果领域存在）；
- 对 similar methods 的 benchmarking；
- real experimental data，而不是 simulation only；
- across distinct systems/datasets 的 general applicability；
- 合适时，用 challenging application 展示真正 utility。

### Dataset / resource

Resource paper 中一些在普通 research article 里显得“太 operational”的内容反而可能是必要内容，例如 resource composition、file/data organization、quality control、Usage Notes，因为 usability/provenance 本身就是 contribution。

所以 content selection 必须 **contribution-type aware**。

## 9. 近期高水平论文 direct reading 的 role pattern

这些只是“证据角色序列”的例子，不是 panel template。

### Nature Cell Biology：method + discovery

2025 年 *Decoding heterogeneous single-cell perturbation responses* 先用 framework/benchmark 定义方法，再用后续 figures 建立 dosage/heterogeneity 能力和 biological applications。可迁移的是：

`method definition -> validation/benchmark -> new analysis capability -> biological discovery`

而不是它的具体配色/布局。

### Nature Cell Biology：大规模 perturbation system

*Systematic reconstruction of molecular pathway signatures using scalable single-cell perturbation screens* 的主图序列大致是：

`large-scale experimental system -> computational method -> cross-context signatures -> validation -> in vivo/in situ applications`

### Nature Methods：benchmark paper

2026 年 27 个 single-cell perturbation prediction methods、29 datasets 的 benchmark，先 overview/workflow，再分别展示不同 generalization scenarios，并专门用一张 main figure 展示 current methods 的 limitation。这是一个很好的例子：**failure-boundary evidence 如果改变结论，就值得占 main display。**

### Nature Medicine：generalization

近期 oncology/generalization 研究常用 trial/site/population-stratified effect/survival display，而不是只给一个 pooled headline metric。Clinical generalization 应该作为 context heterogeneity 被展示，而不是因为“有一个 external dataset”就直接宣称 generalizable。

这些 direct-reading pattern 应帮助我们提出问题，而不是决定 figure count 或 aesthetic。

## 10. 实际可输出的 content + figure planning

对每个重要 content item：

```text
Item
Function: inference / interpretation / reproducibility / compliance / orientation / none
Claim dependency
Decision-changing? yes/no
Destination
Reason
```

对每个 headline claim：

```text
Claim / reader question
Figure needed? why/why not
Statistical unit
Estimand
Data structure
Alternative explanation to expose
Recommended plot
Alternative representation
Required uncertainty/comparator
Main vs support
Panels
```

最终形成：

```text
Main-text evidence chain
Fig. 1 — ...
Fig. 2 — ...
Fig. 3 — ...
Extended Data/SI — ...
Methods — ...
Data/Code/Resource Availability — ...
Repository/artifact docs — ...
Omit — ...
```

## 11. 最终目标

理想论文不是 detail 最多、figure 最多的论文。

它应该做到：

- 每个 main-text paragraph 都推进或限定中心推理；
- 每张 main figure 都关闭一个真实 evidentiary question；
- reproducibility 信息完整，但位置正确；
- codebase operational detail 留在 artifact layer，除非它本身具有科学意义；
- negative/boundary evidence 不被隐藏；
- exact journal + contribution type 决定局部 convention；
- reader 不需要猜“为什么这句话、这个 analysis、这个 panel 会出现在这里”。
