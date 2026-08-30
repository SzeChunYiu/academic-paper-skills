#!/usr/bin/env python3
"""Conservative scanner for authoring-to-publication semantic leakage.

This tool complements audit_manuscript_surface.py. It flags source-level symptoms
that are easy to detect mechanically: chat-style inline bold, code/monospace
markup used for scientific prose, internal enum/status tokens, raw source-like
math outside math mode, suspicious all-caps workflow labels, table numbering
anomalies, LaTeX tables without captions, and overfull-box render-log messages.

Findings are intentionally review-oriented. Scientific necessity, target style,
formal type compatibility, named-object completeness, and contribution fit still
require contextual review under scholarly-surface-semantics.md.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Finding:
    line: int
    column: int
    kind: str
    severity: str
    text: str
    message: str


MARKDOWN_BOLD = re.compile(r"(?<!\*)\*\*(?P<body>[^*\n]+?)\*\*(?!\*)")
LATEX_BOLD = re.compile(r"\\textbf\{(?P<body>[^{}]+)\}|\\bfseries\b")
INLINE_CODE = re.compile(r"(?<!`)`(?P<body>[^`\n]+)`(?!`)")
LATEX_MONOSPACE = re.compile(r"\\texttt\{(?P<body>[^{}]+)\}|\\verb(?P<delim>[^A-Za-z0-9\s])[^\n]*?(?P=delim)")
UPPER_SNAKE = re.compile(r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b")
INTERNAL_STATUS = re.compile(r"\b(?:PASS|FAIL|FAILED|BLOCKED|CANNOT_CHECK|CANNOT\s+CHECK)\b")
ALL_CAPS_MULTIWORD = re.compile(
    r"\b[A-Z][A-Z0-9-]{3,}(?:\s+[A-Z][A-Z0-9/-]{2,}){1,5}\b"
)
# Raw source-like math that commonly leaks from Markdown/code into prose. The
# line is masked for inline/display math and code before this regex is applied.
RAW_MATH_TOKEN = re.compile(
    r"\b[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9{}]+)+(?:\^\{?[-+*A-Za-z0-9]+\}?)?"
    r"|\b[A-Za-z][A-Za-z0-9]*\^\{?[*A-Za-z0-9+-]+\}?"
)
OVERFULL_BOX = re.compile(r"Overfull \\(?:hbox|vbox)")
TABLE_CAPTION = re.compile(r"\bTable\s+(?P<num>\d+)\s*[:.]", re.IGNORECASE)
LATEX_TABLE_BEGIN = re.compile(r"\\begin\{table\*?\}")
LATEX_TABLE_END = re.compile(r"\\end\{table\*?\}")
LATEX_CAPTION = re.compile(r"\\caption(?:\[[^\]]*\])?\{")


def _mask_spans(line: str) -> str:
    """Mask code, URLs, comments, and common math spans while preserving columns."""
    masked = line
    patterns = (
        re.compile(r"https?://\S+"),
        re.compile(r"(?<!\\)%.*$"),
        re.compile(r"\$\$.*?\$\$"),
        re.compile(r"\$[^$\n]*\$"),
        re.compile(r"\\\[.*?\\\]"),
        re.compile(r"\\\(.*?\\\)"),
        re.compile(r"`[^`\n]*`"),
    )
    for pattern in patterns:
        masked = pattern.sub(lambda m: " " * len(m.group(0)), masked)
    return masked


def _is_heading(line: str) -> bool:
    stripped = line.strip()
    if re.match(r"^#{1,6}\s+", stripped):
        return True
    if re.match(r"^\\(?:section|subsection|subsubsection|paragraph)\*?\{", stripped):
        return True
    return False


def _add_matches(
    findings: list[Finding],
    line_no: int,
    line: str,
    pattern: re.Pattern[str],
    *,
    kind: str,
    severity: str,
    message: str,
) -> None:
    for match in pattern.finditer(line):
        findings.append(
            Finding(
                line=line_no,
                column=match.start() + 1,
                kind=kind,
                severity=severity,
                text=match.group(0),
                message=message,
            )
        )


def _audit_latex_tables(findings: list[Finding], lines: list[str]) -> None:
    start: int | None = None
    has_caption = False
    for idx, line in enumerate(lines, 1):
        if start is None and LATEX_TABLE_BEGIN.search(line):
            start = idx
            has_caption = bool(LATEX_CAPTION.search(line))
            if LATEX_TABLE_END.search(line):
                if not has_caption:
                    findings.append(
                        Finding(start, 1, "latex_table_missing_caption", "error", "table", "LaTeX table environment has no caption; manuscript tables require target-appropriate caption/title structure.")
                    )
                start = None
            continue
        if start is not None:
            has_caption = has_caption or bool(LATEX_CAPTION.search(line))
            if LATEX_TABLE_END.search(line):
                if not has_caption:
                    findings.append(
                        Finding(start, 1, "latex_table_missing_caption", "error", "table", "LaTeX table environment has no caption; manuscript tables require target-appropriate caption/title structure.")
                    )
                start = None
                has_caption = False
    if start is not None:
        findings.append(
            Finding(start, 1, "latex_table_unclosed", "error", "table", "LaTeX table environment is not closed in the audited source.")
        )


def _audit_table_numbering(findings: list[Finding], lines: list[str]) -> None:
    captions: list[tuple[int, int]] = []
    for idx, line in enumerate(lines, 1):
        for match in TABLE_CAPTION.finditer(line):
            captions.append((idx, int(match.group("num"))))
    if not captions:
        return
    seen: dict[int, int] = {}
    for line_no, number in captions:
        if number in seen:
            findings.append(
                Finding(line_no, 1, "duplicate_table_number", "error", f"Table {number}", f"Table number {number} is duplicated; first seen on line {seen[number]}.")
            )
        else:
            seen[number] = line_no
    ordered = [number for _, number in captions]
    unique = sorted(set(ordered))
    if unique and unique[0] == 1:
        expected = list(range(1, unique[-1] + 1))
        missing = [n for n in expected if n not in seen]
        for number in missing:
            findings.append(
                Finding(captions[-1][0], 1, "table_number_gap", "error", f"Table {number}", f"Table numbering skips {number}; reconcile environments, captions, and body callouts.")
            )
    if ordered != sorted(ordered):
        findings.append(
            Finding(captions[-1][0], 1, "table_number_order_review", "review", "table numbering", "Table caption numbers are not encountered in increasing order; verify target-specific continuation/placement.")
        )


def audit_text(text: str) -> list[Finding]:
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False
    in_display_math: str | None = None

    for line_no, line in enumerate(lines, 1):
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        # Render-log signal can be recognized anywhere.
        _add_matches(
            findings,
            line_no,
            line,
            OVERFULL_BOX,
            kind="overfull_box",
            severity="review",
            message="Renderer reports an overfull box; inspect the corresponding final page for clipping/overflow before release.",
        )

        if in_display_math is not None:
            if (in_display_math == "$$" and "$$" in line) or (in_display_math == "\\[" and "\\]" in line):
                in_display_math = None
            continue
        if line.count("$$") % 2 == 1:
            in_display_math = "$$"
        if "\\[" in line and "\\]" not in line[line.find("\\[") + 2:]:
            in_display_math = "\\["

        if not _is_heading(line):
            _add_matches(
                findings,
                line_no,
                line,
                MARKDOWN_BOLD,
                kind="inline_bold_review",
                severity="review",
                message="Inline bold in manuscript prose may be chat/Markdown emphasis leakage; justify from target/genre or express emphasis through scholarly structure.",
            )
            _add_matches(
                findings,
                line_no,
                line,
                LATEX_BOLD,
                kind="inline_bold_review",
                severity="review",
                message="Inline LaTeX bold in manuscript prose may be rhetorical markup leakage; retain only for a target-supported publication function.",
            )

        _add_matches(
            findings,
            line_no,
            line,
            INLINE_CODE,
            kind="inline_code_semantics_review",
            severity="review",
            message="Inline code/backticks on a manuscript surface may be literal-code typography leaking onto a scientific concept; translate unless exact syntax is the object.",
        )
        _add_matches(
            findings,
            line_no,
            line,
            LATEX_MONOSPACE,
            kind="monospace_semantics_review",
            severity="review",
            message="Monospace/typewriter markup may be inappropriate for scientific concepts; retain only when literal machine syntax is scientifically necessary.",
        )
        _add_matches(
            findings,
            line_no,
            line,
            UPPER_SNAKE,
            kind="internal_enum_token_review",
            severity="review",
            message="Upper-snake token resembles an internal enum/config/status label; translate to reader-facing prose, mathematical notation, or target-appropriate typography unless it is the scientific object.",
        )
        _add_matches(
            findings,
            line_no,
            line,
            INTERNAL_STATUS,
            kind="internal_status_vocabulary_review",
            severity="review",
            message="CI/audit-style status vocabulary may be leaking into manuscript results; translate to a scientific disposition unless the status is explicitly defined as a study object.",
        )

        if not _is_heading(line):
            caps_line = _mask_spans(line)
            _add_matches(
                findings,
                line_no,
                caps_line,
                ALL_CAPS_MULTIWORD,
                kind="all_caps_workflow_label_review",
                severity="review",
                message="Multiword all-caps label may reflect dashboard/workflow styling rather than scholarly visual language; verify that the label is an actual scientific state/operator.",
            )

        prose = _mask_spans(line)
        _add_matches(
            findings,
            line_no,
            prose,
            RAW_MATH_TOKEN,
            kind="raw_math_token",
            severity="error",
            message="Source-like underscore/caret mathematical token appears outside math/code markup; typeset the scientific object in mathematical notation.",
        )

    _audit_latex_tables(findings, lines)
    _audit_table_numbering(findings, lines)

    unique = {(f.line, f.column, f.kind, f.text, f.message): f for f in findings}
    return sorted(unique.values(), key=lambda f: (f.line, f.column, f.kind))


def audit_files(paths: Iterable[Path]) -> dict[str, list[Finding]]:
    return {
        str(path): audit_text(path.read_text(encoding="utf-8", errors="replace"))
        for path in paths
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on error-severity findings")
    parser.add_argument("--fail-on-review", action="store_true", help="Exit non-zero on any remaining finding")
    args = parser.parse_args()

    reports = audit_files(args.paths)
    if args.as_json:
        print(json.dumps({k: [asdict(f) for f in v] for k, v in reports.items()}, indent=2, ensure_ascii=False))
    else:
        for path, findings in reports.items():
            print(f"{path}: {len(findings)} finding(s)")
            for f in findings:
                print(f"  {f.line}:{f.column} [{f.severity}] {f.kind}: {f.text!r} — {f.message}")

    has_error = any(f.severity == "error" for fs in reports.values() for f in fs)
    has_finding = any(fs for fs in reports.values())
    return 1 if (args.strict and has_error) or (args.fail_on_review and has_finding) else 0


if __name__ == "__main__":
    raise SystemExit(main())
