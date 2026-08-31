# Manuscript excellence release gate

> Mandatory orchestration layer for substantial manuscript drafting, revision, review, and publication-readiness decisions.
>
> This gate complements integrity, correctness, reporting, and surface QA. A paper can be true and reproducible yet still fail as scholarly communication.

## Release principle

Do not call a manuscript publication-ready merely because:

- its claims are verified;
- citations are correct;
- formatting is clean;
- reviewers find no technical blocker;
- every section exists;
- every limitation is disclosed.

A release-ready paper must also form a **coherent, sufficiently developed, reader-activated scientific argument with calibrated numerical and rhetorical presentation**.

## Mandatory stage integration

### Before drafting / major restructuring

Create or refresh:

1. **whole-paper argument graph** using `manuscript-narrative-architecture.md`;
2. **section-function map**;
3. **reader-state activation map** for central terms/entities/experiments;
4. **headline result -> interpretation matrix** for eventual Discussion;
5. **numeric presentation policy** for headline quantities using `numerical-reporting-precision.md`;
6. **epistemic-stance plan** for headline claims using `epistemic-rhetoric-and-qualification.md`.

For a substantial manuscript, inspect several close peer-reviewed analogue papers when available. Extract function and proportion, not wording:

- how they introduce the question;
- when central terminology becomes active;
- how Results blocks depend on one another;
- what belongs in setup/Methods versus Results;
- how numerical precision is rendered;
- how Discussion relates findings to alternatives and prior work;
- how many caveats are local versus consolidated.

Do not copy section names or word counts mechanically.

### Before writing each major section

Write a one-line section contract:

```text
reader enters knowing X
-> asks Q
-> section supplies Y
-> reader leaves able to infer/test Z
```

If `X` is not active yet, repair earlier exposition.

If `Y` contains a central model/dataset/hypothesis/comparator never introduced before, activate it before result-bearing use.

### During Results drafting

Every major result block must pass:

- **necessity** — why this analysis now?
- **setup** — what comparison is being made?
- **evidence** — what was observed/estimated?
- **uncertainty/discriminator** — how should the pattern be judged?
- **local answer** — what question is now answered?
- **handoff** — what remains that motivates the next block?

Do not narrate version chronology when scientific dependency is the real order.

### During Discussion drafting

For every headline result, select the minimum necessary subset of:

```text
meaning
mechanism/explanation
strongest alternative
relation to closest prior work
boundary/generalizability
methodological/practical implication
next discriminator
```

A list of limitations does not satisfy the Discussion requirement.

A list of prior papers does not satisfy the relation-to-prior-work requirement.

### During numerical rendering

Keep full precision in artifacts but explicitly resolve manuscript precision for:

- primary estimates;
- proportions/accuracies/F1/recall/etc.;
- intervals;
- P values;
- exact finite counts/fractions;
- runtimes/resources when claim-bearing.

Reject fixed `%.6f`-style output as the default manuscript policy.

### During epistemic-language revision

For each headline claim:

1. state the strongest positive bounded result directly;
2. attach only the qualification needed to prevent a concrete overreading;
3. consolidate repeated global limitations in Discussion;
4. move audit chronology/status language out of the scientific narrative unless it changes interpretation.

Disclosure and transparency remain mandatory; repetitive defensive narration does not.

## Pre-review excellence QA

Before simulated peer review, require all of the following:

### E1 — macro logic

- whole-paper argument graph has no unexplained central jumps;
- every major section has a reader question and a handoff;
- Results are ordered by scientific dependency rather than repository/run chronology.

### E2 — functional section sufficiency

- setup/formulation sections discharge every prerequisite used later;
- no section is accepted merely because its heading exists;
- no short section is expanded by arbitrary quota; missing dependencies, not length, drive repair.

### E3 — reader-state activation

- central terminology is defined/characterized before first claim-bearing use;
- no surprise model/dataset/hypothesis/comparator appears only in Results or a table;
- tables/figures are locally understandable and do not introduce central paper objects silently.

### E4 — discussion depth

- headline findings are interpreted;
- strongest relevant alternatives are addressed when material;
- relation to closest prior work is explained rather than merely cited;
- limitations are linked to what they change;
- implications are specific enough to follow from the evidence.

### E5 — rhetorical calibration

- positive bounded findings remain visible;
- caveats are not repeated without a distinct function;
- adverse/null results are interpreted scientifically;
- project-governance language does not dominate reader-facing prose.

### E6 — numerical precision

- manuscript digits reflect scientific resolution/uncertainty/decision use;
- exact counts/fractions are preserved where useful;
- thresholds are not obscured by rounding;
- same results use consistent rounding across surfaces.

### E7 — close-analogue plausibility

When comparable high-quality papers exist, verify that the manuscript's explanation depth, result sequencing, discussion depth, and numerical presentation are not obviously anomalous without a scientific reason.

Analogue conformity is not itself a goal. Unexplained genre deviation is a review trigger.

## Reviewer requirements

At least one reviewer/editor pass must assess the paper as a **reader and argument**, not merely as a verifier.

The pass must answer:

1. Can I state the paper's research question after the Introduction without repository knowledge?
2. Can I define every central paper-specific object before Results use it?
3. Can I explain why each major Results block follows the previous one?
4. Can I distinguish the strongest result from the audit/provenance history?
5. Does the Discussion tell me what the findings mean, how they relate to alternatives/prior work, and where they stop?
6. Are the displayed numbers as precise as the science warrants, rather than as precise as the software produced?
7. Is the paper appropriately confident rather than defensive or promotional?

A technically capable reviewer being able to reconstruct missing logic by effort does **not** count as a pass.

## Clean-reader closure

The final clean-room reviewer should receive only:

- current manuscript;
- normal supplementary/publication material;
- ordinary public scholarly sources needed for verification.

They should not receive:

- internal project ontology;
- claim-subtraction ledger;
- version genealogy;
- author explanation of what a missing term was intended to mean;
- prior review discussions.

If the reviewer needs those to reconstruct the paper, readiness is blocked.

## Automated support

Use `audit_narrative_precision.py` as a conservative pre-review signal for:

- excessive decimal precision;
- fixed-width perfect/zero metrics;
- defensive qualification density;
- experiment/version-ID narrative density;
- suspiciously short setup/formulation sections.

Scanner findings require contextual review. They are not universal errors.

## Publication-ready terminal extension

A manuscript cannot enter a publication-ready terminal unless:

- all E1–E7 applicable gates pass;
- no central object appears before its meaning is active;
- no headline evidence block lacks a recoverable dependency on the paper's question;
- Discussion is interpretively sufficient for the article type;
- numerical precision is scientifically justified;
- direct positive bounded findings remain identifiable;
- no unresolved narrative/reader-state review item could cause a qualified new reader to misread the scientific case.

## Boundaries

This gate must not:

- reward longer manuscripts by default;
- force IMRaD where inappropriate;
- force a dedicated Discussion or Problem Formulation heading;
- remove inconvenient evidence;
- weaken necessary methodological transparency;
- invent mechanisms or implications;
- force human-like stylistic noise;
- optimize for AI-detector scores.

The objective is an **excellent scientific argument for a real reader**, not a performance of human authorship.
