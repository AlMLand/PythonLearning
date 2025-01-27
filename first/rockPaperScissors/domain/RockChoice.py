from first.rockPaperScissors.domain.Choice import Choice


class RockChoice(Choice):
    def value(self) -> str:
        return "Stein"

    def sequence(self) -> int:
        return 1
