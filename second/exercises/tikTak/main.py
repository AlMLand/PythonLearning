from npc import Npc
from scenario import Scenario
from user import User


def start():
    scenario = Scenario()
    user = User("user")
    npc = Npc("npc")

    while True:
        scenario.display()

        user.choice(scenario)
        if not scenario.winning():
            break

        scenario.display()

        npc.choice(scenario)
        if not scenario.winning():
            break


start()
