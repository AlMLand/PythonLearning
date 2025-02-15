from second.exercises.tikTak.application.port.outbound.result_port import ResultPort
from second.exercises.tikTak.domain.npc import Npc
from second.exercises.tikTak.domain.result import Result
from second.exercises.tikTak.domain.scenario import Scenario
from second.exercises.tikTak.domain.user import User
from second.exercises.tikTak.infrastructure.adaptor.outbound.persistence_adaptor import PersistenceAdaptor


class ResultService(ResultPort):

    def __init__(self):
        self.persistence_port = PersistenceAdaptor()

    def start_game(self):
        scenario = Scenario()
        user = User("user")
        npc = Npc("npc")

        while True:
            scenario.display()

            user.choice(scenario)
            if scenario.winning():
                self.create_result(Result(user.name, scenario.is_free_space_available()))
                break
            if scenario.undecided():
                self.create_result(Result("no winner", False))
                break

            scenario.display()

            npc.choice(scenario)
            if scenario.winning():
                self.create_result(Result(npc.name, scenario.is_free_space_available()))
                break
            if scenario.undecided():
                self.create_result(Result("no winner", False))
                break

    def create_result(self, result: Result):
        self.persistence_port.create_result(result)

    def get_all_results(self) -> [Result]:
        self.persistence_port.get_all_results()
