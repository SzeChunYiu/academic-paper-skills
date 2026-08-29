# 证据分级的论文接收机会优化

[English](acceptance-optimization_EN.md)

这份指南说明 academic-paper system 如何在不假装“期刊接收可被控制”的前提下，尽可能提高**合法、科学的发表机会**。

核心原则是：

> 从研究问题和设计阶段开始，逐层减少所有可避免的 rejection 原因；同时把无法控制的 editorial uncertainty 明确隔离出来。

## 全生命周期

系统把 publication opportunity 看成一条完整链路：

```text
question value / scientific utility
-> 能支撑目标 claim 的 study design
-> evidence maturity
-> analysis / uncertainty / reporting
-> figures and tables
-> exact target and article type
-> desk-rejection stress test
-> editorial routing
-> expert peer review
-> editor synthesis
-> revision closure
-> transfer / retargeting
```

这明显不只是“润色论文”。

设计本身无法支撑的 claim，不可能靠漂亮的 prose 修好；一个优秀的 specialist paper 也不应该为了模仿 broad-interest journal 而被扭曲。

## 接收建议必须标注 evidence grade

| Grade | 含义 | 用法 |
|---|---|---|
| A | 直接 experimental / quasi-experimental publication-process evidence | 只支持实际测量到的 outcome |
| B | large-scale / multi-journal observational meta-research | strong prior，不当作 causal proof |
| C | single-journal / narrow-domain observational evidence | 用于发现 failure mode，并注明 transfer limit |
| D | 当前 official target policy / reviewer criteria | 在适用时可以形成 exact target gate |
| E | editor/expert practice guidance | workflow guidance，不是 acceptance proof |
| H | public peer-review-history heuristic | 只学习 concern → repair pattern |
| MANUSCRIPT_INTERNAL | 当前项目自己的 scientific evidence/state | 在科学上可成为 hard gate |

一个 accepted paper 的 public review history 不能因为“最后接收了”就自动变成 hard acceptance rule。

## 优化要从写论文之前开始

如果项目仍然是 prospective，系统会检查：

- 这个 research question 在结果为 positive、null、negative 或 heterogeneous 时是否仍然有科学价值？
- proposed design 是否真的能支持 intended headline claim？
- 需要什么 comparator、control、uncertainty、validation、failure-boundary evidence？
- 怎样让研究无论结果方向如何都具有可解释性？
- 有没有合适的 Registered Report route，可以在结果未知之前先接受方法和分析设计的 peer review？

目的不是“设计出容易得到 positive result 的研究”，而是设计出**无论结果方向如何都科学可解释、具有发表价值的研究**。

## Registered Reports

对于仍然 prospective 且符合资格的项目，系统会在 outcome access 之前检查 exact current target policy。

Registered Report 可能允许 Stage 1 在结果未知前 review research question、design 和 analysis；符合 venue 条件的 protocol 可以获得 in-principle acceptance。Stage 2 的发表随后主要取决于是否忠实执行 approved protocol，以及最终 interpretation 是否合理，而不是结果是否 positive/significant。

它不是 universal shortcut：Stage 1 仍可能被拒；不同 field/journal 的 coverage 不同；已经看过结果的项目也不能伪造 prospective status。

## 从 claim 倒推 evidence architecture

每一个 headline claim 都倒推：

```text
claim
-> estimand / scientific object
-> independent unit
-> design / identification
-> measurement validity
-> comparator / control
-> sample / information size
-> uncertainty
-> strongest alternative explanation
-> discriminating evidence
-> robustness / sensitivity
-> failure boundary
```

目标是**shortest sufficient evidence set**，不是实验数量最大化。

## 投稿前 red team

提交之前，pipeline 从多个独立方向攻击 manuscript：

- domain science / prior-work positioning；
- design / identification；
- measurement / controls；
- statistics / uncertainty；
- reporting-standard completeness；
- figure/table/data visibility；
- explanatory sufficiency / sentence logic；
- exact target scope / article type；
- editorial routing / reviewer expertise coverage。

如果 quantitative analysis 是核心，会增加 specialist statistical red team。随机试验支持 statistical review 能改善 manuscript quality，但系统不会把这个结果夸大成“已证明提高 acceptance rate”。

## Desk-rejection stress test

系统会主动尝试用常见、可避免的原因 desk-reject 当前稿件：

1. wrong target / article type；
2. question、rationale 或 contribution 不清；
3. design 无法支撑 central claim；
4. methods / analysis 描述不足或本身薄弱；
5. decisive evidence 被埋藏或视觉表达错误；
6. writing / explanation 阻碍理解；
7. policy / compliance 未解决。

每一个 blocker 必须有具体 closure test。

## Fit-first target ladder

如果目标是“成功发表”，而不是死守某一个 journal，系统建立类似下面的 ladder：

```text
stretch_but_compatible
best_fit
robust_fit
specialist_fallback
alternative_article_type
Registered Report route（若 prospective 且 eligible）
```

比较 target 时看 scientific scope、contribution class、evidence expectation、readership、article type、reporting compatibility、review model 和实际限制，而不是只看 impact factor。

## 从 public peer review 学习，但必须控制 survivorship bias

Nature Communications、PLOS、eLife、TMLR/OpenReview 等透明 review archive 可以让系统看到真实的：

```text
initial claim/evidence
-> reviewer/editor concern
-> actual author repair
-> changed evidence/analysis/figure/text/claim
-> re-review / final state
```

可以学习：

- 什么情况下新增 control 真正排除了 alternative explanation；
- 什么情况下 reanalysis 已经足够；
- figure redesign 怎样把本来就存在的 evidence 暴露出来；
- 什么情况下 authors 选择 narrow claim，而不是继续加 experiment；
- 哪些 reviewer request 最后并不是 editor 真正要求的 publication condition。

但是 accepted histories 天生有 survivorship selection。因此它们只能是 Grade H heuristic，必须记录 survivorship warning，并且和 rejection-report / rejected-case evidence 一起看。

系统绝不会把“某个 change 出现在 acceptance 之前”直接解释为“这个 change 导致 acceptance”。

## Revision 看 scientific delta，不看 response letter 有多长

每轮修稿记录真正发生了什么：

- new evidence / control / validation；
- reanalysis / sensitivity analysis；
- statistics correction；
- figure/table redesign；
- Methods / explanation expansion；
- limitation made visible；
- claim narrowed / removed；
- target / article type changed。

一封很长、很礼貌的 rebuttal 并不能替代 manuscript/evidence 的真实变化。

## Rejection triage

收到 rejection 后先分类：

- scientific blocker；
- target mismatch；
- manuscript/evidence visibility failure；
- policy/compliance；
- unresolved review disagreement；
- uncontrollable editorial context；
- exact policy 下合理的 appeal candidate。

然后才决定应该补 evidence、reanalyze、改 writing/figures、narrow claim、appeal、transfer 还是 retarget。

## 有些东西无法合法 engineer 掉

即使 paper 已经 decision-ready，也可能遇到：

- authors 不知道的 overlapping work；
- 多个 strong submissions 的竞争；
- reviewer availability；
- 对 soft priority criteria 的合理 editor disagreement；
- confidential editorial information；
- 无法完全还原成 public rule 的 editorial discretion。

这些因素单独进入 `uncontrollable editorial context`，避免系统对每一次 rejection 都机械推荐更多 experiments 或更夸张的 framing。

## Hard boundaries

系统绝不使用：

- editor leniency / harshness profile；
- reviewer friendliness score；
- individual acceptance-propensity estimate；
- strategic citations to likely editors/reviewers；
- demographic / political / religious / personality profiling；
- 隐藏 negative/adverse evidence；
- 夸大 novelty/significance；
- fabricated experiments/results；
- prestige-only target ranking；
- AI-detector gaming；
- 把 accepted-paper survivorship pattern 当成 causal acceptance rule。

## 最强允许的 readiness label

acceptance-optimization layer 最多只能给出：

`acceptance_optimized_decision_ready_for_target`

它表示：在当前 evidence 和 policy 下，可避免的 scientific、target、presentation、reviewability blocker 已经被系统性攻击并关闭。

它**不等于 likely accepted**，也不会附带 numeric acceptance probability。
