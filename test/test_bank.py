import unittest

from account_and_bank.Invalid_Amount import InvalidAmountException
from account_and_bank.Insufficient_fund import InsufficientFundsException
from account_and_bank.Invalid_pin import InvalidPinException
from account_and_bank.bank import Bank
from account_and_bank.account import Account


class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank("bank")
        self.account = self.bank.register_customer("Ara", "Ola", "1234")

    def test_new_bank_account_is_empty(self):
        account_number = self.account.number()
        self.assertEqual(self.bank.check_balance(account_number, "1234"), 0)

    def test_deposit_to_account(self):
        account_number = self.account.number()
        self.bank.deposit(account_number, 100)
        self.assertEqual(self.bank.check_balance(account_number, "1234"), 100)

    def test_withdraw_from_account(self):
        account_number = self.account.number()
        self.bank.deposit(account_number, 200)
        self.bank.withdraw(account_number, 50, "1234")
        self.assertEqual(self.bank.check_balance(account_number, "1234"), 150)

    def test_remove_account(self):
        account_number = self.account.number()
        self.bank.remove_account(account_number, "1234")
        try:
            self.bank.find_account(account_number)
        except ValueError as e:
            self.assertEqual("Account does not exist", str(e))

    def test_invalid_pin(self):
        account_number = self.account.number()
        self.bank.deposit(account_number, 9000)
        with self.assertRaises(InvalidPinException):
            self.bank.check_balance(account_number, "3454")
        with self.assertRaises(InvalidPinException):
            self.bank.withdraw(account_number, 500, "3453")

    def test_insufficient_funds(self):
        account_number = self.account.number()
        with self.assertRaises(InsufficientFundsException):
            self.bank.withdraw(account_number, 4000, "1234")
        with self.assertRaises(InsufficientFundsException):
            self.bank.withdraw(account_number, 250, "1234")

    def test_invalid_amounts(self):
        account_number = self.account.number()
        with self.assertRaises(InvalidAmountException):
            self.bank.deposit(account_number, -500)

        self.bank.deposit(account_number, 1000)
        with self.assertRaises(InvalidAmountException):
            self.bank.withdraw(account_number, -2, "1234")
