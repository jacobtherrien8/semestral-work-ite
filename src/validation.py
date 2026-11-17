"""Validation of the user inputs.
"""

MIN_HEIGHT_CM = 100
MAX_HEIGHT_CM = 210

MIN_WEIGHT_KG = 20
MAX_WEIGHT_KG = 150

MIN_AGE = 10
MAX_AGE = 99

POSITIONS = ("forward", "defense")

STYLES = ("sniper", "playmaker", "power")

LENGTH_PREFERENCES = ("short", "normal", "long")

FLEX_PREFERENCES = ("soft", "normal", "stiff")


def validate_height(height_cm):
    """Check that the height is between 100 and 210 cm.

    Returns the height if valid, otherwise raises a ValueError.
    """
    if height_cm < MIN_HEIGHT_CM or height_cm > MAX_HEIGHT_CM:
        raise ValueError(
            f"Height of {height_cm} cm is outside the supported range.\n"
            f"Height must be between {MIN_HEIGHT_CM} and {MAX_HEIGHT_CM} cm."
        )
    return height_cm


def validate_weight(weight_kg):
    """Check that the weight is between 20 and 150 kg.

    Returns the weight if valid, otherwise raises a ValueError.
    """
    if weight_kg < MIN_WEIGHT_KG or weight_kg > MAX_WEIGHT_KG:
        raise ValueError(
            f"Weight of {weight_kg} kg is outside the supported range.\n"
            f"Weight must be between {MIN_WEIGHT_KG} and {MAX_WEIGHT_KG} kg."
        )
    return weight_kg


def validate_age(age):
    """Check that the age is between 10 and 99 years.

    Returns the age if valid, otherwise raises a ValueError.
    """
    if age < MIN_AGE or age > MAX_AGE:
        raise ValueError(
            f"Age of {age} years is outside the supported range.\n"
            f"Age must be between {MIN_AGE} and {MAX_AGE} years."
        )
    return age


def validate_choice(value, allowed, name):
    """Check that a text answer is one of the allowed options.

    Spaces and capital letters are ignored ("  Forward " -> "forward").
    Returns the cleaned answer if valid, otherwise raises a ValueError.
    """
    cleaned = value.strip().lower()
    if cleaned in allowed:
        return cleaned
    raise ValueError(f"{name} must be one of: {', '.join(allowed)}.")