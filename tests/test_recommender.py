"""Tests for src/recommender.py.

Testing strategy: integration testing.
recommend_stick() combines length.py, flex.py and style.py, so these tests
check complete player profiles from input to final recommendation:
    1. typical players     -> the full recommendation matches the values
                              calculated by hand from the specification
    2. a weight in lbs     -> converter.py + recommender.py work together
    3. the result format   -> exactly the 5 keys expected by display.py
    4. invalid data        -> an error from a sub-module is not hidden
Each sub-module is already tested alone in its own test file.

Author: Jacob Therrien
"""
import unittest

from src.converter import convert_lbs_to_kg
from src.recommender import recommend_stick


class TestFullRecommendation(unittest.TestCase):
    """Complete player profiles, from player data to stick."""

    def test_forward_sniper(self):
        """Typical forward.

        Input: 180 cm, 80 kg, forward, sniper, normal length, normal flex.
        Calculation:
            length = 0.81 x 180 + 0 = 145.8 -> down -> 145 cm (57.1 in)
            flex   = 1.1 x 80 = 88 -> nearest 5 -> 90
            sniper -> kick point low, curve toe
        Expected outcome: 145 cm, 57.1 in, flex 90, low, toe.
        """
        player = {
            "height_cm": 180,
            "weight_kg": 80,
            "position": "forward",
            "style": "sniper",
            "length_preference": "normal",
            "flex_preference": "normal",
        }
        expected = {
            "length_cm": 145,
            "length_in": 57.1,
            "flex": 90,
            "kick_point": "low",
            "curve": "toe",
        }
        self.assertEqual(recommend_stick(player), expected,
                         "Wrong recommendation for a typical forward sniper.")

    def test_defense_power(self):
        """Typical defenseman.

        Input: 180 cm, 80 kg, defense, power, long length, stiff flex.
        Calculation:
            length = 0.81 x 180 + 2 = 147.8 -> up -> 148 cm (58.3 in)
            flex   = 1.1 x 80 = 88 -> up -> 90
            power  -> kick point high, curve heel
        Expected outcome: 148 cm, 58.3 in, flex 90, high, heel.
        """
        player = {
            "height_cm": 180,
            "weight_kg": 80,
            "position": "defense",
            "style": "power",
            "length_preference": "long",
            "flex_preference": "stiff",
        }
        expected = {
            "length_cm": 148,
            "length_in": 58.3,
            "flex": 90,
            "kick_point": "high",
            "curve": "heel",
        }
        self.assertEqual(recommend_stick(player), expected,
                         "Wrong recommendation for a typical defense power player.")

    def test_young_player(self):
        """Young, light player.

        Input: 150 cm, 45 kg, forward, playmaker, short length, soft flex.
        Calculation:
            length = 0.81 x 150 - 0.5 = 121.0 -> down -> 121 cm (47.6 in)
            flex   = 1.1 x 45 = 49.5 -> down -> 45
            playmaker -> kick point mid, curve mid
        Expected outcome: 121 cm, 47.6 in, flex 45, mid, mid.
        """
        player = {
            "height_cm": 150,
            "weight_kg": 45,
            "position": "forward",
            "style": "playmaker",
            "length_preference": "short",
            "flex_preference": "soft",
        }
        expected = {
            "length_cm": 121,
            "length_in": 47.6,
            "flex": 45,
            "kick_point": "mid",
            "curve": "mid",
        }
        self.assertEqual(recommend_stick(player), expected,
                         "Wrong recommendation for a young player.")


class TestWeightInPounds(unittest.TestCase):
    """converter.py and recommender.py working together."""

    def test_player_weight_in_lbs(self):
        """Player who gives his weight in lbs.

        Input: 190 cm, 200 lbs, defense, sniper, normal length, normal flex.
        Calculation:
            weight = 200 x 0.453592 = 90.72 kg
            length = 0.81 x 190 + 1 = 154.9 -> up -> 155 cm (61.0 in)
            flex   = 1.1 x 90.72 = 99.79 -> nearest 5 -> 100
            sniper -> kick point low, curve toe
        Expected outcome: 155 cm, 61.0 in, flex 100, low, toe.
        """
        player = {
            "height_cm": 190,
            "weight_kg": convert_lbs_to_kg(200, "lbs"),
            "position": "defense",
            "style": "sniper",
            "length_preference": "normal",
            "flex_preference": "normal",
        }
        expected = {
            "length_cm": 155,
            "length_in": 61.0,
            "flex": 100,
            "kick_point": "low",
            "curve": "toe",
        }
        self.assertEqual(recommend_stick(player), expected,
                         "Wrong recommendation for a weight given in lbs.")


class TestResultFormat(unittest.TestCase):
    """The recommendation has the format expected by display.py."""

    def test_result_has_the_5_expected_keys(self):
        """Keys of the result.

        Input: any valid player.
        Expected outcome: exactly the keys length_cm, length_in, flex,
        kick_point and curve (display.py needs all of them).
        """
        player = {
            "height_cm": 170,
            "weight_kg": 70,
            "position": "forward",
            "style": "power",
            "length_preference": "normal",
            "flex_preference": "normal",
        }
        result = recommend_stick(player)
        self.assertEqual(
            set(result.keys()),
            {"length_cm", "length_in", "flex", "kick_point", "curve"},
            "The recommendation should contain exactly the 5 expected keys.",
        )


class TestInvalidData(unittest.TestCase):
    """Errors from the sub-modules are not hidden by recommender.py."""

    def test_unknown_style_is_rejected(self):
        """Invalid style reaching the recommender.

        Input: a valid player but with the style "goalie".
        Expected outcome: the ValueError from style.py goes through.
        """
        player = {
            "height_cm": 180,
            "weight_kg": 80,
            "position": "forward",
            "style": "goalie",
            "length_preference": "normal",
            "flex_preference": "normal",
        }
        with self.assertRaises(ValueError, msg="'goalie' should be rejected."):
            recommend_stick(player)


if __name__ == "__main__":
    unittest.main()