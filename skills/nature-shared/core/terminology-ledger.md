# Terminology Ledger

A manuscript must use one name for one thing. The same method, model, dataset,
gene, metric, or concept must not drift across shifting names, spellings, or
capitalisation. Reviewers read inconsistent terminology as careless work, and a
term that changes between sections forces the reader to re-learn it.

Build the ledger **before** drafting or polishing prose, and treat it as the
single source of truth for the rest of the job. Consistency against a standard
is impossible if the standard was never written down.

## 1. Build the ledger on first contact

When you first receive a manuscript, draft, or set of notes, extract every
recurring domain term into a ledger before editing any prose:

- methods, models, systems, algorithms, modules, frameworks
- datasets, benchmarks, cohorts, materials, reagents
- genes, proteins, species, cell lines (respect established field nomenclature)
- metrics, units, statistical symbols, mathematical notation
- abbreviations and acronyms, each with its full form
- key concepts the paper defines or repeatedly relies on

For each term, record its canonical form, category, reader-facing identity,
first-use expansion/denotation, and any variants already present in the source.

Use these categories:

- established field term;
- coined/public term;
- public abbreviation or acronym;
- internal/private project label;
- formal symbol or notation;
- standardized identifier.

`Established` is not a bypass based on model memory. Judge it for the intended
reader and verify when the classification affects comprehension or release.

## 2. Present the ledger to the user

Show a compact table before or alongside the first output:

| Canonical term | Category | Intended reader / scientific identity | Public full form or denotation | First definition location | Standalone-surface status | Variants | Decision | Status |
|---|---|---|---|---|---|---|---|---|
| scRNA-seq | public abbreviation | sequencing assay | single-cell RNA sequencing (scRNA-seq) | Abstract, sentence 2 | PASS | "single cell RNA-seq", "scRNAseq" | spell out locally, then use scRNA-seq | PASS |

Flag every collision explicitly: the same concept under different names, or one
name reused for two different concepts. Ask the user to confirm the canonical
choice only when the decision is genuinely ambiguous or domain-sensitive.
Otherwise adopt the form the source uses most often and state that choice.

An internal label is not made reader-facing merely by listing it. Retain it in
manuscript prose only when it denotes a scientifically necessary, stable object
and the local text supplies a semantic identity/role. Otherwise translate it to
the scientific object, move it to artifact documentation, or omit it. Never
guess an unknown expansion; use `AUTHOR_INPUT_NEEDED` in draft notes instead.

## 3. Lock and enforce

Once set, the ledger is fixed for the whole job:

- Use only canonical forms in every output. Do not introduce synonyms to vary
  the prose. Terminology consistency outranks lexical variety in scientific
  writing.
- Define each abbreviation once, at first use, then use the short form.
- Keep units, symbols, and notation identical across every section.
- Define every nonstandard formal symbol by denotation and domain before or at
  its first claim-bearing use. An equality such as `kappa_X = 2` gives a value,
  not the meaning or quantifiers of `kappa_X`.
- When drafting or polishing a later section, reference the ledger built from
  the earlier sections instead of re-deciding term by term.
- If the user later renames a term, change every occurrence in the manuscript,
  not just the current passage, and update the ledger.

## 3b. Enforce standalone surfaces independently

The abstract, highlights, graphical-abstract text, figure legends, table notes,
and other detachable surfaces must be understandable on their own. A definition
in the Introduction does not satisfy first use in the abstract, and an abstract
definition does not automatically satisfy the body.

For each standalone surface:

1. inventory its abbreviations, coined terms, internal labels, and symbols;
2. mark whether each is scientifically necessary there;
3. expand/define it locally, replace it with reader-facing wording, or remove it;
4. record `PASS` or `BLOCKED` in the ledger.

Keep notation budgets proportional to the surface. A technically correct
abstract can still fail if readers must track many paper-private symbols before
they understand the question and result.

## 4. Do not invent terms

Do not coin new names for the author's methods, modules, or concepts. If a term
is missing, undefined, or used inconsistently in ways you cannot resolve from
the source, ask the user or flag it. Never fill the gap with a guessed name.
