from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.play_set import PlaySet


class Player:
    def __init__(self, name: str, play_set: PlaySet):
        self.name = name
        self.play_set = play_set

    def get_card(self) -> Card:
        return self.play_set.get_random_card()

    def put_cards(self, *args: Card):
        self.play_set.put_cards(args)
