import random
import uuid
from account_and_bank.account import Account


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number, amount, pin):
        account = self.find_account(account_number)
        account.withdraw(amount, pin)

    def transfer(self, depositor_account_number, receiver_account_number, amount, pin):
        depositor_account = self.find_account(depositor_account_number)
        receiver_account = self.find_account(receiver_account_number)
        if depositor_account and receiver_account:
            depositor_account.verify_pin(pin)
            if depositor_account.check_balance(pin) >= amount:
                depositor_account.withdraw(amount, pin)
                receiver_account.deposit(amount)

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)
        if account:
            balance = account.check_balance(pin)
            if balance == 0:
                return 0
            return balance
        return -1

    def register_customer(self, first_name, last_name, pin):
        name = f"{first_name}+ " " + {last_name}"
        number = self.get_account_number()
        new_account = Account(number, name, pin)
        self.accounts.append(new_account)
        return new_account

    def remove_account(self, account_number, pin):
        account = self.find_account(account_number)
        if pin == pin:
            self.accounts.remove(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def find_accounts_by_name(self, name):
        found_accounts = []
        for account in self.accounts:
            if account.get_name() == name:
                found_accounts.append(account)
        return found_accounts

    def get_name(self):
        return self.name

    def verify_pin(self, entered_pin):
        if self.pin != entered_pin:
            raise ValueError("Incorrect pin")

    def generate_account_number(self):
        return random.randint(100000, 999999)

    def get_account_number(self):
        return self.generate_account_number()
