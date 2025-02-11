def has_33(*args: int) -> bool:
    control_number = 3

    if args.count(3) < 2:
        return False

    max_index = len(args) - 1
    for index, number in enumerate(args):
        next_index = index + 1
        if number == control_number and next_index <= max_index and args[next_index] == control_number:
            return True

    return False


#####
print(has_33(1, 3, 3, 4, 5, 3))
print(has_33(1, 3, 1, 3))
print(has_33(3, 1, 3))
