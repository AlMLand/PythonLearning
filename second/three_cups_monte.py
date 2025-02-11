import random
from random import shuffle

cups = ["O", "", ""]


def shuffle_cups():
    shuffle(cups)


def random_choice() -> int:
    return random.randint(0, len(cups) - 1)


def user_choice() -> int:
    manipulate_collection_index = 1

    choice = ""
    choice_max = len(cups)
    possible_choices = [f"{index + manipulate_collection_index}" for index, value in enumerate(cups)]

    while choice not in possible_choices:
        choice = input(f"get a number between 1 and {choice_max}: ")

    return int(choice) - manipulate_collection_index


def play():
    win_indicator = "O"

    shuffle_cups()
    cup = cups[user_choice()]

    if win_indicator in cup:
        print("yor won")
    else:
        print("try again")


play()
