# 学术写作研究综述：强论文究竟是怎样写出来的

[English](academic-writing-research_EN.md)

这份文档总结当前仓库写作系统背后的研究依据。它不是一套“顶刊万能句式”，也不是要求所有学科使用同一种结构。核心目标是区分三类东西：哪些写作规律具有较强的跨学科可迁移性，哪些明显依赖学科/体裁/研究设计，哪些应该通过目标期刊与相似论文做局部校准。

最后复核日期：2026-08-22。

## 目录

- [1. 核心结论](#1-核心结论)
- [2. 学术写作首先是推理系统，其次才是语言风格](#2-学术写作首先是推理系统其次才是语言风格)
- [3. 为什么不能用一个固定模板写所有论文](#3-为什么不能用一个固定模板写所有论文)
- [4. 论文的 argument spine](#4-论文的-argument-spine)
- [5. 段落应该被理解为一次小型推理过程](#5-段落应该被理解为一次小型推理过程)
- [6. 句子到句子的逻辑流](#6-句子到句子的逻辑流)
- [7. Cohesion 不等于多加 transition](#7-cohesion-不等于多加-transition)
- [8. 句法应该跟着 rhetorical function 变化](#8-句法应该跟着-rhetorical-function-变化)
- [9. Stance、不确定性与作者存在感](#9-stance不确定性与作者存在感)
- [10. 当前研究发现的 AI-like 学术文本问题](#10-当前研究发现的-ai-like-学术文本问题)
- [11. 为什么 AI 词表和 detector-oriented 改写不是正确方向](#11-为什么-ai-词表和-detector-oriented-改写不是正确方向)
- [12. 怎样读 analogue papers](#12-怎样读-analogue-papers)
- [13. 图和数据本身就是论证的一部分](#13-图和数据本身就是论证的一部分)
- [14. 各章节写作的核心任务](#14-各章节写作的核心任务)
- [15. 一套研究驱动的完整写作流程](#15-一套研究驱动的完整写作流程)
- [16. 哪些东西必须保持局部化而不是写成 universal rule](#16-哪些东西必须保持局部化而不是写成-universal-rule)
- [17. 研究来源](#17-研究来源)

## 1. 核心结论

强学术写作不是“正确语法 + academic words”。真正决定可读性和可信度的是，读者能不能重建：

`question/tension -> contribution -> evidence/reasoning -> boundary -> meaning`

这个结构会在更小尺度重复出现：

- 一个 section 要回答一个 reader question；
- 一个 paragraph 应围绕一个必要 nucleus 展开；
- 一句话要继承当前语境中的东西，执行一个关系，增加新信息，并让下一步推理成为可能。

所以本仓库把写作理解成 **scientific/rhetorical engineering -> language realization**，而不是先找模板再往里面填内容。

## 2. 学术写作首先是推理系统，其次才是语言风格

Mensh 与 Kording 的 *Ten simple rules for structuring papers* 有价值的地方，不在于其具体 C-C-C 模型应该成为所有学科的硬规则，而在于它明确把论文结构与读者如何处理信息联系起来，并把 sentence、paragraph、section、whole paper 看成不同尺度的结构问题。

真正应该问的问题不是：

> 这里怎么写得更 academic？

而是：

> 读者此刻必须先理解什么，下一步科学推理才合理？

这样看很多所谓“语言问题”，会暴露出更深的结构问题：

- transition 不自然，可能是逻辑关系根本没有建立；
- 句子太长，可能是里面藏了多个没有拆开的 inference；
- paragraph 很弱，可能有两个 competing nuclei；
- Results 很流水账，可能按实验时间顺序，而不是按 uncertainty reduction 排列；
- Discussion 很 generic，可能只有结果复述，没有 alternative interpretation、boundary 和 implication。

## 3. 为什么不能用一个固定模板写所有论文

大量跨学科 corpus 研究已经说明，固定模板不适合被普遍化。

### Introduction

Lu 等研究了 **5 个社会科学学科的 500 篇 research article introduction**，发现 rhetorical move/step 分布和 phraseology 存在明显学科差异。

因此，固定“四段引言”或每篇都必须有一个 `gap sentence` 不应成为 universal rule。

### Methods

Cotos、Huffman 与 Link 基于 **30 个学术领域、900 篇 Methods text** 构建 Demonstrating Rigour and Credibility 模型。

这说明 Methods 不只是“把步骤说出来”，它更重要的修辞功能是让证据可信、可评估、可复现。但不同 study design 实现这种可信性的方式不同。

### Abstract

Omidian 等研究了 **6 个学科、5,910 篇 abstract**，发现 recurrent expressions 与 rhetorical moves、discipline 存在系统差异。

Weinberger、Evans 与 Allesina 分析 **超过一百万篇 abstract、8 个学科**。这项工作尤其重要，因为它对很多常见“写作建议”进行了经验检验，发现不少流行规则与 citation outcome 并没有想象中一致，而且 journal context 很重要。

因此 abstract 不能只有一种 funnel。

### Headings / macrostructure

大规模 heading 研究同样说明，不同 broad field 的 section naming 和组织差异很大。

IMRaD 很常见，但它不是推理本身的自然法则。

## 4. 论文的 argument spine

在写正文之前，先建立五个对象：

1. **Question / tension**：什么问题尚未解决、解释、测量、验证、比较、综合或变得可行？
2. **Answer / contribution**：本论文真正建立、提供、澄清、检验、综合、限定或推翻了什么？
3. **Evidence chain**：哪些 observation、analysis、proof、source、case、comparison 或 experiment 使这个 answer 可信？
4. **Boundary**：结论在哪些条件成立，又在哪里停止？
5. **Meaning**：这个有边界的答案对于目标研究社区究竟改变了什么？

Contribution 不只是 `novel method`：

- empirical finding；
- mechanism/explanation；
- method/algorithm/instrument；
- dataset/resource/benchmark；
- theory/proof/model；
- replication/validation/robustness；
- negative/null result；
- synthesis/review/taxonomy；
- clinical/practical/policy implication；
- historical/interpretive argument。

增量工作不需要伪装成“断代式突破”。更可信的写法是让 increment 可审计，并解释它为什么重要。

## 5. 段落应该被理解为一次小型推理过程

比“每段只能做一件事”更准确的模型是：**一个 nucleus + 若干 satellites**。

### Nucleus

这个段落存在的主要理由，可以是 claim、question、result、contrast、problem 或 interpretation。

### Satellites

可包括：

- evidence；
- explanation；
- comparison；
- example；
- qualification；
- counterargument/counterevidence；
- implication；
- methodological reminder；
- bridge。

如果这些都服务同一个 nucleus，result + evidence + qualification + implication 完全可以共存于一段。

一个有用的 paragraph choreography 是：

`nucleus -> support/reasoning -> qualification/alternative -> local inference -> next-reader question`

不要求每段填满所有 slot。

### 什么时候应该拆段

- 两个 proposition 都可以单独成为这一段存在的理由；
- evidence 已经开始支撑另一个 claim；
- population/time scale/system 改变，却没有 integration；
- qualification 已经扩展成独立 argument；
- 读者需要同时记住过多 unresolved relation。

## 6. 句子到句子的逻辑流

句间 flow 是自然学术写作最关键的层级之一。

### 先建 dependency graph

不要先改句型。先把 paragraph 抽象为：

```text
S1 建立 phenomenon A
S2 把 A 限定在 condition B
S3 解释 B 为什么改变 interpretation C
S4 用 evidence 检验 alternative D
S5 得到 bounded inference E
```

然后检查实际句序是否暴露这个依赖。

### Why-this-sentence-now test

第一句之后每一句都可以写成：

`inherits X -> relation R -> adds Y -> enables Z`

- **inherits**：继承前文哪个 active concept/result/question/condition？
- **relation**：evidence、explanation、contrast、consequence、qualification、comparison、inference 等？
- **adds**：增加了什么真正的新 proposition？
- **enables**：为什么它使下一步合理？

很多“AI 感”段落的问题正是：每句话都像一个独立的小总结，彼此没有真正 dependency。

### Given -> new

常见默认推进：

`A -> B; B -> C; C -> D`

下一句从读者已经激活的信息启动，再提供新信息。

但它不是强制模板，还可以是：

- constant topic；
- derived themes；
- contrast pair；
- question -> evidence -> answer；
- claim -> evidence -> boundary。

真正不变的问题是：**读者是否理解为什么顺序是这样。**

## 7. Cohesion 不等于多加 transition

这一点有比较强的 empirical evidence。

Golparvar、Crosthwaite 与 Ziaeian 对 **100 篇 applied-linguistics research articles** 的 local/global/text cohesion 进行分析，发现不同 rhetorical section 的 cohesion pattern 显著不同。

随后一项跨学科研究分析 **300 个 Discussion section**，覆盖 applied linguistics、chemistry 与 economics，发现不同 discipline 的 cohesion pattern 也显著不同。

2026 年一项针对 **64 名中国 EFL 学生** 的 mixed-methods 研究发现，显式 coherence instruction 能改善写作表现，高表现学生拥有更强的 **identity-chain development**。

### Identity chain

读者需要稳定追踪对象：

- exact technical term repetition；
- stable abbreviation；
- explicit noun phrase；
- unambiguous pronoun；
- controlled subtype/category relation；
- `this discrepancy` 这样明确的 demonstrative phrase，而不是只有 `this`。

### 为什么技术术语重复往往是好事

科研写作的核心是 referential precision，而不是 literary synonym variety。

如果 `model`、`system`、`framework`、`approach` 不是完全同义，仅仅为了避免重复而轮换这些词，会让逻辑对象漂移。

### Transition

Transition 只能标记已经存在的关系：

- `therefore` 要有真正 inference；
- `however` 要有真正 contrast/concession；
- `moreover` 不能把两个无关事实变成一个 argument。

因此仓库不设 connector density 目标。

## 8. 句法应该跟着 rhetorical function 变化

自然学术英语不是随机 mixing 长短句。

句型应该在 **job 改变时** 变化：

- decisive local result -> direct finite clause；
- qualification -> subordinate/dependent clause；
- comparison -> parallel syntax；
- procedure -> chronological syntax；
- new mechanism/cause -> explicit clause；
- established technical concept -> compact nominalization；
- contrast -> balanced clauses；
- definition -> term 与 defining property 靠近。

这叫 **functional syntactic variation**。

随机化句长不是写作原则。

## 9. Stance、不确定性与作者存在感

Academic writing 不是“没有作者”的语言。作者选择方法、解释结果、限定 claim、比较 alternative，并对 inference 负责。

### 先分 evidence status

- observed；
- estimated；
- associated；
- experimentally manipulated；
- causally identified；
- simulated；
- inferred；
- hypothesized；
- proved under assumptions；
- interpreted from qualitative/source evidence。

然后 proposition-by-proposition 校准 stance。

### Human vs LLM stance

Mo 与 Crosthwaite 对相同题目下 3 个 LLM 和 human academic writers 做比较，发现 LLM 使用的 stance/engagement resource **范围更窄、更重复**。

这不意味着“多加 hedge”。真正含义是：

> 先判断 proposition 的证据状态和与读者的 rhetorical relationship，再选 language。

### 第一人称

第一人称并不天然“不学术”。在学科/期刊允许时，可以清楚表达：

- study decision；
- analytical choice；
- contribution；
- interpretation；
- paper organization。

当 procedure/object 才是 topic 时，被动语态同样合理。

## 10. 当前研究发现的 AI-like 学术文本问题

这里的 `AI-like` 应被当作 **quality diagnosis**，不是 detector 标签。

### Stance / engagement 窄而重复

Mo & Crosthwaite (2025) 的 matched comparison 发现，LLM 的 stance/engagement repertoire 相比 human writing 更窄、更重复。

### Expression 过于 standardized

Zhao & Lei (2026) 的 corpus 研究发现，AI-generated academic abstracts 的表达更一致、更 standardized，style variability 更低。

### 过度 rare / flowery academic vocabulary

2024 年 Lingua 对 ChatGPT 与 human social-science academic text 的比较报告：ChatGPT 存在 infrequent academic vocabulary 与 excessively flowery language 的过度使用。

### 同一 syntax 模板里做 synonym substitution

同一研究指出，ChatGPT 有时通过在 syntactically equivalent structures 中替换同义词制造“变化”；human text 则表现出更复杂的 subordination pattern。

这不意味着“多写从句就更人”。真正结论是：**lexical substitution 不是 rhetorical/syntactic variety。**

### Authorial stance 被弱化

近期 doctoral-writing 研究讨论了 GenAI 时代 stance homogenization 与 depersonalization 的风险。

修复方式不是 `we` 越多越好，而是在作者确实做 decision / interpretation 的地方，让责任可见。

## 11. 为什么 AI 词表和 detector-oriented 改写不是正确方向

Geng 与 Trotta 2025 ACL 的 **Human-LLM Coevolution** 研究显示，当一些被认为“ChatGPT 常用”的词被公众广泛讨论以后，其频率会发生变化。

这说明静态 `AI word list` 的根本问题：human 和 model 会互相适应，词频 signature 本身会漂移。

因此本仓库明确拒绝：

- AI-word blacklist；
- detector-score optimization；
- deliberate grammar errors；
- random short sentences；
- arbitrary punctuation variation；
- random synonym replacement；
- artificial `burstiness`；
- 隐瞒要求披露的 AI assistance。

写作质量应该能解释为：

- logic；
- readability；
- evidence calibration；
- disciplinary convention；
- author voice；
- exact journal/reporting requirement。

## 12. 怎样读 analogue papers

真正有价值的是 near-neighbor paper，不是名气最大的 paper。

### 优先匹配

1. research question / contribution class；
2. study design；
3. evidence/data type；
4. article type；
5. subfield/community；
6. exact venue + recent period。

### 提取

- research need 如何创建；
- contribution 放在哪里；
- evidence dependency sequence；
- 每个 main figure 要证明什么；
- data/control/uncertainty 如何可视化；
- main text vs Methods/SI；
- paragraph/section move；
- background depth；
- stance/signposting tendency；
- counterexamples。

### 不要复制

- sentence；
- distinctive paragraph pattern；
- distinctive figure layout/palette；
- 没有科学理由的 normalization/statistical choice；
- 从 published PDF 反推 production setting。

Analogue paper 是 **structural/evidence prior**；author voice 是独立的 **expression prior**。

## 13. 图和数据本身就是论证的一部分

每个 major figure 都应该能回答：

- 这个 figure 回答什么 question？
- 支撑/限定什么 claim？
- statistical/sample unit 是什么？
- comparator/control 是否可见？
- uncertainty 是否可见？
- raw/individual observation 是否重要？
- 它排除哪个 alternative interpretation？
- 为什么在 main text，而不是 SI？

相似论文可以帮助识别常见 **figure role**：phenomenon、mechanism、validation、generalization、failure boundary。

但最终 plot type 必须根据自己的 data + estimand 决定。

不要因为目标期刊经常用 heatmap / UMAP / bar chart 就跟着用。

## 14. 各章节写作的核心任务

### Title

表达经过所有 qualification 后仍然成立的 durable contribution。不要用 novelty adjective 补偿 vague contribution。

### Abstract

move inventory 取决于 discipline/article type，但读者至少需要恢复 question、contribution、decisive evidence 与 bounded meaning。

### Introduction

真正 research need 可以是：

- unanswered question；
- contradiction/tension；
- missing mechanism；
- weak/inconclusive evidence；
- measurement/identification problem；
- bottleneck/trade-off；
- missing regime/population；
- replication/robustness need；
- benchmark/resource need；
- theory-data mismatch；
- new opportunity。

不要通过贬低 prior work 制造 gap。

### Methods

Methods 的核心是解释为什么 evidence 值得信任。根据 design 可能包括 provenance、sampling、procedure、measurement、controls、analysis、uncertainty、reproducibility、ethics、assumptions。

### Results

按 **reasoning dependency / uncertainty reduction** 排，而不只是 experiment chronology。

每个 block 可理解为：

`question -> evidence -> bounded local inference -> next uncertainty`

### Discussion

常见但非强制 cycle：

`finding -> interpretation -> prior knowledge/alternatives -> qualification -> implication`

### Conclusion

回到 qualification 后仍然成立的 durable answer，不要用 generic impact language 收尾。

## 15. 一套研究驱动的完整写作流程

1. Inventory claims、data、figures、methods、limitations、verified literature。
2. Build argument spine。
3. Classify contribution/evidence type。
4. 在合适时读 3–6 篇 close analogues。
5. 从作者自己的代表性文本建立 author-voice profile。
6. 选择 section move graph。
7. 建 paragraph nucleus + satellites。
8. 分配 main text / figures / Methods / SI evidence。
9. 对困难段落建立 sentence dependency graph。
10. 修 information progression 与 identity chain。
11. 根据 evidence 校准 stance。
12. 根据 rhetorical function 选择 syntax。
13. 只加必要 connectives。
14. 做 cadence/read-aloud audit。
15. 大重构后 re-voice。
16. 做 editor/reviewer decision preflight。
17. 最后应用 exact journal/reporting requirement。
18. 最终做 claim drift 与 consistency audit。

## 16. 哪些东西必须保持局部化而不是写成 universal rule

不要 universalize：

- Introduction 固定段数/顺序；
- structured vs unstructured abstract；
- conclusion-first Results；
- first-person 频率；
- connector density；
- sentence length；
- nominalization density；
- heading structure；
- Discussion sequencing；
- title form；
- figure 数量/类型；
- visual style；
- citation density；
- background explanation 数量。

这些应该通过：

`exact journal/article type + discipline/study design + close analogue papers + author voice`

进行 calibration，同时永远让 scientific validity 优先。

## 17. 研究来源

### Cross-disciplinary research-article rhetoric

- Lu, X., Casal, J. E., & Liu, Y. (2021). *Rhetorical and phraseological features of research article introductions: Variation among five social science disciplines*. System. Corpus: 500 published introductions.
- Cotos, E., Huffman, S., & Link, S. (2017). *A move/step model for methods sections: Demonstrating Rigour and Credibility*. English for Specific Purposes. Corpus: 900 Methods texts across 30 fields.
- Omidian, T., Shahriari, H., & Siyanova-Chanturia, A. (2018). 研究 6 个学科、5,910 篇 research abstract 的 rhetorical moves 与 recurrent expressions。

### Cohesion / coherence

- Golparvar, S. E., Crosthwaite, P., & Ziaeian, E. (2024). *Mapping cohesion in research articles of applied linguistics: A close look at rhetorical sections*. Journal of English for Academic Purposes, 67, 101316. https://doi.org/10.1016/j.jeap.2023.101316
- Golparvar, S. E., Hu, G., & Seyedi, S. E. (2025). *Cohesion in the discussion section of research articles: A cross-disciplinary investigation*. English for Specific Purposes, 77, 1–19. https://doi.org/10.1016/j.esp.2024.08.004
- *Assessing the effects of explicit coherence instruction on EFL students' integrated writing performance* (2026). Assessing Writing, 67, 101019. https://doi.org/10.1016/j.asw.2026.101019

### AI-generated / AI-assisted academic writing

- Mo, Z., & Crosthwaite, P. (2025). *Exploring the affordances of generative AI large language models for stance and engagement in academic writing*. Journal of English for Academic Purposes, 75, 101499. https://doi.org/10.1016/j.jeap.2025.101499
- *A corpus-driven comparative analysis of AI in academic discourse: Investigating ChatGPT-generated academic texts in social sciences* (2024). Lingua, 312, 103838. https://doi.org/10.1016/j.lingua.2024.103838
- Zhao, N., & Lei, L. (2026). *Informality features in AI-generated academic writing: A corpus-based comparison between human and AI*. Journal of English for Academic Purposes, 79, 101629. https://doi.org/10.1016/j.jeap.2026.101629
- *Reconstructing stance in EFL doctoral thesis writing through generative artificial intelligence* (2025). Humanities and Social Sciences Communications, 12, 1963. https://doi.org/10.1057/s41599-025-06249-x
- Geng, M., & Trotta, R. (2025). *Human-LLM Coevolution: Evidence from Academic Writing*. Findings of ACL 2025, 12689–12696. https://aclanthology.org/2025.findings-acl.657/

### Scientific writing / structure

- Mensh, B., & Kording, K. (2017). *Ten simple rules for structuring papers*. PLOS Computational Biology, 13(9), e1005619. https://doi.org/10.1371/journal.pcbi.1005619
- Weinberger, C. J., Evans, J. A., & Allesina, S. (2015). *Ten Simple (Empirical) Rules for Writing Science*. PLOS Computational Biology, 11(4), e1004205. https://doi.org/10.1371/journal.pcbi.1004205

### Pedagogic reader-flow references

- Harvard College Writing Center, *Transitions*: https://writingcenter.fas.harvard.edu/transitions
- Purdue OWL: https://owl.purdue.edu/

这份 bibliography 只是起点。仓库的写作规则应继续通过新的 corpus 研究与真实 near-neighbor paper direct reading 更新。
