# `academic-writing` 技能

[English](README_EN.md)

`academic-writing` 是本仓库 **canonical、journal-agnostic** 的学术论文写作 skill。它根据真实 scientific evidence 起草和重构 manuscript，而不是从 Nature 模板开始。

旧的 `skills/nature-writing/` 目录只作为 compatibility/reference implementation layer 保留成熟的 section fragments、examples 与 corpus scripts。**新的 user-facing invocation 是 `$academic-writing`。**

## 它做什么

- 先识别真正的 paper archetype，再决定 structure；
- 先建立 argument 与 claim/evidence dependency，再 polish sentences；
- 遇到不熟悉的 paper type / venue 时先 research，而不是猜 convention；
- 用 broad stratified corpus + 3–6 篇 close analogue papers 学习，但不复制 prose/figure identity；
- 检查 central ideas 是否解释到目标读者真正能理解；
- 强化 sentence-to-sentence logical flow；
- 规划论文真正需要的 evidence 与 figures；
- 决定内容进入 main text、Methods、SI、availability、artifact docs 还是删除；
- 保留 author voice，同时避免 generic AI-like prose；
- scientific logic 稳定后才适配 exact target；
- 最终对所有 manuscript-facing surface 做 filename/script/repository leakage 与 punctuation/typography QA。

## Exact venue decision contract

当任务涉及 target-specific readiness 时，`academic-writing` 会解析 **exact
venue × article type × stage × effective date**，并分别保存 scientific gates、
novelty/impact/breadth/audience-interest gates、burden-of-doubt、allowed repairs、
review model、AI/confidentiality policy、acceptance states 与 certification layer。

仓库维护的 TMLR、Nature Article 与 PLOS ONE Research Article snapshots 用于展示
不同 objective，而不是假装所有期刊都已 hard-code。未知、stale、future-effective
或有冲突的 target 必须走 live official-source resolution；fallback profile 永远不能
当成 exact journal policy。

## Study protocol 与 conduct contract

在把 Methods、Results、claims 或 figures 写成 authoritative surface 之前，skill 会
先物化：

```text
protocol version -> analysis-plan version -> conduct receipt
-> deviation ledger -> analysis/result -> bounded claim
```

10 个 maintained study-type adapters 覆盖 randomized、observational、
computational/ML、animal、systematic-review、qualitative、experimental、resource
与 exploratory work，但不宣称存在 universal best design。Behavioral checks 会阻断
false prospective label、undisclosed outcome change、未验证的 randomization/blinding
execution、隐藏的 stopping/exclusion/harms、evaluation leakage、无 timing 支持的
confirmatory status、broken data lineage 与缺失的 required ethics authority。

39-source evidence registry 记录 19 个 full-text、20 个 abstract-level reads、
transfer limits 与 frozen 84-record search log。通过只代表 bounded traceability，
不是 scientific-validity certificate，也不是 journal-acceptance prediction。

## Scientific display decision contract

每个承担 evidence 的 plot、figure、table、image plate 或 diagram 都可以绑定到
machine-readable contract：

```text
reader question -> estimand/scientific object -> statistical unit/data structure
-> candidate representation -> allowed/prohibited inference
-> data snapshot -> analysis receipt -> render receipt -> source data
-> caption/accessibility -> final-size review
```

Maintained adapters 只返回 candidate families 与 scientific obligations，不宣称存在
universal best chart。Behavioral checks 会 fail closed 于 hidden pairing、denominator
drift、stale analysis/render lineage、undefined uncertainty、undisclosed group
omission、embedding/workflow overclaim、color-only encoding 与 final-stage alt-text
缺失。

初始 evidence registry 包含 39 个已核对 sources（20 个 full text、18 个
abstract-level、1 个 official standard），并记录 search provenance、read depth、
supported decisions、transfer limits、contradictions 与 update triggers。

## Writing model

```text
scientific evidence
-> paper archetype
-> protocol + analysis plan + executed conduct + deviations
-> question / contribution
-> claim/evidence/boundary map
-> content selection
-> broad corpus + close analogues（需要时）
-> figure/statistics plan
-> scientific display decision contracts
-> section moves
-> paragraph dependencies
-> sentence dependencies
-> explanatory sufficiency
-> natural scholarly prose + author voice
-> exact target adaptation
-> final manuscript-surface QA
```

## Sentence logic

困难段落逐句检查：

```text
inherits X
-> relation R
-> adds Y
-> enables Z
```

同时检查 identity chains、topic continuity、合适时的 given/new progression、subject–verb distance、stress/emphasis、evidence-to-inference warrant 与 analysis-to-analysis handoff。

Connective 只能标记已有 relation，不能凭空制造逻辑。

## Rich content，但不 bloated

对 central idea/result，检查读者是否获得足够的：

- identity/definition；
- motivation；
- mechanism/inferential logic；
- decisive evidence；
- comparator/baseline；
- uncertainty；
- alternative explanation；
- assumption/boundary；
- prior-work relationship；
- scientific consequence；
- 需要时的 visual evidence。

这是 **minimum sufficient scientific explanation**，不是 maximal word count。

## 从其他 papers 学习

使用两层：

- **broad stratified corpus**：几十/几百篇真正 comparable papers 的 descriptive tendencies；
- **3–6 close analogues**：深入研究 evidence sequence、explanation depth、figure roles、uncertainty、terminology 与 reader assumptions。

Published frequency 不是 quality score，也不是 acceptance rule。

学习背后的 function，再根据当前 paper 的 evidence 写原创 prose、做原创 visuals。

## 不认识的 paper type

如果当前 paper class 无法可靠覆盖，`academic-writing` 不会硬套 nearest template。

它会研究：

1. current official target guidance；
2. applicable reporting/methodological standards；
3. comparable recent papers；
4. nearest-neighbor full papers；
5. counterexamples。

然后建立 temporary manuscript-specific archetype profile。

## Figures

Figure planning：

```text
claim
-> reader question
-> scientific/statistical unit
-> estimand / visual object
-> data structure
-> uncertainty / competing explanation
-> representation
-> main/support/omit
```

Qualitative/theory paper 完全可能不需要 quantitative main figure。Failure boundary 如果改变 headline conclusion，也可以进入 main figure。

Detailed rendering 与 scientific diagrams 交给 figure skill。

## Natural scholarly tone

目标不是 AI-detector evasion。

Skill 会修：

- repetitive stance；
- standardized cadence；
- generic prestige language；
- 损害 technical identity 的 synonym rotation；
- connector stuffing；
- 隐藏 meaningful author decisions 的 depersonalized prose；
- repeated sentence/paragraph templates。

Logic/evidence 修好后再恢复 author voice。

## Final surface gate

交付前检查：

- file/directory paths；
- script/notebook/config/output filenames；
- helper/class/function names；
- CLI commands/flags；
- branch/PR/issue/commit/CI residue；
- availability 之外的 raw project URL；
- doubled/missing punctuation；
- punctuation spacing；
- bracket balance；
- malformed figure references；
- range/minus/hyphen/unit；
- target-aware citation/equation/legend punctuation。

**Audit trail 可以知道 artifact 名字；manuscript 应该写 science。**

## 重复 review / revision

如果希望系统持续 research、write、改 figures、review、revise、re-review，直到 simulated editor 达到 terminal decision，使用 `academic-paper-pipeline`。

## 边界

- 不会虚构 results、experiments、citations、mechanisms、significance、uncertainty 或 novelty。
- 不会为了 presentation 隐藏 contradictory evidence。
- 不会复制 analogue papers 的 distinctive prose 或 visual identity。
- 不会把 Nature convention 强加给 non-Nature target。
- 不会把更多字、更多 figures、更多 experiments 自动视为更强 paper。
- 不会因为 AI session 看得到 repository，就把 implementation detail 泄漏进 manuscript。

## Compatibility

旧 `nature-writing` implementation 为 backward compatibility 与内部 reference 保留，但它不再是 canonical public writing skill，也不应该被新任务 implicit invoke。
