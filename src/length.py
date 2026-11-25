"""Stick length calculation.
"""
import math

LENGTH_FACTOR = 0.81
CM_PER_INCH = 2.54


"""
Return the length adjustment in cm for a position and a preference.

Raises a ValueError if the position or the preference is unknown.
"""

def get_adjustment(position, preference):
    if position not in ("forward", "defense"):
        raise ValueError(
            f"Invalid position: '{position}'. "
            "Position must be one of: forward or defense."
        )
    if preference not in ("short", "normal", "long"):
        raise ValueError(
            f"Invalid preference: '{preference}'. "
            "Preference must be one of: short, normal or long."
        )

    if position == "forward":
        if preference == "short":
            return -0.5
        if preference == "normal":
            return 0
        return 1  # long

    # defense
    if preference == "short":
        return 0
    if preference == "normal":
        return 1
    return 2  # long


def compute_length(height_cm, position, preference):
    """Return the recommended stick length in whole cm.

    length = 0.81 x height + adjustment.
    Forwards round down (shorter stick, better puck control).
    Defensemen round up (longer stick, longer reach).
    """
    raw_length = LENGTH_FACTOR * height_cm + get_adjustment(position, preference)
    if position == "forward":
        return math.floor(raw_length)
    return math.ceil(raw_length)




"""
Convert a length from cm to inches, rounded to 0.1 inch.
"""
def cm_to_inches(length_cm):
    return round(length_cm / CM_PER_INCH, 1)