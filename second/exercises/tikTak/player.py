from abc import ABC

from axisx import AxisX
from axisy import AxisY
from scenario import Scenario


def is_not_letter(current_input) -> bool:
    return current_input[0].upper() not in [AxisX.FIRST.value, AxisX.SECOND.value, AxisX.THIRD.value]


def is_not_digit(current_input) -> bool:
    return current_input[1] not in [AxisY.FIRST.value, AxisY.SECOND.value, AxisY.THIRD.value]


class Player(ABC):
    def __init__(self, name: str):
        self.name = name

    def choice(self, scenario: Scenario, current_input: str = None, is_correct: bool = True):
        example = f"(example {AxisX.FIRST.value}{AxisY.THIRD.value})"
        if is_correct and current_input is None:
            current_input = input(f"do your step {example}: ")
        else:
            current_input = input(f"your input was incorrect \"{current_input}\", try again {example}: ")
        self.set_choice(scenario, current_input.upper())

    def set_choice(self, scenario: Scenario, current_input: str):
        if len(current_input) != 2 or is_not_letter(current_input) or is_not_digit(current_input):
            self.choice(scenario, current_input, False)
        self.update_choice(scenario, current_input)

    def update_choice(self, scenario: Scenario, current_input: str):
        pass
