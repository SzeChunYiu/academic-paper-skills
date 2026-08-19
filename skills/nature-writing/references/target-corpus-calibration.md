# Target-corpus calibration

Use this protocol when the user asks to write for a named journal/venue, emulate current papers in a field, diagnose why a draft does not feel like the target literature, or build/update a local writing profile.

This is a **rhetorical learning** workflow, not a sentence-copying workflow.

## Contents

- [When to calibrate](#when-to-calibrate)
- [Corpus design](#corpus-design)
- [Two-pass corpus analysis](#two-pass-corpus-analysis)
- [Annotation schema](#annotation-schema)
- [Analysis procedure](#analysis-procedure)
- [Profile output](#profile-output)
- [How to use the profile](#how-to-use-the-profile)
- [Anti-copying and overfitting rules](#anti-copying-and-overfitting-rules)
- [Update protocol](#update-protocol)

## When to calibrate

Calibrate when:

- the target journal or venue is explicit and writing style/structure matters;
- the field has a publication ecology not well represented by the static references;
- the article type is unusual (registered report, resource, benchmark, brief report, perspective, qualitative study, theorem paper, etc.);
- the user asks for current target-journal patterns;
- local guidance conflicts with recent published practice;
- a draft is scientifically correct but rhetorically unlike comparable papers.

Do not calibrate merely to make a paper sound more prestigious.

## Corpus design

### Minimum useful sample

For a quick working profile, inspect **8–15 comparable recent papers** when available.

For a maintained repository profile, aim for **30–100 papers** and stratify them before generalizing.

For a research-grade corpus study, use a larger reproducible sample and document selection/exclusion in enough detail to repeat it.

### Match on the dimensions that matter

Prefer papers matching, in order:

1. exact journal/venue;
2. exact article/content type;
3. recent publication period;
4. research paradigm/study design;
5. discipline/subfield;
6. contribution type;
7. comparable evidence structure.

A 2026 clinical cohort article and a 2026 methods resource in the same journal may be poorer rhetorical comparators than two cohort articles in adjacent journals.

### Include counterexamples

Do not select only papers that fit the first pattern noticed. Retain legitimate structural outliers and ask what feature of the study explains the difference.

## Two-pass corpus analysis

Large corpora and close reading answer different questions. Use both without confusing them.

### Pass A — scalable descriptive profiling

When dozens or hundreds of papers have been extracted to `.md`, `.markdown`, or `.txt`, run:

```bash
python scripts/corpus_structure_stats.py CORPUS_DIR --pretty --output corpus-structure.json
```

Use this pass for cheap descriptive signals such as:

- section/heading presence and order;
- paragraph and sentence length distributions;
- figure/table call density;
- selected contrast/consequence/example markers;
- selected hedge/booster/self-reference/contribution signals.

These measurements help identify strata and candidate differences worth reading closely. They are **not writing-quality scores**, do not identify rhetorical moves reliably, and must not be used to conclude that a frequent connective, sentence length, or assertive verb is better writing.

### Pass B — semantic rhetorical reading

Read complete papers or complete rhetorical units to recover what the surface statistics cannot:

- why the paper creates a particular research need;
- why evidence block B follows A;
- what a paragraph's nucleus is;
- which sentences are evidence versus interpretation;
- how alternatives/counterevidence are handled;
- whether a strong verb is actually warranted;
- why a structural outlier makes sense for its study design.

When resources are limited, prioritize semantic reading over collecting more superficial counts. A smaller well-stratified corpus with careful move/evidence annotation is more useful than a huge unstratified frequency table.

## Annotation schema

For each paper, record at least:

### Paper-level

- journal/venue, year, article type;
- discipline/subfield;
- research paradigm / study design;
- contribution type;
- section/headings structure;
- central question/tension;
- central answer/contribution;
- evidence sequence;
- stated boundaries/limitations.

### Section-level

For each major section:

- reader question;
- rhetorical moves and order;
- recurrent moves;
- section opening strategy;
- section closing/handoff strategy;
- location of interpretation and limitations.

### Paragraph-level

For a representative sample of paragraphs:

- paragraph nucleus;
- supporting submoves: evidence, explanation, comparison, qualification, counterargument, implication, bridge;
- topic-sentence strategy;
- figure/table/source integration;
- whether the paragraph leads with question, method, observation, claim, or context.

### Sentence-level

Sample sentences by rhetorical function rather than at random. Record:

- sentence function/move;
- given-new progression;
- active/passive choice and agent visibility;
- tense/aspect;
- hedge/booster strength;
- information density / phrasal versus clausal realization;
- connective or lexical cohesion strategy;
- citation placement.

Do **not** retain reusable full-sentence templates from copyrighted papers. Abstract the pattern.

## Analysis procedure

### 1. Separate invariant from variable

Classify each observed pattern as:

- **argument/evidence invariant** — supported by logic/reporting needs across fields;
- **discipline tendency** — common in this research community;
- **journal/content-type tendency** — local rhetorical convention;
- **house/submission rule** — verify against current official instructions;
- **author-level variation** — do not generalize.

### 2. Count, but do not worship frequency

Useful descriptive measures include:

- section presence/order;
- paragraph counts and median paragraph length by section;
- move prevalence and recurrence after semantic annotation;
- result/figure call placement;
- contribution statement location;
- limitation location;
- title forms;
- abstract move coverage/order;
- first-person/passive tendency;
- selected transition/stance markers.

A frequent pattern is a prior, not a command. Ask what communicative problem it solves.

### 3. Trace whole-paper logic

For every paper, reduce the manuscript to:

`question/tension -> response -> evidence progression -> interpretation -> boundary -> meaning`

Then compare **why** papers with similar questions choose different structures.

### 4. Study transitions between analyses

The most reusable writing insight is often not a phrase but the logic connecting evidence blocks:

- result exposes a mechanism question;
- baseline failure motivates an ablation;
- discovery motivates external validation;
- inconsistency motivates subgroup analysis;
- theorem creates a corollary/application;
- qualitative theme creates a contrast or negative case;
- limitation motivates a sensitivity analysis.

Record these `evidence block A -> reason for block B` links.

### 5. Study claim calibration

Compare each strong claim with the evidence immediately supporting it. Record:

- claim type;
- evidence type;
- uncertainty/boundary;
- hedge/booster;
- whether causality is warranted;
- how counterevidence is handled.

This is more useful than counting words such as `clearly` or `significantly` in isolation.

### 6. Analyze outliers before deleting them

When a paper violates the dominant pattern, ask whether the difference is explained by article type, study design, evidence architecture, audience, or journal mechanics. Legitimate outliers are often what prevent a local convention from being promoted into a bad universal rule.

## Profile output

Produce a temporary profile with these sections:

### A. Corpus

- target and article type;
- date window;
- number of papers;
- inclusion logic;
- important coverage gaps.

### B. Whole-paper architecture

- common argument spines;
- common evidence sequences;
- legitimate alternative architectures.

### C. Section move maps

For each section, list:

- core moves;
- optional/recurrent moves;
- common ordering;
- meaningful variants.

### D. Paragraph logic

- typical paragraph nuclei;
- common satellite combinations;
- how evidence and interpretation are linked.

### E. Sentence realization

- stance;
- voice;
- tense;
- information density;
- transition strategy;
- citation integration.

### F. Transferable rules

Only rules that appear robust across the sampled papers and make rhetorical sense.

### G. Local tendencies

Patterns that should be used as defaults only for this target/article type.

### H. Unresolved variation

Conflicting patterns that should not be turned into a rule.

### I. Counterexamples

Record papers that legitimately violate a common pattern and the study/article feature that explains why. This is the guard against overfitting.

## How to use the profile

Apply profile information in this priority order:

1. scientific accuracy and evidence boundaries;
2. reporting/reproducibility requirements;
3. rhetorical logic from `static/core/rhetorical-engine.md`;
4. discipline/paper-type conventions;
5. temporary target-corpus profile;
6. exact journal house/submission rules.

If the corpus style conflicts with a current official requirement, the official requirement wins for submission mechanics. If it conflicts with evidence integrity, evidence integrity wins.

## Anti-copying and overfitting rules

Never:

- copy distinctive sentences or phrases from a paper into the user's manuscript;
- build a phrase bank from copyrighted prose;
- infer effectiveness from prestige or citation count;
- generalize a pattern from fewer than several independent papers without labeling it tentative;
- mix article types and report the average as one journal style;
- treat a corpus frequency as an exact submission rule;
- turn a descriptive surface statistic into a writing-quality score;
- suppress limitations or inflate novelty because target papers use assertive language.

Learn **moves, relations, sequencing, information structure, and claim calibration**, not wording.

## Update protocol

For maintained profiles:

- record sampling date and paper identifiers;
- retain corpus-selection criteria and extraction provenance;
- add new papers incrementally rather than replacing the corpus silently;
- compare old/new distributions before changing a rule;
- keep previous profile versions when the journal changes practice;
- preserve counterexamples instead of averaging them away;
- promote a local rule into the cross-disciplinary core only after validation outside the source corpus;
- add a regression test whenever the profile changes routing or a hard drafting contract.

The existing `nat-comms-2025-corpus.md` is an example of a local empirical profile. Treat it as one stratum, not as the universal source of academic-writing logic.