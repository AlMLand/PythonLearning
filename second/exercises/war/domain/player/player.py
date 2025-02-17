from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.play_set import PlaySet


class Player:
    def __init__(self, name: str, play_set: PlaySet):
        self.name = name
        self.play_set = play_set
        self.current_card = None

    def get_card(self) -> Card:
        self.current_card = self.play_set.get_random_card()
        return self.current_card

    def put_cards(self, cards: list[Card]):
        self.play_set.put_cards(cards)

    def display(self):
        print(f"Player with name {self.name}")

    def __repr__(self):
        return f"Player [name={self.name}, play_set={self.play_set}]"
