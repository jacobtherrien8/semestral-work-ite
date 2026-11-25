"""
Stick flex calculation.

Return the recommended flex, a multiple of 5 between 30 and 150.
Stiff rounds up, soft rounds down, normal rounds to the nearest 5.
Raises a ValueError if the preference is unknown.
"""

import math

FLEX_FACTOR = 1.1  # half the body weight in lbs = weight in kg x 1.1
FLEX_STEP = 5
MIN_FLEX = 30
MAX_FLEX = 150


def compute_flex(weight_kg, preference):
    if preference not in ("soft", "normal", "stiff"):
        raise ValueError(
            f"Invalid flex preference: '{preference}'. "
            "Flex preference must be one of: soft, normal or stiff."
        )

    raw_flex = round(FLEX_FACTOR * weight_kg, 2)
    steps = raw_flex / FLEX_STEP

    if preference == "stiff":
        flex = math.ceil(steps) * FLEX_STEP     # Round up
    elif preference == "soft":
        flex = math.floor(steps) * FLEX_STEP    # Round down
    else:
        flex = math.floor(steps + 0.5) * FLEX_STEP

    if flex < MIN_FLEX:
        flex = MIN_FLEX
    if flex > MAX_FLEX:
        flex = MAX_FLEX
    return flex