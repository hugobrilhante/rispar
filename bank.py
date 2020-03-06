from decimal import Decimal


class Account:
    assessment: Decimal = Decimal(5)

    def __init__(self, account_number: int, balance: int):
        self.account_number: int = int(account_number)
        self.balance: Decimal = Decimal(balance)

    def deposit(self, value: Decimal):
        self.balance += value

    def debit(self, value: Decimal):
        self.balance += value - self.assessment


class Transaction:

    def __init__(self, account_number: int, value: int):
        self.account_number: int = int(account_number)
        self.value: Decimal = Decimal(value)



