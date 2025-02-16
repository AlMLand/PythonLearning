from second.exercises.war.domain.card.card_name import CardName
from second.exercises.war.domain.card.card_picture import CardPicture
from second.exercises.war.domain.card.card_rank import CardRank
from second.exercises.war.domain.suit import Suit


class Card:
    def __init__(self, suit: Suit, name: CardName, rank: CardRank, picture: CardPicture):
        self.suit = suit
        self.name = name
        self.rank = rank
        self.picture = picture
