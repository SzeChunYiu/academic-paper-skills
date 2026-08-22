# `nature-reviewer` 技能

[English](README_EN.md)

`nature-reviewer` 用于在投稿前模拟 **journal-aware editor + reviewer decision process**。legacy skill name 不代表旗舰 Nature，也不会把 reviewer recommendation 当投票。系统先解析目标 publication model，把 editorial triage 与独立 technical review 分开，最后再做 editor synthesis 和 author-facing repair map。

## 适合用它做什么

- 对 manuscript、abstract、figure set 或 Results storyline 做投稿前压力测试。
- 解析 exact target 的 decision model，而不是套一个 universal novelty/impact score。
- 模拟 editorial triage：scope、article type、target-specific priority、contribution/evidence 是否容易恢复，以及是否成熟到值得送外审。
- 在互盲条件下生成 reviewers，覆盖 validity/methods、contribution/positioning、reproducibility/clarity/boundary 等 lens。
- 每个 Major Concern 都必须有明确 **resolution test**。
- 把问题分类为 publication-criteria blocker、technical blocker、major repairable、claim recalibration、clarity/reporting 或 optional enrichment。
- 区分 `needs more evidence`、`needs reanalysis`、`needs clearer structure`、`narrow/remove claim` 与 `change target/article type`。
- 把 close analogue papers 作为**领域证据期望的 context**，而不是虚构 journal policy。
- 检查 main-text content 和 figures 是否真正暴露 decisive evidence，还是被无关 implementation/repository detail 淹没。
- 如果 headline claim 需要 validation/generalization/failure-boundary evidence，指出缺失的 plot/figure。
- 交叉核对 terminology、units、counts、numeric precision、Methods facts、tables 与 claims。

## 典型请求

- “按 Nature Methods 做：先 editor triage，再三份独立 reviewer reports，最后综合。”
- “这是 PLOS ONE，不要因为不够 broad-interest 扣分；重点看 validity 和 reporting。”
- “哪些 reviewer concerns 真需要新实验，哪些可以通过收窄 claim 关闭？”
- “这些 figures 足以支持 external generalization 吗，还是 pooled metric 把 site heterogeneity 隐藏了？”
- “哪些 implementation/code detail 应从 manuscript 删除，留在 Methods/availability/repository docs？”

## 你需要提供

- Manuscript、关键 sections、figures/legends、Methods 或 author notes。
- 已知的话提供 exact target journal/venue 与 article type。
- Study design、central claims，以及不能新增 experiment/analysis 的现实限制。
- 如果希望 reviewer simulation 纳入 supplementary evidence，也需要一并提供。

## 产出

- Editorial triage simulation。
- 独立 reviewer reports。
- 不按票数、而按 concern reasoning 加权的 editor synthesis。
- Decision-engineering map：concern class、blocking status、resolution test 与 minimum valid repair route。
- Claim/evidence/boundary weakness 与 missing alternative-explanation tests。
- Figure/evidence gap，包括什么时候新增 plot 或把支持证据提升到 main text 能提高 decisionability。
- 当 science sound 但 publication objective 不匹配时，可给 target-fit recommendation。

## 边界

- 不会虚构 reviewer identity、hidden editorial information 或真实期刊的 final decision/probability。
- Reviewer 互相不可见；模拟 triage conclusion 不会喂给 reviewer packet。
- Analogue-paper pattern 只是 contextual evidence expectation，不是 policy。
- 不会建议挑 friendly reviewers、战略性引用潜在 reviewer、隐藏 competitor/adverse evidence 或添加 cosmetic experiments。
- 更多实验并不自动更好；evidence、reanalysis、clarification、claim narrowing/removal 或 target change 都可能是正确 repair。
- 真实 editor decision 之后的 rebuttal/revision package 使用 `nature-response`。

## 相关技能

- `nature-writing`：投稿前修 argument/content/figures。
- `nature-figure`：设计或重建缺失的 decision-relevant visual evidence。
- `nature-statistics`：深入 statistical validity/reporting audit。
- `nature-response`：真实 decision 后关闭 editor/reviewer concerns。
