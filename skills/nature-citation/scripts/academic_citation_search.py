#!/usr/bin/env python3
"""Journal-agnostic citation discovery for academic-paper-skills.

This module intentionally separates evidence scope from bibliography rendering.
By default it searches journal articles without a publisher-prestige filter.
Legacy Nature/Science/Cell scopes remain opt-in for users who explicitly request
them.

The script reuses the mature metadata/export helpers in nature_citation.py so the
new broad mode does not fork author-integrity, RIS/ENW/RDF, Crossref, or text-
segmentation logic.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import nature_citation as legacy


SCOPE_CHOICES = (
    "best-evidence",
    "nature",
    "science",
    "cell",
    "cns",
    "flagship",
)


def normalize(value: str) -> str:
    return " ".join((value or "").casefold().split())


def journal_matches(candidate: legacy.Candidate, journals: list[str]) -> bool:
    if not journals:
        return True
    actual = normalize(candidate.journal)
    return any(normalize(expected) in actual for expected in journals if expected.strip())


def scope_matches(candidate: legacy.Candidate, scope: str) -> bool:
    if scope == "best-evidence":
        return True
    legacy_scope = "cns" if scope == "cns" else scope
    return legacy.in_scope(candidate.journal, legacy_scope)


def candidate_rank(candidate: legacy.Candidate) -> tuple[float, int, int, int]:
    """Metadata-level rank only; scientific support still requires screening."""
    return (
        candidate.score,
        1 if candidate.abstract else 0,
        1 if candidate.doi else 0,
        1 if not candidate.author_warnings else 0,
    )


def search_query(query: str, args: argparse.Namespace) -> tuple[list[legacy.Candidate], list[str]]:
    errors: list[str] = []
    candidates: list[legacy.Candidate] = []
    queries = [query, *legacy.fallback_queries_from_segment(query)]
    seen: set[str] = set()

    for search_term in queries:
        key = normalize(search_term)
        if not key or key in seen:
            continue
        seen.add(key)
        try:
            items = legacy.retry_with_backoff(
                lambda: legacy.fetch_crossref(
                    search_term,
                    rows=args.rows,
                    mailto=args.mailto,
                    from_year=args.from_year,
                    to_year=args.to_year,
                ),
                max_retries=args.max_retries,
            )
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{search_term}: {exc}")
            continue

        for item in items:
            candidate = legacy.candidate_from_crossref(item, source_query=search_term)
            if candidate is None:
                continue
            if not scope_matches(candidate, args.scope):
                continue
            if not journal_matches(candidate, args.journal):
                continue
            candidates.append(candidate)

        if candidates:
            break

    deduped = legacy.dedupe(candidates)
    deduped.sort(key=candidate_rank, reverse=True)
    return deduped[: args.per_query], errors


def read_queries(args: argparse.Namespace) -> list[dict[str, str]]:
    work: list[dict[str, str]] = []

    for query in args.query or []:
        cleaned = legacy.clean_text(query)
        if cleaned:
            work.append({"kind": "query", "text": cleaned, "query": cleaned})

    for claim in args.claim or []:
        cleaned = legacy.clean_text(claim)
        if cleaned:
            work.append({"kind": "claim", "text": cleaned, "query": legacy.query_from_segment(cleaned)})

    text_parts: list[str] = []
    if args.text:
        text_parts.extend(args.text)
    if args.text_file:
        text_parts.append(Path(args.text_file).read_text(encoding="utf-8"))

    for text in text_parts:
        for segment in legacy.segment_text(text, max_chars=args.segment_chars):
            work.append(
                {
                    "kind": "segment",
                    "text": segment.text,
                    "query": segment.search_query,
                }
            )

    if not work:
        raise ValueError("Provide --query, --claim, --text, or --text-file.")
    return work


def write_export(
    candidates: list[legacy.Candidate],
    path: Path,
    export_format: str,
    allow_incomplete_authors: bool,
) -> None:
    if export_format == "ris":
        legacy.write_ris(candidates, path, allow_incomplete_authors=allow_incomplete_authors)
    elif export_format == "enw":
        legacy.write_enw(candidates, path, allow_incomplete_authors=allow_incomplete_authors)
    elif export_format in {"rdf", "zotero-rdf"}:
        legacy.write_zotero_rdf(candidates, path, allow_incomplete_authors=allow_incomplete_authors)
    else:
        raise ValueError(f"Unsupported export format: {export_format}")


def build_payload(args: argparse.Namespace) -> dict[str, Any]:
    work = read_queries(args)
    mapping: list[dict[str, Any]] = []
    all_candidates: list[legacy.Candidate] = []
    errors: list[dict[str, Any]] = []

    for index, item in enumerate(work, 1):
        candidates, query_errors = search_query(item["query"], args)
        all_candidates.extend(candidates)
        mapping.append(
            {
                "id": f"Q{index:03d}",
                "kind": item["kind"],
                "text": item["text"],
                "search_query": item["query"],
                "references": [candidate.as_dict() for candidate in candidates],
            }
        )
        if query_errors:
            errors.append({"id": f"Q{index:03d}", "errors": query_errors})

    unique_candidates = legacy.dedupe(all_candidates)
    unique_candidates.sort(key=candidate_rank, reverse=True)

    payload: dict[str, Any] = {
        "scope": args.scope,
        "journal_filter": args.journal or [],
        "from_year": args.from_year,
        "to_year": args.to_year,
        "query_count": len(mapping),
        "reference_count": len(unique_candidates),
        "queries": mapping,
        "references": [candidate.as_dict() for candidate in unique_candidates],
        "errors": errors,
        "notes": [
            "Default scope is best-evidence: no Nature/Science/Cell prestige filter is applied.",
            "Crossref relevance is discovery metadata, not proof that an article supports a claim.",
            "Screen abstracts/full text or publisher pages before citing a candidate as evidentiary support.",
            "Citation rendering is intentionally separate: apply the exact target journal/style after evidence selection.",
        ],
    }

    if args.export:
        export_path = Path(args.export)
        export_path.parent.mkdir(parents=True, exist_ok=True)
        write_export(
            unique_candidates,
            export_path,
            args.export_format,
            allow_incomplete_authors=args.allow_incomplete_authors,
        )
        payload["export"] = {
            "path": str(export_path),
            "format": args.export_format,
        }

    return payload


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=(
            "Search citation candidates across scholarly journals. Evidence scope and bibliography style are separate; "
            "the default search does not filter to prestige/publisher families."
        )
    )
    p.add_argument("--query", action="append", help="Direct literature query. Repeatable.")
    p.add_argument("--claim", action="append", help="Claim to turn into a search query. Repeatable.")
    p.add_argument("--text", action="append", help="Manuscript text to segment. Repeatable.")
    p.add_argument("--text-file", help="UTF-8 manuscript text file to segment.")
    p.add_argument("--scope", choices=SCOPE_CHOICES, default="best-evidence")
    p.add_argument(
        "--journal",
        action="append",
        help="Optional case-insensitive journal-title substring filter. Repeatable. Do not use unless requested.",
    )
    p.add_argument("--from-year", type=int)
    p.add_argument("--to-year", type=int)
    p.add_argument("--rows", type=int, default=30, help="Crossref rows fetched per query before filtering.")
    p.add_argument("--per-query", type=int, default=8, help="Maximum candidates retained per query/segment.")
    p.add_argument("--segment-chars", type=int, default=700)
    p.add_argument("--mailto", help="Contact email for Crossref polite-pool requests.")
    p.add_argument("--max-retries", type=int, default=2)
    p.add_argument("--export", help="Optional reference-manager export path.")
    p.add_argument("--export-format", choices=("ris", "enw", "zotero-rdf", "rdf"), default="ris")
    p.add_argument("--allow-incomplete-authors", action="store_true")
    p.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    return p


def main() -> int:
    args = parser().parse_args()
    try:
        payload = build_payload(args)
    except Exception as exc:  # noqa: BLE001
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
