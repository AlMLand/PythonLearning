def black_jack(num1: int, num2: int, num3: int):
    required_range = range(1, 12)
    assert num1 in required_range and num2 in required_range and num3 in required_range

    critical_boarder = 21
    numbers = [num1, num2, num3]

    nums_sum = sum(numbers)
    if nums_sum <= critical_boarder:
        return nums_sum

    if 11 in numbers:
        nums_sum -= 10
        if nums_sum <= critical_boarder:
            return nums_sum
    else:
        return "BUST"


#####
print(black_jack(5, 6, 7))
print(black_jack(9, 9, 9))
print(black_jack(9, 9, 11))
