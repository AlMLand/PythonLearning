import unittest

from second.exercises.war.domain.deck.deck_builder import DeckBuilder
from second.exercises.war.domain.suit import Suit


class DeckBuilderTest(unittest.TestCase):

    def test_check_suits(self):
        deck = DeckBuilder.get_start_deck()

        self.assertEqual(deck.acorn_suit.suit, Suit.ACORN)
        self.assertEqual(deck.acorn_suit.cards[0].suit, Suit.ACORN)

        self.assertEqual(deck.leave_suit.suit, Suit.LEAVE)
        self.assertEqual(deck.leave_suit.cards[0].suit, Suit.LEAVE)

        self.assertEqual(deck.heart_suit.suit, Suit.HEART)
        self.assertEqual(deck.heart_suit.cards[0].suit, Suit.HEART)

        self.assertEqual(deck.bell_suit.suit, Suit.BELL)
        self.assertEqual(deck.bell_suit.cards[0].suit, Suit.BELL)
