#!/usr/bin/env python3
"""Describe structural/rhetorical surface patterns in an academic-paper corpus.

This tool is deliberately descriptive. It does not score writing quality and it
cannot infer rhetorical moves reliably from word counts. Use its output as a
scalable companion to semantic move annotation in target-corpus-calibration.md.

Input: UTF-8 .md/.markdown/.txt files or directories containing them.
Output: JSON with per-paper and corpus-level section/paragraph/sentence metrics.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


TEXT_SUFFIXES = {".md", ".markdown", ".txt"}

SECTION_ALIASES = {
    "abstract": "abstract",
    "summary": "abstract",
    "introduction": "introduction",
    "background": "introduction",
    "related work": "related-work",
    "related works": "related-work",
    "literature review": "related-work",
    "materials and methods": "methods",
    "materials & methods": "methods",
    "methods": "methods",
    "method": "methods",
    "methodology": "methods",
    "experimental methods": "methods",
    "experimental": "methods",
    "results": "results",
    "experiments": "results",
    "experimental results": "results",
    "results and discussion": "results-discussion",
    "results & discussion": "results-discussion",
    "discussion": "discussion",
    "discussions": "discussion",
    "conclusion": "conclusion",
    "conclusions": "conclusion",
    "concluding remarks": "conclusion",
    "limitations": "limitations",
    "references": "references",
    "bibliography": "references",
    "acknowledgments": "acknowledgments",
    "acknowledgements": "acknowledgments",
    "supplementary materials": "supplementary",
    "supplementary information": "supplementary",
}

BACK_MATTER = {"references", "acknowledgments", "supplementary"}

MARKERS: dict[str, tuple[str, ...]] = {
    "contrast": (
        "however", "nevertheless", "nonetheless", "in contrast", "by contrast",
        "although", "though", "whereas", "despite", "yet",
    ),
    "addition": (
        "furthermore", "moreover", "in addition", "additionally", "also",
    ),
    "cause_consequence": (
        "therefore", "thus", "consequently", "as a result", "because", "thereby",
    ),
    "example_specification": (
        "for example", "for instance", "specifically", "in particular", "namely",
    ),
    "summary": (
        "overall", "in summary", "collectively", "taken together", "in conclusion",
    ),
    "hedge": (
        "may", "might", "could", "possibly", "potentially", "likely", "appears",
        "appear", "suggests", "suggest", "indicates", "indicate", "consistent with",
    ),
    "booster": (
        "clearly", "demonstrates", "demonstrate", "establishes", "establish",
        "proves", "prove", "undoubtedly", "strongly supports", "decisively",
    ),
    "self_reference": (
        "we ", "we\n", "our ", "this study", "this work", "this paper",
    ),
    "contribution_signal": (
        "here we", "we propose", "we present", "we introduce", "we develop",
        "we show", "we demonstrate", "this study aims", "the present study",
        "our contribution", "our contributions",
    ),
}

FIGURE_RE = re.compile(r"\b(?:fig(?:ure)?\.?|table)\s*[s]?\s*\d+[a-z]?\b", re.IGNORECASE)
WORD_RE = re.compile(r"\b[\w'’-]+\b", re.UNICODE)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9(\[])|(?<=[。！？])")
MARKDOWN_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
NUMBERED_HEADING_RE = re.compile(
    r"^(?:\d+(?:\.\d+)*[.)]?\s+|[IVXLC]+[.)]\s+)?"
    r"(abstract|summary|introduction|background|related works?|literature review|"
    r"materials(?:\s+and|\s*&)?\s+methods|methods?|methodology|experimental methods?|"
    r"results(?:\s+(?:and|&)\s+discussion)?|experiments?|discussion|discussions|"
    r"conclusions?|concluding remarks|limitations?|references|bibliography|"
    r"acknowledg(?:e)?ments?|supplementary (?:materials|information))\s*:?[\s]*$",
    re.IGNORECASE,
)


def clean_inline_markdown(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_heading(text: str) -> str:
    text = clean_inline_markdown(text)
    text = re.sub(r"^\d+(?:\.\d+)*[.)]?\s+", "", text).strip(" :.-")
    key = text.casefold()
    if key in SECTION_ALIASES:
        return SECTION_ALIASES[key]
    if key.startswith("results") and "discussion" in key:
        return "results-discussion"
    if key.startswith("discussion"):
        return "discussion"
    if key.startswith("conclusion"):
        return "conclusion"
    return key


def is_heading(line: str) -> tuple[bool, str]:
    stripped = line.strip()
    if not stripped:
        return False, ""
    match = MARKDOWN_HEADING_RE.match(stripped)
    if match:
        return True, normalize_heading(match.group(2))
    match = NUMBERED_HEADING_RE.match(stripped)
    if match:
        return True, normalize_heading(match.group(1))
    return False, ""


def split_sections(text: str) -> list[tuple[str, str]]:
    """Return ordered (section_name, text) blocks, preserving unknown headings."""
    sections: list[tuple[str, list[str]]] = [("preamble", [])]
    for raw_line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        heading, name = is_heading(raw_line)
        if heading:
            sections.append((name or "untitled", []))
            continue
        sections[-1][1].append(raw_line)
    return [(name, "\n".join(lines).strip()) for name, lines in sections if any(x.strip() for x in lines)]


def split_paragraphs(text: str) -> list[str]:
    paragraphs: list[str] = []
    for block in re.split(r"\n\s*\n+", text.strip()):
        cleaned = clean_inline_markdown(block)
        if len(WORD_RE.findall(cleaned)) >= 3:
            paragraphs.append(cleaned)
    return paragraphs


def split_sentences(text: str) -> list[str]:
    cleaned = clean_inline_markdown(text)
    if not cleaned:
        return []
    parts = [part.strip() for part in SENTENCE_SPLIT_RE.split(cleaned) if part.strip()]
    return parts or [cleaned]


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def count_phrase(text_casefolded: str, phrase: str) -> int:
    phrase = phrase.casefold()
    if phrase.endswith(" ") or " " in phrase.strip():
        return text_casefolded.count(phrase)
    return len(re.findall(rf"\b{re.escape(phrase)}\b", text_casefolded))


def marker_counts(text: str) -> dict[str, int]:
    folded = f" {text.casefold()} "
    return {
        category: sum(count_phrase(folded, phrase) for phrase in phrases)
        for category, phrases in MARKERS.items()
    }


def safe_median(values: list[int]) -> float:
    return float(statistics.median(values)) if values else 0.0


def per_thousand(count: int, word_count: int) -> float:
    return round((count * 1000.0 / word_count), 3) if word_count else 0.0


def summarize_text(text: str) -> dict[str, Any]:
    paragraphs = split_paragraphs(text)
    sentences = split_sentences(text)
    word_list = words(text)
    marker_raw = marker_counts(text)
    return {
        "words": len(word_list),
        "paragraphs": len(paragraphs),
        "sentences": len(sentences),
        "median_paragraph_words": safe_median([len(words(p)) for p in paragraphs]),
        "median_sentence_words": safe_median([len(words(s)) for s in sentences]),
        "figure_table_calls": len(FIGURE_RE.findall(text)),
        "marker_counts": marker_raw,
        "markers_per_1000_words": {
            category: per_thousand(count, len(word_list))
            for category, count in marker_raw.items()
        },
    }


def analyze_paper(path: Path, include_back_matter: bool = False) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    raw_sections = split_sections(text)
    sections: list[dict[str, Any]] = []
    included_texts: list[str] = []
    for order, (name, body) in enumerate(raw_sections, 1):
        if not include_back_matter and name in BACK_MATTER:
            continue
        metrics = summarize_text(body)
        sections.append({"order": order, "name": name, **metrics})
        included_texts.append(body)

    full_text = "\n\n".join(included_texts)
    return {
        "file": str(path),
        "section_sequence": [item["name"] for item in sections],
        "section_count": len(sections),
        "overall": summarize_text(full_text),
        "sections": sections,
    }


def iter_files(inputs: Iterable[str]) -> list[Path]:
    output: list[Path] = []
    seen: set[Path] = set()
    for raw in inputs:
        path = Path(raw).expanduser()
        candidates = [path] if path.is_file() else sorted(path.rglob("*")) if path.is_dir() else []
        for candidate in candidates:
            if not candidate.is_file() or candidate.suffix.casefold() not in TEXT_SUFFIXES:
                continue
            resolved = candidate.resolve()
            if resolved not in seen:
                seen.add(resolved)
                output.append(candidate)
    return output


def weighted_rate(papers: list[dict[str, Any]], category: str) -> float:
    count = sum(p["overall"]["marker_counts"].get(category, 0) for p in papers)
    total_words = sum(p["overall"]["words"] for p in papers)
    return per_thousand(count, total_words)


def aggregate(papers: list[dict[str, Any]]) -> dict[str, Any]:
    section_presence: Counter[str] = Counter()
    section_order: defaultdict[str, list[int]] = defaultdict(list)
    all_paragraph_medians: list[float] = []
    all_sentence_medians: list[float] = []
    total_words = 0
    total_figures = 0

    for paper in papers:
        total_words += paper["overall"]["words"]
        total_figures += paper["overall"]["figure_table_calls"]
        all_paragraph_medians.append(paper["overall"]["median_paragraph_words"])
        all_sentence_medians.append(paper["overall"]["median_sentence_words"])
        seen_in_paper: set[str] = set()
        for section in paper["sections"]:
            name = section["name"]
            if name not in seen_in_paper:
                section_presence[name] += 1
                seen_in_paper.add(name)
            section_order[name].append(section["order"])

    n = len(papers)
    presence = {
        name: {
            "papers": count,
            "fraction": round(count / n, 3) if n else 0.0,
            "median_order": safe_median(section_order[name]),
        }
        for name, count in section_presence.most_common()
    }
    return {
        "paper_count": n,
        "total_words": total_words,
        "median_paper_words": safe_median([p["overall"]["words"] for p in papers]),
        "median_of_paper_median_paragraph_words": safe_median([int(x) for x in all_paragraph_medians]),
        "median_of_paper_median_sentence_words": safe_median([int(x) for x in all_sentence_medians]),
        "figure_table_calls": total_figures,
        "section_presence": presence,
        "markers_per_1000_words": {
            category: weighted_rate(papers, category) for category in MARKERS
        },
        "notes": [
            "These are descriptive surface statistics, not writing-quality scores.",
            "Marker frequency cannot establish rhetorical effectiveness or evidence quality.",
            "Use semantic move annotation and complete-paper reading before turning corpus patterns into writing rules.",
            "Stratify by journal, article type, discipline, study design, and year before comparing groups.",
        ],
    }


def build_payload(files: list[Path], include_back_matter: bool) -> dict[str, Any]:
    papers = [analyze_paper(path, include_back_matter=include_back_matter) for path in files]
    return {
        "corpus": aggregate(papers),
        "papers": papers,
    }


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Describe section/paragraph/sentence patterns in extracted academic-paper text without scoring writing quality."
    )
    p.add_argument("inputs", nargs="+", help="UTF-8 .md/.markdown/.txt file(s) or directories.")
    p.add_argument("--include-back-matter", action="store_true", help="Include references/acknowledgments/supplementary sections.")
    p.add_argument("--output", help="Optional JSON output path. Defaults to stdout.")
    p.add_argument("--pretty", action="store_true", help="Pretty-print JSON.")
    return p


def main() -> int:
    args = parser().parse_args()
    files = iter_files(args.inputs)
    if not files:
        raise SystemExit("No .md/.markdown/.txt corpus files found.")
    payload = build_payload(files, include_back_matter=args.include_back_matter)
    rendered = json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
