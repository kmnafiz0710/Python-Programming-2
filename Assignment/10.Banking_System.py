# Banking System.
class BankAccount:
    def __init__(self, amount):
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        print(f"{amount} has been deposited. Your current balance is {self.amount} tk.")

    def withdraw(self, amount):
        if 0 < amount <= self.amount:
            self.amount -= amount
            print(f"{amount} has been withdrawn. Your current balance is {self.amount} tk.")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return f"Your current account balance is {self.amount} tk."


account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
account.withdraw(300)
print(account.get_balance())
account.withdraw(1500)

