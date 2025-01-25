import random
from dataclasses import dataclass


@dataclass
class RandomWord:

    def __init__(self):
        words: tuple[str, str, str] = ("java", "kotlin", "scala")

        self.hidden_symbol: str = "_"
        self.word = random.choice(words)
        self.hidden_word = [self.hidden_symbol for _ in self.word]

    def set_guess_letters(self, guess: str):
        for index, letter in enumerate(self.word):
            if letter == guess and self.is_letter_hidden(index):
                self.set_letter(index, letter)

    def is_letter_hidden(self, index: int) -> bool:
        return self.hidden_word[index] == self.hidden_symbol

    def set_letter(self, index: int, letter: str):
        self.hidden_word[index] = letter

    def is_hidden_symbol_present(self) -> bool:
        return self.hidden_symbol in self.hidden_word

    def display_hidden_word(self):
        delimiter: str = " "
        hidden_word_to_display: str = delimiter.join(self.hidden_word)
        print(hidden_word_to_display)

    def display_word(self):
        print(self.word)
