class InvalidPinException(Exception):
    def _init_(self, message):
        super()._init_(message)

class InvalidAmountException(Exception):
    def _init_(self, message):
        super()._init_(message)

class InsufficientFundsException(Exception):
    def _init_(self, message):
        super()._init_(message)
