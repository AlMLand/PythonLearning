class Account:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def deposit(self, amount: int):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError(f"current amount {amount} is not valid")

    def withdraw(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError(f"current amount {amount} is bigger as balance {self.balance}")

    def __repr__(self):
        return f"Account owner: {self.name}\nAccount balance: {self.balance}"


a = Account("aaa", 100)
print(a)
a.deposit(50)
print(a)
a.withdraw(75)
print(a)
a.withdraw(5000)
print(a)
