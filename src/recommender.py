"""
Combine all the calculations into one stick recommendation.

Build the full stick recommendation for a player.
"""

from src.flex import compute_flex
from src.length import cm_to_inches, compute_length
from src.style import choose_curve, choose_kick_point

def recommend_stick(player):
    length_cm = compute_length(
        player["height_cm"], player["position"], player["length_preference"]
    )
    length_in = cm_to_inches(length_cm)
    flex = compute_flex(player["weight_kg"], player["flex_preference"])
    kick_point = choose_kick_point(player["style"])
    curve = choose_curve(player["style"])

  
    # Dictionnary with output of the recommended stick
    return {
        "length_cm": length_cm,
        "length_in": length_in,
        "flex": flex,
        "kick_point": kick_point,
        "curve": curve,
    }