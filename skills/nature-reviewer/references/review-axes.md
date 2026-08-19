# Journal-aware review axes

Use these axes after resolving the exact target and loading the shared decision engine. Do not use one prestige-journal rubric for every manuscript.

## Contents

- [Universal scientific axes](#universal-scientific-axes)
- [Target-conditional editorial axes](#target-conditional-editorial-axes)
- [Nature exact profile](#nature-exact-profile)
- [Rigor-first profile](#rigor-first-profile)
- [Engineering / field-advancement profile](#engineering--field-advancement-profile)
- [Clinical / policy-priority profile](#clinical--policy-priority-profile)
- [Evidence-assessment profile](#evidence-assessment-profile)
- [Reviewer emphasis briefs](#reviewer-emphasis-briefs)
- [Missing-evidence handling](#missing-evidence-handling)

## Universal scientific axes

These are relevant to most empirical/research manuscripts, but their realization depends on study design.

### `claim_evidence_validity`

- What are the central claims?
- Does the visible evidence establish each claim at its stated strength and scope?
- Are observation, prediction, association, mechanism, causation, proof and generalization kept distinct?
- Are important alternative explanations discriminated from, acknowledged, or left unresolved?

### `methods_and_analysis`

- Does the design permit the intended inference?
- Are methods, controls/comparators, sampling, measurements, analyses and uncertainty appropriate?
- Are assumptions and consequential choices visible?

### `data_and_reporting_integrity`

- Are denominators, sample/replicate units, exclusions, missingness, uncertainty, figures and tables internally coherent?
- Are ethics, registration, source-data, image/data integrity and reporting requirements satisfied when applicable?

### `prior_work_and_positioning`

- Is the contribution's relationship to prior work accurate and verifiable?
- Are close alternatives, contradictory evidence and important limitations represented fairly?
- Is incrementality hidden or is prior work unfairly weakened to manufacture novelty?

### `reproducibility_or_auditability`

- Can a qualified reader reproduce, reanalyse, verify or independently audit the work at the level appropriate to the field?
- Are data/code/material/source/protocol details available when required?

### `clarity_and_argument_logic`

- Can the reader reconstruct `question -> answer -> evidence -> boundary -> meaning`?
- Does each major analysis have a reason to follow the previous one?
- Does unclear presentation obstruct scientific evaluation rather than merely offend style preference?

## Target-conditional editorial axes

Load only when the exact journal/venue uses them.

### `originality`

Assess what is actually new relative to the closest work. Do not equate `new` with `important`.

### `significance_or_priority`

Assess whether the contribution matters enough under the target's explicit publication model. This may mean field-level advancement, broad scientific consequence, clinical/policy importance, or another target-specific value.

### `breadth_or_readership`

Use only when the journal expects interest beyond a narrow specialty. Identify **which additional readers** would care and what scientific consequence reaches them.

### `field_advancement`

For engineering/computing/society venues, ask whether the work contributes meaningfully to the field, is complete enough, and changes capability/understanding/practice at the expected level.

### `clinical_or_policy_consequence`

For relevant selective clinical/public-health journals, distinguish statistical correctness from clinical/public-health importance and assess whether design strength supports the practical implication.

### `resource_or_reuse_value`

For datasets, software, benchmarks, protocols and resources, assess validation, completeness, documentation and probable research utility when the target values resource contribution.

## Nature exact profile

For flagship Nature, preserve the source-grounded axes:

- `originality`;
- `scientific importance / significance`;
- `interdisciplinary readership interest`;
- `technical soundness / technical failings`;
- `readability for nonspecialists`.

Nature editors make the final broad-readership/priority judgement. Reviewer simulation may advise on it but must not claim editorial authority.

## Rigor-first profile

When the exact target explicitly does not gate on perceived importance/novelty, do **not** manufacture those bars.

Foreground:

- technical rigor;
- scientific/ethical validity;
- data support for conclusions;
- reproducibility/reporting;
- fair literature context;
- clarity sufficient for evaluation.

PLOS ONE is the canonical current example in the shared decision profile.

## Engineering / field-advancement profile

For IEEE-like or other field-advancement targets when confirmed by exact guidance, foreground:

- scope;
- novelty/contribution;
- validity and data;
- method/design soundness;
- reproducibility;
- field advancement;
- logical clarity and supported conclusions;
- compliance.

Do not add a broad interdisciplinary-interest gate unless the exact venue requires it.

## Clinical / policy-priority profile

Foreground:

- importance of question;
- design validity and bias/confounding control;
- effect magnitude and uncertainty;
- reasonable conclusions;
- population/generalizability boundaries;
- harms/adverse outcomes where relevant;
- clinical/public-health/policy consequence under the exact journal criteria;
- reporting-guideline compliance.

## Evidence-assessment profile

For eLife-like assessment models, keep two dimensions separate:

1. **significance of findings**;
2. **strength of evidence**.

Do not translate them into a fake acceptance score. A useful narrow result can have compelling evidence; an important result can currently have incomplete evidence.

## Reviewer emphasis briefs

Assign lenses before any report is generated. These are analysis emphases, not invented reviewer identities.

Default cross-journal panel:

- `Reviewer 1` — validity, methods, data, inference and blocking technical concerns;
- `Reviewer 2` — prior work, originality/contribution and target-specific significance/priority;
- `Reviewer 3` — reproducibility/reporting, clarity/readership and generalization/boundary.

Modify lenses when the article type requires it. For example, a clinical paper may require stronger design/statistical/clinical-interpretation coverage; a theorem paper needs proof/assumption/boundary coverage; qualitative work needs sampling/analytic-credibility/transferability coverage.

All reviewers still inspect the central claims. Different emphasis does not grant access to different facts.

## Missing-evidence handling

Use explicit states:

- `Not assessable from provided material`;
- `AUTHOR_INPUT_NEEDED`;
- `Evidence not shown in the supplied manuscript excerpt`.

Do not convert unavailable material into a presumed defect. If the supplied package was expected to contain the material and the omission itself is verifiable, assess the omission rather than inventing what the missing content would show.
