def spy_game(numbers: list[int]) -> bool:
    required_sequence = "007"

    null = 0
    seven = 7

    if seven not in numbers or numbers.count(null) < 2:
        return False

    new_numbers = [number for number in numbers if number in [null, seven]]
    new_numbers_as_str = "".join(map(str, new_numbers))

    return required_sequence in new_numbers_as_str


#####
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
