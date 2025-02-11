def paper_doll(text: str) -> str:
    new_text = ""
    for letter in text:
        new_text += letter * 3

    return new_text


#####
print(paper_doll("Hello"))
print(paper_doll("Mississippi"))
