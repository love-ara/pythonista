from decimal import Decimal

class Account:
    def __init__(self, name: str, balance: Decimal):
        self.__name = name
        self.balance = balance

    @property
    def balance(self):
        return self.balance


    @balance.setter
    def balance(self, amount: Decimal):
        if amount < Decimal(0.00):
            raise ValueError("Invalid balance for account")
        self.balance += amount

    def __str__(self):
        return f"Name: {self.__name} Balance: {self.balance}"

    # def deposit(self, amount: Decimal):
    #     if amount <= Decimal(0.00):
    #         raise ValueError("Amount must be greater than zero")
    #     self.__balance += amount


account = Account("Miriam", Decimal(-10))
print(account)
#account.balance = 1000
#print(account.balance)





