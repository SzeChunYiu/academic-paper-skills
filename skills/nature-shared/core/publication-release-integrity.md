# Publication release integrity

> Fail-closed contract for resolving one current manuscript authority and binding
> a verified claim ledger to the exact reader-facing manuscript and submission
> package bytes. Use after scientific/manuscript closure and before any
> submission-ready, public-posting-ready, publication-ready, release, or exact
> mirror claim.

## Defect this contract closes

Manuscript correctness and package correctness are different questions.
Research-integrity verification can bind an atomic-claim ledger to one audited
file while a stale PDF, a different source tree, an obsolete manuscript, or an
archive containing extra historical files is delivered.

This is the **multiple manuscript/package authority** failure class. A directory
name such as `final`, a Git branch, a current-looking PDF, a passing source audit,
or a free-standing checksum file does not by itself resolve which object governs.

The required chain is:

```text
claim-ledger -> canonical manuscript -> submission package
```

Every arrow is an exact identity relation, not a prose assertion.

## Non-negotiable authority rule

Before release, inventory every plausible current manuscript candidate that a
reasonable maintainer could mistake for the live paper. Record its manuscript
ID, SHA-256 fingerprint, disposition and reason.

Allowed dispositions are:

- `authoritative` — the one reader-facing manuscript governing this release;
- `superseded` — replaced by a named successor but retained as provenance;
- `historical_provenance` — evidence of development, never current authority;
- `excluded_incompatible` — scientifically or structurally incompatible with
  the selected paper;
- `withdrawn` — removed from current authority without deleting history;
- `quarantined` — retained but ineligible pending resolution.

There must be **exactly one authoritative** manuscript candidate. A superseded
candidate names `superseded_by`; every non-authoritative disposition records why.
Do not merge claims merely because two candidates concern the same study.

Selecting manuscript authority does not upgrade scientific authority. Null,
adverse, harmful, retracted, contradicted, timed-out and bounded results remain
in the claim ledger and reader manuscript at their verified scope.

## Final-byte binding

Materialize a manifest conforming to:

```text
../release-contracts/publication-release-manifest.schema.json
```

Record for every release artifact:

```text
artifact ID
role
safe relative path
SHA-256 and byte count
```

The canonical `reader_manuscript` is the exact PDF or other file that reviewers
will read, not merely its LaTeX/Word/Markdown source. The `claim_ledger` artifact
must be the ledger that already passed the independent research-integrity gate.
Its `manuscript_id` must equal the selected authority, and its
`manuscript_fingerprint` must equal the canonical reader-manuscript SHA-256.
Its independent `coverage_check.reviewed_manuscript_fingerprint` must also equal
that same digest; co-location of an old review record inside a newly rehashed
ledger is not review of the final build.
The publication-release verifier re-runs the fail-closed research-integrity
verifier against those exact reader-manuscript bytes; a matching fingerprint
alone is insufficient. `public_posting_ready` is a release state and receives
the same non-closing-claim, independent-coverage, source-status and byte-binding
checks as submission or publication readiness.

Any edit, rebuild, metadata rewrite, linearization, signing step, archive rebuild,
or file replacement changes bytes and invalidates the affected binding. Rehash,
rerun dependent checks, and create a new release decision; never update only the
checksum text.

## Package modes

### File-set upload

Use `format: file_set` when the submission system receives independent files.
The declared member list is the exact upload set. Each member maps to one
hash-and-size-bound artifact, and the canonical reader manuscript must be in it.

### ZIP delivery

Use `format: zip` when a ZIP is the actual delivered or mirrored object. Bind:

- the ZIP's own SHA-256 and byte count;
- the complete non-directory member-name set;
- every central-directory entry whose name ends in `/` must be empty rather
  than a payload-bearing member disguised as directory metadata;
- each member to a declared artifact;
- each member's decompressed SHA-256 and byte count.

A missing or **unexpected package member**, duplicate member, stale manuscript,
or archive-byte mismatch blocks release. Do not include a competing manuscript
in the archive merely to preserve provenance; keep provenance outside the
submission package and record its disposition in the authority inventory.

## Release-payload privacy gate

Hash-safe paths in the manifest do not prove that delivered file contents are
free of workstation disclosure. Inspect every declared artifact and every member
of a declared ZIP artifact for high-confidence local absolute path families such
as macOS, Linux, or Windows user-home paths. A signed review receipt can be valid
repository-side provenance while still being unsuitable for delivery because it
records the reviewer's private candidate directory. Keep that exact receipt
outside the upload set and deliver only a sanitized digest plus a repository-
relative locator. The verifier blocks these path families without printing the
private value; this narrow gate is not a complete personal-data or anonymity
audit.

Persist the verifier-emitted release-manifest SHA-256 and byte count in the
governing release record. This binds the control manifest itself without creating
an impossible self-hash field inside that same manifest.

## Deterministic verification

Run from the directory containing the release manifest:

```bash
python ../path/to/nature-shared/scripts/verify_publication_release.py \
  publication-release-manifest.json --pretty
```

The verifier checks:

1. required identity fields and supported release state;
2. unique artifact, candidate and package-member identities;
3. one canonical authority and explicit competing-candidate dispositions;
4. local artifact hashes and byte counts;
5. claim-ledger manuscript ID/fingerprint/release-state synchronization;
6. a fresh fail-closed research-integrity verification of that ledger against
   the exact reader-manuscript bytes, including independent-review fingerprint
   identity;
7. exact file-set or ZIP membership;
8. canonical manuscript inclusion;
9. ZIP wrapper hash/size and member hash/size equality.

Run the verifier again on any exact mirror checkout or delivery directory. A
shared manifest plus a fresh `PASS` demonstrates byte identity of the recorded
objects; repository names, branch equality or copied checksums do not.

## Release rule

Do not use `submission_ready`, `publication_ready`, `public_posting_ready`,
`exact mirror`, or an equivalent release claim unless all applicable gates pass:

```text
scientific/atomic verification
+ current claim-ledger verification
+ exact target/package completeness
+ canonical authority resolution
+ publication release integrity PASS
+ final human visual/accessibility review of the bound reader manuscript
```

A missing candidate inventory, unresolved candidate, hash/size mismatch, stale
claim-ledger fingerprint, review fingerprint from an older candidate, incomplete
package member set, extra package file, or post-review/post-verification mutation
is `BLOCKED`. The repair is to resolve authority,
regenerate from the selected state where necessary, refresh the ledger, rebuild
the package, and rerun the full binding—not to relabel an old artifact.

## Certification boundary

A verifier `PASS` proves only that the recorded authority, ledger, artifact and
package identity checks succeeded for the bytes inspected.

It is **not a reproducible-build certificate**. It does not prove that source can
rebuild the PDF, that the science is true, that the venue rules are satisfied,
that rights/ethics/access are resolved, that an external repository accepted the
same bytes, or that a journal will accept the paper. Those remain separate gates.
