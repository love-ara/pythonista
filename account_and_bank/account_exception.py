class InvalidPinException(Exception):
    def _init_(self, message):
        super().__init__(message)


class InvalidAmountException(Exception):
    def _init_(self, message):
        super().__init__(message)


class InsufficientFundsException(Exception):
    def _init_(self, message):
        super().__init__(message)
