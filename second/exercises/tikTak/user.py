from player import Player
from scenario import Scenario


class User(Player):
    def __init__(self, name: str):
        super().__init__(name)

    def update_choice(self, scenario: Scenario, current_input: str):
        scenario.update(current_input, "X")
