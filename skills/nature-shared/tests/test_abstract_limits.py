from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
SCRIPT = SHARED / "scripts" / "verify_abstract_limits.py"
CONTRACT = SHARED / "core" / "preprint-repository-admissibility.md"
MANIFEST = SKILLS / "academic-paper-pipeline" / "manifest.yaml"


def _load():
    spec = importlib.util.spec_from_file_location("verify_abstract_limits", SCRIPT)
    assert spec and spec.loader
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


mod = _load()
SHORT = "We report a bounded result. " * 8
LONG = "We report a bounded result with several qualifications. " * 45


class AbstractLimitTests(unittest.TestCase):
    """Two units, two venues, one binding constraint."""

    def test_arxiv_limit_is_recorded_with_its_source(self) -> None:
        spec = mod.REPOSITORY_LIMITS["arxiv"]
        assert spec["chars"] == 1920
        assert "will not be accepted" in spec["quote"]
        assert spec["source"].startswith("https://info.arxiv.org")

    def test_a_long_abstract_is_over_the_repository_limit(self) -> None:
        r = mod.evaluate(LONG, "arxiv", None, None)
        assert r["verdict"] == "OVER"
        assert any("over the arxiv limit" in f["message"].lower() for f in r["findings"])

    def test_a_short_abstract_is_within_limits(self) -> None:
        assert mod.evaluate(SHORT, "arxiv", None, None)["verdict"] == "WITHIN_LIMITS"

    def test_both_venues_are_checked_together(self) -> None:
        r = mod.evaluate(SHORT, "arxiv", 10, "Nature Machine Intelligence")
        assert r["verdict"] == "OVER"
        assert len(r["limits_checked"]) == 2

    def test_the_binding_limit_is_named(self) -> None:
        """An author writing to words should not have to convert to characters."""
        r = mod.evaluate(SHORT, "arxiv", 200, "NMI")
        assert r["binding_limit"]["limit"] in ("arxiv characters", "NMI words")
        assert "headroom" in r["binding_limit"]

    def test_an_unknown_repository_cannot_be_evaluated_not_passed(self) -> None:
        r = mod.evaluate(SHORT, "somewhere-else", None, None)
        assert any(f["severity"] == "CANNOT_EVALUATE" for f in r["findings"])

    def test_characters_are_counted_after_markup_is_resolved(self) -> None:
        assert mod.plain(r"\textbf{Result} of $x$ \cite{a}") == "Result of x"

    def test_an_escaped_percent_does_not_truncate_the_abstract(self) -> None:
        """A literal \\% is content; only an unescaped % starts a comment."""
        got = mod.plain(r"We report 14.29\% false promotion and 0.857 accuracy.")
        assert "false promotion" in got
        assert "0.857" in got
        assert "14.29%" in got

    def test_a_real_comment_is_still_stripped(self) -> None:
        assert mod.plain("Result here. % an editorial note\nMore text.") == "Result here. More text."

    def test_abstract_is_found_in_all_four_conventions(self) -> None:
        for body in (r"\begin{abstract}Bounded result here.\end{abstract}",
                     r"\subsection{Abstract}\label{abstract}Bounded result here.\section{X}",
                     "## Abstract\n\nBounded result here.\n\n## Next\n",
                     "abstract: |\n  Bounded result here.\ntitle: x\n"):
            assert "Bounded result" in mod.extract(body), body[:30]

    def test_a_separated_abstract_is_resolved_not_measured_as_empty(self) -> None:
        """An \\input abstract read as empty would report as within limits."""
        body = r"\begin{abstract}\input{abstract.tex}\end{abstract}"
        flat = mod.flatten(body, lambda t: "Bounded result here.")
        assert "Bounded result" in mod.extract(flat)

    def test_an_unlocatable_abstract_exits_two(self) -> None:
        import os, tempfile
        fd, path = tempfile.mkstemp(suffix=".tex")
        os.write(fd, b"\\documentclass{article}\\begin{document}No abstract.\\end{document}")
        os.close(fd)
        try:
            assert mod.main(["--manuscript", path]) == 2
        finally:
            os.unlink(path)

    def test_contract_states_the_abstract_limit(self) -> None:
        import re
        text = re.sub(r"\s+", " ", CONTRACT.read_text(encoding="utf-8").lower())
        assert "1920" in text
        assert "tighter" in text

    def test_pipeline_routes_the_checker(self) -> None:
        assert "verify_abstract_limits.py" in MANIFEST.read_text(encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
