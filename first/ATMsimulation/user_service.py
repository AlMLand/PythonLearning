balance_key = "balance"
name_key = "name"
pin_key = "pin"
id_key = "id"

user1 = {name_key: "Aaa", balance_key: 1000, pin_key: 111, "id": 1}
user2 = {name_key: "Bbb", balance_key: 200, pin_key: 222, "id": 2}
users = [user1, user2]


def get_current_user_by_name_and_pin(user_name: str, user_pin: int):
    for user in users:
        if is_user_name_and_pin_valid(user_name, user_pin):
            return user


def is_user_name_and_pin_valid(user_name: str, user_pin: int):
    for user in users:
        if user[name_key] == user_name and user[pin_key] == user_pin:
            return True
    return False


def decrease_user_balance(current_user: dict[str, int] | dict[str, int], withdraw_amount: float):
    current_user[balance_key] -= withdraw_amount


def is_user_balance_sufficient(current_user: dict[str, int] | dict[str, int], withdraw_amount: float):
    return current_user[balance_key] >= withdraw_amount


def increase_user_balance(current_user: dict[str, int] | dict[str, int], deposit_amount: float):
    current_user[balance_key] += deposit_amount


def get_user_balance(current_user: dict[str, int] | dict[str, int]):
    return current_user[balance_key]
