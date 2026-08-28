# Study Protocol and Conduct Decision Contract

Use this contract before Methods/Results drafting, claim certification, display
engineering, reporting-standard assessment, or venue acceptance engineering
when an empirical, computational, qualitative, review, or resource study record
is in scope.

It answers:

```text
What was planned?
When was it frozen relative to data/outcome access?
What was actually executed?
What changed, why, and with what inferential consequence?
Which analyses and claims remain licensed by that record?
```

It does **not** answer whether the scientific claim is true or whether a journal
will accept it.

## Authoritative artifacts

- Schema: `../study-contracts/study-protocol-conduct-contract.schema.json`
- Maintained adapters: `../study-contracts/maintained-study-adapters.json`
- Evidence registry: `../study-contracts/study-protocol-evidence-registry.json`
- Research ledger: `../research/study-protocol-conduct-evidence-ledger-2026-08.md`
- Resolver/evaluator: `../scripts/resolve_study_protocol.py`

The initial evidence base contains 39 reconciled sources: 19 read in full text
and 20 at abstract level. The broad discovery log freezes 12 queries and 84
screening records. Read depth, supported decisions, contradictions, transfer
limits, and update triggers are explicit.

## Non-universal architecture

Resolve:

`study archetype × design tags × evidence modality × applicable governance`

The resolver returns applicable obligations, not a `best_design`. The maintained
catalog currently covers randomized intervention, observational causal,
observational association, computational/ML, animal/preclinical, systematic
review, qualitative/interpretive, experimental, resource/dataset, and
exploratory/descriptive work.

If nothing matches, return an unresolved domain-research requirement. Never
silently force clinical-trial registration, quantitative power, saturation,
target-trial emulation, or machine-learning splits onto unrelated work.

## Required object chain

Materialize and version:

1. scientific question and estimand/interpretive target;
2. protocol identity, version, status, freeze time, and hash;
3. registration applicability, basis, identifier, and timing;
4. primary/secondary outcomes or evidence targets;
5. analysis-plan identity, version, freeze time, sample-size/data-adequacy
   rationale, stopping, exclusions, missingness, multiplicity/model selection,
   sensitivity, and data-split plan where applicable;
6. conduct record: enrollment/sampling, assignment, concealment, blinding,
   intervention fidelity, outcome collection, harms, QC, exclusions/attrition,
   raw-data snapshot, operators/instruments/environment when relevant;
7. analysis execution bound to the plan and raw snapshot;
8. append-only deviations/amendments;
9. claim status and allowed/prohibited inference;
10. ethics/governance authority and source/evidence provenance.

Final Methods prose is a projection of these objects, not their replacement.

## State distinctions

Keep independent:

- `planned`;
- `executed`;
- `verified_by_receipt`;
- `unknown`;
- `not_done`;
- `not_applicable`;
- `prespecified/confirmatory`;
- `deviation`;
- `exploratory/post_hoc/interpretive`.

Do not convert `unknown` to `done` because a manuscript sentence uses the past
tense. Do not erase a deviation by updating the final protocol text.

For pre-existing data, distinguish `after_data_before_outcome_access` from
`after_outcome_access`. The former can support an outcome-blind confirmatory
status only when both protocol and analysis plan precede outcome access; it must
not be relabeled `before_data_access`.

## Automatic blockers

The evaluator fails closed on bounded contradictions:

- false prospective timing;
- required registration that is missing/late;
- undisclosed primary-outcome changes;
- randomized assignment named but not execution-verified;
- hidden blinding differences;
- unlogged stopping/sample-size change;
- assigned/excluded/analyzed counts that do not reconcile;
- omitted adverse events;
- machine-learning evaluation leakage;
- confirmatory labels unsupported by timing;
- missing required ethics authority;
- analysis input not bound to the raw-data snapshot;
- structural schema failure.

Passing means only that these recorded invariants passed. It does not establish
valid measurement, adequate power, correct code, truthful source records,
absence of bias, successful replication, generalization, or acceptance.

## Repair routes

Allowed routes preserve history and evidence:

- reconcile from authoritative source objects;
- restore a prespecified analysis/outcome;
- append a dated deviation/amendment with reason and affected claims;
- disclose actual assignment/blinding/fidelity/attrition/harms;
- rerun from the correct data snapshot or uncontaminated split;
- add an explicitly versioned sensitivity analysis;
- reclassify as deviation, exploratory, post hoc, descriptive, or interpretive;
- narrow/remove a claim;
- run a new prospective study.

Never backdate, fabricate approvals/receipts, rename an outcome retroactively,
delete adverse/null/harmful observations, overwrite the original plan, or treat
registration/checklist completion as certification.

Missing required ethics authority is not repaired by claim narrowing. Verify
authority before proceeding; unauthorized use may be non-repairable.

## Certification boundary

Return separate machine-readable fields for:

- schema validity;
- protocol traceability;
- conduct traceability;
- deviation visibility;
- outcome alignment;
- unresolved domain obligations.

Always include:

```text
does_not_certify:
  - scientific_truth
  - absence_of_bias
  - reporting_guideline_completion
  - journal_acceptance
```

Venue acceptance remains governed by the exact
`venue × article type × stage × effective date` decision contract after the
science record has been evaluated.
