# class CardPicture(Enum): picture: str
from second.exercises.war.application.service.game_service import GameService

# class CardName(Enum): name: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace

# class CardRank(Enum): rank: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

# class CardSuit(Enum): name -> acorn, leave, heart, bell

# class Card: suit: Suit, name: CardName, rank: Rank, picture: CardPicture

# class SuitSet: suit: Suit, cards: list[Card]

# class Deck: deck_cards: {suit_set_acorn: SuitSet, suit_set_leave: SuitSet, suit_set_heart: SuitSet, suit_set_bell: SuitSet}
#       def randomize_deck(self):

# class PlaySet: cards: list[Card]
#       def get_random(self): -> get card is to delete it from cards

# class Player(ABC): name: str, play_set: PlaySet
#       def get_random(self):

# class GameService:
#   def start(user_count)
#   def prepare(user_count) -> create deck, create users from split
#   def start_session(users) -> in loop:
#                           def do_users_step()
#                           def compare_user_cards()
#                           def put_cards_to_winner()
#                           def print_local_winner_name_cards()
#                           def check_for_global_win() - def print_global_winner_name() - stop game
#                           def wait_for_input_to_go_further()
#
# is_war()
#   true but another value is bigger -> ignore
#   true and another value is smaller -> do that
#       only players in war -> get more cards
#       check for war
#   mozhet War class wwesti
#
GameService(3).start()
