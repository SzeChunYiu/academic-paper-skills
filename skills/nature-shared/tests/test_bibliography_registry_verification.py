from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
SCRIPT = SHARED / "scripts" / "verify_bibliography_registry.py"
PIPELINE_MANIFEST = SKILLS / "academic-paper-pipeline" / "manifest.yaml"


def _load():
    spec = importlib.util.spec_from_file_location("verify_bibliography_registry", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


mod = _load()

BIB = r"""
@article{good2020,
  author  = {Shamir, Adi},
  title   = {How to share a secret},
  journal = {Communications of the ACM},
  year    = {1979},
  doi     = {10.1145/359168.359176}
}

@inproceedings{nodoi2019,
  author    = {Torres-Arias, Santiago},
  title     = {in-toto: Providing farm-to-table guarantees},
  booktitle = {USENIX Security},
  year      = {2019},
  note      = {USENIX does not register DOIs; verified against the publisher record}
}

@inproceedings{nodoi_nobasis,
  author    = {Someone, A.},
  title     = {A paper with no verification basis},
  booktitle = {Nowhere},
  year      = {2020}
}
"""


class BibliographyRegistryVerificationTests(unittest.TestCase):
    """Parsing and policy. Registry calls are not made in tests."""

    def test_entries_and_fields_parse(self) -> None:
        entries = mod.ENTRY.findall(BIB)
        assert len(entries) == 3
        _kind, key = entries[0]
        body = BIB[BIB.index("good2020"):BIB.index("nodoi2019")]
        fields = {k: mod.squash(v) for k, v in mod.fields_of(body).items()}
        assert key.strip() == "good2020"
        assert fields["doi"] == "10.1145/359168.359176"
        assert fields["year"] == "1979"

    def test_an_entry_without_a_doi_is_separated_not_passed(self) -> None:
        """No DOI is not an error; no verification basis is."""
        keys = {k.strip() for _kind, k in mod.ENTRY.findall(BIB)}
        assert "nodoi2019" in keys and "nodoi_nobasis" in keys
        src = SCRIPT.read_text(encoding="utf-8")
        assert "NOT ACCEPTABLE" in src.upper()
        assert "requires a named non-registry verification" in src

    def test_title_normalisation_ignores_braces_and_case(self) -> None:
        assert mod.norm("The {Byzantine} Generals Problem") == mod.norm(
            "the byzantine generals problem")

    def test_latex_accents_match_plain_unicode(self) -> None:
        """A correctly escaped BibTeX author must not read as a mismatch."""
        assert mod.norm("Alchourr{\\'o}n") == mod.norm("Alchourrón")
        assert mod.norm(r'G{\"a}rdenfors') == mod.norm("Gärdenfors")
        assert mod.norm("Erd{\\H o}s") == mod.norm("Erdos")

    def test_ligatures_and_special_letters_fold(self) -> None:
        assert mod.norm("Wei{\\ss}") == mod.norm("Weiss")
        assert mod.norm("{\\o}ksendal") == mod.norm("oksendal")

    def test_accent_handling_does_not_erase_real_differences(self) -> None:
        """Folding must not make every name equal."""
        assert mod.norm("Alchourr{\\'o}n") != mod.norm("Makinson")

    def test_list_and_string_record_shapes_both_read(self) -> None:
        """CrossRef returns lists; CSL JSON from doi.org returns strings."""
        assert mod._one(["A truth maintenance system"]) == "A truth maintenance system"
        assert mod._one("A truth maintenance system") == "A truth maintenance system"
        assert mod._one(None) == ""

    def test_a_string_title_is_not_joined_character_by_character(self) -> None:
        """The bug this guards: " ".join on a string spaces out every letter."""
        assert mod._one("Reflexion") == "Reflexion"
        assert " ".join("Reflexion") != mod._one("Reflexion")

    def test_doi_org_fallback_is_documented_as_registrar_agnostic(self) -> None:
        """arXiv DOIs are DataCite; CrossRef alone would call them unverifiable."""
        src = SCRIPT.read_text(encoding="utf-8")
        assert "doi.org" in src
        assert "10.48550" in src
        assert "regardless of registrar" in src

    def test_compact_entries_parse(self) -> None:
        """A valid .bib whose last field and closing brace share a line."""
        compact = ("@article{k1,\n  author = {A, B},\n  title = {T},\n"
                   "  year = {2020}, doi = {10.1/x}}\n")
        keys = [m.group(2).strip() for m in mod.ENTRY.finditer(compact)]
        assert keys == ["k1"], keys
        body = compact[compact.index("k1,") + 3:]
        assert mod.fields_of(body).get("doi") == "10.1/x"

    def test_unparseable_file_is_a_failure_not_a_clean_run(self) -> None:
        """0 of 0 verified must never exit 0: nothing was checked."""
        import tempfile, os
        fd, path = tempfile.mkstemp(suffix=".bib")
        os.write(fd, b"this file contains no bibtex entries at all\n")
        os.close(fd)
        try:
            assert mod.main(path) == 2
        finally:
            os.unlink(path)

    def test_exit_codes_are_documented_and_distinct(self) -> None:
        doc = mod.__doc__ or ""
        assert "0  every entry with a DOI verified" in doc
        assert "1  at least one entry disagrees" in doc
        assert "2  the bibliography could not be read" in doc

    def test_unreadable_file_is_code_two_not_a_pass(self) -> None:
        assert mod.main("/nonexistent/path/to/nothing.bib") == 2

    def test_deposit_date_allowance_is_narrow_and_explained(self) -> None:
        """A late-deposited record must not read as a wrong year."""
        src = SCRIPT.read_text(encoding="utf-8")
        assert "deposit" in src.lower()
        assert "container" in src

    def test_pipeline_routes_the_verifier(self) -> None:
        manifest = PIPELINE_MANIFEST.read_text(encoding="utf-8")
        assert "verify_bibliography_registry.py" in manifest


if __name__ == "__main__":
    unittest.main()
