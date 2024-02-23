from account import Account
from decimal import Decimal

account1 = Account('John Green', Decimal('50.00'))
account1.withdraw(Decimal('20.00'))
print(account1.balance)