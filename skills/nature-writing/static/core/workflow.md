# Writing workflow

Run this workflow for drafting or restructuring. The order is:

`argument -> source/content triage -> analogue/voice calibration -> evidence/figure planning -> rhetorical moves -> paragraph nuclei -> sentence dependencies -> natural scholarly realization -> journal adaptation`

not `repository/docs/template -> prose`.

## 1. Build the argument spine

Before drafting, identify:

- **question / tension** — what is not yet settled, explained, measured, compared, validated, synthesized, or enabled?
- **answer / contribution** — what does this paper actually establish or provide?
- **evidence chain** — which results, analyses, proofs, cases, comparisons, or sources make that answer credible?
- **boundary** — where does the answer stop holding?
- **meaning** — why does the bounded answer matter to the intended research community?

If there are multiple contributions, identify one dominant spine and attach secondary branches. Do not compress unrelated contributions into one inflated novelty claim.

If an essential link is absent, expose the missing link rather than inventing it.

## 1b. Build the Terminology Ledger

On first contact with the material, extract recurring terms, abbreviations, notation, variables, datasets, models, populations, conditions, and proper names. Lock canonical forms and reuse them across every section. See `../../../nature-shared/core/terminology-ledger.md`.

## 2. Classify contribution and evidence type

Use `static/core/rhetorical-engine.md` to classify the dominant contribution: empirical finding, mechanism, method, resource/benchmark, theory/proof, validation/replication, negative/null result, synthesis/review, or practical/clinical/policy implication.

Also identify the evidence type and research paradigm. A randomized trial, qualitative interview study, theorem paper, materials experiment, benchmark paper, and historical argument require different rhetorical structures even when they target similarly selective journals.

## 2b. Triage source material before it leaks into the manuscript

For substantial drafting/rewrite from mixed source material — notes, code, repositories, configs, project docs, experiment logs, notebooks, figure folders — load `../../../nature-shared/core/manuscript-content-selection.md`.

For every candidate content item, classify whether it is:

- inference-critical;
- interpretation-critical;
- reproducibility-critical;
- compliance/provenance-critical;
- orientation-critical;
- or none.

Then assign the correct destination:

`main text / main figure / legend / Methods / Extended Data / SI / availability / repository-artifact docs / omit`

### Repository-to-manuscript leakage gate

Flag file paths, script/helper/class names, setup commands, CLI flags, configs, branch/PR/issue history, unit tests, internal module structure, repeated GitHub links, and developer workflow as potential **implementation-detail leakage**.

Translate artifacts into scientific abstractions:

- script/function -> scientifically consequential method/analysis;
- config -> consequential parameter values;
- GitHub/resource link -> Code/Resource Availability;
- setup/reproduction commands -> artifact README/appendix;
- internal names -> canonical scientific terminology.

Use the test:

> If the implementation were rewritten but the scientific method and results stayed identical, would this detail still matter?

If not, do not let it occupy scientific narrative merely because it exists in the repository.

## 2c. Run focused analogue-paper study for substantial rewrites

When the task is substantial and the field, study design, contribution class, or target is known, load `../../../nature-shared/core/analogue-paper-calibration.md`.

Use a few close papers as **structural/evidence priors**. Prefer comparability over prestige. Study:

- how the research need is created;
- how the contribution is positioned;
- how evidence blocks are sequenced and why;
- what main-text evidence is visible for comparable claims;
- what the main figures are meant to establish;
- what data/uncertainty/controls/validation/generalization/failure boundaries are shown;
- what is moved to Methods/SI/Extended Data;
- how much background, signposting, citation synthesis, and local interpretation the audience receives.

Do not copy phrases, distinctive paragraph structures, figure compositions, palettes, normalization/statistical choices, or journal mechanics inferred from published PDFs.

Skip or bound this step for tiny edits or when no trustworthy comparator set exists.

## 2d. Build an author-voice profile when the rewrite should remain recognizably theirs

When representative author prose is available or the user asks to preserve style, load `../../../nature-shared/core/author-voice-profile.md`.

Record a compact profile:

- voice invariants: cadence, agency, technical directness, signposting level, stable terminology, epistemic rhythm;
- flexible traits: paragraph/sentence length, transitions, headings, context amount, local compression.

Do not preserve errors or ambiguity as `voice`.

Use the separation:

`author evidence = truth constraint`

`journal rules = compliance constraint`

`analogue papers = structural/evidence priors`

`author voice = expression prior`

After large structural rewriting, run a re-voice pass so the improved section does not sound like generic academic English or a clone of the analogue set.

## 3. Plan evidence and figures before prose becomes fixed

For Results/full manuscripts, load:

- `../../../nature-shared/core/main-text-discipline.md`;
- `../../../nature-shared/core/figure-evidence-planning.md` when figures/plots are not already settled.

### 3a. Allocate evidence

Classify each result as core discovery, necessary support, qualification, robustness, heterogeneity, provenance detail, alternative inference, edge case, or artifact operation.

Build the **shortest sufficient evidence chain** while keeping conclusion-changing qualifications visible.

### 3b. Build a claim-to-figure plan

For every headline claim ask:

```text
What reader question should a figure answer?
What is the scientific/statistical unit?
What is the estimand/quantity of interest?
What variation, pairing, uncertainty, or alternative explanation must be visible?
What plot/image/table/schematic family best exposes that evidence?
Does this deserve main-text space or support placement?
```

The writing skill may proactively propose figures/plots; `nature-figure` owns detailed rendering.

Examples of starting points:

- small-sample continuous groups -> individual observations/distribution;
- paired effect -> connected pairs/paired differences;
- time/dose/ordered parameter -> trajectory when order is meaningful;
- association -> scatter/hexbin with justified relation model;
- classification -> ROC/precision–recall/operating-point display according to the decision problem;
- calibration -> calibration/reliability curve, not discrimination alone;
- survival -> censoring-aware survival/cumulative-incidence display;
- heterogeneity -> forest/stratified effect display;
- ML benchmark -> per-task/site/run comparisons when variation matters, not just grand means;
- robustness -> sensitivity curves/intervals, usually support;
- imaging -> representative image plus quantitative evidence for population-level claims;
- null/negative result -> effect estimate + uncertainty/equivalence logic;
- qualitative/theory -> do not force quantitative plots.

Do not add a plot because analysis software generated it or top-tier papers commonly contain it.

## 4. Select section moves, not a universal skeleton

Load the requested section fragment. When the material does not fit its default pattern, or cross-disciplinary calibration matters, load `references/section-move-atlas.md`.

For each section:

1. Write the reader question the section must answer.
2. Select the minimum rhetorical moves needed.
3. Order moves so each creates a reason for the next.
4. Mark optional/recurrent moves rather than forcing every move once.
5. Check the final move hands the reader a useful next question.

Use `references/cross-disciplinary-writing-evidence.md` when deciding whether a proposed rule is robust or merely local to one discipline/corpus.

## 4a. Map paragraphs as nucleus + satellites

Each paragraph needs one **nucleus**: the proposition or reader task that makes it necessary.

Supporting **satellites** may include evidence, explanation, comparison, example, qualification, counterargument, implication, methodological reminder, or bridge.

Do not require one rhetorical function per paragraph. Split only when independent nuclei compete or parsing becomes difficult.

Record:

`nucleus -> supporting evidence/reasoning -> qualification if needed -> next-reader question`

## 4b. Alignment gate when framing is genuinely ambiguous

Use an alignment gate only when a wrong assumption would materially change the scientific argument.

Surface compactly:

- proposed argument spine;
- dominant contribution/evidence type;
- section move map;
- primary reader/audience;
- high-leverage assumptions not supplied by the author.

If immediate drafting is preferred, proceed with explicit placeholders/assumptions rather than inventing evidence.

## 5. Draft from evidence and reasoning outward

Keep claims near the evidence/reasoning that warrants them. Avoid claim stacks followed much later by support.

For Results, a useful block is often:

`question -> setup if needed -> observation/estimate -> evidence -> bounded local inference -> bridge`

Not every paragraph needs every element, and some disciplines defer most interpretation to Discussion.

For theory/humanities/qualitative work, use the corresponding proof, source, case, theme, interpretation, or analytic warrant rather than forcing quantitative evidence logic.

## 6. Build sentence dependency before polishing sentences

For a difficult paragraph, reduce each sentence to its proposition and map dependencies.

Example:

```text
S1 establishes A
S2 qualifies A under B
S3 explains why B changes interpretation C
S4 tests C against alternative D
S5 closes with bounded inference E
```

Then, for each sentence after the first:

`inherits X -> relation R -> adds Y -> enables Z`

If a sentence inherits nothing, has no meaningful relation, or could be moved almost anywhere without consequence, it may be an orphan sentence or generic mini-summary.

Load `references/paragraph-flow.md` for dependency-graph, handoff, and coherence repair.

## 7. Engineer information progression and identity chains

A useful default is given -> new:

`A -> B; B -> C; C -> D`

But this is not universal. Use constant-topic, derived-theme, contrast, question-answer, claim-evidence-boundary, or another defensible progression when needed.

Keep core entities trackable through **identity chains**:

- exact technical term repetition;
- stable abbreviation;
- precise demonstrative noun phrase;
- unambiguous pronoun;
- clearly marked subtype/category relation.

Do not rotate synonyms for central technical concepts merely to reduce repetition.

## 8. Realize the paragraph as natural scholarly prose

For substantial drafting/rewrite or prose that feels generic, over-smoothed, formulaic, connector-heavy, or machine-like, load `../../../nature-shared/core/natural-scholarly-prose.md`.

Use this hierarchy:

`scientific relation -> information flow -> lexical/reference continuity -> stance -> syntax -> connective -> cadence`

### Match syntax to rhetorical function

- chronological syntax for procedures when sequence matters;
- explicit clauses for new causal/conceptual relations;
- compact noun phrases for established technical concepts;
- parallel syntax for genuinely parallel evidence/functions;
- observation and interpretation separated when combination would inflate certainty;
- qualification integrated when subordination clarifies the boundary;
- main new information placed where rhetorical emphasis is recoverable.

Functional variation is natural. Random variation is not.

### Use precise conventional vocabulary

Choose vocabulary for field meaning, evidence strength, collocation, reader familiarity, and economy—not rarity.

Do not create `academic style` by synonymizing precise verbs, inflating nouns, or inserting generic prestige phrases.

### Use connectives only for real relations

Do not target connector density. Add explicit markers only when the relation would otherwise be difficult to recover.

### Run cadence audit last

After logic/stance are stable, check repeated openings, identical clause rhythms, buried verbs, noun stacks, abrupt boundaries, and generic closings.

Do not inject random short sentences, punctuation quirks, errors, or `burstiness` to appear human.

## 9. Calibrate epistemic stance to evidence

Distinguish observed, estimated, inferred, simulated, proved, hypothesized, associated, and causally identified claims.

Use the strongest verb warranted by evidence. Sweep unsupported `first`, `unique`, `unprecedented`, `comprehensive`, `complete`, `always`, and `never`.

Do not hide incrementality merely to make the contribution appear larger.

## 10. Run the reader-prediction, content, voice, and coherence audit

After each paragraph ask:

1. What should a competent skeptical reader now believe?
2. What question will that reader probably ask next?
3. Does the next paragraph answer or intentionally redirect it?
4. Is needed evidence/definition/comparison/qualification missing?
5. Can every sentence's position be justified through `inherits -> relation -> adds -> enables`?
6. Did repository/artifact detail enter the narrative without a scientific function?
7. Could any content be relocated to Methods/SI/availability/repository without weakening understanding?
8. Is a needed figure/plot missing because a central pattern is being described inefficiently in prose?

Then reverse-outline the section using paragraph nuclei.

If an author-voice profile is active, check stable terminology, recognizable agency/directness/cadence/signposting without preserving defects.

## 11. Re-voice after major structural/natural-prose repair

Natural scholarly prose is the quality floor. Author voice is the identity layer above it.

After major rewriting:

1. compare representative original/revised passages;
2. restore observed cadence, agency, technical density, signposting, terminology;
3. keep scientific/coherence repairs;
4. reject analogue wording leakage and generic journal cosplay;
5. verify no claim became stronger merely because prose became more fluent.

Never define voice through an AI-detector score, word blacklist, deliberate errors, or arbitrary sentence-length variance.

## 12. Apply journal and article-type adaptation last

Only after the scientific argument works, resolve exact journal/content type/stage using the shared resolver.

Journal adaptation may change audience assumptions, section labels, compression, title/abstract conventions, reference rendering, display allocation, and submission mechanics. It must not change evidence, causal strength, uncertainty, novelty boundary, limitations, or coherent author identity beyond what the target actually requires.

For broader venue/field tendencies beyond close analogues, load `references/target-corpus-calibration.md`.

## 13. Final anti-template / content-drift audit

Check for:

- repeated empty frames;
- connector-led paragraph glue without relation;
- generic `highlight/underscore` closings where a concrete consequence is available;
- ornamental vocabulary;
- repeated syntax with synonym substitution;
- depersonalized constructions hiding consequential author decisions;
- repository URLs/file paths/helper names in narrative without scientific necessity;
- exhaustive technical detail that belongs in Methods/artifact docs;
- redundant panels/plots;
- any change in causality, generality, certainty, novelty, limitation scope, or displayed uncertainty.

These are diagnostics, not banned phrases/objects.

## 14. Return prose plus decision-facing planning when useful

Return requested prose together with only notes that help revision.

For substantial manuscript planning/rewrite, also maintain compactly:

- **content-allocation ledger** — item -> function -> destination -> reason;
- **repository-leakage list** — artifact detail -> scientific abstraction/correct destination;
- **figure/plot suggestion ledger** — claim/question -> unit/estimand -> plot -> uncertainty/comparator -> main/support;
- **shortest evidence chain**;
- **important missing evidence/boundaries**.

Do not bury the prose under audit machinery unless the user asks for full detail.

## 15. Revise locally before rewriting globally

When the author redirects a draft:

- change affected claims/paragraphs unless the argument spine breaks;
- preserve Terminology Ledger and voice invariants;
- replace/compress rather than accumulate duplicated functions;
- rerun stance/coherence/content-allocation checks locally;
- rebuild argument/move/figure plans if the premise changes;
- drop invalid analogue-derived assumptions rather than forcing conformity.

Revision should strengthen the argument without reviewer-driven prose accretion, repository leakage, target-corpus cloning, or machine-like generic smoothing.
