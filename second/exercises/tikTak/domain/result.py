class Result:
    def __init__(self, winner_name: str, is_game_board_free_space_available: bool):
        self.winner_name = winner_name
        self.is_game_board_free_space_available = is_game_board_free_space_available

    def __repr__(self):
        return (f"Result [winner_name: {self.winner_name}, "
                f"is_game_board_free_space_available: {self.is_game_board_free_space_available}]")
