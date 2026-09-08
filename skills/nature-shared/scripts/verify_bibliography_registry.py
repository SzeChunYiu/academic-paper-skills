#!/usr/bin/env python3
"""Verify a bibliography field by field against the DOI registry.

A fabricated or misattributed reference is among the most damaging things a
manuscript can carry. It is treated as a fatal integrity finding by editors, it
survives every check that only asks whether a bibliography exists, and it is
easy to introduce without meaning to: from recall, from a plausible-looking
suggestion, or by carrying an entry across from a different manuscript because
the topic looked close.

This verifier answers one question per entry: **does the record this entry
claims actually exist, and does it say what the entry says it says?**

Two design commitments make it worth running.

*It reads the file that will ship.* Not a list of candidates kept beside it, not
the notes a reference was chosen from. What can be wrong is what was typed into
the .bib, so that is what is checked.

*It never silently passes an entry it could not check.* An entry with no DOI is
reported separately as requiring a named non-registry basis, and an entry whose
`note` does not record one is called out as unacceptable rather than tolerated.
Some venues genuinely do not register DOIs, so absence of a DOI is not an error;
absence of any verification is.

Year comparison allows one specific benign disagreement: a registry record
deposited years after publication carries the deposit date, so a mismatch is
only reported when the venue name does not itself carry the year the entry
claims. Without that allowance every older conference paper reads as wrong.

Exit codes
    0  every entry with a DOI verified
    1  at least one entry disagrees with its registered record
    2  the bibliography could not be read
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = "orion-citation-verify/1.0 (mailto:sze-chun.yiu@fysik.su.se)"
# Entries are matched by balanced braces rather than by a closing "\n}",
# because a perfectly valid .bib written compactly ends its last field and the
# entry on the same line. The old pattern found zero entries in such a file and
# the run then reported "0 / 0 verified" and exited 0 — an unparsed bibliography
# passing as a checked one.
ENTRY = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.S)
FIELD_NAME = re.compile(r"(\w+)\s*=\s*")


def fields_of(body):
    """Parse `name = {value}` pairs with balanced braces.

    A line-terminated pattern misses every field in a compactly written entry,
    which silently drops its DOI and sends a perfectly checkable reference into
    the unverifiable bucket.
    """
    out = {}
    for m in FIELD_NAME.finditer(body):
        i = m.end()
        if i >= len(body):
            break
        if body[i] == "{":
            depth, j = 0, i
            while j < len(body):
                if body[j] == "{":
                    depth += 1
                elif body[j] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            out[m.group(1).lower()] = body[i + 1:j]
        elif body[i] == '"':
            j = body.find('"', i + 1)
            if j > 0:
                out[m.group(1).lower()] = body[i + 1:j]
        else:
            j = body.find(",", i)
            out[m.group(1).lower()] = body[i:j if j > 0 else len(body)]
    return out


# LaTeX accent macros, so a correctly-escaped BibTeX author matches the plain
# Unicode the registry returns. Without this every accented name is reported as
# a mismatch, which would make the check unusable for most of the world's
# authors and would train its reader to ignore it.
# Both spellings occur in real BibTeX: a braced argument (\'{o}, \H{o}) and a
# bare letter after the macro (\'o, \H o). Missing the second form reports
# Erd{\H o}s as a different author from Erdos.
_ACCENT = re.compile(
    r"\\[`'^\"~=.]\s*\{?([a-zA-Z])\}?"
    r"|\\[a-zA-Z]+\s*\{([a-zA-Z])\}"
    r"|\\[a-zA-Z]\s+([a-zA-Z])"
)
_LIGATURE = {"\\ss": "ss", "\\o": "o", "\\O": "O", "\\l": "l", "\\L": "L",
             "\\aa": "aa", "\\AA": "AA", "\\ae": "ae", "\\AE": "AE"}


def strip_latex(s):
    """Reduce LaTeX-escaped text to comparable plain letters."""
    for k, v in _LIGATURE.items():
        s = s.replace(k, v)
    s = _ACCENT.sub(lambda m: m.group(1) or m.group(2) or m.group(3), s)
    return re.sub(r"[{}\\]", "", s)


def fold(s):
    """Fold accented Unicode to ASCII so both sides compare on the same ground."""
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFKD", s)
                   if not unicodedata.combining(c))


def norm(s):
    s = fold(strip_latex(s))
    return re.sub(r"[^a-z0-9 ]", " ", s.lower())


def squash(s):
    return re.sub(r"\s+", " ", s).strip()


def _one(v):
    """CrossRef returns lists where CSL JSON returns strings; accept both.

    Joining a string here would compare the record character by character and
    report every doi.org-resolved entry as a title mismatch.
    """
    if isinstance(v, (list, tuple)):
        return " ".join(str(x) for x in v)
    return "" if v is None else str(v)


def _crossref(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["message"], "crossref"


def _doi_org(doi):
    """Content-negotiate CSL JSON at doi.org.

    CrossRef indexes only what CrossRef registers. Preprints registered through
    DataCite, arXiv's 10.48550 prefix among them, return an error there and
    would otherwise be reported as unverifiable — which for recent machine
    learning work is most of the literature a paper needs to cite. doi.org
    resolves every registered DOI regardless of registrar, so it is the correct
    fallback rather than a second guess.
    """
    url = "https://doi.org/" + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept": "application/vnd.citationstyles.csl+json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r), "doi.org"


def fetch(doi):
    """Return (record, registrar). CrossRef first; doi.org for everything else."""
    try:
        return _crossref(doi)
    except Exception:
        return _doi_org(doi)


def main(path):
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        print("cannot read: %s" % e)
        return 2

    rows, bad, nodoi = [], [], []
    entries = []
    for m in ENTRY.finditer(text):
        # Walk braces from the entry's opening brace so the body ends where the
        # entry ends, whatever the file's line discipline.
        i = text.index("{", m.start())
        depth, j = 0, i
        while j < len(text):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        entries.append((m.group(2).strip(), text[m.end():j]))

    if not entries and text.strip():
        print("CANNOT PARSE: no bibliography entries found in a non-empty file. "
              "This is reported as a failure, never as a clean run: a bibliography "
              "nothing could read has not been checked.")
        return 2

    for key, body in entries:
        f = {k: squash(v) for k, v in fields_of(body).items()}
        doi = f.get("doi")
        if not doi:
            nodoi.append((key, f.get("title", "")[:60], f.get("note", "")[:70]))
            continue
        try:
            m, registrar = fetch(doi)
        except Exception as e:
            bad.append((key, doi, "FETCH FAILED: %s" % e))
            continue
        reg_title = norm(_one(m.get("title")))
        my_title = norm(f.get("title", ""))
        authors = m.get("author") or []
        reg_first = (authors[0].get("family") if authors else "") or ""
        my_first = norm(f.get("author", "").split(",")[0]).strip()
        yr = None
        for k in ("published-print", "published-online", "issued"):
            v = m.get(k, {}).get("date-parts", [[None]])[0][0]
            if v:
                yr = v
                break
        container = _one(m.get("container-title"))

        problems = []
        key_words = [w for w in my_title.split() if len(w) > 3][:4]
        if not all(w in reg_title for w in key_words):
            problems.append("title: registry has %r" % squash(reg_title)[:60])
        if my_first and reg_first and my_first not in norm(reg_first):
            problems.append("first author: registry has %r, bib has %r" % (reg_first, my_first))
        my_year = f.get("year", "")
        if yr and my_year and str(yr) != my_year:
            # A deposit-date-only record is not a contradiction if the venue
            # name carries the year the entry claims.
            if my_year not in container:
                problems.append("year: registry %s vs bib %s (container %r)" % (yr, my_year, container[:40]))
        if problems:
            bad.append((key, doi, "; ".join(problems)))
        else:
            rows.append((key, doi, reg_first, my_year, ("%s via %s" % (container, registrar))[:44]))
        time.sleep(0.6)

    print("VERIFIED %d / %d entries with a DOI" % (len(rows), len(rows) + len(bad)))
    for k, d, a, y, c in rows:
        print("  %-32s %-30s %-12s %s  %s" % (k, d, a, y, c))
    if nodoi:
        print()
        print("NO DOI — requires a named non-registry verification (%d)" % len(nodoi))
        for k, t, n in nodoi:
            print("  %-32s %s" % (k, t))
            print("      basis: %s" % (n or "NONE RECORDED — not acceptable"))
    if bad:
        print()
        print("MISMATCH (%d) — these must not ship" % len(bad))
        for k, d, why in bad:
            print("  %-32s %-30s %s" % (k, d, why))
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
