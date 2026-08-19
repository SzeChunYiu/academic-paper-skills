# Section: Methods (writing)

## Reader job

Methods must make the evidence-generation process and its credibility recoverable:

`what was studied -> how evidence was generated -> consequential choices -> analysis/inference -> controls/validation -> reproducibility/boundary`

A computational pipeline is only one subtype.

## Select moves by study design

Common moves include:

- study/design overview
- material/data/population/source definition
- sampling/inclusion/exclusion
- measurement/representation
- apparatus/procedure/intervention
- model/algorithm/formalization
- analysis/statistics/inference
- controls/baselines/validation
- sensitivity/robustness/uncertainty
- ethics/registration/consent
- reproducibility/data/code/material availability

Use only the moves required by the design and reporting standard.

## Rationale rule

Explain **why** a choice was made when a reasonable alternative would materially change interpretation: sampling, endpoint, comparator, preprocessing, model, threshold, assay, time window, statistical test, coding framework, etc.

Do not claim an untested `technical advantage` inside Methods. State the design intention/property; let Results establish whether the advantage exists.

## Organization

Choose the structure that minimizes reader backtracking:

- chronological procedure
- evidence-source/experiment based
- conceptual component based
- analysis-question based
- overview -> detailed components

## Computational subtype

For genuine model/pipeline papers, a useful sequence is:

`problem/formalization -> data/representation -> components -> objective/training -> inference -> complexity/resources -> implementation -> evaluation protocol`

Evaluation design—splits/leakage, baselines, metrics, hyperparameters, compute, seeds, ablations, uncertainty, stress/external tests—is part of methodological credibility.

## Non-computational reminder

Clinical, experimental, qualitative, social-science, theoretical and historical/source-based research need different credibility moves. Load `references/method.md` before imposing a pipeline vocabulary.

## Vague phrases to eliminate

Do not leave unsupported placeholders such as:

- `under standard conditions`
- `using routine methods`
- `data were analyzed statistically`
- `the method was validated`
- `samples were randomly assigned` without the actual process

Replace them with the information needed to evaluate/reproduce the work, or flag the missing input.

## Audit

Every major Results claim should trace to a visible method/analysis path. If readers cannot reconstruct how the evidence supporting a central claim was generated, fix that before polishing prose.