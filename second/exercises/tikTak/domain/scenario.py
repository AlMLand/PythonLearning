from second.exercises.tikTak.domain.game_board import GameBoard
from second.exercises.tikTak.domain.row import Row


class Scenario:
    def __init__(self):
        self.game_board = GameBoard()

    def display(self):
        self.game_board.display()

    def is_free_space_available(self):
        return self.game_board.is_free_space_available()

    def get_all_rows(self) -> list[Row]:
        return self.game_board.get_all_rows()

    def winning(self) -> bool:
        for win_sc in self._win_scenarios():
            if win_sc:
                self.display()
                print("=) you won =)")
                return False
        for lose_sc in self._lose_scenarios():
            if lose_sc:
                self.display()
                print("=( you lose =(")
                return False
        if not self.game_board.is_free_space_available():
            print("!! no winner !!")
            return False
        return True

    def _win_scenarios(self):
        return (
            self.game_board.identical_r1c1_r2c1_r3c2_values("|_X_", "|_X_", "|_X_"),
            self.game_board.identical_r1c2_r2c2_r3c2_values("|_X_", "|_X_", "|_X_"),
            self.game_board.identical_r1c3_r2c3_r3c3_values("|_X_|", "|_X_|", "|_X_|"),
            self.game_board.identical_r1c1_r1c2_r1c3_values("|_X_", "|_X_", "|_X_|"),
            self.game_board.identical_r2c1_r2c2_r2c3_values("|_X_", "|_X_", "|_X_|"),
            self.game_board.identical_r3c1_r3c2_r3c3_values("|_X_", "|_X_", "|_X_|"),
            self.game_board.identical_r1c1_r2c2_r3c3_values("|_X_", "|_X_", "|_X_|"),
            self.game_board.identical_r1c3_r2c2_r3c1_values("|_X_|", "|_X_", "|_X_")
        )

    def _lose_scenarios(self):
        return (
            self.game_board.identical_r1c1_r2c1_r3c2_values("|_O_", "|_O_", "|_O_"),
            self.game_board.identical_r1c2_r2c2_r3c2_values("|_O_", "|_O_", "|_O_"),
            self.game_board.identical_r1c3_r2c3_r3c3_values("|_O_|", "|_O_|", "|_O_|"),
            self.game_board.identical_r1c1_r1c2_r1c3_values("|_O_", "|_O_", "|_O_|"),
            self.game_board.identical_r2c1_r2c2_r2c3_values("|_O_", "|_O_", "|_O_|"),
            self.game_board.identical_r3c1_r3c2_r3c3_values("|_O_", "|_O_", "|_O_|"),
            self.game_board.identical_r1c1_r2c2_r3c3_values("|_O_", "|_O_", "|_O_|"),
            self.game_board.identical_r1c3_r2c2_r3c1_values("|_O_|", "|_O_", "|_O_")
        )
