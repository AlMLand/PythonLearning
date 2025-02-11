# VARIANT 1
l = []
for i in "asdf":
    l.append(i)
print(l)

# VARIANT 2, obe peremennie (proizwolnoe imja) dolzhni naziwatsja odinakowo
l = [letter for letter in "asdf"]
print(l)

# mozhno menjat wremennuju peremennuju
l = [f"{letter} - wer" for letter in "asdf"]
print(l)
# mozhno dobawit if statement, esli if statement is true -> dobawit w list
l = [x + "c" for x in "asdf" if x == "a" or x == "d"]
print(l)
l = [x + "xxx" if x == "a" or x == "d" else "AAA" for x in "asdf"]
print(l)

l = [x for x in range(0, 11)]
print(l)
# mozhno menjat wremennuju peremennuju
l = [f"{x} - wer" for x in range(11)]
print(l)
# mozhno dobawit if statement, esli if statement is true -> dobawit w list
l = [x for x in range(11) if x % 2 == 0]
print(l)

#############################################################################################

l = []
for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        l.append(x * y)
print(l)
# the same in one line
l = [x * y for y in [100, 200, 300] for x in [2, 4, 6]]
print(l)
