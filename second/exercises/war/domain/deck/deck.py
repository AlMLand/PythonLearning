import random

from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.play_set import PlaySet
from second.exercises.war.domain.suitset.suit_set import SuitSet


class Deck:
    def __init__(self, acorn_suit: SuitSet, leave_suit: SuitSet, heart_suit: SuitSet, bell_suit: SuitSet):
        self.acorn_suit = acorn_suit
        self.leave_suit = leave_suit
        self.heart_suit = heart_suit
        self.bell_suit = bell_suit
        self.whole_card_deck = self.acorn_suit.cards + self.leave_suit.cards + self.heart_suit.cards + self.bell_suit.cards

    def split(self, player_count: int) -> [PlaySet]:
        whole_card_deck = self._randomize_whole_deck()
        split_cards = [whole_card_deck[i::player_count] for i in range(player_count)]
        return [PlaySet(cards) for cards in split_cards]

    def _randomize_whole_deck(self) -> [Card]:
        random.shuffle(self.whole_card_deck)
        return self.whole_card_deck
