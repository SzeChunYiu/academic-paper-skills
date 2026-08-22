# 文档索引

[English](README_EN.md)

仓库已经从一组 Nature-oriented skills 扩展成更完整的 academic-paper system。这里是当前 architecture、写作研究和使用文档的入口。

## 学术写作

- [学术写作研究综述：强论文究竟是怎样写出来的](academic-writing-research.md) — 跨学科 rhetoric、cohesion、stance、sentence flow、human/LLM academic-writing research 与 section-specific writing。
- [自然学术写作：句子到句子的逻辑与表达指南](natural-scholarly-writing.md) — 用 dependency、given/new、identity chain、stance、functional syntax、connective、cadence 与 author voice 修 paragraph/sentence flow。
- [解释充分性：论文到底讲清楚了吗？](explanatory-sufficiency.md) — adaptive elaboration、hidden-premise check、reader reconstruction，以及判断简洁文字是否把必要推理压缩掉了。
- [论文到底应该写什么、哪些内容不该进正文，以及应该画什么图？](manuscript-content-and-figures.md) — content admission、repository-to-manuscript leakage、main/Methods/SI/availability allocation、figure roles 与 plot suggestions。

## 架构

- [All-journals Academic-Paper Architecture](all-journals-architecture.md) — journal resolution、writing、analogue calibration、natural prose、author voice、figures、citations、review 与 revision lifecycle。
- [Editor–Reviewer Decision Architecture](editor-reviewer-decision-architecture.md) — target-aware editorial triage、independent review、editor synthesis、decision proof 与 revision closure。

## 教程与接入

- [Open-source Agent Frameworks](open-source-agent-frameworks.md) — OpenClaw/OpenCode/Hermes 与其他 agent 接入。
- [Nature Paper Card Tutorial](nature-paper-card-tutorial.md) — Paper Card 使用教程。

## 核心设计原则

1. Scientific validity 高于 journal prestige 和 surface style。
2. Exact current journal/article-type/stage rule 高于 publisher-family assumption。
3. Evidence completeness 由整个 publication package 承担，而不是把所有细节塞进 main text。
4. Close analogue papers 是 structural/evidence priors，不是 wording/visual templates。
5. Natural scholarly prose 面向 reader-facing reasoning quality，不做 detector evasion。
6. Explanatory sufficiency 是自适应的 reader support：补缺失推理，不为字数本身扩写。
7. Author voice 是 logic/clarity 修复后的 identity layer。
8. Figure choice 来自 claims、estimands、data structure、uncertainty 与 alternative explanations。
9. Repository/artifact documentation 除非具有科学功能，否则不应泄漏进 scientific narrative。
10. Editor/reviewer engineering 指 decisionability 与 valid evidence，不是 manipulation。
11. 写作/评审规则应来自 empirical corpora、direct reading、official guidance 与 regression tests。
