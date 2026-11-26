"""Tests for src/validation.py.

Testing strategy: boundary value testing.
For each numeric input (height, weight, age), the tests check:
    1. a normal value          -> must be accepted and returned unchanged
    2. the exact limits        -> must be accepted (limits are inclusive)
    3. one step outside limits -> must be rejected with a ValueError
For text choices, the tests check a valid option, a messy input
(extra spaces, capital letters) and an unknown option.

"""
import unittest

from src.validation import (
    POSITIONS,
    STYLES,
    validate_age,
    validate_choice,
    validate_height,
    validate_weight,
)


class TestValidateHeight(unittest.TestCase):
    """Tests for validate_height (allowed range: 100-210 cm)."""

    def test_valid_height(self):
        """Normal value.

        Input: 180 cm (inside the range).
        Expected outcome: the height is accepted and returned unchanged (180).
        """
        self.assertEqual(
            validate_height(180), 180,
            "A normal height of 180 cm should be accepted.",
        )

    def test_limits_are_accepted(self):
        """Exact limits.

        Input: 100 cm (minimum) and 210 cm (maximum).
        Expected outcome: both are accepted, because the limits are inclusive.
        This would catch a mistake like '<' written instead of '<='.
        """
        self.assertEqual(
            validate_height(100), 100,
            "The minimum height of 100 cm should be accepted.",
        )
        self.assertEqual(
            validate_height(210), 210,
            "The maximum height of 210 cm should be accepted.",
        )

    def test_out_of_range_is_rejected(self):
        """One step outside the limits.

        Input: 99 cm (just below) and 211 cm (just above).
        Expected outcome: both raise a ValueError.
        """
        with self.assertRaises(ValueError, msg="99 cm should be rejected."):
            validate_height(99)
        with self.assertRaises(ValueError, msg="211 cm should be rejected."):
            validate_height(211)


class TestValidateWeight(unittest.TestCase):
    """Tests for validate_weight (allowed range: 20-150 kg)."""

    def test_limits_are_accepted(self):
        """Exact limits.

        Input: 20 kg (minimum) and 150 kg (maximum).
        Expected outcome: both are accepted and returned unchanged.
        """
        self.assertEqual(
            validate_weight(20), 20,
            "The minimum weight of 20 kg should be accepted.",
        )
        self.assertEqual(
            validate_weight(150), 150,
            "The maximum weight of 150 kg should be accepted.",
        )

    def test_out_of_range_is_rejected(self):
        """One step outside the limits.

        Input: 19 kg (just below) and 151 kg (just above).
        Expected outcome: both raise a ValueError.
        """
        with self.assertRaises(ValueError, msg="19 kg should be rejected."):
            validate_weight(19)
        with self.assertRaises(ValueError, msg="151 kg should be rejected."):
            validate_weight(151)


class TestValidateAge(unittest.TestCase):
    """Tests for validate_age (allowed range: 10-99 years)."""

    def test_minimum_age_is_accepted(self):
        """Exact minimum.

        Input: 10 years (the minimum age requirement).
        Expected outcome: the age is accepted and returned unchanged.
        """
        self.assertEqual(
            validate_age(10), 10,
            "A 10-year-old player should be accepted.",
        )

    def test_too_young_is_rejected(self):
        """One step below the minimum.

        Input: 9 years.
        Expected outcome: a ValueError is raised (player too young).
        """
        with self.assertRaises(ValueError, msg="A 9-year-old should be rejected."):
            validate_age(9)


class TestValidateChoice(unittest.TestCase):
    """Tests for validate_choice (text answers: position, style, preferences)."""

    def test_valid_choice(self):
        """Valid option.

        Input: "forward" with the allowed positions (forward, defense).
        Expected outcome: accepted and returned as "forward".
        """
        self.assertEqual(
            validate_choice("forward", POSITIONS, "Position"), "forward",
            "'forward' is a valid position and should be accepted.",
        )

    def test_input_is_cleaned(self):
        """Messy input.

        Input: "  Sniper " (extra spaces and a capital letter).
        Expected outcome: cleaned and accepted as "sniper".
        """
        self.assertEqual(
            validate_choice("  Sniper ", STYLES, "Style"), "sniper",
            "Spaces and capital letters should be ignored.",
        )

    def test_invalid_choice_is_rejected(self):
        """Unknown option.

        Input: "goalie" (not in the allowed positions).
        Expected outcome: a ValueError is raised.
        """
        with self.assertRaises(ValueError, msg="'goalie' should be rejected."):
            validate_choice("goalie", POSITIONS, "Position")


if __name__ == "__main__":
    unittest.main()