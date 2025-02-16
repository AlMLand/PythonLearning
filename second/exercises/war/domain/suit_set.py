from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.suit import Suit


class SuitSet:
    def __init__(self, suit: Suit, cards: list[Card]):
        self.suit = suit
        self.cards = cards
