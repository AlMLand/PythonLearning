from abc import ABC, abstractmethod

from second.exercises.tikTak.domain.play_mode import Mode
from second.exercises.tikTak.domain.result import Result


class ResultPort(ABC):
    @abstractmethod
    def start_game(self, mode: Mode):
        pass

    @abstractmethod
    def create_result(self, result: Result):
        pass

    @abstractmethod
    def get_all_results(self) -> [Result]:
        pass
