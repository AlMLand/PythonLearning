import unittest

from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.card.card_name import CardName
from second.exercises.war.domain.card.card_picture import CardPicture
from second.exercises.war.domain.card.card_rank import CardRank
from second.exercises.war.domain.deck import Deck
from second.exercises.war.domain.suit import Suit
from second.exercises.war.domain.suit_set import SuitSet


class DeckTest(unittest.TestCase):
    _acorn_suit = SuitSet(Suit.ACORN, [Card(Suit.ACORN, CardName.TWO, CardRank.RANK_2, CardPicture.picture_2)])
    _leave_suit = SuitSet(Suit.LEAVE, [Card(Suit.LEAVE, CardName.THREE, CardRank.RANK_3, CardPicture.picture_3)])
    _heart_suit = SuitSet(Suit.HEART, [Card(Suit.HEART, CardName.FOUR, CardRank.RANK_4, CardPicture.picture_4)])
    _bell_suit = SuitSet(Suit.BELL, [Card(Suit.BELL, CardName.FIVE, CardRank.RANK_5, CardPicture.picture_5)])
    _deck = Deck(_acorn_suit, _leave_suit, _heart_suit, _bell_suit)

    def test_split_by_two(self):
        split = self._deck.split(2)

        self.assertEqual(len(split), 2)
        self.assertEqual(len(split[0].cards), 2)
        self.assertEqual(len(split[1].cards), 2)

    def test_split_by_three(self):
        split = self._deck.split(3)

        self.assertEqual(len(split), 3)
        self.assertEqual(len(split[0].cards), 2)
        self.assertEqual(len(split[1].cards), 1)
        self.assertEqual(len(split[2].cards), 1)
