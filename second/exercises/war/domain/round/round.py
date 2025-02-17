from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.player.player import Player
from second.exercises.war.domain.round.war import War


class Round:
    def __init__(self, players: list[Player]):
        self._players = players
        self._round_players = players.copy()

    def play(self):
        cards_to_win = self._players_choice_card()

        cards = cards_to_win
        while War.is_war(cards):
            players_in_war = War.get_players_in_war(self._round_players, cards)

            if War.is_war_rank_biggest(self._round_players, players_in_war):
                self._round_players = players_in_war
                cards = self._players_choice_card()
                cards_to_win += cards
            else:
                break

        round_winner = self._get_round_winner()
        round_winner.put_cards(cards_to_win)
        print(f"the round winner is {round_winner.name}, he has {round_winner.play_set.current_cards_amount()} cards")

        return round_winner

    def _players_choice_card(self) -> list[Card]:
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
        max_rank = 0
        winner = None

        for player in self._round_players:
            player.display()
            card = player.current_card
            if card is not None:
                card.display()
                rank = card.rank.value
                if rank > max_rank:
                    max_rank = rank
                    winner = player

        return winner
