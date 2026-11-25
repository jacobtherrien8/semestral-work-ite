"""Entry point of the Hockey Stick Recommender.

Usage: python main.py

Author: Jacob Therrien
"""
from src.display import show_recommendation
from src.input import ask_player_info
from src.recommender import recommend_stick


def main():
    """Run the program: ask the questions, compute the stick, display it."""
    print("=== Hockey Stick Recommender ===")
    player = ask_player_info()
    stick = recommend_stick(player)
    show_recommendation(stick)


if __name__ == "__main__":
    main()

    