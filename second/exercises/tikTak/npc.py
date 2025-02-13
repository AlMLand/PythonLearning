from play_symbol import PlaySymbol
from player import Player
from scenario import Scenario


class Npc(Player):
    def __init__(self, name: str, random_choice: bool = True):
        super().__init__(name, random_choice)

    def update_choice(self, scenario: Scenario, current_input: str) -> bool:
        return scenario.game_board.update_board(current_input, PlaySymbol.symbol_o.value)
