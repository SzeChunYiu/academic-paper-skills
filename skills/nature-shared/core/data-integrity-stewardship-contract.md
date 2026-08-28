# Data Integrity and Stewardship Decision Contract

Use this contract after study protocol/conduct resolution and before analysis,
statistics, displays, claims, availability statements, repository release, or
submission-readiness assessment when scientific data are in scope.

It answers:

```text
What source or acquisition record produced the data?
Which immutable raw or exact external-reference origin preserves that record?
What validation, QC, correction, and transformation actually occurred?
Which analysis-ready snapshot fed each analysis, result, and display?
What use, access, retention, and release are authorized?
Which defects, exclusions, missingness choices, and deviations remain visible?
```

It does **not** answer whether measurements are accurate, the sample is
representative, the analysis is correct, a scientific claim is true, a release
is anonymous, or a journal will accept the paper.

## Authoritative artifacts

- Schema: `../data-contracts/data-integrity-stewardship-contract.schema.json`
- Maintained adapters: `../data-contracts/maintained-data-adapters.json`
- Evidence registry: `../data-contracts/data-integrity-evidence-registry.json`
- Research ledger: `../research/data-integrity-stewardship-evidence-ledger-2026-08.md`
- Frozen search log: `../research/data-integrity-stewardship-search-log-2026-08-28.json`
- Resolver/evaluator: `../scripts/resolve_data_integrity.py`

The initial registry reconciles 41 sources: 22 peer-reviewed studies read in
full text, 13 official standards/guidance/policy sources, and 6 abstract-level
reads. The discovery record freezes 12 OpenAlex queries and 84 screened
metadata records. This is targeted triangulation, not a systematic-review or
exhaustive-coverage claim.

## Non-universal resolution

Resolve:

`data modality × study context × sensitivity/governance tags × policy as-of date`

Maintained adapters cover common:

- tabular/observational data;
- human or clinical sensitive data;
- Indigenous or community-governed data;
- qualitative or interpretive sensitive material;
- computational/ML benchmarks;
- high-throughput omics or metabolomics;
- biological or neuroimaging;
- sensor, field, or instrument streams;
- simulation or synthetic data;
- shared resources and repositories.

Adapters return applicable obligations and source provenance, never a universal
`best_quality` score. Unmatched modalities remain explicit live domain-research
obligations. Exact institutional, legal, funder, repository, consent, licence,
and community-governance requirements must be resolved from current competent
official sources. A maintained adapter cannot certify compliance with an
unresolved exact policy.

## Required authority chain

Preserve and version:

```text
source/acquisition record
-> immutable raw or exact external-reference origin
-> validation and QC receipts
-> versioned transformation receipts
-> immutable analysis-ready snapshot
-> analysis/display input bindings
-> release or controlled-access object
-> bounded claim and availability statement
```

For each object record identities, versions, hashes, timestamps, scientific
units, schemas/codebooks, units, missing-value codes, record and byte counts,
known defects, decisions, corrections, exclusions, missingness, duplicates,
semantic changes, operators/instruments/environments where material, rights,
authority, sensitivity, access conditions, retention, licences, identifiers,
and append-only deviations.

The raw snapshot is an immutable observation boundary. When a competent remote
database or physical authority cannot appropriately be copied locally, record an
exact externally versioned origin instead: query, source version, retrieval time,
returned snapshot identity, and fixity where available. Do not invent a local raw
file requirement. A corrected dataset is a new version with lineage; do not
overwrite the original. An analysis-ready snapshot is not authoritative merely
because a script can load it: every input must trace through executed
transformations and required QC to the preserved origin objects.

## State distinctions

Keep independent:

- `planned`, `executed`, and `verified_by_receipt`;
- `unknown`, `not_checked`, `not_done`, and `not_applicable`;
- raw, validated, analysis-ready, display-source, and released snapshots;
- required, optional, prohibited, and unresolved obligations;
- public, controlled, restricted, closed, and not-released access;
- disclosed, resolved, quarantined, withdrawn, and non-repairable deviations.

Do not turn a documentation statement into an execution receipt. A checksum
establishes identity, not accuracy. A persistent identifier establishes a
locator only when it resolves to the declared version. FAIR metadata does not
override privacy, consent, collective authority, licence, or rights constraints.

## Bounded automatic blockers

The evaluator fails closed on recorded contradictions including:

- a raw snapshot marked mutable;
- a missing authoritative raw/external-reference origin, a transformation input/output missing from the
  lineage graph, or a cyclic/competing derivation history;
- a declared transformation without an execution receipt;
- an analysis hash that differs from its declared input snapshot;
- record-count changes not reconciled to declared unit decisions;
- hidden exclusions or adverse/null decisions;
- semantic, schema, code, or unit drift not declared as a transformation;
- required QC shown as passing without a receipt;
- adapter-required QC silently relabeled optional or not applicable;
- failed required QC represented as sufficient;
- required instrument calibration that is unverified;
- realized missingness handling that differs from the plan without a deviation;
- missing required consent, authority, collective governance, or third-party
  rights;
- unauthorized public release of sensitive or restricted data;
- a verified release claim without a resolvable identifier or locator;
- a released hash that does not match the declared snapshot;
- structural schema failure.

An unmatched modality or required exact policy that remains unresolved returns
an unresolved state rather than inheriting invented generic rules.

## Repair routes and non-repairable boundaries

Allowed repairs preserve history and authority:

- restore or locate the authoritative source/raw snapshot;
- quarantine invalid material without deleting its provenance;
- append a correction, unit decision, exclusion, or dated deviation;
- execute and receipt the required QC, calibration, or transformation;
- rerun dependent analyses and displays from the corrected snapshot;
- reconcile counts and disclose missingness, exclusions, adverse/null results,
  batch effects, contamination, or other known defects;
- add a versioned sensitivity analysis;
- use an authorized controlled-access route;
- secure prospective permission or third-party rights where valid;
- replace, version, restrict, or withdraw a false/unsafe release;
- narrow or remove claims that the remaining evidence cannot support.

Claim narrowing cannot create source observations, consent, ethics or community
authority, a licence, privacy protection, calibration, an execution receipt, or
an actually deposited release. If required authority never existed, stop the
unauthorized use and record the non-repairable boundary rather than repairing it
with prose.

## Availability and release

Keep separate:

1. whether release is scientifically useful;
2. whether release is authorized;
3. whether the stated object exists and is the claimed version;
4. whether peer reviewers can obtain sufficient access;
5. whether the manuscript accurately describes the access route and limits.

Open release is not universally correct. Controlled, restricted, synthetic,
metadata-only, or no-release routes may be required. Conversely, a generic
"available on request" sentence is not evidence that a usable governed access
route exists. Bind every availability statement to the exact snapshot, hash,
version, identifier/locator, licence, access conditions, and resolution time.

## Certification boundary

Return separate machine-readable fields for:

- schema validity;
- raw-snapshot immutability;
- transformation and analysis-input traceability;
- QC receipt status;
- decision/deviation visibility;
- governance and release resolution;
- unmatched adapters and unresolved exact policies.

Always preserve exclusions equivalent to:

```text
does_not_certify:
  - measurement_accuracy
  - completeness_or_representativeness
  - absence_of_bias
  - privacy_or_anonymity
  - legal_or_policy_compliance
  - scientific_truth
  - analytic_reproducibility
  - journal_acceptance
```

Passing certifies only that the recorded, machine-checkable lifecycle invariants
passed. Scientific validity, statistical assurance, display validity, reporting
completion, exact venue fit, and real acceptance remain separate layers.

## Workflow handoff

After resolution, pass the exact analysis-ready snapshot IDs and hashes to
statistics, claims, and scientific display contracts. Pass the governed release
object to availability prose and target-specific submission checks. If a
blocker affects an in-scope result, display, availability statement, or claim,
that downstream object remains blocked until repaired, rerun, withdrawn, or
appropriately narrowed.
