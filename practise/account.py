from decimal import Decimal
class Account:
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance


    def deposit(self, amount: Decimal):
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive')
        self.balance += amount

    def withdraw(self, amount: Decimal):
        if amount > self.balance:
            raise ValueError('Amount must be less than or equal to balance')
        self.balance -= amount











