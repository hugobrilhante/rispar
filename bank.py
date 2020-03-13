import csv
from decimal import Decimal
from typing import List


class Account:
    assessment: Decimal = Decimal(500)

    def __init__(self, account_number: int, balance: int):
        self.account_number: int = int(account_number)
        self.balance: Decimal = Decimal(balance)

    def deposit(self, value: Decimal):
        self.balance += value

    def debit(self, value: Decimal):
        self.balance += value
        if self.balance < 0:
            self.balance -= self.assessment


class Transaction:

    def __init__(self, account_number: int, value: int):
        self.account_number: int = int(account_number)
        self.value: Decimal = Decimal(value)


class Bank:

    def __init__(self, account_file: str, transaction_file: str):
        self.accounts: dict = {}
        self.transactions: dict = {}

        with open(account_file) as f:
            accounts = csv.reader(f, delimiter=',')
            for a, b in accounts:
                self.register_account(Account(a, b))

        with open(transaction_file) as f:
            transactions = csv.reader(f, delimiter=',')
            for a, v in transactions:
                self.register_transaction(Transaction(a, v))

    def calculate_balances(self) -> None:
        for account_number, account in self.accounts.items():
            transactions = self.get_transactions(account_number)
            for transaction in transactions:
                if transaction.value > 0:
                    account.deposit(transaction.value)
                else:
                    account.debit(transaction.value)

    def get_account(self, account_number: int) -> Account:
        return self.accounts[account_number]

    def get_balances(self) -> None:
        for account in self.accounts.values():
            print(account.account_number, account.balance, sep=',')

    def get_transactions(self, account_number: int) -> List[Transaction]:
        return self.transactions[account_number]

    def register_account(self, account: Account) -> None:
        self.accounts[account.account_number] = account

    def register_transaction(self, transaction: Transaction) -> None:
        try:
            self.transactions[transaction.account_number]
        except KeyError:
            self.transactions[transaction.account_number] = [transaction]
        else:
            self.transactions[transaction.account_number].append(transaction)
