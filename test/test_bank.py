import unittest

from account_and_bank import bank
from account_and_bank.account_exception import InvalidPinException, InvalidAmountException, InsufficientFundsException
from account_and_bank.bank import Bank
from account_and_bank.account import Account


class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank("bank")

    def test_new_bank_account_is_empty(self):
        account = self.bank.register_customer("Ara", "Ola", "8778")
        account_number = account.get_account_number()
        self.assertEqual(self.bank.check_balance(account_number, "8778"), 0)

    def test_deposit_to_account(self):
        account = self.bank.register_customer("Derin", "Sola", "1234")
        account_number = account.get_account_number()
        self.bank.deposit(account_number, 100)
        self.assertEqual(self.bank.check_balance(account_number, "1234"), 100)

    def test_withdraw_from_account(self):
        account = self.bank.register_customer("Preshy", "Colala", "5678")
        account_number = account.get_account_number()
        self.bank.deposit(account_number, 200)
        self.bank.withdraw(account_number, 50, "5678")
        self.assertEqual(self.bank.check_balance(account_number, "5678"), 150)

    def test_remove_account(self):
        account = self.bank.register_customer("Fadekemi", "Salako", "5678")
        account_number = account.get_account_number()
        self.bank.remove_account(account_number, "5678")
        self.assertIsNone(self.bank.find_account(account_number))

    def test_invalid_pin(self):
        account = self.bank.register_customer("Ayomi", "Tide", "1234")
        account_number = account.get_account_number()
        with self.assertRaises(InvalidPinException):
            self.bank.check_balance(account_number, "3454")
        with self.assertRaises(InvalidPinException):
            self.bank.withdraw(account_number, 50, "3453")