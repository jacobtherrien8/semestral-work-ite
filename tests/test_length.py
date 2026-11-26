"""Tests for src/length.py.

Testing strategy:
    1. get_adjustment -> every combination of position and preference
                         (2 x 3 = 6 cases) gives the value of the specification,
                         and unknown values raise a ValueError
    2. compute_length -> the rounding rule depends on the position:
                         forwards round DOWN, defensemen round UP
    3. cm_to_inches   -> known conversions, rounded to 0.1 inch
Expected values are calculated by hand with: length = 0.81 x height + adjustment.

Author: Jacob Therrien
"""
import unittest

from src.length import cm_to_inches, compute_length, get_adjustment


class TestGetAdjustment(unittest.TestCase):
    """Tests for get_adjustment (length adjustment in cm)."""

    def test_forward_adjustments(self):
        """Every preference for a forward.

        Input: forward + short, normal, long.
        Expected outcome: -0.5, 0 and +1 cm, as in the specification.
        """
        self.assertEqual(get_adjustment("forward", "short"), -0.5,
                         "Forward + short should give -0.5 cm.")
        self.assertEqual(get_adjustment("forward", "normal"), 0,
                         "Forward + normal should give 0 cm.")
        self.assertEqual(get_adjustment("forward", "long"), 1,
                         "Forward + long should give +1 cm.")

    def test_defense_adjustments(self):
        """Every preference for a defenseman.

        Input: defense + short, normal, long.
        Expected outcome: 0, +1 and +2 cm, as in the specification.
        """
        self.assertEqual(get_adjustment("defense", "short"), 0,
                         "Defense + short should give 0 cm.")
        self.assertEqual(get_adjustment("defense", "normal"), 1,
                         "Defense + normal should give +1 cm.")
        self.assertEqual(get_adjustment("defense", "long"), 2,
                         "Defense + long should give +2 cm.")

    def test_unknown_position_is_rejected(self):
        """Unknown position.

        Input: "goalie" + normal.
        Expected outcome: a ValueError is raised.
        """
        with self.assertRaises(ValueError, msg="'goalie' should be rejected."):
            get_adjustment("goalie", "normal")

    def test_unknown_preference_is_rejected(self):
        """Unknown preference.

        Input: forward + "medium".
        Expected outcome: a ValueError is raised.
        """
        with self.assertRaises(ValueError, msg="'medium' should be rejected."):
            get_adjustment("forward", "medium")


class TestComputeLength(unittest.TestCase):
    """Tests for compute_length (length in whole cm)."""

    def test_forward_rounds_down(self):
        """Rounding rule for a forward.

        Input: 180 cm, forward, normal.
        Calculation: 0.81 x 180 + 0 = 145.8 -> rounded DOWN.
        Expected outcome: 145 cm.
        """
        self.assertEqual(compute_length(180, "forward", "normal"), 145,
                         "145.8 should be rounded down to 145 for a forward.")

    def test_defense_rounds_up(self):
        """Rounding rule for a defenseman.

        Input: 180 cm, defense, normal.
        Calculation: 0.81 x 180 + 1 = 146.8 -> rounded UP.
        Expected outcome: 147 cm.
        """
        self.assertEqual(compute_length(180, "defense", "normal"), 147,
                         "146.8 should be rounded up to 147 for a defenseman.")

    def test_long_preference(self):
        """Long stick preference, for both positions.

        Input 1: 180 cm, defense, long -> 0.81 x 180 + 2 = 147.8 -> up -> 148.
        Input 2: 175 cm, forward, long -> 0.81 x 175 + 1 = 142.75 -> down -> 142.
        Expected outcome: 148 cm and 142 cm.
        """
        self.assertEqual(compute_length(180, "defense", "long"), 148,
                         "Defense + long at 180 cm should give 148 cm.")
        self.assertEqual(compute_length(175, "forward", "long"), 142,
                         "Forward + long at 175 cm should give 142 cm.")


class TestCmToInches(unittest.TestCase):
    """Tests for cm_to_inches (1 inch = 2.54 cm)."""

    def test_known_conversions(self):
        """Known conversions.

        Input: 145 cm and 148 cm.
        Calculation: 145 / 2.54 = 57.09 -> 57.1 ; 148 / 2.54 = 58.27 -> 58.3.
        Expected outcome: 57.1 and 58.3 inches.
        """
        self.assertEqual(cm_to_inches(145), 57.1,
                         "145 cm should be 57.1 inches.")
        self.assertEqual(cm_to_inches(148), 58.3,
                         "148 cm should be 58.3 inches.")


if __name__ == "__main__":
    unittest.main()


    