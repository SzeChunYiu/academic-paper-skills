# Research-integrity verification evidence ledger — 2026-08-30

## Scope

This note records the current external basis for the shared AI-writing research-integrity gate. It is not a claim that any registry or automated validator can guarantee truth. The design separates bibliographic identity/status checks from semantic claim-to-source verification and from manuscript-internal scientific checks.

## Expert synthesis

The design was reviewed through four roles:

1. **Research-integrity methodologist** — atomic claim scope, causal/inferential overreach, selective evidence, uncertainty and abstention.
2. **Scholarly-metadata engineer** — persistent identifiers, source identity, versions, corrections/retractions, multi-registry disagreement and metadata provenance.
3. **Adversarial LLM evaluator** — fabricated citations, semantic citation hallucination, self-grading failure, omitted-claim attacks, prompt injection/source poisoning and stale-verification replay.
4. **CI/reproducibility engineer** — fail-closed states, machine-readable receipts, immutable fingerprints, independent coverage, deterministic rechecks and final-artifact binding.

Consensus: no single check is sufficient. A DOI resolving does not establish semantic support; an LLM judgment does not establish independent verification; and a previously clean audit does not certify a later manuscript revision.

## Current evidence and authoritative infrastructure

### Crossref metadata and post-publication updates

Crossref documents its public REST API as exposing scholarly metadata deposited by members and trusted sources, including post-publication updates. A single Crossref DOI can be retrieved through the `/works/{doi}` route.

- https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/

**Pipeline implication:** resolve DOI identity against a registry record rather than reconstructing title/authors/year from model memory. Registry resolution is an identity check, not a claim-entailment check.

### Retractions, withdrawals, corrections and expressions of concern

Crossref's Retraction Watch production documentation says Retraction Watch data is available through Crossref services; Crossref documents update/retraction information in REST metadata and provides a separately downloadable dataset. The former Labs endpoint is explicitly deprecated/out-of-date.

- https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/
- https://www.crossref.org/labs/retraction-watch/

**Pipeline implication:** source status must be refreshed near release. Stored status receipts expire; a stale clean result cannot be replayed indefinitely. Retraction/withdrawal blocks ordinary evidentiary use. Corrections and expressions of concern require explicit adjudication.

### DataCite DOI metadata

DataCite documents a public REST API for retrieving DataCite DOI metadata, including single DOI lookup, with no authentication required for public retrieval.

- https://support.datacite.org/docs/rest-api
- https://support.datacite.org/docs/how-do-i-query-the-rest-api-and-whats-in-the-response

**Pipeline implication:** Crossref must not be treated as the universal DOI registry. DataCite provides a second route for datasets, software and other DataCite-registered research objects.

### PubMed retraction typing

PubMed documents `Retracted Publication` as a Publication Type.

- https://pubmed.ncbi.nlm.nih.gov/help/

**Pipeline implication:** PMID-indexed biomedical sources can be cross-checked against PubMed publication typing in addition to DOI metadata.

### OpenAlex independent retraction signal

OpenAlex exposes work-level bibliographic metadata and a retraction signal (`is_retracted`) in its Works model/API. The implementation uses OpenAlex only as an independent cross-check, never as proof of semantic support.

- https://help.openalex.org/
- https://api.openalex.org/

**Pipeline implication:** disagreement among registries must not be silently averaged away. A blocking status from an authoritative/independent source should trigger adjudication.

## 2026 evidence on LLM hallucination and citation verification

### Hallucinated citations are already entering scholarly literature

Nature reported on 1 April 2026 that an analysis suggested tens of thousands of 2025 publications might contain invalid AI-generated references. A later Nature report on 8 May 2026 described an audit of 2.5 million papers and 97 million references that identified thousands of biomedical papers with untraceable references.

- https://www.nature.com/articles/d41586-026-00969-z
- https://www.nature.com/articles/d41586-026-00748-w

**Pipeline implication:** reference existence/identity checks are release-critical rather than cosmetic bibliography QA.

### Accuracy incentives can reward guessing instead of abstention

Kalai, Nachum, Vempala and Zhang, *Nature* (published 22 April 2026), argue that standard accuracy/pass-rate evaluation can reward guessing over admitting uncertainty and propose explicit error penalties/abstention-aware evaluation.

- https://www.nature.com/articles/s41586-026-10549-w
- DOI: 10.1038/s41586-026-10549-w

**Pipeline implication:** `UNRESOLVED`/`BLOCKED` and claim narrowing are legitimate outcomes. The research pipeline should make unsupported confidence more costly than abstention.

### LLM-as-a-judge is not enough for citation attribution

Choi et al., ACL 2026, explicitly motivate retrieval-augmented citation validation partly because the reliability of LLM-as-a-judge alone is in doubt. Their CiteGuard work treats citation validation as grounded attribution rather than free-form model judgment.

- https://aclanthology.org/2026.acl-long.282/
- DOI: 10.18653/v1/2026.acl-long.282

**Pipeline implication:** a model's self-report is inadmissible as a verification method. Citation support should bind a claim to retrieved evidence, with an exact locator/fingerprint, and then receive independent review.

### Evidence-based generation lacks one universally sufficient metric

Schreieder, Schopf and Färber, ACL 2026, survey 134 papers and 300 evaluation metrics across attribution/citation/quotation and describe fragmented terminology and evaluation practice.

- https://aclanthology.org/2026.acl-long.1430/
- DOI: 10.18653/v1/2026.acl-long.1430

**Pipeline implication:** do not collapse research integrity into a single scalar "hallucination score." Use separate gates for existence, identity, status, entailment, scope, internal consistency, coverage and independent verification.

## Resulting controls

The shared gate therefore requires or recommends:

- retrieval-first source registration; no citation identifiers synthesized from memory;
- canonical source identity checks and current publication-status receipts;
- claim-to-source evidence locators plus SHA-256 fingerprints;
- semantic support states (`ENTAILS`, `BOUNDS`, `PARTIAL`, `CONTRADICTS`, `NOT_CHECKED`);
- independent claim-level verification;
- an independent coverage pass to detect claims omitted from the ledger;
- counterevidence searches for high-risk causal, clinical/safety, novelty/priority, headline quantitative, legal/policy and compliance claims;
- deterministic recomputation/cross-surface checks for numbers, units, figures, methods, data/code versions and proofs where applicable;
- exact-final-manuscript SHA-256 binding so verification cannot be replayed after an edit;
- freshness limits on stored source-status checks and optional live Crossref/DataCite/OpenAlex/PubMed refresh;
- retrieved sources treated as untrusted data, preventing source/PDF prompt injection from becoming agent instructions;
- fail-closed release: unresolved, contradicted or blocked claims prevent readiness rather than being guessed through.

## Transfer limits

- Metadata registries can contain incomplete or incorrect deposits.
- Retraction/correction signals can lag or disagree.
- A real source can still be misinterpreted.
- Semantic entailment and literature completeness can require expert judgment.
- Search coverage can never prove that no contradictory publication exists.
- Hashes bind evidence/artifacts to versions; they do not prove scientific validity.
- Independent AI review reduces correlated error only when it is genuinely context-separated and grounded; it is not a substitute for human/domain review when stakes require it.

Accordingly, a passing integrity ledger means **required checks completed with no recorded blocker**, not “100% truth proven.”
