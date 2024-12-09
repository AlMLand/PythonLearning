from rockPaperScissors.domain.Choice import Choice


class ScissorsChoice(Choice):
    def value(self) -> str:
        return "Schäre"

    def sequence(self) -> int:
        return 3
