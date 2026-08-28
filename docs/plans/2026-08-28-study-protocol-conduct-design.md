# Study Protocol and Conduct Decision Contracts — Design

## Purpose and boundary

This iteration makes the study record upstream of manuscript prose a first-class,
versioned object. Its job is to answer: what was planned, when was it frozen,
what was actually done, what changed, and which claims remain licensed? It does
not certify that the science is true, that a reporting checklist is complete, or
that a journal will accept the paper.

The system must not force a randomized-trial template onto observational,
computational, animal, qualitative, review, resource, theoretical, or exploratory
work. A common core records identity, timing, protocol and analysis-plan versions,
conduct receipts, deviations, ethics/governance, claim status, and provenance.
Maintained study-type adapters add bounded obligations. If no adapter applies,
the resolver returns an unresolved research need rather than silently selecting a
generic standard.

## Architecture

Use four layers:

1. A JSON Schema defines the portable study protocol/conduct object.
2. A maintained adapter catalog activates study-type obligations and cites a
   separate, time-versioned evidence registry.
3. A resolver/evaluator returns applicable obligations and fail-closed blockers
   for high-risk contradictions that can be checked without inventing science.
4. The academic-writing, paper-pipeline, and project-state surfaces route through
   this contract before Methods, Results, claims, figures, or readiness decisions.

The provenance path is:

`research question -> protocol version -> analysis-plan version -> conduct receipt
-> deviation ledger -> analysis/result -> claim`.

Registration, reporting-standard completion, schema validity, protocol
traceability, conduct traceability, scientific validity, and journal acceptance
remain separate state dimensions.

## Hard behaviors

The first evaluator blocks false prospective labels, undisclosed primary-outcome
changes, unverified randomized assignment execution, hidden blinding changes,
unlogged stopping/sample-size deviations, unreconciled exclusions or attrition,
omitted adverse events, computational train/test or preprocessing leakage,
confirmatory labels unsupported by timing, missing required ethics authority, and
overclaiming from an incomplete protocol record.

Every blocker returns evidence-preserving repair routes. Valid routes include
reconciling from authoritative records, disclosing and versioning a deviation,
running a prespecified or explicitly added sensitivity analysis, reclassifying an
analysis as exploratory/post hoc, narrowing a claim, or conducting a new
prospective study. Invalid routes include backdating, inventing receipts,
retroactively relabeling a primary outcome, deleting adverse/null observations,
or treating checklist completion as proof of validity.

## Evidence and update policy

Every adapter requires multiple relevant sources with read depth, supported
decisions, and transfer limits. Broad discovery is frozen in a query log;
source-specific synthesis is recorded in an evidence ledger. Empirical bias
studies support hard blockers more strongly than editorial preference. Official
reporting standards define record fields and disclosure expectations but cannot,
on their own, certify conduct quality.

The registry is reviewed by date. New standards or evidence create a new
version; they do not rewrite the historical basis of an already materialized
contract. Domain-specific gaps remain explicit research tasks.

