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


scenarios = ("|___", "|___", "|___|", "|___", "|___", "|___|", "|___", "|___", "|___|")
win_scenarios = (
    ((0, "|_X_"), (3, "|_X_"), (6, "|_X_")), ((1, "|_X_"), (4, "|_X_"), (7, "|_X_")),
    ((2, "|_X_"), (5, "|_X_"), (8, "|_X_")), ((0, "|_X_"), (1, "|_X_"), (2, "|_X_")),
    ((3, "|_X_"), (4, "|_X_"), (5, "|_X_")), ((6, "|_X_"), (7, "|_X_"), (8, "|_X_")),
    ((0, "|_X_"), (4, "|_X_"), (8, "|_X_")), ((2, "|_X_"), (4, "|_X_"), (6, "|_X_"))
)
lose_scenarios = (
    ((0, "|_O_"), (3, "|_O_"), (6, "|_O_")), ((1, "|_O_"), (4, "|_O_"), (7, "|_O_")),
    ((2, "|_O_"), (5, "|_O_"), (8, "|_O_")), ((0, "|_O_"), (1, "|_O_"), (2, "|_O_")),
    ((3, "|_O_"), (4, "|_O_"), (5, "|_O_")), ((6, "|_O_"), (7, "|_O_"), (8, "|_O_")),
    ((0, "|_O_"), (4, "|_O_"), (8, "|_O_")), ((2, "|_O_"), (4, "|_O_"), (6, "|_O_"))
)

first_row = {f"{RowHorizontal.FIRST.value}{RowVertical.FIRST.value}": scenarios[0],
             f"{RowHorizontal.FIRST.value}{RowVertical.SECOND.value}": scenarios[1],
             f"{RowHorizontal.FIRST.value}{RowVertical.THIRD.value}": scenarios[2]}
second_row = {f"{RowHorizontal.SECOND.value}{RowVertical.FIRST.value}": scenarios[3],
              f"{RowHorizontal.SECOND.value}{RowVertical.SECOND.value}": scenarios[4],
              f"{RowHorizontal.SECOND.value}{RowVertical.THIRD.value}": scenarios[5]}
third_row = {f"{RowHorizontal.THIRD.value}{RowVertical.FIRST.value}": scenarios[6],
             f"{RowHorizontal.THIRD.value}{RowVertical.SECOND.value}": scenarios[7],
             f"{RowHorizontal.THIRD.value}{RowVertical.THIRD.value}": scenarios[8]}
keys = {RowHorizontal.FIRST.value: first_row, RowHorizontal.SECOND.value: second_row,
        RowHorizontal.THIRD.value: third_row}


def display():
    print(f"   _{RowVertical.FIRST.value}_ _{RowVertical.SECOND.value}_ _{RowVertical.THIRD.value}_")
    print(f"{RowHorizontal.FIRST.value} " +
          first_row[f"{RowHorizontal.FIRST.value}{RowVertical.FIRST.value}"] +
          first_row[f"{RowHorizontal.FIRST.value}{RowVertical.SECOND.value}"] +
          first_row[f"{RowHorizontal.FIRST.value}{RowVertical.THIRD.value}"])
    print(f"{RowHorizontal.SECOND.value} " +
          second_row[f"{RowHorizontal.SECOND.value}{RowVertical.FIRST.value}"] +
          second_row[f"{RowHorizontal.SECOND.value}{RowVertical.SECOND.value}"] +
          second_row[f"{RowHorizontal.SECOND.value}{RowVertical.THIRD.value}"])
    print(f"{RowHorizontal.THIRD.value} " +
          third_row[f"{RowHorizontal.THIRD.value}{RowVertical.FIRST.value}"] +
          third_row[f"{RowHorizontal.THIRD.value}{RowVertical.SECOND.value}"] +
          third_row[f"{RowHorizontal.THIRD.value}{RowVertical.THIRD.value}"])


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

    row = keys[current_input[0]]
    current_value = row[current_input]
    row[current_input] = "".join([c if i != 2 else "X" for i, c in enumerate(current_value)])


def is_not_delimiter(current_input):
    return not current_input[2] == "-"


def is_not_digit(current_input):
    return current_input[1] not in [RowVertical.FIRST.value, RowVertical.SECOND.value, RowVertical.THIRD.value]


def is_not_letter(current_input):
    return current_input[0].upper() not in [RowHorizontal.FIRST.value, RowHorizontal.SECOND.value,
                                            RowHorizontal.THIRD.value]


def win_validation() -> bool:
    for win_sc in win_scenarios:
        if (win_sc[0][1] == scenarios[win_sc[0][0]] and win_sc[1][1] == scenarios[win_sc[1][0]]
                and win_sc[2][1] == scenarios[win_sc[2][0]]):
            print("=) you won =)")
            return False
    for lose_sc in lose_scenarios:
        if (lose_sc[0][1] == scenarios[lose_sc[0][0]] and lose_sc[1][1] == scenarios[lose_sc[1][0]]
                and lose_sc[2][1] == scenarios[lose_sc[2][0]]):
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
