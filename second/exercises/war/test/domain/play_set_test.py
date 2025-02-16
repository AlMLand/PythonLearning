import unittest

from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.card.card_name import CardName
from second.exercises.war.domain.card.card_picture import CardPicture
from second.exercises.war.domain.card.card_rank import CardRank
from second.exercises.war.domain.play_set import PlaySet
from second.exercises.war.domain.suit import Suit


class PlaySetTest(unittest.TestCase):

    def test_get_random_than_drop_random_card_from_cards(self):
        cards = [
            Card(Suit.ACORN, CardName.TWO, CardRank.RANK_2, CardPicture.picture_2),
            Card(Suit.ACORN, CardName.THREE, CardRank.RANK_3, CardPicture.picture_3)
        ]
        play_set = PlaySet(cards)

        result = play_set.get_random_card()

        self.assertEqual(result.suit, Suit.ACORN)
        self.assertEqual(len(play_set.cards), 1)

    def test_put_cards_when_append_new_card_size_is_three(self):
        cards = [Card(Suit.ACORN, CardName.TWO, CardRank.RANK_2, CardPicture.picture_2)]
        play_set = PlaySet(cards)
        card_1 = Card(Suit.HEART, CardName.THREE, CardRank.RANK_3, CardPicture.picture_3)
        card_2 = Card(Suit.LEAVE, CardName.FOUR, CardRank.RANK_4, CardPicture.picture_4)

        play_set.put_cards(card_1, card_2)

        self.assertEqual(len(play_set.cards), 3)
