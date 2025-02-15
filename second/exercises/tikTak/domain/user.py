from second.exercises.tikTak.domain.play_mode import Mode
from second.exercises.tikTak.domain.play_symbol import PlaySymbol
from second.exercises.tikTak.domain.player import Player
from second.exercises.tikTak.domain.scenario import Scenario


class User(Player):
    def __init__(self, name: str, mode: Mode = Mode.SINGLE):
        super().__init__(name)
        self.mode = mode

    def update_choice(self, scenario: Scenario, current_input: str) -> bool:
        return scenario.game_board.update_board(current_input, self.set_user_symbol())

    def set_user_symbol(self) -> str:
        if self.mode == Mode.SINGLE:
            return PlaySymbol.symbol_x.value
        else:
            return PlaySymbol.symbol_o.value
