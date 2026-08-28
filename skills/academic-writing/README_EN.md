# `academic-writing` Skill

[中文说明](README.md)

`academic-writing` is the canonical journal-agnostic writing skill for this repository. It drafts and restructures manuscripts from scientific evidence rather than from a Nature template.

The older `skills/nature-writing/` directory remains only as a compatibility/reference implementation layer for mature section fragments, examples, and corpus scripts. **New user-facing invocation is `$academic-writing`.**

## What It Does

- resolves the real paper archetype before choosing structure;
- builds the argument and claim/evidence dependencies before polishing sentences;
- researches unfamiliar paper types/venues instead of guessing conventions;
- studies broad stratified corpora and 3–6 close analogue papers without copying prose or figure identity;
- checks whether ideas are explained deeply enough for the intended reader;
- makes sentence-to-sentence logic explicit;
- binds raw, validated, analysis-ready, analysis-input, and release data objects before drafting downstream claims;
- plans what evidence and figures the paper actually needs;
- decides what belongs in main text, Methods, SI, availability, artifact docs, or nowhere;
- preserves a recognizable author voice while avoiding generic AI-like prose;
- adapts the scientifically stable manuscript to the exact target last;
- runs a hard final filename/script/repository leakage and punctuation/typography gate.

## Exact Venue Decision Contracts

When target-specific readiness matters, `academic-writing` resolves **exact
venue × article type × stage × effective date**. It keeps scientific gates,
novelty/impact/breadth/audience-interest gates, burden-of-doubt rules, allowed
repairs, review model, AI/confidentiality policy, acceptance states, and any
certification layer separate.

Maintained TMLR, Nature Article, and PLOS ONE Research Article snapshots
demonstrate materially different objectives. They are examples of the
architecture, not a claim that every journal is hard-coded. Unknown, stale,
future-effective, or conflicting targets require live official-source
resolution; a fallback profile is never presented as exact journal policy.

## Study Protocol And Conduct Contracts

Before Methods, Results, claims, or figures are drafted as authoritative, the
skill can materialize:

```text
protocol version -> analysis-plan version -> conduct receipt
-> deviation ledger -> analysis/result -> bounded claim
```

Ten maintained study-type adapters cover randomized, observational,
computational/ML, animal, systematic-review, qualitative, experimental,
resource, and exploratory work without declaring a universal best design.
Behavioral checks block false prospective labels, undisclosed outcome changes,
unverified randomization/blinding execution, hidden stopping/exclusions or
harms, evaluation leakage, unsupported confirmatory status, broken data lineage,
and missing required ethics authority.

The 39-source evidence registry records 19 full-text and 20 abstract-level
reads, explicit transfer limits, and a frozen 84-record search log. Passing is a
bounded traceability result, not a scientific-validity certificate and not a
journal-acceptance prediction.

## Data Integrity And Stewardship Contracts

Before statistics, Results, displays, claims, availability statements, or
readiness decisions, the skill binds:

```text
source/acquisition record -> immutable raw or exact external-reference origin -> validation/QC receipts
-> versioned transformations -> immutable analysis-ready snapshot
-> analysis/display inputs -> governed release -> bounded claim
```

Ten maintained modality/governance adapters activate relevant obligations
without claiming a universal data-quality score or hard-coded coverage of every
discipline, law, institution, funder, repository, licence, or community policy.
Unmatched and exact-policy cases remain live official-source research duties.
Behavioral checks fail closed on mutable raw data, broken lineage, missing
execution/QC/calibration evidence, input-hash or count mismatch, hidden
adverse/null exclusions, unit/semantic drift, unauthorized sensitive release,
missing authority or rights, and false release/version claims.

The 41-source evidence base includes 22 peer-reviewed full-text studies, 13
official standards/guidance/policies, and 6 abstract-level reads, plus 12 frozen
queries and 84 screened metadata records. Passing certifies only recorded
lifecycle invariants—not measurement accuracy, completeness,
representativeness, privacy, legal compliance, reproducibility, scientific
truth, or acceptance.

## Scientific Display Decision Contracts

Every evidence-bearing plot, figure, table, image plate, or diagram can now be
bound to a machine-readable contract:

```text
reader question -> estimand/scientific object -> statistical unit/data structure
-> candidate representation -> allowed/prohibited inference
-> data snapshot -> analysis receipt -> render receipt -> source data
-> caption/accessibility -> final-size review
```

Maintained adapters return candidate families and scientific obligations, not a
universal best chart. Behavioral checks fail closed on hidden pairing,
denominator drift, stale analysis/render lineage, undefined uncertainty,
undisclosed group omission, embedding/workflow overclaims, color-only encoding,
and missing final-stage alt text.

The initial evidence registry contains 39 reconciled sources (20 full text, 18
abstract-level, one official standard), with search provenance, read depth,
supported decisions, transfer limits, contradictions, and update triggers.

## Writing Model

For substantial work:

```text
scientific evidence
-> paper archetype
-> protocol + analysis plan + executed conduct + deviations
-> raw snapshot + QC + transformations + analysis-ready/release bindings
-> question / contribution
-> claim/evidence/boundary map
-> content selection
-> broad corpus + close analogues when useful
-> figure/statistics plan
-> scientific display decision contracts
-> section moves
-> paragraph dependencies
-> sentence dependencies
-> explanatory sufficiency
-> natural scholarly prose + author voice
-> exact target adaptation
-> final manuscript-surface QA
```

## Sentence Logic

A difficult paragraph is audited sentence by sentence:

```text
inherits X
-> relation R
-> adds Y
-> enables Z
```

The skill also checks identity chains, topic continuity, given/new progression when useful, subject–verb distance, emphasis position, evidence-to-inference warrants, and analysis-to-analysis handoffs.

A connective labels a relationship. It does not create one.

## Rich Content Without Bloat

For a central idea/result, the skill asks whether the reader has enough of the following to understand and evaluate it:

- identity/definition;
- motivation;
- mechanism/inferential logic;
- decisive evidence;
- comparator/baseline;
- uncertainty;
- alternative explanation;
- assumption/boundary;
- relation to prior work;
- scientific consequence;
- visual evidence when useful.

This is **minimum sufficient scientific explanation**, not maximal word count.

## Learning From Other Papers

Use two scales:

- **broad stratified corpus** — descriptive tendencies across dozens/hundreds of genuinely comparable papers;
- **3–6 close analogues** — deep reasoning about evidence sequence, explanation depth, figure roles, uncertainty, local terminology, and reader assumptions.

Published frequency is not a quality score and not an acceptance rule.

Learn the function behind the writing/figure choice, then create original prose and visuals for the current evidence.

## Unknown Paper Types

If the current paper class is not covered confidently, `academic-writing` does not force a nearby template.

It researches:

1. current official target guidance;
2. applicable reporting/methodological standards;
3. comparable recent papers;
4. nearest-neighbor full papers;
5. counterexamples.

It then builds a temporary manuscript-specific archetype profile.

## Figures

Figure planning follows:

```text
claim
-> reader question
-> scientific/statistical unit
-> estimand / visual object
-> data structure
-> uncertainty / competing explanation
-> representation
-> main/support/omit
```

A qualitative/theory paper may need no quantitative main figure. A failure boundary may deserve a main figure when it changes the headline conclusion.

Detailed rendering and scientific diagrams route to the figure skill.

## Natural Scholarly Tone

The goal is not AI-detector evasion.

The skill repairs:

- repetitive stance;
- standardized cadence;
- generic prestige language;
- synonym rotation that damages technical identity;
- connector stuffing;
- depersonalized prose that hides meaningful author decisions;
- repeated sentence/paragraph templates.

It preserves author voice after logic/evidence repair.

## Final Surface Gate

Before delivery, manuscript-facing text is checked for:

- file/directory paths;
- script/notebook/config/output filenames;
- helper/class/function names;
- CLI commands/flags;
- branch/PR/issue/commit/CI residue;
- raw project URLs outside availability sections;
- doubled/missing punctuation;
- punctuation spacing;
- bracket balance;
- malformed figure references;
- range/minus/hyphen/unit issues;
- target-aware citation/equation/legend punctuation.

**The audit trail may name the artifact; the manuscript should name the science.**

## Repeated Review/Revision

For a closed-loop process that keeps researching, writing, rebuilding figures, reviewing, revising, and re-reviewing until the simulated editor reaches a terminal decision, use `academic-paper-pipeline`.

## Boundaries

- Never invent results, experiments, citations, mechanisms, significance, uncertainty, or novelty.
- Never hide contradictory evidence to improve presentation.
- Never copy distinctive prose or visual identity from analogue papers.
- Never force Nature conventions onto a non-Nature target.
- Never equate more words, more figures, or more experiments with a stronger paper.
- Never leave repository implementation detail in manuscript prose merely because it is available to the AI session.

## Compatibility

The old `nature-writing` implementation remains installed for backward compatibility and internal references, but it is not the canonical public writing skill and should not be implicitly invoked for new work.
