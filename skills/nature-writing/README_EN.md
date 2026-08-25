# `nature-writing` Skill

[中文说明](README.md)

`nature-writing` drafts, restructures, and plans journal-aware academic manuscripts from author-provided evidence. It is no longer a Nature-style template writer: it resolves the paper's scientific archetype, builds the argument/evidence dependencies, studies broad/close paper corpora when useful, decides what content and figures belong in the paper, checks explanation depth and sentence logic, preserves author voice, and finishes with a hard manuscript-surface leakage/punctuation scrub before applying exact journal rules.

## What To Use It For

- Build titles, abstracts, introductions, related work, Methods, Results, Discussions, Conclusions, or a full manuscript argument.
- Resolve the dominant **paper archetype** — mechanism/discovery, randomized intervention, observational, computational/ML, method/tool/software, resource/dataset, theory/proof, qualitative, review/synthesis, or hybrid — before deciding what evidence and figures the paper needs.
- Reconstruct `question/tension -> contribution -> evidence chain -> boundary -> meaning` before drafting prose.
- Study a broad stratified corpus for tendencies and 3–6 close analogues for deep claim/evidence/explanation/figure reasoning, without copying wording or layouts.
- Check **explanatory sufficiency**: whether a central idea, method, mechanism, result, equation, or implication has enough identity, rationale, logic, evidence, boundary, and connection for the intended reader to understand it without guessing.
- Detect hidden premises and conceptual jumps where a polished short sentence has compressed away an essential reasoning step.
- Decide what belongs in main text, figures, legends, Methods, Extended Data/SI, Data/Code/Resource Availability, repository documentation, or nowhere.
- Detect and remove **repository-to-manuscript leakage** such as file paths, script/notebook/config/output filenames, helper/class/function names, CLI commands, internal modules, developer workflow, and repeated project links when they do not perform a scientific/access function.
- Suggest what figures/plots the paper needs from the claim, reader question, estimand, data structure, uncertainty, alternative explanation, and paper archetype before `nature-figure` renders them.
- Repair paragraphs whose individual sentences are grammatical but disconnected by mapping `inherits -> relation -> adds -> enables` for every sentence.
- Make academic prose more natural without detector gaming: preserve precise technical repetition, use functionally motivated syntax, calibrate stance locally, avoid connector stuffing and generic prestige language, then restore the author's own cadence and agency.
- Allocate Results to the shortest sufficient main-text evidence chain while keeping conclusion-changing negative/failure evidence and boundaries visible.
- Run a final **manuscript-surface QA** over title/abstract/body/legends/table notes/Methods/equations/availability text for artifact leakage, punctuation spacing, bracket balance, malformed figure references, range/minus/hyphen issues, units, and target-aware copy-editing.
- Run editor/reviewer decision preflight and choose the minimum valid repair: explanation/restructuring, evidence, reanalysis, correction, claim narrowing/removal, or target/article-type change.
- Prepare first-submission materials and exact target-journal/article-type/stage checks.

## Workflow

For substantial manuscript work, the writing engine follows roughly:

```text
evidence/claims
-> paper archetype
-> argument spine
-> content triage
-> broad corpus / close analogue calibration when useful
-> author-voice profile
-> evidence + figure/plot planning
-> section move graph
-> paragraph nuclei + satellites
-> sentence dependency / information flow
-> explanatory sufficiency / hidden-premise audit
-> natural scholarly prose
-> editor/reviewer preflight
-> exact journal adaptation
-> final consistency + manuscript-surface leakage/punctuation release gate
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

The research hierarchy is:

```text
author evidence = truth constraint
paper archetype = evidence/reader-dependency prior
journal/reporting rules = compliance constraint
broad corpus = descriptive tendency layer
close analogues = manuscript-specific structural/evidence priors
author voice = expression prior
```

Frequency is never a writing-quality score.

## Studying Many Papers

When dozens or hundreds of extracted `.md`/`.txt` papers are available, the package can combine:

```bash
python scripts/corpus_structure_stats.py CORPUS_DIR --pretty --output corpus-structure.json
python scripts/corpus_figure_inventory.py CORPUS_DIR --json corpus-figures.json --csv corpus-displays.csv
```

The first profiles section/paragraph/sentence surface statistics. The second inventories figures/tables/captions and proposes transparent **candidate** evidence roles such as orientation, mechanism, validation, OOD/generalization, robustness, failure/limitation, heterogeneity, calibration, resource coverage, theory/model and qualitative synthesis.

Those labels are triage heuristics, not semantic truth, acceptance predictors, or instructions to copy frequent plots. Semantic close reading remains mandatory before changing a writing rule.

## Typical Requests

- "Rebuild this Introduction from the actual evidence and research need; don't force a Nature template."
- "First classify what kind of paper this really is, then tell me what evidence sequence and main figures fit that archetype."
- "This explanation is too compressed. Check whether a reader can actually understand the idea and expand only the missing reasoning."
- "Study 50 recent papers for broad tendencies, then deeply read 4–6 true analogues before rewriting our Results."
- "This paragraph sounds AI-written. Repair the sentence-to-sentence logic and make it natural while preserving my voice; don't optimize an AI detector."
- "The source material includes code and repository docs. Keep only scientifically relevant information in the paper and run a final filename/script leakage scrub."
- "Audit our figure captions: remove plotting-pipeline filenames/helper names and fix punctuation without deleting necessary scientific identifiers."
- "Given these claims and data, propose the main figures and specific plot types before we write the Results."
- "Preflight this paper as editor and reviewers and identify the cheapest scientifically valid changes before submission."

## What You Need To Provide

- Core claims/questions, figures, data/results, Methods facts, limitations, and any evidence that must not be altered.
- Representative author prose when preserving a recognizable voice matters.
- Target field, paper type, study design, and exact journal/venue when known.
- Comparable papers if you already have preferred analogues; otherwise the workflow can define the comparator profile.
- Source code/repository/project materials only when relevant to method/resource/reproducibility work; the skill will not automatically turn them into manuscript prose.
- Extracted paper corpora when you want broad empirical calibration.

## Outputs

Depending on the task, outputs can include:

- ready-to-paste manuscript prose after final surface QA;
- dominant/secondary paper-archetype plan;
- argument spine and section move map;
- **explanation ledger**: `concept/inference -> reader baseline -> missing explanation element(s) -> recommended expansion -> destination -> sufficient/under-explained/over-explained`;
- content-allocation ledger: `main / figure / legend / Methods / Extended Data/SI / availability / repository / omit`;
- repository-leakage list with the scientific abstraction or correct destination for each removed artifact detail;
- final manuscript-surface QA findings and resolutions;
- shortest sufficient evidence chain;
- figure/plot suggestion ledger: `claim/question -> statistical unit -> estimand -> plot -> uncertainty/comparator -> main/support`;
- broad-corpus descriptive profile and close-analogue `adopt / adapt / reject / unresolved` decisions;
- compact author-voice profile and re-voice notes;
- sentence/paragraph dependency repairs;
- editor/reviewer blocker map and resolution tests;
- first-submission package and `ready / ready_with_author_checks / blocked` status when requested.

## Method Sources

The writing rules are research-backed rather than based on one prestige-journal style.

- [`docs/academic-writing-research_EN.md`](../../docs/academic-writing-research_EN.md): cross-disciplinary research on rhetorical moves, cohesion, stance, human/LLM academic writing, section structure, and writing process.
- [`docs/deep-paper-calibration_EN.md`](../../docs/deep-paper-calibration_EN.md): paper archetypes, stratified recent-paper reading, broad-corpus/close-analogue calibration, figure inventory, leakage and punctuation QA.
- [`docs/natural-scholarly-writing_EN.md`](../../docs/natural-scholarly-writing_EN.md): practical sentence-to-sentence flow and natural-prose repair.
- [`docs/explanatory-sufficiency_EN.md`](../../docs/explanatory-sufficiency_EN.md): how to detect under-explanation, hidden premises, and when to elaborate versus compress.
- [`docs/manuscript-content-and-figures_EN.md`](../../docs/manuscript-content-and-figures_EN.md): what belongs in a paper, repository-to-manuscript leakage, evidence allocation, and plot/figure planning.
- `../nature-shared/core/paper-archetype-atlas.md`: archetype-specific evidence/writing/figure priors.
- `../nature-shared/research/stratified-paper-reading-2025-2026.md`: recent cross-archetype direct-reading notes.
- `../nature-shared/core/analogue-paper-calibration.md`: focused 3–6-paper near-neighbor study.
- `../nature-shared/core/explanatory-sufficiency.md`: minimum-sufficient explanation and reader-reconstruction contract.
- `../nature-shared/core/natural-scholarly-prose.md`: natural scholarly expression contract.
- `../nature-shared/core/manuscript-content-selection.md`: content admission and destination model.
- `../nature-shared/core/figure-evidence-planning.md`: claim-driven plot/figure planning.
- `../nature-shared/core/manuscript-surface-qa.md`: final artifact-leakage and punctuation/typography release gate.

## Boundaries

- The skill does not invent results, mechanisms, statistical significance, references, uncertainty, limitations, novelty, or rationales not supported by the work.
- It does not equate longer prose with better explanation; routine knowledge and already-sufficient passages remain concise.
- It does not treat `humanizing` as AI-detector evasion, deliberate mistakes, word blacklists, random sentence lengths, or forced informality.
- It does not copy sentences, distinctive paragraph structures, figure layouts, or visual identity from analogue papers.
- It does not treat broad-corpus frequencies or keyword role labels as quality/acceptance scores.
- It does not assume more experiments are always the answer; explanation/restructuring, narrowing/removing a claim, or changing target can be correct.
- It does not put every reproducibility detail in the main narrative: Methods, SI, availability statements, and repositories have different jobs.
- It does not expose internal filenames/scripts/helpers in manuscript-facing prose merely because they appear in project files.
- Exact current target-journal instructions and reporting standards override generic/local formatting and punctuation defaults.
- For final figure rendering/export, use `nature-figure`; for real post-decision rebuttals/revision correspondence, use `nature-response`.

## Related Skills

- `nature-polishing`: polish/restructure existing prose using the same explanation, archetype, surface-QA, natural-prose and author-voice principles.
- `nature-figure`: turn the claim/archetype-driven figure plan into publication figures and perform visual + legend/caption QA.
- `nature-reviewer`: isolated editor/reviewer simulation, including archetype fit, under-explanation, figure adequacy and surface hygiene.
- `nature-response`: close real editor/reviewer concerns after a decision.
- `nature-citation`: best-evidence citation discovery plus explicit CNS/Nature scopes when requested.
- `nature-academic-search`: broader literature discovery and verification.
- `nature-statistics`: statistical design, reporting, estimands, uncertainty, and figure statistics.
