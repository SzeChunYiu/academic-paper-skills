# Atomic Audit and Redesign of `academic-paper-skills`

**Repository:** `SzeChunYiu/academic-paper-skills`  
**Audit snapshot:** commit `fefc3f138e9ad30a56e35f50cc44f06850ccc89d` on `main`  
**Commit date:** 2026-08-25  
**Audit date:** 2026-08-26  
**Scope:** all 22 top-level skills; the canonical writing and pipeline skills; all shared core contracts; all section routers; principal manifests, tests, CI workflows, architecture documents, and research-evidence documents; current external reporting, transparency, provenance, authorship, AI-use, accessibility, and reproducibility standards.

---

## 1. Executive verdict

This repository is already far beyond a generic “write an academic paper” prompt collection. Its strongest contribution is a coherent set of **reasoning-level writing controls**:

- truth is separated from style and journal fit;
- papers are represented as question/tension → contribution → evidence → boundary → meaning;
- sections are move graphs rather than rigid templates;
- paragraphs are nuclei with supporting submoves;
- sentence flow is modeled through dependency and information progression;
- citations, figures, review comments, revisions, and release states receive explicit treatment;
- unsupported claims and manuscript-surface defects are intended to fail closed.

The central limitation is that the system is still primarily a **manuscript-development system**. It is not yet a complete **research-to-publication assurance system**. It becomes strongest after evidence and results already exist, but it lacks equally rigorous machinery for:

1. specifying the research question, estimand, hypotheses, units, and decision criteria;
2. designing and versioning protocols, preregistrations, statistical analysis plans, and deviations;
3. validating and versioning data, code, environments, and computational outputs;
4. tracing each claim through analysis objects or source passages to the underlying research artifacts;
5. distinguishing author-attested consistency, computational reproduction, independent verification, and external replication;
6. resolving reporting requirements by study design and result type;
7. testing manuscript intelligence behaviorally and adversarially rather than checking only whether instruction phrases exist.

The recommended destination is therefore not a larger writing prompt. It is a modular **academic-paper operating system** with a stable scientific core, study/design adapters, venue adapters, utility tools, machine-readable state, and executable assurance gates.

### Keep, revise, add, separate

| Decision | Components |
|---|---|
| **Keep as core intellectual assets** | atomic-claim verification; explanatory sufficiency; argument spine; move-based section reasoning; natural scholarly prose; author voice; analogue calibration; figure-evidence planning; concern IDs; revision closure; journal resolver; manuscript-surface QA |
| **Revise** | binary readiness semantics; duplicate taxonomies; duplicate routers; five-type paper taxonomy; fixed analogue sample counts; target-centric terminal state; chat-only state; phrase-presence tests |
| **Add** | research contract; estimand/design layer; protocol/SAP/preregistration; deviation ledger; data QA and provenance; reproducible analysis objects; unified claim provenance; reporting-guideline resolver; full declaration and accessibility layers; post-publication version/correction logic |
| **Separate from canonical science core** | daily literature recommender; downloader; Paper-to-PPT; Image-to-PPT; Paper-to-Patent; other delivery utilities |

---

## 2. Audit panel and how disagreements were resolved

This audit used a five-lens expert panel. These are analytical roles, not claims of human co-authorship.

| Lens | Background represented | Primary responsibility |
|---|---|---|
| **Research methodologist and statistician** | study design, estimands, bias, uncertainty, causal reasoning, robustness | ask whether the study design and analysis can support the manuscript’s claims |
| **Academic rhetoric and genre specialist** | cross-disciplinary rhetorical moves, paragraph/sentence cohesion, disciplinary variation | ask whether readers can reconstruct the argument without forcing one genre template |
| **Evidence and citation specialist** | systematic searching, source appraisal, metadata, passage grounding, entailment | ask whether each literature claim is supported by the cited source and whether the evidence landscape is fairly represented |
| **Reproducibility, ethics, and open-science specialist** | protocols, data/code stewardship, provenance, authorship, conflicts, AI use, accessibility, corrections | ask whether the research record is inspectable, accountable, reusable, and safe |
| **Agent and editorial-system architect** | schemas, state machines, test fixtures, routing, CI, reviewer isolation | convert scientific and rhetorical rules into deterministic state, interfaces, and tests |

The panel’s central disagreement was whether the solution should be a universal checklist. The resolution is:

> The core should encode universal **invariants**—truthfulness, traceability, explicit uncertainty, accountability, and readable reasoning. Study-type, discipline, reporting-standard, and venue requirements should be **adapters**, not universal prose templates.

A second disagreement concerned verification. Requiring independent verification of every underlying datum before any manuscript can be “ready” is scientifically admirable but operationally impossible for many editing tasks. The resolution is:

> Readiness must expose an **assurance profile**, not collapse all confidence into one binary label. Internal consistency, artifact traceability, computational reproduction, independent verification, and external replication are different states.

---

## 3. Repository coverage

The audit covered these 22 top-level skills:

1. `academic-paper-pipeline`
2. `academic-writing`
3. `nature-academic-search`
4. `nature-citation`
5. `nature-data`
6. `nature-downloader`
7. `nature-experiment-log`
8. `nature-figure`
9. `nature-image2ppt`
10. `nature-literature-pipeline`
11. `nature-paper-card`
12. `nature-paper-to-patent`
13. `nature-paper2ppt`
14. `nature-polishing`
15. `nature-proposal-writer`
16. `nature-reader`
17. `nature-ref-verifier`
18. `nature-response`
19. `nature-reviewer`
20. `nature-shared`
21. `nature-statistics`
22. `nature-writing`

The deepest read was applied to the scientific/writing path:

- `skills/academic-writing/**`
- `skills/academic-paper-pipeline/**`
- `skills/nature-writing/**`
- `skills/nature-shared/core/**`
- `skills/nature-reviewer/**`
- `skills/nature-response/**`
- `skills/nature-polishing/**`
- `skills/nature-academic-search/**`
- `skills/nature-paper-card/**`
- `skills/nature-citation/**`
- `skills/nature-ref-verifier/**`
- `skills/nature-statistics/**`
- `skills/nature-data/**`
- `skills/nature-experiment-log/**`
- `skills/nature-figure/**`
- representative tests and all relevant CI workflows;
- `docs/academic-writing-research_EN.md`;
- `docs/all-journals-architecture.md`;
- the cross-disciplinary writing evidence and section move atlas.

Utility implementations were assessed architecturally and through their public contracts; this audit was not a line-by-line security review of every downloader or presentation-conversion implementation.

---

## 4. What the repository already does unusually well

### 4.1 Truth precedes style

The canonical writing skill explicitly routes scientific validity before rhetorical realization, author voice, journal objectives, and formatting. This prevents a common failure mode in which “polishing” silently strengthens a causal, generalizability, novelty, or performance claim.

**Preserve this invariant unchanged.**

### 4.2 The argument spine is compact and generalizable

The sequence

`question/tension → contribution → evidence chain → boundary → meaning`

works across empirical, methodological, theoretical, qualitative, resource, review, and interpretive papers. It is appropriately abstract: it describes the job of a scholarly argument without imposing IMRaD.

**Promote this to the canonical project schema.** Every section and figure should declare which node or edge of this spine it serves.

### 4.3 Paragraph and sentence reasoning is research-informed

The repository rejects simplistic rules such as “one paragraph has one function,” “all Results paragraphs must be conclusion-first,” “short sentences are always better,” and “more transitions create more flow.” Its nucleus/satellite model and sentence dependency test are among its best assets.

**Compile these into diagnostics rather than adding more prose rules.**

### 4.4 Atomic-claim verification is the correct unit of integrity

The atomic claim contract preserves qualifiers, comparators, negation, conditions, scope, and quantifiers. This is exactly the level at which unsupported inference usually enters a paper.

**The ledger should become machine-readable and graph-linked, but the conceptual contract should remain.**

### 4.5 Explanation is treated separately from verbosity

The explanatory-sufficiency dimensions—identity, purpose, mechanism, evidence, boundary, and connection—correctly identify why technically accurate prose can still be scientifically insufficient.

**Retain these dimensions as section- and archetype-conditioned checks.**

### 4.6 Figures are evidence units, not decorations

The figure planning and figure skill already ask what a figure proves, what comparator and uncertainty it exposes, and why it belongs in the main text.

**Add computational lineage and accessibility; do not replace the evidence-first design logic.**

### 4.7 Review and revision use persistent concern IDs

The reviewer/response architecture separates triage, independent reviewer roles, editor synthesis, concern identity, closure route, and manuscript change. This is far stronger than generating generic reviewer comments or verbose rebuttals.

**Preserve concern identity across all project state.**

### 4.8 Journal routing is appropriately subordinate to scientific validity

The architecture correctly treats exact journal rules as compliance constraints rather than scientific truth. This is essential for journal transfer and prevents prestige contamination.

**Scientific assurance and target readiness should now become two separate machine-readable objects.**

---

## 5. The 12 highest-value gaps

### Gap 1 — No research contract before prose

The argument spine is necessary but not sufficient. The system needs a pre-writing research contract with:

- research question/tension;
- contribution class;
- unit of observation;
- unit of inference;
- population/domain/corpus;
- intervention/exposure/phenomenon;
- comparator/alternative account;
- outcome/evidence criterion;
- estimand or target quantity;
- hypotheses or interpretive propositions;
- intended headline claims;
- claim boundaries;
- decisive evidence required;
- abort/narrow/reframe rules.

This lets the pipeline distinguish “the manuscript is unclear” from “the design cannot answer the question.”

### Gap 2 — No first-class protocol, analysis plan, or deviation state

The pipeline needs versioned protocol and analysis-plan objects. Final Methods prose must be a projection of these objects, not the authority itself.

Required states include:

- draft/frozen/amended/superseded protocol;
- registration status and identifier;
- statistical/computational analysis plan;
- date and actor of deviations;
- affected outcomes/claims;
- inferential consequences;
- manuscript disclosure location.

This is the only reliable way to distinguish prespecified, exploratory, and post hoc analyses across revision rounds.

### Gap 3 — Data availability is not data governance

An availability statement cannot substitute for an authoritative data asset. Each data object should carry:

- identity and version;
- owner/controller;
- access status and reason;
- license;
- sensitivity and consent constraints;
- schema/data dictionary;
- units, keys, and identifiers;
- acquisition/generation;
- inclusion/exclusion lineage;
- transformation lineage;
- checksums or immutable snapshot identity;
- validation reports;
- known defects.

The availability paragraph should be generated from this record.

### Gap 4 — No executable analysis object

A statistics-reporting skill cannot repair a design-to-analysis mismatch after the fact. The system needs analysis objects with:

- analysis-plan link;
- prespecified/deviation/exploratory status;
- question/estimand;
- input data snapshot;
- exclusions/filters;
- code/workflow and version;
- environment and lockfile/container;
- hardware if relevant;
- seeds/nondeterminism;
- model/test/proof/interpretive method;
- diagnostics;
- robustness/sensitivity;
- exact outputs;
- execution receipt and input/output hashes;
- reproducibility status.

### Gap 5 — Source grounding is split across three systems

The repository separately handles bibliographic identity, paper/page grounding, and claim verification. They should be one provenance graph with three independent status dimensions:

1. source identity;
2. locator grounding;
3. semantic entailment.

A correct DOI does not establish that the source supports the claim; a relevant passage does not establish that the inference is proportional; a claim can be supported by a source that has later been corrected or retracted.

### Gap 6 — No analysis object connects data to prose and figures

Each reported result should point to a versioned analysis object containing:

- question/hypothesis/estimand;
- prespecified or exploratory status;
- input data snapshot and exclusions;
- code/notebook/workflow version;
- software/environment lock;
- random seeds and nondeterminism statement;
- model/test specification;
- diagnostic and robustness outputs;
- exact result values;
- generated tables/figures;
- execution receipt and checksums.

Without this, figure and Results consistency can be checked only manually.

### Gap 7 — Readiness is too binary

The atomic claim contract’s fail-closed posture is valuable, but one terminal `verification-complete` state risks conflating different achievements. The system should report separate dimensions:

- manuscript internal consistency;
- literature metadata verification;
- passage/locator verification;
- semantic entailment verification;
- protocol traceability;
- data provenance completeness;
- computational rerun;
- independent reproduction;
- external replication or triangulation;
- target-submission compliance.

A manuscript may be ready for author review while not independently reproduced; it may be computationally reproducible while based on a weak design; it may be scientifically sound but not formatted for a target journal.

### Gap 8 — Two taxonomies and duplicate routers can disagree

The shared core includes a rich archetype atlas, while the legacy writing manifest still exposes a five-type taxonomy. Resource, qualitative, systematic-review, clinical, theory, and hybrid papers can be routed differently depending on entry point.

Make the archetype atlas canonical. Treat any simpler taxonomy only as a coarse supertype. Classify at three levels:

- paper-level dominant and secondary archetype;
- study-level archetype;
- result/claim-level evidence type.

### Gap 9 — Section guidance is rhetorical but not executable

The section move atlas is strong, but the router does not enforce machine-readable contracts. Each section needs:

- reader question;
- required inputs;
- allowed claim classes;
- forbidden upgrades;
- reporting-guideline hooks;
- cross-section invariants;
- traceability links;
- objective exit tests;
- not-applicable rationale.

This allows two agents to make comparable decisions and enables schema validation.

### Gap 10 — Important manuscript parts are not first-class routes

The current main section routes omit or under-model:

- keywords and indexing terms;
- highlights;
- graphical abstract;
- plain-language summary;
- dedicated limitations layer;
- protocol/registration statement;
- data, code, software, model, and materials availability;
- ethics/consent;
- author contributions;
- conflicts and funding;
- acknowledgements;
- AI-use disclosure;
- supplementary information;
- accessibility/alt text;
- version/correction provenance;
- post-publication amendment.

These are not cosmetic appendices; many affect trust, reuse, accountability, and interpretation.

### Gap 11 — The tests mostly validate text presence, not scientific behavior

The canonical and pipeline tests largely assert that required markers exist in Markdown. CI is strong for utility execution, metadata, and file consistency, but the highest-risk manuscript behaviors are not exercised.

A scientifically meaningful test suite needs adversarial manuscript fixtures with expected:

- atomic claims;
- provenance links;
- blockers;
- severity;
- repair route;
- assurance state;
- release decision.

### Gap 12 — Scientifically normative components and delivery utilities share one product surface

PPT reconstruction, paper-to-PPT, patent drafting, downloading, and a daily literature recommender are useful, but they should consume a validated research record rather than define the paper-writing core. The daily recommender’s fixed weighted ranking, including “journal quality,” is especially unsuitable as a manuscript evidence-selection policy.

Separate:

- **scientific core**
- **discipline/study adapters**
- **venue adapters**
- **evidence/search tools**
- **downstream communication/IP utilities**

---

## 6. Full research-to-publication lifecycle audit

Legend:

- **Strong** — conceptually mature and broadly usable;
- **Partial** — useful components exist but lack coverage, schema, or integration;
- **Weak** — narrow or mostly prose-level;
- **Missing** — no canonical capability;
- **Conflict** — multiple components can produce incompatible routing or policy.

| Lifecycle stage | Status | Existing assets | Atomic missing capabilities |
|---|---|---|---|
| 0. Governance, confidentiality, and intake | Weak | ethics text; truth boundary; target resolver | confidentiality label; permitted AI processing; data/manuscript sensitivity; authorship authority; decision owner; regulatory constraints; conflict check |
| 1. Research question and contribution contract | Partial | argument spine; contribution classes; paper archetypes | estimand; unit of inference; scope/population; comparator/alternative; decision criteria; feasibility; minimum evidence contract |
| 2. Evidence landscape and novelty positioning | Partial | academic search; citation; paper card; analogue calibration | reproducible screening state; living search; contradiction graph; systematic-review mode; retraction/version status; saturation/stopping criteria |
| 3. Study design and protocol | Missing | archetype prompts; some compliance checks | generic protocol schema; design rationale; sampling frame; outcome/variable plan; protocol version; registration; SAP; deviation process |
| 4. Ethics, consent, governance, and contribution planning | Partial | ethics/compliance text | ethics record object; approvals and amendments; consent/data governance; CRediT agreement; funding/COI ledger; AI-use plan |
| 5. Study conduct and experimental record | Weak | experiment-log template | audit trail; calibration/QC; randomization/blinding execution; intervention fidelity; adverse events; protocol deviations; raw-data hashes |
| 6. Data management and quality | Weak | availability-statement skill | data dictionary; validation rules; provenance; transformation log; access/license/sensitivity; immutable snapshots; partition integrity |
| 7. Analysis and computation | Weak/Partial | statistics reporting/review; figure scripts | estimand-to-model mapping; SAP execution; clean environment; checksums; diagnostics; missingness; multiplicity; robustness; computational receipt |
| 8. Claim, evidence, and figure architecture | Strong | atomic claims; explanation; content allocation; figure planning | unified graph; result-to-protocol status; analysis object links; assurance dimensions |
| 9. Section architecture and drafting | Strong/Partial | move atlas; section fragments; natural prose; voice | section schemas; missing front/back matter; adapter-conditioned exit tests; semantic diff |
| 10. Citation and source integrity | Partial/Strong | metadata verification; paper cards; citation tools | identity+locator+entailment unification; retractions/corrections; source version; conflicting evidence synthesis |
| 11. Internal assurance and independent review | Strong/Partial | reviewer engine; concern IDs; decision closure | immutable review packet; calibrated rubrics; reproducibility reviewer; conflicts; behavioral tests; evidence of reviewer independence |
| 12. Revision and response | Strong | response skill; closure routes; consistency sweep | automated manuscript/ledger delta; claim-strength regression; state migration; response-to-change verification |
| 13. Journal projection and submission package | Partial/Strong | journal resolver; submission-package output | completed reporting checklist object; machine-readable declarations; artifact deposit verification; accessibility gate |
| 14. Release, versioning, and post-publication | Missing/Weak | surface QA; some version language | release manifest; version relations; correction/retraction/update workflow; living review/search updates; durable project crate |

---

## 7. Skill-by-skill atomic audit

### 7.1 `academic-paper-pipeline`

**Role now:** canonical closed-loop manuscript orchestrator.

**Strong**

- persistent conceptual state;
- editorial/reviewer loop;
- concern IDs and closure;
- fail-closed language;
- target-specific readiness is explicitly a simulation.

**Gaps**

- begins at manuscript development, not study conception;
- ledgers are instructions rather than validated schemas;
- scientific assurance and journal readiness remain too coupled;
- no protocol/data/analysis objects;
- no clean handoff bundle;
- tests largely check phrases.

**Disposition:** keep and elevate to the sole orchestrator. Rename the internal state from “manuscript state” to “research-paper state.”

**Required change:** the orchestrator must refuse to infer missing scientific objects, but it should still support manuscript-only mode by labeling upstream state `AUTHOR_ATTESTED` or `NOT_AVAILABLE`, not by pretending it was independently verified.

---

### 7.2 `academic-writing`

**Role now:** canonical journal-agnostic writing/restructuring engine.

**Strong**

- truth boundary;
- argument spine;
- archetype routing;
- atomic verification;
- explanation, content selection, figure planning, natural prose, and target-last hierarchy.

**Gaps**

- section contracts are prose;
- front/back matter is incomplete;
- output is optimized for interactive coaching rather than durable state;
- readiness language does not expose assurance dimensions;
- it still depends heavily on the legacy `nature-writing` asset tree.

**Disposition:** keep as the writing engine, but make it consume canonical project-state objects and emit versioned section artifacts plus semantic deltas.

---

### 7.3 `nature-academic-search`

**Role now:** reproducible search planning and execution support.

**Strong**

- publication-ecology awareness;
- query planning;
- evidence-first intent;
- reproducibility language.

**Gaps**

- no canonical screening/deduplication/inclusion state;
- no search peer review or query validation;
- no living-search update record;
- no retraction/correction/version status;
- no result-level risk-of-bias or certainty link;
- ordinary literature support and systematic evidence synthesis are not clearly separated.

**Disposition:** migrate to `academic-search` and add modes:

- `background-context`
- `claim-support`
- `analogue-calibration`
- `systematic-evidence-synthesis`
- `living-update`

Each mode needs different completeness claims and stopping rules.

---

### 7.4 `nature-citation`

**Role now:** source discovery, metadata handling, and bibliography export.

**Strong**

- evidence selection is separated from rendering;
- avoids default prestige filtering;
- metadata/export utilities are practical.

**Gaps**

- citation identity is not enough to establish claim support;
- no source-version/correction/retraction state;
- no assertion-level citation span;
- no explicit primary-versus-secondary source rationale;
- no balance/contradiction ledger.

**Disposition:** retain as a bibliographic service inside the unified provenance layer.

---

### 7.5 `nature-data`

**Role now:** data-availability drafting.

**Strong**

- prevents invented access claims;
- distinguishes access conditions.

**Gaps**

- not a data-management skill;
- no data dictionary, QA, version, checksum, license, governance, transformation, or lineage;
- availability prose is not generated from an authoritative asset record.

**Disposition:** replace with a broader `research-data` skill. Keep availability generation as one output mode.

---

### 7.6 `nature-downloader`

**Role now:** source acquisition and file retrieval.

**Strong**

- practical retrieval workflow;
- tests and runtime engineering;
- useful input to paper cards.

**Gaps**

- scientifically normative policy is mixed with access mechanics;
- source preference rules can be language/region specific;
- no universal hash/version/license receipt required at ingestion;
- not part of paper reasoning.

**Disposition:** move under `utilities/source-acquisition`; emit an immutable acquisition receipt consumed by the source ledger.

---

### 7.7 `nature-experiment-log`

**Role now:** Markdown experimental logging.

**Strong**

- recognizes that experimental context must be captured;
- useful for laboratory-style notes.

**Gaps**

- materials-oriented rather than cross-disciplinary;
- no protocol version, deviation, calibration, operator, randomization/blinding execution, adverse event, raw-data hash, or chain of custody;
- no structured link to manuscript Methods or Results.

**Disposition:** replace with a generic `study-conduct-log` plus discipline adapters.

---

### 7.8 `nature-figure`

**Role now:** scientific figure design and production guidance.

**Strong**

- figure-as-evidence contract;
- comparator, uncertainty, and statistical-unit awareness;
- visual and production QA.

**Gaps**

- no mandatory analysis/data/code lineage;
- no deterministic regeneration receipt;
- image-integrity checks are not generalized;
- accessibility and long descriptions are not first-class;
- source-data package is not a canonical artifact.

**Disposition:** keep; add `figure_spec`, `analysis_id`, `data_snapshot_id`, `render_receipt`, `alt_text`, `long_description`, and `source_data_asset_id`.

---

### 7.9 `nature-image2ppt`

**Role now:** editable reconstruction of presentation slides from images.

**Disposition:** downstream utility. It should never be loaded by the canonical paper-writing router unless explicitly requested.

---

### 7.10 `nature-literature-pipeline`

**Role now:** daily discovery and ranked digest.

**Strong**

- useful personal awareness workflow;
- repeatable intake and ranking structure.

**Gaps**

- fixed weighted scoring can hide uncertainty;
- “journal quality” can reintroduce prestige bias;
- topical recommendation is not evidence synthesis;
- top-k ranking can create false completeness.

**Disposition:** rename and quarantine as `literature-recommender`. Its outputs must be labeled discovery leads, never a manuscript evidence base without a separate search/screen/appraisal process.

---

### 7.11 `nature-paper-card`

**Role now:** grounded structured reading of individual papers.

**Strong**

- distinguishes page-grounded, structure-grounded, and source-limited states;
- blocks invented page locations;
- useful bridge from source to synthesis.

**Gaps**

- no canonical design-specific extraction;
- no result-level risk-of-bias/applicability;
- no source checksum/version;
- no correction/retraction link;
- no explicit claim-entailment relation;
- no extraction conflict/adjudication state.

**Disposition:** keep as the source-object constructor, extended by archetype-specific extraction schemas.

---

### 7.12 `nature-paper-to-patent`

**Disposition:** downstream IP utility. It should consume a validated contribution/evidence/boundary bundle and remain outside the canonical academic-paper core.

---

### 7.13 `nature-paper2ppt`

**Disposition:** downstream communication utility. It should consume the claim/figure/section graph and record any simplification or claim compression.

---

### 7.14 `nature-polishing`

**Role now:** layered scientific and linguistic editing.

**Strong**

- truth-preserving editing;
- style and target adaptation occur after logic;
- rejects detector-oriented “humanization.”

**Gaps**

- overlaps heavily with `academic-writing`;
- no automated semantic diff;
- no claim-strength or qualifier regression check;
- no invariant that every changed number/citation/identifier is ledger-backed.

**Disposition:** merge into `academic-writing` as `mode=revise|polish|target-adapt`.

---

### 7.15 `nature-proposal-writer`

**Role now:** proposal/project development with section contracts and research canon.

**Strong**

- recognizes upstream project state;
- section-contract concept;
- evidence and argument planning;
- useful precursor to a paper.

**Gaps**

- separate state model from the paper pipeline;
- arbitrary numeric readiness thresholds;
- AI-detection/avoidance concepts should not be quality gates;
- external calibration steps need reproducible records;
- proposal-to-study-to-paper lineage is not preserved.

**Disposition:** salvage its project-state and section-contract ideas, merge them into the canonical research contract, and remove arbitrary scores/detector-oriented gates.

---

### 7.16 `nature-reader`

**Role now:** paper-reading workflow.

**Strong**

- staged reading;
- useful coordination with paper cards.

**Gaps**

- one reading sequence can be over-universal;
- no explicit question-driven extraction plan;
- no contradiction/evidence graph;
- no design-specific bias/applicability;
- no reader disagreement/adjudication.

**Disposition:** integrate with paper-card modes: `triage`, `claim-check`, `method-reconstruction`, `systematic-extraction`, and `analogue-study`.

---

### 7.17 `nature-ref-verifier`

**Role now:** bibliographic reference verification.

**Strong**

- metadata identity and cross-file consistency;
- prevents malformed references.

**Gaps**

- identity is not support;
- no retraction/correction/updated-version check;
- no preprint-to-version-of-record relation;
- no duplicate-work/entity resolution;
- no source-type appropriateness.

**Disposition:** merge with citation and paper-card provenance while preserving a separate metadata-verification status.

---

### 7.18 `nature-response`

**Role now:** reviewer-response and revision closure.

**Strong**

- concern-by-concern closure;
- multiple legitimate closure routes;
- response prose is subordinate to manuscript change;
- editorial decision continuity.

**Gaps**

- manuscript and ledger changes are not mechanically diffed;
- concern closure can be asserted without executing a semantic invariant check;
- no explicit evidence that a changed claim remains supported elsewhere;
- response package is not one canonical release object.

**Disposition:** keep; require `concern → action → artifact delta → re-verification → closure evidence`.

---

### 7.19 `nature-reviewer`

**Role now:** editor/reviewer simulation.

**Strong**

- separates editor triage and blind reviewers;
- avoids vote counting;
- records decision-relevant concerns;
- target criteria are resolved.

**Gaps**

- reviewer independence is instructed, not technically enforced;
- no immutable input packet hash;
- no calibrated gold/adversarial reviews;
- fixed panel structures can be over-rigid;
- no explicit reviewer conflict/competence profile;
- simulated acceptance risk must remain clearly distinct from scientific assurance.

**Disposition:** keep, but split:

- `scientific-assurance-review`
- `target-editorial-simulation`

Only the latter predicts fit/priority.

---

### 7.20 `nature-shared`

**Role now:** common knowledge and contracts.

**Strong**

- the repository’s intellectual center;
- rich evidence, reasoning, QA, and review contracts;
- cross-disciplinary and counterexample-aware.

**Gaps**

- monolithic and heavily prose-based;
- old and new taxonomies coexist;
- generic and Nature-specific compliance are mixed;
- contracts are duplicated across routers;
- no formal schema/version/migration system;
- policy provenance and review dates are not uniformly machine-readable.

**Disposition:** split into:

- `core/invariants`
- `schemas`
- `adapters/archetypes`
- `adapters/reporting-guidelines`
- `adapters/disciplines`
- `adapters/venues`
- `policy-snapshots`
- `validators`

---

### 7.21 `nature-statistics`

**Role now:** statistical reporting and manuscript review.

**Strong**

- warns against common reporting errors;
- keeps statistics proportional to evidence.

**Gaps**

- no study-design planning;
- no estimand;
- no power/precision or sampling logic;
- no executable analysis plan;
- no missingness/multiplicity/diagnostic framework;
- no computational lineage;
- limited treatment of causal inference, prediction, qualitative quantification, or complex dependence.

**Disposition:** expand into `analysis-and-inference`, with adapters rather than one universal statistics checklist.

---

### 7.22 `nature-writing`

**Role now:** legacy rich writing asset tree and support-only router.

**Strong**

- section move atlas;
- empirical writing research;
- rhetorical engine;
- paragraph/sentence/voice assets;
- full target and review integration.

**Gaps**

- duplicates the canonical skill;
- legacy name obscures scope;
- five-type taxonomy conflicts with the archetype atlas;
- missing section routes;
- large context surface and repeated policies invite drift.

**Disposition:** freeze as a compatibility facade. Move authoritative assets under neutral shared paths and make `academic-writing` the only triggerable writer.

---

## 8. Proposed canonical architecture

```text
skills/
  academic-paper-pipeline/        # sole orchestrator
  academic-writing/               # section planning, drafting, revision
  academic-search/                # background, claim support, systematic modes
  academic-source/                # acquisition, paper card, metadata, entailment
  research-design/                # question, estimand, protocol, sampling, SAP
  research-data/                  # data assets, QA, governance, snapshots
  analysis-and-inference/         # analysis objects, diagnostics, robustness
  scientific-figure/              # evidence specs, rendering, source data, access
  scientific-review/              # assurance review and concern closure
  academic-submission/            # target projection and package
  academic-shared/
    invariants/
    schemas/
    adapters/
      archetypes/
      reporting-guidelines/
      disciplines/
      venues/
    validators/
    policy-snapshots/
  utilities/
    source-acquisition/
    literature-recommender/
    paper-to-ppt/
    image-to-ppt/
    paper-to-patent/
```

### Core invariants

The scientific core should be small and stable:

1. no claim stronger than its warrant;
2. every material assertion has identity, scope, status, and provenance;
3. every reported result has a reconstructable evidence-generation path;
4. prespecified and exploratory work are distinguished;
5. uncertainty, alternatives, and boundary conditions are visible;
6. every consequential change is versioned and attributable;
7. human actors retain accountability;
8. confidential inputs are processed only under an explicit permission policy;
9. venue rules cannot strengthen scientific claims;
10. release labels state exactly what was and was not verified.

### Adapter hierarchy

Resolution order:

1. exact study/result design;
2. reporting/risk-of-bias standard;
3. discipline/community convention;
4. paper archetype;
5. exact venue/content type/stage;
6. generic fallback.

A venue adapter may alter format, emphasis, limits, and placement. It may not alter the scientific assurance state.

---

## 9. Canonical research-paper state bundle

A serious project should persist, at minimum:

```text
paper-project/
  project.yaml
  research-contract.yaml
  reporting-profile.yaml
  protocol/
    protocol-v001.yaml
    analysis-plan-v001.yaml
    deviations.jsonl
  sources/
    source-ledger.jsonl
    search-runs.jsonl
    screening-decisions.jsonl
  data/
    data-assets.jsonl
    validation-reports/
  analyses/
    analysis-ledger.jsonl
    execution-receipts/
  claims/
    claim-ledger.jsonl
    support-edges.jsonl
  figures/
    figure-ledger.jsonl
    source-data/
    accessibility/
  manuscript/
    sections/
    manuscript-vNNN.md
    semantic-deltas.jsonl
  review/
    concerns.jsonl
    review-packets/
    responses/
  declarations/
    ethics.yaml
    contributions.yaml
    funding-conflicts.yaml
    ai-use.yaml
  release/
    assurance-report.json
    target-readiness.json
    release-manifest.json
  ro-crate-metadata.json
```

The accompanying YAML template in this audit provides a compact starting point.

---

## 10. Unified provenance graph

The graph should separate **entities**, **activities**, and **agents**.

### Core entity types

- research question;
- protocol and SAP versions;
- source document and source version;
- source passage/figure/table;
- data snapshot;
- code/workflow/environment;
- analysis result;
- figure/table;
- atomic claim;
- section/manuscript version;
- review concern;
- declaration;
- release report.

### Core activity types

- search;
- screening;
- extraction;
- data collection/generation;
- cleaning/transformation;
- analysis;
- figure rendering;
- drafting/editing;
- review;
- revision;
- verification;
- release.

### Core agent types

- author/contributor;
- analyst;
- extractor/reviewer;
- software/AI system;
- institution;
- funder;
- repository;
- journal/editorial actor.

### Mandatory high-value edges

```text
claim --supported_by--> source_passage
claim --supported_by--> analysis_result
claim --bounded_by--> limitation_or_assumption
analysis_result --answers--> question_or_estimand
analysis_result --implements--> analysis_plan_item
analysis_result --uses--> data_snapshot
analysis_result --generated_by--> code_environment_execution
figure --visualizes--> analysis_result
table --reports--> analysis_result
methods_statement --describes--> protocol_or_analysis_object
result_statement --reports--> analysis_result
discussion_statement --interprets--> claim
citation --identifies--> source_version
manuscript_version --revises--> prior_manuscript_version
concern --resolved_by--> artifact_delta
release_report --assesses--> manuscript_and_artifact_bundle
```

### Three independent source checks

Every literature-support edge must preserve:

1. **identity status** — does the work/version exist and match the citation?
2. **locator status** — can the supporting content be located?
3. **entailment status** — does that content support the exact claim at the stated strength and scope?

No single “verified citation” flag should replace these.

---

## 11. Assurance profile and release semantics

Use an assurance vector, then optionally summarize it with a class.

### Assurance dimensions

| Dimension | Example states |
|---|---|
| Claim coverage | incomplete / sampled / exhaustive |
| Author evidence consistency | unchecked / checked / conflicting |
| Source metadata | unverified / single-source / multi-source |
| Source locator | absent / structure-grounded / page-or-object-grounded |
| Source entailment | unchecked / partial / verified / contradicted |
| Protocol traceability | unavailable / author-attested / version-linked |
| Deviation transparency | unknown / recorded / reconciled |
| Data provenance | unavailable / described / snapshot+checksum |
| Computation | unavailable / traceable / rerun / clean-environment rerun |
| Independent verification | none / partial / complete for defined scope |
| External replication/triangulation | none / supportive / conflicting |
| Reporting compliance | unresolved / self-checked / independently checked |
| Target mechanics | unresolved / draft-ready / submission-ready |
| Accessibility | unreviewed / checked / validated |
| Confidentiality and AI-use | unresolved / compliant / blocked |

### Optional assurance classes

- **A0 — Draft only:** material upstream inputs are missing or unverified.
- **A1 — Manuscript-consistent:** claims are exhaustively mapped and consistent with author-provided evidence/source passages, but artifacts may not be independently checked.
- **A2 — Artifact-traceable:** protocol/data/code/analysis/figure versions are linked and deviations are visible.
- **A3 — Computationally reproduced:** defined results regenerate from the recorded data and procedures in a clean or controlled environment.
- **A4 — Independently verified:** an independent party verified the defined content/artifact scope.
- **A5 — Externally replicated or triangulated:** new evidence independently tests the central claim.

These classes are not a universal quality ranking. A qualitative or theoretical paper may require different evidence dimensions; a strong A1 manuscript can contain a valid noncomputational argument, while A3 does not rescue a biased study design.

### Separate target projection

Store target state independently:

- `not_resolved`
- `formatting_incomplete`
- `reporting_items_incomplete`
- `package_complete`
- `submission_ready_for_target`

Never infer scientific validity from target readiness or vice versa.

---

## 12. The proposed research-to-paper method

### Stage 0 — Establish authority, confidentiality, and operating mode

Record:

- who owns the scientific decisions;
- whether the work is public, internal, confidential, proprietary, or regulated;
- whether external AI processing is allowed;
- whether raw data/source material may be uploaded or quoted;
- intended output and target stage;
- which upstream artifacts exist.

Output: `project.yaml`.

### Stage 1 — Build the research contract

Specify:

- live question or tension;
- contribution class;
- unit of observation and inference;
- population/domain/corpus;
- intervention/exposure/phenomenon;
- comparator/alternative account;
- outcome/evidence criterion;
- estimand or target quantity, if applicable;
- hypotheses or interpretive propositions;
- claim boundaries;
- decisive evidence needed;
- abort/narrow/reframe criteria.

Output: `research-contract.yaml`.

### Stage 2 — Resolve archetype, design, and reporting profile

Classify at paper, study, and result levels. Select applicable reporting, design, bias, and artifact standards. Record not-applicable rationales.

Output: `reporting-profile.yaml`.

### Stage 3 — Design and freeze the protocol

Create the protocol, sampling/corpus strategy, variables/outcomes/coding rules, analysis plan, data-management plan, and ethics/governance record. Register or time-stamp when appropriate.

Output: versioned protocol/SAP plus registration reference.

### Stage 4 — Construct the evidence landscape

Choose search mode. Log databases/sources/platforms, queries, dates, limits, deduplication, screening, eligibility, exclusions, and stopping/saturation. Build contradiction and uncertainty maps, not only supportive citation lists.

Output: search and source ledgers.

### Stage 5 — Conduct the study and record deviations

Capture raw observations/source decisions, operators, instruments/software, quality controls, blinding/randomization execution, coding/adjudication, deviations, failures, and data lineage.

Output: conduct log and immutable data snapshots.

### Stage 6 — Execute analyses as versioned objects

Each analysis has a question, plan status, input snapshot, code/environment, diagnostics, exact output, and execution receipt. Separate confirmatory, exploratory, sensitivity, and post hoc analyses.

Output: analysis ledger and receipts.

### Stage 7 — Build the claim graph

Split all intended assertions atomically. Link each to an analysis result, source passage, proof step, or explicit author-attested premise. Record scope, boundary, contradiction, and assurance.

Output: exhaustive claim ledger.

### Stage 8 — Design figures and tables from decision needs

For each display, state what question it answers, what comparison or uncertainty it exposes, and which claim it supports. Link to source data and analysis version. Create accessibility descriptions.

Output: figure/table specifications and source-data package.

### Stage 9 — Plan sections with contracts

For each section, declare reader question, required inputs, moves, allowed claims, forbidden upgrades, cross-section dependencies, reporting hooks, and exit tests.

Output: section contract set.

### Stage 10 — Draft in evidence order, publish in reader order

A common empirical drafting order is:

`Methods/evidence objects → Results/figures → Discussion → Introduction/related work → Abstract → Title`

This is a default, not a universal rule. Theory, qualitative, humanities, resource, and review papers use archetype-specific draft orders.

Every sentence inherits a claim or rhetorical function; no polished prose is allowed to create a new unsupported scientific proposition.

### Stage 11 — Run integrity and completeness passes

Run:

- claim/support/entailment;
- method/result bidirectional traceability;
- statistics/analysis;
- citation identity and version;
- figure/table/prose consistency;
- terminology and numerical consistency;
- declarations and AI use;
- accessibility;
- confidentiality/project leakage;
- target reporting checklist.

Output: assurance report with blockers.

### Stage 12 — Conduct independent review

Freeze and hash the review packet. Use scientifically distinct reviewers where warranted: design/statistics, domain/evidence, reproducibility/artifacts, and rhetoric/readability. Do not expose editor conclusions to reviewers. Record conflicts and competence scope.

Output: concern ledger.

### Stage 13 — Revise by concern closure

For every concern:

`concern → diagnosis → closure route → artifact/manuscript delta → re-verification → closure evidence`

A response letter cannot close a scientific concern without the corresponding manuscript/artifact state.

### Stage 14 — Release and preserve

Generate:

- manuscript version;
- target package;
- completed reporting checklist;
- data/code/material declarations;
- contributor/funding/COI/AI records;
- accessibility assets;
- assurance profile;
- release manifest;
- version/provenance package.

Post-publication corrections, updates, and retractions must create linked versions rather than overwrite history.

---

## 13. Machine-readable section contract

Recommended generic schema:

```yaml
section_id: results.primary_outcome
applies_when:
  archetypes: [randomized_trial]
reader_question: "What was the prespecified primary effect and how uncertain is it?"
required_inputs:
  - protocol.primary_outcome
  - analysis.primary_effect
  - participant_flow
allowed_claim_classes:
  - descriptive
  - comparative
  - causal_within_randomized_contrast
forbidden_moves:
  - introduce_unreported_outcome
  - omit_denominator
  - convert_post_hoc_to_prespecified
  - infer_equivalence_from_non_significance
required_traceability:
  - methods_analysis_link
  - protocol_status_link
  - figure_or_table_link
reporting_hooks:
  - CONSORT_2025.outcomes_and_estimation
cross_section_invariants:
  - abstract_primary_result_matches
  - discussion_claim_strength_not_greater
exit_tests:
  - exact_effect_and_uncertainty_present
  - analysis_population_named
  - prespecified_status_explicit
  - harms_not_selectively_omitted
```

---

## 14. Section-by-section academic paper contracts

### 14.1 Title

**Scientific job**

Identify the durable object, relation/contribution, and necessary design or population qualifiers at the strength the evidence permits.

**Required inputs**

- central claim ID;
- contribution class;
- design/archetype;
- target community’s searchable terminology;
- causal/generalizability assurance.

**Allowed**

- descriptive relation;
- association;
- causal claim only under a defensible causal design;
- method/resource identity;
- theorem/result under stated assumptions;
- population/design label where omission would mislead.

**Forbidden**

- new claim not in the body;
- unsupported “novel,” “first,” “robust,” “general,” “effective,” or “safe”;
- hiding the actual population, simulation status, or retrospective design;
- “validation” when only internal testing occurred and the field treats the term ambiguously.

**Exit tests**

- exact title proposition exists in the claim ledger;
- no title term increases scope or certainty;
- main searchable entities are present;
- title remains true after all limitations are applied;
- target mechanics are satisfied without changing meaning.

---

### 14.2 Abstract

**Scientific job**

Provide the highest-value compressed representation of the paper’s question, design/approach, main evidence, bounded answer, and significance.

**Required inputs**

- locked primary results or core proof/synthesis;
- exact sample/data/corpus/setting;
- uncertainty or evidentiary basis;
- contribution and boundary;
- registration/resource information when required.

**Allowed moves**

- context/need;
- objective/question;
- design/approach;
- principal result(s);
- mechanism/interpretation if directly supported;
- bounded conclusion;
- availability/registration when central.

**Forbidden**

- result not reported in the body;
- stronger causal or generalizable wording than the body;
- choosing only the most favorable secondary result;
- treating absence of significance as equivalence or no effect;
- hiding simulation, internal testing, subgroup, or exploratory status.

**Exit tests**

- every number and named result has a body/analysis link;
- primary result receives priority;
- uncertainty and denominator appear where needed;
- conclusion is no stronger than Discussion;
- no undefined private term;
- word/structure rules are target-resolved.

---

### 14.3 Keywords and indexing terms

**Scientific job**

Make the paper discoverable under the concepts, methods, populations, and phenomena it actually studies.

**Required inputs**

- terminology ledger;
- controlled vocabularies where relevant;
- target index rules;
- title terms.

**Forbidden**

- adding fashionable methods or diseases not materially studied;
- using a broader population or causal term than the paper supports;
- treating keywords as a novelty claim.

**Exit tests**

- covers the core object, design/method, and outcome/phenomenon;
- terminology matches the body;
- controlled terms are used when appropriate;
- no misleading scope expansion.

---

### 14.4 Highlights, graphical abstract, and plain-language summary

**Scientific job**

Translate the same evidence for a different reading surface and audience.

**Required inputs**

- headline claims;
- limitations and uncertainty;
- audience literacy assumptions;
- accessibility requirements.

**Forbidden**

- promotional language stronger than the manuscript;
- omission of a boundary that changes practical interpretation;
- replacing uncertainty with an absolute statement;
- inaccessible image-only communication.

**Exit tests**

- each statement maps to a claim;
- no additional practical recommendation is introduced;
- plain-language terms preserve causal/statistical meaning;
- graphical claims have alt text and textual equivalent.

---

### 14.5 Introduction

**Scientific job**

Let readers understand why the question remains live and why this study or argument is an appropriate response.

**Required inputs**

- evidence landscape;
- contradiction/gap/tension map;
- contribution and scope;
- design rationale;
- relevant theory or mechanism.

**Core move families**

1. establish the territory;
2. create the research need;
3. synthesize and position prior work;
4. state the question/hypothesis/objective;
5. state the response/contribution and scope.

**Forbidden**

- fabricated scarcity (“few studies”) when the real need is different;
- citation lists without synthesis;
- absolute novelty unsupported by a reproducible search;
- criticizing prior work for questions it did not intend to answer;
- using journal prestige as evidence quality;
- introducing claims that never return in the paper.

**Exit tests**

- every factual literature claim has an entailment-checked source;
- the need follows from the evidence map;
- the present contribution addresses the stated need;
- hypotheses/objectives match protocol and Methods;
- scope terms match the population/data/design.

---

### 14.6 Related work or literature review

**Scientific job**

Map the intellectual decision space—approaches, assumptions, evidence, disagreements, trade-offs, and unresolved alternatives.

**Required inputs**

- search mode and coverage claim;
- eligibility/relevance criteria;
- source cards;
- comparison dimensions;
- contradiction and uncertainty map.

**Forbidden**

- author-by-author bibliography tour unless chronology is analytically necessary;
- “comprehensive” or “systematic” without reproducible methods;
- selective omission of counterevidence;
- inferring study quality from venue prestige;
- citing a review as if it were the primary experiment when primary evidence is required.

**Exit tests**

- paragraph nuclei are conceptual comparisons;
- representative sources are justified;
- contrary and null evidence is visible;
- coverage language matches search method;
- the final synthesis creates the exact research need.

---

### 14.7 Methods — overview

**Scientific job**

Make evidence generation, credibility, interpretation, and—where appropriate—reproduction possible.

Every consequential Methods statement should link forward to the Results/claims it governs. Every material Result should link back to a Methods object.

#### Design and setting

Record study design, temporal orientation, setting, sites/corpus/domain, recruitment/acquisition period, and rationale.

**Blockers:** vague design; retrospective/prospective ambiguity; target population mismatch; setting omitted when it affects transfer.

#### Population, sample, material, or corpus

Record sampling frame, inclusion/exclusion, recruitment/selection, unit of observation, unit of inference, clustering, repeated measures, attrition, and final analytic populations.

**Blockers:** denominators cannot be reconstructed; duplicate units; exclusion rules were created after seeing results without disclosure; corpus limits are hidden.

#### Variables, constructs, outcomes, labels, or evidence criteria

Define operationalization, measurement validity, outcome time points, label/reference-standard creation, coding rules, and adjudication.

**Blockers:** construct and measure are conflated; target leakage; labelers or adjudication unknown; primary outcome not identifiable.

#### Intervention, exposure, procedure, apparatus, or source treatment

Describe what was done, by whom/what, when, in what sequence, under what conditions, with fidelity/QC.

**Blockers:** critical parameters absent; comparator not reconstructable; protocol deviations hidden.

#### Sampling, power, precision, or information adequacy

Use the criterion appropriate to the design:

- statistical power or precision;
- saturation/information power;
- corpus coverage;
- theorem assumptions and counterexample search;
- benchmark size/diversity;
- resource completeness.

**Blockers:** retrospective sample-size justification presented as prospective; arbitrary threshold without rationale; analytic unit differs from power unit.

#### Data processing and quality

Record acquisition, cleaning, missingness, transformations, normalization, imputation, deduplication, exclusions, leakage prevention, train/test partitioning, and validation reports.

**Blockers:** preprocessing uses test information; outcome-aware exclusions undisclosed; units changed without record; missing data mechanism ignored when material.

#### Analysis and inference

Record estimand/question, model/test/proof/interpretive procedure, assumptions, software/environment, uncertainty, multiplicity, diagnostics, robustness, and prespecified/exploratory status.

**Blockers:** analysis cannot answer the stated question; model selected on test data; cluster dependence ignored; no primary analysis; post hoc analysis presented as confirmatory.

#### Controls, baselines, alternatives, and robustness

Specify negative/positive controls, comparator selection, ablations, sensitivity analyses, alternative explanations, falsification tests, and external evaluation.

**Blockers:** straw-man baseline; no relevant control; robustness claim based on cosmetic variations; external claim based on internal split.

#### Ethics, consent, registration, and governance

Record approval/waiver, consent, participant/community protections, registration, protocol/SAP access, sensitive data governance, and changes.

**Blockers:** missing required approval; contradictory approval IDs; undisclosed post-registration changes; confidential data exposed.

#### Reproducibility and resources

Record data/code/material/model availability, licenses, persistent identifiers, versions, checksums, environment, execution instructions, and access restrictions.

**Blockers:** availability statement points to absent or mismatched artifact; code cannot identify the analysis version; access restriction is misrepresented as open.

**Methods section exit tests**

- a knowledgeable reader can reconstruct the evidence-generation logic;
- all consequential choices have rationale or are standard and unambiguous;
- all primary Results have a Methods link;
- all Methods elements that imply an output have a forward link or explicit “not used” status;
- deviations and exploratory changes are visible;
- reporting-standard items are mapped, not merely mentioned.

---

### 14.8 Results

**Scientific job**

Report the evidence that answers the paper’s questions, with sufficient context, denominators, uncertainty, and bounded local inference.

**Robust result block**

`question → setup if needed → observation/estimate → evidence → bounded inference → bridge`

**Required inputs**

- analysis object;
- protocol/SAP status;
- data snapshot and analytic population;
- exact numerical/qualitative/proof evidence;
- figure/table object;
- uncertainty and diagnostics.

**Forbidden**

- causal wording unsupported by design;
- changing denominators silently;
- selective outcome or subgroup reporting;
- treating `p > threshold` as proof of no effect;
- reporting only accuracy without class distribution/calibration/decision context where material;
- calling an internal split external validation;
- hiding failed, null, or contradictory analyses that alter the conclusion;
- interpreting an embedding/visualization as mechanistic evidence without support.

**Exit tests**

- every result sentence maps to an analysis/source/proof object;
- prespecified versus exploratory status is explicit;
- sample/statistical unit and denominator are recoverable;
- effect size and uncertainty are present where applicable;
- figures/tables and prose agree exactly;
- local inference does not exceed the result;
- primary and adverse/negative outcomes are not selectively omitted.

---

### 14.9 Figures, tables, legends, and source data

**Scientific job**

Expose evidence structure, comparison, uncertainty, distribution, mechanism, or boundary efficiently and honestly.

**Required inputs**

- claim ID;
- analysis ID;
- data snapshot;
- visual question and decision role;
- statistical/sample unit;
- uncertainty representation;
- source-data asset;
- accessibility description.

**Forbidden**

- truncation or transformations that mislead;
- bar-only summaries that conceal distributions when individual data are decision-relevant;
- unmarked smoothing, exclusions, or composite construction;
- duplicated images presented as independent evidence;
- inconsistent color/label semantics;
- significance marks without test/adjustment details;
- figure generated from a different analysis version than the text.

**Exit tests**

- one can identify what the display supports and what it does not;
- axes, units, denominators, groups, and uncertainty are complete;
- legend is standalone and matches Methods;
- source data reproduce plotted values;
- render receipt identifies code/environment/input;
- alt text is brief and meaningful;
- complex figures have a longer textual description;
- accessibility text does not merely duplicate the caption.

---

### 14.10 Discussion

**Scientific job**

Interpret the findings, compare explanations and prior evidence, establish boundaries, and state proportional implications.

**Required inputs**

- locked claim graph;
- uncertainty/limitations;
- prior-work map;
- alternative explanations;
- external-validity analysis;
- practical/theoretical decision context.

**Allowed recursive cycle**

`finding → interpretation → comparison → alternative → qualification → implication`

**Forbidden**

- introducing new evidence;
- upgrading association to causation;
- treating a preferred mechanism as established when alternatives remain;
- universalizing beyond the sample/domain;
- hiding limitations in a ritual final paragraph;
- converting predictive performance into clinical utility without decision evidence;
- recommending policy/intervention beyond the design.

**Exit tests**

- central question receives a bounded answer;
- each major finding is interpreted at the correct assurance;
- alternatives and counterevidence are considered;
- limitations state their consequence for interpretation;
- generalizability is argued, not asserted;
- implications are proportional and identify unresolved work.

---

### 14.11 Limitations

Limitations may be integrated near claims and/or summarized in a dedicated section. The system should maintain a separate limitation object regardless of layout.

For each limitation record:

- source: design, sampling, measurement, analysis, missingness, bias, model, theory, source base, or reporting;
- affected claims;
- likely direction or nature of impact, if knowable;
- mitigation already applied;
- residual uncertainty;
- whether the claim must be narrowed, removed, or only qualified.

**Forbidden**

- generic ritual limitations with no consequence;
- limitation language that contradicts an unqualified title/abstract;
- “future work” used to avoid a current validity problem.

---

### 14.12 Conclusion

**Scientific job**

State the durable bounded answer that remains after all qualifications.

**Forbidden**

- new results;
- new causal or practical recommendation;
- aspirational impact presented as demonstrated;
- novelty adjective replacing a specific contribution.

**Exit tests**

- conclusion is derivable from verified headline claims;
- boundary is visible;
- no statement is stronger than the abstract or Discussion;
- it adds synthesis rather than mechanically repeating the abstract.

---

### 14.13 Data, code, software, model, materials, and protocol availability

These statements must be generated from asset records.

Each record includes:

- object type and identity;
- persistent identifier/location;
- exact version;
- license;
- access status and restrictions;
- reason for restriction;
- request process if applicable;
- checksum or repository version;
- relation to the reported analysis;
- embargo date if any;
- preservation status.

**Blockers**

- “available on request” without lawful/feasible process;
- claiming openness for restricted artifacts;
- dead/private repository;
- wrong version;
- missing license;
- artifact does not reproduce the reported scope.

---

### 14.14 Ethics, consent, and governance

Required fields are design-dependent, but the object should support:

- reviewing body and approval/waiver;
- identifier and date;
- consent/assent and exceptions;
- participant/community protections;
- animal welfare;
- sensitive data and indigenous/community governance where relevant;
- protocol amendments;
- dual-use or safety issues;
- institutional or legal restrictions.

The manuscript text is a projection of the authoritative record.

---

### 14.15 Authorship, contributions, funding, conflicts, acknowledgements, and AI use

**Contributions**

Use CRediT-compatible roles where relevant, but do not use CRediT to decide who qualifies as an author. Record contributor confirmation and responsibility.

**Funding and conflicts**

Record source, award, funder role in design/conduct/analysis/reporting, financial and nonfinancial relationships, and management.

**Acknowledgements**

Distinguish nonauthor contributions, permissions, and services.

**AI use**

Record:

- tool/model/service and version/date when available;
- purpose;
- inputs provided;
- whether confidential or personal data were processed;
- human verification;
- generated text/image/code/data role;
- disclosure location;
- target policy.

AI cannot be an author or accountable agent. Human authors retain responsibility.

---

### 14.16 Supplementary information

**Scientific job**

Provide necessary depth without hiding evidence required to evaluate headline claims.

**Required**

- stable identifiers and crosslinks;
- same terminology/numbering/versions as main text;
- complete methods, analyses, and source data where routed;
- independent accessibility and surface QA;
- clear status of exploratory material.

**Forbidden**

- moving a fatal limitation out of sight;
- placing the only definition of a primary outcome or key method in an inaccessible supplement;
- figures/tables produced from undocumented analysis versions.

---

### 14.17 References and citation surfaces

Every reference should have:

- canonical work identity;
- cited version;
- metadata verification status;
- correction/retraction/update status;
- source type;
- manuscript claim spans it supports;
- locator and entailment status;
- primary/secondary rationale;
- conflict/counterevidence relation where material.

A bibliography can be perfectly formatted and still scientifically wrong. Rendering is the final step.

---

### 14.18 Metadata, accessibility, and versioning

First-class objects should cover:

- author identifiers and affiliations;
- title/abstract/keywords/language;
- funder and award metadata;
- resource relations and versions;
- alt text and long descriptions;
- semantic table headers;
- transcripts for media;
- manuscript and artifact version links;
- correction, withdrawal, update, or retraction relations.

This is part of publication integrity, not merely production polish.

---

## 15. Study and paper archetype adapters

| Archetype/design | Primary research objects | Key additional checks | Reporting/assurance adapters |
|---|---|---|---|
| Randomized trial | protocol, allocation, intervention/comparator, outcomes, participant flow, SAP, harms | concealment, blinding, fidelity, attrition, outcome switching, effect and precision | SPIRIT 2025 for protocol; CONSORT 2025 for report |
| Observational causal study | target population, treatment strategies, time zero, confounders, estimand, identification assumptions | immortal-time bias, confounding, positivity, measurement, missingness, sensitivity | STROBE for reporting; TARGET when emulating a target trial; ROBINS-I when appraising nonrandomized intervention evidence |
| Descriptive/associational observational study | sampling frame, measures, time, population, association estimand | selection, measurement, clustering, multiplicity, overcausal language | STROBE and relevant extensions |
| Diagnostic/prognostic/prediction model | intended use, target population, predictors, outcome/reference standard, model development/evaluation | leakage, overfitting, calibration, discrimination, subgroup performance, external testing, fairness, utility | TRIPOD+AI; PROBAST+AI; CLAIM 2024 for medical imaging AI |
| General ML/benchmark | task, dataset lineage, split, metric, baselines, seeds, compute, ablations, external evaluation | contamination, tuning on test, weak baseline, variance, cherry-picked seeds, resource cost, failure analysis | domain-specific adapter; artifact/reproducibility profile |
| Animal/preclinical | species/strain, unit, randomization, blinding, exclusions, welfare, sample-size rationale | pseudoreplication, cage/litter effects, attrition, selective reporting | ARRIVE 2.0 |
| Qualitative | researcher position, sampling rationale, setting, data generation, coding/analysis, reflexivity, negative cases | audit trail, saturation/information power, credibility, transferability, quotation provenance | SRQR or COREQ as appropriate |
| Systematic review/meta-analysis | protocol, question framework, search, screening, extraction, risk of bias, synthesis | reproducible search, duplicate assessment, heterogeneity, publication bias, certainty, update date | PRISMA 2020; PRISMA-S; RoB 2/ROBINS-I; GRADE |
| Method/tool/instrument | use case, design requirements, implementation, benchmark/validation, limitations, availability | comparator fairness, usability, robustness, failure boundary, resource requirements | domain and artifact adapters |
| Dataset/resource/benchmark | scope, acquisition, governance, schema, curation, quality, version, license, intended/forbidden uses | representativeness, consent, leakage, duplicates, documentation, maintenance | FAIR, DataCite, RO-Crate; domain-specific data standards |
| Theory/formal | definitions, assumptions, theorem/proposition, proof architecture, counterexamples, consequences | quantifier/scope, hidden assumptions, circularity, edge cases, computational verification if used | formal-proof adapter rather than empirical checklist |
| Humanities/interpretive | source corpus, provenance, historiography/theory, interpretive method, argument chain | source completeness claims, translation, positionality, counterinterpretations, archival limits | discipline/source-critical adapter |
| Hybrid/multi-study | per-study objects plus synthesis graph | incompatible populations/units, selective integration, cross-study claim inflation | compose adapters; never force one paper-level checklist onto all studies |

---

## 16. Bidirectional traceability rules

### Methods → Results

Every consequential method choice must either:

- govern at least one result/claim; or
- be marked as contextual, quality-control, unused, failed, or removed.

This identifies orphan methods and undisclosed analysis branches.

### Results → Methods and protocol

Every material result must identify:

- analysis ID;
- method/protocol item;
- prespecified/exploratory/deviation status;
- analytic population/data snapshot;
- figure/table object.

This detects outcome switching, HARKing, silent denominator changes, and post hoc confirmation language.

### Abstract/title/conclusion → body

Every standalone claim must map to one or more body claims and inherit their boundaries.

### Review concern → artifact delta

A concern closes only when the changed manuscript/artifact set is revalidated.

---

## 17. Behavioral and adversarial test program

### 17.1 Test fixtures, not instruction phrases

Each fixture should include:

```text
fixture/
  project-state/
  manuscript/
  sources/
  data-or-synthetic-analysis/
  expected-claims.json
  expected-provenance.json
  expected-blockers.json
  expected-assurance.json
  expected-release-decision.json
```

### 17.2 Minimum adversarial fixture set

#### Claim and reasoning

- one sentence containing two claims with different support;
- qualifier dropped between Results and Abstract;
- association rewritten as causation;
- local subgroup generalized to all populations;
- null result described as no effect;
- mechanistic explanation inferred from correlation;
- theorem stated without a necessary assumption;
- definition changed between sections.

#### Statistics and design

- pseudoreplication;
- clustered data analyzed as independent;
- primary outcome switched;
- uncorrected multiplicity;
- missing data handled inconsistently;
- equivalence claimed from non-significance;
- post hoc subgroup presented as prespecified;
- effect size/prose/figure mismatch;
- sample-size unit differs from analysis unit;
- sensitivity analysis contradicts headline claim.

#### ML/AI

- patient leakage across train/test;
- tuning on test set;
- internal split labeled external validation;
- cherry-picked random seed;
- weak or outdated baseline;
- class imbalance hidden by accuracy;
- calibration omitted;
- fairness claim based only on overall performance;
- embedding plot overinterpreted;
- benchmark contamination.

#### Literature and citation

- correct DOI but source does not support claim;
- secondary source cited for a primary result;
- retracted or corrected source;
- preprint and version of record duplicated;
- selective citation omits contrary evidence;
- “systematic” claim with unreproducible search;
- page locator fabricated;
- metadata collision between similarly titled papers.

#### Qualitative/humanities

- quotations lack source/participant provenance;
- researcher reflexivity absent when consequential;
- negative cases omitted;
- saturation asserted without evidence;
- translation choices alter interpretation;
- archive coverage overstated.

#### Figures and artifacts

- caption denominator differs from plot;
- units differ between axis and prose;
- hidden exclusions;
- plot generated from old data snapshot;
- missing source data;
- missing alt text;
- alt text simply repeats caption;
- inaccessible table headers;
- repository link exists but artifact version is wrong.

#### Ethics, authorship, and AI

- confidential manuscript sent to an unapproved AI service;
- AI-assisted drafting not disclosed under target policy;
- AI listed as author;
- contributor roles disputed or unconfirmed;
- funder role omitted;
- ethics approval identifier inconsistent;
- data sharing claim violates consent;
- dual-use risk ignored.

### 17.3 Metrics

Measure at least:

- atomic claim segmentation precision/recall/F1;
- claim-scope preservation;
- source identity accuracy;
- locator accuracy;
- entailment accuracy;
- blocker recall and false-blocker rate;
- severity calibration;
- Methods↔Results traceability completeness;
- section-contract completeness;
- numerical/terminological consistency;
- concern state-transition correctness;
- reproducibility success rate;
- reviewer-independence leakage rate;
- assurance-label calibration;
- deterministic schema validation;
- cross-model/cross-run stability.

### 17.4 Evaluation discipline

- gold labels require domain-methodology adjudication;
- ambiguous cases should permit multiple defensible outputs;
- test both under-blocking and over-blocking;
- keep hidden holdout fixtures;
- include mutation tests that change one qualifier, denominator, source version, or artifact hash;
- version the evaluation dataset and rubrics;
- never optimize only for polished prose preference.

---

## 18. Priority roadmap

### P0 — Scientific correctness and architecture

1. Make the archetype atlas canonical and deprecate the five-type router.
2. Introduce the project, research-contract, protocol, data, analysis, claim, source, figure, concern, declaration, assurance, and release schemas.
3. Add research-design, protocol/SAP/preregistration, and deviation modules.
4. Build the unified provenance graph.
5. Replace binary readiness with an assurance profile and separate target projection.
6. Expand statistics into analysis-and-inference.
7. Expand data availability into data governance and QA.
8. Add study-design/reporting-standard resolution.
9. Implement machine-readable section contracts.
10. Separate the daily recommender and delivery utilities from the scientific core.
11. Unify citation identity, source locator, entailment, and source-version status.
12. Add behavioral/adversarial fixtures and semantic CI gates.
13. Add confidentiality, AI-use, authorship, funding, conflict, and ethics state.
14. Link figures/tables to data and analysis objects.
15. Persist every serious run as a resumable project bundle.

### P1 — Coverage and assurance depth

1. Sampling/power/precision/information-adequacy adapters.
2. Missing data, multiplicity, diagnostics, and sensitivity adapters.
3. Causal inference and target-trial adapter.
4. Prediction/ML leakage, calibration, fairness, and external-testing adapter.
5. Systematic review search, risk-of-bias, and certainty adapter.
6. Qualitative reflexivity, coding, saturation, and audit-trail adapter.
7. Full front/back matter and declaration routes.
8. Accessibility validation.
9. DataCite/RO-Crate export.
10. Source correction/retraction/version checker.
11. Post-publication correction/update workflow.
12. Semantic manuscript delta and claim-strength regression checks.
13. Merge polishing and proposal-state logic into canonical skills.

### P2 — Maintainability and ecosystem

1. Freeze legacy `nature-*` writing facade and publish migration mappings.
2. Generate documentation from schemas to prevent drift.
3. Add bilingual parity tests.
4. Add policy snapshot review dates and source provenance.
5. Optimize context loading by task and schema dependencies.
6. Build a versioned benchmark corpus with community contribution rules.
7. Add telemetry only for consented, nonconfidential evaluation data.
8. Add plugin/tool interfaces around stable schemas rather than prose coupling.

---

## 19. Suggested pull-request sequence

### PR 1 — Canonical taxonomy and state kernel

- canonical archetype IDs;
- old taxonomy migration map;
- project/claim/source/concern schemas;
- stable IDs and validators;
- no behavior change yet.

**Acceptance:** every existing skill can refer to the same IDs; old projects remain readable.

### PR 2 — Research contract, protocol, SAP, and deviations

- new research-design skill;
- generic protocol schema;
- design adapters;
- preregistration/registration fields;
- deviation ledger.

**Acceptance:** a manuscript can distinguish unavailable, author-attested, prespecified, and deviated analyses.

### PR 3 — Data/analysis provenance

- data asset and analysis schemas;
- execution receipt;
- source/claim/analysis/figure edges;
- checksums and version links.

**Acceptance:** every numerical Result in a fixture traces to an analysis and input snapshot.

### PR 4 — Section contracts and complete manuscript surfaces

- YAML contracts for all sections and declarations;
- adapter hooks;
- section validator;
- semantic cross-section invariants.

**Acceptance:** missing or contradictory title/abstract/method/result/declaration states fail deterministically.

### PR 5 — Reporting and assurance adapters

- resolver;
- initial adapters for trial, observational, review, qualitative, animal, ML/prediction, theory/resource;
- assurance vector;
- target projection.

**Acceptance:** the same scientific state can be projected to multiple journals without changing claim assurance.

### PR 6 — Behavioral test harness

- synthetic fixtures;
- hidden mutations;
- expected state and blockers;
- CI metrics and thresholds;
- phrase-presence tests retained only for packaging, not scientific correctness.

**Acceptance:** each P0 failure mode has at least one red fixture and a stable green repair.

### PR 7 — Consolidation and utility separation

- `academic-writing` owns writing;
- `nature-writing` compatibility facade;
- polishing merged as a mode;
- proposal project state migrated;
- utilities moved and excluded from implicit routing;
- documentation generated from schemas.

**Acceptance:** no duplicate authoritative contract; migration guide passes tests.

---

## 20. Concrete release criteria for the improved system

A scope may be labeled **manuscript-consistent** only when:

- all in-scope manuscript assertions are atomically represented;
- each assertion’s support and boundary are explicit;
- contradictions and unresolved items are enumerated;
- title, abstract, body, figures, tables, and conclusion agree;
- no release placeholder remains.

A scope may be labeled **artifact-traceable** only when:

- protocol/SAP/data/code/analysis/figure versions are linked;
- deviations are recorded;
- assets have stable identity and checksums or equivalent version control;
- availability statements match actual access.

A scope may be labeled **computationally reproduced** only when:

- the defined outputs regenerate from recorded inputs and procedures;
- the environment and execution receipt are preserved;
- comparison tolerances are declared;
- failures are not silently waived.

A scope may be labeled **independently verified** only when:

- the verifier and verification scope are identified;
- the input packet is fixed;
- the verifier is independent for the claimed purpose;
- findings and unresolved exceptions are preserved.

A scope may be labeled **submission-ready for target** only when:

- scientific assurance state is reported, not implied;
- exact current target instructions were resolved;
- the applicable reporting checklist is complete or has justified N/A items;
- all declarations and artifacts are consistent;
- accessibility and surface QA pass;
- the package contains no confidential or project-internal leakage.

---

## 21. External research and standards basis

The redesign is consistent with the following current or foundational sources reviewed for this audit:

### Reporting and design-specific transparency

- EQUATOR Network definition and study-type library of reporting guidelines.
- CONSORT 2025, including its 30-item randomized-trial reporting checklist, participant flow, protocol/SAP access, deviations, data sharing, outcomes, missingness, and prespecified/post hoc distinctions.
- SPIRIT 2025, including its 34-item randomized-trial protocol framework.
- STROBE for observational reporting.
- PRISMA 2020 and PRISMA-S for review and reproducible search reporting.
- ARRIVE 2.0 for animal research.
- SRQR and COREQ for qualitative research.
- TRIPOD+AI and PROBAST+AI for prediction models.
- CLAIM 2024 for medical-imaging AI, including the distinction between internal and external testing.

### Transparency, reproducibility, and registration

- TOP 2025, which explicitly separates disclosure/sharing/certification, results transparency, computational reproducibility, replication, registered reports, multiverse analyses, and many-analyst studies.
- OSF registration documentation: a registration is a frozen project state; preregistration normally precedes data collection or analysis.
- FAIR principles, which apply to data and also to algorithms, tools, and workflows.
- FORCE11 software citation principles.
- W3C PROV for entities, activities, agents, derivation, attribution, and revision.
- RO-Crate for packaging research objects and provenance.
- DataCite metadata/version/relation types for persistent scholarly objects.

### Accountability, AI, and accessibility

- CRediT’s 14 contribution roles; CRediT describes contribution and does not determine authorship.
- ICMJE January 2026 recommendations on AI disclosure, human accountability, nonauthorship of AI systems, and review confidentiality.
- COPE guidance on AI use and correction/retraction principles.
- JATS4R accessibility recommendations: alt text for figures, long descriptions for complex visuals, semantic tables, and accessible links.

### Statistical and causal inference

- ASA guidance that p-values alone do not determine scientific conclusions or practical importance.
- ICH E9(R1) estimand and sensitivity-analysis framework.
- TARGET guidance for transparent target-trial emulation.

These standards should be versioned adapters. They are not substitutes for methodological judgment and should not be converted into arbitrary quality scores.

---

## 22. Final conclusion

The repository should not be rebuilt from scratch. Its rhetoric, explanation, claim verification, figure reasoning, journal resolution, and review/response logic are valuable and unusually mature.

The decisive next step is to move from:

> “an agent that knows many good rules for writing and reviewing a manuscript”

to:

> “a versioned system that preserves scientific intent, evidence, analysis, provenance, uncertainty, accountability, and reader-facing argument from research conception through publication and correction.”

That transition requires fewer new prose rules than it may appear. It requires:

- one canonical taxonomy;
- one canonical project state;
- upstream protocol/data/analysis objects;
- a unified provenance graph;
- section contracts;
- assurance profiles;
- study-specific adapters;
- and adversarial behavioral tests.

Once those are present, the existing writing intelligence can operate on a trustworthy scientific substrate, and “writing a paper” becomes a reproducible transformation of verified research state rather than a fluent reconstruction from chat context.
