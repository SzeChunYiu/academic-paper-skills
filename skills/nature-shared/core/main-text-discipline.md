# Main-Text Discipline for Scientific Papers

Use this shared contract when drafting, restructuring, compressing, or revising the main text of a scientific manuscript, especially Results. It operationalizes content selection and evidence allocation; it is not a journal policy. Current journal instructions and field-specific reporting standards override it when they require information in the main text.

For broader source-material triage — especially code/repository details, project links, implementation documentation, Methods/SI/availability placement, or deciding what should be omitted entirely — load `manuscript-content-selection.md` first. For deciding what visual evidence/plots are needed, load `figure-evidence-planning.md`.

## Contents

- [1. Separate evidence completeness from main-text completeness](#1-separate-evidence-completeness-from-main-text-completeness)
- [2. Run the content admission gate](#2-run-the-content-admission-gate)
- [3. Classify every result before placement](#3-classify-every-result-before-placement)
- [4. Build the shortest sufficient evidence chain](#4-build-the-shortest-sufficient-evidence-chain)
- [5. Prevent implementation-detail leakage](#5-prevent-implementation-detail-leakage)
- [6. Prevent revision accretion](#6-prevent-revision-accretion)
- [7. Separate main text, figures, captions, Methods, SI and availability](#7-separate-main-text-figures-captions-methods-si-and-availability)
- [8. Apply statistical reporting discipline](#8-apply-statistical-reporting-discipline)
- [9. Run the paragraph necessity test](#9-run-the-paragraph-necessity-test)
- [10. Stop explanatory recursion](#10-stop-explanatory-recursion)
- [11. Audit claim repetition](#11-audit-claim-repetition)
- [12. Return an auditable compression record](#12-return-an-auditable-compression-record)
- [Non-negotiable exceptions](#non-negotiable-exceptions)

## 1. Separate evidence completeness from main-text completeness

Preserve the complete evidential record across the manuscript, figures, tables, Methods, source data, Extended Data/Supplementary Information (SI), availability statements, repositories, and reporting checklists. Do not force that full record into the main text.

Reserve main-text space for information that establishes, advances, explains, or materially bounds the central scientific argument.

The main text is **not** required to contain every detail needed to operate the codebase or reproduce every analysis command. Reproducibility completeness can be achieved through the full publication/artifact package.

Do not use compression to hide inconvenient evidence. If an observation changes the direction, magnitude, scope, causal interpretation, generalizability, or credibility of the central conclusion, keep it visible in the main text even if it is nominally a robustness, subgroup, or negative analysis.

## 2. Run the content admission gate

For every candidate sentence/detail/panel, classify its scientific function using `manuscript-content-selection.md`:

- **F1 inference-critical** — necessary to believe/evaluate a claim;
- **F2 interpretation-critical** — necessary to understand meaning/boundary;
- **F3 reproducibility-critical** — necessary to reproduce/verify;
- **F4 compliance/provenance-critical** — ethics/reporting/access/audit;
- **F5 orientation-critical** — materially reduces cognitive cost of understanding design/system.

A detail with **no F1–F5 function** should usually be omitted from the publication package or kept only in project documentation.

A detail with a function does **not** automatically belong in main text. Choose the lowest-friction correct destination.

### Main-text admission test

Ask:

> If the reader does not see this during the first-pass narrative, will they misunderstand, mis-evaluate, or overgeneralize the central claim?

- **Yes** -> main text/main display likely.
- **No, but reproduction requires it** -> Methods/availability/artifact.
- **No, but deep scrutiny benefits** -> Extended Data/SI.
- **No scientific/publication function** -> omit.

## 3. Classify every result before placement

Build a result-allocation table before drafting or restructuring Results:

| Class | Decision test | Default destination |
|---|---|---|
| `core_discovery` | Does it advance the paper's central conclusion? | Main text, with adequate evidence |
| `necessary_support` | Must the reader see it to accept the core discovery? | Main text briefly |
| `qualification` | Does it materially bound or alter the central interpretation? | Main text if yes; otherwise support |
| `robustness` | Does it show the result survives an alternative specification, estimator, seed, threshold, or inference procedure without changing the conclusion? | Extended Data/SI, with a concise pointer when useful |
| `heterogeneity` | Is variation across groups/settings/tasks/models itself part of the central claim? | Main text if central; otherwise support |
| `provenance_detail` | Does it document traceability, preprocessing, implementation, or audit detail without advancing the conclusion? | Methods, Source Data, availability, repository, or SI |
| `alternative_inference` | Does it test the same claim using a secondary inferential route? | Support unless it changes acceptance of the claim |
| `edge_case` | Does it define a failure boundary that changes how the claim must be read? | Main text if interpretation changes; otherwise support |
| `artifact_operation` | Does it explain how to run/install/navigate the code/resource rather than evaluate the science? | Repository/artifact appendix, usually not manuscript narrative |

Classify by function in **this paper**, not by analysis name. An ablation can be a core result if component dependence is a central contribution; a subgroup can be headline evidence; a code-access link can be mandatory yet still belong in Code Availability rather than Results.

## 4. Build the shortest sufficient evidence chain

After classification, write the minimum ordered chain that lets the reader:

1. understand the central observation/question;
2. see the decisive comparison/control/mechanistic evidence;
3. judge primary uncertainty/inference;
4. inspect central generalization/validation when claimed;
5. understand any boundary that changes the conclusion.

Do not reproduce the chronological record of experiments or analyses.

A useful Results dependency sequence is:

`question -> decisive evidence -> bounded local inference -> remaining uncertainty -> next evidence`

Route repeated support checks to Extended Data/SI with stable pointers. Draft final prose only after the analysis/result-allocation table is stable.

### Figure-chain test

For each headline claim ask whether prose alone is sufficient. If the reader needs to inspect distribution, pairing, heterogeneity, relationship, uncertainty, mechanism, generalization, or high-dimensional structure, build a claim-driven figure using `figure-evidence-planning.md`.

Do not add a plot simply because the analysis produced one.

## 5. Prevent implementation-detail leakage

Do not let source-code or repository structure dictate manuscript content.

Flag as potential **repository-to-manuscript leakage**:

- file/directory paths;
- script/helper/function/class names;
- setup/install commands;
- CLI flags;
- branch/PR/issue/CI details;
- config plumbing;
- internal module architecture;
- repeated GitHub/project links;
- developer workflow;
- unit-test names;
- variable names that have a scientific equivalent.

Translate implementation artifacts into scientific abstractions:

- script -> scientifically consequential method;
- config -> consequential parameter values;
- code function -> algorithm/analysis operation;
- repository URL -> Code/Resource Availability;
- environment/bootstrap -> artifact README plus essential version/hardware notes in Methods when needed.

Use the test:

> If the implementation were rewritten but the scientific method and results stayed identical, would this detail still matter?

If not, it probably should not be in narrative prose.

Exception: software architecture/interface can be manuscript content when it is itself the scientific/engineering contribution being evaluated.

## 6. Prevent revision accretion

Every requested addition triggers a deletion/relocation check across the affected paragraph/section:

1. State what new scientific function the proposed sentence serves.
2. Find existing sentences/panels that already serve that function.
3. Prefer replacement, combination, compression, or relocation before appending.
4. Re-read the paragraph after the edit and delete any unit made redundant.
5. Re-run content admission, paragraph necessity, and claim-repetition audits.

For reviewer-driven edits, ask:

> Does this addition change what the reader needs to know about the science, or mainly document that the authors answered a reviewer?

Keep decision-relevant science visible. Put exhaustive rebuttal logic in the response letter; put deep support in SI/Methods when appropriate.

## 7. Separate main text, figures, captions, Methods, SI and availability

### Main text

What was found, why the evidence matters, the decisive support/comparison, and conclusion-changing boundaries.

### Main figure/table

Evidence whose pattern/comparison/relationship/distribution/heterogeneity is better inspected visually. Every display must have a scientific reader question.

### Figure/table legend

What is shown and how to decode it: groups, units, sample/statistical units, error/interval meaning, tests/annotations, scale bars, panel conditions. Avoid turning legends into long Methods or Discussion sections unless the exact target requires details there.

### Methods

What was done/how/why at the level required for interpretation and replication. Detailed derivations, training strategies, exhaustive architecture/construction, preprocessing, statistics, and implementation choices generally live here when they would distract from Results.

### Extended Data / SI

Why the conclusion survives deeper scrutiny: secondary controls, robustness, sensitivity, extra baselines, extended diagnostics, parameter sweeps, specialist details, large calculations/data, non-central edge cases.

### Data/Code/Resource Availability

Authoritative access location for data/code/materials/resources, persistent repository/DOI/accession, version/release/commit when needed, license, and restrictions.

Treat it as the **one-stop shop** for access rather than scattering project links throughout the narrative.

### Repository / artifact appendix

Installation, dependencies, reproduction commands, file organization, APIs, developer instructions, scripts and runtime requirements.

Do not repeat a full set of effect sizes, confidence intervals, and P values in main prose + caption + table. Choose authoritative locations and use cross-references efficiently while preserving journal-required content.

## 8. Apply statistical reporting discipline

Compute and retain every analysis required by the design, protocol, reporting standard, and integrity audit. In the main text, normally report:

- the descriptive quantity needed to understand the effect;
- the primary effect/estimand;
- primary uncertainty/inferential evidence needed to support the claim.

Route secondary intervals, alternative estimators/inference procedures, multiplicity checks, sensitivity analyses, and model-level heterogeneity to support material unless they change the conclusion or are required in main text.

Never select only the most favorable statistic.

### Data-display discipline

When small-sample continuous data, pairing, outliers, heterogeneity, or distribution shape matter, prefer displays that expose them rather than bars of means alone. The figure should visually represent the actual design/statistical unit.

## 9. Run the paragraph necessity test

For every Results paragraph, ask:

> If this paragraph were removed, would the reader still understand and have adequate evidence for the paper's central claim?

- **No:** keep it.
- **Yes, but the detail is needed for reproduction:** Methods/artifact/availability.
- **Yes, but a reviewer may want deep support:** Extended Data/SI/response letter.
- **Yes, and the point appears elsewhere:** delete/compress.

When only one sentence is necessary, keep that sentence and relocate the rest.

## 10. Stop explanatory recursion

Do not explain an explanation indefinitely in the main text.

If a statistical/graphical/implementation detail needs several sentences to reconcile it with the main result, state:

1. the scientifically necessary result;
2. any conclusion-changing boundary;
3. a concise pointer to the deeper support.

Keep the full reconciliation in main text only when resolving that discrepancy is itself part of the discovery.

## 11. Audit claim repetition

A major claim may be introduced, demonstrated, interpreted and synthesized, but each appearance must perform a different function.

Build a claim-location map across:

- title/abstract;
- heading/transition;
- figure/table;
- legend;
- Results;
- Discussion;
- conclusion;
- supplementary/support material.

Mark each occurrence `introduce`, `demonstrate`, `decode`, `interpret`, `qualify`, `synthesize`, `shorten`, or `delete`.

Delete restatements that add no new evidence, boundary, interpretation, or reader function.

## 12. Return an auditable compression record

For substantial Results/full-manuscript restructuring, return or maintain:

1. **Content-allocation ledger:** item, F1–F5 function, claim dependency, decision-changing status, destination, reason.
2. **Result-allocation table:** result, class, effect on central interpretation, destination, support pointer.
3. **Shortest evidence chain:** ordered main-text claims and decisive evidence.
4. **Figure/plot suggestion ledger:** claim/question, data unit, estimand, proposed visual, uncertainty/comparator, main/support placement when enough data context exists.
5. **Repository-leakage list:** code/project details removed or translated, with correct abstraction/destination.
6. **Deletion/relocation log:** appended, replaced, compressed, moved or deleted material.
7. **Statistics-location record:** primary main report and secondary support analyses.
8. **Claim-repetition map.**
9. **Word-count delta** for revised main-text subsections when useful.

The prose/figure plan remains the deliverable. Keep audit tables compact unless the user requests detail.

## Non-negotiable exceptions

- Do not move information required for reproducibility, research integrity, participant safety, ethics, or mandatory reporting merely to save words.
- Do not bury contradictory or conclusion-changing evidence in SI.
- Do not strip a qualification that prevents a misleading causal, clinical, societal, mechanistic, or generalization claim.
- Do not remove statistics required by the target journal, study design, or field standard.
- Do not remove central code/data access information; put it in the correct availability/artifact location.
- When the user/editor explicitly requires a point in main text, comply but still replace/compress neighboring redundancy where possible.
