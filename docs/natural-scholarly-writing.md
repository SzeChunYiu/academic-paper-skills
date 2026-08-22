# 自然学术写作：句子到句子的逻辑与表达指南

[English](natural-scholarly-writing_EN.md)

这份指南把仓库中的学术写作研究转成可直接执行的修改流程，特别针对这种情况：科学内容本身没有明显错误，但段落读起来过于模板化、过度光滑、像机器生成、句子彼此割裂，或者充满连接词却仍然没有真正的逻辑流动。

它**不是** AI detector 规避指南。不要为了“更像人”而故意加入语法错误、随机长短句、奇怪标点，也不要因为网上有人说某个词“像 AI”就机械删除。

## 核心思想

一个段落真正自然，不是因为句式变化很多，而是因为读者能够理解：**为什么这句话恰好现在出现？**

对于第一句之后的每一句，问：

`继承 X -> 执行关系 R -> 增加 Y -> 使下一步 Z 成为可能`

如果这四项说不清楚，就先不要从换词开始。

## 1. 先写 proposition，再写漂亮句子

把一个不自然的段落暂时拆成最朴素的科学命题：

```text
P1. 模型在内部测试集上表现很好。
P2. 到外部队列后优势消失。
P3. 两个队列的年龄分布明显不同。
P4. 按年龄分层后差异缩小。
P5. 因此原来的泛化 claim 太宽。
```

再画依赖：

```text
P1 建立泛化预期
P2 反驳这个预期
P3 提出可能解释
P4 检验这个解释
P5 根据 P2–P4 收窄结论
```

先把这个依赖关系弄清楚，再重新写英文。

## 2. 每句话都要有依赖关系

### 看似流畅但实际很弱的写法

```text
The model achieved high accuracy on the internal cohort.
Furthermore, external validation is important for clinical models.
The external cohort contained older participants.
Moreover, age is an important clinical factor.
The model performed less well externally.
```

每句话都没有语法问题，但顺序只是“话题相关”，不是科学推理。

### 更强的推理顺序

```text
The model achieved high accuracy on the internal cohort, but performance declined in the external cohort. The external cohort contained substantially older participants, raising the possibility that age-dependent case mix contributed to the discrepancy. Consistent with this explanation, age-stratified analysis reduced the performance gap, although it did not eliminate it. The model therefore generalizes less uniformly across populations than the internal evaluation alone suggests.
```

这里的流动来自：

- 内部结果 -> 外部矛盾；
- 矛盾 -> 候选解释；
- 解释 -> 判别性分析；
- 分析 -> 有边界的结论。

不是因为连接词更多。

## 3. Given -> new 是默认原则，不是死模板

常见而有效的信息推进：

```text
S1: A -> B
S2: B -> C
S3: C -> D
```

下一句从读者已经激活的信息出发，再增加新信息，可以降低工作记忆负担。

但是不同推理需要不同模式。

### Constant topic

```text
The intervention increased response rate.
It also shortened recovery time.
It did not alter adverse-event frequency.
```

适合同一个对象的多个平行属性。

### Contrast

```text
The internal cohort showed a strong effect.
The external cohort showed little evidence of the same effect.
```

平行结构让差异本身更清楚。

### Question -> evidence -> answer

```text
We next asked whether the effect depended on baseline severity. Stratified estimates increased monotonically across severity groups. This pattern suggests that the average treatment effect masks clinically relevant heterogeneity.
```

不要把所有段落强行改成同一种信息推进方式。

## 4. 建立 identity chain，而不是疯狂换同义词

读者必须持续知道“我们现在还在讲哪个对象”。

### 技术术语重复往往是好事

如果全文定义了 `calibration model`，只要 referent 没变，就继续叫 `calibration model`。

不要仅仅为了避免重复而写成：

```text
the model -> the framework -> the approach -> the system -> the technique
```

如果这些词并不严格同义，这种“高级换词”反而破坏逻辑追踪，而且很容易形成一种机器式润色感。

### 把 this / these 说清楚

弱：

```text
This may explain the difference.
```

如果前面有多个可能 referent，更清楚的是：

```text
This age imbalance may explain the difference.
```

### 概念链也可以推进

```text
sampling bias -> differential recruitment -> cohort composition -> external-validity boundary
```

概念可以发展，但每一步都要让读者看见关系。

## 5. 先确定关系，再选 transition

相邻句子之间先确定科学关系：

- evidence；
- explanation；
- cause；
- consequence；
- contrast；
- concession；
- comparison；
- specification；
- example；
- inference；
- qualification；
- next question。

然后才判断是否需要 `however / therefore / moreover` 等连接词。

### 不一定需要连接词

```text
The mutation increased receptor abundance. Surface-binding capacity increased in parallel.
```

关系已经很明确，再加 `Furthermore` 可能只是噪声。

### 需要连接词的时候

```text
The mutation increased receptor abundance. However, ligand affinity was unchanged.
```

这里 `however` 标记了会影响解释的真正对立。

## 6. 让 topic 和新信息出现在读者容易处理的位置

句子开头通常适合放当前活跃的 topic / 已知语境；句尾往往天然获得强调。

比较：

```text
A reduction in prediction error of 18% was observed after recalibration of the model using site-specific prevalence estimates.
```

和：

```text
Recalibrating the model with site-specific prevalence estimates reduced prediction error by 18%.
```

第二句更直接暴露“动作 -> 结果”。

但这不是“永远用主动语态”。当 process/object 才是当前 topic 时，被动语态完全合理。

## 7. 因为 rhetorical function 改变，所以句法改变

不要用 long-short-long-short 的随机交替来“像人”。

合理的功能性变化包括：

### 直接结果

```text
The intervention reduced mortality.
```

### 带关键条件的结果

```text
The intervention reduced mortality only among participants with severe baseline disease.
```

### 限定

```text
Although the association remained after covariate adjustment, residual confounding cannot be excluded.
```

### 对比

```text
Model A improved sensitivity, whereas Model B mainly improved calibration.
```

### 机制关系

```text
Because the mutation prevents receptor internalization, surface abundance remains elevated after stimulation.
```

不同功能自然产生不同句型，这才是真正的 variation。

## 8. 普通但精准的词，通常比华丽词更好

不要因为某个词更罕见，就觉得更 academic。

优先选择：

- field 中真正自然的术语；
- 与证据强度匹配的 verb；
- 正常 collocation；
- 读者能立即识别的表达。

常见空泛 prestige 句式：

- `paves the way for`；
- `underscores the critical importance of`；
- `provides valuable insights into`；
- `represents a significant advancement`；
- `plays a crucial role in`。

这些不是禁词，但如果它们遮住了真正 scientific consequence，就应该把 consequence 写出来。

不要写：

```text
These findings provide valuable insights into treatment heterogeneity.
```

如果真正想表达的是：

```text
The average treatment effect masks a subgroup in which the intervention provides little benefit.
```

就直接写后者。

## 9. Stance 要随证据变化，而不是随“文风”变化

自然学术写作中 confidence 会变化，是因为证据状态不同。

### 直接观察

`We observed...`

### Estimate

`The estimated difference was...`

### Association

`X was associated with Y.`

### 间接解释

`This pattern suggests...`

### 可行解释

`One possibility is...`

### Formal result

`Under assumptions A–C, the theorem establishes...`

不要因为 `demonstrates` 听起来更强就使用它。

## 10. 该有作者的时候，不要把作者全部抹掉

过度机器化的学术英语经常把所有 decision 都写成没人负责的被动结构。

在期刊/学科允许时，第一人称可以清楚表达责任：

```text
We chose the external cohort before inspecting outcome labels.
We interpret this discrepancy as evidence of population-specific calibration drift.
```

当过程才是当前 topic 时，用 process-centered 句法：

```text
Samples were randomized before imaging.
```

真正的问题不是 active vs passive，而是：**这句话此刻应该 foreground 什么？**

## 11. 段尾要做科学工作

弱的 generic closing：

```text
Taken together, these findings highlight the importance of robust validation.
```

更有用的段尾可以是：

### 有边界的结论

```text
The model therefore transfers across sites only after prevalence recalibration.
```

### 剩余不确定性

```text
Whether the residual performance gap reflects unmeasured case mix remains unresolved.
```

### 向下一段交接

```text
We therefore tested whether site-specific feature distributions accounted for the remaining gap.
```

下一段应该接住这个 consequence/question。

## 12. 检查 machine-like standardization

大改后重点扫描：

- 多句都用相同开头；
- 每段都用 generic implication 收尾；
- `Moreover/Furthermore/Additionally` 反复出现；
- 连续很多 `This study...`；
- 每个 interpretation 都只用一个 hedge；
- 同义词很多，但稳定技术术语很少；
- 句子模板完全相同，只换名词动词；
- 作者做出的关键 decision 全变成 agentless passive；
- 语言很顺，但 evidence dependency 很弱。

不要机械修。先问每句话的 rhetorical function 是什么。

## 13. 最后再做 read-aloud cadence audit

只有逻辑稳定后才读出声或模拟口读，检查：

- 长 subject 是否把 verb 拖得太远；
- 是否连续出现同一 rhythm；
- 是否所有句子都同一种开头；
- 关键结论是否埋在中间；
- sentence boundary 是否把一个本应整体表达的关系切断；
- 段落是否没有自然强调点。

只有 cadence 影响理解或 author voice 时才修改。

不要故意加错误或随机变化。

## 14. 大重构之后一定 re-voice

正确顺序：

1. 修科学逻辑；
2. 修句间/段间 dependency；
3. 修 information flow 和 stance；
4. 写成清楚自然的学术英语；
5. 恢复作者自己的 voice。

保留：

- cadence；
- agency；
- technical directness；
- signposting level；
- stable terminology；
- epistemic rhythm。

不要因为原稿中有 ambiguity、awkward calque、unsupported certainty 或 redundancy 就把这些也当作“作者风格”保留下来。

## 15. 一个紧凑的段落检查表

最终检查：

- **Nucleus:** 这一段为什么存在？
- **Dependency:** 为什么这些句子必须按这个顺序？
- **Inheritance:** 每句话继承了什么？
- **Relation:** 它与前一句是什么关系？
- **Advance:** 它增加了什么新信息？
- **Enablement:** 它为什么使下一步成为可能？
- **Identity:** 读者能否持续追踪核心对象？
- **Stance:** claim 强度是否与证据匹配？
- **Syntax:** 句型是否匹配 rhetorical function？
- **Connective:** transition 是否真的做了工作？
- **Cadence:** 节奏变化是否有功能原因？
- **Voice:** 这还是不是同一个作者在写？
- **Drift:** 改写是否偷偷加强了 causality / generality / certainty / novelty / importance？

## 16. 不要这样“humanize”

不要：

- 优化 AI detector probability；
- 因为某个词出现在“AI vocabulary”网帖就删除；
- 故意加入错误；
- 随机化句子长度；
- 强行加入 contraction/slang；
- 对核心术语疯狂换同义词；
- 模仿某位在世作者的独特文风；
- 从 analogue paper 复制特色句子；
- 在关系不成立之前先加连接词；
- 用“humanization”掩盖 unsupported claim。

目标不是隐藏文本怎么产生，而是让科学推理真正可读，并且让文本保持可辨认的作者声音。
