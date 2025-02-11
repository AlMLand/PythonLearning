def summer_69(numbers: list[int]) -> int:
    start_exclude_range = 6
    end_exclude_range = 9

    if start_exclude_range not in numbers:
        return sum(numbers)

    new_numbers = []
    is_exclude_range = False
    for number in numbers:
        if number != start_exclude_range and not is_exclude_range:
            new_numbers.append(number)
        elif is_exclude_range and number == end_exclude_range:
            is_exclude_range = False
        else:
            is_exclude_range = True

    return sum(new_numbers)


#####
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
