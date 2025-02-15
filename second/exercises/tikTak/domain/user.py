from second.exercises.tikTak.domain.play_symbol import PlaySymbol
from second.exercises.tikTak.domain.player import Player
from second.exercises.tikTak.domain.scenario import Scenario


class User(Player):
    def __init__(self, name: str):
        super().__init__(name)

    def update_choice(self, scenario: Scenario, current_input: str) -> bool:
        return scenario.game_board.update_board(current_input, PlaySymbol.symbol_x.value)
