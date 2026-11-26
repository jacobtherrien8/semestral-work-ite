"""Tests for src/converter.py.

Testing strategy:
    1. a known conversion        -> 1 lb must give exactly 0.453592 kg
    2. a realistic player weight -> 176 lbs must give about 79.83 kg
    3. a weight already in kg    -> must be returned unchanged
    4. zero                      -> 0 lbs must give 0 kg
Decimal results are compared with assertAlmostEqual, because computers
store decimals with tiny rounding errors (for example 79.83219199999999).

"""
import unittest

from src.converter import LBS_TO_KG, convert_lbs_to_kg


class TestConvertLbsToKg(unittest.TestCase):
    """Tests for convert_lbs_to_kg."""

    def test_one_pound(self):
        """Known conversion.

        Input: 1 lbs.
        Expected outcome: exactly the conversion factor, 0.453592 kg.
        """
        self.assertAlmostEqual(
            convert_lbs_to_kg(1, "lbs"), LBS_TO_KG,
            msg="1 lb should be equal to 0.453592 kg.",
        )

    def test_realistic_weight_in_lbs(self):
        """Realistic player weight.

        Input: 176 lbs.
        Expected outcome: 176 x 0.453592 = 79.832192 kg.
        """
        self.assertAlmostEqual(
            convert_lbs_to_kg(176, "lbs"), 79.832192,
            msg="176 lbs should be about 79.83 kg.",
        )

    def test_weight_in_kg_is_unchanged(self):
        """Weight already in kg.

        Input: 80 with the unit "kg".
        Expected outcome: no conversion, 80 is returned unchanged.
        """
        self.assertEqual(
            convert_lbs_to_kg(80, "kg"), 80,
            "A weight in kg should not be converted.",
        )

    def test_zero(self):
        """Zero.

        Input: 0 lbs.
        Expected outcome: 0 kg.
        """
        self.assertEqual(
            convert_lbs_to_kg(0, "lbs"), 0,
            "0 lbs should be 0 kg.",
        )


if __name__ == "__main__":
    unittest.main()