import random
import uuid
from typing import Any

from account_and_bank.account import Account


class Bank:
    def __init__(self, name):
        self.__name = name
        self.__accounts = []

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number, amount, pin):
        account = self.find_account(account_number)
        account.withdraw(amount, pin)

    def transfer(self, depositor_account_number, receiver_account_number, amount, pin):
        depositor_account = self.find_account(depositor_account_number)
        receiver_account = self.find_account(receiver_account_number)

        depositor_account.withdraw(amount, pin)
        receiver_account.deposit(amount)

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)

        return account.check_balance(pin)

    def register_customer(self, first_name, last_name, pin):
        name = f"{first_name} {last_name}"
        number = self.generate_account_number()

        new_account = Account(number, name, pin)
        self.__accounts.append(new_account)

        return new_account

    def remove_account(self, account_number, pin):
        account = self.find_account(account_number)
        account.verify_pin(pin)

        self.__accounts.remove(account)

    def find_account(self, account_number):
        for account in self.__accounts:
            if account.number() == account_number:
                return account

        raise ValueError("Account does not exist")

    def get_name(self):
        return self.__name

    @staticmethod
    def generate_account_number():
        return random.randint(100000, 999999)

    @staticmethod
    def get_account_number(account: Account):
        return account.number()
