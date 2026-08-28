# Exact venue decision contract

> Operational contract for resolving how a particular venue decides a
> particular article type at a particular stage and date. Last reviewed:
> 2026-08-28.

## Why this layer exists

There is no universal journal acceptance function. Technical validity may be
the dominant gate at one venue, while another adds novelty, importance, or
interdisciplinary breadth. A third may publish a reviewed assessment rather
than make a conventional post-review accept/reject decision.

Resolve the exact decision tuple before giving target-specific advice:

```text
exact venue
× exact article/content type
× normalized stage
× effective/as-of date
```

Do not merge this target projection into the scientific assurance state. A
journal transfer changes the target objective and mechanics; it does not make
evidence stronger or weaker.

## Machine-readable assets

- `decision-contracts/venue-decision-contract.schema.json` — normative shape;
- `decision-contracts/profiles/*.json` — maintained exact snapshots;
- `decision-contracts/fallback-profiles.json` — non-exact planning profiles;
- `../../scripts/resolve_venue_contract.py` — tuple/date resolver and bounded
  criteria evaluator.

Maintained profiles currently demonstrate TMLR Research Papers, flagship
Nature Articles, and PLOS ONE Research Articles. This is deliberately not a
claim that all journals are hard-coded.

## Required contract fields

Every exact profile records:

1. exact venue identity and aliases;
2. exact article/content type and aliases;
3. applicable normalized stages;
4. effective-from/effective-until dates when the official source states them;
5. an explicit effective-date basis when the source does not state a date;
6. observed-active, reviewed, and next-review dates;
7. official source title, URL, authority, access date, and supported fields;
8. unresolved source conflicts;
9. scientific/eligibility gates;
10. novelty, impact, breadth, and audience-interest gates kept separate;
11. burden-of-doubt defaults and criterion-specific overrides;
12. allowed repair routes and whether each is explicit, conditional, or
    unresolved;
13. review model, decision owner, and vote rule;
14. author/reviewer AI use and confidentiality policy;
15. criteria-evaluation states and observed real decision labels;
16. any journal certification/annotation layer, separate from acceptance;
17. the nearest fallback profile for planning only.

An absent or unresolved policy is represented as absent or unresolved. Never
fill a required field from reputation, a sister journal, or a generic profile.

## Resolution precedence

Use the strongest applicable authority:

1. a live contract materialized from current official sources for the exact
   tuple;
2. an active maintained exact snapshot whose supported validity window covers
   the requested date;
3. a publisher/venue-family or publication-model fallback clearly labeled
   `profile_is_not_venue_policy`;
4. a generic scholarly default.

Live official-source resolution outranks a maintained snapshot. A fallback is
never promoted to exact policy, even when its behavior resembles the target.

## Live official-source resolution

For an unknown, stale, conflicting, submission-critical, or historically
unsupported tuple:

1. confirm the official venue domain and exact venue title;
2. confirm article/content type and normalized stage;
3. open current official author, editor/reviewer, decision-criteria, ethics,
   AI, and confidentiality pages;
4. record page titles, URLs, access dates, and any stated policy effective date;
5. if no effective date is stated, record that fact and the observed-active
   date—do not invent a historical start date;
6. map each contract field to one or more source IDs;
7. record conflicts and unknowns rather than resolving them by guess;
8. validate the materialized contract against the schema;
9. mark `provenance.resolution_mode` as `live_official_resolution`;
10. pass that record to the resolver as a live contract.

Example:

```bash
python skills/nature-shared/scripts/resolve_venue_contract.py \
  --venue TMLR \
  --article-type "Research Paper" \
  --stage initial_submission \
  --as-of 2026-08-28 \
  --live-contract /path/to/materialized-live-contract.json
```

The resolver does not scrape arbitrary pages and silently infer policy. Live
research requires semantic source review because official pages often divide
criteria across author, reviewer, ethics, and publisher-policy documents.

## Time semantics

- `effective_from` and `effective_until` are used only when supported by the
  source or an explicitly controlled fixture.
- `observed_active_at` means only that the policy was observed on that date.
  It cannot be back-cast to earlier dates.
- A future-effective contract is listed but not activated before its start
  date.
- An expired contract is provenance, not current guidance.
- When the requested date falls outside supported validity, resolve live or
  from an authoritative archive; do not select the nearest snapshot silently.

## Decision evaluation boundary

`evaluate_acceptance` is a deterministic comparison of supplied observations
against stated contract gates. Its successful state is
`contract_criteria_satisfied`, never `accepted` and never an acceptance
probability. The function:

- evaluates scientific gates before target-objective gates;
- applies only explicit burden-of-doubt rules;
- returns gate IDs rather than a prestige score;
- retains the target's non-universal objective ID;
- never evaluates a journal certification layer automatically;
- never claims to reproduce confidential editor judgement.

This makes behavioral differences inspectable. A sound, modest paper can
satisfy TMLR's evidence-plus-some-interest objective and PLOS ONE's rigorous
scholarly-record objective while failing Nature's independent novelty,
importance, or interdisciplinary-breadth gates.

## Repair routes

Do not translate every evidence/claim mismatch into “run more experiments.”
The exact contract can distinguish:

- add evidence;
- reanalyse;
- correct an error;
- clarify the argument or reporting;
- narrow a claim;
- remove a claim;
- change article type or venue;
- revise and re-review;
- appeal under an exact appeal policy.

TMLR explicitly permits claim reduction as an alternative to more evidence.
For a selective broad-interest target, scientifically necessary narrowing can
still expose a target-objective mismatch. The science repair remains valid even
when the target fit is lost.

## Acceptance and certification are separate

Acceptance states describe the venue's decision process. A certification,
badge, highlight, public assessment, or repository source-certification is a
different layer.

TMLR's Featured, Outstanding, and Reproducibility certifications annotate
accepted work and must not raise the ordinary acceptance bar. Nature and PLOS
ONE profiles record no equivalent article-level certification in the reviewed
exact sources. Resolver certification says only how the policy contract was
resolved; it does not certify the paper or predict acceptance.

## Maintenance rule

Add an exact profile only when repeated use justifies maintaining it. Keep old
snapshots for provenance, close their validity window when a superseding policy
is known, add the new snapshot, and add a behavior fixture for the change.

Never expand the profile directory into an unverified list of venue names.
Coverage is provided by maintained exact profiles **plus** live official-source
resolution, not by pretending every journal is already encoded.
