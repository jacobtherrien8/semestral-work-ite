"""
Kick point and curve recommendation based on the playing style.



Return the kick point for a playing style.

Raises a ValueError if the style is unknown.
"""

def choose_kick_point(style):
    if style == "sniper":
        return "low"
    if style == "playmaker":
        return "mid"
    if style == "power":
        return "high"
    raise ValueError(
        f"Invalid style: '{style}'. Style must be one of: sniper, playmaker or power."
    )



"""
Return the blade curve for a playing style.

Raises a ValueError if the style is unknown.
"""

def choose_curve(style):
    if style == "sniper":
        return "toe"
    if style == "playmaker":
        return "mid"
    if style == "power":
        return "heel"
    raise ValueError(
        f"Invalid style: '{style}'. Style must be one of: sniper, playmaker or power."
    )