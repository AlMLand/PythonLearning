from second.exercises.war.domain.deck.deck_builder import DeckBuilder
from second.exercises.war.domain.player.player import Player
from second.exercises.war.domain.player.player_builder import PlayerBuilder
from second.exercises.war.domain.round import Round


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
            round_winner, cards = Round(self._players).play()
            round_winner.put_cards(cards)
            print(
                f"the round winner is {round_winner.name}, he has {round_winner.play_set.current_cards_amount()} cards")

            if round_winner.play_set.is_max_possible_amount():
                print(f"the game winner is {round_winner.name}")
                break

            # input("start next round...")
