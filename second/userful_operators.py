# range
from random import shuffle, randint

for i in range(4):
    print(i)
for i in range(len("asd"), 6):
    print(i)

list_int = list(range(10))
print(list_int)

# enumerate
word = "Alex"
for i in enumerate(word):
    print(i)

# zip, do list of tuples, length is a shorts list, other elements are ignored
l1 = ["a", "b", "c"]
l2 = [1, 2, 3, 4, 5]
l3 = [True, False, True, False]
for i in zip(l1, l2, l3):
    print(i)
# do just two lists to one list
for i in l1 + l2:
    print(i)
# list of typles
l = list(zip(l1, l2, l3))
print(l)

# in, checks - like contains()
word = "asdf"
result = "d" in word
print(result)
aa = "key1" in {"key1": "v1", "key2": "v2"}
print(aa)
vv = "v2" in {"key1": "v1", "key2": "v2"}.values()
print(vv)

# shuffle, mischt die elemente
ll = [1, 2, 3, 4, 5]
shuffle(ll)
print(ll)
# random int in the range
print(randint(0, 100))
