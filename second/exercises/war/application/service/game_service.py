from second.exercises.war.domain.deck.deck_builder import DeckBuilder
from second.exercises.war.domain.player.player import Player
from second.exercises.war.domain.player.player_builder import PlayerBuilder


class GameService:
    def __init__(self, player_count: int):
        self.player_count = player_count

    def start(self):
        players = self.prepare()
        self.start_session(players)

    def prepare(self) -> list[Player]:
        deck = DeckBuilder.get_start_deck()
        play_sets = deck.split(self.player_count)
        players = PlayerBuilder.create_players(play_sets)
        return players

    def start_session(self, players: list[Player]):
        while True:
            players_to_cards = [(player, player.get_card()) for player in players]

            biggest_card = 0
            winner_player = None
            for player, card in players_to_cards:
                if card is None:
                    players.remove(player)
                    print(f"player {player.name} dont have any card's and is going")
                    continue
                player.display()
                if card is not None:
                    card.display()
                    rank = card.rank.value
                    if rank > biggest_card:
                        biggest_card = rank
                        winner_player = player

            cards = [pc[1] for pc in players_to_cards if pc[1] is not None]
            winner_player.put_cards(cards)

            print(f"the round winner is {winner_player.name}")

            if winner_player.play_set.is_max_possible_amount():
                print(f"the game winner is {winner_player.name}")
                break

            # input("start next round...")
