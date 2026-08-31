from __future__ import annotations

import itertools
import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
CONTRACT = SHARED / "core" / "atomic-claim-verification.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def gf2_rank(vectors: tuple[int, ...], dimension: int) -> int:
    rows = list(vectors)
    rank = 0
    for bit in reversed(range(dimension)):
        pivot = next((i for i in range(rank, len(rows)) if rows[i] & (1 << bit)), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i] & (1 << bit):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def is_zero_sum_free_binary_subsequence(word: tuple[int, ...]) -> bool:
    for size in range(1, len(word) + 1):
        for subsequence in itertools.combinations(word, size):
            total = 0
            for value in subsequence:
                total ^= value
            if total == 0:
                return False
    return True


def is_zero_sum_free_binary_contiguous(word: tuple[int, ...]) -> bool:
    for start in range(len(word)):
        total = 0
        for value in word[start:]:
            total ^= value
            if total == 0:
                return False
    return True


def brute_binary_zsf(alphabet: tuple[int, ...]) -> int:
    # In F_2, a zero-sum-free word cannot repeat a letter, so enumerating
    # subsets of the alphabet is a complete bounded oracle.
    return max(
        (
            len(word)
            for size in range(len(alphabet) + 1)
            for word in itertools.combinations(alphabet, size)
            if is_zero_sum_free_binary_subsequence(word)
        ),
        default=0,
    )


def is_zero_sum_free_mod(word: tuple[int, ...], modulus: int) -> bool:
    for size in range(1, len(word) + 1):
        for subsequence in itertools.combinations(word, size):
            if sum(subsequence) % modulus == 0:
                return False
    return True


class AtomicClaimVerificationTests(unittest.TestCase):
    def test_contract_is_fail_closed_and_checks_entailment(self) -> None:
        contract = read(CONTRACT)
        normalized_contract = " ".join(contract.split())
        for marker in (
            "exact_atomic_proposition",
            "qualifiers_and_scope",
            "support_or_entailment_status",
            "SUPPORTED_INTERNAL + UNRESOLVED",
            "UNRESOLVED",
            "CONTRADICTED",
            "BLOCKED",
            "A pointer is not verification",
            "definition -> theorem -> corollary -> specialization",
            "upper- and lower-bound locators",
            "Independent coverage pass",
        ):
            self.assertIn(marker, contract)
        self.assertIn("not necessarily a contiguous factor", normalized_contract)

    def test_formal_semantics_and_non_derivability_require_real_proof_obligations(
        self,
    ) -> None:
        contract = " ".join(read(CONTRACT).lower().split())
        for marker in (
            "name, symbol, terminal state, or type signature alone",
            "admissible inputs",
            "output or conclusion semantics",
            "side conditions",
            "non-derivability",
            "terminal normal form",
            "upper witness",
            "all shorter derivations",
            "soundness and completeness",
        ):
            self.assertIn(marker, contract)

    def test_stale_unresolved_findings_require_explicit_status_transition(self) -> None:
        contract = " ".join(read(CONTRACT).lower().split())
        for marker in (
            "epistemic-status transition",
            "already-frozen evidence",
            "explicit correction or supersession record",
            "preserve the original finding",
            "every current-authority surface",
            "not optional new science",
        ):
            self.assertIn(marker, contract)

    def test_contiguous_factor_and_subsequence_invariants_are_not_conflated(self) -> None:
        e1, e2 = 0b01, 0b10
        word = (e1, e2, e1)
        self.assertTrue(is_zero_sum_free_binary_contiguous(word))
        self.assertFalse(is_zero_sum_free_binary_subsequence(word))

    def test_binary_alphabet_refinement_claim_is_contradicted(self) -> None:
        for dimension in range(1, 4):
            universe = tuple(range(1 << dimension))
            for size in range(len(universe) + 1):
                for alphabet in itertools.combinations(universe, size):
                    self.assertEqual(
                        brute_binary_zsf(alphabet),
                        gf2_rank(alphabet, dimension),
                        (dimension, alphabet),
                    )

    def test_nonbinary_alphabet_sensitivity_remains_possible(self) -> None:
        alphabet = (2, 3)
        maximum = 0
        for length in range(1, 6):
            if any(
                is_zero_sum_free_mod(word, 6)
                for word in itertools.product(alphabet, repeat=length)
            ):
                maximum = length
        self.assertEqual(maximum, 3)
        self.assertLess(maximum, 5)  # D(Z_6) - 1

    def test_contract_is_routed_through_manuscript_changing_workflows(self) -> None:
        routed = (
            SHARED / "manifest.yaml",
            SKILLS / "academic-writing" / "manifest.yaml",
            SKILLS / "academic-paper-pipeline" / "manifest.yaml",
            SKILLS / "nature-writing" / "manifest.yaml",
            SKILLS / "nature-reviewer" / "manifest.yaml",
            SKILLS / "nature-polishing" / "manifest.yaml",
            SKILLS / "nature-response" / "manifest.yaml",
        )
        for path in routed:
            self.assertIn("atomic-claim-verification.md", read(path), str(path))

    def test_pipeline_readiness_requires_zero_fail_closed_assertions(self) -> None:
        for path in (
            SHARED / "core" / "academic-paper-iteration-pipeline.md",
            SKILLS / "academic-paper-pipeline" / "SKILL.md",
        ):
            text = read(path)
            for marker in ("SUPPORTED_INTERNAL", "UNRESOLVED", "CONTRADICTED", "BLOCKED"):
                self.assertIn(marker, text, str(path))
            self.assertIn("atomic", text.lower(), str(path))

    def test_abstract_contracts_are_target_aware_and_self_contained(self) -> None:
        for path in (
            SKILLS / "nature-writing" / "static" / "fragments" / "section" / "abstract.md",
            SKILLS / "nature-polishing" / "static" / "fragments" / "section" / "abstract.md",
        ):
            text = read(path).lower()
            for marker in ("exact target", "self-contained", "inline", "display equation", "internal"):
                self.assertIn(marker, text, str(path))


if __name__ == "__main__":
    unittest.main()
