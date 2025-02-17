from collections import Counter

from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.player.player import Player


class Round:
    def __init__(self, players: list[Player]):
        self._players = players.copy()

    def play(self):
        players_to_cards = self.players_choice_card()
        cards_to_win = self.get_cards_to_win(players_to_cards)

        while Round._is_war(players_to_cards):
            counter = Counter(player_to_card[1].rank for player_to_card in players_to_cards)
            players_in_war = [player_to_card[0] for player_to_card in players_to_cards
                              if counter[player_to_card[1].rank] > 1]
            if self.is_war_value_bigger(players_in_war):
                self._players = players_in_war
                players_to_cards = self.players_choice_card()
                cards_to_win += self.get_cards_to_win(players_to_cards)

        round_winner = Round._get_round_winner(players_to_cards)
        return round_winner, cards_to_win

    def is_war_value_bigger(self, players_in_war: list[Player]) -> bool:
        max_rank_in_war = max(set([player.current_card.rank.value for player in players_in_war]))
        max_rank_all = max([player.current_card.rank.value for player in self._players])
        return max_rank_in_war >= max_rank_all

    @staticmethod
    def get_cards_to_win(players_to_cards: list[tuple[Player, Card]]) -> list[Card]:
        return [player_to_card[1] for player_to_card in players_to_cards]

    @staticmethod
    def _is_war(players_to_cards: list[tuple[Player, Card]]) -> bool:
        card_ranks = list(map(lambda player_to_card: player_to_card[1].rank, players_to_cards))
        return len(card_ranks) != len(set(card_ranks))

    def players_choice_card(self) -> list[(Player, Card)]:
        return list(filter(lambda player_to_card: player_to_card[1] is not None,
                           [(player, player.get_card()) for player in self._players]))

    @staticmethod
    def _get_round_winner(players_to_round_cards: list[tuple[Player, Card]]):
        winner = None
        biggest_card = 0

        for player, card in players_to_round_cards:
            player.display()
            card.display()
            rank = card.rank.value
            if rank > biggest_card:
                biggest_card = rank
                winner = player

        return winner
