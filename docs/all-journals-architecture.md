# All-journals academic-paper architecture

The repository keeps the historical `nature-*` skill names for compatibility, but the core academic workflows do **not** infer the target journal, evidence standard, writing style, or publication objective from those names.

Last architecture review: 2026-08-22.

## Design goal

Support arbitrary academic journals, disciplines, study designs, and article types without maintaining a brittle hard-coded list of thousands of titles or forcing one prestige-journal style onto every paper.

The current architecture separates:

1. **truth / evidence** — what the data, sources, methods, proofs, and analyses actually establish;
2. **argument / rhetorical logic** — how the contribution, evidence chain, boundaries, and meaning are organized;
3. **analogue-paper priors** — what a few genuinely comparable papers reveal about local evidence, figure, and rhetorical conventions;
4. **natural scholarly realization** — how sentence dependencies, information flow, identity chains, stance, syntax, and cadence make reasoning readable;
5. **author voice** — the manuscript's recognizable cadence, agency, terminology, technical density, and signposting;
6. **discipline/reporting obligations** — design-specific methods, statistics, ethics, reproducibility, and reporting standards;
7. **journal-specific editorial objective** — breadth/priority, field advancement, rigor-first, clinical priority, evidence-assessment, conference selection, etc.;
8. **house style / submission mechanics** — headings, limits, formats, legends, source data, templates, production rules;
9. **editor/reviewer decision logic** — triage, independent technical review, synthesis, and decision-relevant repair;
10. **revision closure** — evidence/analysis/correction/clarification/claim-narrowing/removal rather than response-letter length.

The governing hierarchy is:

`scientific validity -> argument/evidence architecture -> reader clarity/natural prose -> author voice -> reporting obligations -> journal objective -> house style/mechanics`

Exact journal rules are resolved at use time when needed.

## Full manuscript lifecycle

A serious manuscript workflow can now be represented as:

`best evidence -> argument spine -> close analogue study -> section/paragraph move design -> evidence/figure allocation -> sentence dependency + natural prose -> author re-voice -> exact journal resolution -> editor/reviewer preflight -> submission -> revision closure`

Not every task needs every stage. Routers load only relevant resources.

## Shared journal resolver

`skills/nature-shared/journal-formats/journal-resolution.md` defines the common resolution tuple:

`exact journal -> article/content type -> submission stage -> output component`

Resolution priority:

1. current exact official journal instructions;
2. exact versioned local profile when available;
3. publisher/venue family fallback profile;
4. discipline/reporting profile;
5. generic scholarly default.

The live exact guide is required for submission-critical numeric/mechanical rules.

## Family profiles

`skills/nature-shared/journal-formats/journal-family-profiles.md` provides fallback questions and writing/workflow context for:

- Nature Portfolio;
- Science / AAAS;
- Cell Press;
- IEEE;
- ACM;
- PLOS;
- Springer/BMC/SpringerOpen;
- Elsevier;
- Wiley and society journals;
- APA-style social/behavioral venues;
- medical/clinical reporting;
- humanities/law.

Family profiles are deliberately not universal submission contracts.

## Publication decision profiles

`skills/nature-shared/journal-formats/editorial-decision-profiles.md` separates incompatible editorial objectives rather than using one `novelty + rigor + impact` formula.

Fallback profiles include:

- selective broad-interest;
- selective field-advancement;
- rigor-first scholarly record;
- clinical/policy-priority;
- evidence-assessment without conventional post-review gatekeeping;
- deadline-constrained conference selection.

Exact target guidance always overrides the fallback profile.

## Shared writing intelligence

### Rhetorical engine

`skills/nature-writing/static/core/rhetorical-engine.md` treats the manuscript as:

`question/tension -> answer/contribution -> evidence chain -> boundary -> meaning`

Contribution types include empirical findings, mechanisms, methods, resources, theory, replication/validation, negative/null results, syntheses, and practical/clinical/policy implications.

Sections are move graphs rather than universal templates.

### Paragraph model

A paragraph uses one **nucleus** plus necessary satellites such as evidence, explanation, comparison, qualification, counterevidence, implication, or bridge.

The repository does not require every paragraph to perform exactly one rhetorical function.

### Sentence-flow model

`skills/nature-writing/references/paragraph-flow.md` and `skills/nature-shared/core/natural-scholarly-prose.md` operate below the paragraph level.

For every non-initial sentence in a difficult paragraph:

`inherits X -> relation R -> adds Y -> enables Z`

The repair order is:

`proposition/dependency -> relation -> information progression -> identity/reference chain -> topic/emphasis -> stance -> syntax -> connective -> cadence`

Given->new is a useful default, not a universal sentence template.

### Natural scholarly prose

`skills/nature-shared/core/natural-scholarly-prose.md` addresses prose that is technically correct but generic, over-smoothed, formulaic, repetitive, connector-heavy, or machine-like.

It explicitly rejects:

- AI-detector score optimization;
- `AI word` blacklists;
- deliberate mistakes;
- random sentence-length `burstiness`;
- arbitrary synonym replacement;
- forced informality.

Instead, it targets:

- proposition-level reasoning;
- identity chains;
- purposeful syntactic variation;
- locally calibrated stance;
- precise conventional vocabulary;
- real rather than decorative connectives;
- authorial responsibility where relevant;
- cadence after logic is stable.

Research synthesis: `docs/academic-writing-research_EN.md` / `docs/academic-writing-research.md`.

Operational guide: `docs/natural-scholarly-writing_EN.md` / `docs/natural-scholarly-writing.md`.

## Analogue-paper calibration

`skills/nature-shared/core/analogue-paper-calibration.md` provides a focused close-reading layer for substantial rewrites.

A typical focused pass studies **3–6 genuinely close analogues** when available, matched by:

- question/contribution class;
- study design;
- data/evidence type;
- article type;
- subfield/community;
- exact target venue and recent period when useful.

Comparability outranks prestige.

The analogue pass extracts:

- research-need construction;
- evidence dependency;
- section/paragraph moves;
- figure roles;
- visible controls/uncertainty/raw observations;
- validation/generalization/failure-boundary patterns;
- main-text versus Methods/SI allocation;
- background/signposting/interpretation conventions.

It learns **functions, relations, evidence architecture, and visual grammar**, not distinctive wording or visual identity.

## Author voice

`skills/nature-shared/core/author-voice-profile.md` is deliberately separate from analogue style.

Conceptual split:

`author evidence = truth constraint`

`journal/reporting rules = compliance constraint`

`analogue papers = structural/evidence priors`

`author voice = expression prior`

The voice profile can preserve:

- argument tempo;
- sentence cadence;
- agency (`we` / passive / process focus);
- technical density;
- stance rhythm;
- paragraph rhythm;
- citation integration;
- stable terminology.

Natural scholarly prose is the **quality floor**; author voice is the **identity layer**. Voice preservation must not restore ambiguity, errors, or unsupported claims.

## Function changes by skill

### Writing

`nature-writing` is now a journal-aware writing/restructuring engine rather than a `Nature-style` template writer.

It can:

- build the argument spine;
- calibrate section moves cross-disciplinarily;
- close-read analogue papers;
- preserve/reconstruct author voice;
- repair natural sentence-to-sentence flow;
- allocate evidence across main text/figures/Methods/SI;
- resolve exact journal rules;
- run editor/reviewer decision preflight;
- build initial-submission packages.

### Polishing

`nature-polishing` uses layered editing:

1. target-independent scientific/logical edit;
2. natural-scholarly-prose + author re-voice when needed;
3. verified target-dependent adaptation.

This prevents polishing from changing evidentiary strength merely to imitate a prestigious journal or `humanizing` prose through detector-oriented noise.

### Figures

`nature-figure` separates scientific figure design from target-journal production mechanics.

Its analogue-figure layer studies what comparable figures **prove**, what data units/comparators/uncertainty they expose, and what is placed in main text versus SI.

Final plot choice remains data/estimand-driven. A plot is not selected merely because it is common in analogue papers.

### Citation discovery

General citation requests default to `best-evidence` instead of CNS-family filtering.

`scripts/academic_citation_search.py` reuses the legacy citation script's metadata parsing, author-integrity checks, deduplication, and RIS/ENW/Zotero export helpers but does not apply a prestige whitelist by default.

Explicit `nature`, `science`, `cell`, `cns`, and `flagship` scopes remain available when the user explicitly requests them.

Evidence selection and final bibliography rendering are separate. A manuscript targeting Journal X does not imply its citations should come only from Journal X.

### Academic search

The search strategy is publication-ecology aware: conference proceedings can be primary literature in computing/engineering; books and archives can be primary scholarship in humanities; guidelines can be appropriate evidence in clinical contexts. Citation count is not a universal evidence score.

### Reviewer simulation

`nature-reviewer` now models:

`exact target criteria -> editorial triage -> mutually blind reviewers -> editor synthesis -> author-facing decision map`

Reviewers do not receive the simulated editor's triage conclusion.

Editors are modeled as weighing arguments rather than counting reviewer votes.

Analogue papers may inform **contextual evidence expectations**, but never become invented publication policy.

### Revision response

`nature-response` treats revision as closure of decision-relevant concerns.

Closure routes include:

- add decisive evidence;
- reanalyse existing evidence;
- correct an error;
- clarify/restructure existing evidence;
- narrow the claim;
- remove the claim;
- explain justified nonimplementation;
- reconsider target/article type when fit is the real problem.

### Reference verification

Reference verification distinguishes:

- bibliographic identity/metadata correctness;
- target-journal rendering style;
- in-text/reference cross-link correctness.

Journal transfer should re-render from verified metadata instead of manually editing already-formatted strings when possible.

## Backward compatibility

This architecture does not rename the `nature-*` skill directories or entry-point names.

The compatibility rule is:

> legacy name does not imply legacy scope.

Exact Nature-family profiles and legacy explicit CNS citation behavior remain available when specifically requested.

## Research architecture

The writing engine uses several evidence layers rather than one source of truth:

### Large corpus research

Used to test whether writing patterns survive across disciplines/sections.

Examples currently encoded include:

- 500 research-article introductions across five social-science disciplines;
- 900 Methods texts across 30 fields;
- 5,910 abstracts across six disciplines;
- >1 million abstracts across eight disciplines;
- section-level and cross-disciplinary cohesion corpora;
- recent human-versus-LLM academic-writing corpora.

### Direct reading

Used to understand complete argument/evidence sequences in contrasting publication ecologies.

### Close analogue study

Used for paper-class-specific local decisions before serious rewriting.

### Broad target-corpus calibration

Used when distributions/tendencies across a venue/field matter beyond a handful of analogues.

### Official target guidance

Used for exact editorial/reporting/formatting/mechanical requirements.

No one layer should be mistaken for the others.

## Adding an exact journal profile later

Add an exact profile only when repeated use justifies maintaining it.

A profile should record:

- exact journal title;
- reviewed date;
- official source URLs/titles;
- article/content types covered;
- stage distinctions;
- verified limits/mechanics;
- known unresolved/conflicting rules.

Then add a precise router value or exact-target branch without changing the generic resolver.

## Research basis reviewed 2026-08-22

The repository has now been calibrated against:

- current official author/editor/reviewer resources across major publisher/venue ecosystems;
- large cross-disciplinary rhetorical-move corpora;
- Methods/abstract/heading research;
- local/global/text cohesion studies;
- human-versus-LLM academic-writing research on stance, lexical/syntactic patterns, standardization, and authorial identity;
- direct reading of recent papers across Nature Portfolio, PLOS, JAMA, IEEE, eLife, JMLR and other publication ecologies;
- close analogue-paper and figure-analysis workflows.

Because journal guidance and language practices change, these files are versioned routing/reasoning knowledge rather than permanent substitutes for current official sources or direct reading of relevant papers.
