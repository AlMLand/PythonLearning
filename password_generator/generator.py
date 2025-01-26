import random
import string


class Generator:

    def __init__(self, length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.digits = digits
        self.special_chars = special_chars

    def create_password(self) -> str | None:
        characters: str = ""

        if self.uppercase:
            characters += string.ascii_uppercase
        if self.lowercase:
            characters += string.ascii_lowercase
        if self.digits:
            characters += string.digits
        if self.special_chars:
            characters += string.punctuation

        if not characters:
            print("Error: at least one character type must be selected")
            return None

        password = self._create_with_length(characters)
        return password

    def _create_with_length(self, characters):
        return "".join(random.choice(characters) for _ in range(self.length))
