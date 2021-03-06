import HW03_Suraj_Nair_wordle as wordle
import os

from wordle_analyze import WordleAnalyze

class WordleSolver:
    def __init__(self, number_of_automated_games: int = 1) -> None:
        self.number_of_automated_games = number_of_automated_games

    def start_solver(self) -> None:
        game = wordle.Wordle(True, self.number_of_automated_games)
        game.start_game()


if __name__ == "__main__":
    # 3 is the number of times the game will run
    if os.path.exists("logger.db"):
        os.remove("logger.db")
    solver = WordleSolver(1000)
    solver.start_solver()
    analyze = WordleAnalyze()
    analyze.get_report()
