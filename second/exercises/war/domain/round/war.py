from collections import Counter

from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.player.player import Player


class War:

    @staticmethod
    def is_war(cards_to_win: list[Card]) -> bool:
        card_ranks = [card.rank.value for card in cards_to_win]

        return len(card_ranks) != len(set(card_ranks))

    @staticmethod
    def get_players_in_war(round_players: list[Player], cards: list[Card]):
        counter = Counter(card_to_win.rank for card_to_win in cards)

        return [player for player in round_players if counter[player.current_card.rank] > 1]

    @staticmethod
    def is_war_rank_biggest(round_players: list[Player], players_in_war: list[Player]) -> bool:
        max_rank_in_war = max(set([player.current_card.rank.value for player in players_in_war]))
        max_rank_all = max([player.current_card.rank.value for player in round_players])

        return max_rank_in_war >= max_rank_all
