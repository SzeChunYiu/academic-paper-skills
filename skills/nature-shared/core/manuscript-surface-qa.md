# Manuscript surface QA

> Final last-mile contract for manuscript prose, figure/table legends, titles, abstracts, Methods, Results, Discussion, equations, and submission-facing text. Use after scientific content, explanation depth, argument, and figure roles are stable. Last reviewed: 2026-08-25.

## Purpose

Content-selection rules can prevent repository details from entering a draft, but later rewriting can reintroduce them. A figure legend can suddenly contain `results/final_plot_v3.svg`; a Methods paragraph can inherit `scripts/train_model.py`; a Results sentence can name a helper function; an abstract can accidentally carry a repository URL. This contract therefore treats **artifact leakage and surface copy-editing as a final independent gate**.

The invariant is:

> A manuscript-facing surface must read as a scientific document even when the underlying project contains code, repositories, notebooks, scripts, configs, file trees, dashboards, tests, and build artifacts.

This gate is not a substitute for `manuscript-content-selection.md` or
`atomic-claim-verification.md`. It is the final catch after drafting and
scientific verification.

## Surfaces that must be audited

Audit all text that could be submitted or pasted into a manuscript:

- title and running title;
- abstract/summary;
- Introduction, Results, Methods, Discussion and Conclusion;
- section/subsection headings;
- figure callouts in body text;
- complete figure legends/captions;
- table titles/notes;
- equation introductions and explanatory prose;
- Extended Data/SI prose when it is paper-facing;
- acknowledgements/declarations when relevant;
- Data/Code/Resource Availability.

Also audit generated alt text or long descriptions if they will accompany the publication.

## Pass 0 - standalone-surface and terminology isolation

Read the abstract, highlights, legends, and table notes independently of the
body. For each surface:

- inventory abbreviations, coined terms, internal/private labels, and formal
  symbols;
- require a local reader-facing identity, full form, or denotation before
  claim-bearing use;
- remove a private label when a plain scientific description carries the same
  information;
- never infer an unknown expansion;
- check whether notation density obscures the question, result, or boundary.

A consistent token can still be opaque. `R6M`, a run name, or a paper-private
symbol is not publication-ready merely because it is used consistently.

### Abstract display-math rule

Resolve the exact target first. Some mathematical venues permit formulas, while
IEEE currently requires a self-contained single-paragraph abstract without
abbreviations or mathematical equations.

For an unknown target, prefer continuous prose and verbal or inline mathematics.
Use a displayed equation in an abstract only when all are true:

1. it is central to the result;
2. the target/genre permits it;
3. inline or verbal wording would lose necessary meaning;
4. every retained symbol is locally defined;
5. adjacent prose explains the scientific meaning.

Short equalities/inequalities and multiple display blocks are review signals,
not universal errors. The source-level decision matters; a PDF line break is not
automatically a rendering bug.

## Pass 1 — artifact-token scrub

Flag likely repository/developer residue. A flag is a request for contextual review, not an automatic deletion.

### High-confidence residue

- local paths such as `/Users/...`, `/home/...`, `C:\\...`;
- repository paths such as `src/...`, `scripts/...`, `tests/...`, `configs/...`;
- script/notebook/config filenames such as `.py`, `.ipynb`, `.yaml`, `.yml`, `.json`, `.sh`, `.toml`, `.ini`, `.cfg`;
- helper or class paths such as `module.Class.method()`;
- backticked code identifiers copied into prose when a scientific term exists;
- CLI flags such as `--checkpoint-dir` or shell commands;
- branch, PR, issue, CI, unit-test, commit or build-history references;
- exact temporary/output filenames such as `fig2_final_v7.svg`, `metrics_test.csv`, `model_best.pt`;
- developer-only directory/module architecture;
- raw stack traces, exception names or debug output.

### Review-needed residue

- raw GitHub/GitLab repository URLs outside a designated availability/artifact section;
- package names when the prose really needs the scientific operation, not the package identity;
- dataset filenames when a stable dataset/accession/entity name would be clearer;
- software version/build strings outside Methods/Availability;
- internal variable names, model checkpoint labels, experiment-run IDs and configuration keys.

## Pass 2 — scientific translation

For every flagged token, choose one action.

### Translate

Replace implementation identity with scientific meaning.

Examples:

- `scripts/preprocess.py` -> the actual preprocessing operation;
- `calculate_site_auc()` -> site-level discrimination analysis;
- `configs/robustness.yaml` -> the scientifically consequential robustness settings;
- `model_best.pt` -> the selected model/checkpoint under the stated selection criterion;
- `src/calibration/` -> the calibration procedure if that procedure matters scientifically.

### Relocate

Put access/navigation material in one authoritative location:

- persistent repository/DOI/accession -> Code/Data/Resource Availability;
- reproduction commands -> artifact documentation or formal reproducibility appendix;
- exact file inventory -> repository README/data dictionary;
- environment/bootstrap instructions -> artifact docs;
- exhaustive parameter/config listings -> SI/artifact when genuinely useful.

### Retain with justification

A literal identifier may remain only when it is itself part of the scientific object or required for unambiguous access/reproduction.

Examples:

- a canonical database accession;
- a standardized gene/protein/variant identifier;
- a formally named software package central to the method;
- a public dataset release identifier;
- a file format or filename explicitly required by the target venue or artifact protocol;
- an API/interface name when software-interface design is itself an evaluated contribution.

Even then, avoid repeating it in multiple manuscript surfaces.

### Omit

Delete developer detail with no F1–F5 scientific function.

## Hard figure-caption and legend boundary

Figure legends are especially prone to leakage because plotting pipelines naturally know filenames, script names and output objects.

A paper-facing legend should never mention an internal rendering filename merely because the figure generator knows it.

Bad manuscript-facing text:

`Panel b was generated by scripts/plot_auc.py from outputs/site_metrics.csv.`

Scientific translation:

`b, Site-level discrimination across external validation cohorts; points show cohort estimates and bars show 95% confidence intervals.`

Operational provenance belongs in source-data/artifact metadata, not in the legend.

Do not place these in legends unless scientifically required:

- plot script names;
- local/source image filenames;
- notebook names;
- export filenames;
- build versions;
- folder paths;
- helper-function names;
- command-line invocations;
- repository navigation instructions.

For adapted/reused third-party material, retain the required citation/permission attribution because that is publication provenance, not leakage.

## Hard body-text boundary

A manuscript sentence should normally name:

- the scientific operation;
- the data/entity/population;
- the comparison or estimator;
- the evidence/result;
- the relevant uncertainty/boundary.

It should not narrate how the project repository is organized.

When a software package is central, introduce it as a scientific method/tool once, then describe subsequent operations scientifically rather than repeatedly restating package or module names.

## Availability-section exception

Data/Code/Resource Availability is the correct place for authoritative access identifiers. In this section, persistent URLs, accessions, package/release names, archive versions and commits may be appropriate.

Even here:

- prefer durable archive/DOI/release links over local paths;
- do not dump the directory tree;
- do not paste installation instructions unless the venue explicitly expects an artifact appendix;
- give one canonical access path rather than repeating links.

## Pass 2b - release placeholders and authoring residue

In draft mode, keep unresolved facts in author-facing notes rather than fluent
manuscript assertions. In final/public/submission mode, unresolved placeholders
are release errors.

Review or block as appropriate:

- missing author/affiliation/title metadata;
- `TBD`, `AUTHOR_INPUT_NEEDED`, `[Evidence needed: ...]`, or
  `\\todo{...}` inside manuscript-facing text;
- `TK`, `TBC`, or `XXX` only in an authoring context such as `[TK]`,
  `Title: TK`, or `DOI: XXX`—not when they are legitimate scientific terms;
- `author/affiliation/DOI/URL/identifier to be supplied/inserted`;
- `Review source` or similar internal document-state labels in a public artifact;
- internal claim-governance prose such as a claim `receives` authority, a result
  `owns` an idea, or a proof `carries authority`, when ordinary scientific wording
  should state what is established and under which assumptions.

Do not match ordinary procedural prose merely because it contains `must be
inserted`; the placeholder object and authoring context must be present.

## Pass 3 — punctuation and typography QA

Punctuation errors are copy-editing defects, not rhetorical style. Run this pass after the scientific text is stable.

### Mechanical checks

Flag and repair when unambiguous:

- doubled punctuation such as `,,`, `;;`, `::`, accidental `..`;
- spaces before commas, periods, semicolons, question marks or exclamation marks;
- missing spaces after sentence punctuation where the next token is prose;
- unmatched parentheses/brackets/quotation marks;
- repeated spaces;
- inconsistent punctuation at the end of parallel list items;
- punctuation stranded outside/inside parentheses inconsistently within the same grammatical pattern;
- broken figure references such as `Fig.. 2`, `Fig  2`, `Fig.2` when the target uses `Fig. 2`;
- malformed statistical expressions caused by punctuation/spacing edits.

### Meaning-sensitive checks

Do not auto-fix without context:

- comma placement that changes restrictive/non-restrictive meaning;
- semicolon versus period;
- colon placement;
- hyphenation of scientific compounds;
- slash versus `per` or ratio notation;
- punctuation around quotations;
- punctuation around citations;
- serial comma policy;
- equation-final punctuation;
- capitalization/punctuation of figure titles.

Resolve these from normal English grammar plus exact target style.

## Scientific punctuation distinctions

### Hyphen, en dash and minus sign

Do not treat these as interchangeable.

- hyphen: compound formation where required (`dose-dependent`, target/style dependent);
- en dash: ranges or paired relationships when the target uses it (`5–10 min`, `Ni–Co` in IEEE-style contexts);
- minus sign: negative numeric values (`−80 °C`) in publication typography.

Exact journal production rules override generic defaults. Do not convert every ASCII hyphen mechanically because hyphens also occur in identifiers and chemical/biological names.

### Colon

Use a colon when the second unit genuinely explains, specifies or enumerates the first. Do not use colons as default AI-style sentence glue.

### Semicolon

Use when it clarifies a relationship between independent clauses or separates complex list elements. Do not chain many semicolons to avoid making sentence structure explicit.

### Parentheses

Parentheses should contain genuinely secondary material. If the parenthetical contains a premise needed for the main inference, integrate it into the sentence.

### Equations

Treat displayed equations as grammatical elements of surrounding prose. Apply target-specific equation punctuation rather than assuming one publisher's convention. IEEE, for example, has explicit mathematics punctuation rules; other venues may differ.

### Citations

Citation punctuation/order is target-specific. Never globally move citations before/after punctuation without resolving the target style.

## Units, numbers and symbols

Surface QA also checks common punctuation-adjacent numeric problems:

- consistent space between number and unit where required by target/SI convention;
- consistent minus sign;
- ranges not confused with subtraction;
- percentages and confidence intervals formatted consistently;
- `n`, `P/p`, test statistics and mathematical symbols styled consistently with the target;
- no commas accidentally inserted into accession/position identifiers;
- thousands separators and decimal marks consistent with target language/style.

## Pass 4 — sentence-boundary sanity

Many punctuation mistakes are symptoms of sentence-boundary problems.

Flag:

- fragments created by deleting a clause during compression;
- comma splices;
- one sentence carrying several unrelated claims joined by commas/semicolons;
- a colon followed by material that does not specify the preceding clause;
- parentheses that contain the main scientific action;
- long lists whose parallel grammar has broken during revision.

Repair the syntax, not just the mark.

## Pass 5 - final manuscript-only read

Before delivery, read the manuscript **without looking at the repository**.

Ask:

1. Could any filename/path/helper/command only be understood by someone who has the project tree open?
2. Does each software/repository mention perform a scientific or access function?
3. Could an internal identifier be replaced by the scientific object it represents?
4. Are access links concentrated in their designated section?
5. Do legends describe scientific displays rather than the plotting pipeline?
6. Are punctuation and bracket pairs mechanically clean?
7. Does punctuation clarify the logic rather than mask a sentence-structure problem?
8. Did copy-editing alter a scientific identifier, equation, range, citation or chemical/biological name?
9. Can the abstract be understood without definitions supplied only in the body?
10. Does any coined/internal label lack a scientific identity or reason to remain?
11. Does any symbol have a value but no denotation/domain/quantifiers?
12. Does any draft placeholder or internal document-state label remain?

The manuscript should pass this read independently of the codebase.

## Pass 6 - rendered PDF/artifact review when delivered

Source-text scanning does not preserve pagination or visual hierarchy. When a
PDF or other rendered submission artifact is delivered:

1. render and inspect every page, including the abstract and final page;
2. check gratuitous abstract display breaks, sparse spill pages, stranded
   headings, clipped/overlapping text, and reference pagination;
3. inspect document metadata for a real title and author information;
4. check tagged/accessibility state when the target or workflow requires it;
5. rerun placeholder and availability checks on extracted text while treating
   extraction-only spacing/math artifacts as non-authoritative;
6. verify the rendered artifact matches the audited source version.

## Interaction with other contracts

Run after:

- `manuscript-content-selection.md` for scientific admission/placement;
- `explanatory-sufficiency.md` for explanation depth;
- `natural-scholarly-prose.md` for sentence flow/voice;
- `figure-evidence-planning.md` for figure necessity and evidence roles.
- `atomic-claim-verification.md` for content-level claim/proof closure.

This contract is the final **surface hygiene** layer.

## Automation boundary

A linter can safely flag high-confidence artifact tokens and mechanical
punctuation patterns. It can also surface display math inside a detected abstract,
candidate opaque/unexpanded identifiers, and paper-private Greek symbols with
alphanumeric labels, but those findings remain review-only because target rules
and field terminology vary. It cannot decide
whether a package/name is scientifically necessary, whether a hyphen belongs in
a field-specific term, or whether a comma changes meaning. Automated findings
must therefore be reviewed in context and reconciled with the Terminology Ledger.

Use `scripts/audit_manuscript_surface.py` for a conservative scan when plain
text, Markdown, Pandoc YAML, or LaTeX is available. Pass `--final` only for
public/submission-ready surfaces so unresolved placeholders become errors.
`--strict` fails on error-severity findings; `--fail-on-review` is the more
conservative candidate gate and fails while any contextual-review item remains.
The latter intentionally disallows `--known-identifier`: standard-term and
target-permitted-display dispositions must be recorded in the terminology/audit
ledger, because a token exemption is not evidence. In non-gating exploratory
scans, repeated `--known-identifier` arguments can reduce verified field-term
noise without hard-coding every discipline's identifiers.

## Non-negotiable output rule

For manuscript-facing deliverables, do not expose internal file/script/helper names in the prose merely because they appear in the source project or were used to create the output.

Operational traceability can be maintained separately in the audit record. **The audit record may name the artifact; the manuscript prose should name the science.**
