from second.exercises.war.domain.card.card import Card
from second.exercises.war.domain.deck.deck_builder import DeckBuilder
from second.exercises.war.domain.player.player import Player
from second.exercises.war.domain.player.player_builder import PlayerBuilder


class GameService:
    _players: list[Player]

    def __init__(self, player_count: int):
        self.player_count = player_count

    def start(self):
        self._players = self._prepare()
        self._start_session()

    def _prepare(self) -> list[Player]:
        deck = DeckBuilder.get_start_deck()
        play_sets = deck.split(self.player_count)
        players = PlayerBuilder.create_players(play_sets)
        return players

    def _start_session(self):
        while True:
            players_to_round_cards = [(player, player.get_card()) for player in self._players]

            round_winner = self._get_round_winner(players_to_round_cards)
            cards = [pc[1] for pc in players_to_round_cards if pc[1] is not None]
            round_winner.put_cards(cards)
            print(
                f"the round winner is {round_winner.name}, he has {round_winner.play_set.current_cards_amount()} cards")

            if round_winner.play_set.is_max_possible_amount():
                print(f"the game winner is {round_winner.name}")
                break

            # input("start next round...")

    def _get_round_winner(self, players_to_round_cards: list[tuple[Player, Card]]):
        winner = None
        biggest_card = 0

        for player, card in players_to_round_cards:
            if card is None:
                self._players.remove(player)
                print(f"player {player.name} dont have any card's and is going")
                continue
            player.display()
            if card is not None:
                card.display()
                rank = card.rank.value
                if rank > biggest_card:
                    biggest_card = rank
                    winner = player

        return winner
