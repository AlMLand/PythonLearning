from hangman.attempt import Attempt
from hangman.random_word import RandomWord
from hangman.state import hangman_states

print("welcome to hangman\n")

attempt = Attempt(6)
random_word = RandomWord()


def display_progress():
    attempt.display_attempts()
    print(hangman_states[attempt.count])
    random_word.display_hidden_word()


while attempt.is_attempt_available() and random_word.is_hidden_symbol_present():
    display_progress()
    guess: str = input("guess a letter: ").lower()

    if guess in random_word.word:
        random_word.set_guess_letters(guess)
    else:
        print("incorrect, try again")
        attempt.decrease_attempts()

    if not random_word.is_hidden_symbol_present():
        display_progress()
        print("congratulations, you won")
        break

if not attempt.is_attempt_available():
    display_progress()
    print(f"sorry, you lost, the word was: {random_word.word}")
