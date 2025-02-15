from second.exercises.tikTak.application.port.outbound.result_port import ResultPort
from second.exercises.tikTak.domain.npc import Npc
from second.exercises.tikTak.domain.play_mode import Mode
from second.exercises.tikTak.domain.player import Player
from second.exercises.tikTak.domain.result import Result
from second.exercises.tikTak.domain.scenario import Scenario
from second.exercises.tikTak.domain.user import User
from second.exercises.tikTak.infrastructure.adaptor.outbound.persistence_adaptor import PersistenceAdaptor


class ResultService(ResultPort):

    def __init__(self):
        self.persistence_port = PersistenceAdaptor()

    def start_game(self, mode: Mode):
        scenario = Scenario()

        user_1 = User("user_1")
        user_2: Player
        if mode is Mode.MULTI:
            user_2 = User("user_2", Mode.MULTI)
        else:
            user_2 = Npc("npc")

        while True:
            scenario.display()

            user_1.choice(scenario)
            if scenario.winning(user_1.name):
                self.create_result(Result(user_1.name, scenario.is_free_space_available()))
                break
            if scenario.undecided():
                self.create_result(Result("no winner", False))
                break

            scenario.display()

            user_2.choice(scenario)
            if scenario.winning(user_2.name):
                self.create_result(Result(user_2.name, scenario.is_free_space_available()))
                break
            if scenario.undecided():
                self.create_result(Result("no winner", False))
                break

    def create_result(self, result: Result):
        self.persistence_port.create_result(result)

    def get_all_results(self) -> [Result]:
        self.persistence_port.get_all_results()
