## Summary

Repository README/skill documentation is kept bilingual and validated so user-facing documentation does not drift away from the actual skill behavior.

## What it checks

The README validators cover:

- matching `README.md` / `README_EN.md` presence for skills
- matching heading counts for mirrored skill docs
- mirrored language-switch links
- proper title-first structure
- root README skill-count badge and index count
- `nature-shared` support-package wording and exclusion from the triggerable skill count

## Why

The repository now changes at the shared-contract level across journal routing, writing, figures, review, citation, and revision. Documentation drift can therefore misrepresent behavior even when the skill code/contracts are correct.

README validation should be treated as part of the architecture contract, not cosmetic cleanup.

## Validation

Run the current repository validators rather than preserving a historical hard-coded count:

```bash
python scripts/validate-readmes.py
python scripts/validate-readme-mirror.py
python scripts/validate-skill-index.py
```
