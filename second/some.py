# https://docs.python.org/3/library/index.html

statement = "print only the words starts with s in this sentence"
l = [x for x in statement.split() if x.startswith("s")]
print(l)

########
for x in range(0, 11):
    print(x)

########
l = [x for x in range(1, 51) if x % 3 == 0]
print(l)

########
statement = "print every word in this sentence that has an even number length"
required_word_length = len("even")
l = [word for word in statement.split() if len(word) == required_word_length]
print(l)

########
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print(f"{x} by 3 and by 5")
    elif x % 3 == 0:
        print(f"{x} only by 3")
    elif x % 5 == 0:
        print(f"{x} only by 5")
    else:
        print(f"{x} nothing")
########
statement = "create a list of the first letters of every word in this string"
l = [letter for word in statement.split() for index, letter in enumerate(word) if index == 0]
print(l)
