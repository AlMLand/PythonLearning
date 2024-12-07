number: int = 1
maxNumber: int = 5
exitOption = "exit"


def is_end() -> bool:
    return userInput == exitOption


while number <= maxNumber:
    print(number)

    userInput = input("put 'exit' to end: ").lower()
    if is_end():
        print("successfully end 'while loop'")
        break

    number += 1
