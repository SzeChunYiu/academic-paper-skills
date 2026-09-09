#!/usr/bin/env python3
"""Check an abstract against every limit that can block the submission at once.

An abstract is usually the last thing anyone measures and one of the few places
where two venues impose *different, simultaneously binding* limits. A paper
going to a preprint server and a journal has to satisfy the tighter of the two,
and discovering that only at the submission form means rewriting the abstract
after the package is frozen.

Two units, deliberately kept apart because venues do not agree on one:

*Characters, for the repository.* arXiv states plainly that "abstracts longer
than 1920 characters will not be accepted; abridge your abstract if necessary"
(<https://info.arxiv.org/help/prep.html>). That is measured on the plain text a
submission form receives, after LaTeX markup is resolved, not on the source.

*Words, for the journal.* Most journal limits are stated in words, and the count
excludes markup for the same reason.

The tighter constraint is reported as the binding one, so an author writing to
200 journal words does not have to convert anything to know whether the
repository will also take it.

Reading the abstract is itself where this check fails silently. An abstract is
routinely `\\input` from its own file, held in YAML front matter, or written
under a `\\subsection` rather than a `\\section`. A reader that stops at any of
those measures an empty abstract and reports it as comfortably within limits,
which is the one outcome worse than not checking. Includes are resolved, four
markup conventions are tried, and **an abstract that cannot be located exits 2**
rather than passing.

Exit codes
    0  within every limit supplied
    1  over at least one limit
    2  the abstract could not be located, or inputs were unreadable
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCHEMA_VERSION = "manuscript.abstract-limits.v1"

# Repository character limits, with the source that states them.
REPOSITORY_LIMITS = {
    "arxiv": {
        "chars": 1920,
        "quote": ("abstracts longer than 1920 characters will not be accepted; "
                  "abridge your abstract if necessary"),
        "source": "https://info.arxiv.org/help/prep.html",
    },
}

BEGIN = re.compile(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", re.S)
SECT = re.compile(
    r"\\(?:sub)*section\*?\{\s*Abstract\s*\}\s*(?:\\label\{[^}]*\})?"
    r"(.*?)(?=\\(?:sub)*section|\Z)", re.S | re.I)
MD = re.compile(r"^#{1,3}\s*Abstract\s*$(.*?)(?=^#{1,3}\s|\Z)", re.S | re.I | re.M)
YAML = re.compile(r"^abstract:\s*[|>]-?\s*$(.*?)(?=^\S|\Z)", re.S | re.I | re.M)
INPUT = re.compile(r"\\input\{([^}]+)\}")


def plain(text: str) -> str:
    """Reduce LaTeX to the text a submission form would receive."""
    t = re.sub(r"%.*?$", "", text, flags=re.M)
    t = re.sub(r"\\(?:label|cite[a-zA-Z]*|ref|input|hypersetup)\s*\{[^}]*\}", "", t)
    t = re.sub(r"\\[a-zA-Z]+\s*", " ", t)
    # Math delimiters are markup: an author pasting the abstract into a form
    # types the symbol, not the dollars around it.
    t = t.replace("$", "")
    t = t.replace("{", " ").replace("}", " ").replace("\\", " ")
    return re.sub(r"\s+", " ", t).strip()


def flatten(body: str, lookup) -> str:
    """Resolve \\input up to a bounded depth so a separated abstract is seen."""
    for _ in range(4):
        if not INPUT.search(body):
            break
        body = INPUT.sub(lambda m: "\n" + lookup(m.group(1).strip()) + "\n", body)
    return body


def extract(body: str) -> str:
    for pattern in (BEGIN, SECT, MD, YAML):
        m = pattern.search(body)
        if m and plain(m.group(1)):
            return plain(m.group(1))
    return ""


def evaluate(abstract: str, repository: str | None, journal_words: int | None,
             journal_name: str | None) -> dict:
    chars, words = len(abstract), len(abstract.split())
    findings, limits = [], []

    if repository:
        spec = REPOSITORY_LIMITS.get(repository.lower())
        if spec is None:
            findings.append({
                "severity": "CANNOT_EVALUATE",
                "message": "no character limit recorded for repository %r; add it with "
                           "its source rather than assuming there is none" % repository,
            })
        else:
            limits.append(("%s characters" % repository, spec["chars"], chars))
            if chars > spec["chars"]:
                findings.append({
                    "severity": "ERROR",
                    "message": "%d characters, %d over the %s limit of %d. %s"
                               % (chars, chars - spec["chars"], repository,
                                  spec["chars"], spec["quote"]),
                    "source": spec["source"],
                })

    if journal_words:
        limits.append(("%s words" % (journal_name or "journal"), journal_words, words))
        if words > journal_words:
            findings.append({
                "severity": "ERROR",
                "message": "%d words, %d over the %s limit of %d"
                           % (words, words - journal_words,
                              journal_name or "journal", journal_words),
            })

    # Which limit binds first, expressed in the unit the author is writing in.
    binding = None
    if limits:
        headroom = [(name, lim, have, lim - have) for name, lim, have in limits]
        binding = min(headroom, key=lambda t: t[3])

    errors = [f for f in findings if f["severity"] == "ERROR"]
    return {
        "schema_version": SCHEMA_VERSION,
        "verdict": "OVER" if errors else "WITHIN_LIMITS",
        "characters": chars,
        "words": words,
        "limits_checked": [{"limit": n, "max": m, "actual": a} for n, m, a in limits],
        "binding_limit": (
            {"limit": binding[0], "max": binding[1], "actual": binding[2],
             "headroom": binding[3]} if binding else None),
        "findings": findings,
        "note": ("Characters are counted on plain text after markup is resolved, "
                 "because that is what a submission form receives."),
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--manuscript", required=True)
    ap.add_argument("--repository", default="arxiv")
    ap.add_argument("--journal-words", type=int, default=None)
    ap.add_argument("--journal-name", default=None)
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args(argv)

    path = Path(args.manuscript)
    if not path.is_file():
        print(json.dumps({"verdict": "CANNOT_EVALUATE",
                          "error": "manuscript not found: %s" % path}, indent=2))
        return 2

    root = path.parent
    body = path.read_text(encoding="utf-8", errors="replace")

    def lookup(target):
        for cand in (target, target + ".tex"):
            p = root / cand
            if p.is_file():
                return p.read_text(encoding="utf-8", errors="replace")
        return ""

    abstract = extract(flatten(body, lookup))
    if not abstract:
        print(json.dumps({
            "verdict": "CANNOT_EVALUATE",
            "error": "abstract not located in %s. This is reported as a failure, "
                     "never as within-limits: an abstract nobody could read has "
                     "not been measured." % path}, indent=2))
        return 2

    result = evaluate(abstract, args.repository, args.journal_words, args.journal_name)
    result["manuscript"] = str(path)
    payload = json.dumps(result, indent=2)
    if args.json_out:
        Path(args.json_out).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 1 if result["verdict"] == "OVER" else 0


if __name__ == "__main__":
    raise SystemExit(main())
