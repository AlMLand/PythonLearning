import random
from abc import ABC

from axis_x import AxisX
from axis_y import AxisY
from scenario import Scenario


def _is_not_letter(current_input) -> bool:
    return current_input[0].upper() not in [AxisX.FIRST.value, AxisX.SECOND.value, AxisX.THIRD.value]


def _is_not_digit(current_input) -> bool:
    return current_input[1] not in [AxisY.FIRST.value, AxisY.SECOND.value, AxisY.THIRD.value]


class Player(ABC):
    def __init__(self, name: str, random_choice: bool = False):
        self.name = name
        self.random_choice = random_choice

    def choice(self, scenario: Scenario):
        example = f"(example {AxisX.FIRST.value}{AxisY.THIRD.value})"

        is_run = True
        current_input = ""

        while is_run:
            if self.random_choice:
                print("automated step")
                random_row = random.choice(scenario.get_all_rows())
                random_cell = random.choice(random_row.get_all_cells())
                current_input = random_cell.coordinate()
            elif current_input == "":
                current_input: str = input(f"do your step {example}: ")
            else:
                current_input: str = input(f"your input was incorrect \"{current_input}\", try again {example}: ")

            current_input_upper_case = current_input.upper()
            if len(current_input) != 2 or _is_not_letter(current_input_upper_case) or _is_not_digit(current_input):
                print(f"repeat this step, you choice {current_input} is not possible")
            else:
                is_run = not self.update_choice(scenario, current_input_upper_case)

    def update_choice(self, scenario: Scenario, current_input: str) -> bool:
        pass
