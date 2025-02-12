from play_symbol import PlaySymbol
from player import Player
from scenario import Scenario


class User(Player):
    def __init__(self, name: str):
        super().__init__(name)

    def update_choice(self, scenario: Scenario, current_input: str) -> bool:
        return scenario.update(current_input, PlaySymbol.symbol_x.value)
