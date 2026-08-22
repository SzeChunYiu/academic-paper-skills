## Summary

The repository validates the root README skill index against the actual `skills/` directory so the public landing page stays synchronized with the installable system.

## What it checks

- README skill-index count matches the current number of triggerable skills
- Chinese and English index tables list the same skill directories in the same order
- each index link points to an existing skill README
- `nature-shared` remains an internal support package and is excluded from the triggerable-skill count
- the root badge count matches the actual directory state

## Validation

Do not preserve a historical hard-coded skill count in this note. Run:

```bash
python scripts/validate-skill-index.py
python scripts/validate-readmes.py
```

The validator reports the current count from the repository itself.
