"""Tests for src/flex.py.

Testing strategy:
    1. the 3 rounding rules -> stiff rounds UP, soft rounds DOWN,
                               normal rounds to the NEAREST multiple of 5
    2. special cases        -> a value exactly halfway (82.5), and the
                               decimal trap 1.1 x 50 = 55.00000000000001
    3. the limits           -> the flex never goes below 30 or above 150
    4. an unknown preference raises a ValueError
Expected values are calculated by hand with: raw flex = 1.1 x weight (kg).

Author: Jacob Therrien
"""
import unittest

from src.flex import compute_flex


class TestRoundingRules(unittest.TestCase):
    """Tests for the 3 rounding rules of compute_flex."""

    def test_stiff_rounds_up(self):
        """Stiff preference.

        Input: 80 kg, stiff.
        Calculation: 1.1 x 80 = 88 -> rounded UP to a multiple of 5.
        Expected outcome: 90.
        """
        self.assertEqual(compute_flex(80, "stiff"), 90,
                         "88 should be rounded up to 90 for a stiff flex.")

    def test_soft_rounds_down(self):
        """Soft preference.

        Input: 80 kg, soft.
        Calculation: 1.1 x 80 = 88 -> rounded DOWN to a multiple of 5.
        Expected outcome: 85.
        """
        self.assertEqual(compute_flex(80, "soft"), 85,
                         "88 should be rounded down to 85 for a soft flex.")

    def test_normal_rounds_to_nearest(self):
        """Normal preference, in both directions.

        Input 1: 80 kg -> 88.0 -> nearest multiple of 5 -> 90 (rounds up).
        Input 2: 78 kg -> 85.8 -> nearest multiple of 5 -> 85 (rounds down).
        Expected outcome: 90 and 85.
        """
        self.assertEqual(compute_flex(80, "normal"), 90,
                         "88 should be rounded to the nearest 5, which is 90.")
        self.assertEqual(compute_flex(78, "normal"), 85,
                         "85.8 should be rounded to the nearest 5, which is 85.")


class TestSpecialCases(unittest.TestCase):
    """Tests for the tricky values of compute_flex."""

    def test_exactly_halfway_rounds_up(self):
        """Value exactly between two multiples of 5.

        Input: 75 kg, normal.
        Calculation: 1.1 x 75 = 82.5 -> halfway between 80 and 85 -> rounds UP.
        Expected outcome: 85.
        Python's round(16.5) would give 16 (-> 80), which is why
        flex.py uses math.floor(x + 0.5) instead.
        """
        self.assertEqual(compute_flex(75, "normal"), 85,
                         "82.5 is halfway and should be rounded up to 85.")

    def test_decimal_trap(self):
        """Decimal error of the computer.

        Input: 50 kg, stiff.
        Calculation: 1.1 x 50 gives 55.00000000000001 in Python, not 55.
        Without round(..., 2) in flex.py, rounding up would give 60.
        Expected outcome: 55.
        """
        self.assertEqual(compute_flex(50, "stiff"), 55,
                         "1.1 x 50 should be treated as exactly 55.")


class TestLimits(unittest.TestCase):
    """Tests for the minimum (30) and maximum (150) flex."""

    def test_minimum_flex(self):
        """Very light player.

        Input: 20 kg, soft.
        Calculation: 1.1 x 20 = 22 -> down -> 20 -> raised to the minimum.
        Expected outcome: 30.
        """
        self.assertEqual(compute_flex(20, "soft"), 30,
                         "The flex should never be below 30.")

    def test_maximum_flex(self):
        """Very heavy player.

        Input: 150 kg, stiff.
        Calculation: 1.1 x 150 = 165 -> up -> 165 -> lowered to the maximum.
        Expected outcome: 150.
        """
        self.assertEqual(compute_flex(150, "stiff"), 150,
                         "The flex should never be above 150.")


class TestInvalidPreference(unittest.TestCase):
    """Tests for an unknown flex preference."""

    def test_unknown_preference_is_rejected(self):
        """Unknown preference.

        Input: 80 kg, "hard".
        Expected outcome: a ValueError is raised.
        """
        with self.assertRaises(ValueError, msg="'hard' should be rejected."):
            compute_flex(80, "hard")


if __name__ == "__main__":
    unittest.main()