from second.exercises.war.domain.deck.deck import Deck
from second.exercises.war.domain.suitset.suit_set_builder import SuitSetBuilder


class DeckBuilder:
    @staticmethod
    def get_start_deck() -> Deck:
        suit_sets = SuitSetBuilder.get_start_suit_set()
        return Deck(suit_sets[0], suit_sets[1], suit_sets[2], suit_sets[3])
