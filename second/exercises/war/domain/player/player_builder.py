import random
import string

from second.exercises.war.domain.play_set import PlaySet
from second.exercises.war.domain.player.player import Player


class PlayerBuilder:
    @staticmethod
    def create_players(play_sets: [PlaySet]) -> list[Player]:
        return [Player(f"player_{random.choice(string.ascii_uppercase)}", play_set) for play_set in play_sets]
