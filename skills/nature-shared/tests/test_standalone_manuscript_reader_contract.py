from __future__ import annotations

import importlib.util
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
STANDALONE = SHARED / "core" / "standalone-manuscript-reader-contract.md"
LITERATURE = SHARED / "core" / "literature-version-and-source-quality.md"
SCANNER = SHARED / "scripts" / "audit_standalone_manuscript.py"
WRITING_MANIFEST = SKILLS / "academic-writing" / "manifest.yaml"
PIPELINE_MANIFEST = SKILLS / "academic-paper-pipeline" / "manifest.yaml"
REVIEWER_MANIFEST = SKILLS / "nature-reviewer" / "manifest.yaml"
CITATION_MANIFEST = SKILLS / "nature-citation" / "manifest.yaml"
CITATION_WORKFLOW = SKILLS / "nature-citation" / "static" / "core" / "workflow.md"


def _version(text: str) -> tuple[int, ...]:
    for line in text.splitlines():
        if line.startswith("version:"):
            return tuple(int(part) for part in line.split(":", 1)[1].strip().split("."))
    raise AssertionError("manifest version missing")


def _load_scanner():
    spec = importlib.util.spec_from_file_location("audit_standalone_manuscript", SCANNER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_standalone_contract_makes_each_paper_zero_context_and_reading_order_safe() -> None:
    text = STANDALONE.read_text(encoding="utf-8").lower()
    for marker in (
        "every paper must first stand on its own",
        "zero-context reader baseline",
        "reading-order definition law",
        "reader-facing name first; internal identifier second",
        "paper-series independence",
        "claim subtraction is an authoring operation, not a manuscript section",
        "related work is a function, not a mandatory section",
        "development chronology is not the default results structure",
        "clean-room reader review",
    ):
        assert marker in text, marker


def test_contract_explicitly_catches_project_ontology_and_repository_projection() -> None:
    text = STANDALONE.read_text(encoding="utf-8").lower()
    for marker in (
        "private research-management vocabulary stays private by default",
        "machine terminal strings",
        "repository dumping",
        "borrowed terminology from neighbouring work",
        "availability section functions as a file manifest",
        "could a qualified reader encountering only this manuscript explain",
    ):
        assert marker in text, marker


def test_literature_contract_prefers_formal_version_without_journal_prestige_rule() -> None:
    text = LITERATURE.read_text(encoding="utf-8").lower()
    for marker in (
        "version-of-record preference",
        "ispreprintof",
        "haspreprint",
        "preprints are allowed",
        "mature-claim anchor rule",
        "computing/ml conference boundary",
        "open access is not a quality class",
        "internal project documents cannot substitute for external prior work",
        "reference lists should be selective but complete for interpretation",
    ):
        assert marker in text, marker


def test_all_relevant_skills_always_load_new_contracts() -> None:
    writing = WRITING_MANIFEST.read_text(encoding="utf-8")
    pipeline = PIPELINE_MANIFEST.read_text(encoding="utf-8")
    reviewer = REVIEWER_MANIFEST.read_text(encoding="utf-8")
    citation = CITATION_MANIFEST.read_text(encoding="utf-8")

    standalone_path = "../nature-shared/core/standalone-manuscript-reader-contract.md"
    literature_path = "../nature-shared/core/literature-version-and-source-quality.md"

    assert standalone_path in writing
    assert standalone_path in pipeline
    assert standalone_path in reviewer
    assert literature_path in writing
    assert literature_path in pipeline
    assert literature_path in reviewer
    assert literature_path in citation
    assert "../nature-shared/core/terminology-ledger.md" in pipeline

    assert _version(writing) >= (1, 12, 0)
    assert _version(pipeline) >= (1, 14, 0)
    assert _version(reviewer) >= (2, 9, 0)
    assert _version(citation) >= (3, 2, 0)


def test_citation_workflow_resolves_version_before_manuscript_selection() -> None:
    text = CITATION_WORKFLOW.read_text(encoding="utf-8").lower()
    for marker in (
        "resolve publication version and maturity",
        "ispreprintof",
        "haspreprint",
        "peer-reviewed journal/proceedings version",
        "search breadth and manuscript citation breadth are different",
        "dedicated related work section is optional",
    ):
        assert marker in text, marker


def test_scanner_flags_exact_failure_classes_without_calling_all_ids_errors() -> None:
    scanner = _load_scanner()
    sample = """
# Related work and claim subtraction
Most directly for our D1 control, the donor families establish the parent idea.
The retained terminal is P9_NEURAL_ESCALATION_NOT_JUSTIFIED__NO_RETRY.
See evidence/protected_v2/RESULT.json and run:
python papers/project/reproduce_final.py
Paper III defines the missing object.

References
A. Author. Example. arXiv preprint arXiv:2601.00001.
B. Author. Example. arXiv preprint arXiv:2601.00002.
C. Author. Example. arXiv preprint arXiv:2601.00003.
D. Author. Example. arXiv preprint arXiv:2601.00004.
E. Author. Example. arXiv preprint arXiv:2601.00005.
"""
    result = scanner.audit(sample)
    codes = {item["code"] for item in result["findings"]}
    assert result["decision"] == "BLOCKED"
    assert "machine_terminal_leak" in codes
    assert "repository_path_leak" in codes
    assert "cli_leak" in codes
    assert "private_authoring_vocabulary" in codes
    assert "paper_series_dependency" in codes
    assert "opaque_project_id_first_use" in codes
    assert "preprint_concentration" in codes
    opaque = [item for item in result["findings"] if item["code"] == "opaque_project_id_first_use"]
    assert opaque and all(item["severity"] == "review" for item in opaque)


def test_scanner_allows_plain_reader_facing_science() -> None:
    scanner = _load_scanner()
    sample = """
We test whole-domain procedural transfer by training on numerical and graph-algorithm structures and
holding out transactional workflows as an entire domain. The central comparison asks whether typed
relational organization improves transfer relative to an untyped representation. Data and code are
available from the archived repository cited in the availability statement.
"""
    result = scanner.audit(sample)
    assert result["decision"] == "PASS"
    assert result["findings"] == []
