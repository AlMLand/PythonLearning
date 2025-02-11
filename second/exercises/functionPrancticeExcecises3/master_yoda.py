def master_yoda(sentence: str) -> str:
    split: list[str] = sentence.split()
    split.reverse()

    return " ".join(split)


#####
print(master_yoda("I am home"))
print(master_yoda("We are ready"))
