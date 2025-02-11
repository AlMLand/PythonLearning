def lesser_of_two_evens(num1: int, num2: int) -> int:
    if is_even(num1) and is_even(num2):
        return min(num1, num2)
    else:
        return max(num1, num2)


def is_even(num) -> bool:
    return num % 2 == 0


#####
print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))
