# `academic-paper-pipeline` 技能

[English](README_EN.md)

`academic-paper-pipeline` 是整个 academic-paper system 的 end-to-end orchestration layer。它把 **research → writing → figures/statistics → independent review → editor synthesis → revision → re-review** 变成一个持续循环，直到 simulated editor 认为当前 manuscript 对 resolved target 已经 publication-ready，或者遇到必须由真实作者提供新 experiment/data 的 blocker。

它是 journal-agnostic 的。Nature 只是可选 target adapter，不再是系统默认身份。

## 它解决什么问题

仓库已经有 writing、figure、statistics、research、review、revision 等很多 specialist capabilities。没有 pipeline 时，它们容易变成彼此断开的单次 prompt。

Pipeline 在所有轮次维持同一个 persistent manuscript state：

- claim/evidence ledger；
- figure ledger；
- source/research ledger；
- stable reviewer concern IDs；
- editor must-address conditions；
- revision delta；
- 当前 publication-readiness posture。

## Iteration model

```text
target + paper archetype
-> evidence/source intake
-> research calibration
-> argument + claim/evidence architecture
-> content/figure/statistics planning
-> academic writing
-> technical/reporting/surface QA
-> editor triage
-> independent reviewers
-> editor synthesis
-> minimum-sufficient revision
-> targeted re-review
-> editor closure
   ↳ 只要真实 blocker 仍存在就继续
-> simulated_publication_ready_for_target
   或 explicit blocked/retarget state
```

决定是否收敛的是 editor，不是 reviewer 票数。

## 更接近真实的 review behavior

- 第一轮 reviewers 互相不可见。
- 每个 Major Concern 有稳定 ID 与 resolution test。
- Editor 明确区分 must-address 与 non-essential requests。
- Major technical revision 默认回到对应 original reviewer(s)。
- Minor clarity/surface issue 在 target process 允许时可由 editor 自己 closure。
- Round 1 之后出现新的 blocking concern，必须有明确原因，例如 revision regression、new evidence 暴露新问题等；否则 pipeline 会阻止 reviewer 不断移动 goalpost。
- Reviewer disagreement 按 evidence、expertise 和 editor judgment 处理，不平均 score。

## Revision 时 AI session 可以主动做什么

在工具/data 允许时，pipeline 可以自己执行：

- 研究 current literature 与 nearest papers；
- verify/replace citations；
- 校准 novelty / prior-work boundary；
- reanalyse 用户提供的数据；
- 检查 statistics/reporting；
- 用已有 data 设计/生成新 plots；
- 重构 figure sequence；
- 做 workflow/mechanism diagram/flowchart；
- 展开解释不足的 scientific reasoning；
- 修 sentence-to-sentence logic；
- humanize academic tone，同时保持 author voice；
- 调整 main/Methods/SI/availability allocation；
- 删除 file/script/repository leakage；
- 修 punctuation 与 scientific typography；
- narrow/remove unsupported claims；
- 建议 target/article-type transfer。

它**不能虚构新实验结果**。如果 blocker 真正需要新的 experiment/data collection，就标记 `blocked_on_author_evidence`，并给出 minimum resolution test。

## 不认识的 paper type 自动 research

如果当前 skill set 不能可靠覆盖某种 paper，session 不应硬套 nearest template，而必须先 research。

应检查：

1. current official target guidance；
2. applicable reporting/methodological standards；
3. 需要时约 8–15 篇 comparable recent papers 建 quick profile；
4. 3–6 篇 nearest-neighbor papers 做 deep reading；
5. 主动寻找 counterexamples。

然后建立一个 **temporary manuscript-specific archetype profile**，包括 evidence dependencies、section moves、explanation depth、figure/table roles、support allocation 和 unresolved uncertainty。

## Writing quality gate

Sentence flow 会检查：

```text
inherits X
-> relation R
-> adds Y
-> enables Z
```

同时检查：

- topic/context continuity；
- identity/reference chains；
- 合适时的 given/new progression；
- subject–verb separation；
- stress/emphasis position；
- evidence-to-interpretation warrant；
- analysis-to-analysis handoff；
- connective 是否真的对应逻辑关系。

目标是 rich、coherent scholarly reasoning，而不是 AI 式的短 mini-summary，也不是 verbose filler。

## Content richness

对 central idea/result，pipeline 会检查读者是否获得必要的：

- identity/definition；
- motivation；
- mechanism/inferential logic；
- decisive evidence；
- comparator/baseline；
- uncertainty；
- alternative explanation；
- boundary/assumption；
- prior-work relationship；
- scientific consequence；
- 需要时的 visual evidence。

`Rich` 指科学内容足够理解和评估，不等于单纯写得更长。

## Figure 与 diagram learning

Pipeline 会先判断 paper archetype 再规划 figure sequence。

它可以从：

- broad stratified paper corpora；
- close analogues；
- recent cross-archetype direct-reading notes；
- Graphviz、Schemdraw、Mermaid 等成熟 diagram backends

学习能力和 design principle，但不复制 copyrighted figure layout/visual identity。

## Publication-ready state

成功 terminal label 是：

`simulated_publication_ready_for_target`

要求没有 unresolved integrity、target-criteria 或 central technical blocker；evidence/statistics/reporting/figures 足够；explanation 与 logical flow 足够；prior work 公平；main/support allocation 合理；prose 自然并保留 author voice；最终 artifact-leakage/punctuation QA 通过。

它表示 **simulation 认为 manuscript 已适合 submit/finalize**，不是保证真实期刊一定 accept。

## 其他 terminal states

- `blocked_on_author_evidence`
- `scientifically_sound_but_target_mismatch`
- `current_claims_not_established`
- `blocked_by_integrity_or_compliance`

每种状态都必须给出 cheapest valid path forward。

## 典型请求

- “不断 review + revise，直到 editor 认为可以投稿。”
- “按接近真实 Nature Methods 的返修流程，同一批 reviewers 反复检查直到所有 blocker closed。”
- “这个 paper type 很特殊，先 research comparable papers 应该怎么写，再进入 review/revision loop。”
- “用我们已有 data 补 reviewers 真正需要的 analysis/plots，但绝对不要 invent experiments。”
- “一直迭代 manuscript、figures 和 response，直到只剩 optional comments。”

## 边界

Pipeline 不会 game reviewers、按票数决策、优化 acceptance score、虚构 data、隐藏 negative results 或添加 cosmetic experiments。

目标是让 scientific manuscript 本身更强，不是让 reviewer 模拟器开心。