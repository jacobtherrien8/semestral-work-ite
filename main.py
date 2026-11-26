"""Entry point of the Hockey Stick Recommender.

Usage: python main.py

"""
from src.display import show_recommendation
from src.input import ExitProgram, ask_player_info
from src.recommender import recommend_stick


def main():
    """Run the program: ask the questions, compute the stick, display it.

    The user can type "e" at any question to stop the program.
    """
    print("=== Hockey Stick Recommender ===")
    print('Press "e" to exit the program.')
    try:
        player = ask_player_info()
    except ExitProgram:
        print("Hockey recommendation stopped.")
        return
    stick = recommend_stick(player)
    show_recommendation(stick)


if __name__ == "__main__":
    main()