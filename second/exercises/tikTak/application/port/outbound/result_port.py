from abc import ABC, abstractmethod

from second.exercises.tikTak.domain.result import Result


class ResultPort(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def create_result(self, result: Result):
        pass

    @abstractmethod
    def get_all_results(self) -> [Result]:
        pass
