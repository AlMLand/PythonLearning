from rockPaperScissors.domain.Choice import Choice


class PaperChoice(Choice):
    def value(self) -> str:
        return "Papier"

    def sequence(self) -> int:
        return 2
