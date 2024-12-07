letters: list[str] = ["Aa", "Bb", "Cc", "Dd"]

print(letters)
print(letters[0])

# last element
print(letters[-1])

# for last element
print(letters[-2])

# edit some value
letters[1] = "Ee"
print(letters)

# all elements from start index until end index (end index not including)
subLetters = letters[1:2]
print(subLetters)

# add a new element
subLetters.append("Ff")
print(subLetters)

# remove a element
subLetters.pop(0)
print(subLetters)
