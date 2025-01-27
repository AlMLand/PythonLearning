from abc import ABC


class Choice(ABC):
    def value(self) -> str:
        pass

    def sequence(self) -> int:
        pass
