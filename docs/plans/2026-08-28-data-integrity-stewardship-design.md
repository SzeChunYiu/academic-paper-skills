# Data Integrity and Stewardship Contract Design

## Objective

Model the scientific data layer that sits between study conduct and every
analysis, table, figure, claim, repository object, and availability statement.
The system must detect bounded contradictions without pretending that a schema,
checksum, FAIR score, repository deposit, or automated quality check proves that
the observations are accurate or the scientific claim is true.

## Approaches considered

1. **One universal data-quality checklist.** Simple, but scientifically unsafe:
   calibration, missingness, batch structure, consent, image metadata, and
   benchmark leakage have different meanings across modalities.
2. **Hard-code every discipline and repository.** More specific at first, but it
   cannot remain complete and would silently become stale.
3. **Invariant lifecycle core plus maintained modality/governance adapters and
   explicit live resolution.** This is the selected design. Cross-domain
   invariants are automatic; adapters add obligations only when applicable;
   unmatched domain policies remain unresolved rather than inheriting an
   invented generic rule.

## Architecture

The authoritative chain is:

```text
source/acquisition record
-> immutable raw or exact external-reference origin
-> validation and QC receipts
-> versioned transformation receipts
-> analysis-ready snapshot
-> analysis/display inputs
-> release or controlled-access object
-> bounded data and scientific claims
```

The contract records data identity, scientific unit, collection context,
schema/codebook and units, hashes, corrections, exclusions, missingness,
duplicates, QC results, transformation code/environment, lineage edges,
rights/consent, sensitivity classification, retention, release version, access
route, licence, persistent identifier, and append-only deviations.

The resolver uses:

```text
data modality x study context x sensitivity/governance tags x policy as-of date
```

It returns applicable obligations, source provenance, transfer limits, and
unresolved exact-domain research. It never returns a universal `best_quality`
score. Maintained adapters cover common tabular/observational, human/clinical,
qualitative, computational benchmark, high-throughput omics, biological
imaging, sensor/field, simulation/synthetic, and shared resource cases. Exact
institutional, legal, funder, repository, and community-standard obligations
must still be resolved from current official sources.

## Bounded automatic checks

The evaluator fails closed on structural invalidity and machine-checkable
contradictions, including raw-snapshot mutation, broken lineage, analysis-input
hash mismatch, undocumented transformations/corrections, unreconciled unit
counts, hidden exclusions or adverse/null records, semantic/unit drift, required
QC represented as passing without a receipt, required calibration not verified,
unresolved uniqueness collisions, plan/realized missingness conflict, prohibited
public release of sensitive data, absent third-party rights, and false release
or version claims.

Allowed repairs preserve history: restore an authoritative snapshot, quarantine
invalid material, append a correction/deviation, rerun transformations and
analyses, disclose missingness/exclusions, add sensitivity analysis, use a valid
controlled-access route, secure permission, replace/withdraw a release, or
narrow/remove the affected claim. Claim narrowing cannot create consent,
licence, privacy protection, source observations, or an execution receipt.

## Certification boundary

Passing certifies only the recorded invariant checks. It does not certify
measurement accuracy, completeness, representativeness, absence of bias,
privacy/anonymity, legal compliance, reproducibility, scientific truth, or
journal acceptance. `unknown`, `not_checked`, `not_applicable`, `failed`, and
`passed` remain distinct.

## Research and provenance

The evidence registry must separate peer-reviewed studies, community standards,
official policies, specifications, and guidance. Every source records read
depth, publication/effective dates, access/review dates, supported decisions,
limits, and contradictions. A frozen OpenAlex discovery log documents breadth
without claiming systematic-review completeness. Policy sources are
time-versioned; future-effective rules are not backcast, and observed-current
pages without an explicit effective date are not treated as historical proof.

## Integration and tests

The shared contract is loaded by canonical `academic-writing` before Methods,
Results, statistics, displays, claims, and availability prose, and by
`academic-paper-pipeline` after study-protocol/conduct resolution. Project state
gains an additive data-lifecycle section and assurance fields while preserving
existing keys.

Behavior fixtures demonstrate valid bounded traceability and failures for raw
mutation, broken transform lineage, silent adverse/null deletion, unit drift,
unverified QC/calibration, sensitive public release, rights conflict, false
repository availability, and non-universal unresolved adapters. Structural
malformation must block before semantic evaluation.
