from account_and_bank.account_exception import InvalidPinException, InsufficientFundsException, InvalidAmountException


def _validate_amount(amount):
    if amount <= 0:
        raise InvalidAmountException("Amount should be greater than zero")


class Account:
    def __init__(self, number, name, pin):
        self.name = name
        self.number = number
        self.pin = pin
        self.balance = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def _set_pin(self, pin):
        self.pin = pin

    def get_pin(self):
        return self.pin

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    @staticmethod
    def _validate_pin(self, pin):
        if not pin.isdigit():
            raise InvalidPinException("Pin should have only digits")
        if len(pin) != 4:
            raise InvalidPinException("PIN should be four digits long")


    def deposit(self, amount):
        _validate_amount(amount)
        self.balance += amount

    def withdraw(self, amount, pin):
        self._verify_pin(pin)
        _validate_amount(amount)
        self._check_for_sufficient_balance(amount)
        self.balance -= amount

    def _verify_pin(self, entered_pin):
        self._validate_pin(self, entered_pin)
        if self.pin != entered_pin:
            raise InvalidPinException("Incorrect pin")

    def _check_for_sufficient_balance(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds. Top up account")

    def check_balance(self, pin):
        self._verify_pin(pin)
        return self.balance

    def get_account_number(self):
        return self.number
