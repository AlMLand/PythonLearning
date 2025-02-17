from second.exercises.war.domain.deck.deck_builder import DeckBuilder
from second.exercises.war.domain.player.player import Player
from second.exercises.war.domain.player.player_builder import PlayerBuilder
from second.exercises.war.domain.round.round import Round


class GameService:
    def __init__(self, player_count: int):
        self.player_count = player_count
        self.players = self._prepare()

    def _prepare(self) -> list[Player]:
        deck = DeckBuilder.get_start_deck()
        play_sets = deck.split(self.player_count)
        players = PlayerBuilder.create_players(play_sets)

        return players

    def start(self):
        while True:
            round_winner = Round(self.players).play()

            if round_winner.play_set.is_max_possible_amount():
                print(f"the game winner is {round_winner.name}")
                break

            # input("start next round, press the Enter button...")
