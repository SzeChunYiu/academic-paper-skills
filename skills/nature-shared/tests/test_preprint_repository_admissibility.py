from __future__ import annotations

import datetime
import importlib.util
import json
from pathlib import Path

import unittest

SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
CONTRACT = SHARED / "core" / "preprint-repository-admissibility.md"
RULES = SHARED / "preprint-repositories" / "arxiv-admissibility-rules.json"
PIPELINE_MANIFEST = SKILLS / "academic-paper-pipeline" / "manifest.yaml"
PIPELINE_SKILL = SKILLS / "academic-paper-pipeline" / "SKILL.md"


def _flat(path: Path) -> str:
    """Lowercased, whitespace-collapsed text, so assertions survive line wrapping."""
    import re as _re

    return _re.sub(r"\s+", " ", path.read_text(encoding="utf-8").lower())


def _load(name: str):
    path = SHARED / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader, path
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


detector = _load("detect_manuscript_content_type")
gate = _load("verify_preprint_admissibility")
integrity = _load("audit_deposit_integrity")


RESEARCH_BODY = r"""
\documentclass{article}
\begin{document}
\section{Introduction}
Prior work is summarised in \citep{smith2020}.
\section{Methods}
We ran the protocol on 1,200 instances.
\section{Results}
\begin{table}\begin{tabular}{cc}a&b\end{tabular}\end{table}
The federation reproduced 0.983 of decisions, with $p = 0.0032$.
\section{Discussion}
\end{document}
"""

SYNTHESIS_BODY = r"""
\documentclass{article}
\begin{document}
\section{Introduction}
This survey reviews the landscape.
\section{Background}
\section{Related work}
\section{State of the art}
\section{Open problems}
\section{Outlook}
\end{document}
"""


# --------------------------------------------------------------------------
# The contract document
# --------------------------------------------------------------------------


def _rules_doc(policy_as_of: str = "2026-09-08") -> dict:
    doc = json.loads(RULES.read_text(encoding="utf-8"))
    doc["policy_as_of"] = policy_as_of
    return doc


def _decl(**kw) -> dict:
    base = {
        "schema_version": gate.DECLARATION_SCHEMA,
        "repository": "arXiv",
        "primary_category": "cs.AI",
        "cross_list": [],
        "declared_content_type": "research",
        "peer_review_doi": None,
    }
    base.update(kw)
    return base


TODAY = datetime.date(2026, 9, 8)


def _detection(indicators: list[str], mismatch: str | None = None) -> dict:
    return {
        "structural": {"verdict": "PRIMARY_RESEARCH_PRESENT",
                       "negation_conflicts_with_structure": False},
        "declared": {"type": None},
        "synthesis_indicators": indicators,
        "mismatch": mismatch,
    }


class PreprintRepositoryAdmissibilityTests(unittest.TestCase):
    """Admissibility gate, detector and deposit-integrity audit."""

    def test_contract_exists_and_states_the_governing_rule(self) -> None:
        text = _flat(CONTRACT)
        assert "moderated venue" in text
        # The whole point: renaming must not satisfy the gate.
        assert "cannot be satisfied by renaming" in text
        assert "exit code 2 is not a pass" in text


    def test_contract_forbids_relabelling_as_a_remedy_when_the_label_overstates(self) -> None:
        text = _flat(CONTRACT)
        assert "relabelling is not available" in text or "relabelling is not an available" in text


    def test_contract_protects_the_disclosure_and_refuses_detector_targeting(self) -> None:
        text = _flat(CONTRACT)
        assert "that disclosure stays" in text
        assert "machine-text detector" in text


    def test_contract_states_its_own_limits(self) -> None:
        text = _flat(CONTRACT)
        assert "known limits" in text
        assert "not that none" in text  # absence of a rule is not clearance


# --------------------------------------------------------------------------
# Wiring
# --------------------------------------------------------------------------

    def test_pipeline_routes_the_contract_without_growing_the_always_load_set(self) -> None:
        """Routed on demand, not always loaded: the working set is deliberately small.

        The contract must still be unmissable, so the manifest carries a routing
        condition and SKILL.md says in words that it is not optional.
        """
        manifest = PIPELINE_MANIFEST.read_text(encoding="utf-8")
        assert "core/preprint-repository-admissibility.md" in manifest
        always, _, rest = manifest.partition("references:")
        assert "preprint-repository-admissibility" not in always
        assert "preprint-repository-admissibility" in rest

        skill = PIPELINE_SKILL.read_text(encoding="utf-8")
        assert "core/preprint-repository-admissibility.md" in skill
        assert "Preprint deposit admissibility gate" in skill
        assert "not optional" in skill


    def test_pipeline_exposes_all_three_executables(self) -> None:
        manifest = PIPELINE_MANIFEST.read_text(encoding="utf-8")
        for script in (
            "detect_manuscript_content_type.py",
            "verify_preprint_admissibility.py",
            "audit_deposit_integrity.py",
        ):
            assert script in manifest, script


# --------------------------------------------------------------------------
# Rules file: policy is data, and carries its source
# --------------------------------------------------------------------------

    def test_rules_carry_a_source_url_and_operative_quotation(self) -> None:
        doc = json.loads(RULES.read_text(encoding="utf-8"))
        assert doc["schema_version"] == gate.RULES_SCHEMA
        assert doc["sources"], "a ruleset with no source is not usable"
        src = doc["sources"][0]
        assert src["url"].startswith("https://")
        assert src["quotes"]["scope"]
        assert src["quotes"]["consequence"]
        for rule in doc["rules"]:
            assert rule["applies_to"]["archives"]
            assert rule["triggers_on_content_types"]


    def test_rules_distinguish_named_from_construed_content_types(self) -> None:
        """A construed type must not be presented as quoted policy."""
        doc = json.loads(RULES.read_text(encoding="utf-8"))
        basis = doc["rules"][0]["content_type_basis"]
        assert basis["review"] == "named"
        assert basis["position"] == "named"
        assert basis["perspective"] == "construed"


    def test_no_rule_penalises_disclosed_ai_assistance(self) -> None:
        doc = json.loads(RULES.read_text(encoding="utf-8"))
        blob = json.dumps(doc["rules"]).lower()
        for token in ("ai_disclosure", "ai assistance", "llm"):
            assert token not in blob, "disclosure must never be a blocking condition"
        topics = [n["topic"].lower() for n in doc["non_rules"]]
        assert any("ai assistance" in t for t in topics)

    def test_non_cs_archives_carry_an_advisory_not_silence(self) -> None:
        """No documented refusal practice outside cs is not the same as permission."""
        res = gate.evaluate(
            _rules_doc(),
            _decl(primary_category="math.NT", declared_content_type="survey"),
            _detection([]), TODAY, 120,
        )
        assert res["verdict"] == "PASS", "an advisory must never block"
        assert res["advisories"], "the site-wide standard must still be surfaced"
        advisory = [f for f in res["findings"] if f["verdict"] == "ADVISORY"]
        assert advisory
        # An advisory is not a satisfied requirement; nothing was satisfied.
        assert advisory[0]["verdict"] != "SATISFIED"

    def test_advisory_does_not_fire_on_ordinary_research(self) -> None:
        res = gate.evaluate(_rules_doc(), _decl(primary_category="math.NT"),
                            _detection([]), TODAY, 120)
        assert res["verdict"] == "PASS"
        assert res["advisories"] == []

    def test_cs_block_still_outranks_the_advisory(self) -> None:
        res = gate.evaluate(_rules_doc(), _decl(declared_content_type="survey"),
                            _detection([]), TODAY, 120)
        assert res["verdict"] == "BLOCK"

    def test_arxiv_ai_policy_is_cited_as_responsibility_not_refusal(self) -> None:
        doc = json.loads(RULES.read_text(encoding="utf-8"))
        src = [s for s in doc["sources"] if s["id"] == "arxiv-moderation-policy"]
        assert src, "the site-wide moderation policy must be a cited source"
        q = src[0]["quotes"]["generative_ai_responsibility"].lower()
        assert "responsibility of the author" in q
        assert "should not be listed as an author" in q

    def test_contract_requires_compiling_the_packaged_source(self) -> None:
        """A package that does not build cannot be deposited at all."""
        text = _flat(CONTRACT)
        assert "compiles the submission itself" in text
        assert "hard deposit blocker" in text
        assert "compile the packaged source on the repository's toolchain" in text

    def test_contract_pins_the_repository_toolchain_not_the_newest(self) -> None:
        text = _flat(CONTRACT)
        assert "tex live 2023 and tex live 2025" in text
        assert "with 2025 being the default" in text
        assert "nobody can reach is worse than none" in text

    def test_contract_requires_shipping_the_bibliography_with_the_source(self) -> None:
        """Adding citations without their source turns a good package into a blocked one."""
        text = _flat(CONTRACT)
        assert "block you from proceeding with your submission" in text

    def test_buildability_sources_are_cited(self) -> None:
        doc = json.loads(RULES.read_text(encoding="utf-8"))
        ids = {s["id"] for s in doc["sources"]}
        assert {"arxiv-tex-submission", "arxiv-texlive"} <= ids

    def test_buildability_is_declared_a_non_rule_with_its_reason(self) -> None:
        """It cannot be decided from metadata, so it must not masquerade as a rule."""
        doc = json.loads(RULES.read_text(encoding="utf-8"))
        entry = [n for n in doc["non_rules"] if "buildability" in n["topic"].lower()]
        assert entry, "buildability must be recorded"
        assert "cannot be decided from metadata" in entry[0]["statement"]

    def test_contract_requires_a_clean_log_not_merely_a_pdf(self) -> None:
        """pdflatex writes output even when it has errored."""
        text = _flat(CONTRACT)
        assert "a produced pdf is not a clean build" in text
        assert "-halt-on-error" in text
        assert "no `! ` lines" in text or "no ! lines" in text

    def test_contract_requires_rebuilding_from_current_source(self) -> None:
        text = _flat(CONTRACT)
        assert "never a working copy taken earlier" in text
        assert "leaves no trace in the diff" in text

    def test_the_detector_bias_claim_is_cited_not_asserted(self) -> None:
        """The one outside-world claim this contract makes must carry its source."""
        doc = json.loads(RULES.read_text(encoding="utf-8"))
        ev = [n.get("evidence") for n in doc["non_rules"] if n.get("evidence")]
        assert ev, "the detector claim must cite a source"
        assert ev[0]["doi"]
        assert "non-native" in ev[0]["finding"].lower()
        assert "patterns" in _flat(CONTRACT)
        assert "10.1016/j.patter.2023.100779" in _flat(CONTRACT)


# --------------------------------------------------------------------------
# Detector
# --------------------------------------------------------------------------

    def test_detector_reads_a_research_body_as_primary_research(self) -> None:
        rec = detector.detect(RESEARCH_BODY, "tex", {"title": "An exact study of X"})
        assert rec["structural"]["verdict"].startswith("PRIMARY_RESEARCH")
        assert rec["synthesis_indicators"] == []


    def test_detector_fires_on_a_survey_title_alone(self) -> None:
        rec = detector.detect(RESEARCH_BODY, "tex", {"title": "Large Language Models: A Survey"})
        assert "declared_review_or_position_label" in rec["synthesis_indicators"]


    def test_detector_fires_on_an_explicit_primary_research_negation(self) -> None:
        body = RESEARCH_BODY.replace(
            "\\section{Discussion}",
            "\\section{Discussion}\nThis work does not report a new primary empirical study.",
        )
        rec = detector.detect(body, "tex", {"title": "A study"})
        assert "explicit_primary_research_negation" in rec["synthesis_indicators"]
        # A denial contradicting a real Results section is itself the finding.
        assert rec["structural"]["negation_conflicts_with_structure"] is True


    def test_detector_reads_a_synthesis_body_as_synthesis(self) -> None:
        rec = detector.detect(SYNTHESIS_BODY, "tex", {"title": "A Survey of Things"})
        assert rec["synthesis_indicators"]


    def test_composition_is_not_read_as_a_position_paper(self) -> None:
        """Substring matching read 'the composition calculus' as a position paper."""
        roles = detector._role_of("The composition calculus")
        assert "synthesis" not in roles


    def test_descriptively_named_results_sections_are_not_penalised(self) -> None:
        """Real papers name results sections without using the word 'Results'."""
        body = RESEARCH_BODY.replace("\\section{Results}", "\\section{Nine protected cross-domain cases}")
        rec = detector.detect(body, "tex", {"title": "A bounded transfer law"})
        assert rec["structural"]["verdict"].startswith("PRIMARY_RESEARCH")
        assert rec["synthesis_indicators"] == []


    def test_markdown_headings_are_found_in_a_mixed_format_body(self) -> None:
        """A LaTeX shell pulling Markdown prose still has sections."""
        body = "\\documentclass{article}\n\\begin{document}\n## Results\n\nWe measured 0.98.\n"
        assert "Results" in detector.extract_sections(body, "tex")


# --------------------------------------------------------------------------
# Admissibility gate
# --------------------------------------------------------------------------

    def test_gate_blocks_a_perspective_in_cs_without_peer_review(self) -> None:
        res = gate.evaluate(_rules_doc(), _decl(declared_content_type="perspective"),
                            _detection([]), TODAY, 120)
        assert res["verdict"] == "BLOCK"


    def test_gate_passes_the_same_paper_once_peer_reviewed(self) -> None:
        res = gate.evaluate(_rules_doc(),
                            _decl(declared_content_type="perspective", peer_review_doi="10.1/x"),
                            _detection([]), TODAY, 120)
        assert res["verdict"] == "PASS"


    def test_gate_passes_ordinary_research_in_cs(self) -> None:
        res = gate.evaluate(_rules_doc(), _decl(), _detection([]), TODAY, 120)
        assert res["verdict"] == "PASS"


    def test_rule_is_out_of_scope_for_a_mathematics_primary(self) -> None:
        res = gate.evaluate(_rules_doc(),
                            _decl(primary_category="math.NT", declared_content_type="survey"),
                            _detection([]), TODAY, 120)
        assert res["verdict"] == "PASS"


    def test_cross_list_into_cs_does_not_escape_the_cs_practice(self) -> None:
        res = gate.evaluate(_rules_doc(),
                            _decl(primary_category="math.CO", cross_list=["cs.AI"],
                                  declared_content_type="survey"),
                            _detection([]), TODAY, 120)
        assert res["verdict"] == "BLOCK"


    def test_evidence_of_synthesis_triggers_even_when_the_author_declares_research(self) -> None:
        res = gate.evaluate(_rules_doc(), _decl(),
                            _detection(["declared_review_or_position_label"]), TODAY, 120)
        assert res["verdict"] == "BLOCK"


    def test_unset_category_cannot_be_evaluated_and_is_not_a_pass(self) -> None:
        res = gate.evaluate(_rules_doc(), _decl(primary_category="AUTHOR_TO_SET"),
                            _detection([]), TODAY, 120)
        assert res["verdict"] == "CANNOT_EVALUATE"


    def test_missing_detection_cannot_be_evaluated(self) -> None:
        res = gate.evaluate(_rules_doc(), _decl(), None, TODAY, 120)
        assert res["verdict"] == "CANNOT_EVALUATE"


    def test_stale_ruleset_refuses_to_certify(self) -> None:
        res = gate.evaluate(_rules_doc(policy_as_of="2020-01-01"), _decl(),
                            _detection([]), TODAY, 120)
        assert res["verdict"] == "CANNOT_EVALUATE"
        assert any("old" in r for r in res["not_evaluable_because"])


    def test_overstating_label_blocks_and_refuses_to_offer_a_relabel(self) -> None:
        res = gate.evaluate(_rules_doc(), _decl(),
                            _detection([], mismatch="LABEL_OVERSTATES_CONTENT"), TODAY, 120)
        assert res["verdict"] == "BLOCK"
        note = " ".join(res["integrity_notes"]).lower()
        assert "not an available remedy" in note


    def test_understating_label_is_reported_as_correctable(self) -> None:
        res = gate.evaluate(_rules_doc(), _decl(),
                            _detection([], mismatch="LABEL_UNDERSTATES_CONTENT"), TODAY, 120)
        note = " ".join(res["integrity_notes"]).lower()
        assert "legitimate" in note


    def test_pass_is_not_described_as_a_prediction(self) -> None:
        res = gate.evaluate(_rules_doc(), _decl(), _detection([]), TODAY, 120)
        assert "not a prediction" in res["meaning"].lower()


# --------------------------------------------------------------------------
# Deposit integrity
# --------------------------------------------------------------------------

    def test_missing_reference_apparatus_is_an_error(self) -> None:
        body = "\\documentclass{article}\\begin{document}\\section{Conclusion}Done.\\end{document}"
        res = integrity.audit(body, [], None)
        assert res["verdict"] == "FINDINGS"
        assert any(f["code"] == "no_reference_apparatus" for f in res["findings"])


    def test_a_paper_with_a_bibliography_is_clean(self) -> None:
        res = integrity.audit(RESEARCH_BODY + "\n\\printbibliography\n",
                              ["@article{smith2020, title={x}}"], None)
        assert res["error_count"] == 0


    def test_setcitestyle_is_not_read_as_a_fabricated_reference(self) -> None:
        body = (RESEARCH_BODY.replace("\\begin{document}",
                "\\setcitestyle{authoryear,round,citesep={;}}\n\\begin{document}")
                + "\n\\printbibliography\n")
        res = integrity.audit(body, ["@article{smith2020, title={x}}"], None)
        assert not any(f["code"] == "dangling_citation_keys" for f in res["findings"])


    def test_nocite_star_is_not_read_as_a_fabricated_reference(self) -> None:
        body = RESEARCH_BODY + "\n\\nocite{*}\n\\printbibliography\n"
        res = integrity.audit(body, ["@article{smith2020, title={x}}"], None)
        assert not any(f["code"] == "dangling_citation_keys" for f in res["findings"])


    def test_a_genuinely_dangling_key_is_still_caught(self) -> None:
        body = RESEARCH_BODY.replace("smith2020", "ghost1999") + "\n\\printbibliography\n"
        res = integrity.audit(body, ["@article{smith2020, title={x}}"], None)
        assert any(f["code"] == "dangling_citation_keys" for f in res["findings"])


    def test_assistant_voice_is_an_error(self) -> None:
        body = RESEARCH_BODY.replace("\\section{Discussion}",
                                     "\\section{Discussion}\nCertainly! Here is the revised section.")
        res = integrity.audit(body + "\\printbibliography", ["@a{smith2020,t={x}}"], None)
        assert any(f["code"] == "assistant_voice_leakage" for f in res["findings"])


    def test_preamble_placeholder_is_a_warning_not_an_error(self) -> None:
        body = ("\\documentclass{article}\n\\def\\openreview{XXXX}\n\\begin{document}\n"
                "\\section{Results}A result.\\printbibliography\\end{document}")
        res = integrity.audit(body, ["@a{k,t={x}}"], None)
        codes = {f["code"]: f["severity"] for f in res["findings"]}
        assert codes.get("unresolved_placeholder_in_preamble") == "WARN"
        assert "unresolved_placeholder" not in codes


    def test_body_placeholder_is_an_error(self) -> None:
        body = ("\\documentclass{article}\n\\begin{document}\n\\section{Results}\n"
                "TODO write this up.\\printbibliography\\end{document}")
        res = integrity.audit(body, ["@a{k,t={x}}"], None)
        assert any(f["code"] == "unresolved_placeholder" for f in res["findings"])


    def test_broken_cross_reference_is_caught(self) -> None:
        body = RESEARCH_BODY.replace("\\section{Results}",
                                     "\\section{Results}\\label{res}See \\ref{nowhere}.")
        res = integrity.audit(body + "\\printbibliography", ["@a{smith2020,t={x}}"], None)
        assert any(f["code"] == "unresolved_cross_reference" for f in res["findings"])


    def test_disclosure_divergence_is_informational_and_never_an_error(self) -> None:
        house = "Generative AI tools were used for drafting and editing assistance."
        body = (RESEARCH_BODY + "\nLarge language model systems were used extensively.\n"
                "\\printbibliography")
        res = integrity.audit(body, ["@a{smith2020,t={x}}"], house)
        finding = [f for f in res["findings"] if f["code"] == "disclosure_diverges_from_house_form"]
        assert finding and finding[0]["severity"] == "INFO"
        assert res["error_count"] == 0


    def test_audit_declares_that_style_is_out_of_scope(self) -> None:
        res = integrity.audit(RESEARCH_BODY + "\\printbibliography", ["@a{smith2020,t={x}}"], None)
        assert "detector" in res["scope_note"].lower()


if __name__ == "__main__":
        unittest.main()

