#!/usr/bin/env python3
"""Conservative last-mile audit for manuscript-facing text.

The scanner flags likely repository/artifact leakage and high-confidence
mechanical punctuation defects. It does not rewrite text and intentionally
leaves meaning-sensitive grammar, hyphenation, citation placement, and
field-specific identifiers to human/LLM contextual review.
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


@dataclass(frozen=True)
class Finding:
    line: int
    column: int
    kind: str
    severity: str
    text: str
    message: str
    availability_context: bool = False


def _section_heading(line: str) -> str | None:
    m = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", line)
    if not m:
        return None
    heading = re.sub(r"[*_`]+", "", m.group(1)).strip().lower()
    return heading


def _iter_context(lines: list[str]):
    in_fence = False
    availability = False
    for idx, line in enumerate(lines, 1):
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            yield idx, line, availability, True
            continue
        heading = _section_heading(line)
        if heading is not None:
            availability = heading in AVAILABILITY_HEADINGS
        yield idx, line, availability, in_fence


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


def audit_text(text: str) -> list[Finding]:
    findings: list[Finding] = []
    lines = text.splitlines()

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

    for line_no, line, availability, in_fence in _iter_context(lines):
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

    _audit_delimiters(findings, lines)

    # Deduplicate exact overlaps while preserving distinct diagnostic classes.
    unique = {(f.line, f.column, f.kind, f.text, f.message, f.availability_context): f for f in findings}
    return sorted(unique.values(), key=lambda f: (f.line, f.column, f.kind))


def audit_files(paths: Iterable[Path]) -> dict[str, list[Finding]]:
    return {str(path): audit_text(path.read_text(encoding="utf-8", errors="replace")) for path in paths}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Plain-text or Markdown manuscript files")
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when any error-severity finding is present")
    args = parser.parse_args()

    reports = audit_files(args.paths)
    if args.as_json:
        print(json.dumps({k: [asdict(f) for f in v] for k, v in reports.items()}, indent=2, ensure_ascii=False))
    else:
        for path, findings in reports.items():
            print(f"{path}: {len(findings)} finding(s)")
            for f in findings:
                context = " availability" if f.availability_context else ""
                print(f"  {f.line}:{f.column} [{f.severity}{context}] {f.kind}: {f.text!r} — {f.message}")

    has_error = any(f.severity == "error" for findings in reports.values() for f in findings)
    return 1 if args.strict and has_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
