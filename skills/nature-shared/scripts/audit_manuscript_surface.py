#!/usr/bin/env python3
"""Conservative last-mile audit for manuscript-facing text.

The scanner flags likely repository/artifact leakage and high-confidence
mechanical punctuation defects. It also emits review-only candidates for
abstract display math and unexplained abbreviations/opaque identifiers. It does
not rewrite text and intentionally leaves meaning-sensitive grammar,
hyphenation, citation placement, and field-specific identifiers to contextual
review.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


AVAILABILITY_HEADINGS = {
    "data availability",
    "code availability",
    "data and code availability",
    "code and data availability",
    "resource availability",
    "software availability",
    "artifact availability",
    "data/code/resource availability",
}

CODE_EXTENSIONS = (
    "py", "ipynb", "yaml", "yml", "json", "sh", "toml", "ini", "cfg",
    "js", "ts", "tsx", "jsx", "rmd", "qmd", "bat", "ps1", "pt", "pth",
    "ckpt", "pkl", "joblib",
)

# Extensions that make a relative project path substantially less ambiguous than
# prose such as "test/retest" or "results/discussion". The scanner intentionally
# does not hard-fail every prefix/token pair.
PROJECT_FILE_EXTENSIONS = CODE_EXTENSIONS + (
    "csv", "tsv", "xlsx", "xls", "parquet", "feather", "h5", "hdf5", "npz", "npy",
    "svg", "pdf", "png", "jpg", "jpeg", "tif", "tiff", "eps",
    "md", "rst", "tex", "bib", "log", "txt",
)

PATH_PREFIXES = (
    "src", "script", "scripts", "test", "tests", "config", "configs",
    "asset", "assets", "output", "outputs", "result", "results", "build",
    "dist", "notebook", "notebooks",
)

COMMON_IDENTIFIERS = {
    "AI", "API", "CI", "DNA", "DOI", "HTTP", "HTTPS", "ISBN", "ISSN",
    "ML", "ORCID", "PDF", "RNA", "SI", "URL",
}

IDENTIFIER_TOKEN = r"[A-Z](?:[A-Z0-9-]{0,10}[A-Z0-9])"
SYMBOL_LABEL_TOKEN = r"[A-Z](?:[A-Z0-9-]{0,10}[A-Z0-9])?"
IDENTIFIER_CANDIDATE = re.compile(rf"\b{IDENTIFIER_TOKEN}\b")
FORWARD_IDENTIFIER_DEFINITION = re.compile(
    r"\b(?:[A-Za-z][A-Za-z0-9-]*)(?:\s+[A-Za-z][A-Za-z0-9-]*){1,10}"
    rf"\s*\((?P<identifier>{IDENTIFIER_TOKEN})\)"
)
REVERSE_IDENTIFIER_DEFINITION = re.compile(
    rf"\b(?P<identifier>{IDENTIFIER_TOKEN})\s*\("
    r"(?:[A-Za-z][A-Za-z0-9-]*)(?:\s+[A-Za-z][A-Za-z0-9-]*){1,10}\)"
)

LATEX_GREEK_NAMES = (
    "alpha|beta|gamma|delta|epsilon|varepsilon|zeta|eta|theta|vartheta|iota|"
    "kappa|lambda|mu|nu|xi|omicron|pi|varpi|rho|varrho|sigma|varsigma|tau|"
    "upsilon|phi|varphi|chi|psi|omega"
)
OPAQUE_GREEK_SYMBOL = re.compile(
    rf"(?P<symbol>(?:[Α-Ωα-ω]|\\(?:{LATEX_GREEK_NAMES}))"
    rf"(?:_?\{{(?:\\mathrm\{{)?{SYMBOL_LABEL_TOKEN}\}}?\}}|_?{SYMBOL_LABEL_TOKEN}))"
)

ABSTRACT_DISPLAY_MATH = re.compile(
    r"\$\$.*\$\$|\$\$|\\\[|\\begin\{(?:displaymath|equation\*?|align\*?|gather\*?|multline\*?)\}"
)

SUBMISSION_PLACEHOLDER = re.compile(
    r"\b(?:TBD|AUTHOR_INPUT_NEEDED)\b"
    r"|\[(?:TK|TBC|XXX)(?::[^\]]*)?\]"
    r"|\b(?:Title|DOI|Author|Affiliation)\s*:\s*(?:TK|TBC|XXX)\b"
    r"|\[(?:Evidence\s+needed|insert)[^\]]*\]"
    r"|\\todo\{[^}]*\}"
    r"|\b10\.X{3,}/(?:placeholder|TBD|XXX)\b"
    r"|^\s*Review\s+source\s*[-:]"
    r"|\b(?:author(?:\s+information)?|affiliation|DOI|URL|"
    r"(?:permanent\s+)?archival\s+identifier|persistent\s+identifier)\b"
    r".{0,60}\b(?:to\s+be\s+supplied|to\s+be\s+inserted|must\s+be\s+inserted)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Finding:
    line: int
    column: int
    kind: str
    severity: str
    text: str
    message: str
    availability_context: bool = False


def _section_heading_info(line: str) -> tuple[int, str] | None:
    m = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", line)
    if not m:
        return None
    heading = re.sub(r"\s+\{[^{}]*\}\s*$", "", m.group(1))
    heading = re.sub(r"[*_`]+", "", heading).strip().lower()
    level = len(re.match(r"^\s{0,3}(#+)", line).group(1))
    return level, heading


def _iter_context(lines: list[str]):
    in_fence = False
    availability = False
    availability_level: int | None = None
    abstract = False
    abstract_level: int | None = None
    latex_abstract = False
    plain_abstract = False
    yaml_abstract = False
    yaml_abstract_indent = 0
    for idx, line in enumerate(lines, 1):
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            yield idx, line, availability, True, abstract or latex_abstract
            continue
        if in_fence:
            yield idx, line, availability, True, abstract or latex_abstract
            continue

        context_line = re.sub(r"(?<!\\)%.*$", "", line)

        if yaml_abstract and line.strip():
            indentation = len(line) - len(line.lstrip())
            if indentation <= yaml_abstract_indent and (
                line.strip() in {"---", "..."}
                or re.match(r"^\s*[A-Za-z_][A-Za-z0-9_-]*\s*:", line)
            ):
                yaml_abstract = False

        yaml_match = re.match(
            r"^(?P<indent>\s*)abstract\s*:\s*(?P<style>[|>])\s*$",
            context_line,
            re.IGNORECASE,
        )
        if yaml_match:
            yaml_abstract = True
            yaml_abstract_indent = len(yaml_match.group("indent"))
        yaml_inline_abstract = bool(
            re.match(r"^\s*abstract\s*:\s*\S.+$", context_line, re.IGNORECASE)
            and not yaml_match
        )

        stripped = context_line.strip()
        if re.fullmatch(r"abstract\s*:?", stripped, re.IGNORECASE):
            plain_abstract = True
        elif plain_abstract and (
            re.match(r"^(?:\d+(?:\.\d+)*[.)]?\s+)?introduction\b", stripped, re.IGNORECASE)
            or re.match(r"^keywords?\s*:", stripped, re.IGNORECASE)
        ):
            plain_abstract = False

        if re.search(r"\\begin\{abstract\*?\}", context_line):
            latex_abstract = True

        heading_info = _section_heading_info(line)
        if heading_info is not None:
            level, heading = heading_info

            if heading == "abstract":
                abstract = True
                abstract_level = level
            elif abstract_level is not None and level <= abstract_level:
                abstract = False
                abstract_level = None

            if heading in AVAILABILITY_HEADINGS:
                availability = True
                availability_level = level
            elif availability_level is not None and level <= availability_level:
                availability = False
                availability_level = None

        yield idx, line, availability, False, (
            abstract or latex_abstract or plain_abstract or yaml_abstract or yaml_inline_abstract
        )

        if re.search(r"\\end\{abstract\*?\}", context_line):
            latex_abstract = False


def _iter_prose_lines(lines: list[str]):
    """Yield only non-fenced manuscript lines with original line numbers."""
    in_fence = False
    for idx, line in enumerate(lines, 1):
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield idx, line


def _add_regex_findings(
    findings: list[Finding],
    line_no: int,
    line: str,
    pattern: re.Pattern[str],
    kind: str,
    severity: str,
    message: str,
    availability: bool,
    downgrade_in_availability: bool = False,
) -> None:
    for match in pattern.finditer(line):
        sev = "review" if downgrade_in_availability and availability else severity
        findings.append(
            Finding(
                line=line_no,
                column=match.start() + 1,
                kind=kind,
                severity=sev,
                text=match.group(0),
                message=message,
                availability_context=availability,
            )
        )


def _audit_delimiters(findings: list[Finding], lines: list[str]) -> None:
    """Audit parentheses/brackets in prose only, ignoring fenced code entirely."""
    for opening, closing, kind in (("(", ")", "parentheses"), ("[", "]", "brackets")):
        stack: list[tuple[int, int]] = []
        for line_no, line in _iter_prose_lines(lines):
            for col, ch in enumerate(line, 1):
                if ch == opening:
                    stack.append((line_no, col))
                elif ch == closing:
                    if stack:
                        stack.pop()
                    else:
                        findings.append(
                            Finding(
                                line_no,
                                col,
                                f"unbalanced_{kind}",
                                "error",
                                ch,
                                f"Closing {kind} delimiter has no matching opener.",
                            )
                        )
        for line_no, col in stack:
            findings.append(
                Finding(
                    line_no,
                    col,
                    f"unbalanced_{kind}",
                    "error",
                    opening,
                    f"Opening {kind} delimiter has no matching closer.",
                )
            )


def _mask_nonprose_for_identifier_scan(line: str) -> str:
    """Mask common non-prose spans before heuristic identifier review."""
    masked = re.sub(r"https?://\S+", lambda m: " " * len(m.group(0)), line)
    masked = re.sub(r"\b10\.\d{4,9}/\S+", lambda m: " " * len(m.group(0)), masked)
    masked = re.sub(r"\[[0-9,;\s-]+\]", lambda m: " " * len(m.group(0)), masked)
    masked = re.sub(r"\$[^$]*\$", lambda m: " " * len(m.group(0)), masked)
    masked = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), masked)
    return masked


def _defined_identifiers(line: str) -> set[str]:
    return {
        match.group("identifier")
        for pattern in (FORWARD_IDENTIFIER_DEFINITION, REVERSE_IDENTIFIER_DEFINITION)
        for match in pattern.finditer(line)
    }


def _identifier_definition_starts(line: str) -> dict[str, list[int]]:
    starts: dict[str, list[int]] = {}
    for pattern in (FORWARD_IDENTIFIER_DEFINITION, REVERSE_IDENTIFIER_DEFINITION):
        for match in pattern.finditer(line):
            starts.setdefault(match.group("identifier"), []).append(match.start())
    return starts


def _normalize_opaque_symbol(symbol: str) -> str:
    normalized = symbol.replace("\\mathrm", "")
    return re.sub(r"[^A-Za-z0-9Α-Ωα-ω]+", "", normalized)


def _opaque_symbol_is_defined(line: str, match: re.Match[str]) -> bool:
    prefix = line[:match.start()]
    suffix = line[match.end():]
    numeric_only = re.compile(
        r"(?:the\s+)?(?:number|value|constant\s+value)?\s*(?:equal\s+to\s+)?[-+]?\d",
        re.IGNORECASE,
    )
    semantic_tail = re.match(
        r"\s+(?:denotes?|represents?|is\s+defined\s+as)\s+(?P<definition>[^.;,]+)",
        suffix,
        re.IGNORECASE,
    )
    if semantic_tail:
        return not bool(numeric_only.match(semantic_tail.group("definition").strip()))

    has_definition_lead = bool(
        re.search(r"\b(?:let|define|write|where)\s*$", prefix, re.IGNORECASE)
    )
    if not has_definition_lead:
        return False
    copular = re.match(
        r"\s+(?:(?:is|be)\s+|as\s+)(?P<definition>[^.;,]+)",
        suffix,
        re.IGNORECASE,
    )
    if not copular:
        return False
    definition = copular.group("definition").strip()
    # A bare value or equality does not supply denotation/domain/role.
    return not bool(numeric_only.match(definition))


def _display_math_lines(lines: list[str]) -> tuple[set[int], set[int]]:
    """Return all display-math lines and one opening line per display block."""
    inside: str | None = None
    math_lines: set[int] = set()
    opening_lines: set[int] = set()
    begin_re = re.compile(r"\\begin\{(?P<env>displaymath|equation\*?|align\*?|gather\*?|multline\*?)\}")
    for line_no, line in _iter_prose_lines(lines):
        if inside is not None:
            math_lines.add(line_no)
            if (
                (inside == "$$" and "$$" in line)
                or (inside == "\\[" and "\\]" in line)
                or (inside.startswith("env:") and re.search(rf"\\end\{{{re.escape(inside[4:])}\}}", line))
            ):
                inside = None
            continue

        dollar_count = line.count("$$")
        if dollar_count:
            math_lines.add(line_no)
            opening_lines.add(line_no)
            if dollar_count % 2 == 1:
                inside = "$$"
            continue
        if "\\[" in line:
            math_lines.add(line_no)
            opening_lines.add(line_no)
            if "\\]" not in line[line.index("\\[") + 2:]:
                inside = "\\["
            continue
        begin = begin_re.search(line)
        if begin:
            math_lines.add(line_no)
            opening_lines.add(line_no)
            env = begin.group("env")
            if not re.search(rf"\\end\{{{re.escape(env)}\}}", line[begin.end():]):
                inside = f"env:{env}"
    return math_lines, opening_lines


def _audit_wrapped_placeholders(
    findings: list[Finding],
    contexts: list[tuple[int, str, bool, bool, bool]],
    *,
    final: bool,
) -> None:
    """Catch placeholder phrases split by a hard line wrap."""
    for left, right in zip(contexts, contexts[1:]):
        left_no, left_line, left_availability, left_fence, _ = left
        right_no, right_line, _, right_fence, _ = right
        if right_no != left_no + 1 or left_fence or right_fence:
            continue
        if not left_line.strip() or not right_line.strip():
            continue
        joined = f"{left_line.rstrip()} {right_line.lstrip()}"
        boundary = len(left_line.rstrip())
        for match in SUBMISSION_PLACEHOLDER.finditer(joined):
            if not (match.start() <= boundary < match.end()):
                continue
            findings.append(
                Finding(
                    line=left_no,
                    column=match.start() + 1,
                    kind="submission_placeholder",
                    severity="error" if final else "review",
                    text=match.group(0),
                    message="Unresolved manuscript placeholder or internal document-state label split across lines; keep it only in an explicitly non-final draft note.",
                    availability_context=left_availability,
                )
            )


def audit_text(
    text: str,
    *,
    final: bool = False,
    known_identifiers: Iterable[str] = (),
) -> list[Finding]:
    findings: list[Finding] = []
    lines = text.splitlines()
    known = COMMON_IDENTIFIERS | {item.upper() for item in known_identifiers}
    seen_identifiers: dict[str, set[str]] = {"abstract": set(), "body": set()}
    reviewed_opaque_identifiers: dict[str, set[str]] = {"abstract": set(), "body": set()}
    defined_opaque_symbols: dict[str, set[str]] = {"abstract": set(), "body": set()}
    reviewed_opaque_symbols: dict[str, set[str]] = {"abstract": set(), "body": set()}
    previous_prose_line: dict[str, str] = {"abstract": "", "body": ""}
    contexts = list(_iter_context(lines))
    display_math_lines, display_math_openings = _display_math_lines(lines)

    ext = "|".join(map(re.escape, CODE_EXTENSIONS))
    project_ext = "|".join(map(re.escape, PROJECT_FILE_EXTENSIONS))
    prefixes = "|".join(map(re.escape, PATH_PREFIXES))

    # One literal backslash after a Windows drive letter is the normal path form.
    # Forward-slash Windows paths are also common in copied logs/scripts.
    local_path = re.compile(
        r"(?:/Users/|/home/|/tmp/|[A-Za-z]:[\\/])[^\s`'\"]+",
        flags=re.IGNORECASE,
    )

    # Hard-error relative repository paths only when they look like actual files.
    # This avoids false positives for ordinary scientific prose such as
    # "test/retest" and "results/discussion".
    repo_file_path = re.compile(
        rf"\b(?:{prefixes})/(?:[A-Za-z0-9_.@+\-]+/)*[A-Za-z0-9_.@+\-]+\.(?:{project_ext})\b",
        flags=re.IGNORECASE,
    )
    # Deep extensionless paths are still suspicious but are review-only because
    # slash-separated scientific notation can be legitimate in some fields.
    repo_nested_path = re.compile(
        rf"\b(?:{prefixes})/[A-Za-z0-9_.@+\-]+/[A-Za-z0-9_.@+\-/]+\b",
        flags=re.IGNORECASE,
    )

    code_file = re.compile(rf"(?<![\w/.-])(?:[A-Za-z0-9_.-]+\.)+(?:{ext})\b", re.IGNORECASE)
    cli_flag = re.compile(r"(?<!\w)--[a-z][a-z0-9-]*\b", re.IGNORECASE)
    code_call = re.compile(r"`(?:[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*\(\)|[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)+)`")
    dev_history = re.compile(
        r"\b(?:pull request|PR|issue)\s*#?\d+\b|\bbranch\s+[`'\"]?[A-Za-z0-9_./-]+|\bcommit\s+[0-9a-f]{7,40}\b|\bCI(?:/CD)?\s+(?:job|run|pipeline)\b",
        re.IGNORECASE,
    )
    repo_url = re.compile(r"https?://(?:www\.)?(?:github\.com|gitlab\.com)/[^\s)\]>]+", re.IGNORECASE)
    suspicious_output = re.compile(
        r"\b(?:fig(?:ure)?|plot|model|metrics?|predictions?|results?)[A-Za-z0-9_.-]*(?:final|best|latest|v\d+)[A-Za-z0-9_.-]*\.(?:svg|pdf|png|tiff?|csv|tsv|xlsx?|pt|pth|ckpt)\b",
        re.IGNORECASE,
    )

    repeated_punct = re.compile(r",,|;;|::|(?<!\.)\.\.(?!\.)|!!+|\?\?+")
    space_before = re.compile(r"\s+[,;!?](?=\s|$)|\s+\.(?=\s|$)")
    missing_after = re.compile(r"(?<!\d)([,;!?])(?=[A-Za-z])")
    repeated_space = re.compile(r"(?<!^) {2,}(?! )")
    broken_fig = re.compile(r"\bFig\.\.|\bFig\.(?=\d)|\bFig {2,}\d", re.IGNORECASE)
    ascii_range = re.compile(r"(?<![A-Za-z0-9])\d+(?:\.\d+)?-\d+(?:\.\d+)?(?![A-Za-z0-9])")

    for line_no, line, availability, in_fence, abstract in contexts:
        if not line.strip():
            continue

        # A manuscript containing fenced code is itself review-worthy, but do not
        # recursively lint code punctuation or delimiters as prose.
        if in_fence:
            if re.match(r"^\s*```", line):
                findings.append(
                    Finding(
                        line_no,
                        1,
                        "code_fence",
                        "review",
                        line.strip(),
                        "Code fence on a manuscript-facing surface; verify that code belongs in the paper rather than artifact documentation.",
                        availability,
                    )
                )
            continue

        if abstract and line_no in display_math_openings:
            _add_regex_findings(
                findings,
                line_no,
                line,
                ABSTRACT_DISPLAY_MATH,
                "abstract_display_math_review",
                "review",
                "Displayed mathematics in an abstract is target-dependent; prefer prose/inline math unless it is necessary, locally defined, interpreted, and permitted.",
                availability,
            )

        _add_regex_findings(
            findings,
            line_no,
            line,
            SUBMISSION_PLACEHOLDER,
            "submission_placeholder",
            "error" if final else "review",
            "Unresolved manuscript placeholder or internal document-state label; keep it only in an explicitly non-final draft note.",
            availability,
        )

        scope = "abstract" if abstract else "body"
        for symbol_match in OPAQUE_GREEK_SYMBOL.finditer(line):
            symbol = symbol_match.group("symbol")
            normalized_symbol = _normalize_opaque_symbol(symbol)
            if symbol.upper() in known or normalized_symbol.upper() in known:
                continue
            if _opaque_symbol_is_defined(line, symbol_match):
                defined_opaque_symbols[scope].add(normalized_symbol)
                continue
            if (
                normalized_symbol in defined_opaque_symbols[scope]
                or normalized_symbol in reviewed_opaque_symbols[scope]
            ):
                continue
            findings.append(
                Finding(
                    line=line_no,
                    column=symbol_match.start() + 1,
                    kind="undefined_symbol_review",
                    severity="review",
                    text=symbol,
                    message="Paper-private symbol may be undefined; state its denotation, domain, and role before claim-bearing use. An equality that gives only a value is not a definition.",
                    availability_context=availability,
                )
            )
            reviewed_opaque_symbols[scope].add(normalized_symbol)

        defined_here = _defined_identifiers(line)
        definition_starts = _identifier_definition_starts(line)
        previous = previous_prose_line[scope]
        wrapped_definitions = (
            _defined_identifiers(f"{previous} {line}") - defined_here if previous else set()
        )
        is_heading_line = bool(
            _section_heading_info(line)
            or re.fullmatch(
                r"\s*(?:abstract|introduction|methods?|results?|discussion|conclusions?|references|keywords?)\s*:?\s*",
                line,
                re.IGNORECASE,
            )
        )
        identifier_scan = (
            ""
            if is_heading_line or line_no in display_math_lines
            else _mask_nonprose_for_identifier_scan(line)
        )
        for match in IDENTIFIER_CANDIDATE.finditer(identifier_scan):
            token = match.group(0)
            if token in known:
                continue
            is_opaque = any(ch.isdigit() for ch in token)
            # Parenthetical apposition can expand an acronym, but it does not by
            # itself prove that an alphanumeric code is public, stable, or worth
            # exposing. Keep such labels reviewable until the terminology ledger
            # explicitly exempts them with --known-identifier.
            if is_opaque:
                if token in reviewed_opaque_identifiers[scope]:
                    continue
            else:
                definition_precedes_use = any(
                    start <= match.start() for start in definition_starts.get(token, ())
                )
                if (
                    token in seen_identifiers[scope]
                    or token in wrapped_definitions
                    or definition_precedes_use
                ):
                    continue
            prefix = line[max(0, match.start() - 3):match.start()]
            if prefix.endswith("_") or prefix.endswith("_{"):
                continue
            kind = "opaque_identifier_review" if is_opaque else "unexpanded_abbreviation_review"
            message = (
                "Opaque alphanumeric label may be internal; give it a reader-facing scientific identity or remove/relocate it."
                if kind == "opaque_identifier_review"
                else "Abbreviation/acronym may be unexplained on this standalone surface; expand or define it locally unless verified as universal for the intended reader."
            )
            findings.append(
                Finding(
                    line=line_no,
                    column=match.start() + 1,
                    kind=kind,
                    severity="review",
                    text=token,
                    message=message,
                    availability_context=availability,
                )
            )
            if is_opaque:
                reviewed_opaque_identifiers[scope].add(token)
            seen_identifiers[scope].add(token)
        seen_identifiers[scope].update(defined_here | wrapped_definitions)
        previous_prose_line[scope] = line

        _add_regex_findings(
            findings,
            line_no,
            line,
            local_path,
            "local_path",
            "error",
            "Local filesystem path should not appear in manuscript-facing prose.",
            availability,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            repo_file_path,
            "repository_path",
            "error",
            "Repository file path should be translated into scientific meaning or moved to artifact documentation.",
            availability,
            downgrade_in_availability=True,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            repo_nested_path,
            "repository_path_review",
            "review",
            "Slash-separated project-like path is suspicious; verify that it is not ordinary scientific notation/prose before relocating it.",
            availability,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            code_file,
            "code_filename",
            "error",
            "Code/config/checkpoint filename leaked into manuscript-facing text.",
            availability,
            downgrade_in_availability=True,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            cli_flag,
            "cli_flag",
            "error",
            "Command-line flag belongs in artifact/reproducibility documentation unless explicitly required.",
            availability,
            downgrade_in_availability=True,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            code_call,
            "code_identifier",
            "error",
            "Code/helper identifier should normally be replaced by the scientific operation.",
            availability,
            downgrade_in_availability=True,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            dev_history,
            "developer_history",
            "error",
            "Branch/PR/issue/commit/CI history is developer provenance, not scientific narrative.",
            availability,
            downgrade_in_availability=True,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            repo_url,
            "repository_url",
            "review",
            "Repository URL should normally be concentrated in a designated availability/artifact section.",
            availability,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            suspicious_output,
            "output_filename",
            "error",
            "Internal output filename should not be exposed in a paper-facing figure/body/legend surface.",
            availability,
            downgrade_in_availability=True,
        )

        _add_regex_findings(
            findings,
            line_no,
            line,
            repeated_punct,
            "repeated_punctuation",
            "error",
            "Likely accidental repeated punctuation.",
            availability,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            space_before,
            "space_before_punctuation",
            "error",
            "Unexpected space before punctuation.",
            availability,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            missing_after,
            "missing_space_after_punctuation",
            "error",
            "Likely missing space after punctuation.",
            availability,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            repeated_space,
            "repeated_space",
            "warning",
            "Repeated spaces in prose; verify typography.",
            availability,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            broken_fig,
            "figure_reference_punctuation",
            "error",
            "Malformed figure-reference punctuation/spacing.",
            availability,
        )
        _add_regex_findings(
            findings,
            line_no,
            line,
            ascii_range,
            "range_hyphen_review",
            "review",
            "Numeric range uses ASCII hyphen; verify target style (often en dash) and ensure this is not subtraction/identifier syntax.",
            availability,
        )

    _audit_wrapped_placeholders(findings, contexts, final=final)
    _audit_delimiters(findings, lines)

    # Deduplicate exact overlaps while preserving distinct diagnostic classes.
    unique = {(f.line, f.column, f.kind, f.text, f.message, f.availability_context): f for f in findings}
    return sorted(unique.values(), key=lambda f: (f.line, f.column, f.kind))


def audit_files(
    paths: Iterable[Path],
    *,
    final: bool = False,
    known_identifiers: Iterable[str] = (),
) -> dict[str, list[Finding]]:
    return {
        str(path): audit_text(
            path.read_text(encoding="utf-8", errors="replace"),
            final=final,
            known_identifiers=known_identifiers,
        )
        for path in paths
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="Plain-text, Markdown, Pandoc-YAML, or LaTeX manuscript files",
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when any error-severity finding is present")
    parser.add_argument(
        "--fail-on-review",
        action="store_true",
        help="Conservative candidate gate: exit non-zero while any finding remains; contextual dispositions still belong in the audit ledger",
    )
    parser.add_argument("--final", action="store_true", help="Treat release placeholders as final-manuscript errors")
    parser.add_argument(
        "--known-identifier",
        action="append",
        default=[],
        help="Reader-verified standard identifier to exempt from heuristic acronym/opaque-label review; repeat as needed",
    )
    args = parser.parse_args()

    if args.fail_on_review and args.known_identifier:
        parser.error(
            "--known-identifier cannot suppress findings under --fail-on-review; "
            "record semantic identity and disposition in the terminology/audit ledger"
        )

    reports = audit_files(
        args.paths,
        final=args.final,
        known_identifiers=args.known_identifier,
    )
    if args.as_json:
        print(json.dumps({k: [asdict(f) for f in v] for k, v in reports.items()}, indent=2, ensure_ascii=False))
    else:
        for path, findings in reports.items():
            print(f"{path}: {len(findings)} finding(s)")
            for f in findings:
                context = " availability" if f.availability_context else ""
                print(f"  {f.line}:{f.column} [{f.severity}{context}] {f.kind}: {f.text!r} — {f.message}")

    has_error = any(f.severity == "error" for findings in reports.values() for f in findings)
    has_finding = any(findings for findings in reports.values())
    return 1 if (args.strict and has_error) or (args.fail_on_review and has_finding) else 0


if __name__ == "__main__":
    raise SystemExit(main())
