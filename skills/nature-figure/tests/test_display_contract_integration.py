from __future__ import annotations

import unittest
from pathlib import Path


FIGURE = Path(__file__).parents[1]


class DisplayContractIntegrationTests(unittest.TestCase):
    def test_figure_router_loads_shared_display_decision_contract(self) -> None:
        manifest = (FIGURE / "manifest.yaml").read_text(encoding="utf-8")
        skill = (FIGURE / "SKILL.md").read_text(encoding="utf-8")
        contract = (FIGURE / "references" / "figure-contract.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("scientific-display-decision-contract.md", manifest)
        self.assertIn("resolve_scientific_display.py", manifest)
        self.assertIn("Scientific display decision contract", skill)
        self.assertIn("data snapshot", contract.lower())
        self.assertIn("analysis receipt", contract.lower())
        self.assertIn("render receipt", contract.lower())
        self.assertIn("allowed inference", contract.lower())
        self.assertIn("prohibited inference", contract.lower())


if __name__ == "__main__":
    unittest.main()
