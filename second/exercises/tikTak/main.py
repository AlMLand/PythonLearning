from axisx import AxisX
from axisy import AxisY
from scenario import Scenario


def user_choice(scenario: Scenario, current_input: str = None, is_correct: bool = True):
    example = f"(example {AxisX.FIRST.value}{AxisY.THIRD.value})"
    if is_correct and current_input is None:
        current_input = input(f"do your step {example}: ")
    else:
        current_input = input(f"your input was incorrect \"{current_input}\", try again {example}: ")
    set_choice(scenario, current_input.upper())


def set_choice(scenario: Scenario, current_input: str):
    if len(current_input) != 2 or is_not_letter(current_input) or is_not_digit(current_input):
        user_choice(scenario, current_input, False)
    scenario.update(current_input)


def is_not_digit(current_input) -> bool:
    return current_input[1] not in [AxisY.FIRST.value, AxisY.SECOND.value, AxisY.THIRD.value]


def is_not_letter(current_input) -> bool:
    return current_input[0].upper() not in [AxisX.FIRST.value, AxisX.SECOND.value, AxisX.THIRD.value]


def enemy_choice():
    pass


def start():
    is_run = True
    scenario = Scenario()

    while is_run:
        scenario.display()
        user_choice(scenario)
        enemy_choice()
        is_run = scenario.scenario_validation()


start()
