from __future__ import annotations

import importlib.util
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
ABSTRACT = SHARED / "core" / "abstract-information-budget.md"
SECTIONS = SHARED / "core" / "manuscript-section-craftsmanship.md"
EXCELLENCE = SHARED / "core" / "manuscript-excellence-release-gate.md"
PIPELINE_CORE = SHARED / "core" / "academic-paper-iteration-pipeline.md"
SCANNER = SHARED / "scripts" / "audit_abstract_information.py"
WRITING = SKILLS / "academic-writing" / "manifest.yaml"
PIPELINE = SKILLS / "academic-paper-pipeline" / "manifest.yaml"
REVIEWER = SKILLS / "nature-reviewer" / "manifest.yaml"


def _version(text: str) -> tuple[int, ...]:
    for line in text.splitlines():
        if line.startswith("version:"):
            return tuple(int(part) for part in line.split(":", 1)[1].strip().split("."))
    raise AssertionError("manifest version missing")


def _load_scanner():
    spec = importlib.util.spec_from_file_location("audit_abstract_information", SCANNER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_abstract_contract_is_information_budget_not_number_quota() -> None:
    text = ABSTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "abstract is not a miniature copy of every manuscript section",
        "scarce information budget",
        "rhetorical spine, not a section sampler",
        "do not force a mini-imrad sequence",
        "the numerical-salience gate",
        "q0 required reporting / design identity",
        "q1 headline scientific anchor",
        "q2 secondary support",
        "q3 audit/provenance/process diagnostic",
        "q4 formatter residue",
        "treat an inferential result as one semantic bundle",
        "number-to-meaning test",
        "no abstract result catalogue",
        "positive-claim visibility",
        "abstract-to-paper consistency",
        "abstract reader-recovery test",
    ):
        assert marker in text, marker
    assert "maximum n numbers per abstract" in text
    assert "do not universalize" in text
    assert "fixed number of numbers" in text
    assert "reporting-mandated studies" in text or "reporting-mandated" in text


def test_section_contract_covers_each_major_manuscript_surface() -> None:
    text = SECTIONS.read_text(encoding="utf-8").lower()
    for heading in (
        "## 2. title",
        "## 3. abstract",
        "## 4. keywords / indexing terms",
        "## 5. introduction",
        "## 6. related work / prior-work positioning",
        "## 7. problem formulation / theory / task definition / formal setup",
        "## 8. methods / materials and methods / experimental setup",
        "## 9. results",
        "## 10. discussion",
        "## 11. limitations / threats to validity",
        "## 12. conclusion",
        "## 13. figures",
        "## 14. tables",
        "## 15. figure and table legends / captions",
        "## 16. equations, definitions, theorems, proofs, algorithms",
        "## 17. references and citations",
        "## 18. supplementary information / extended data / appendices",
        "## 19. data / code / resource availability",
        "## 20. ethics, funding, competing interests, author contributions, acknowledgements",
        "## 21. section headings and subheadings",
    ):
        assert heading in text, heading


def test_section_contract_is_functional_not_template_driven() -> None:
    text = SECTIONS.read_text(encoding="utf-8").lower()
    for marker in (
        "every section is an interface",
        "section is a **scientific function**, not a mandatory section",
        "functional sufficiency, not length",
        "organize by scientific procedure, not code layout",
        "organize by scientific dependency",
        "discussion should not repeat results",
        "a dedicated section is optional",
        "a separate conclusion is optional",
        "writing order versus reading order",
        "cross-section duplication audit",
        "section-specific anti-ai-writing audit",
        "clean-reader section audit",
        "functional completeness and reader dependency",
    ):
        assert marker in text, marker


def test_scanner_flags_number_heavy_benchmark_abstract() -> None:
    scanner = _load_scanner()
    sample = """
Abstract
We study a controlled representation diagnostic. On a frozen 420-case battery, the governed system makes 0/360 false promotions versus 180/360 for the comparator while both score 60/60 on clean positives. On a second 30-case battery it scores 30/30 versus 0/30, with paired difference 1.0 and 95% CI [1.0, 1.0]. On 400 contracts it scores 400/400 versus 250/400, while another product scores 50/400 and a typed product scores 400/400. A source audit authenticates 76/80 bridges. These finite batteries establish a scoped authority relation.

1 Introduction
Text.
"""
    result = scanner.audit(sample)
    codes = {item["code"] for item in result["findings"]}
    assert result["decision"] == "REVIEW"
    assert "abstract_numeric_density" in codes
    assert "abstract_multiple_quantitative_substories" in codes
    assert result["metrics"]["numeric_token_count"] >= 10


def test_scanner_flags_six_decimal_and_private_id_abstract() -> None:
    scanner = _load_scanner()
    sample = """
Abstract
Learning failure can reflect missing information or missing computation. In M1, the semantic view reaches 1.000000 while affine gluing remains at 0.510417. A held-out domain reaches 1.000000 versus 0.906250, 0.500000, and 0.250000 for three comparison views. The result motivates a diagnostic methodology before architecture escalation.

1 Introduction
Text.
"""
    result = scanner.audit(sample)
    codes = {item["code"] for item in result["findings"]}
    assert result["decision"] == "REVIEW"
    assert "abstract_formatter_precision" in codes
    assert "abstract_private_identifier" in codes


def test_scanner_allows_compact_non_numeric_theory_abstract() -> None:
    scanner = _load_scanner()
    sample = """
Abstract
Current predictive adequacy need not certify later evidence-triggered revision. We formalize a prospective compatibility condition and give an exact one-bit witness showing that two present-equivalent states can require different later actions after the same evidence event. This yields an audit for testing retained representations while separating present adequacy from future revision adequacy. The result is a non-certification statement under the declared task and evidence process, not a claim that deployed language models generally discard revision-relevant information.

1 Introduction
Text.
"""
    result = scanner.audit(sample)
    assert result["decision"] == "PASS"
    assert result["counts"] == {"error": 0, "unresolved": 0, "review": 0}


def test_reporting_mandated_profile_does_not_apply_generic_numeric_quota() -> None:
    scanner = _load_scanner()
    sample = """
Abstract
Background: We evaluated treatment A versus treatment B. Methods: In this randomized trial, 412 participants were assigned 206 per group. Results: The primary outcome occurred in 61/202 (30.2%) versus 82/199 (41.2%), risk difference -11.0 percentage points (95% CI -20.0 to -2.0). Serious adverse events occurred in 8/202 and 9/199. Conclusions: Treatment A reduced the primary outcome under this trial design.

1 Introduction
Text.
"""
    generic = scanner.audit(sample)
    mandated = scanner.audit(sample, reporting_mandated=True)
    assert any(item["code"] == "abstract_numeric_density" for item in generic["findings"])
    assert not any(item["code"] == "abstract_numeric_density" for item in mandated["findings"])


def test_scanner_blocks_supplied_hard_abstract_word_limit() -> None:
    scanner = _load_scanner()
    sample = "Abstract\n" + "word " * 80 + "\n\n1 Introduction\nText."
    result = scanner.audit(sample, max_words=70)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "abstract_word_limit_exceeded" for item in result["findings"])


def test_scanner_can_enforce_no_references_target_rule() -> None:
    scanner = _load_scanner()
    sample = """
Abstract
Prior work [12] motivates the question. We establish the central result and its implication.

1 Introduction
Text.
"""
    result = scanner.audit(sample, references_disallowed=True)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "abstract_reference_disallowed" for item in result["findings"])


def test_excellence_and_pipeline_require_abstract_and_section_craftsmanship() -> None:
    excellence = EXCELLENCE.read_text(encoding="utf-8").lower()
    pipeline_core = PIPELINE_CORE.read_text(encoding="utf-8").lower()
    for marker in (
        "abstract information budget",
        "section craftsmanship",
        "abstract-to-paper consistency",
        "clean-reader abstract",
    ):
        assert marker in excellence or marker in pipeline_core, marker


def test_manifests_always_load_new_contracts_and_scanner() -> None:
    writing = WRITING.read_text(encoding="utf-8")
    pipeline = PIPELINE.read_text(encoding="utf-8")
    reviewer = REVIEWER.read_text(encoding="utf-8")
    for text in (writing, pipeline, reviewer):
        assert "../nature-shared/core/abstract-information-budget.md" in text
        assert "../nature-shared/core/manuscript-section-craftsmanship.md" in text
        assert "../nature-shared/scripts/audit_abstract_information.py" in text
        assert "../nature-shared/research/section-specific-academic-writing-evidence-2026-08-31.md" in text
    assert _version(writing) >= (1, 15, 0)
    assert _version(pipeline) >= (1, 17, 0)
    assert _version(reviewer) >= (3, 2, 0)
