# Preprint-repository admissibility

A preprint server is a **moderated venue**, not a file host. It declines
manuscripts for what they are and for how they are packaged, independently of
whether the science is any good. Treat a deposit as a submission with its own
admissibility contract, resolved before the manuscript is written into a
package — never as an upload step at the end.

This contract exists because a pipeline that models journals as gated venues
and preprints as uploads has nowhere to catch a content-type refusal. That is a
real failure mode with a costly consequence: where a repository refuses on
content type, the author is typically told not to resubmit, and that an appeal
will be considered only once peer review has completed somewhere else. One
mislabelled deposit can therefore remove the preprint route for the life of the
manuscript.

## The rule that governs the decision

**A repository refuses a manuscript for what it IS. It is not persuaded by what
the manuscript CALLS itself, and it cannot be satisfied by renaming.**

Everything below follows from that.

## Resolve four things before packaging

1. **Target repository and primary category.** The category decides which rules
   apply at all. An unset category is not a deferred decision; it means no
   admissibility question has been answered.
2. **Cross-lists.** Rules scoped to an archive are evaluated against the
   cross-list too. Choosing a primary outside a restricted archive while
   cross-listing into it does not escape that archive's practice.
3. **Content type, from the evidence.** What the manuscript displays: a
   results-bearing section, a methods-bearing section, tables, figures,
   theorems, displayed derivations, availability statements.
4. **Whether a restricted type has its required documentation.** Where a
   repository admits a restricted content type only with completed peer review,
   the journal reference and DOI go in the submission metadata. Workshop review
   generally does not satisfy such a requirement.

## Declared type versus displayed content

Read both, and keep them apart. Agreement is evidence. Disagreement is a
finding, and **the direction decides what may be done about it**:

| Situation | Reading | Available remedy |
|---|---|---|
| Body carries primary research; surfaces call it a review, perspective or programme | The label **understates** the paper | Correct the label. This is legitimate and makes the submission more accurate. |
| Body carries no primary research; surfaces call it research | The label **overstates** the paper | **Relabelling is not available.** Either the manuscript gains primary research, or the route changes to one that accepts synthesis. |

A manuscript that denies reporting primary research in its backmatter while
displaying primary research in its body has one of the two wrong. A moderator
reads the sentence. Resolve it before depositing.

## Burden of proof runs one way

A content-type restriction excludes manuscripts that **are** reviews or position
pieces. It does not require every other manuscript to prove that it is not one.

So: fire on positive evidence of synthesis — an explicit self-label, an explicit
denial of primary research, heavy citation with no evidence display of its own,
sections that are predominantly synthesis. Never fire on a manuscript's failure
to look like a template. Terse theory papers, papers whose results sections are
named descriptively, and mathematics papers that display theorems rather than
measurements are all ordinary research and must pass.

## What this contract does not do

- **It does not predict a moderation decision.** A pass means no rule in the
  ruleset was triggered by the evidence supplied. It confers no authority.
- **It does not touch disclosure.** Where AI assistance is disclosed, that
  disclosure stays. No rule here rewards shortening or hiding it, and none
  should be added. Repositories cite generative AI as a cause of submission
  volume, not as an independent ground for refusing a submission.
- **It does not score prose.** Style is the writing skills' concern. Nothing
  here is keyed to a machine-text detector.

## Executable gates

Policy is data. The verifiers assert none of their own, and a ruleset past its
staleness horizon causes a refusal to certify rather than a silent application
of superseded rules.

| Step | Script | Meaning of a failure |
|---|---|---|
| Read what the manuscript displays | `scripts/detect_manuscript_content_type.py` | exit 2 only: the manuscript could not be read |
| Apply repository policy | `scripts/verify_preprint_admissibility.py` | 0 pass, 1 blocked, **2 could not evaluate** |
| Find hard artifacts | `scripts/audit_deposit_integrity.py` | 0 clean, 1 errors, 2 could not audit |

Rulesets live in `preprint-repositories/`. Each carries the source URL, the
retrieval date and the operative sentence verbatim. A rule that cannot be quoted
from a primary source does not belong in a ruleset.

**Exit code 2 is not a pass.** A deposit the gate could not assess must never be
recorded as one it assessed and cleared. Where a ruleset records a policy as
unverified for an archive, that is an open question, not clearance.

## Order of operations

Run admissibility **before** the package is built, not after. Category and
content type are inputs to how the manuscript is written and titled; discovering
a content-type problem after a package is frozen means rebuilding it, and
discovering it after a deposit is refused means losing the route.

1. Resolve repository, primary category and cross-lists.
2. Detect content type from the manuscript body.
3. Run the admissibility gate. Resolve every block and every cannot-evaluate.
4. Run the integrity audit. Resolve every error.
5. Build the package; then run whatever package-format checks the project has.

## Known limits, stated so they are not mistaken for coverage

- A manuscript that is substantively a survey, carries taxonomy tables, gives
  itself a neutral title and cites moderately can pass the content-type gate.
  The gate catches declared labels and strong structural cases; it is not a
  substitute for the author answering honestly what the manuscript is.
- Absence of a rule for an archive means the policy was not found, not that none
  exists.
- Repository practice changes without a migration period. The staleness horizon
  is the mechanism that stops this contract from going quietly out of date.
