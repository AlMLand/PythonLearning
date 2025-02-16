from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.card.card_name import CardName
from second.exercises.war.domain.card.card_picture import CardPicture
from second.exercises.war.domain.card.card_rank import CardRank
from second.exercises.war.domain.suit import Suit
from second.exercises.war.domain.suitset.suit_set import SuitSet


class SuitSetBuilder:
    @staticmethod
    def get_start_suit_set() -> list[SuitSet]:
        return [
            SuitSet(
                Suit.ACORN,
                [
                    Card(Suit.ACORN, CardName.TWO, CardRank.RANK_2, CardPicture.picture_2),
                    Card(Suit.ACORN, CardName.THREE, CardRank.RANK_3, CardPicture.picture_3),
                    Card(Suit.ACORN, CardName.FOUR, CardRank.RANK_4, CardPicture.picture_4),
                    Card(Suit.ACORN, CardName.FIVE, CardRank.RANK_5, CardPicture.picture_5),
                    Card(Suit.ACORN, CardName.SIX, CardRank.RANK_6, CardPicture.picture_6),
                    Card(Suit.ACORN, CardName.SEVEN, CardRank.RANK_7, CardPicture.picture_7),
                    Card(Suit.ACORN, CardName.EIGHT, CardRank.RANK_8, CardPicture.picture_8),
                    Card(Suit.ACORN, CardName.NINE, CardRank.RANK_9, CardPicture.picture_9),
                    Card(Suit.ACORN, CardName.TEN, CardRank.RANK_10, CardPicture.picture_10),
                    Card(Suit.ACORN, CardName.JACK, CardRank.RANK_11, CardPicture.picture_11),
                    Card(Suit.ACORN, CardName.QUEEN, CardRank.RANK_12, CardPicture.picture_12),
                    Card(Suit.ACORN, CardName.KING, CardRank.RANK_13, CardPicture.picture_13),
                    Card(Suit.ACORN, CardName.ACE, CardRank.RANK_14, CardPicture.picture_14)
                ]
            ),
            SuitSet(
                Suit.LEAVE,
                [
                    Card(Suit.LEAVE, CardName.TWO, CardRank.RANK_2, CardPicture.picture_2),
                    Card(Suit.LEAVE, CardName.THREE, CardRank.RANK_3, CardPicture.picture_3),
                    Card(Suit.LEAVE, CardName.FOUR, CardRank.RANK_4, CardPicture.picture_4),
                    Card(Suit.LEAVE, CardName.FIVE, CardRank.RANK_5, CardPicture.picture_5),
                    Card(Suit.LEAVE, CardName.SIX, CardRank.RANK_6, CardPicture.picture_6),
                    Card(Suit.LEAVE, CardName.SEVEN, CardRank.RANK_7, CardPicture.picture_7),
                    Card(Suit.LEAVE, CardName.EIGHT, CardRank.RANK_8, CardPicture.picture_8),
                    Card(Suit.LEAVE, CardName.NINE, CardRank.RANK_9, CardPicture.picture_9),
                    Card(Suit.LEAVE, CardName.TEN, CardRank.RANK_10, CardPicture.picture_10),
                    Card(Suit.LEAVE, CardName.JACK, CardRank.RANK_11, CardPicture.picture_11),
                    Card(Suit.LEAVE, CardName.QUEEN, CardRank.RANK_12, CardPicture.picture_12),
                    Card(Suit.LEAVE, CardName.KING, CardRank.RANK_13, CardPicture.picture_13),
                    Card(Suit.LEAVE, CardName.ACE, CardRank.RANK_14, CardPicture.picture_14)
                ]
            ),
            SuitSet(
                Suit.HEART,
                [
                    Card(Suit.HEART, CardName.TWO, CardRank.RANK_2, CardPicture.picture_2),
                    Card(Suit.HEART, CardName.THREE, CardRank.RANK_3, CardPicture.picture_3),
                    Card(Suit.HEART, CardName.FOUR, CardRank.RANK_4, CardPicture.picture_4),
                    Card(Suit.HEART, CardName.FIVE, CardRank.RANK_5, CardPicture.picture_5),
                    Card(Suit.HEART, CardName.SIX, CardRank.RANK_6, CardPicture.picture_6),
                    Card(Suit.HEART, CardName.SEVEN, CardRank.RANK_7, CardPicture.picture_7),
                    Card(Suit.HEART, CardName.EIGHT, CardRank.RANK_8, CardPicture.picture_8),
                    Card(Suit.HEART, CardName.NINE, CardRank.RANK_9, CardPicture.picture_9),
                    Card(Suit.HEART, CardName.TEN, CardRank.RANK_10, CardPicture.picture_10),
                    Card(Suit.HEART, CardName.JACK, CardRank.RANK_11, CardPicture.picture_11),
                    Card(Suit.HEART, CardName.QUEEN, CardRank.RANK_12, CardPicture.picture_12),
                    Card(Suit.HEART, CardName.KING, CardRank.RANK_13, CardPicture.picture_13),
                    Card(Suit.HEART, CardName.ACE, CardRank.RANK_14, CardPicture.picture_14)
                ]
            ),
            SuitSet(
                Suit.BELL,
                [
                    Card(Suit.BELL, CardName.TWO, CardRank.RANK_2, CardPicture.picture_2),
                    Card(Suit.BELL, CardName.THREE, CardRank.RANK_3, CardPicture.picture_3),
                    Card(Suit.BELL, CardName.FOUR, CardRank.RANK_4, CardPicture.picture_4),
                    Card(Suit.BELL, CardName.FIVE, CardRank.RANK_5, CardPicture.picture_5),
                    Card(Suit.BELL, CardName.SIX, CardRank.RANK_6, CardPicture.picture_6),
                    Card(Suit.BELL, CardName.SEVEN, CardRank.RANK_7, CardPicture.picture_7),
                    Card(Suit.BELL, CardName.EIGHT, CardRank.RANK_8, CardPicture.picture_8),
                    Card(Suit.BELL, CardName.NINE, CardRank.RANK_9, CardPicture.picture_9),
                    Card(Suit.BELL, CardName.TEN, CardRank.RANK_10, CardPicture.picture_10),
                    Card(Suit.BELL, CardName.JACK, CardRank.RANK_11, CardPicture.picture_11),
                    Card(Suit.BELL, CardName.QUEEN, CardRank.RANK_12, CardPicture.picture_12),
                    Card(Suit.BELL, CardName.KING, CardRank.RANK_13, CardPicture.picture_13),
                    Card(Suit.BELL, CardName.ACE, CardRank.RANK_14, CardPicture.picture_14)
                ]
            )
        ]
