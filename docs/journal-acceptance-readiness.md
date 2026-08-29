# 期刊接收准备度：编辑、审稿人、路由与修稿

论文是否被接收，并不是由某一个编辑、某一个审稿人，或者一封“很会推销”的 cover letter 决定。更接近真实投稿流程的模型是：

```text
科学有效性 / integrity
-> 精确期刊与文章类型匹配
-> 编辑初筛
-> 编辑 / 专业能力路由
-> 外部同行评审
-> 编辑综合判断
-> 修稿闭环
-> 最终 reporting / compliance
```

因此，这个 package 优化的是 **decision readiness（让论文容易被公平、准确地判断）**，而不是 acceptance probability。

## 1. 编辑真正控制什么

编辑通常在这些关键节点拥有决定权：

- 论文是否在 scope 内、是否成熟到值得送审；
- contribution 是否满足该期刊真正的 publication objective；
- 谁来处理稿件；
- 需要哪些审稿专业能力；
- 冲突的 reviewer 意见应该如何加权；
- 哪些问题是修稿必须解决的；
- revision 是否真的关闭了这些 blocker；
- 一篇科学上没有问题的稿件，是否仍然不适合当前 target。

所以 editor triage 与 editor synthesis 很重要，但这并不意味着作者应该针对某个编辑的个人偏好做“心理优化”。

## 2. 公开编辑身份应该怎样使用

公开的 editor 信息只有在解决**专业路由问题**时才有价值，例如：

- 哪个 editorial team / section 覆盖这项科学问题？
- 该期刊是否具有理解这篇稿件 domain + methods 的编辑能力？
- 这篇跨学科稿件是否需要多种 expertise 才能公平评估？
- submission system 是否允许作者 suggest / request editor？
- 某个潜在 editor 是否存在 conflict of interest？

优先使用官方 editor / editorial board 页面；只有在需要核实专业方向时，再使用 ORCID、institutional profile 或公开 publication record。

不要建立这些画像：

- editor 是否“宽松 / 严格”；
- 推测 acceptance propensity；
- personality / ideology；
- citation preference；
- 推测 reviewer friendship network；
- 把 demographic characteristic 当作 persuasion variable。

**Editor identity 是 routing metadata，不是 persuasion target。**

## 3. Multi-editor desk preflight

Desk decision 中确实存在主观判断，尤其是 novelty、priority、breadth、interest 等较“soft”的标准。因此，只模拟一个 editor 不够稳健。

投稿前应该独立运行多种 editor lens：

1. **Scope / article type** — 这篇稿件真的属于这个期刊 / 文章类型吗？
2. **Contribution / positioning** — 真正的 advance 是否清楚、且相对于最近 prior work 定位公平？
3. **Evidence maturity** — 科学证据是否成熟到值得占用 reviewer time？
4. **Readership / objective** — 是否满足 target 明确写出的 importance / interest / utility 标准？
5. **Routing clarity** — domain、method、evidence class、所需 reviewer expertise 是否一眼可恢复？

每个 lens 应该在看到其他结果前独立完成，再做 synthesis。

不能“数票”。如果某一个合理的 editor lens 可以给出有力 desk-rejection reason，就应该把那个理由当成 risk item 去修复或确认不适用。

## 4. Reviewer expertise coverage

对每一个 headline claim，先判断需要哪些专业能力才能公平评估：

```text
domain science
study design / causal identification
statistics
computation / ML
measurement / instrumentation
imaging / assay
clinical / translational / policy context
resource / data stewardship
reproducibility
```

如果期刊允许 reviewer suggestions，就推荐**独立且能力覆盖互补**的专家，而不是挑预计会比较友好的 reviewer。

## 5. Cover letter 是 routing aid，不是广告

好的 cover letter 应该让 editor 很快知道：

- paper 实际建立了什么；
- 为什么属于这个 exact journal；
- novelty / importance 在该期刊公开标准下是什么；
- 是否有 related / concurrent submission 或需要 confidential handling 的事项。

不要使用作者 prestige、flattery、没有证据支撑的“breakthrough / first ever”，也不要为了影响 editor 而战略性引用 editor 本人的论文。

真正的 scientific case 必须在 manuscript 本身成立。

## 6. 修稿本身就是 acceptance engineering

Peer review 后，不应该优化“回复信有多长、多客气”，而应该优化 **revision delta**。

每个 blocking concern 都应该有 resolution test，并通过以下一种真实 route 关闭：

- 加入 decisive evidence；
- 对已有数据重新分析；
- 修正错误；
- 把已经存在但难以找到的证据暴露 / 解释清楚；
- 补足缺失推理；
- 重做弱或误导的 figure / table；
- 缩小 claim；
- 删除 claim；
- 更换 target / article type。

Reviewer 的 request 并不自动等于 mandatory requirement。Editor 应该判断哪些问题真正映射到 publication criteria，哪些只是 optional enrichment。

## 7. Retargeting 不是失败

一篇科学上成熟的 paper 仍然可能不适合某一个 venue：太 specialist、breadth 不足、out of scope，或者 article type 错了。

Target ladder 应该比较：

```text
scope
contribution class
article type
novelty / importance / utility threshold
readership
methods / reporting compatibility
editorial expertise coverage
practical constraints
```

不要只按 impact factor / prestige 排期刊。

## 8. 不可控制的不确定性

即使 paper 已经 decision-ready，真实投稿仍可能因为作者无法正当控制的因素被拒：

- 同时或刚刚 accepted 的高度 overlapping work；
- 多篇强稿之间的 editorial competition；
- reviewer availability；
- editor 对 soft priority criteria 的合理分歧；
- 作者不可见的 confidential information；
- 合法的 editorial discretion。

这些因素要和 repairable manuscript problem 分开记录。

不能因为一次这种 rejection 就自动增加实验、增加 hype，或者开始做 personalized editor targeting。

## 9. Package 现在追踪什么

Academic-paper pipeline 会独立追踪：

```text
science / integrity
scope
contribution / novelty
readership / objective
evidence maturity
methods / statistics / reporting
visual evidence
editorial routing
reviewer coverage
revision closure
compliance
uncontrollable editorial context
```

它可以输出 `decision_ready_for_submission_to_target`，但不会输出 numeric acceptance probability。

如果 exact journal 允许 editor suggestion，机器可验证的 routing profile 要求：

- 当前 policy evidence；
- 官方 editor / editorial-board source；
- professional expertise evidence；
- conflict status；
- 明确的 permitted use。

像 `acceptance_probability`、`leniency_score`、personality、ideology、citation preference 这样的字段会被 validator 直接拒绝。

## Bottom line

真正可持续的 acceptance strategy 是：

**把 science 做对 → 选对 journal → 让 contribution 一眼可恢复 → 暴露 decisive evidence 与 boundary → 让稿件容易被路由到正确 expertise → 经得起 independent review → 让 editor adjudicate 真正 blocker → 逐轮修改 manuscript，直到这些 blocker 在科学上被关闭。**

这叫 acceptance engineering。针对个人 editor 做 manipulation，不是。
