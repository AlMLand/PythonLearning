numbers: list[int] = [1, 2, 3, 4]
newNumbers: list[int] = []

for number in numbers:
    print(number)
    newNumbers.append(number + 1)

print(newNumbers)
