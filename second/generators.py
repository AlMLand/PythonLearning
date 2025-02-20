def create_cubes_1(n: int) -> list[int]:
    return [number ** 3 for number in range(n)]


def create_cubes_2(n: int):
    for number in range(n):
        yield number ** 3


print(create_cubes_1(10))
print(list(create_cubes_2(10)))
print(create_cubes_2(10))


###############

def generate_fibonaci(n: int):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for i in generate_fibonaci(10):
    print(i)


###############

def simple_generator(n: int):
    for number in range(n):
        yield number


generator = simple_generator(3)

print(next(generator))
print(next(generator))
print(next(generator))
