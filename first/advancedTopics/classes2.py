class AgeException(Exception):
    # constructor
    def __init__(self, message):
        super().__init__(message)

    # toString() method
    def __str__(self):
        return f"Error {self.args[0]}"


class AccountHolder:
    # constructor
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.is_age_valid(age)
        self.age = age

    @staticmethod
    def is_age_valid(age):
        if age < 18:
            raise AgeException("age is invalid")


class BankAccount:
    # constructor
    def __init__(self, account_number: int, account_holder: AccountHolder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "invalid deposit amount"
        else:
            self.balance += amount
            return f"deposited {amount} €, balance is {self.balance} €"

    def withdraw(self, amount):
        if amount <= 0:
            return "invalid withdraw amount"
        elif self.balance < amount:
            return "invalid balance"
        else:
            self.balance -= amount
            return f"withdraw {amount} €, balance is {self.balance} €"

    def get_balance(self):
        return self.balance


holder = AccountHolder("Aa", "Bb", 33)
bank_account = BankAccount(1, holder)
print(bank_account.get_balance())
print(bank_account.deposit(100))
print(bank_account.withdraw(33))
print(bank_account.get_balance())
