from first.ATMsimulation.user_service import get_user_balance, increase_user_balance, is_user_balance_sufficient, \
    decrease_user_balance

check_balance_id = "1"
deposit_money_id = "2"
withdraw_money_id = "3"
exit_id = "4"

menu_items = (
    {check_balance_id: "Check Balance"},
    {deposit_money_id: "Deposit Money"},
    {withdraw_money_id: "Withdraw Money"},
    {exit_id: "Exit"}
)


def print_menu_items_and_get_user_choice():
    print("Main menu:")
    for menu_item in menu_items:
        for key, value in menu_item.items():
            print(f"{key}. {value}")
    return input("Enter your Choice: ")


def is_valid_menu_choice(current_menu_choice: str) -> bool:
    if current_menu_choice in [check_balance_id, deposit_money_id, withdraw_money_id, exit_id]:
        return True
    else:
        return False


def handle_menu_item(menu_item_id: str, current_user: dict[str, int] | dict[str, int]):
    if menu_item_id == check_balance_id:
        print(f"Your balance: {get_user_balance(current_user)}")
    elif menu_item_id == deposit_money_id:
        deposit_amount = float(input("How many want you to deposit: "))
        increase_user_balance(current_user, deposit_amount)
        print(f"Your new balance: {get_user_balance(current_user)}, deposit amount: {deposit_amount}")
    elif menu_item_id == withdraw_money_id:
        withdraw_amount = float(input("How many want you to withdraw: "))
        if is_user_balance_sufficient(current_user, withdraw_amount):
            decrease_user_balance(current_user, withdraw_amount)
            print(f"Your new balance: {get_user_balance(current_user)}, withdraw amount: {withdraw_amount}")
        else:
            print(f"Your balance is not sufficient")
    else:
        print("Goodbye")
