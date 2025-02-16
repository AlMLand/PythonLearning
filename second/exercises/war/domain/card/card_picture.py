from enum import Enum

from second.exercises.war.domain.card.card_name import CardName
from second.exercises.war.domain.card.card_rank import CardRank


class CardPicture(Enum):
    picture_2: str = (
        f"""
         _______
        |   {CardRank.RANK_2.value}   |
        |  {CardName.TWO.value}  |
        |   {CardRank.RANK_2.value}   |
         -------
        """
    )
    picture_3: str = (
        f"""
         _______
        |   {CardRank.RANK_3.value}   |
        | {CardName.THREE.value} |
        |   {CardRank.RANK_3.value}   |
         -------
        """
    )
    picture_4: str = (
        f"""
         _______
        |   {CardRank.RANK_4.value}   |
        |  {CardName.FOUR.value} |
        |   {CardRank.RANK_4.value}   |
         -------
        """
    )
    picture_5: str = (
        f"""
         _______
        |   {CardRank.RANK_5.value}   |
        |  {CardName.FIVE.value} |
        |   {CardRank.RANK_5.value}   |
         -------
        """
    )
    picture_6: str = (
        f"""
         _______
        |   {CardRank.RANK_6.value}   |
        |  {CardName.SIX.value}  |
        |   {CardRank.RANK_6.value}   |
         -------
        """
    )
    picture_7: str = (
        f"""
         _______
        |   {CardRank.RANK_7.value}   |
        | {CardName.SEVEN.value} |
        |   {CardRank.RANK_7.value}   |
         -------
        """
    )
    picture_8: str = (
        f"""
         _______
        |   {CardRank.RANK_8.value}   |
        | {CardName.EIGHT.value} |
        |   {CardRank.RANK_8.value}   |
         -------
        """
    )
    picture_9: str = (
        f"""
         _______
        |   {CardRank.RANK_9.value}   |
        |  {CardName.NINE.value} |
        |   {CardRank.RANK_9.value}   |
         -------
        """
    )
    picture_10: str = (
        f"""
         _______
        |   {CardRank.RANK_10.value}  |
        |  {CardName.TEN.value}  |
        |   {CardRank.RANK_10.value}  |
         -------
        """
    )
    picture_11: str = (
        f"""
         _______
        |       |
        |  {CardName.JACK.value} |
        |       |
         -------
        """
    )
    picture_12: str = (
        f"""
         _______
        |       |
        | {CardName.QUEEN.value} |
        |       |
         -------
        """
    )
    picture_13: str = (
        f"""
         _______
        |       |
        |  {CardName.KING.value} |
        |       |
         -------
        """
    )
    picture_14: str = (
        f"""
         _______
        |       |
        |  {CardName.ACE.value}  |
        |       |
         -------
        """
    )
