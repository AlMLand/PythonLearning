import datetime


def calculate_low_and_upper_cases():
    print(f"Hallo user, today is {datetime.date.today()}")

    current = input("You can give my a hind and you get a info: ")

    lower_case = len([char for char in current if char.islower()])
    upper_case = len([char for char in current if char.isupper()])
    digits = len([char for char in current if char.isdigit()])

    print(f"your have {lower_case} letter in lower case, {upper_case} in upper case and {digits} digits")


calculate_low_and_upper_cases()
