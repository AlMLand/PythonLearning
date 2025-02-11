def animal_crackers(word: str) -> bool:
    words = word.split()
    assert len(words) == 2

    return words[0][0] == words[1][0]


#####
print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Crazy Kangaroo"))
