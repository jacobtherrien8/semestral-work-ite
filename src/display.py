"""Display of the stick recommendation.

Author: Jacob Therrien
"""


def show_recommendation(stick):
    """Print the recommended stick in a readable format.

    Args:
        stick (dict): The recommendation returned by recommend_stick(),
            with the keys length_cm, length_in, flex, kick_point and curve.
    """
    print()
    print("=== Recommended hockey stick ===")
    print(f"Length     : {stick['length_cm']} cm ({stick['length_in']} in)")
    print(f"Flex       : {stick['flex']}")
    print(f"Kick point : {stick['kick_point']}")
    print(f"Curve      : {stick['curve']}")