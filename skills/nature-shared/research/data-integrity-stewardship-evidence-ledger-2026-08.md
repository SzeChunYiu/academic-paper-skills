# Data Integrity and Stewardship Evidence Ledger

**Review date:** 2026-08-28  
**Registry:** `../data-contracts/data-integrity-evidence-registry.json`  
**Frozen discovery log:** `data-integrity-stewardship-search-log-2026-08-28.json`

## Review method and boundary

This targeted review triangulates 41 reconciled sources: 22 peer-reviewed full
texts, 6 abstract-level records, 6 official/technical standards, 5 official
guidance documents, and 2 current publisher-policy pages. Twelve frozen
OpenAlex queries produced 84 metadata-screened records across data management,
cleaning, FAIR stewardship, dataset documentation, provenance, missingness,
omics batch effects, imaging metadata/QC, sensor drift, qualitative data,
privacy/re-identification, and repository versioning.

This is a broad engineering evidence base, not a systematic review and not a
claim that all disciplines, laws, funders, repositories, or institutional rules
have been encoded. Sources enter the resolver only through explicit source
references. Each source records read depth, supported decisions, limits,
contradictions, access date, and—where applicable—policy effective-date basis.

## 1. Fixity detects change, not truth

BagIt defines a valid package as one whose manifest checksums verify. FORCE11's
data-citation principles similarly distinguish persistence, fixity, provenance,
and identification of the specific version or timeslice that supports a claim.
These are necessary for answering “is this the same object?” They cannot answer
“was the measurement accurate?”, “is the cohort representative?”, or “is the
scientific interpretation correct?”

**Contract consequence:** bind raw, processed, analysis, figure-source, and
release objects with identity, version, hash, byte or record count where
appropriate, and lineage edges. A hash mismatch or a claimed immutable object
that changed is blocking. A matching hash is only a fixity receipt.

**Transfer limit:** some authoritative sources are remote databases or physical
records for which local immutable copies are inappropriate. In those cases,
record the exact query, source version or retrieval date, and returned snapshot
identity rather than inventing a local raw-file requirement.

## 2. Provenance must expose entities, activities, agents, and derivation

W3C PROV models the entities, activities, and agents involved in producing an
object and explicitly includes derivation, responsibility, versioning, and the
provenance of provenance. RO-Crate packages research-object context and
workflow metadata. Wilson et al. recommend preserving raw data, recording every
processing step, and retaining intermediate products; BIDS separates raw from
derived imaging data partly to prevent accidental changes to raw data.

**Contract consequence:** every material derived dataset requires an input
snapshot, output snapshot, transformation identity/version, execution receipt,
parameters, environment or instrument context when material, and actor. Manual
edits are transformations, not exceptions. The analysis input must equal the
declared analysis-ready snapshot; prose does not close a broken edge.

**Contradiction resolved:** a fully serialized workflow is useful but not always
possible for interactive coding, qualitative redaction, or expert adjudication.
The invariant is not “all work must be automated”; it is that the selected
coordinates, decisions, redactions, adjudications, and reasons remain explicit,
versioned, and connected to input/output objects.

## 3. Data quality is contextual and multidimensional

Kahn et al. organize secondary EHR data quality into conformance,
completeness, and plausibility, and distinguish internal verification from
external validation. Weiskopf and Weng found multiple dimensions—including
completeness, correctness, concordance, plausibility, and currency—and multiple
assessment methods. Both reviews show why `quality_score: 92` without an
intended use, expectation, method, denominator, and reference is not meaningful.
Kahn et al. further distinguish computational conformance from plausibility: a
calculation can exactly follow a flawed specification.

**Contract consequence:** represent quality assertions as scoped checks with a
dimension, target object, method, expectation/reference, denominator, result,
receipt, and consequence. Preserve `not_checked`, `unknown`, `not_applicable`,
`failed`, and `passed`. The resolver returns applicable dimensions; it never
computes a universal best-quality score.

**Transfer limit:** EHR terminology is a useful adapter, not a universal
ontology. Imaging, metabolomics, qualitative coding, sensors, benchmarks, and
simulations require different observable checks and external references.

## 4. Cleaning is a scientific transformation, not invisible hygiene

Van den Broeck et al. describe repeated screening, diagnosis, and editing,
emphasize that errors can enter at every data-flow stage—including during
cleaning—and recommend reporting cleaning methods, error types/rates,
deletions/corrections, and analyses with and without remaining outliers. They
also distinguish erroneous values, true extremes, true normal values, and
unresolved suspect values. Zuur et al. show that exploration should expose
outliers, heterogeneity, collinearity, dependence, zero structure, and other
model-relevant features before analysis.

**Contract consequence:** corrections, recodings, deduplication, exclusions,
outlier treatment, and imputation must be append-only decisions tied to units,
reasons, timing, and affected results/claims. A QC flag does not authorize
deletion. True adverse, harmful, null, or extreme observations remain visible
unless an evidence-backed exclusion rule applies.

**Allowed repairs:** diagnose against source records; correct with a receipt;
quarantine rather than erase; restore omitted units; rerun from the corrected
snapshot; report sensitivity with/without disputed values; disclose deviations;
or narrow/remove the dependent claim.

## 5. Missingness is not a blank cell problem

Sterne et al. explain that missingness can cause bias and loss of precision,
that complete-case analysis is not generally safe, and that missing-at-random
versus missing-not-at-random cannot usually be distinguished from observed data
alone. Multiple imputation requires a justified model and must propagate
uncertainty; sensitivity analyses are needed for unverifiable missingness
assumptions.

**Contract consequence:** bind missing-value codes, field/unit denominators,
missingness summaries, planned handling, realized handling, imputed-dataset
versions, and sensitivity results. The automatic evaluator checks contradiction
and lineage—not whether MAR, MNAR, or an imputation model is scientifically
correct.

**Repair boundary:** claim narrowing may address a bounded incomplete sample,
but it cannot manufacture missing observations, consent, or the planned primary
outcome. Preserve missingness as missing rather than silently filling it with a
single guessed value.

## 6. Quality assurance and quality control are different states

The mQACC recommendations distinguish preventive quality assurance—training,
SOPs, system suitability, calibration, and audits—from quality-control
observations such as reference materials, blanks, replicates, pooled samples,
and performance metrics. They explicitly avoid naming one universal best QC
threshold and instead require authors to report the criteria and evidence used.
The UK Biobank imaging work demonstrates a large-scale automated, modality-
specific processing and QC pipeline rather than a generic `qc_passed` flag.
Leek et al. show that batch effects may be widespread, outcome-confounded, and
not removed by ordinary normalization.

**Contract consequence:** store planned QC/QA, the actual receipt, threshold or
reference, result, batch/instrument/operator context, and consequence. If an
adapter marks calibration, blank/reference material, batch balance, or imaging
validation as required, `passed` without a receipt blocks. A failed required QC
result cannot be repaired by changing only the manuscript adjective.

**Transfer limit:** mQACC, UK Biobank, and FDA guidance are adapter evidence,
not universal thresholds. FDA CGMP guidance applies only to its regulated
scope. Unknown instruments or modalities trigger live domain research.

## 7. Community standards are powerful precisely because they are local

BIDS specifies organization and metadata for neuroimaging, supports automated
validation, and separates raw data from derivatives. REMBI proposes metadata
for biological images. MIAME defines minimum microarray information for
interpretation and independent verification. OME-NGFF discusses interoperable
metadata and original/derived image linkage while explicitly preserving format
trade-offs. Frictionless Table Schema expresses field types, constraints,
missing codes, and keys for tabular data.

**Contract consequence:** maintained adapters can require a current standard or
record an explicit non-applicability reason, but they cannot freeze one version
forever or force BIDS, REMBI, MIAME, OME-NGFF, or a tabular schema onto unrelated
data. The exact extension/specification, version, repository, and validation
receipt must be resolved live when consequential.

## 8. Documentation enables scrutiny but does not make a dataset good

Datasheets and Data Cards expose motivation, composition, collection,
preprocessing, filtering, missingness, intended use, limitations, distribution,
and maintenance. Data Cards explicitly treat transparency as contextual and
audience-specific, and distinguish documentation quality from dataset quality.
FAIR principles support machine and human discovery and reuse but do not certify
accuracy, ethics, or openness.

**Contract consequence:** require a data dictionary/datasheet or domain
equivalent for material datasets, but certify only that the declared fields and
lineage are present and internally checked. Never emit `dataset_unbiased`,
`dataset_complete`, `safe_to_use`, or `fit_for_all_uses` from a documentation
artifact.

## 9. Openness is not always the ethical objective

FAIR emphasizes findability and reusable access conditions, not unrestricted
download. CARE adds collective benefit, authority to control, responsibility,
and ethics for Indigenous data. Springer Nature and UK Data Service guidance
separate participant communication, technical protection, access governance,
and third-party rights. Rocher et al. provide strong empirical evidence that
removing direct identifiers and sampling do not automatically make rich data
anonymous. Qualitative-data sources add risks from contextual detail, voice,
text, relationships, and secondary interpretation.

**Contract consequence:** resolve sensitivity, consent, community authority,
rights, law, ethics, and intended release route independently. Public release of
data declared identifiable/sensitive without an authorized release basis is
blocking. Controlled access, trusted environments, safe outputs, synthetic or
representative data, metadata-only records, and justified non-release are valid
routes.

**Non-repairable by prose or claim narrowing:** lack of required authority,
consent, rights, or privacy protection. A narrower efficacy claim does not make
an unauthorized public dataset lawful or ethical.

## 10. Availability, FAIRness, and reproducibility are separate states

Federer et al. found that many PLOS ONE availability statements did not point
to repositories or contained insufficient locator information. Stodden et al.
obtained artifacts for 44% of a sample under an upon-request policy and
reproduced findings for 26%. Hardwicke et al. found that open data alone did not
ensure analytic reproducibility; unclear analytic procedures were a major
cause. Wallach et al. documented limited raw-data and protocol sharing in a
biomedical sample. Vines et al. show why person-dependent access decays over
time.

**Contract consequence:** keep separate:

- manuscript availability wording;
- repository object existence and resolution;
- rights/access-route validity;
- specific version/fixity;
- human/machine reusability;
- analytic reproducibility;
- scientific replication.

A DOI-looking string, `available upon request`, open-data badge, or FAIR label
does not satisfy all six.

## 11. Version of record, living datasets, and corrections

Scientific Data requires a static version representing what was peer reviewed,
separate from living updates, and describes correction or retraction routes when
availability materially changes. DataCite's versioning guidance distinguishes
versions and related identifiers. TRUST emphasizes preservation, sustainability,
transparent repository scope, and ongoing audit rather than one-time trust.

**Contract consequence:** bind every claim to the exact dataset version or
timeslice reviewed and analyzed. New releases do not overwrite the paper's
evidence object. Corrections add versions, relations, reasons, and affected
claims; withdrawals preserve tombstone metadata where the repository permits.

**Policy-date rule:** official pages observed current on 2026-08-28 are not
evidence that the same wording governed earlier work unless the authority gives
an explicit effective date. Exact journal, funder, institutional, legal, and
repository rules remain a live-resolution task.

## Maintained adapter evidence map

| Adapter | Primary evidence | Added obligations | Transfer boundary |
|---|---|---|---|
| general tabular/observational | `kahn-2016-dq`, `weiskopf-2013-ehr-dq`, `frictionless-table-schema`, `van-den-broeck-2005-cleaning` | dictionary/schema, keys, denominators, missingness, corrections, plausibility checks | no universal completeness/plausibility threshold |
| human/clinical sensitive | `springer-sensitive-data`, `ukds-anonymisation`, `rocher-2019-reidentification`, `sterne-2009-missing` | consent/authority, identifier risk, access route, missingness and attrition lineage | exact law, ethics, institution, and consent control |
| Indigenous/community-governed | `carroll-2020-care`, `wilkinson-2016-fair` | collective authority, benefit, responsibility, ethics, reuse conditions | resolve with the actual rights-holders |
| qualitative/interpretive | `hesse-2023-qualitative-sharing`, `kuula-luumi-2020-participants`, `ukds-anonymisation` | contextual identifiability, redaction/adjudication, consent and reuse boundary | open transcript release is not universal |
| computational benchmark | `gebru-2021-datasheets`, `pushkarna-2022-data-cards`, `hardwicke-2021-analytic` | upstream source/version, split/unit identity, preprocessing lineage, intended use/limits | documentation does not certify unbiasedness or generalization |
| high-throughput omics/metabolomics | `leek-2010-batch`, `broadhurst-2022-mqacc`, `brazma-2001-miame` | batch design, calibration/reference/QC receipts, current community metadata | thresholds and repositories are assay/version specific |
| biological/neuro imaging | `gorgolewski-2016-bids`, `sarkans-2021-rembi`, `moore-2021-ome-ngff`, `alfaro-2018-ukb-qc` | acquisition metadata, raw/derivative separation, format/validator/QC receipts | resolve modality and extension; no universal image QC |
| sensor/field/instrument | `broadhurst-2022-mqacc`, `van-den-broeck-2005-cleaning`, `wilson-2017-good-enough` | calibration, clock/unit/location, drift and environmental context, raw stream preservation | exact instrument standard requires live research |
| simulation/synthetic | `w3c-prov-overview`, `wilson-2017-good-enough`, `force11-data-citation` | generator/version/seed/config, input snapshot, stochastic replicate identity | traceability does not validate the model or realism |
| shared data resource/repository | `lin-2020-trust`, `scientific-data-policies`, `datacite-metadata`, `datacite-versioning` | persistent identity, preservation, licence/access, static reviewed version, update log | exact repository and venue requirements remain live |

## Automatic blocker evidence map

| Blocker | Evidence basis | Valid repair boundary |
|---|---|---|
| raw object changed or fixity mismatch | `rfc8493-bagit`, `force11-data-citation`, `wilson-2017-good-enough` | restore authoritative snapshot or version change; rerun descendants |
| broken/missing transformation edge | `w3c-prov-overview`, `ro-crate-1-1`, `hardwicke-2021-analytic` | reconstruct from receipts or rerun; prose is insufficient |
| analysis input differs from declared dataset | `force11-data-citation`, `hardwicke-2021-analytic` | bind/rerun correct version and regenerate results/displays |
| silent correction, exclusion, or adverse/null deletion | `van-den-broeck-2005-cleaning`, `sterne-2009-missing` | restore, append decision/reason, disclose, sensitivity, narrow claim |
| schema/unit/key drift | `frictionless-table-schema`, `kahn-2016-dq`, `gorgolewski-2016-bids` | reconcile dictionary and transform; rerun affected outputs |
| required QC/calibration declared pass without receipt | `broadhurst-2022-mqacc`, `alfaro-2018-ukb-qc`, `leek-2010-batch` | locate actual receipt or remeasure/rerun; otherwise mark unknown/failed |
| sensitive data routed to unauthorized public release | `rocher-2019-reidentification`, `springer-sensitive-data`, `ukds-anonymisation`, `carroll-2020-care` | authorized de-identification assessment, controlled route, safe output, or no release |
| third-party/collective rights absent | `carroll-2020-care`, `nature-reporting-standards`, `springer-sensitive-data` | secure authority/permission or remove/replace data; claim narrowing cannot create rights |
| release/version claim not resolvable | `federer-2018-statements`, `stodden-2018-policy`, `datacite-versioning`, `lin-2020-trust` | deposit/repair exact object and locator or state real restriction/unavailability |

## Certification boundary

A passing evaluator result means only that the recorded schema and bounded
identity, lineage, QC, governance, and release contradictions passed. It does
not certify:

- measurement accuracy or source-record truth;
- completeness, representativeness, or fitness for every use;
- absence of bias, batch effects, leakage, or data fabrication;
- anonymity, privacy, ethics, consent, rights, or legal compliance;
- correct statistical or computational analysis;
- analytic reproducibility or independent replication;
- FAIRness as a scalar achievement;
- acceptance by any journal or venue.

## Update triggers

Re-run targeted research when an official policy/specification changes, a
source is corrected/retracted/superseded, a new modality or governance class is
encountered, a blocker or repair route is challenged by stronger evidence, or
an exact institutional/legal/funder/repository/community rule is consequential.
The scheduled registry review is 2027-02-28.
