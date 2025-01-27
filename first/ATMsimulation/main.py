from first.ATMsimulation.atm_menu import handle_menu_item, is_valid_menu_choice, print_menu_items_and_get_user_choice
from first.ATMsimulation.user_service import get_current_user_by_name_and_pin

is_atm_activated = False

print("Welcome to the simple ATM simulator")

user_name: str = input("Please enter your Name: ")
user_pin: int = int(input("Please enter your PIN: "))

current_user = get_current_user_by_name_and_pin(user_name, user_pin)
if current_user is not None:
    is_atm_activated = True


def choice_handling(current_menu_choice: str):
    if is_valid_menu_choice(current_menu_choice):
        handle_menu_item(current_menu_choice, current_user)
        global is_atm_activated
        is_atm_activated = False
    else:
        print("This choice dont exists, please try again")
        choice_handling(print_menu_items_and_get_user_choice())


if is_atm_activated:
    choice_handling(print_menu_items_and_get_user_choice())
else:
    print("You Name or PIN is not valid")
