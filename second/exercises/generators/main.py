### 1
import random


def generate_squares(n: int):
    for number in range(n):
        yield number ** 2


print(list(generate_squares(10)))


### 2
def generate_random(amount: int, start: int, end: int):
    for i in range(amount):
        yield random.randint(start, end)


print(list(generate_random(12, 1, 10)))

### 3
s = "Alex"
for e in iter(s):
    print(e)

### 4
