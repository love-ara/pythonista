import unittest

from account_and_bank.account import Account
from account_and_bank.Invalid_Amount import InvalidAmountException
from account_and_bank.Insufficient_fund import InsufficientFundsException
from account_and_bank.Invalid_pin import InvalidPinException


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("number", "name", "3454")

    def test_account_is_empty(self):
        self.assertEqual(self.account.check_balance(), 0)

    def test_account_can_deposit(self):
        self.account.deposit(5000.0)
        self.assertEqual(self.account.check_balance(), 5000.0)

    def test_account_can_withdraw(self):
        self.account.deposit(8000)
        self.account.withdraw(2000, "3454")
        self.assertEqual(self.account.check_balance(), 6000.0)

    def test_withdraw_amount_cannot_exceed_balance(self):
        self.account.deposit(8000.0)
        with self.assertRaises(InsufficientFundsException):
            self.account.withdraw(9000.0, "3454")

    def test_deposit_amount_must_be_greater_than_zero(self):
        with self.assertRaises(InvalidAmountException):
            self.account.deposit(0.0)
        with self.assertRaises(InvalidAmountException):
            self.account.deposit(-1.0)

    def test_withdraw_amount_must_be_greater_than_zero(self):
        with self.assertRaises(InvalidAmountException):
            self.account.withdraw(0.0, "3454")
        with self.assertRaises(InvalidAmountException):
            self.account.withdraw(-1.0, "3454")
