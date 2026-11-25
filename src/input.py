"""
Ask the user for their information, repeating each question until valid.

"""
from src.converter import convert_lbs_to_kg
from src.validation import (
    FLEX_PREFERENCES,
    LENGTH_PREFERENCES,
    POSITIONS,
    STYLES,
    validate_age,
    validate_choice,
    validate_height,
    validate_weight,
)


def read_number(question):
    """Ask a question until the user types a number.

    Args:
        question (str): Text shown to the user.

    Returns:
        float: The number typed.
    """
    while True:
        answer = input(question)
        try:
            return float(answer)
        except ValueError:
            print("Please enter a number, for example 180.")


def ask_age():
    """Ask the age until it is valid (10-99 years).

    Returns:
        int: The validated age.
    """
    while True:
        age = int(read_number("Age: "))
        try:
            return validate_age(age)
        except ValueError as error:
            print(error)


def ask_height():
    """Ask the height until it is valid (100-210 cm).

    Returns:
        float: The validated height in cm.
    """
    while True:
        height = read_number("Height (cm): ")
        try:
            return validate_height(height)
        except ValueError as error:
            print(error)


def ask_unit():
    """Ask the weight unit until the answer is 1 (kg) or 2 (lbs).

    Returns:
        str: "kg" or "lbs".
    """
    while True:
        answer = input("Weight unit? 1 = kg, 2 = lbs: ").strip()
        if answer == "1":
            return "kg"
        if answer == "2":
            return "lbs"
        print("Please type 1 for kg or 2 for lbs.")


def ask_weight_kg():
    """Ask the unit, then the weight, and return it validated in kg.

    Returns:
        float: The validated weight in kg.
    """
    unit = ask_unit()
    while True:
        weight = read_number(f"Weight ({unit}): ")
        weight_kg = convert_lbs_to_kg(weight, unit)
        try:
            return validate_weight(weight_kg)
        except ValueError as error:
            print(error)


def ask_choice(question, allowed, name):
    """Ask a question until the answer is one of the allowed options.

    Args:
        question (str): Text shown to the user.
        allowed (tuple): Accepted answers.
        name (str): Name of the input, used in the error message.

    Returns:
        str: The cleaned, valid answer.
    """
    while True:
        answer = input(question)
        try:
            return validate_choice(answer, allowed, name)
        except ValueError as error:
            print(error)


def ask_player_info():
    """Ask all the questions and return the player's data.

    Returns:
        dict: The validated answers, with the keys used by recommend_stick().
    """
    return {
        "age": ask_age(),
        "height_cm": ask_height(),
        "weight_kg": ask_weight_kg(),
        "position": ask_choice(
            "Position (forward/defense): ", POSITIONS, "Position"),
        "style": ask_choice(
            "Style (sniper/playmaker/power): ", STYLES, "Style"),
        "length_preference": ask_choice(
            "Stick length (short/normal/long): ", LENGTH_PREFERENCES, "Length preference"),
        "flex_preference": ask_choice(
            "Flex (soft/normal/stiff): ", FLEX_PREFERENCES, "Flex preference"),
    }