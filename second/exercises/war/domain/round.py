from collections import Counter

from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.player.player import Player


class Round:
    def __init__(self, players: list[Player]):
        self._players = players
        self._round_players = players.copy()

    def play(self):
        cards_to_win = self.players_choice_card()

        cards = cards_to_win
        while Round._is_war(cards):
            counter = Counter(card_to_win.rank for card_to_win in cards)
            players_in_war = [player for player in self._round_players if counter[player.current_card.rank] > 1]
            if self.is_war_value_bigger(players_in_war):
                self._round_players = players_in_war
                cards = self.players_choice_card()
                cards_to_win += cards
            else:
                break

        round_winner = self._get_round_winner()
        return round_winner, cards_to_win

    def is_war_value_bigger(self, players_in_war: list[Player]) -> bool:
        max_rank_in_war = max(set([player.current_card.rank.value for player in players_in_war]))
        max_rank_all = max([player.current_card.rank.value for player in self._round_players])
        return max_rank_in_war >= max_rank_all

    @staticmethod
    def _is_war(cards_to_win: list[Card]) -> bool:
        card_ranks = [card.rank.value for card in cards_to_win]
        return len(card_ranks) != len(set(card_ranks))

    def players_choice_card(self) -> list[Card]:
        round_cards: list[Card] = []

        for player in self._round_players:
            card = player.get_card()
            if card is None:
                self._players.remove(player)
                self._round_players.remove(player)
            else:
                round_cards.append(card)

        return round_cards

    def _get_round_winner(self):
        winner = None
        biggest_card = 0

        for player in self._round_players:
            player.display()
            if player.current_card is not None:
                player.current_card.display()
                rank = player.current_card.rank.value
                if rank > biggest_card:
                    biggest_card = rank
                    winner = player

        return winner
