import math
import string
from functools import reduce


##### 1
def volume(radius: int) -> float:
    return (4 / 3) * math.pi * math.pow(radius, 3)


print(volume(2))


###### 2
def is_in_range(number: int, start: int, end: int) -> bool:
    return number in range(start, end + 1)


print(is_in_range(5, 2, 7))
print(is_in_range(11, 1, 10))


##### 4
def as_unique(collection) -> set[int]:
    return set(collection)


print(as_unique([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


##### 5
def multiply(collection: list[int]) -> int:
    return reduce(lambda r, n: n * r, collection)


print(multiply([1, 2, 3, -4]))


##### 6
def is_palindrome(word: str) -> bool:
    if word.strip() == "":
        return False

    return word == word[::-1]


print(is_palindrome("     \n     "))
print(is_palindrome("helleh"))
print(is_palindrome("hellehd"))


##### 7
def is_pangram(text: str) -> bool:
    text = text.lower()
    alphabet = list(string.ascii_lowercase)

    for letter in text:
        if letter in alphabet:
            alphabet.remove(letter)

    return len(alphabet) == 0


print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("The quick brown fox jumps over the dog"))
