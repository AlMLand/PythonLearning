import random

from second.exercises.war.domain.card.card import Card


class PlaySet:
    def __init__(self, cards: list[Card]):
        self.cards = cards
        self._max_possible_amount = 52

    def get_random_card(self) -> Card:
        random_card = random.choice(self.cards)
        self.cards.remove(random_card)
        return random_card

    def put_cards(self, *args: list[Card]):
        self.cards.extend(*args)

    def is_max_possible_amount(self) -> bool:
        return len(self.cards) == self._max_possible_amount
