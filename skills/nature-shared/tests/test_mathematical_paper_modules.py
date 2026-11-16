from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
REFEREE = SHARED / "core" / "mathematical-referee-review.md"
EXPOSITION = SHARED / "core" / "mathematical-exposition-contract.md"
SCRIPT = SHARED / "scripts" / "audit_math_manuscript.py"
ATLAS = SHARED / "core" / "paper-archetype-atlas.md"

sys.path.insert(0, str(SHARED / "scripts"))
import audit_math_manuscript as audit_module  # noqa: E402

PREAMBLE = r"""\documentclass{amsart}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{hypothesis}[theorem]{Hypothesis}
\begin{document}
"""


def write(tmp: Path, body: str, name: str = "main.tex") -> Path:
    path = tmp / name
    path.write_text(PREAMBLE + body + "\n\\end{document}\n", encoding="utf-8")
    return path


def codes(report: dict) -> list[str]:
    return [f["code"] for f in report["findings"]]


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").replace("*", "").lower().split())


def test_referee_contract_keeps_axes_separate_and_names_blocking_rules() -> None:
    text = flat(REFEREE)
    for marker in (
        "the four separated axes", "correctness", "checkability", "novelty / priority",
        "significance / fit", "restatement identity", "condition propagation", "silent condition",
        "verified_with_fix", "small-case falsification", "agreement of two programs",
        "computer-assisted", "at least two", "mathematics referee report skeleton",
        "simulated acceptance is not real acceptance", "minor comments are never blocking",
    ):
        assert marker in text, marker


def test_referee_contract_grades_its_sources_and_flags_unread_text() -> None:
    text = REFEREE.read_text(encoding="utf-8")
    assert "**D (official policy).** The American Mathematical Society" in text
    assert "not re-read" in text
    assert "## Contents" in text


def test_exposition_contract_freezes_scope_and_lists_checks() -> None:
    text = flat(EXPOSITION)
    for marker in (
        "main results stated precisely", "in its statement", "revision rules for a frozen-scope paper",
        "may not add new theorems", "pre-submission checklist", "msc", "two programs",
    ):
        assert marker in text, marker


def test_archetype_atlas_routes_theory_papers_to_the_math_modules() -> None:
    text = ATLAS.read_text(encoding="utf-8")
    assert "mathematical-referee-review.md" in text
    assert "mathematical-exposition-contract.md" in text


def test_reviewer_and_pipeline_manifests_load_the_math_modules_on_demand() -> None:
    for manifest in (SKILLS / "nature-reviewer" / "manifest.yaml", SKILLS / "academic-paper-pipeline" / "manifest.yaml"):
        text = manifest.read_text(encoding="utf-8")
        assert "mathematical-referee-review.md" in text, manifest
        assert "audit_math_manuscript.py" in text, manifest


def test_clean_paper_has_no_errors(tmp_path: Path) -> None:
    path = write(tmp_path, r"""
\begin{lemma}\label{lem:a} One. \end{lemma}
\begin{proof} Direct. \end{proof}
\begin{theorem}\label{thm:b} Two. \end{theorem}
\begin{proof} By Lemma~\ref{lem:a}. \end{proof}
""")
    report = audit_module.audit(path)
    assert report["ok"], report["findings"]
    assert report["dependency_graph"] == {"thm:b": ["lem:a"]}


def test_undefined_reference_duplicate_label_and_missing_citation_are_errors(tmp_path: Path) -> None:
    (tmp_path / "refs.bib").write_text("@article{known, title={x}}\n", encoding="utf-8")
    path = write(tmp_path, r"""
\begin{theorem}\label{thm:a} See \cite{known,unknown}. \end{theorem}
\begin{proof} By Lemma~\ref{lem:missing}. \end{proof}
\begin{lemma}\label{thm:a} Again. \end{lemma}
\begin{proof} Done. \end{proof}
\bibliography{refs}
""")
    report = audit_module.audit(path)
    found = codes(report)
    assert {"undefined_reference", "duplicate_label", "undefined_citation"} <= set(found)
    assert not report["ok"]


def test_dependency_cycle_is_an_error_and_forward_reference_a_warning(tmp_path: Path) -> None:
    path = write(tmp_path, r"""
\begin{lemma}\label{lem:a} A. \end{lemma}
\begin{proof} Use Lemma~\ref{lem:b}. \end{proof}
\begin{lemma}\label{lem:b} B. \end{lemma}
\begin{proof} Use Lemma~\ref{lem:a}. \end{proof}
""")
    report = audit_module.audit(path)
    assert "dependency_cycle" in codes(report)
    assert "forward_reference_in_proof" in codes(report)


def test_silent_condition_is_an_error_and_named_condition_is_not(tmp_path: Path) -> None:
    silent = write(tmp_path, r"""
\begin{hypothesis}\label{hyp:Y} A finite check holds. \end{hypothesis}
\begin{theorem}\label{thm:main} The value is $27q-2$. \end{theorem}
\begin{proof} By Hypothesis~\ref{hyp:Y}. \end{proof}
""", "silent.tex")
    assert "silent_condition" in codes(audit_module.audit(silent))
    named = write(tmp_path, r"""
\begin{hypothesis}\label{hyp:Y} A finite check holds. \end{hypothesis}
\begin{theorem}\label{thm:main} Assume Hypothesis~\ref{hyp:Y}. The value is $27q-2$. \end{theorem}
\begin{proof} By Hypothesis~\ref{hyp:Y}. \end{proof}
""", "named.tex")
    report = audit_module.audit(named)
    assert "silent_condition" not in codes(report)
    assert report["conditional_statements"] == ["thm:main"]


def test_condition_propagates_through_a_lemma(tmp_path: Path) -> None:
    path = write(tmp_path, r"""
\begin{hypothesis}\label{hyp:Y} H. \end{hypothesis}
\begin{lemma}\label{lem:a} Under Hypothesis~\ref{hyp:Y}, A. \end{lemma}
\begin{proof} By Hypothesis~\ref{hyp:Y}. \end{proof}
\begin{theorem}\label{thm:main} B. \end{theorem}
\begin{proof} By Lemma~\ref{lem:a}. \end{proof}
""")
    report = audit_module.audit(path)
    silent = [f for f in report["findings"] if f["code"] == "silent_condition"]
    assert [f["token"] for f in silent] == ["thm:main"]


def test_abstract_without_conditions_is_flagged_when_a_result_is_conditional(tmp_path: Path) -> None:
    path = write(tmp_path, r"""
\begin{abstract} We determine the constant for all q. \end{abstract}
\begin{hypothesis}\label{hyp:Y} H. \end{hypothesis}
\begin{theorem}\label{thm:main} Assume Hypothesis~\ref{hyp:Y}. B. \end{theorem}
\begin{proof} By Hypothesis~\ref{hyp:Y}. \end{proof}
""")
    assert "abstract_omits_conditions" in codes(audit_module.audit(path))


def test_late_and_paragraph_proofs_and_restatements_are_recognized(tmp_path: Path) -> None:
    path = write(tmp_path, r"""
\begin{theorem}\label{thm:intro} Main. \end{theorem}
This is Theorem~\ref{thm:body}.
\begin{theorem}\label{thm:two} Second. \end{theorem}
\begin{lemma}\label{lem:a} A. \end{lemma}
\begin{proof} Direct. \end{proof}
\begin{theorem}\label{thm:body} Main again. \end{theorem}
\begin{proof}[Proof of Theorem~\ref{thm:body}] By Lemma~\ref{lem:a}. \end{proof}
\emph{Proof of Theorem~\ref{thm:two}.} Similar.
""")
    report = audit_module.audit(path)
    assert "statement_without_proof" not in codes(report), report["findings"]
    assert "forward_reference_in_proof" not in codes(report)
    assert "paragraph_proof" in codes(report)
    assert report["dependency_graph"]["thm:intro"] == ["thm:body"]


def test_statement_without_proof_and_markers(tmp_path: Path) -> None:
    path = write(tmp_path, r"""
\begin{theorem}\label{thm:a} Claimed. \end{theorem}
Clearly this is fine. TODO: finish.
""")
    report = audit_module.audit(path)
    found = codes(report)
    assert "statement_without_proof" in found
    assert "handwave_marker" in found
    assert "todo_marker" in found


def test_input_files_are_followed_and_missing_ones_reported(tmp_path: Path) -> None:
    (tmp_path / "sec.tex").write_text("\\begin{lemma}\\label{lem:s} S. \\end{lemma}\n\\begin{proof} D. \\end{proof}\n",
                                      encoding="utf-8")
    path = write(tmp_path, r"""
\input{sec}
\input{absent}
\begin{theorem}\label{thm:a} T. \end{theorem}
\begin{proof} By Lemma~\ref{lem:s}. \end{proof}
""")
    report = audit_module.audit(path)
    assert "sec.tex" in report["files"]
    assert "undefined_reference" not in codes(report)
    assert "missing_input" in codes(report)


def test_comments_are_ignored(tmp_path: Path) -> None:
    path = write(tmp_path, r"""
% \ref{nowhere} TODO
\begin{theorem}\label{thm:a} T. \end{theorem}
\begin{proof} 100\% done. \end{proof}
""")
    assert audit_module.audit(path)["ok"]


def test_command_line_exit_codes(tmp_path: Path) -> None:
    good = write(tmp_path, "\\begin{theorem}\\label{t} T.\\end{theorem}\\begin{proof}D.\\end{proof}", "good.tex")
    bad = write(tmp_path, "\\begin{theorem}\\label{t} T.\\end{theorem}\\begin{proof}\\ref{x}\\end{proof}", "bad.tex")
    run = lambda *a: subprocess.run([sys.executable, str(SCRIPT), *a], capture_output=True, text=True)
    assert run(str(good)).returncode == 0
    result = run(str(bad))
    assert result.returncode == 1
    assert json.loads(result.stdout)["counts"]["error"] == 1
    assert run(str(tmp_path / "none.tex")).returncode == 2
