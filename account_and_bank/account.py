from account_and_bank.Invalid_Amount import InvalidAmountException
from account_and_bank.Insufficient_fund import InsufficientFundsException
from account_and_bank.Invalid_pin import InvalidPinException

class Account:
    def __init__(self, number, name, pin):
        self._validate_pin(pin)

        self.__name = name
        self.__number = number
        self.__pin = pin
        self.__balance = 0

    def name(self):
        return self.__name

    def check_balance(self, pin):
        self.verify_pin(pin)
        return self.__balance

    def number(self):
        return self.__number

    @staticmethod
    def _validate_pin(pin):
        if not pin.isdigit():
            raise InvalidPinException("Pin should have only digits")
        if len(pin) != 4:
            raise InvalidPinException("PIN should be four digits long")

    @staticmethod
    def _validate_amount(amount):
        if amount <= 0:
            raise InvalidAmountException("Amount should be greater than zero")

    def deposit(self, amount):
        self._validate_amount(amount)

        self.__balance += amount

    def withdraw(self, amount, pin):
        self._validate_funds(amount)
        self._validate_amount(amount)

        self.__balance -= amount

    def validate(self, amount, pin):
        self.verify_pin(pin)
        self._validate_amount(amount)
        self._validate_funds(amount)

    def verify_pin(self, entered_pin):
        if self.__pin != entered_pin:
            raise InvalidPinException("Incorrect pin")

    def _validate_funds(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsException("Insufficient funds. Top up account")

    def __repr__(self):
        return f"Account name: {self.__name}\nBalance: {self.__balance}"
