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

        player_1 = User("user_1")
        player_2: Player
        if mode is Mode.MULTI:
            player_2 = User("user_2", Mode.MULTI)
        else:
            player_2 = Npc("npc")

        in_progress = True
        while in_progress:
            for user in [player_1, player_2]:
                scenario.display()
                user.choice(scenario)
                if scenario.winning(user.name):
                    self.create_result(Result(user.name, scenario.is_free_space_available()))
                    in_progress = False
                    break
                if scenario.undecided():
                    self.create_result(Result("no winner", False))
                    in_progress = False
                    break

    def create_result(self, result: Result):
        self.persistence_port.create_result(result)

    def get_all_results(self) -> [Result]:
        self.persistence_port.get_all_results()
