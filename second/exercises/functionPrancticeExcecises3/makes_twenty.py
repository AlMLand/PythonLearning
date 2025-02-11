def makes_twenty(num1: int, num2: int) -> bool:
    twenty = 20
    return num1 == twenty or num2 == twenty or num1 + num2 == twenty


#####
print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))
