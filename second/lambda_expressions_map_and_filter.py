##### map


def square(num):
    return num ** 2


numbers = [1, 2, 3, 4, 5]

##
for item in map(square, numbers):
    print(item)
##
result = list(map(square, numbers))
print(result)
##
result = list(map(lambda number: number ** 2, numbers))
print(f"result {result}")

####

names = ["Aaa", "Bbb", "Ccc", "Dd"]


def splicer(text: str):
    if len(text) % 2 == 0:
        return "even"
    else:
        return text[0]


##
result = list(map(splicer, names))
print(result)
##
result = list(map(lambda text: "even" if len(text) % 2 == 0 else text[0], names))
print(f"result: {result}")


##### filter

def is_even(num: int) -> bool:
    return num % 2 == 0


##
for i in filter(is_even, numbers):
    print(i)
##
result = list(filter(is_even, numbers))
print(result)
##
result = list(filter(lambda num: num % 2 == 0, numbers))
print(result)
