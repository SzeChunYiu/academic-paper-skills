# Manuscript section craftsmanship contract

> Shared section-by-section writing contract for research manuscripts. It complements whole-paper narrative architecture, venue budgeting, standalone-reader independence, formal-spine preservation, statistics, figures, citation integrity, and surface QA.
>
> The purpose is not to force IMRaD or one disciplinary template. The purpose is to make every manuscript surface perform the right **reader-facing scientific job** for the paper archetype and exact venue.

## Core principle

A paper is not excellent because all conventional headings are present.

Every section is an interface:

```text
reader enters with state X
-> asks question Q
-> receives object/evidence/interpretation Y
-> leaves able to understand or evaluate Z
```

If a section cannot name that transition, its content or placement is suspect.

## 1. Resolve section architecture before prose

Before substantial drafting, record:

```text
target venue + article type
paper archetype
binding word/page/display constraints
intended reader baseline
required sections / prohibited sections / flexible sections
whole-paper argument graph
section-function map
reader-state activation map
formal-spine inventory, when active
headline claim/evidence map
```

Then decide which sections the paper actually needs.

Do not add a `Related Work`, `Problem Formulation`, `Limitations`, or `Conclusion` heading merely because a generic template has one.

Do not omit a scientific function merely because the target does not require a heading for it.

## 2. Title

### Reader job

Let a searcher identify the scientific object/question and the main contribution or finding with minimal decoding.

### Usually include

- central scientific object, relation, method, or phenomenon;
- contribution-defining modifier only when actually supported;
- searchable field terms;
- design label when required for identification, such as `randomized trial`.

### Avoid

- project/repository names unless the public system/resource itself is the contribution;
- internal version/experiment IDs;
- unsupported modifiers such as `universal`, `optimal`, `exact`, `causal`, `autoregressive`, or `robust`;
- long compound-noun stacks;
- unfamiliar acronyms unless field-standard;
- decorative puns or questions when they obscure the result or target convention disfavors them.

### Exit test

A qualified reader who sees only the title should not form a materially false expectation of the paper.

Use target-specific title word/character limits from `venue-constrained-manuscript-budget.md`.

## 3. Abstract

Use `abstract-information-budget.md`.

The abstract is a standalone entry point, not a compressed result ledger.

### Exit test

A clean reader can state:

```text
problem -> what was done/established -> headline result -> meaning -> important boundary
```

without decoding internal IDs or juggling nonessential numerical batteries.

## 4. Keywords / indexing terms

### Reader/search job

Make the paper retrievable by the concepts a real scholar would search for.

### Prefer

- canonical field terminology;
- central method/object/domain terms;
- standard synonyms not already obvious from the title when the venue permits them.

### Avoid

- private project labels;
- every coined term in the paper;
- generic words such as `study`, `analysis`, or `model` without domain meaning;
- keyword stuffing.

Keywords are metadata, not a second abstract.

## 5. Introduction

### Reader job

Move the reader from the relevant field state to the exact unanswered question and make the present paper's scientific response intelligible.

A useful dependency pattern is:

```text
relevant context
-> concrete unresolved problem/gap/tension
-> why the gap matters for inference/theory/practice
-> what this paper asks/does
-> bounded contribution / headline answer preview
```

This resembles move-based models such as CARS, but do not force the same move count or phraseology across disciplines.

### Include only background that performs work

Background earns space when it:

- defines a prerequisite concept;
- establishes the problem's importance;
- shows why existing approaches do not resolve the exact question;
- motivates a design choice or comparator;
- establishes the scientific boundary of the contribution.

### Avoid

- mini-review catalogues;
- broad history unrelated to the claim;
- demonstrating how much literature the authors read;
- introducing every later experiment;
- detailed results;
- project genealogy;
- generic promises of significance.

### Closing paragraph

Usually make recoverable:

- exact question/objective;
- scientific strategy;
- central contribution(s);
- headline result/answer when the genre permits;
- important scope boundary.

A table-of-contents roadmap is optional and often lower value than a clear contribution statement.

### Exit test

Before leaving the Introduction, a new reader can answer:

1. What exactly is unknown/problematic?
2. Why is that gap worth resolving?
3. What does this paper do about it?
4. What central concepts are already active?
5. What kind of answer/evidence should I expect?

## 6. Related work / prior-work positioning

This is a **scientific function**, not a mandatory section.

### Reader job

Orient the paper relative to intellectual origins, closest prior capability, strongest comparator, and the residual gap.

### Include

- foundational origins needed for credit and understanding;
- the closest work needed to locate the residual contribution;
- comparator families needed to interpret the evaluation;
- materially conflicting prior evidence.

### Avoid

- exhaustive search inventories;
- `claim subtraction`, `donor`, `parent`, or ownership accounting;
- one paragraph per neighboring paper;
- listing every paper found during novelty verification;
- repeating Introduction positioning in full;
- spending more space on neighboring work than on the current paper's scientific object without a genre-specific reason.

### Placement

Prior work may be integrated into:

- Introduction;
- method/problem setup;
- Results when a comparator becomes scientifically relevant;
- Discussion for deeper interpretation;
- a dedicated section when the field/venue or argument genuinely benefits.

### Exit test

The reader can state the closest established capability and the precise unresolved difference without reconstructing an internal novelty ledger.

Use `venue-constrained-manuscript-budget.md` to control footprint.

## 7. Problem formulation / theory / task definition / formal setup

### Reader job

Make every downstream claim-bearing object interpretable before Results or proofs rely on it.

### Applicable content

- scientific problem and target quantity/object;
- domain/codomain or population/task family when consequential;
- variables/state/components;
- assumptions and scope;
- comparator/action/decision semantics;
- objective/loss/criterion/estimand;
- representation/input/output boundaries;
- equivalence/admissibility definitions;
- central formal operator/relation;
- one motivating example or counterexample when abstraction would otherwise be opaque.

Use `formal-spine-preservation.md` when the formal object is part of the contribution.

### Functional sufficiency, not length

A one-paragraph setup can be sufficient if every later dependency is active.

A three-page setup can be insufficient if a central metric, model family, hypothesis, or experiment role first appears in Results.

### Avoid

- undefined D0/D1/M1/P4-X-style labels as primary scientific vocabulary;
- definitions by reference to a previous paper in the same project;
- equations without prose telling the reader their scientific role;
- formal notation introduced merely to look rigorous;
- assumptions that appear only after a theorem/result fails without them.

### Exit test

A qualified reader can define every central object that the next major section will manipulate, estimate, prove, compare, or score.

## 8. Methods / Materials and Methods / Experimental setup

### Reader job

Let readers understand how evidence was generated and, at the depth required by field/venue, reproduce or reuse the work.

### Organize by scientific procedure, not code layout

A useful high-level structure can include:

```text
study/design overview
-> data/materials/participants/source selection
-> experimental or computational conditions
-> intervention/model/method implementation
-> outcomes/targets/measurements
-> analysis/statistics
-> robustness/sensitivity when prespecified or methodologically central
-> ethics/governance and deviations where relevant
```

Not every paper needs every item.

### Reproducibility versus narrative placement

The main narrative may need only enough method detail to interpret a Result, while the full Methods carries reproducibility detail. Do not bury claim-changing design features in a repository.

### Include

- actual scientific and independent units;
- selection/inclusion/exclusion rules;
- data split/holdout construction when relevant;
- comparator definitions and why they are fair enough for the claim;
- outcome/metric/estimand definitions;
- important hyperparameter/model-selection procedures when they affect inference;
- uncertainty/statistical analysis;
- randomization/blinding/prespecification when applicable;
- deviations and missing-data handling when consequential;
- software/hardware details only to the depth needed for reproduction or claim interpretation.

### Avoid

- source-tree walkthroughs;
- helper/function/class names when a scientific abstraction exists;
- CLI transcripts;
- CI/test-run chronology;
- unexplained implementation constants;
- `as previously described` shortcuts when exact target/reporting standards require the full reusable method;
- results masquerading as method description.

### Exit test

A relevant expert can understand what generated the evidence, what varied, what was held fixed, what was measured, and what analysis maps observations to claims.

Use current design-specific reporting guidelines where applicable.

## 9. Results

### Reader job

Expose the shortest sufficient evidence chain that answers the paper's scientific questions.

### Organize by scientific dependency

Prefer:

```text
local question
-> why this analysis/test is needed now
-> comparison/setup
-> decisive observation/estimate
-> uncertainty or discriminator
-> bounded local inference
-> unresolved question that motivates the next block
```

Use `sentence-logic-and-cohesion.md` and `main-text-discipline.md`.

### Lead with the message, then evidence

The reader should not have to mentally inspect ten numbers to infer what happened.

Use prose to state the scientific pattern; use tables/figures for dense exact comparison.

### Include

- primary/headline results;
- decisive controls/comparators;
- uncertainty and actual analysis unit;
- negative/null/adverse findings that change interpretation;
- robustness or heterogeneity when it is central or claim-changing;
- enough method context to interpret each result.

### Avoid

- run/version chronology;
- every robustness check in main text;
- restating full tables numerically;
- introducing a new model/dataset/hypothesis without prior activation;
- discussion-length literature interpretation;
- celebratory `PASS`/`FAIL` language instead of scientific results;
- exact machine terminals.

### Exit test

For each Results subsection the reader can answer:

1. What question was tested?
2. Why was this test necessary after the previous result?
3. What comparison or quantity answers it?
4. What was found with what uncertainty?
5. What can and cannot be inferred?
6. Why does the next result exist?

## 10. Discussion

### Reader job

Explain what the findings mean in the scientific landscape, not merely repeat what happened.

For each headline result, choose the necessary subset of:

```text
bounded answer
-> interpretation/mechanism
-> strongest alternative explanation
-> relation to closest prior evidence/theory
-> boundary/generalizability
-> scientific or practical implication
-> next discriminating question
```

Use `epistemic-rhetoric-and-qualification.md`.

### Prior work in Discussion

The closest studies often deserve deeper comparison here than in the Introduction, because the present results now make the comparison meaningful.

Do not re-list all neighboring work. Explain whether the result:

- agrees;
- conflicts;
- extends;
- narrows;
- changes the interpretation of;
- or addresses a different question from prior evidence.

### Limitations belong to interpretation

A limitation should state what inference it changes, not merely prove author humility.

### Avoid

- paragraph-by-paragraph Results repetition;
- new unreported empirical results;
- audit chronology;
- a limitations dump with no scientific synthesis;
- spending more space defending novelty than interpreting findings;
- generic `future work is needed` endings;
- speculation presented at the same confidence as observed results.

### Exit test

A reader can state:

- the paper's strongest surviving conclusion;
- why the evidence supports that interpretation;
- the strongest live alternative;
- how the result changes the relationship to prior work;
- where the conclusion stops;
- what important question remains.

## 11. Limitations / threats to validity

A dedicated section is optional. The function is mandatory when material limitations exist.

### Organize by inferential consequence

Useful classes include:

- construct/measurement validity;
- internal validity/identification;
- statistical/inferential uncertainty;
- external validity/generalization;
- comparator or implementation validity;
- data/evidence availability;
- reproducibility boundary;
- ethical/societal boundary when relevant.

### Use the pattern

```text
limitation -> what claim it weakens/does not weaken -> why -> possible discriminator/repair
```

### Avoid

- ceremonial lists of everything the study did not do;
- repeating the same synthetic/naturalistic caveat in several sections;
- apologizing for a deliberate bounded scope that still supports the stated claim;
- using `limitation` to hide a design flaw that actually invalidates the claim.

A fatal validity problem is not a limitation paragraph; it is a claim/evidence blocker.

## 12. Conclusion

A separate Conclusion is optional and venue/archetype dependent.

### Reader job

Close the scientific argument with the answer and its consequence.

### Prefer

- one compact synthesis of what has been established;
- the most important implication or changed understanding;
- a final boundary/next question only when it adds something not already clear.

### Avoid

- rewriting the Abstract;
- re-listing all contributions;
- introducing new data, citations, or claims;
- generic `in conclusion` filler;
- making the Conclusion longer simply to appear substantial.

A short Conclusion can be excellent when the Discussion already did the interpretive work.

## 13. Figures

Use `scientific-display-decision-contract.md`, `figure-evidence-planning.md`, and `visual-evidence-atlas.md`.

### Reader job

Let the reader inspect a pattern, comparison, distribution, relationship, mechanism, hierarchy, or workflow more efficiently or faithfully than prose/table alone.

### Avoid

- decorative diagrams;
- dashboard-like internal workflow labels;
- panels that exist only because an experiment was run;
- hiding uncertainty, pairing, failures, or denominators;
- visual complexity that cannot survive venue rendering.

Each figure needs a scientific reader question.

## 14. Tables

### Reader job

Support lookup or exact multi-dimensional comparison where precise values matter more than shape/pattern.

### Prefer tables for

- exact benchmark comparisons;
- parameter/specification summaries;
- compact categorical comparison;
- study characteristics;
- detailed estimates where readers need exact values.

### Avoid

- duplicating the same values in prose and figure;
- dozens of columns because the analysis emitted them;
- table-first terminology that has not been activated;
- raw formatter precision;
- uncaptioned or ambiguously numbered tables.

Prose should tell the reader what to learn from the table, not recite every cell.

## 15. Figure and table legends / captions

### Reader job

Make the display locally intelligible without becoming a second Methods or Discussion section.

Normally include as applicable:

- brief informative title;
- what each panel/row/column encodes;
- groups/conditions;
- units/scales;
- sample/statistical unit and `n` where required;
- uncertainty/error-bar semantics;
- tests/annotations/symbol definitions;
- abbreviations required to decode the display.

### Avoid

- long interpretation paragraphs;
- unsupported conclusions;
- exhaustive procedural detail when Methods carries it;
- private file/artifact IDs.

Exact target legend rules override generic defaults.

## 16. Equations, definitions, theorems, proofs, algorithms

Use `formal-spine-preservation.md` and `atomic-claim-verification.md`.

### Reader job

Expose the formal scientific object and what it licenses.

### Requirements

- define every nonstandard symbol before or at first use;
- state domains/conditions/assumptions when they matter;
- connect equation to scientific meaning in prose;
- distinguish definitions, proved statements, candidate laws, hypotheses, and heuristics;
- retain decisive non-implications and boundaries;
- place formal objects in main text when hiding them would erase scientific identity.

### Avoid

- decorative math;
- raw source tokens;
- equations with no interpretive sentence;
- proof details in main text when only the result/intuition is needed and support is allowed;
- using notation to conceal uncertainty or an undefined concept.

## 17. References and citations

Use `literature-version-and-source-quality.md` and `research-integrity-verification.md`.

### Reader job

Provide the evidence and intellectual lineage needed to verify, contextualize, and position claims.

### Select for function

- original/foundational source when relevant;
- strongest current version of record;
- closest prior work;
- evidence for factual/background statements;
- methodological/reporting authority;
- materially conflicting evidence.

### Avoid

- bibliography as literature-search dump;
- citing preprints when a formal version exists without reason;
- citation clusters whose individual roles are unclear;
- citing a review for a precise claim when a primary source is needed;
- strategic citation unrelated to scientific support.

## 18. Supplementary Information / Extended Data / appendices

### Reader job

Provide deep support without forcing the first-pass argument to carry every detail.

Good support content includes:

- full derivations/proofs when main-text result is preserved;
- secondary robustness/sensitivity analyses;
- additional baselines;
- extended method details;
- large tables;
- specialist diagnostics;
- reproducibility materials allowed by target.

### Do not move to support

- conclusion-changing contradictory evidence;
- a definition needed to understand the main result;
- the contribution-defining formal spine;
- primary outcome needed to evaluate the claim;
- a critical comparator whose absence makes main-text evidence misleading.

Support is not a hiding place.

## 19. Data / code / resource availability

### Reader job

Tell the reader where authoritative research artifacts can be accessed and under what conditions.

Prefer one concise authoritative statement containing as applicable:

- persistent archive/repository/DOI/accession;
- release/version/commit needed to bind results;
- access restrictions;
- license;
- source-data location;
- machine-readable result-to-artifact manifest when useful.

### Avoid

- full repository file trees;
- build logs;
- every artifact path/hash in manuscript prose;
- repeated URLs throughout the scientific narrative.

Detailed operation belongs in artifact documentation.

## 20. Ethics, funding, competing interests, author contributions, acknowledgements

These surfaces have compliance/provenance functions and often exact target wording requirements.

### Rule

Resolve the live target policy and applicable reporting guideline. Do not invent or stylistically embellish disclosures.

### Avoid

- mixing acknowledgements or governance details into Results/Discussion;
- using these sections to make scientific claims;
- omitting required disclosures to save space.

## 21. Section headings and subheadings

### Reader job

Expose the conceptual organization of the argument at navigation scale.

Prefer headings that name:

- the scientific object;
- question;
- comparison;
- result;
- mechanism;
- boundary;
- method component.

Avoid headings dominated by:

- internal version IDs;
- project workflow stages;
- `gate`, `terminal`, `receipt`, `PASS`, `FAIL` unless those are formal study objects;
- generic labels so vague that they do not help navigation.

Do not use more heading levels than the reader needs.

## 22. Writing order versus reading order

The final paper is read in one order, but it need not be drafted in that order.

A useful empirical-paper workflow is often:

```text
stable evidence/figures
-> Methods / Results
-> interpretation / Discussion
-> Introduction
-> final Abstract
-> final Title
```

But this is a workflow heuristic, not a universal law. Theory, qualitative, review, resource, and prospective protocol papers may need different drafting sequences.

The invariant is that the final **reading order** satisfies reader dependencies.

## 23. Section transition audit

At every major boundary ask:

```text
What does the reader now know?
What unresolved question remains?
Why is the next section the correct next operation on that question?
```

A section change should not merely mean `the authors did another thing`.

## 24. Cross-section duplication audit

A concept/result may appear in several surfaces only if each appearance has a different function:

```text
Abstract      -> entry-point claim
Introduction  -> motivates/previews
Results       -> establishes
Discussion    -> interprets/bounds
Conclusion    -> synthesizes, if needed
```

Delete duplicate restatements that add no new reader function.

## 25. Section-specific anti-AI-writing audit

Common generative failures differ by section:

### Title
- inflated modifiers;
- overly technical compound noun stacks.

### Abstract
- generic five-sentence template;
- result catalogue;
- too many numbers;
- over-hedging or hype.

### Introduction
- encyclopedic background;
- citation catalogue;
- generic significance language;
- formulaic `however, few studies...` gap regardless of evidence.

### Methods
- code/config leakage;
- pseudo-detail with missing scientific design choices;
- invented procedural completeness.

### Results
- chronological experiment log;
- table recitation;
- every paragraph ending in generic significance language;
- surprise entities.

### Discussion
- Results repetition;
- limitations list replacing interpretation;
- generic future-work boilerplate;
- exhaustive nearest-work defense.

### Conclusion
- abstract repetition;
- promotional final sentence not supported by evidence.

Do not solve these by banning phrases alone. Repair the scientific/rhetorical function.

## 26. Close-analogue calibration

For substantial papers, inspect several genuinely close, high-quality, preferably peer-reviewed papers.

For each section record **function**, not copied form:

```text
what reader question the section answers
what prerequisite it assumes
what evidence/detail is kept in main text
what is moved to Methods/support
how much space it receives relative to the paper's contribution
how terminology is introduced
how numbers are selected
how the section hands off to the next
```

Do not copy sentence templates, headings, or percentages mechanically.

Genre research repeatedly shows real disciplinary variation.

## 27. Clean-reader section audit

A reviewer with no project context should be able to answer, section by section:

- Title: what paper am I about to read?
- Abstract: why/what/finding/meaning?
- Introduction: what exact unresolved problem motivates it?
- Setup: what objects/assumptions are needed?
- Methods: how was evidence generated?
- Results: what did each test establish and why now?
- Discussion: what does it mean and where does it stop?
- Figures/tables: what question does each display answer?
- Support/availability: where can deeper evidence and artifacts be checked?

If the answer depends on internal author knowledge, the paper is not ready.

## 28. Release gate

Do not call a substantial manuscript publication-ready until every applicable section/surface:

- has a defined reader-facing function;
- is sufficient for downstream dependencies;
- contains no unexplained private vocabulary;
- respects target-specific space and structure;
- uses evidence/detail appropriate to that section's role;
- does not hide claim-changing content in support;
- does not duplicate another section without a distinct purpose;
- hands off coherently to the next reader question;
- passes the relevant specialized contract (abstract, formal, statistics, display, integrity, surface QA).

## 29. Transfer boundary

This contract does **not** claim one universal research-paper structure.

Section functions and rhetorical moves vary by:

- discipline;
- epistemology;
- empirical/theoretical/qualitative/review/resource archetype;
- venue/article type;
- reporting standard;
- paper length;
- intended readership.

When the local convention is uncertain or consequential, research the exact venue and close papers before imposing a template.

The invariant is **functional completeness and reader dependency**, not conformity to a generic paper outline.
