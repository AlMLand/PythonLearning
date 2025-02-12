from player import Player
from scenario import Scenario


class Npc(Player):
    def __init__(self, name: str, random_choice: bool = True):
        super().__init__(name, random_choice)

    def update_choice(self, scenario: Scenario, current_input: str):
        scenario.update(current_input, "O")
