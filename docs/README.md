# 文档索引

[English](README_EN.md)

仓库已经从一组 Nature-oriented skills 扩展成更完整的 academic-paper system。这里是当前 architecture、写作研究和使用文档的入口。

## 学术写作

- [学术写作研究综述：强论文究竟是怎样写出来的](academic-writing-research.md) — 跨学科 rhetoric、cohesion、stance、sentence flow、human/LLM academic-writing research 与 section-specific writing。
- [自然学术写作：句子到句子的逻辑与表达指南](natural-scholarly-writing.md) — 用 dependency、given/new、identity chain、stance、functional syntax、connective、cadence 与 author voice 修 paragraph/sentence flow。
- [解释充分性：论文到底讲清楚了吗？](explanatory-sufficiency.md) — adaptive elaboration、hidden-premise check、reader reconstruction，以及判断简洁文字是否把必要推理压缩掉了。
- [论文到底应该写什么、哪些内容不该进正文，以及应该画什么图？](manuscript-content-and-figures.md) — content admission、repository-to-manuscript leakage、main/Methods/SI/availability allocation、figure roles 与 plot suggestions。
- [深度论文校准：学习科学任务，而不是模仿顶刊表面](deep-paper-calibration.md) — paper archetypes、2025–2026 cross-archetype direct reading、broad corpus vs close analogue、可扩展 figure/caption inventory、最终 artifact-leakage scrub 与 punctuation QA。

## 架构

- [All-journals Academic-Paper Architecture](all-journals-architecture.md) — journal resolution、writing、analogue calibration、natural prose、author voice、figures、citations、review 与 revision lifecycle。
- [Editor–Reviewer Decision Architecture](editor-reviewer-decision-architecture.md) — target-aware editorial triage、independent review、editor synthesis、decision proof 与 revision closure。
- [期刊接收准备度：编辑、审稿人、路由与修稿](journal-acceptance-readiness.md) — 把 acceptance 拆成 target fit、editorial triage、editor expertise routing、reviewer coverage、evidence maturity、revision closure 与不可控制 editorial context；公开 editor identity 只用于专业路由，不用于个人化 manipulation。

## 教程与接入

- [Open-source Agent Frameworks](open-source-agent-frameworks.md) — OpenClaw/OpenCode/Hermes 与其他 agent 接入。
- [Nature Paper Card Tutorial](nature-paper-card-tutorial.md) — Paper Card 使用教程。

## 核心设计原则

1. Scientific validity 高于 journal prestige 和 surface style。
2. Exact current journal/article-type/stage rule 高于 publisher-family assumption。
3. Evidence completeness 由整个 publication package 承担，而不是把所有细节塞进 main text。
4. 先判断 paper 的 epistemic archetype，再借鉴 writing / figure convention。
5. Broad corpus 用于学习 tendency，3–6 篇 close analogues 用于 manuscript-specific 深度推理；frequency 不是 quality。
6. Natural scholarly prose 面向 reader-facing reasoning quality，不做 detector evasion。
7. Explanatory sufficiency 是自适应 reader support：补缺失推理，不为字数本身扩写。
8. Author voice 是 logic/clarity 修复后的 identity layer。
9. Figure choice 来自 claims、estimands、data structure、uncertainty 与 alternative explanations。
10. Repository/artifact documentation 除非具有科学功能，否则不应泄漏进 scientific narrative；最终所有 manuscript-facing surface 都要再做一次 leakage scrub。
11. Punctuation 与 scientific typography 是 final copy-editing QA，不是任意 style decoration。
12. Acceptance/editor/reviewer engineering 指 decisionability、target fit、expertise routing 与 valid evidence，不是 manipulation；不输出 acceptance probability，也不根据公开 editor identity 推断 leniency/personality/ideology。
13. 写作/评审规则应来自 empirical corpora、stratified direct reading、official guidance、counterexamples 与 regression tests。
