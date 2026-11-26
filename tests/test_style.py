"""Tests for src/style.py.

Testing strategy:
    1. every valid style   -> must give the kick point / curve from the
                              specification (sniper, playmaker, power)
    2. an unknown style    -> must raise a ValueError (no silent wrong answer)
All 3 styles are tested because the list is short: this covers every
possible valid input of the functions.

"""
import unittest

from src.style import choose_curve, choose_kick_point


class TestChooseKickPoint(unittest.TestCase):
    """Tests for choose_kick_point (sniper -> low, playmaker -> mid, power -> high)."""

    def test_each_style(self):
        """Every valid style.

        Input: "sniper", "playmaker" and "power".
        Expected outcome: "low", "mid" and "high", as in the specification.
        """
        self.assertEqual(
            choose_kick_point("sniper"), "low",
            "A sniper should get a low kick point (quick release).",
        )
        self.assertEqual(
            choose_kick_point("playmaker"), "mid",
            "A playmaker should get a mid kick point.",
        )
        self.assertEqual(
            choose_kick_point("power"), "high",
            "A power player should get a high kick point (slapshots).",
        )

    def test_unknown_style_is_rejected(self):
        """Unknown style.

        Input: "snipper" (typo).
        Expected outcome: a ValueError is raised instead of a wrong answer.
        """
        with self.assertRaises(ValueError, msg="'snipper' should be rejected."):
            choose_kick_point("snipper")


class TestChooseCurve(unittest.TestCase):
    """Tests for choose_curve (sniper -> toe, playmaker -> mid, power -> heel)."""

    def test_each_style(self):
        """Every valid style.

        Input: "sniper", "playmaker" and "power".
        Expected outcome: "toe", "mid" and "heel", as in the specification.
        """
        self.assertEqual(
            choose_curve("sniper"), "toe",
            "A sniper should get a toe curve.",
        )
        self.assertEqual(
            choose_curve("playmaker"), "mid",
            "A playmaker should get a mid curve.",
        )
        self.assertEqual(
            choose_curve("power"), "heel",
            "A power player should get a heel curve.",
        )

    def test_unknown_style_is_rejected(self):
        """Unknown style.

        Input: "goalie" (not a playing style of the program).
        Expected outcome: a ValueError is raised instead of a wrong answer.
        """
        with self.assertRaises(ValueError, msg="'goalie' should be rejected."):
            choose_curve("goalie")


if __name__ == "__main__":
    unittest.main()