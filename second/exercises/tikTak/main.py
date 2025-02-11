from enum import Enum

"""
       _1_ _2_ _3_
    A |___|___|___|
    B |___|___|___|
    C |___|___|___|

"""


class RowHorizontal(Enum):
    FIRST: str = "A"
    SECOND: str = "B"
    THIRD: str = "C"


class RowVertical(Enum):
    FIRST: str = "1"
    SECOND: str = "2"
    THIRD: str = "3"


class Scenario:
    scenarios = (
        [f"{RowHorizontal.FIRST.value}{RowVertical.FIRST.value}", "|___"],
        [f"{RowHorizontal.FIRST.value}{RowVertical.SECOND.value}", "|___"],
        [f"{RowHorizontal.FIRST.value}{RowVertical.THIRD.value}", "|___|"],  # 2
        [f"{RowHorizontal.SECOND.value}{RowVertical.FIRST.value}", "|___"],
        [f"{RowHorizontal.SECOND.value}{RowVertical.SECOND.value}", "|___"],
        [f"{RowHorizontal.SECOND.value}{RowVertical.THIRD.value}", "|___|"],  # 5
        [f"{RowHorizontal.THIRD.value}{RowVertical.FIRST.value}", "|___"],
        [f"{RowHorizontal.THIRD.value}{RowVertical.SECOND.value}", "|___"],
        [f"{RowHorizontal.THIRD.value}{RowVertical.THIRD.value}", "|___|"]  # 8
    )
    win_scenarios = (
        ((0, "|_X_"), (3, "|_X_"), (6, "|_X_")), ((1, "|_X_"), (4, "|_X_"), (7, "|_X_")),
        ((2, "|_X_|"), (5, "|_X_|"), (8, "|_X_|")), ((0, "|_X_"), (1, "|_X_"), (2, "|_X_|")),
        ((3, "|_X_"), (4, "|_X_"), (5, "|_X_|")), ((6, "|_X_"), (7, "|_X_"), (8, "|_X_|")),
        ((0, "|_X_"), (4, "|_X_"), (8, "|_X_|")), ((2, "|_X_|"), (4, "|_X_"), (6, "|_X_"))
    )
    lose_scenarios = (
        ((0, "|_O_"), (3, "|_O_"), (6, "|_O_")), ((1, "|_O_"), (4, "|_O_"), (7, "|_O_")),
        ((2, "|_O_|"), (5, "|_O_|"), (8, "|_O_|")), ((0, "|_O_"), (1, "|_O_"), (2, "|_O_|")),
        ((3, "|_O_"), (4, "|_O_"), (5, "|_O_|")), ((6, "|_O_"), (7, "|_O_"), (8, "|_O_|")),
        ((0, "|_O_"), (4, "|_O_"), (8, "|_O_|")), ((2, "|_O_"), (4, "|_O_"), (6, "|_O_"))
    )


def display():
    print(f"   _{RowVertical.FIRST.value}_ _{RowVertical.SECOND.value}_ _{RowVertical.THIRD.value}_")
    print(f"{RowHorizontal.FIRST.value} " + Scenario.scenarios[0][1] + Scenario.scenarios[1][1] + Scenario.scenarios[2][
        1])
    print(
        f"{RowHorizontal.SECOND.value} " + Scenario.scenarios[3][1] + Scenario.scenarios[4][1] + Scenario.scenarios[5][
            1])
    print(f"{RowHorizontal.THIRD.value} " + Scenario.scenarios[6][1] + Scenario.scenarios[7][1] + Scenario.scenarios[8][
        1])


def choice(current_input: str = None, is_correct: bool = True):
    example = f"(example {RowHorizontal.FIRST.value}{RowVertical.THIRD.value})"
    if is_correct and current_input is None:
        current_input = input(f"do your step {example}: ")
    else:
        current_input = input(f"your input was incorrect \"{current_input}\", try again {example}: ")
    set_choice(current_input.upper())


def set_choice(current_input: str):
    if len(current_input) != 2 or is_not_letter(current_input) or is_not_digit(current_input):
        choice(current_input, False)

    Scenario.scenarios = tuple(
        map(
            lambda item: item if item[0] != current_input else (
                item[0], "".join([c if i != 2 else "X" for i, c in enumerate(item[1])])), Scenario.scenarios
        )
    )


def is_not_delimiter(current_input):
    return not current_input[2] == "-"


def is_not_digit(current_input):
    return current_input[1] not in [RowVertical.FIRST.value, RowVertical.SECOND.value, RowVertical.THIRD.value]


def is_not_letter(current_input):
    return current_input[0].upper() not in [RowHorizontal.FIRST.value, RowHorizontal.SECOND.value,
                                            RowHorizontal.THIRD.value]


def win_validation() -> bool:
    for win_sc in Scenario.win_scenarios:
        if (win_sc[0][1] == Scenario.scenarios[win_sc[0][0]][1] and win_sc[1][1] == Scenario.scenarios[win_sc[1][0]][1]
                and win_sc[2][1] == Scenario.scenarios[win_sc[2][0]][1]):
            display()
            print("=) you won =)")
            return False
    for lose_sc in Scenario.lose_scenarios:
        if (lose_sc[0][1] == Scenario.scenarios[lose_sc[0][0]][1] and lose_sc[1][1] ==
                Scenario.scenarios[lose_sc[1][0]][1]
                and lose_sc[2][1] == Scenario.scenarios[lose_sc[2][0]][1]):
            display()
            print("=( you lose =(")
            return False
    return True


def start():
    is_run = True
    while is_run:
        display()
        choice()
        is_run = win_validation()


start()
