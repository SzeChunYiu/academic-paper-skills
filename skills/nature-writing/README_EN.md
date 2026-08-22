# `nature-writing` Skill

[中文说明](README.md)

`nature-writing` drafts, restructures, and plans journal-aware academic manuscripts from author-provided evidence. It is no longer a Nature-style template writer: it builds the scientific argument first, studies close analogue papers when useful, decides what content and figures belong in the paper, checks whether important ideas are explained deeply enough, repairs sentence-to-sentence logic and natural scholarly prose, preserves the author's voice, and applies exact journal requirements last.

## What To Use It For

- Build titles, abstracts, introductions, related work, Methods, Results, Discussions, Conclusions, or a full manuscript argument.
- Reconstruct `question/tension -> contribution -> evidence chain -> boundary -> meaning` before drafting prose.
- Study a few genuinely comparable papers to learn current evidence architecture, figure roles, main-text/SI allocation, explanation depth, and local rhetorical conventions without copying wording.
- Check **explanatory sufficiency**: whether a central idea, method, mechanism, result, equation, or implication has enough identity, rationale, logic, evidence, boundary, and connection for the intended reader to understand it without guessing.
- Detect hidden premises and conceptual jumps where a polished short sentence has compressed away an essential reasoning step.
- Decide what belongs in main text, figures, legends, Methods, Extended Data/SI, Data/Code/Resource Availability, repository documentation, or nowhere.
- Detect and remove **repository-to-manuscript leakage** such as file paths, script/helper names, setup commands, configs, internal modules, developer workflow, and repeated project links when they do not perform a scientific function.
- Suggest what figures/plots the paper needs from the claim, reader question, estimand, data structure, uncertainty, and competing explanation before `nature-figure` renders them.
- Repair paragraphs whose individual sentences are grammatical but disconnected by mapping `inherits -> relation -> adds -> enables` for every sentence.
- Make academic prose more natural without detector gaming: preserve precise technical repetition, use functionally motivated syntax, calibrate stance locally, avoid connector stuffing and generic prestige language, then restore the author's own cadence and agency.
- Allocate Results to the shortest sufficient main-text evidence chain while keeping conclusion-changing negative evidence and boundaries visible.
- Run editor/reviewer decision preflight and choose the minimum valid repair: explanation/restructuring, evidence, reanalysis, correction, claim narrowing/removal, or target/article-type change.
- Prepare first-submission materials and exact target-journal/article-type/stage checks.

## Workflow

For substantial manuscript work, the writing engine follows roughly:

```text
evidence/claims
-> argument spine
-> content triage
-> close analogue study
-> author-voice profile
-> evidence + figure/plot planning
-> section move graph
-> paragraph nuclei + satellites
-> sentence dependency / information flow
-> explanatory sufficiency / hidden-premise audit
-> natural scholarly prose
-> editor/reviewer preflight
-> exact journal adaptation
-> final consistency and claim-drift audit
```

For important ideas, the explanation-depth check asks whether the reader can reconstruct, as relevant:

```text
what
-> why it is here
-> how it works / why the inference follows
-> what evidence or comparison supports it
-> what assumption/boundary applies
-> what it enables next
```

The skill does **not** force all six elements into every passage. Explanation expands with `centrality × unfamiliarity × inferential dependence` and contracts for routine, already-explained, or artifact-only material.

The key separation is:

```text
author evidence = truth constraint
journal/reporting rules = compliance constraint
analogue papers = structural/evidence priors
author voice = expression prior
```

Natural scholarly prose is the quality floor; author voice is the identity layer above it.

## Typical Requests

- "Rebuild this Introduction from the actual evidence and research need; don't force a Nature template."
- "This explanation is too compressed. Check whether a reader can actually understand the idea and expand only the missing reasoning."
- "Read 4–6 similar papers first, then rewrite these Results and tell me what should stay in the main text versus SI."
- "This paragraph sounds AI-written. Repair the sentence-to-sentence logic and make it natural while preserving my voice; don't optimize an AI detector."
- "The source material includes code and repository docs. Keep only scientifically relevant information in the paper and move operational details to the right place."
- "Given these claims and data, propose the main figures and specific plot types before we write the Results."
- "Preflight this paper as editor and reviewers and identify the cheapest scientifically valid changes before submission."

## What You Need To Provide

- Core claims/questions, figures, data/results, Methods facts, limitations, and any evidence that must not be altered.
- Representative author prose when preserving a recognizable voice matters.
- Target field, paper type, study design, and exact journal/venue when known.
- Comparable papers if you already have preferred analogues; otherwise the workflow can identify the needed comparator profile.
- Source code/repository/project materials only when they are relevant to method/resource/reproducibility work; the skill will not automatically turn them into manuscript prose.

## Outputs

Depending on the task, outputs can include:

- ready-to-paste manuscript prose;
- argument spine and section move map;
- **explanation ledger**: `concept/inference -> reader baseline -> missing explanation element(s) -> recommended expansion -> destination -> sufficient/under-explained/over-explained`;
- content-allocation ledger: `main / figure / legend / Methods / Extended Data/SI / availability / repository / omit`;
- repository-leakage list with the scientific abstraction or correct destination for each removed artifact detail;
- shortest sufficient evidence chain;
- figure/plot suggestion ledger: `claim/question -> statistical unit -> estimand -> plot -> uncertainty/comparator -> main/support`;
- analogue-paper `adopt / adapt / reject / unresolved` decisions;
- compact author-voice profile and re-voice notes;
- sentence/paragraph dependency repairs;
- editor/reviewer blocker map and resolution tests;
- first-submission package and `ready / ready_with_author_checks / blocked` status when requested.

## Method Sources

The writing rules are research-backed rather than based on one prestige-journal style.

- [`docs/academic-writing-research_EN.md`](../../docs/academic-writing-research_EN.md): cross-disciplinary research on rhetorical moves, cohesion, stance, human/LLM academic writing, section structure, and writing process.
- [`docs/natural-scholarly-writing_EN.md`](../../docs/natural-scholarly-writing_EN.md): practical sentence-to-sentence flow and natural-prose repair.
- [`docs/explanatory-sufficiency_EN.md`](../../docs/explanatory-sufficiency_EN.md): how to detect under-explanation, hidden premises, and when to elaborate versus compress.
- [`docs/manuscript-content-and-figures_EN.md`](../../docs/manuscript-content-and-figures_EN.md): what belongs in a paper, repository-to-manuscript leakage, evidence allocation, and plot/figure planning.
- `references/cross-disciplinary-writing-evidence.md`: empirical corpus evidence embedded in the skill.
- `references/direct-reading-notes-2025-2026.md`: direct reading across contrasting publication ecologies.
- `../nature-shared/core/analogue-paper-calibration.md`: focused 3–6-paper near-neighbor study.
- `../nature-shared/core/explanatory-sufficiency.md`: minimum-sufficient explanation and reader-reconstruction contract.
- `../nature-shared/core/natural-scholarly-prose.md`: research-backed natural scholarly expression contract.
- `../nature-shared/core/manuscript-content-selection.md`: content admission and destination model.
- `../nature-shared/core/figure-evidence-planning.md`: claim-driven plot/figure planning.

## Boundaries

- The skill does not invent results, mechanisms, statistical significance, references, uncertainty, limitations, novelty, or rationales that are not supported by the work.
- It does not equate longer prose with better explanation; routine knowledge and already-sufficient passages remain concise.
- It does not treat `humanizing` as AI-detector evasion, deliberate mistakes, word blacklists, random sentence lengths, or forced informality.
- It does not copy sentences, distinctive paragraph structures, figure layouts, or visual identity from analogue papers.
- It does not assume more experiments are always the answer; explanation/restructuring, narrowing/removing a claim, or changing target can be correct.
- It does not put every reproducibility detail in the main narrative: Methods, SI, availability statements, and repositories have different jobs.
- Exact current target-journal instructions and reporting standards override generic/local placement defaults.
- For final figure rendering and export, use `nature-figure`; for real post-decision rebuttals/revision correspondence, use `nature-response`.

## Related Skills

- `nature-polishing`: polish/restructure existing prose using the same explanatory-sufficiency, natural-prose, and author-voice principles.
- `nature-figure`: turn the claim-driven figure plan into publication figures and perform visual QA.
- `nature-reviewer`: isolated editor/reviewer simulation, including under-explanation and decisionability checks.
- `nature-response`: close real editor/reviewer concerns after a decision.
- `nature-citation`: best-evidence citation discovery plus explicit CNS/Nature scopes when requested.
- `nature-academic-search`: broader literature discovery and verification.
- `nature-statistics`: statistical design, reporting, estimands, uncertainty, and figure statistics.
