#!/usr/bin/env python3
"""Fail-closed validator for AI-assisted academic research-integrity ledgers."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable
from xml.etree import ElementTree

ALLOWED_RELEASE = {"VERIFIED", "BOUNDED_INFERENCE", "COHERENT_DEFINITION", "NOT_APPLICABLE"}
FAIL_CLOSED = {"SUPPORTED_INTERNAL", "UNRESOLVED", "CONTRADICTED", "BLOCKED", "NOT_ASSESSABLE"}
SUPPORT_PASS = {"ENTAILS", "BOUNDS"}
SOURCE_WARRANTS = {"source", "literature"}
INTERNAL_WARRANTS = {"author_data", "analysis", "proof", "method_record"}
VERIFICATION_METHODS = {
    "registry_lookup",
    "publisher_or_primary_record",
    "fulltext_span_check",
    "deterministic_recompute",
    "deterministic_derivation",
    "human_review",
    "independent_model_with_retrieved_source",
    "authoritative_project_record",
}
SELF_ATTEST_METHODS = {"model_self_report", "authoring_model_judgment", "title_only", "metadata_only"}
HIGH_RISK_CLASSES = {
    "causal",
    "clinical_or_safety",
    "novelty_or_priority",
    "quantitative_result",
    "legal_or_policy",
    "availability_or_compliance",
}
STATUS_BLOCKING = {"RETRACTED", "WITHDRAWN"}
STATUS_WARNING = {"CORRECTED", "EXPRESSION_OF_CONCERN", "UNKNOWN"}
RELEASE_STATES = {
    "submission_ready",
    "publication_ready",
    "public_posting_ready",
    "simulated_publication_ready_for_target",
}


def norm_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").casefold()
    return " ".join(re.sub(r"[^\w]+", " ", value, flags=re.UNICODE).split())


def title_similarity(a: str, b: str) -> float:
    a, b = norm_text(a), norm_text(b)
    if not a or not b:
        return 0.0
    return 1.0 if a == b else SequenceMatcher(a=a, b=b).ratio()


def author_family(value: str) -> str:
    """Return a normalized family name from common scholarly name renderings."""
    raw = unicodedata.normalize("NFKC", value or "").strip()
    if not raw:
        return ""
    if "," in raw:
        family = raw.split(",", 1)[0].strip()
        return norm_text(family)
    normalized = norm_text(raw)
    return normalized.split()[-1] if normalized else ""


def datacite_creator_name(creator: dict[str, Any]) -> str:
    """Normalize DataCite creator metadata to Given Family when possible."""
    given = str(creator.get("givenName", "")).strip()
    family = str(creator.get("familyName", "")).strip()
    if given or family:
        return " ".join(x for x in (given, family) if x)
    rendered = str(creator.get("name", "")).strip()
    if "," in rendered:
        family_part, given_part = (x.strip() for x in rendered.split(",", 1))
        return " ".join(x for x in (given_part, family_part) if x)
    return rendered


def get_identifier(source: dict[str, Any], *schemes: str) -> str | None:
    wanted = {x.casefold() for x in schemes}
    for item in source.get("identifiers", []):
        if str(item.get("scheme", "")).casefold() in wanted:
            value = str(item.get("value", "")).strip()
            if value:
                return value.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    return None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def parse_checked_at(value: str) -> datetime | None:
    raw = (value or "").strip()
    if not raw:
        return None
    try:
        if raw.endswith("Z"):
            raw = raw[:-1] + "+00:00"
        parsed = datetime.fromisoformat(raw)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:
        return None


def status_check_is_fresh(check: dict[str, Any], max_age_days: int) -> bool:
    checked = parse_checked_at(str(check.get("checked_at", "")))
    if checked is None:
        return False
    age = (datetime.now(timezone.utc) - checked).total_seconds()
    return -86400 <= age <= max_age_days * 86400


def request_json(url: str, timeout: float, user_agent: str) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": user_agent, "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - fixed scholarly endpoints
        return json.load(response)


def crossref_lookup(doi: str, *, timeout: float, user_agent: str, mailto: str | None) -> dict[str, Any]:
    suffix = f"?mailto={urllib.parse.quote(mailto)}" if mailto else ""
    payload = request_json(
        f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}{suffix}", timeout, user_agent
    )
    message = payload.get("message", {})
    updates = [
        norm_text(str(x.get("type", "")))
        for x in (message.get("updated-by") or [])
        if isinstance(x, dict)
    ]
    status = "ACTIVE"
    if any("retract" in x or "withdraw" in x for x in updates):
        status = "RETRACTED"
    elif any("expression of concern" in x for x in updates):
        status = "EXPRESSION_OF_CONCERN"
    elif any("correct" in x or "update" in x for x in updates):
        status = "CORRECTED"
    issued = message.get("issued", {}).get("date-parts", [[None]])
    return {
        "provider": "crossref",
        "found": True,
        "doi": message.get("DOI", doi),
        "title": (message.get("title") or [""])[0],
        "authors": [
            " ".join(filter(None, [a.get("given", ""), a.get("family", "")])).strip()
            for a in message.get("author", [])
        ],
        "year": issued[0][0] if issued and issued[0] else None,
        "status": status,
        "raw_update_types": updates,
    }


def datacite_lookup(doi: str, *, timeout: float, user_agent: str) -> dict[str, Any]:
    payload = request_json(
        f"https://api.datacite.org/dois/{urllib.parse.quote(doi, safe='')}", timeout, user_agent
    )
    attrs = payload.get("data", {}).get("attributes", {})
    titles, creators = attrs.get("titles") or [], attrs.get("creators") or []
    return {
        "provider": "datacite",
        "found": True,
        "doi": attrs.get("doi", doi),
        "title": (titles[0].get("title") if titles else "") or "",
        "authors": [datacite_creator_name(c) for c in creators],
        "year": attrs.get("publicationYear"),
        "status": "ACTIVE" if attrs.get("isActive", True) else "UNKNOWN",
    }


def openalex_status(doi: str, *, timeout: float, user_agent: str) -> dict[str, Any]:
    params = urllib.parse.urlencode({"filter": f"doi:https://doi.org/{doi}", "per_page": 1})
    results = request_json(f"https://api.openalex.org/works?{params}", timeout, user_agent).get("results") or []
    if not results:
        return {"provider": "openalex", "found": False, "status": "UNKNOWN"}
    work = results[0]
    return {
        "provider": "openalex",
        "found": True,
        "doi": (work.get("doi") or "").removeprefix("https://doi.org/"),
        "title": work.get("title") or "",
        "year": work.get("publication_year"),
        "status": "RETRACTED" if work.get("is_retracted") else "ACTIVE",
    }


def pubmed_lookup(pmid: str, *, timeout: float, user_agent: str) -> dict[str, Any]:
    params = urllib.parse.urlencode({"db": "pubmed", "id": pmid, "retmode": "xml"})
    request = urllib.request.Request(
        f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?{params}",
        headers={"User-Agent": user_agent},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310
        root = ElementTree.parse(response).getroot()
    article = root.find(".//PubmedArticle")
    if article is None:
        return {"provider": "pubmed", "found": False, "status": "UNKNOWN"}
    title_node = article.find(".//ArticleTitle")
    pub_types = ["".join(x.itertext()) for x in article.findall(".//PublicationType")]
    authors = []
    for author in article.findall(".//Author"):
        name = " ".join(
            x
            for x in (
                (author.findtext("ForeName") or "").strip(),
                (author.findtext("LastName") or "").strip(),
            )
            if x
        )
        if name:
            authors.append(name)
    year_node = article.find(".//PubDate/Year")
    return {
        "provider": "pubmed",
        "found": True,
        "pmid": pmid,
        "title": "".join(title_node.itertext()) if title_node is not None else "",
        "authors": authors,
        "year": int(year_node.text) if year_node is not None and (year_node.text or "").isdigit() else None,
        "status": "RETRACTED"
        if any(norm_text(x) == "retracted publication" for x in pub_types)
        else "ACTIVE",
        "publication_types": pub_types,
    }


def compare_identity(source: dict[str, Any], record: dict[str, Any]) -> tuple[bool, list[str]]:
    problems: list[str] = []
    expected = source.get("bibliographic", {})
    if expected.get("title"):
        score = title_similarity(str(expected["title"]), str(record.get("title", "")))
        if score < 0.95:
            problems.append(f"title mismatch (similarity={score:.3f})")
    if expected.get("year") and record.get("year") and int(expected["year"]) != int(record["year"]):
        problems.append(f"year mismatch ({expected['year']} != {record['year']})")
    expected_authors = [str(x) for x in expected.get("authors", []) if str(x).strip()]
    actual_authors = [str(x) for x in record.get("authors", []) if str(x).strip()]
    if expected_authors and actual_authors:
        expected_family = author_family(expected_authors[0])
        actual_family = author_family(actual_authors[0])
        if expected_family and actual_family and expected_family != actual_family:
            problems.append(f"first-author mismatch ({expected_family} != {actual_family})")
    return not problems, problems


def live_verify_source(source: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    doi = get_identifier(source, "doi", "datacite_doi")
    pmid = get_identifier(source, "pmid")
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    if doi:
        try:
            records.append(crossref_lookup(doi, timeout=args.timeout, user_agent=args.user_agent, mailto=args.mailto))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"crossref: {exc}")
            try:
                records.append(datacite_lookup(doi, timeout=args.timeout, user_agent=args.user_agent))
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, json.JSONDecodeError) as dc_exc:
                errors.append(f"datacite: {dc_exc}")
        try:
            records.append(openalex_status(doi, timeout=args.timeout, user_agent=args.user_agent))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"openalex: {exc}")
    elif pmid:
        try:
            records.append(pubmed_lookup(pmid, timeout=args.timeout, user_agent=args.user_agent))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, ElementTree.ParseError) as exc:
            errors.append(f"pubmed: {exc}")
    else:
        return {"source_id": source.get("source_id"), "verifiable_online": False, "records": [], "errors": []}

    found = [x for x in records if x.get("found")]
    identity = []
    for record in found:
        ok, problems = compare_identity(source, record)
        identity.append({"provider": record.get("provider"), "match": ok, "problems": problems})
    statuses = {str(x.get("status", "UNKNOWN")).upper() for x in found}
    status = next(
        (
            x
            for x in (
                "RETRACTED",
                "WITHDRAWN",
                "EXPRESSION_OF_CONCERN",
                "CORRECTED",
                "ACTIVE",
            )
            if x in statuses
        ),
        "UNKNOWN",
    )
    return {
        "source_id": source.get("source_id"),
        "verifiable_online": True,
        "records": records,
        "identity_matches": identity,
        "status": status,
        "errors": errors,
    }


def require_keys(item: dict[str, Any], keys: Iterable[str], prefix: str, errors: list[str]) -> None:
    for key in keys:
        if key not in item or item[key] in (None, "", []):
            errors.append(f"{prefix}: missing required field {key}")


def validate_ledger(ledger: dict[str, Any], *, live: bool, args: argparse.Namespace) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    require_keys(
        ledger,
        (
            "schema_version",
            "manuscript_id",
            "manuscript_fingerprint",
            "coverage_check",
            "claims",
            "sources",
            "evidence_receipts",
            "citation_usages",
        ),
        "ledger",
        errors,
    )
    sources = {str(x.get("source_id")): x for x in ledger.get("sources", []) if x.get("source_id")}
    claims = {str(x.get("claim_id")): x for x in ledger.get("claims", []) if x.get("claim_id")}
    receipts = {
        str(x.get("receipt_id")): x for x in ledger.get("evidence_receipts", []) if x.get("receipt_id")
    }
    author = str(ledger.get("authoring_agent_id", "")).strip()
    release_requested = str(ledger.get("release", {}).get("requested_state", "draft")) in RELEASE_STATES

    if ledger.get("schema_version") != "1.0":
        errors.append("ledger: schema_version must be 1.0")
    if release_requested and ledger.get("verification_scope") != "full_manuscript":
        errors.append("ledger: release requires full_manuscript verification_scope")

    fingerprint = str(ledger.get("manuscript_fingerprint", ""))
    if not re.fullmatch(r"sha256:[0-9a-fA-F]{64}", fingerprint):
        errors.append("ledger: manuscript_fingerprint must be sha256:<64 hex>")
    manuscript = getattr(args, "manuscript", None)
    if manuscript:
        try:
            if sha256_file(Path(manuscript)).casefold() != fingerprint.casefold():
                errors.append("ledger: manuscript fingerprint does not match the audited manuscript")
        except OSError as exc:
            errors.append(f"ledger: cannot hash manuscript: {exc}")
    elif release_requested:
        errors.append("ledger: release requires --manuscript to bind verification to the exact final artifact")

    coverage = ledger.get("coverage_check", {})
    if coverage.get("status") != "PASS":
        errors.append("ledger: independent atomic-claim coverage_check must PASS")
    coverage_verifier = str(coverage.get("verifier_id", "")).strip()
    if not coverage_verifier:
        errors.append("ledger: coverage_check missing verifier_id")
    elif author and coverage_verifier == author:
        errors.append("ledger: coverage verifier must differ from authoring agent")
    if str(coverage.get("verification_method", "")) not in {
        "human_review",
        "independent_model_with_retrieved_source",
    }:
        errors.append(
            f"ledger: coverage_check uses inadmissible verification_method {coverage.get('verification_method')!r}"
        )

    for label, items, key in (
        ("source", ledger.get("sources", []), "source_id"),
        ("claim", ledger.get("claims", []), "claim_id"),
        ("receipt", ledger.get("evidence_receipts", []), "receipt_id"),
        ("citation", ledger.get("citation_usages", []), "citation_id"),
    ):
        ids = [str(x.get(key, "")) for x in items]
        for duplicate, count in Counter(ids).items():
            if duplicate and count > 1:
                errors.append(f"duplicate {label} id: {duplicate}")

    live_results: list[dict[str, Any]] = []
    max_age = int(getattr(args, "max_status_age_days", 30))
    for sid, source in sources.items():
        require_keys(
            source,
            ("source_id", "source_type", "identifiers", "bibliographic"),
            f"source {sid}",
            errors,
        )
        if not any(
            str(x.get("value", "")).strip()
            for x in source.get("identifiers", [])
            if isinstance(x, dict)
        ):
            errors.append(f"source {sid}: no stable or explicit identifier")
        require_keys(source.get("bibliographic", {}), ("title",), f"source {sid}.bibliographic", errors)

        adjudicated = source.get("status_adjudication", {}).get("status") == "PASS"
        declared = str(source.get("declared_publication_status", "UNKNOWN")).upper()
        if declared in STATUS_BLOCKING:
            errors.append(f"source {sid}: publication status is {declared}")
        elif declared in STATUS_WARNING:
            message = f"source {sid}: publication status is {declared}; dependent claims require explicit adjudication"
            (errors if release_requested and not adjudicated else warnings).append(message)

        identity_checks = source.get("identity_checks", [])
        status_checks = source.get("status_checks", [])
        for check in [*identity_checks, *status_checks]:
            require_keys(
                check,
                ("provider", "status", "checked_at", "verification_method", "verifier_id"),
                f"source {sid} check",
                errors,
            )
            method = str(check.get("verification_method", ""))
            if method in SELF_ATTEST_METHODS or method not in VERIFICATION_METHODS:
                errors.append(f"source {sid}: untrusted source-check verification_method {method!r}")

        identity_pass = any(str(x.get("status", "")).upper() == "MATCH" for x in identity_checks)
        all_statuses = {str(x.get("status", "UNKNOWN")).upper() for x in status_checks}
        fresh_statuses = {
            str(x.get("status", "UNKNOWN")).upper()
            for x in status_checks
            if status_check_is_fresh(x, max_age)
        }
        stored_blockers = sorted(all_statuses & STATUS_BLOCKING)
        stored_adverse = sorted(all_statuses & {"CORRECTED", "EXPRESSION_OF_CONCERN"})
        if stored_blockers:
            errors.append(
                f"source {sid}: stored publication-status check reports blocking status {', '.join(stored_blockers)}"
            )
        if stored_adverse:
            message = (
                f"source {sid}: stored publication-status check reports {', '.join(stored_adverse)}; "
                "requires explicit adjudication"
            )
            (errors if release_requested and not adjudicated else warnings).append(message)

        has_current_positive = "ACTIVE" in fresh_statuses or (
            "CORRECTED" in fresh_statuses and adjudicated
        )
        unresolved_adverse = bool(stored_blockers) or (
            bool(all_statuses & {"CORRECTED", "EXPRESSION_OF_CONCERN"}) and not adjudicated
        )
        status_pass = has_current_positive and not unresolved_adverse
        if release_requested and status_checks and not status_pass and not live:
            errors.append(
                f"source {sid}: stored publication-status check is invalid or older than {max_age} days"
            )

        live_identity = False
        live_status_pass = False
        if live:
            result = live_verify_source(source, args)
            live_results.append(result)
            if result.get("verifiable_online"):
                found = [x for x in result.get("records", []) if x.get("found")]
                if not found:
                    errors.append(f"source {sid}: identifier not resolved by configured live registries")
                live_identity = bool(result.get("identity_matches")) and any(
                    x.get("match") for x in result["identity_matches"]
                )
                if result.get("identity_matches") and not live_identity:
                    problems = "; ".join(
                        ", ".join(x.get("problems", [])) for x in result["identity_matches"]
                    )
                    errors.append(f"source {sid}: live metadata mismatch: {problems}")
                current = str(result.get("status", "UNKNOWN")).upper()
                if current in STATUS_BLOCKING:
                    errors.append(f"source {sid}: live status is {current}")
                elif current in STATUS_WARNING:
                    message = f"source {sid}: live status is {current}; requires explicit adjudication"
                    (errors if release_requested and not adjudicated else warnings).append(message)
                live_status_pass = current == "ACTIVE" or (current == "CORRECTED" and adjudicated)

        if release_requested and not (live_identity or identity_pass):
            errors.append(f"source {sid}: release requires a resolved identity check")
        if release_requested and not (live_status_pass or status_pass):
            errors.append(f"source {sid}: release requires a current publication-status check")

    for rid, receipt in receipts.items():
        require_keys(
            receipt,
            (
                "receipt_id",
                "claim_id",
                "warrant_type",
                "verification_method",
                "support_status",
                "scope_match",
                "verifier_id",
            ),
            f"receipt {rid}",
            errors,
        )
        cid = str(receipt.get("claim_id", ""))
        if cid not in claims:
            errors.append(f"receipt {rid}: unknown claim_id {cid}")
        method = str(receipt.get("verification_method", ""))
        if method in SELF_ATTEST_METHODS or method not in VERIFICATION_METHODS:
            errors.append(f"receipt {rid}: untrusted verification_method {method!r}")
        warrant = str(receipt.get("warrant_type", ""))
        if warrant in SOURCE_WARRANTS:
            source_id = str(receipt.get("source_id", ""))
            if source_id not in sources:
                errors.append(f"receipt {rid}: source warrant points to unknown source {source_id}")
            if not str(receipt.get("locator", "")).strip():
                errors.append(f"receipt {rid}: source warrant requires an exact locator")
            if not re.fullmatch(
                r"sha256:[0-9a-fA-F]{64}", str(receipt.get("evidence_fingerprint", ""))
            ):
                errors.append(f"receipt {rid}: source warrant requires sha256 evidence_fingerprint")
        elif warrant in INTERNAL_WARRANTS:
            if not str(receipt.get("artifact_pointer", "")).strip():
                errors.append(f"receipt {rid}: {warrant} warrant requires artifact_pointer")
        elif warrant not in {"definition", "not_applicable"}:
            errors.append(f"receipt {rid}: unknown warrant_type {warrant!r}")

    by_claim: dict[str, list[dict[str, Any]]] = {}
    for receipt in receipts.values():
        by_claim.setdefault(str(receipt.get("claim_id", "")), []).append(receipt)

    for cid, claim in claims.items():
        require_keys(
            claim,
            (
                "claim_id",
                "location",
                "text",
                "claim_class",
                "risk",
                "release_status",
                "independent_check",
            ),
            f"claim {cid}",
            errors,
        )
        release_status = str(claim.get("release_status", ""))
        if release_status in FAIL_CLOSED or release_status not in ALLOWED_RELEASE:
            errors.append(f"claim {cid}: non-closing release_status {release_status!r}")
        claim_receipts = by_claim.get(cid, [])
        if release_status != "NOT_APPLICABLE" and not claim_receipts:
            errors.append(f"claim {cid}: no evidence receipt")
        if claim_receipts and not any(
            str(x.get("support_status")) in SUPPORT_PASS
            and str(x.get("scope_match")) == "MATCH"
            for x in claim_receipts
        ):
            errors.append(f"claim {cid}: no scope-matched receipt with ENTAILS/BOUNDS support")
        if any(str(x.get("support_status")) == "CONTRADICTS" for x in claim_receipts):
            errors.append(f"claim {cid}: contradictory evidence receipt present")

        independent = claim.get("independent_check", {})
        if independent.get("status") != "PASS":
            errors.append(f"claim {cid}: independent_check must PASS")
        verifier = str(independent.get("verifier_id", "")).strip()
        if not verifier:
            errors.append(f"claim {cid}: independent_check missing verifier_id")
        elif author and verifier == author:
            errors.append(f"claim {cid}: independent verifier must differ from authoring agent")

        claim_class = str(claim.get("claim_class", ""))
        if str(claim.get("risk", "")) == "high" or claim_class in HIGH_RISK_CLASSES:
            if claim.get("counterevidence_search", {}).get("status") not in {"DONE", "NOT_APPLICABLE"}:
                errors.append(
                    f"claim {cid}: high-risk claim requires counterevidence_search DONE/NOT_APPLICABLE"
                )
            if claim_class in {
                "causal",
                "clinical_or_safety",
                "novelty_or_priority",
                "legal_or_policy",
            } and not any(str(x.get("warrant_type")) in SOURCE_WARRANTS for x in claim_receipts):
                errors.append(f"claim {cid}: high-risk external claim requires source evidence")

    for index, citation in enumerate(ledger.get("citation_usages", []), 1):
        prefix = f"citation_usage[{index}]"
        require_keys(citation, ("citation_id", "source_id", "location", "claim_ids"), prefix, errors)
        source_id = str(citation.get("source_id", ""))
        if source_id not in sources:
            errors.append(f"{prefix}: unknown source_id {source_id}")
        claim_ids = [str(x) for x in citation.get("claim_ids", [])]
        if not claim_ids:
            errors.append(f"{prefix}: citation is not mapped to any atomic claim")
        for cid in claim_ids:
            if cid not in claims:
                errors.append(f"{prefix}: unknown claim_id {cid}")
            elif not any(
                str(x.get("source_id", "")) == source_id for x in by_claim.get(cid, [])
            ):
                errors.append(f"{prefix}: source {source_id} has no evidence receipt for claim {cid}")

    cited = {str(x.get("source_id", "")) for x in ledger.get("citation_usages", [])}
    for sid, source in sources.items():
        if not source.get("bibliography_only") and sid not in cited:
            warnings.append(f"source {sid}: present in source registry but unused in citation_usages")

    return {
        "decision": "BLOCKED" if errors else "PASS",
        "error_count": len(errors),
        "warning_count": len(warnings),
        "errors": errors,
        "warnings": warnings,
        "live_source_checks": live_results,
        "summary": {
            "claims": len(claims),
            "sources": len(sources),
            "evidence_receipts": len(receipts),
            "citation_usages": len(ledger.get("citation_usages", [])),
        },
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate a fail-closed research-integrity ledger.")
    parser.add_argument("ledger", type=Path)
    parser.add_argument(
        "--manuscript", type=Path, help="Exact final manuscript/artifact whose SHA-256 must match the ledger"
    )
    parser.add_argument(
        "--online", action="store_true", help="Refresh DOI/PMID identity and retraction/status checks"
    )
    parser.add_argument("--max-status-age-days", type=int, default=30)
    parser.add_argument("--mailto", help="Contact email for Crossref polite-pool requests")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--user-agent", default="academic-paper-skills-integrity/1.0")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--pretty", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        ledger = json.loads(args.ledger.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(
            json.dumps({"decision": "BLOCKED", "errors": [f"cannot read ledger: {exc}"]}),
            file=sys.stderr,
        )
        return 2
    report = validate_ledger(ledger, live=args.online, args=args)
    rendered = json.dumps(report, ensure_ascii=False, indent=2 if args.pretty else None)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["decision"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
