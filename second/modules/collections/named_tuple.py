from collections import namedtuple

Dog = namedtuple("Dog", ["name", "breed", "age"])
d = Dog("Aaa", "Bbb", 1)

print(d)
print(type(d))

print(d.breed)
print(d[1])
