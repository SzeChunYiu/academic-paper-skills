# 深度论文校准：学习科学任务，而不是模仿顶刊表面

[English](deep-paper-calibration_EN.md)

现在 academic-paper skills 使用两层互补研究：

1. **广泛、分层的 corpus**：从很多论文中学习描述性趋势；
2. **少量真正近邻的 analogue papers**：深挖当前 manuscript 的具体论证与 evidence dependency。

目标不是把所有论文都写成 Nature、Science、Cell、IEEE、JAMA 或 NeurIPS 的样子，而是理解不同 paper class 在解决什么不同的 reader problem。

## 为什么 universal paper template 不成立

不同论文有不同的 epistemic promise。

- mechanism paper：什么过程产生了这个 phenomenon？
- randomized trial：intervention 是否改变 prespecified outcome？
- benchmark paper：方法在公平、相关的 evaluation regime 中是否有效？
- resource paper：资源覆盖什么、质量是否可信、是否可复用？
- theory paper：在什么 assumptions 下证明了什么？
- qualitative paper：识别出什么 experience/process/meaning，解释如何被 evidence 支撑？

工作 tuple 是：

```text
contribution archetype
× study design
× evidence modality
× intended reader
× publication model
```

Journal/venue convention 最后才适配。

## 当前建模的 paper archetypes

Shared atlas 至少区分：

- experimental discovery / mechanism；
- randomized trial / intervention；
- observational / epidemiological / clinical association；
- computational / machine-learning empirical；
- method / tool / software / instrument；
- dataset / resource / benchmark-resource；
- theory / proof / mathematical；
- qualitative / interpretive；
- review / systematic review / perspective / synthesis；
- hybrid papers。

这些是 priors，不是硬分类。一个 method paper 也可能同时做 biological discovery；一个 trial 可以包含 mechanism sub-study。

## Direct reading 学到了什么

我们按 paper class 刻意精读了互相差异很大的 2025–2026 papers。

### Computational benchmark

2026 Nature Methods single-cell perturbation benchmark 的公开 main-figure sequence 大致是：

```text
workflow + datasets
→ OOD benchmark
→ current methods 的 explicit limitation
→ 第二种 generalization regime
→ 更广泛 benchmark
```

真正值得学的不是“五张图”，而是 **如果 failure/limitation 改变 headline interpretation，它完全可以成为 main figure**。

### Experimental mechanism

2025 Nature Cell Biology mechanism paper 的早期 evidence progression 是：

```text
curvature-dependent phenotype
→ dynamics
→ force/dependency evidence
→ mathematical model
```

每张图都在删除一个不同的不确定性。

### Randomized trial

2025 Nature Medicine phase 2a trial 开始于：

```text
participant flow
→ primary outcome + 95% CI
→ pharmacokinetics
```

这是 trial decision logic，而不是 `schematic -> mechanism -> benchmark`。

### Resource paper

2025 Scientific Data resource paper 先用 sampling geography + richness distributions 回答“覆盖了什么”，再用 processing workflow 回答“资源怎么产生”。

### Qualitative paper

2025 PLOS ONE endometriosis interview study 只有 participant table，没有 main figure；另一个 interview study 则有一张简单 themes figure。

所以：

> `qualitative study → theme diagram` 不是规则。

Figure 必须真正有 scientific/orientation function。

### Theory + numerics

JMLR 2025 的 theory-heavy papers 显示 theorem/proof 与 numerical evidence 有不同 epistemic status。数值图可以说明 practical behavior，但不能替代 mathematical proof。

## 大规模 empirical evidence

Direct reading 还要和更大的 corpus research 配合。

目前研究依据包括：

- 500 篇 published research-article introductions，覆盖五个 social-science disciplines，显示 rhetorical realization 有明显学科差异；
- 600 篇 social-science introductions 的 corpus，把 phrase frames 映射到 rhetorical moves；
- 数百篇 science/engineering/social-science introductions 的 syntactic-complexity studies；
- applied linguistics、education、electrical engineering、biology 的 cross-disciplinary engagement research；
- **Viziometrics：超过 800 万张 PubMed figures** 的 visual-type classification，显示 figure type 随 field/topic 明显变化。

因此正确结论不是“学习平均论文”，而是：

> **先分层，再归纳。**

## Broad corpus 与 close analogues 分工

### Broad corpus：30–100+ papers

用于估计趋势：

- section presence/order；
- paragraph/sentence distributions；
- figure/table counts；
- caption length；
- figure-call location；
- recurring evidence roles；
- common plot families；
- main-versus-support allocation；
- semantic annotation 后的 rhetorical move prevalence。

Frequency 不是 quality。

### Close analogues：3–6 papers

用于深入理解：

- exact claim/evidence dependencies；
- 为什么 evidence block B 必须跟在 A 后；
- explanation depth；
- comparator/uncertainty 如何可视化；
- 哪些 negative/failure evidence 留在 main；
- local terminology 与 reader assumptions。

## 可扩展 figure/caption corpus inventory

如果论文已经提取成 `.md` / `.txt`，可以运行：

```bash
python skills/nature-writing/scripts/corpus_figure_inventory.py CORPUS_DIR \
  --json corpus-figures.json \
  --csv corpus-displays.csv
```

它会统计：

- figure/table captions；
- body 中 figure/table calls；
- caption 所在 section；
- 透明的 keyword-based **candidate evidence roles**，例如 orientation/workflow、primary finding、mechanism、validation、OOD/generalization、robustness、failure/limitation、heterogeneity、calibration/diagnostic、resource coverage、theory/model、qualitative synthesis。

这些 role 只是 corpus triage heuristic：**不是 semantic ground truth，不是 writing-quality score，不是 acceptance predictor，也不是“出现次数最多的 plot 就应该照抄”。**

同时使用 `corpus_structure_stats.py` 得到 section/paragraph/sentence surface statistics，再进行 semantic reading。

## Figure planning 最终仍然从当前 paper 出发

最终决策链：

```text
claim
→ reader question
→ scientific/statistical unit
→ estimand
→ data structure
→ uncertainty / alternative explanation
→ representation
→ main/support/omit
```

例如：

- paired effect → 应该显式展示 paired change；
- probabilistic prediction → 如果 claim 涉及 probability quality，就需要 calibration；
- generalization → 要展示 claim 中真正承诺的 regimes；
- failure boundary → 如果改变 headline conclusion，就不应自动塞到 SI；
- small-n continuous data → 必要时展示 individual observations/distribution；
- qualitative theme → 只有 relationship 用图比 prose 更清楚时才画。

不要从“顶刊经常用 heatmap”开始。

## 最终 manuscript-surface QA

只做 content planning 还不够。后续 rewrite、figure generation、caption drafting 都可能把 repository detail 再带回来。

现在所有 manuscript-facing surface 都有最终检查：

- local/repository file paths；
- script/notebook/config filenames；
- output filenames；
- helper/class/function names；
- CLI commands/flags；
- branch/PR/issue/commit/CI/test history；
- designated availability 之外的 raw repository links；
- figure legend 中的 plotting-pipeline language。

核心规则：

> **audit trail 可以知道 artifact 的名字；paper 应该写 science。**

保守机械扫描器：

```bash
python skills/nature-shared/scripts/audit_manuscript_surface.py manuscript.md --strict
```

它也会抓高置信度 punctuation 问题，比如 doubled punctuation、错误 spacing、破损的 Fig. reference、unmatched brackets。会改变 meaning 的 punctuation 仍需 context-aware editing。

## Punctuation 不是“style preference”

Package 现在把 punctuation/copy-editing 作为独立 final QA layer。

它区分：

- 可安全 flag 的 mechanical defect；
- target-specific punctuation，例如 citation/equation punctuation；
- meaning-sensitive punctuation，例如 restrictive comma；
- scientific typography，例如 hyphen / en dash / minus sign。

不存在对所有 journals/disciplines 都安全的 global punctuation transform。

## 我们明确不学习什么

不会推断：

- figures 越多越好；
- prestige journal 常见 layout 就天然更优；
- 某种 visual type 会“导致 acceptance”；
- final published paper 能告诉我们真正 accept 的 causal reason；
- figure type 与 impact 的 correlation 是投稿秘诀；
- 一个 local caption style 是 universal rule；
- qualitative、theoretical、clinical、computational paper 应有相同 figure grammar。

Published papers 是 **某个 publication ecology 中 surviving solutions**，不是 causal acceptance recipes。

## Serious rewrite 可维护的 manuscript-specific plan

```text
Dominant paper archetype
Secondary archetype(s)
Core reader decision
Headline claims
Evidence dependencies
Explanation-depth hotspots
Main-figure roles
Supporting evidence roles
Content to relocate/omit
Close analogue set
Broad-corpus tendencies
Patterns adopted/adapted/rejected
Final manuscript-surface leakage findings
Punctuation/copy-editing findings
```

最终 deliverable 仍然是 prose 和 figures。Research machinery 的目的是提高决策质量，不是让作者被 audit table 淹没。

## 核心原则

> 学习优秀论文背后的 **scientific function 与 reader problem**，不要复制 visible surface。