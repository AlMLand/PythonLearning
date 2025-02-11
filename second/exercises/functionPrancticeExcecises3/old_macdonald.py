def capitalize_first_and_fourth_letter(word: str) -> str:
    assert len(word) >= 4

    prefix = word[:3]
    suffix = word[3:]

    return prefix.capitalize() + suffix.capitalize()

    # capitalized_word = ""
    # for index, letter in enumerate(word):
    #     if index == 0 or index == 3:
    #         capitalized_word += letter.upper()
    #     else:
    #         capitalized_word += letter
    #
    # return capitalized_word


#####
print(capitalize_first_and_fourth_letter("macdonald"))
