# `nature-polishing` 技能

[English](README_EN.md)

`nature-polishing` 用于改写、重构、压缩或翻译 academic prose，同时保持科学含义、evidence boundary、terminology、citation intent 和 author voice。它是 journal-aware 的，而不是 Nature-only；所谓“降低 AI 味”被当作写作质量问题——logic、information flow、stance、syntax、cadence 与真实 author voice——而不是 AI-detector evasion。

## 适合用它做什么

- 把中文学术文本翻译为可投稿英文，同时不改变 science。
- 在换词之前先修 sentence-to-sentence logic。
- 用 proposition dependency 和 `inherits -> relation -> adds -> enables` 重写段落。
- 当 prose 过于 generic、over-smoothed、formulaic、repetitive、connector-heavy 或 machine-like 时，恢复更自然的学术表达。
- 保留有用的技术术语重复和 authorial agency，而不是机械换同义词或删除 `we`。
- substantial rewrite 前精读几篇 close analogue papers，学习 local rhetorical/evidence convention，但不复制 wording。
- 建 compact author-voice profile，大重构后做 re-voice pass。
- 全文润色时识别 codebase/repository debris，并通过 manuscript-content-selection logic 把 operational detail 放到正确位置。
- 压缩 Results，把 core evidence 与 robustness/support 分配到 main text、caption、Methods、Extended Data/SI、availability/artifact layer。
- 科学逻辑稳定后，再适配 exact target journal/article type/stage。
- 对全文或多轮返修稿扫描 terminology、unit、numeric precision、claim drift 与重复 evidence。

## 工作方式

对于 substantial rewrite，整体顺序是：

```text
scientific meaning / claims
-> paragraph and sentence dependency
-> information flow + identity chains
-> stance and evidence strength
-> functional syntax and precise vocabulary
-> necessary connectives
-> natural cadence
-> author re-voice
-> exact journal adaptation
-> consistency / claim-drift audit
```

需要时先读 3–6 篇 close analogue papers，提供 **structural/evidence priors**；作者自己的代表性文本提供 **expression prior**。

“Humanize” 永远不代表故意加错误、随机长短句、奇怪标点、slang 或 AI-word blacklist。

## 方法来源

- [`docs/academic-writing-research.md`](../../docs/academic-writing-research.md)：跨学科写作、cohesion、stance 与 human/LLM academic-writing evidence。
- [`docs/natural-scholarly-writing.md`](../../docs/natural-scholarly-writing.md)：句子到句子的 flow 与自然 academic prose 实操。
- [`docs/manuscript-content-and-figures.md`](../../docs/manuscript-content-and-figures.md)：content allocation 与 repository-to-manuscript leakage。
- `../nature-shared/core/natural-scholarly-prose.md`：research-backed natural-prose contract。
- `../nature-shared/core/author-voice-profile.md`：manuscript voice preservation。
- `../nature-shared/core/analogue-paper-calibration.md`：close-paper structural calibration。
- `../nature-shared/core/main-text-discipline.md`：Results compression 与 evidence allocation。

## 典型请求

- “把这段中文 Results 改成清楚的学术英语，不要写成 generic AI prose。”
- “这段语法都对，但句子之间不连。先重建 dependency 再润色。”
- “大重构 Discussion 后，帮我把作者自己的 voice 恢复回来。”
- “先读几篇真正相似的论文再润色，但不要复制它们的句子。”
- “把不该进 manuscript 的 implementation/repository detail 移掉，并放到正确 layer。”
- “把这个科学内容已经稳定的 draft 从 Journal A 转到 Journal B，但不要改变 claim strength。”

## 你需要提供

- 原文和 section context。
- 不能改变的 facts、data、citations、terminology、uncertainty 和 claims。
- 需要保留 voice 时提供代表性的作者原文。
- 需要 journal-specific adaptation 时提供 target journal/venue 和 article type。
- 希望的输出：只给 rewrite、original/rewrite 对照，或 rewrite + reasoning/risk notes。

## 产出

- 可直接粘贴的英文改写或中英对照版本。
- 关键 change notes：logic、sentence dependency、stance、terminology 与 claim boundaries。
- 大型修改可附 author-voice profile / voice-drift notes。
- 可选 natural-prose diagnostics：orphan sentence、vague referent、connector stuffing、repeated template、generic prestige language、nonfunctional syntactic repetition。
- Results/full-manuscript compression 时可附 main-text allocation/deletion record。
- terminology/unit/precision/claim drift consistency risk list。
- 需要作者确认的 facts 或 citation intent。

## 边界

- 不会虚构 results、mechanisms、statistical significance、citations 或 unsupported interpretation。
- 不会为了显得 prestige 而加强 causality、generality、certainty、novelty 或 importance。
- 不会优化 AI-detector score、维护 `AI-word` blacklist、故意加错误或制造随机 `burstiness`。
- 不会复制 analogue papers 的 distinctive prose，也不会模仿某位在世作者的独特风格。
- Layout-only LaTeX 任务跳过 prose、analogue、naturalization 与 re-voice pass。
- 从零搭 section 或规划 evidence/figures 用 `nature-writing`；最终 figure rendering 用 `nature-figure`。

## 相关技能

- `nature-writing`：argument architecture、content selection、plot/figure suggestions 与 section drafting。
- `nature-figure`：claim-driven figure rendering 与 visual QA。
- `nature-response`：reviewer response 与 revision correspondence。
- `nature-statistics`：statistical text、estimands、uncertainty 与 figure statistics。
- `nature-reviewer`：pre-submission editor/reviewer stress testing。
