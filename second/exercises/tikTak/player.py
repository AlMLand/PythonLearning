import random
from abc import ABC

from axis_x import AxisX
from axis_y import AxisY
from row import Row
from scenario import Scenario


def _is_not_letter(current_input) -> bool:
    return current_input[0].upper() not in [AxisX.FIRST.value, AxisX.SECOND.value, AxisX.THIRD.value]


def _is_not_digit(current_input) -> bool:
    return current_input[1] not in [AxisY.FIRST.value, AxisY.SECOND.value, AxisY.THIRD.value]


class Player(ABC):
    def __init__(self, name: str, random_choice: bool = False):
        self.name = name
        self.random_choice = random_choice

    def choice(self, scenario: Scenario, current_input: str = None, is_correct: bool = True):
        example = f"(example {AxisX.FIRST.value}{AxisY.THIRD.value})"

        if self.random_choice:
            print("automated step")
            random_row: Row = random.choice([scenario.row_1, scenario.row_2, scenario.row_3])
            current_input = random.choice([
                random_row.cell_1.coordinate(), random_row.cell_2.coordinate(), random_row.cell_3.coordinate()
            ])
        elif is_correct and current_input is None:
            current_input = input(f"do your step {example}: ")
        else:
            current_input = input(f"your input was incorrect \"{current_input}\", try again {example}: ")

        if not self.set_choice(scenario, current_input.upper()):
            print(f"repeat this step, you choice {current_input} is not possible")
            self.choice(scenario, current_input, False)

    def set_choice(self, scenario: Scenario, current_input: str) -> bool:
        if len(current_input) != 2 or _is_not_letter(current_input) or _is_not_digit(current_input):
            self.choice(scenario, current_input, False)
        return self.update_choice(scenario, current_input)

    def update_choice(self, scenario: Scenario, current_input: str) -> bool:
        pass
