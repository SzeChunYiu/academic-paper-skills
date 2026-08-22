# `nature-citation` 技能

[English](README_EN.md)

`nature-citation` 用于把 manuscript passage 或 scientific claim 拆成可引用单元，并在默认情况下按 **best-fit evidence** 找支撑文献，而不是静默使用 prestige-journal whitelist。只有用户明确要求时，才使用 Nature / Science / Cell / CNS / flagship 等 scope。

## 适合用它做什么

- 给 Introduction、Discussion、Methods rationale、reviewer response 或单条 scientific claim 补 supporting references。
- 把长段落拆成稳定编号 claim，例如 `S001`、`S002`。
- 默认广泛搜索最合适 evidence，不再自动限定 Nature/Science/Cell。
- 在任务明确要求时使用 `nature`、`science`、`cell`、`cns`、`flagship` 或其他显式 scope。
- 把 **evidence selection** 与 **目标期刊 bibliography rendering** 分开。
- 说明每篇 candidate source 到底支撑 claim 的哪一部分，以及哪里只属于 adjacent/partial support。
- 默认导出可检查 RIS，并在导出前拦截 personal-author metadata 缺失/不完整的记录。
- 通过 DOI/PMID 获取结构化 author metadata，保留顺序、given names/initials、suffixes 与 collective authors。

## 典型请求

- “给这个 Introduction 的每个 claim 找最强 evidence，不要按 journal prestige 过滤。”
- “这个句子尽量用 primary studies 支撑，并解释 support match。”
- “这个特殊对比只允许近五年 CNS-family papers。”
- “我已经确认这些 DOI，导出 Zotero/EndNote 可用的 RIS。”

## 你需要提供

- 待引用 passage、claim list、DOI list 或 PMID list。
- Evidence scope：默认 `best-evidence`，或者明确 journal/family scope。
- Year range、是否允许 review/guideline/preprint，以及需要时的 discipline-specific evidence constraints。
- 导出格式，例如 `RIS`、`ENW`、Zotero `RDF`。

## 产出

- Claim-segmentation table 与 candidate-reference table。
- 每个 claim 的 insertion point、DOI、journal、year、source type 与 support note。
- 当 paper 只能支持 claim 的一部分时给出明确 evidence-mismatch warning。
- 可选 JSON/TSV/Markdown/HTML review material。
- Reference-manager export；默认 RIS。

## 边界

- 不把 citation count 或 journal prestige 当作 universal evidence-quality score。
- Target Journal X 不代表 citations 只能来自 Journal X。
- Candidate papers 是 support options，不保证最终一定合适。
- 不会把 blog、press release 或 search snippet 当作唯一 scientific evidence。
- 不会因为 source wording 更强就自动加强 manuscript claim。

## 相关技能

- `nature-academic-search`：更广 multi-source literature discovery、verification、citation metrics 与 influential-citer analysis。
- `nature-ref-verifier`：校验已选 bibliographic metadata 与 target rendering。
- `nature-writing`：把 evidence/citations 整合回 manuscript argument。
