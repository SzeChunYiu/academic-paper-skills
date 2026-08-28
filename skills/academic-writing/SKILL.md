---
name: academic-writing
description: Canonical journal-agnostic academic manuscript writing skill. Draft, restructure, expand, compress, or plan titles, abstracts, Introductions, related work, Methods, Results, Discussions, Conclusions, and full-paper arguments from author-provided evidence. Resolve the paper archetype and target independently, research unfamiliar paper types/venues instead of forcing a template, study broad corpora and a few close analogue papers without copying them, plan evidence/figures, check explanatory sufficiency and sentence-to-sentence logic, preserve author voice, and run final manuscript-surface leakage/punctuation QA. Nature is only one optional target adapter. Use for academic writing, paper drafting, manuscript logic, natural scholarly prose, rich content, plot/figure planning, journal transfer, editor/reviewer preflight, 学术写作、科研写作、论文写作、句间逻辑、论文结构、论文润色与投稿写作.
---

# Academic Writing — Canonical Router

`academic-writing` is the canonical writing identity for this repository.

**Nature is not the default.** Target journal, paper archetype, evidence standard, article type, reporting obligations, prose conventions, and figure logic are resolved independently.

The historical `skills/nature-writing/` directory remains only as a compatibility/reference implementation layer for section fragments, corpus scripts, examples, and older integrations. New user-facing routing should invoke `$academic-writing`.

## Load the core

Read [manifest.yaml](manifest.yaml) and every file under `always_load`.

For detailed section/paper-type fragments and mature writing references, the compatibility implementation remains under `../nature-writing/`. Use it as a library, not as a signal that the target is Nature.

At minimum, before substantial manuscript work load the relevant shared contracts for:

- paper archetype;
- content selection;
- sentence logic and cohesion;
- explanatory sufficiency;
- natural scholarly prose;
- figure/evidence planning;
- final manuscript-surface QA.

## 1. Resolve the scientific paper, not a prestige style

Classify:

```text
scientific question / contribution
study design
evidence modality
dominant paper archetype
secondary archetype(s)
intended reader
article type
target journal/venue if known
submission stage
```

Use `../nature-shared/core/paper-archetype-atlas.md`.

Do not force one structure across:

- mechanism/discovery papers;
- randomized interventions;
- observational studies;
- computational/ML papers;
- methods/tools/software/instruments;
- resources/datasets;
- theory/proof papers;
- qualitative/interpretive studies;
- reviews/perspectives/systematic syntheses;
- hybrids.

## 2. Self-research when uncertain

If the paper type, target, reporting standard, writing convention, or figure grammar is not confidently covered, use `../nature-shared/core/unknown-paper-research-protocol.md` **before** inventing a rule.

Research, as needed:

1. current official target guidance;
2. applicable reporting/methodological standards;
3. a quick 8–15-paper comparable profile;
4. 3–6 nearest-neighbor papers for deep reading;
5. counterexamples.

Build a temporary manuscript-specific archetype profile.

Comparability outranks prestige.

## 3. Freeze truth and source boundaries

Separate:

- author-provided results/data;
- claims/inferences;
- literature/context;
- methods facts;
- project/repository artifacts;
- missing evidence;
- limitations/constraints.

Never invent results, mechanisms, significance, citations, experiments, novelty, or uncertainty.

External research can improve context, methods guidance, interpretation, citations, and genre calibration. It cannot become a result the study did not produce.

## 4. Build the argument before prose

Use the argument spine:

```text
question / unresolved tension
-> bounded contribution / answer
-> evidence progression
-> strongest alternative / uncertainty
-> boundary
-> meaning
```

For each headline claim build a claim/evidence/boundary record. For a full
manuscript, formal/theory section, or readiness decision, also load
`../nature-shared/core/atomic-claim-verification.md` and inventory every atomic
definition, assertion, proof dependency, number, source claim, availability
statement, and cross-section restatement. A pointer is not verification; check
that the located warrant entails the proposition at its stated scope.

Do not manufacture a `gap` merely to make the paper sound important.

## 5. Make the content rich enough to understand

Use `../nature-shared/core/explanatory-sufficiency.md` and `../nature-shared/core/manuscript-content-selection.md` together.

For central ideas/results, ensure the intended reader receives the necessary subset of:

- what the concept/result is;
- why it is needed here;
- how the mechanism/inference works;
- decisive evidence;
- meaningful comparator/baseline;
- uncertainty;
- strongest alternative explanation;
- assumption/boundary;
- relation to prior work;
- consequence/what follows.

`Rich` means scientifically sufficient, not verbose.

Do not delete reasoning merely to make prose short. Do not add textbook filler merely to make prose long.

## 6. Keep project artifacts out of the paper

Before drafting and again before release, separate scientific content from repository/developer detail.

Translate:

- scripts/functions -> scientific operations;
- configs -> consequential parameters;
- source directories -> scientific modules/steps only when scientifically relevant;
- project URLs -> one authoritative availability location;
- reproduction commands/file trees -> artifact documentation.

Never expose filenames, paths, helper names, temporary output files, branches, PRs, commits, CI/tests, or CLI commands in manuscript prose/legends just because they exist in the project.

Use `../nature-shared/core/manuscript-surface-qa.md` as the final release gate.

## 7. Study papers at two scales

### Broad corpus

For dozens/hundreds of comparable extracted papers, use the compatibility scripts under `../nature-writing/scripts/`:

- `corpus_structure_stats.py`;
- `corpus_figure_inventory.py`.

Use broad corpora for **conditional descriptive tendencies**, not quality scores.

Stratify by archetype/study design/article type before aggregating.

### Close analogues

Deep-read roughly 3–6 true near-neighbors when useful.

Learn:

- argument/evidence dependencies;
- explanation depth;
- figure roles;
- comparator/uncertainty choices;
- main-versus-support allocation;
- sentence/paragraph handoffs;
- stance and terminology.

Do not copy sentences, distinctive paragraph architecture, layouts, palettes, or visual identity.

## 8. Plan figures before prose becomes rigid

Use `../nature-shared/core/figure-evidence-planning.md`.

For every major claim ask:

```text
reader question
-> scientific/statistical unit
-> estimand / visual object
-> data structure
-> uncertainty / alternative explanation
-> representation
-> main / support / omit
```

A qualitative or theory paper may need no quantitative figure. A limitation/failure can deserve a main figure if it changes the headline interpretation.

Route rendering and detailed diagram design to the scientific-figure capability.

## 9. Build section and paragraph logic

Use the relevant compatibility fragments under `../nature-writing/static/` and references under `../nature-writing/references/` as needed.

Plan sections as reader questions and move graphs, not a universal IMRaD/Nature skeleton.

Each paragraph needs a nucleus plus only the satellites required for:

- evidence;
- explanation;
- comparison;
- qualification;
- counterargument;
- implication;
- bridge.

## 10. Make every sentence logically connected

Use `../nature-shared/core/sentence-logic-and-cohesion.md`.

For each non-initial sentence in a difficult paragraph:

```text
inherits X
-> relation R
-> adds Y
-> enables Z
```

Then check:

- stable identity chains;
- topic/context continuity;
- given/new progression where appropriate;
- subject–verb distance;
- evidence-to-inference warrant;
- stress/emphasis placement;
- analysis-to-analysis handoff;
- connectives only when they label a real relation.

A connective cannot manufacture logic.

## 11. Humanize by improving scholarly control, not detector evasion

Use `../nature-shared/core/natural-scholarly-prose.md` and `../nature-shared/core/author-voice-profile.md` when appropriate.

Natural scholarly writing should show:

- locally calibrated stance;
- purposeful agency;
- functionally motivated syntactic variation;
- stable terminology;
- precise conventional vocabulary;
- non-mechanical cadence;
- real sentence dependencies;
- a recognizable author voice.

Do not use AI-word blacklists, random sentence lengths, deliberate errors, fake informality, or detector optimization.

## 12. Apply exact target rules and decision contract last

Scientific validity and reader logic come first.

When a target is known, resolve:

`exact venue × article type × stage × effective date`

Then resolve the output component separately for house style and mechanics.

Use `../nature-shared/journal-formats/venue-decision-contract.md` to keep these
target fields explicit and independent:

- scientific/eligibility gates;
- novelty, impact, breadth, and audience-interest gates;
- burden-of-doubt rules;
- allowed repair routes, including claim narrowing when supported;
- review model and decision owner;
- author/reviewer AI use and confidentiality;
- acceptance states;
- any certification layer, separate from acceptance;
- official sources, access dates, effective-date basis, and unresolved policy.

Use current official instructions for submission-critical requirements.

Prefer live official-source resolution for exact current readiness. A maintained
exact profile is versioned local knowledge. A fallback profile is not exact journal policy. If the tuple/date is unknown, future-effective, stale, or
conflicting, mark it unresolved and run live official-source resolution rather
than attributing a generic objective to the journal.

## 13. Editor/reviewer preflight

For submission readiness, use the shared editor/reviewer decision engine or `$academic-paper-pipeline` for repeated closed-loop review/revision.

Distinguish:

- target-fit blockers;
- exact-contract/source/date uncertainty;
- technical blockers;
- missing explanation;
- reporting/statistical problems;
- figure/evidence gaps;
- claim recalibration;
- optional enrichment.

More experiments are not automatically the right repair.

## 14. Final release gate

Before returning manuscript-facing text:

1. atomic claim/evidence/proof/source verification for full, formal, or
   submission-ready scope;
2. explanatory sufficiency;
3. sentence/paragraph logic;
4. terminology/number/unit consistency;
5. figure/legend adequacy;
6. citation/prior-work fairness;
7. main-versus-support allocation;
8. artifact-leakage scrub;
9. punctuation/spacing/bracket/range/minus/hyphen/unit QA;
10. locally intelligible standalone surfaces and target-resolved abstract
    displays;
11. zero unexplained private terms/symbols, unresolved surface-review items, or
    release placeholders in manuscript-facing text;
12. every-page rendered-artifact, metadata, accessibility, and final-page/spill
    review when a PDF or equivalent final artifact exists;
13. exact target compliance when known.

Do not describe a full manuscript as publication/submission/public-posting ready
while any in-scope atomic item is `SUPPORTED_INTERNAL`, `UNRESOLVED`,
`CONTRADICTED`, `BLOCKED`, or `NOT_ASSESSABLE`.
Continue useful draft work, but return the corresponding blocked state and exact
resolution test. A prose improvement cannot close a mathematical contradiction
or missing proof.

When plain-text/Markdown is available, the shared conservative surface scanner may flag high-confidence mechanical issues. Contextual review still decides the repair.

## Output

Return the requested prose first.

For substantial work, add only the decision-support material useful to the user, such as:

- paper archetype;
- argument spine;
- explanation gaps;
- content allocation;
- figure/plot suggestions;
- unresolved evidence;
- editor/reviewer risks;
- final surface-QA state.

Do not bury the manuscript under internal audit machinery unless the user asks.

## Compatibility boundary

- `$academic-writing` is the canonical invocation.
- `skills/nature-writing/` remains a compatibility/reference implementation layer only.
- A request targeting Nature should resolve Nature through normal journal routing; a request targeting another venue must not inherit Nature rules.
- New docs and examples should use `academic-writing` as the public name.
