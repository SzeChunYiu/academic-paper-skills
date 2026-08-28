# `nature-figure` 技能

[English](README_EN.md)

`nature-figure` 用于规划、设计、生成和审查 journal-aware 科研图件。它可以在**真正开始画图之前**先决定：论文到底需要哪些 figure、每个 panel 应回答什么科学问题、哪些 data/uncertainty 必须可见、什么 plot family 才匹配真实 estimand 与 data structure；之后再进入 Python 或 R 渲染。

## 适合用它做什么

- 判断一个 claim 是否真的需要 figure，还是 prose/table 更清楚。
- 建立 claim-driven figure plan：`claim -> reader question -> statistical unit -> estimand -> data structure -> uncertainty/alternative explanation -> plot -> main/support placement`。
- 为每个 display 建立 scientific display decision contract，把 reader task、estimand、statistical unit、allowed/prohibited inference、immutable data/analysis/render/source-data chain、caption 与 accessibility state 连起来。
- 为 distribution、paired effect、trajectory、association、agreement、calibration、classification、survival、heterogeneity、sensitivity、benchmark、ablation、imaging、high-dimensional data、null result 等建议合适 plot family。
- 精读几篇 close analogue papers，学习**figure role 与 evidence expectation**，但不复制 layout、palette、normalization 或 visual identity。
- 通过 shared manuscript-content-selection logic 决定哪些 evidence 应进入 main figures，哪些去 Extended Data/SI。
- 根据 data、legend 或 manuscript claim 生成 Python / R plotting script 与可编辑 publication figure。
- 把已有图件重画成更清楚的 multi-panel evidence chain。
- 规划 Figure 1、mechanism diagram、workflow、graphical abstract 或 supplementary figure。
- 审查 panel label、uncertainty、statistical unit、accessibility、最终 PDF 实际字号、source data、image integrity 与 export format。
- 最后按 exact target journal/article type/stage 适配 packaging，但不改变 underlying evidence。
- 用户明确要求时，使用独立 OpenRouter GPT Image 2 路径生成 concept schematic / graphical abstract 草稿，并单独做 target-policy 与 human scientific review。

## 工作方式

Planning 先于 rendering：

```text
claim
-> reader question
-> figure necessity
-> scientific/statistical unit
-> estimand
-> data structure
-> alternative explanation / uncertainty
-> representation
-> scientific display decision contract
-> panel/evidence sequence
-> main vs support
-> analogue calibration when useful
-> Python/R rendering
-> exact journal adaptation
-> visual + source-data QA
```

重要规则：

- **只做 figure/plot planning 时不需要先选 Python 或 R。** 真正开始 plotting/rendering 才进入 backend gate。
- 不存在 universal best chart：maintained adapters 只返回 candidate families 与 obligations；unmatched task 需要 domain research。
- Denominator、group、transformation、data snapshot、analysis receipt、render receipt、source data 与 caption 不得各自漂移。
- 某个 chart 在顶刊或 analogue papers 中很常见，不构成使用它的充分理由。
- 小样本 continuous data 往往需要显示 individual observations/distribution，而不是只有 mean bar。
- Paired data 在 pairing 就是 estimand 时应该把 pairing 画出来。
- 当 calibration/threshold behavior 是科学或临床问题时，AUC 不能替代它们。
- UMAP/t-SNE 单图不能独立承担 quantitative separation 或 mechanism claim。
- Null result 应展示 effect estimate 与适当 uncertainty/equivalence logic，而不是只靠 `P > 0.05`。
- 每个 panel 都必须关闭一个真实 evidence/orientation question，而不是为了填满版面。

## 典型请求

- “根据这些 Results，先告诉我 Figures 1–4 应该是什么、每个 panel 要证明什么，先别画。”
- “这是 paired data，帮我选最能展示 treatment effect 和 uncertainty 的 plot。”
- “先读 4 篇类似 Nature Methods 论文，看看我们的 method paper 缺哪些 validation/benchmark/generalization figures。”
- “我们的 model 声称 external generalization。不要只给 pooled metric，帮我规划 site-level、calibration 和 failure-boundary plots。”
- “按这个 figure plan 用 Python 画出来，并导出 editable SVG/PDF 和 source-data mapping。”
- “做 graphical abstract 草稿，但把 generated imagery 和 quantitative evidence 严格分开。”

## 示例预览

| 方向 | 预览 | 可借鉴模式 |
|------|------|------------|
| 多面板论文图 | <a href="assets/gallery/fig1-material-mechanism-rich.png"><img src="assets/gallery/fig1-material-mechanism-rich.png" width="220" alt="Material design and physical validation"></a> | 学习 heterogeneous evidence 如何组成一条 visual argument；不要把具体 composition 当模板。 |
| 图表类型 atlas | <a href="assets/chart-atlas/atlas-03-heatmaps.png"><img src="assets/chart-atlas/atlas-03-heatmaps.png" width="220" alt="Heatmap atlas"></a> | 候选 visual grammar；最终选择必须服从 data structure 与 reader task。 |
| 第三方 figures4papers 参考 | <a href="assets/figures4papers/figure_VIGIL/figures/comparison_radar.png"><img src="assets/figures4papers/figure_VIGIL/figures/comparison_radar.png" width="220" alt="VIGIL comparison radar"></a> | 仅用于 inspiration/reference；先读版权说明，也不要因为看起来“像论文”就继承这种 chart。 |

## 你需要提供

Planning 阶段：

- headline claims/questions；
- 每个 claim 有哪些 data；
- 已知的话提供 statistical/experimental unit、pairing/repeated structure、groups/conditions、time/order 和重要 uncertainty；
- target field/paper type/journal（如果已知）。

Rendering 阶段：

- raw data 或 analysis-ready table；
- 已选 figure plan，或允许技能先提出方案；
- output format 与 target dimensions/stage；
- Python/R 偏好；若没有，技能会询问或复用保存的本机偏好。

## 产出

根据任务可以输出：

- figure/plot suggestion ledger：`claim/question -> unit -> estimand -> plot -> uncertainty/comparator -> main/support`；
- Figure 1–N evidence-role plan 与 panel map；
- main-versus-Extended-Data/SI visual allocation；
- analogue figures 的 `adopt / adapt / reject` notes；
- 可运行 Python 或 R plotting script；
- SVG/PDF/TIFF/PNG figure files，优先 editable vector output；
- panel notes、source-data mapping、exclusion counts 与逐 panel QA；
- AI-schematic 任务中的 concept draft 与需要人工科学核验/重画的元素列表。

## 内置参考

- `../nature-shared/core/figure-evidence-planning.md`：claim-driven figure necessity 与 question-to-plot atlas。
- `../nature-shared/core/manuscript-content-selection.md`：main/support/Methods/availability/repository allocation。
- `references/analogue-figure-calibration.md`：从 similar papers 学 visual evidence role，但不复制 identity。
- [`docs/manuscript-content-and-figures.md`](../../docs/manuscript-content-and-figures.md)：面向用户的论文内容与 figure planning 指南。
- `references/figure-contract.md`：core conclusion、evidence hierarchy、panel map 与 review-risk checks。
- `references/qa-contract.md`：export QA、source-data constraints 与 visual inspection。
- `references/journal-adaptation.md`：exact target/stage packaging。
- `references/ai-graphical-abstract-workflow.md`：AI graphical abstract 的 evidence/policy/provenance boundary。
- `references/template-catalog.md`、`references/chart-types.md`、`references/demos.md`：候选 implementation/pattern，不能自动变成 scientific choice。

## 边界

- 不会虚构 data、statistical test、sample size、uncertainty、mechanism 或 experimental condition。
- 不会因为 top papers 常用某种 plot 就自动选择它。
- 不会静默删除 observations/variables、隐藏 adverse variation，或用 deceptive axis/crop/normalization 放大效果。
- 不会把 embedding、bar、radar 等熟悉形式当作 evidence，除非它们真的回答 reader question。
- AI-generated image 永远不当作 quantitative data 或 experimental evidence。
- Automated validator 不能替代 final physical-size visual inspection。
- Published figure 不是 submission contract；exact target rule 单独解析。
- 第三方 assets 继续受原始 terms 与 notices 约束。

## 相关技能

- `nature-writing`：建立 claim/evidence/content plan，并可在 prose 固定之前主动要求 figure suggestions。
- `nature-statistics`：审查 estimand、uncertainty、statistical unit、multiplicity 与 inferential display choice。
- `nature-reviewer`：检查 figure 是否真正关闭 decision-relevant reviewer question。
- `nature-paper2ppt`：把已经验证的 manuscript figures 用于 presentation。

## 与其他技能的关系

- 用户问的是**“该画什么”**时，`nature-figure` 可以停留在 planning layer，不需要 backend choice。
- 用户问的是**“这些内容到底该不该进论文”**时，与 `nature-writing` / shared manuscript-content selection 联动。
- 如果核心不确定性是 statistical，先让 `nature-statistics` 确定正确 estimand/inference。
- 如果 final figure 需要写回 Results/Discussion，`nature-writing` 负责 manuscript narration。
- `nature-figure` 负责 visual evidence planning/rendering/QA；它不替代 manuscript argument design 或 statistical review。
