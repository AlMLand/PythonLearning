print("give two numbers and i'll divide them")
print("enter 'q' to quit")

while True:
    first_number = input("first number: ")
    if first_number == 'q':
        print("goodbye")
        break
    second_number = input("second number: ")
    if second_number == 'q':
        print("goodbye")
        break
    try:
        result = float(first_number) / float(second_number)
        print(f"result: {result}")
    except ValueError:
        print("numbers only")
    except ZeroDivisionError:
        print("can't divide by 0")
