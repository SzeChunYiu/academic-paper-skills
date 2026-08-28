# Journal resolution contract

> Shared contract for `nature-writing`, `nature-polishing`, `nature-figure`, citation workflows, and any future academic-paper skill that must work beyond Nature Portfolio.
>
> Last reviewed: 2026-08-28.

## Core principle

A publisher family is **not** a manuscript format. A journal name is still not enough when the journal publishes multiple article types, and the same article can have different requirements at initial submission, revision, accepted-in-principle, and production stages.

For exact compliance and decision modeling, resolve this tuple before applying
house rules or acceptance objectives:

`exact journal -> article/content type -> submission stage -> effective/as-of date -> output component`

The backward-compatible house-style/mechanics projection remains:

`exact journal -> article/content type -> submission stage -> output component`

The decision-contract layer adds the effective/as-of date; it does not remove
the established output-component route.

Examples of output components are title, abstract, main text, references, figure, table, graphical abstract, supplementary file, cover letter, data/code statement, and response-to-reviewers package.

Never copy a rule from a flagship or sister journal merely because the publisher is shared.

## Resolution order

Use the first level that is sufficiently specific for the user's task.

### Level 1 — exact live journal instructions

Use when the user names a journal, asks whether a manuscript is submission-ready, asks for a word/reference/figure limit, needs a template, or requests final journal formatting.

1. Identify the exact journal title.
2. Identify the article/content type. Do not assume `Article`/`Research Article` exists or means the same thing everywhere.
3. Identify the stage: `planning`, `initial-submission`, `revision`, `accepted`, or `production`.
4. Open the current official journal instructions, template, or author portal.
5. For decision readiness, also open official editor/reviewer criteria, ethics,
   AI-use, and confidentiality policies rather than treating the author guide
   as the whole acceptance model.
6. Record page title, URL, access date, stated effective date, or an explicit
   `effective date not stated` status.
7. Materialize the result using
   [venue-decision-contract.md](venue-decision-contract.md) when exact decision
   criteria matter.
8. Apply only rules that are explicitly supported by the recorded sources.
9. If official pages conflict, prefer the page that is both more specific to
   the exact journal/content type and more specific to the current stage. Flag
   unresolved conflicts instead of guessing.

Do not rely on search snippets for exact limits when the official page itself is available.

### Level 2 — exact local profile

Use a versioned file in `journal-formats/` only when one exists for the exact target and its review date is acceptable for the job. Re-check the live guide for submission-critical or time-sensitive requirements.

Current exact profiles in this repository include flagship Nature, Nature Communications, and Nature Machine Intelligence.

Maintained machine-readable **decision** profiles additionally include bounded
snapshots for TMLR Research Papers, flagship Nature Articles, and PLOS ONE
Research Articles. A future-effective profile is never activated early, and an
observed-active snapshot is never back-cast before its observation date.

### Level 3 — publisher/venue family profile

Use `journal-family-profiles.md` for writing stance, likely workflow, template behavior, citation-family hints, and questions to check. Family profiles are **fallbacks**, not submission contracts.

Likewise, publication-model fallbacks in `editorial-decision-profiles.md` and
`decision-contracts/fallback-profiles.json` are not exact journal policy and
must trigger live official-source resolution for an exact readiness claim.

### Level 4 — discipline/reporting profile

When no stable journal-specific rule is available, preserve the conventions of the research community and study design. Examples:

- biomedical/clinical: structured reporting, study registration where applicable, participant/ethics detail, effect sizes and uncertainty, reporting checklists
- life science experimental: reproducible methods, resources/reagents, biological versus technical replicates, image integrity
- engineering/computer science: explicit problem definition, baselines, ablations, complexity/runtime, implementation detail, benchmark protocol
- physical science/materials: characterization, uncertainty, units, instrument settings, sample preparation, theory/experiment boundary
- social science/psychology: construct definition, preregistration/status where applicable, sampling, power/uncertainty, validated measures, limitations
- qualitative research: sampling rationale, reflexivity/positionality where relevant, coding/analysis procedure, saturation or alternative adequacy rationale
- humanities: argument/source architecture and discipline-specific notes/bibliography conventions rather than forced IMRaD

Use a recognized reporting guideline when the study design calls for one. A journal's visual style never overrides research-reporting obligations.

### Level 5 — generic scholarly default

When no target is known:

- optimize for accurate claims, readable structure, reproducibility, and field-appropriate terminology
- do not invent journal limits, citation punctuation, mandatory declarations, or file formats
- keep references in a structurally complete form (DOI/PMID/URL when available) and defer final punctuation/style conversion until a target is known
- use accessible figures and captions that remain understandable without relying on color alone
- preserve enough Methods/detail to support interpretation and replication

## Separate five concerns that are often conflated

Every consuming skill should keep these independent:

1. **Evidence selection** — which sources best support a claim.
2. **Scientific/argument structure** — how the paper makes and bounds its contribution.
3. **Reporting requirements** — what methods, ethics, statistics, data/code, and declarations must be present.
4. **House style** — wording, title/abstract preferences, citation rendering, heading conventions, figure/legend conventions.
5. **Submission mechanics** — templates, file types, anonymization, line numbers, upload order, source files, production checks.

A high-prestige journal filter must never be used as a proxy for evidence quality unless the user explicitly asks for that source restriction.

## Journal detection

Resolve a target from, in descending confidence:

1. exact journal title supplied by the user
2. manuscript/template metadata (journal name, class/package, Word template title)
3. submission portal or author-guide URL supplied by the user
4. explicit publisher/venue family (`IEEE`, `ACM`, `Cell Press`, `PLOS`, etc.)
5. citation/format clues — use only as a hypothesis, never as confirmation

If a manuscript is clearly already formatted for one journal but the user names another target, the user's named target wins.

Do not infer flagship `Nature`, `Science`, or `Cell` from phrases such as “top journal”, “CNS-style”, or “high impact”. Treat those as writing aspirations unless the target is explicit.

## Article-type resolution

The same journal can publish research articles, brief reports, reviews, perspectives, methods/resources, protocols, registered reports, letters, and other formats with different requirements.

Before enforcing exact limits, find the exact content type. If the user has not named it, infer only when the manuscript itself makes the type obvious; otherwise keep the draft structurally generic and mark the unresolved type in the compliance report.

## Stage resolution

Use these stage labels consistently:

- `planning` — argument/figure design before submission formatting
- `initial-submission` — first editor/reviewer-facing package
- `revision` — post-decision manuscript and correspondence
- `accepted` — accepted or accepted-in-principle, before production
- `production` — final source/figure/proof requirements

A production requirement must not be presented as an initial-submission requirement unless the official guide says so.

## Citation routing

Separate **source scope** from **rendering style**.

### Source scope

Default: `best-evidence`.

Search broadly across appropriate scholarly venues and rank candidates by direct support, study design, methodological quality, recency when relevant, and relevance to the exact claim.

Optional user-requested scopes include:

- exact journal
- publisher/venue family
- flagship-only
- date range
- study type
- open-access only
- primary research only / reviews only

Never silently restrict a general citation request to Nature/Science/Cell.

### Rendering style

Resolve separately from the target journal or requested style. Common families include:

- numeric sequence in brackets
- numeric superscript
- author-date
- author-number hybrids
- notes/bibliography

Do not guess punctuation, author truncation, journal abbreviation, title capitalization, or DOI presentation from the family alone when exact output is required. Prefer the current official journal guide, its official template/BibTeX/CSL style, or a trusted reference-manager style file.

Keep machine-readable metadata complete even when the rendered bibliography abbreviates it.

## Figure routing

For a named journal, resolve these independently:

- initial-review versus production file requirements
- single/double-column or page-width targets
- raster/vector file types and resolution
- font/line/label constraints
- color mode and accessibility expectations
- panel-label convention
- legend placement and content
- source-data requirements
- graphical-abstract/TOC-graphic eligibility
- image-integrity rules
- AI-generated or AI-assisted image policy

A visual corpus from one journal can inspire composition but cannot establish another journal's technical requirements.

## Writing and polishing routing

Journal adaptation should change only what the evidence supports:

- breadth of audience and assumed background
- title/abstract compression and framing
- section architecture and heading style
- degree of methodological detail in main text versus Methods/SI
- terminology/abbreviation density
- reference and display-item economy
- required front/back matter

It must **not** change facts, effect sizes, uncertainty, causal strength, novelty boundaries, or limitations to sound more like a prestigious journal.

## Compliance report

When exact journal compliance is requested, finish with a compact audit in four buckets:

- `verified` — requirement checked against an exact current source
- `applied` — manuscript/figure change made to satisfy it
- `unresolved` — journal/content type/stage or source conflict remains
- `not applicable` — checked but not relevant to this manuscript

For each exact numeric or mechanical requirement, retain enough source context to re-check later.

## Source-of-truth policy

Publisher and journal policies change. Local profiles are versioned knowledge, not immutable truth.

- Exact live author instructions outrank this file.
- Exact journal profiles outrank family profiles.
- Family profiles outrank generic defaults only for non-numeric, non-submission-critical guidance.
- When in doubt, preserve the manuscript's scientific validity and mark the formatting issue unresolved.
