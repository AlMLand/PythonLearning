def check_even_numbers(numbers: list[int]) -> {}:
    return {(index, number) for index, number in enumerate(numbers) if number % 2 == 0}


print(check_even_numbers([20, 3, 3, 41]))

#####

ints = {("aaa", 11), ("bbb", 22), ("ccc", 33), ("ddd", 10)}
for k, v in ints:  # tuple unpacking
    print(f"my: {k}, {v}")


def get_most(objects) -> ():
    temp_key = None
    temp_value = 0

    for key, value in objects:
        if value > temp_value:
            temp_key = key
            temp_value = value
        else:
            pass

    return temp_key, temp_value


current_key, current_value = get_most(ints)
print(f"current key: {current_key}, current value: {current_value}")

#####
