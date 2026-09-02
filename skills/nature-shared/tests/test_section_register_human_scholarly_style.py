from __future__ import annotations

import importlib.util
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
CONTRACT = SHARED / "core" / "section-register-and-human-scholarly-style.md"
RESEARCH = SHARED / "research" / "top-tier-section-register-style-evidence-2026-09-02.md"
SCHEMA = SHARED / "analysis-contracts" / "scholarly-register-profile.schema.json"
VERIFIER = SHARED / "scripts" / "verify_scholarly_register_profile.py"
KERNEL = SHARED / "core" / "ai-session-execution-kernel.md"
WRITING = SKILLS / "academic-writing" / "manifest.yaml"
PIPELINE = SKILLS / "academic-paper-pipeline" / "manifest.yaml"
REVIEWER = SKILLS / "nature-reviewer" / "manifest.yaml"


def _load_verifier():
    spec = importlib.util.spec_from_file_location("verify_scholarly_register_profile", VERIFIER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _version(text: str) -> tuple[int, ...]:
    for line in text.splitlines():
        if line.startswith("version:"):
            return tuple(int(part) for part in line.split(":", 1)[1].strip().split("."))
    raise AssertionError("manifest version missing")


def _section(kind: str) -> dict:
    profiles = {
        "abstract": {
            "reader_job": "recover the minimum sufficient scientific case without reading the paper",
            "rhetorical_mode": "compressed problem-to-answer case",
            "opening_moves": ["activate the concrete problem"],
            "paragraph_nuclei": ["question", "headline result", "bounded meaning"],
            "argument_tempo": "fast and selective",
            "agency": "author agency only when it clarifies what was done or established",
            "tense": "mixed according to field state, completed study, and durable conclusion",
            "stance": "direct for established findings and bounded for interpretation",
            "syntax_rhythm": "compact clauses with no artificial sentence-length variation",
            "citation_integration": "normally citation-light or unreferenced subject to target rules",
            "numerical_formal_density": "minimum decisive anchors unless reporting standards require more",
            "list_box_use": "structured labels or point form only when target/article type requires or benefits",
            "figure_table_interaction": "does not depend on figures or tables to be intelligible",
            "transition_behavior": "move progression is compressed rather than connector-heavy",
            "closing_handoff": "close on bounded meaning rather than a second result ledger",
        },
        "results": {
            "reader_job": "inspect the evidence chain that answers the paper's scientific questions",
            "rhetorical_mode": "evidence-led question and inference progression",
            "opening_moves": ["state the local question or why the analysis is needed"],
            "paragraph_nuclei": ["observation", "comparison", "discriminator", "bounded local inference"],
            "argument_tempo": "progressive and evidence paced",
            "agency": "active author agency when experimental or analytical choices matter",
            "tense": "often past for completed observations with field-dependent present for durable figure content",
            "stance": "observation and local inference are grammatically distinguished",
            "syntax_rhythm": "direct finite clauses for results with subordinate structure for conditions and boundaries",
            "citation_integration": "limited to method provenance or comparison needed for the local result",
            "numerical_formal_density": "prose states the pattern while displays carry dense arrays",
            "list_box_use": "paragraph-led unless the scientific object is genuinely parallel/discrete",
            "figure_table_interaction": "figure calls attach to the evidence sentence and do not duplicate all displayed values",
            "transition_behavior": "the previous result creates the reason for the next analysis",
            "closing_handoff": "bounded inference or unresolved question motivates the next block",
        },
        "discussion": {
            "reader_job": "interpret the findings relative to alternatives, prior evidence, boundaries, and consequences",
            "rhetorical_mode": "recursive interpretive synthesis",
            "opening_moves": ["state the strongest surviving finding at an interpretive level"],
            "paragraph_nuclei": ["interpretation", "prior-work relation", "alternative", "boundary", "implication"],
            "argument_tempo": "slower and more reflective than Results",
            "agency": "authorial interpretation is visible when responsibility matters",
            "tense": "often more present-tense because durable meaning and literature relations are discussed",
            "stance": "wider locally calibrated range from direct findings to conditional mechanism and speculation",
            "syntax_rhythm": "integrative sentences may be longer when they bind evidence and qualification",
            "citation_integration": "prior work is synthesized where the current result makes comparison meaningful",
            "numerical_formal_density": "usually lower than Results unless magnitude is central to interpretation",
            "list_box_use": "connected prose by default because inferential relations matter",
            "figure_table_interaction": "refers back to decisive displays without reciting them",
            "transition_behavior": "moves through interpretation, alternatives, boundaries, and implications rather than additive connectors",
            "closing_handoff": "close on consequence, live boundary, or discriminating next question",
        },
    }
    base = profiles[kind]
    return {
        "section_kind": kind,
        **base,
        "deliberately_absent": ["generic prestige filler"],
        "legitimate_alternatives": ["field-specific realization with the same reader job"],
        "transfer_decision": "adapt",
        "confidence": "high",
    }


def _record() -> dict:
    return {
        "schema_version": "1.0.0",
        "profile_id": "style-profile-1",
        "mode": "whole_manuscript",
        "target": "example research venue",
        "article_type": "research article",
        "archetype": "computational empirical",
        "evidence_sources": [
            {
                "source_id": "corpus1",
                "source_type": "corpus_meta",
                "reference": "cross-disciplinary move and phraseology corpus",
                "scope": "research article sections across disciplines",
                "support": "section and discipline materially condition rhetorical realization",
                "transfer_limit": "frequency is descriptive rather than a quality score",
            },
            {
                "source_id": "guide1",
                "source_type": "editorial_guidance",
                "reference": "current target/editorial guidance",
                "scope": "article-specific writing and structure expectations",
                "support": "target distinguishes summary, results, discussion, and display functions",
                "transfer_limit": "target mechanics are not universal prose laws",
            },
            {
                "source_id": "paper1",
                "source_type": "deep_paper",
                "reference": "recent close high-quality analogue paper",
                "scope": "abstract, results, discussion, displays",
                "support": "observed section-specific agency, stance, tempo, and display interaction",
                "transfer_limit": "learn functions and habits, never wording",
            },
        ],
        "sections": [_section("abstract"), _section("results"), _section("discussion")],
        "manuscript_voice_invariants": ["precise technical directness with stable terminology"],
        "cross_section_register_transitions": [
            "abstract compression opens into fuller argument",
            "results evidence reporting gives way to discussion interpretation",
        ],
        "copyright_boundary": {
            "source_sentences_stored": False,
            "phrase_templates_stored": False,
            "distinctive_wording_reused": False,
            "note": "Only rhetorical abstractions and observations are retained.",
        },
        "unresolved_gaps": [],
        "release": {"decision": "PASS", "notes": []},
    }


def test_contract_models_multiple_section_registers_without_detector_cosplay() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "one author thinking differently for different intellectual jobs",
        "storytelling means dependency, not drama",
        "abstract register",
        "introduction register",
        "theory / problem formulation register",
        "methods register",
        "results register",
        "discussion register",
        "caption / legend register",
        "table register",
        "supplementary / extended data register",
        "point form, lists, boxes and structured elements",
        "functional variation, not burstiness engineering",
        "there is no universal `avoid first person` rule",
        "citation integration is part of style",
        "numerical and formal density follow section purpose",
        "figures and tables change the prose register",
        "human scholarly writing is not one style",
    ):
        assert marker in text, marker

    assert "ai-detector evasion" in text
    assert "never store or reuse characteristic sentences" in text
    assert "do not set a global `figures per 1,000 words`" in text


def test_contract_preserves_legitimate_structured_and_formal_registers() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    assert "jama-style trial" in text
    assert "cell-style highlights" in text
    assert "roadmaps" in text
    assert "the following theorem" in text
    assert "resource organization itself is the contribution" in text
    assert "do not `de-mechanize` mandated reporting structure" in text


def test_research_ledger_separates_corpus_guidance_and_deep_papers() -> None:
    text = RESEARCH.read_text(encoding="utf-8").lower()
    for marker in (
        "large genre / corpus evidence",
        "official editorial / venue evidence",
        "deep reading of real papers",
        "500 published research article introductions",
        "900 methods sections",
        "5,910 abstracts",
        "nature methods",
        "jama",
        "cell press",
        "nature physics",
        "nature cell biology",
        "nature machine intelligence",
        "scientific data",
        "jmlr",
        "there is no universal `top-journal voice`",
        "storytelling means intellectual dependency",
        "point form is a publication-surface decision",
    ):
        assert marker in text, marker


def test_schema_forbids_phrase_banks_and_records_section_habits() -> None:
    text = SCHEMA.read_text(encoding="utf-8")
    for marker in (
        '"source_type"',
        '"section_kind"',
        '"reader_job"',
        '"rhetorical_mode"',
        '"paragraph_nuclei"',
        '"agency"',
        '"stance"',
        '"syntax_rhythm"',
        '"citation_integration"',
        '"numerical_formal_density"',
        '"list_box_use"',
        '"figure_table_interaction"',
        '"copyright_boundary"',
        '"phrase_templates_stored"',
    ):
        assert marker in text


def test_valid_whole_manuscript_register_profile_passes() -> None:
    verifier = _load_verifier()
    result = verifier.validate(_record())
    assert result["decision"] == "PASS"
    assert result["counts"] == {"error": 0, "review": 0}


def test_uniform_register_across_sections_requires_review() -> None:
    verifier = _load_verifier()
    record = _record()
    first = record["sections"][0]
    for section in record["sections"][1:]:
        for field in (
            "rhetorical_mode",
            "argument_tempo",
            "agency",
            "stance",
            "syntax_rhythm",
            "list_box_use",
            "transition_behavior",
            "closing_handoff",
        ):
            section[field] = first[field]
    record["release"]["decision"] = "REVIEW"
    result = verifier.validate(record)
    assert result["decision"] == "REVIEW"
    assert any(item["code"] == "uniform_register_across_sections" for item in result["findings"])


def test_missing_evidence_layer_is_review_not_fake_certainty() -> None:
    verifier = _load_verifier()
    record = _record()
    record["evidence_sources"] = [s for s in record["evidence_sources"] if s["source_type"] != "corpus_meta"]
    record["release"]["decision"] = "REVIEW"
    result = verifier.validate(record)
    assert result["decision"] == "REVIEW"
    assert any(item["code"] == "whole_profile_evidence_layer_gap" for item in result["findings"])


def test_copied_phrase_or_detector_field_blocks_profile() -> None:
    verifier = _load_verifier()
    record = _record()
    record["phrase_templates"] = ["copied source wording"]
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "forbidden_style_copy_or_detector_field" for item in result["findings"])


def test_local_section_profile_can_be_narrow_when_close_paper_is_present() -> None:
    verifier = _load_verifier()
    record = _record()
    record["mode"] = "local_section"
    record["sections"] = [_section("results")]
    record["evidence_sources"] = [s for s in record["evidence_sources"] if s["source_type"] == "deep_paper"]
    record["cross_section_register_transitions"] = []
    result = verifier.validate(record)
    assert result["decision"] == "PASS"


def test_kernel_keeps_compact_one_author_multiple_registers_invariant() -> None:
    text = KERNEL.read_text(encoding="utf-8").lower()
    assert "one author, multiple scholarly registers" in text
    assert "section-register-and-human-scholarly-style.md" in text


def test_public_skills_route_register_contract_progressively() -> None:
    contract = "section-register-and-human-scholarly-style.md"
    research = "top-tier-section-register-style-evidence-2026-09-02.md"
    schema = "scholarly-register-profile.schema.json"
    verifier = "verify_scholarly_register_profile.py"

    writing = WRITING.read_text(encoding="utf-8")
    pipeline = PIPELINE.read_text(encoding="utf-8")
    reviewer = REVIEWER.read_text(encoding="utf-8")

    for text in (writing, pipeline, reviewer):
        assert contract in text
        assert research in text
        assert schema in text
        assert verifier in text
        always = text.split("references:", 1)[0]
        assert contract not in always

    assert _version(writing) >= (1, 19, 0)
    assert _version(pipeline) >= (1, 22, 0)
    assert _version(reviewer) >= (3, 6, 0)
