# AI-session context engineering evidence — 2026-08-31

> Research note for the academic-paper session-kernel/context-routing optimization.
>
> This note supports the orchestration design. It does not claim that one context strategy is universally optimal across every model or workload.

## 1. Problem being addressed

The academic-writing manifests had accumulated many detailed always-loaded contracts. Those contracts protect important scientific invariants, but loading all of them before the session knows whether it is researching, architecting, drafting one section, reviewing, or releasing creates avoidable context competition.

The optimization question is therefore:

> How can an AI writing session preserve rigorous scientific constraints while exposing only the information needed for the current decision?

## 2. Evidence basis

### 2.1 Long context does not imply reliable use of all context

Liu et al., **Transactions of the Association for Computational Linguistics** 12, 157–173 (2024), “Lost in the Middle: How Language Models Use Long Contexts,” DOI 10.1162/tacl_a_00638.

- Evaluated multi-document QA and key-value retrieval across long-context models.
- Found that performance can degrade substantially depending on where relevant information appears in the context.
- Relevant information placed in the middle was often used less reliably than information near the beginning or end.

Transfer to this pipeline:

- do not assume that putting every writing rule into one giant context guarantees compliance;
- preserve high-priority invariants in a compact kernel;
- retrieve detailed rules when they become decision-relevant.

Source: https://aclanthology.org/2024.tacl-1.9/

### 2.2 Effective context length can be smaller than advertised context length

Hsieh et al., “RULER: What's the Real Context Size of Your Long-Context Language Models?” arXiv:2404.06654 (2024).

- Extends simple needle retrieval with multi-needle, tracing and aggregation tasks.
- Reports substantial performance degradation as context length and task complexity increase even for models marketed with large context windows.

Transfer:

- context capacity should not be treated as permission to preload every contract/source/review;
- complex writing sessions should externalize stable state and retrieve task-specific context.

Source: https://arxiv.org/abs/2404.06654

### 2.3 OpenAI guidance explicitly recommends leaner prompts and relevant-only tool/context exposure

OpenAI, **Model guidance** (current as checked 2026-08-31):

- recommends favoring leaner prompts;
- recommends removing repeated instructions/examples;
- recommends stating each instruction once;
- recommends exposing only tools relevant to the task;
- reports internal coding-agent evals where leaner configurations improved evaluation scores while reducing tokens/cost, with the explicit caveat that results vary by workload and should be validated on representative tasks.

Transfer:

- replace duplicated always-loaded contracts with a compact kernel + triggered detail;
- avoid duplicated instruction statements across simultaneously loaded files;
- validate the restructuring with repository regressions rather than assuming less context is automatically better.

Source: https://developers.openai.com/api/docs/guides/latest-model

### 2.4 OpenAI harness engineering: give the agent a map, not a giant manual

OpenAI, **Harness engineering: leveraging Codex in an agent-first world** (2026).

The article describes a failed “one big AGENTS.md” pattern and identifies several problems:

- context is scarce;
- giant instruction files crowd out task/code/relevant docs;
- when everything is important, guidance loses prioritization;
- monolithic manuals rot and are hard to verify.

Transfer:

- the academic-writing system should have one compact map/kernel;
- detailed scholarly contracts should remain modular and verifiable;
- session checkpoints should carry current decisions instead of replaying the whole work history.

Source: https://openai.com/index/harness-engineering/

### 2.5 OpenAI agent guidance favors smaller clear steps and explicit exit conditions

OpenAI, **A practical guide to building agents**:

- recommends breaking dense routines into smaller, clearer steps;
- recommends making each step correspond to a specific action/output;
- describes runs as loops with explicit exit conditions;
- recommends multiple agents only when complexity/tool overlap justifies orchestration.

Transfer:

- academic sessions use one primary operation (`BOOTSTRAP`, `RESEARCH`, `ARCHITECT`, `COMPOSE`, `AUDIT`, `REVISE`, `REVIEW`, `RELEASE`);
- each operation has an exit test;
- parallelism is reserved for genuinely independent workstreams.

Source: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/

### 2.6 Anthropic context engineering treats context as a finite resource

Anthropic, **Effective context engineering for AI agents** (2025):

- defines context engineering as curating the optimal set of tokens from a larger universe of possible information;
- emphasizes iterative refinement of context across long-running agent loops.

Transfer:

- treat manuscript context as an actively managed working set;
- keep stable state in external artifacts/checkpoints;
- refresh the working set when the operation changes.

Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

### 2.7 Progressive disclosure is an established skill-design pattern

Anthropic, **Equipping agents for the real world with Agent Skills** (2025):

- describes skill metadata as a first level of context;
- full skill instructions as a second level loaded when relevant;
- linked reference files as further levels loaded only when needed;
- explicitly calls progressive disclosure the core design principle for scalable skills.

Transfer:

- the public academic writing/reviewer manifests should load a small kernel;
- detailed formal/statistics/abstract/release contracts should be discovered by stage/task triggers rather than all occupying startup context.

Source: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

## 3. Design decisions supported by the evidence

### 3.1 Compact always-loaded kernel

Always retain non-negotiable scientific invariants and routing logic, not all implementation detail.

### 3.2 Stage-specific bundles

Separate research, architecture, composition, audit, revision, review and release. This reduces unrelated constraints competing during prose generation.

### 3.3 Stable checkpoints

Store decisions, blockers, claim/evidence IDs, required contracts and next action in a compact external state object. Do not use the whole conversation history as the only working memory.

### 3.4 Evidence cards

Convert sources into claim-linked cards; retrieve exact source passages only when needed. This preserves provenance without carrying raw search corpora into every writing turn.

### 3.5 Delta-first revision

Give revisers the affected section, live concern IDs, resolution tests and changed evidence rather than every prior review artifact.

### 3.6 Deterministic tools before model context

Use validators/scanners for counts, hashes, schema checks and mechanical signals, then pass concise results into the model for scholarly judgment.

### 3.7 Deliberate whole-paper passes

Whole-paper context remains necessary for global coherence, self-containment, consistency, review and release. The optimization is not “never use long context”; it is “use full context when the question is genuinely global.”

## 4. Important limits

- The cited evidence does not establish one universal optimal token budget.
- Different models have different context behavior.
- Some academic tasks genuinely need the whole manuscript or a large source set.
- Removing too much context can be as harmful as loading too much.
- Progressive disclosure is only safe if the routing kernel reliably triggers mandatory detailed contracts.
- Efficiency gains must be evaluated against scientific correctness, not token count alone.

## 5. Repository-level testable hypothesis

The new architecture should improve session effectiveness if it can simultaneously maintain:

1. all existing scientific release invariants;
2. mandatory triggerability of detailed contracts;
3. much smaller always-loaded manifest working sets;
4. resumable compact checkpoints;
5. no increase in false PASS behavior in existing regression suites.

That is the standard used for this change.
