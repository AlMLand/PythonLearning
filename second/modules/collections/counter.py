from collections import Counter


def get_counter(collection):
    return Counter(collection)


print(get_counter([1, 1, 1, 1, 3, 3, 3, 5, 5, 5, 5, 5, ]))
print(get_counter("strrr"))
print(get_counter(["aa", "kl", "kl", "as", "aa", "kl"]))
