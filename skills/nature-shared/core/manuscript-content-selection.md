# Manuscript content selection and artifact-leakage control

> Shared contract for deciding **what belongs in an academic paper, where it belongs, and what should stay out**. This is a scientific relevance/allocation model, not a universal journal page-budget rule. Exact reporting requirements and journal instructions override local placement defaults.

Last reviewed: 2026-08-22.

## Contents

- [Purpose](#purpose)
- [The problem: implementation-detail leakage](#the-problem-implementation-detail-leakage)
- [The five-function admission test](#the-five-function-admission-test)
- [Destination model](#destination-model)
- [Repository-to-manuscript translation](#repository-to-manuscript-translation)
- [What belongs in main text](#what-belongs-in-main-text)
- [What belongs in figures and tables](#what-belongs-in-figures-and-tables)
- [What belongs in legends](#what-belongs-in-legends)
- [What belongs in Methods](#what-belongs-in-methods)
- [What belongs in Extended Data or Supplementary Information](#what-belongs-in-extended-data-or-supplementary-information)
- [What belongs in Data/Code/Resource Availability](#what-belongs-in-datacoderesource-availability)
- [What belongs only in repository or developer documentation](#what-belongs-only-in-repository-or-developer-documentation)
- [What should usually be omitted entirely](#what-should-usually-be-omitted-entirely)
- [Decision-changing exceptions](#decision-changing-exceptions)
- [Content selection by contribution type](#content-selection-by-contribution-type)
- [The deletion and relocation tests](#the-deletion-and-relocation-tests)
- [Compression without evidence hiding](#compression-without-evidence-hiding)
- [Output contract](#output-contract)
- [Research basis](#research-basis)

## Purpose

A paper is not a compressed repository, lab notebook, project website, or exhaustive record of everything the authors did.

Its main narrative should contain the **minimum sufficient information needed to understand, evaluate, and correctly bound the scientific contribution**, while the complete reproducibility record is distributed across Methods, figures/tables, Extended Data/SI, source data, availability statements, repositories, and reporting checklists.

The core principle is:

> **Evidence completeness is a property of the publication package; narrative completeness is a property of the reader's reasoning path.**

The main text should not become the storage location for every detail merely because the detail exists in the source material.

## The problem: implementation-detail leakage

A common failure in AI-assisted technical writing is **implementation-detail leakage** (also useful to call **repository-to-manuscript leakage**): details from the source code, repository, developer workflow, or file organization are copied into manuscript prose without being translated into their scientific meaning.

Examples:

- local or repository file paths;
- script filenames;
- helper-function/class names;
- branch, PR, issue, commit-development history;
- unit-test names;
- CLI commands and installation steps;
- directory trees;
- internal module architecture;
- configuration plumbing;
- project website/repository links repeated throughout the Results;
- implementation notes that do not affect inference or reproducibility;
- variable names copied from source code when a scientific name exists.

These details can be important **artifacts** but are often poor **manuscript content**.

The failure is broader than verbosity. It is a **relevance and allocation error**: a fact has been placed where it does not perform the reader-facing scientific job of that section.

## The five-function admission test

Before adding any content unit to the manuscript, ask whether it performs at least one of these functions.

### F1 — inference-critical

Does the reader need it to believe, reject, or correctly quantify a scientific claim?

Examples:

- primary comparison/effect;
- decisive control;
- uncertainty interval;
- result that discriminates between plausible explanations;
- conclusion-changing negative evidence.

### F2 — interpretation-critical

Does the reader need it to understand what the result means or where the claim stops?

Examples:

- clinically/physically meaningful scale;
- subgroup/failure boundary that changes generality;
- alternative explanation;
- key assumption;
- limitation that changes interpretation.

### F3 — reproducibility-critical

Does a competent researcher need it to recreate the study/analysis or verify the result?

Examples:

- inclusion/exclusion criteria;
- key preprocessing;
- experimental conditions;
- model/training details;
- software versions when consequential;
- algorithm parameters;
- access to central code/data.

### F4 — compliance/provenance-critical

Is it required for ethics, reporting standards, data/code/material availability, registration, attribution, or auditability?

### F5 — orientation-critical

Does it substantially reduce the cognitive cost of understanding the study design, system, or evidence sequence?

Examples:

- concise system overview;
- cohort flow when selection is complex;
- experimental timeline;
- method schematic;
- definition of an unfamiliar central object.

### Admission outcome

- If **none** of F1–F5 applies: usually omit from the publication package or keep only in project documentation.
- If a function applies: choose the **lowest-friction destination** that satisfies the function without interrupting the main argument.

A fact does not earn main-text space merely because it is true.

## Destination model

Use this default allocation hierarchy.

### Main text

For information necessary to follow and evaluate the **central argument**.

### Main figure/table

For decisive evidence whose structure/pattern/comparison is better inspected visually than described in prose.

### Figure/table legend

For decoding the display: what is shown, units, groups, sample/statistical units, statistical notation, essential display-specific conditions, and exact definitions needed to read it.

### Methods

For reproducibility and interpretation details about what was done, how, and why, especially details that would interrupt the Results narrative.

### Extended Data / Supplementary Information

For important supporting evidence, robustness, secondary analyses, specialist detail, large calculations/data, or background necessary to scrutinize the work but not necessary to follow the central narrative.

### Data / Code / Resource Availability

For the authoritative access location: persistent repository/DOI/accession/link, version/release/commit when required, restrictions, licenses, and how data/code/materials can be accessed.

### Repository / artifact documentation

For installation, file organization, command-line usage, developer APIs, environment setup, scripts, tests, reproduction commands, and extensive artifact instructions.

### Omit

For details that add neither scientific understanding, evaluation, reproducibility, compliance, nor useful orientation.

## Repository-to-manuscript translation

Do not paste repository language into the paper. Translate **implementation artifacts into scientific abstractions**.

| Repository/code artifact | Manuscript translation |
|---|---|
| `scripts/preprocess.py` | Describe the scientifically consequential preprocessing steps in Methods; omit the filename unless artifact navigation specifically requires it. |
| `src/models/calibrator.py::fit()` | Describe the calibration procedure/algorithm, not the function path. |
| YAML/JSON config | Report scientifically consequential parameter values in Methods/SI; keep full config in the repository. |
| internal class/module hierarchy | Usually repository documentation; include an architecture diagram only if software architecture itself is a contribution/evaluation object. |
| CLI invocation | Repository/artifact instructions; manuscript may describe the experimental command conceptually only when needed for reproducibility. |
| unit tests | Repository quality assurance; mention validation only when the validation result itself is scientific evidence or the paper is specifically about software reliability. |
| branch/PR/issue | Developer provenance; normally omit. |
| GitHub project URL | Put in Code/Resource Availability or an artifact appendix, not repeatedly in Results/Introduction. |
| environment setup | Artifact docs; report consequential software/hardware/version information in Methods or artifact appendix. |
| helper variable names | Replace with scientific terminology. |
| generated intermediate files | Omit unless the intermediate object is scientifically meaningful or required for reproducibility. |

### Scientific-abstraction test

For every code-derived detail ask:

> If the implementation were rewritten from scratch but the scientific method and results stayed identical, would this detail still matter to the paper?

- **Yes** -> it may be scientific content.
- **No** -> it is probably artifact/documentation detail.

### Interface-versus-inference distinction

A software paper may legitimately describe an interface, architecture, or workflow when **usability/reusability/system design is part of the contribution**. Even then, distinguish:

- what the interface enables scientifically;
- what architectural decision is being evaluated;
- what is merely documentation needed to operate the software.

## What belongs in main text

The main text should normally contain:

### Introduction

- enough context for the target reader to understand the question;
- the real research need/tension;
- fair positioning of the strongest relevant prior work;
- the paper's bounded contribution/question;
- only technical detail needed to understand why the question matters.

Do not include:

- repository history;
- implementation walkthroughs;
- long tool/version lists;
- exhaustive literature catalogues;
- every failed approach;
- project links unless directly relevant to access/use and the venue expects them there.

### Results / analysis

- question/rationale for the evidence block;
- decisive observation/estimate/comparison;
- primary uncertainty/inference;
- direct local interpretation at the strength the design permits;
- result/qualification that materially changes the headline conclusion;
- enough method context to understand what the result actually represents.

A Nature Computational Science editorial explicitly recommends logical narrative order rather than experiment chronology and says detailed derivations, training strategies, and exhaustive architecture descriptions should be reserved for Methods when they would distract from Results.

Do not include by default:

- filenames/scripts;
- exhaustive hyperparameter descriptions;
- repository navigation instructions;
- every benchmark number in prose when a table/figure already communicates it;
- every robustness check;
- every intermediate diagnostic;
- software setup details;
- long methodological derivations unless the method itself is the result being established.

### Discussion

- durable finding after qualification;
- interpretation and plausible alternatives;
- relation to prior evidence/theory;
- limitations that bound the claim;
- specific scientific/clinical/technical implications;
- unresolved questions/future work only when they follow from the current result.

Do not use Discussion as a storage area for new data or implementation notes.

## What belongs in figures and tables

A main display item should **earn its place** by doing scientific work that prose cannot perform as efficiently.

Use a main figure/table when it:

- makes a central pattern/comparison inspectable;
- exposes distribution/heterogeneity/pairing/uncertainty relevant to the claim;
- shows a mechanism/sequence/system needed to understand the evidence;
- compares methods/conditions on common axes;
- shows generalization or failure boundaries central to the claim;
- compresses high-dimensional evidence without hiding the estimand;
- provides a decisive visual test of an alternative explanation.

Nature Portfolio explicitly advises authors to make each figure earn its place and support the paper's main message. Nature Metabolism similarly advises highlighting crucial data in main figures and moving tangential data to Extended Data/SI or leaving it out.

Do not create a figure when:

- two numbers can be stated more clearly in one sentence;
- the panel repeats another panel's inference;
- it exists mainly because the analysis software generated it;
- it is decorative rather than evidentiary/orienting;
- the key scientific question cannot be identified.

## What belongs in legends

Legends decode displays; they are not miniature Results/Methods/Discussion sections.

Include as needed:

- what each panel shows;
- groups/conditions;
- sample/statistical unit and `n` definition;
- axes/units;
- error/interval meaning;
- statistical test/annotation definitions when required;
- scale bars/imaging conventions;
- concise panel-specific experimental context.

Avoid:

- repeating the Results paragraph;
- extended interpretation;
- full protocol;
- general paper background;
- implementation setup unrelated to reading the figure.

Exact target rules may require more specific legend content.

## What belongs in Methods

Methods should contain all elements necessary for interpretation and replication, without using the Results narrative as a second Methods section.

Common Methods content:

- study design and rationale where method choice affects inference;
- data/material/source provenance;
- inclusion/exclusion/sampling;
- experimental procedure;
- measurement definitions;
- preprocessing;
- model/algorithm details;
- training/fitting/inference procedures;
- controls;
- statistics/uncertainty/multiplicity;
- sensitivity definitions;
- software/hardware details when consequential;
- ethics/registration;
- reproducibility information.

Nature's current formatting guidance says Methods should contain the elements necessary for interpretation and replication and discourages detailed repetition of already-published methods. Nature Climate Change describes a useful reader standard: a field-competent reader should be able to reproduce the results.

For computational papers, detailed mathematical derivations, training strategies, and exhaustive model construction often belong here rather than Results unless those details are themselves the central contribution/evidence.

## What belongs in Extended Data or Supplementary Information

Use support material for **important but non-narrative-critical** content.

Candidates:

- secondary controls;
- robustness/sensitivity analyses;
- alternative estimators/specifications;
- extra baselines;
- parameter/hyperparameter sweeps;
- extended diagnostics;
- large tables/raw data;
- full derivations/calculations;
- additional examples/cases;
- non-central edge cases;
- supplementary methods/notes;
- specialist material needed for deep scrutiny rather than first-pass understanding.

### Do not bury decision-changing evidence

A negative result, subgroup, failure mode, or limitation stays in the main text if it changes the direction, magnitude, scope, credibility, causal interpretation, clinical meaning, or generalizability of the headline claim.

Nature distinguishes Extended Data as peer-reviewed display material integral/essential to the paper but outside the limited main display set, while SI is material directly relevant/essential background that is too large, impractical, or specialized for the main paper.

## What belongs in Data/Code/Resource Availability

Use availability sections as the **one-stop shop** for artifact access.

Include as required:

- persistent repository/DOI/accession;
- code/data/resource release location;
- version/release/commit/tag when useful or required;
- license;
- access restrictions and reason;
- controlled-access procedure;
- identifier for archived artifact;
- linkage to source data or protocols.

Nature Portfolio requires dedicated Code Availability statements for central custom code/algorithms and encourages durable access that enables readers to repeat published results. A Nature Climate Change editorial explicitly describes Data and Code Availability statements as one-stop access points.

Therefore, avoid scattering raw repository URLs throughout Introduction/Results unless the target format or scientific argument specifically calls for them.

## What belongs only in repository or developer documentation

Usually keep these out of manuscript prose:

- installation commands;
- dependency installation instructions;
- directory/file trees;
- API docs;
- internal class/function names;
- CLI flags;
- developer architecture unrelated to the scientific claim;
- unit-test instructions;
- CI configuration;
- branch/PR/issue references;
- debugging notes;
- release workflow;
- exact local paths;
- environment bootstrap scripts;
- exhaustive examples of software use.

For venues with formal artifact-evaluation appendices, put reproducibility-operation details in the artifact package/appendix according to that venue rather than forcing them into the scientific Results narrative.

## What should usually be omitted entirely

Omit content when it has no F1–F5 function and does not belong in artifact docs.

Examples:

- analysis performed but irrelevant to any retained claim;
- redundant descriptions of a figure/table;
- repeated significance statements without new evidence or interpretation;
- tangential exploratory observations that do not define a useful boundary;
- generic literature facts that do not contribute to the research need;
- every design alternative considered during development;
- failed implementation attempts with no scientific consequence;
- internal administrative/project information;
- boilerplate code descriptions that readers cannot use to evaluate the science.

`We did it` is not sufficient reason to publish it.

## Decision-changing exceptions

Do not relocate/omit content merely for concision when it changes:

- primary outcome definition;
- causal interpretation;
- magnitude/direction of the effect;
- stated population/regime/generalizability;
- central mechanism;
- validity of the statistical model;
- key selection/exclusion logic;
- reproducibility of a central method;
- research-integrity/ethics assessment;
- the reader's ability to see adverse/contradictory evidence.

These remain visible in the appropriate high-salience location.

## Content selection by contribution type

### Experimental discovery / mechanism

Main narrative usually needs:

- phenomenon/main effect;
- decisive control;
- mechanistic perturbation/evidence if mechanism is claimed;
- rescue/orthogonal validation when required by the claim;
- boundary/generalization central to the conclusion.

Supporting detail:

- repeated controls;
- protocol variants;
- secondary readouts;
- large robustness sets.

### Clinical / epidemiological / observational

Main narrative usually needs:

- population/design orientation;
- primary outcome/effect estimate;
- uncertainty;
- confounding/identification logic needed for interpretation;
- clinically meaningful absolute quantities when relevant;
- central heterogeneity/safety/limitations.

Support:

- secondary endpoints;
- alternate models;
- extensive subgroup/sensitivity tables unless decision-changing.

### Computational / machine learning

Main narrative usually needs:

- problem/task and data regime;
- fair comparator/baseline framing;
- primary benchmark evidence;
- uncertainty across runs/tasks/sites when it affects interpretation;
- ablation/mechanistic evidence **only if it supports a claimed cause/component role**;
- external/OOD/generalization evidence when claimed;
- failure cases/efficiency trade-off when central.

Methods/SI/repository usually hold:

- exhaustive architecture description;
- training details/hyperparameter grids;
- implementation plumbing;
- scripts/configs;
- full benchmark tables;
- reproduction commands;
- package setup.

### Method / instrument / tool

Main narrative commonly needs:

- method concept/orientation;
- validation of accuracy/precision/sensitivity/specificity/dynamic range as relevant;
- reproducibility/robustness;
- fair comparison to existing methods;
- general applicability;
- one or more demonstrations that the method enables useful new inference if this is part of the claim.

Nature Methods explicitly expects strong validation data for performance, reproducibility, general applicability, and potential for discovering new biology for its Article format.

### Dataset / resource / benchmark

Main narrative commonly needs:

- resource composition/coverage;
- provenance/quality controls;
- known biases/limitations;
- what is newly possible;
- representative utility/benchmark evidence;
- durable access statement.

Repository docs should hold extensive user instructions.

### Theory / mathematical

Main narrative commonly needs:

- problem and assumptions;
- theorem/result statement;
- proof idea or key reasoning sufficient to understand significance;
- consequence/counterexample/regime boundary;
- empirical/numerical illustration only when it clarifies or validates a claim.

Long derivations/proofs may be placed according to venue norms without hiding assumptions critical to interpreting the result.

### Qualitative / interpretive / humanities

Main narrative needs the analytic/source evidence necessary to support the interpretation, including counterevidence/negative cases where they bound the claim. Do not force quantitative plots or an experimental evidence ladder onto these genres.

## The deletion and relocation tests

### Deletion test

Ask:

> If this content disappeared from the **main narrative**, would a competent target reader still understand and adequately evaluate the central claim?

- **No** -> keep/main or main display.
- **Yes, but reproduction/audit suffers** -> move Methods/availability/artifact/SI.
- **Yes, but deeper scrutiny loses a useful check** -> Extended Data/SI.
- **Yes, and no other publication function suffers** -> omit.

### Relocation test

Ask:

> Is the information important, but its current location interrupts the reader's scientific reasoning?

Common relocations:

- Result -> Methods: technical procedure/derivation.
- Result -> SI: non-central robustness/detail.
- Introduction -> Code Availability: repository/access link.
- Main text -> legend: display decoding.
- Legend -> Methods: protocol detail.
- Paper -> repository README: installation/usage/dev instructions.

### One-sentence replacement test

If a multi-sentence block only communicates a simple fact that the reader needs for interpretation, compress it to the minimum statement and move operational detail to the correct support location.

## Compression without evidence hiding

A concise high-impact paper should not become a selective paper.

The aim is:

`shortest sufficient evidence chain + visible decision-changing boundaries + complete support package`

Never use the main/SI boundary to hide:

- contradictory evidence;
- adverse outcomes;
- failed external validation;
- important subgroup reversal;
- uncertainty that weakens the headline interpretation;
- exclusions that materially affect conclusions;
- limitations that change generalizability.

## Output contract

For substantial manuscript planning/rewrite, produce or maintain a compact content-allocation ledger:

```text
Content item
Scientific function: F1/F2/F3/F4/F5/none
Claim dependency
Decision-changing? yes/no
Best destination: main text / main figure / legend / Methods / Extended Data / SI / availability / repository / omit
Reason
If moved, replacement pointer in main text
```

Also flag **repository leakage** explicitly:

```text
Repository leakage
- item
- why it is implementation/documentation rather than scientific narrative
- correct scientific abstraction or destination
```

## Research basis

Current editorial/writing guidance supporting this contract includes:

- Nature Portfolio, *How to write your paper*: focused/concise message; make each figure earn its place; use supplementary material for technical information supporting conclusions but not crucial to the narrative.
- Nature, *Formatting guide*, *Initial submission*, *Supplementary information*, and *Composition of a Nature research paper*: separate main paper, Methods, Extended Data, SI, and Data/Code Availability functions.
- Nature Computational Science (2025), *On writing accessible computational science papers*: Results should follow logical narrative rather than lab chronology; only important results in main text; detailed derivations/training/model construction belong in Methods when they distract from the Results narrative.
- Nature Methods (2017), *So you're writing a paper*: results and figures are the core; give enough method context for understanding, put details in Methods, make every word perform useful work, and avoid gratuitous information.
- Nature Metabolism (2024), *How to let your data shine*: crucial data belong in well-organized main figures; tangential data can move to Extended Data/SI or be omitted.
- Nature Climate Change (2025), *Making the most of the Methods*: Methods should support reproduction; brief method rationale may be repeated in main text for comprehension; Data/Code Availability statements serve as one-stop access points.
- ACM artifact-evaluation practice: installation, dependencies, hardware/software environment, scripts, and reproduction procedures are artifact documentation functions rather than necessarily main scientific narrative.

These sources are evidence about good allocation principles and specific venue structures. Always verify the exact target's current rules before submission.
