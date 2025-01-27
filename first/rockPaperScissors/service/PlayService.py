import random
import time

from first.rockPaperScissors.domain.PaperChoice import PaperChoice
from first.rockPaperScissors.domain.RockChoice import RockChoice
from first.rockPaperScissors.domain.ScissorsChoice import ScissorsChoice
from first.rockPaperScissors.domain.StopChoice import StopChoice

__ERROR_MESSAGE = "Timur gib bitte nur die Zahlen zwischen 1 und 4 an, Danke dir.\n"
__TIME_TO_SLEEP_ONE_SECONDS = 1
__TIME_TO_SLEEP_TWO_SECONDS = 2

stop_choice = StopChoice()
rock_choice = RockChoice()
paper_choice = PaperChoice()
scissors_choice = ScissorsChoice()


def user_choice() -> int:
    number = 0
    try:
        number = int(
            input(f"Timur, wähle zwischen:\n"
                  f"{rock_choice.sequence()} - {rock_choice.value()}\n"
                  f"{paper_choice.sequence()} - {paper_choice.value()}\n"
                  f"{scissors_choice.sequence()} - {scissors_choice.value()}\n"
                  f"{stop_choice.sequence()} - {stop_choice.value()}\n"
                  f"schreibe hier deine Zahl: ")
        )
        return number
    except ValueError:
        print(__ERROR_MESSAGE)
        user_choice()
    finally:
        if number not in range(rock_choice.sequence(), stop_choice.sequence() + 1):
            print(__ERROR_MESSAGE)
            user_choice()


def compute_and_print_result(user: int, npc: int):
    if user == npc:
        print(" ----- Unentschieden ----- \n")
    elif rock_hits_scissors(npc, user) or paper_hits_rock(npc, user) or scissors_hits_paper(npc, user):
        print(" ----- Timur, du gewinnst ----- \n")
    else:
        print(" ----- Computer hat gewonnen ----- \n")


def scissors_hits_paper(npc: int, user: int) -> bool:
    return user == scissors_choice.sequence() and npc == paper_choice.sequence()


def paper_hits_rock(npc: int, user: int) -> bool:
    return user == paper_choice.sequence() and npc == rock_choice.sequence()


def rock_hits_scissors(npc: int, user: int) -> bool:
    return user == rock_choice.sequence() and npc == scissors_choice.sequence()


def stop_play(user: int):
    if user == stop_choice.sequence():
        print("Danke für das Spiel, Timur!\n")


def start():
    choice = user_choice()
    stop_play(choice)
    while choice != stop_choice.sequence():
        npc = npc_choice()
        delay()
        compute_and_print_result(choice, npc)
        time.sleep(__TIME_TO_SLEEP_TWO_SECONDS)
        choice = user_choice()
        stop_play(choice)


def npc_choice() -> int:
    choices = [rock_choice.sequence(), paper_choice.sequence(), scissors_choice.sequence()]
    return int(random.choice(choices))


def delay():
    time.sleep(__TIME_TO_SLEEP_ONE_SECONDS)
    print("     Schnick")
    time.sleep(__TIME_TO_SLEEP_ONE_SECONDS)
    print("         Schnack")
    time.sleep(__TIME_TO_SLEEP_ONE_SECONDS)
    print("             Schnuck")
    time.sleep(__TIME_TO_SLEEP_ONE_SECONDS)
