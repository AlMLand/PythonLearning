import random
import time

from rockPaperScissors.domain.PaperChoice import PaperChoice
from rockPaperScissors.domain.RockChoice import RockChoice
from rockPaperScissors.domain.ScissorsChoice import ScissorsChoice
from rockPaperScissors.domain.StopChoice import StopChoice

__time_to_sleep_one_seconds = 1
__time_to_sleep_two_seconds = 2

stop_choice = StopChoice()
rock_choice = RockChoice()
paper_choice = PaperChoice()
scissors_choice = ScissorsChoice()


def user_choice() -> int:
    try:
        return int(
            input(f"Timur, wähle zwischen:\n"
                  f"{rock_choice.sequence()} - {rock_choice.value()}\n"
                  f"{paper_choice.sequence()} - {paper_choice.value()}\n"
                  f"{scissors_choice.sequence()} - {scissors_choice.value()}\n"
                  f"{stop_choice.sequence()} - {stop_choice.value()}\n"
                  f"schreibe hier deine Zahl: ")
        )
    except ValueError:
        print("Timur gib bitte nur die Zahlen zwischen 1 und 4 an, Danke dir.\n")
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
    user = user_choice()
    stop_play(user)
    while user != stop_choice.sequence():
        npc = npc_choice()
        delay()
        compute_and_print_result(user, npc)
        time.sleep(__time_to_sleep_two_seconds)
        user = user_choice()
        stop_play(user)


def npc_choice() -> int:
    choices = [rock_choice.sequence(), paper_choice.sequence(), scissors_choice.sequence()]
    return int(random.choice(choices))


def delay():
    time.sleep(__time_to_sleep_one_seconds)
    print("     Schnick")
    time.sleep(__time_to_sleep_one_seconds)
    print("         Schnack")
    time.sleep(__time_to_sleep_one_seconds)
    print("             Schnuck")
    time.sleep(__time_to_sleep_one_seconds)
