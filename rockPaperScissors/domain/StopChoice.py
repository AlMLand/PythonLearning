from rockPaperScissors.domain.Choice import Choice


class StopChoice(Choice):
    def value(self) -> str:
        return "Stop"

    def sequence(self) -> int:
        return 4
