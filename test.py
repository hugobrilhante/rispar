import csv
import unittest
from decimal import Decimal
from io import StringIO
from unittest.mock import patch

from bank import Account, Bank, Transaction


class BankTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank()
        with open('accounts.csv') as f:
            accounts = csv.reader(f, delimiter=',')
            for a, b in accounts:
                self.account = Account(a, b)
                self.bank.register_account(self.account)

        with open('transactions.csv') as f:
            transactions = csv.reader(f, delimiter=',')
            for a, v in transactions:
                self.transaction = Transaction(a, v)
                self.bank.register_transaction(self.transaction)

    def test_get_account(self) -> None:
        self.assertIsInstance(self.bank.get_account(self.account.account_number), Account)

    def test_get_transactions(self) -> None:
        self.assertEqual(len(self.bank.get_transactions(self.transaction.account_number)), 2)

    def test_register_accounts(self) -> None:
        self.assertEqual(len(self.bank.accounts.items()), 1)

    def test_register_transactions(self) -> None:
        self.assertEqual(len(self.bank.transactions.items()), 1)

    def test_calculate_transactions(self) -> None:
        self.bank.calculate_balances()
        self.assertEqual(self.account.balance, Decimal(132423))

    def test_get_balance(self) -> None:
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.bank.get_balances()
            self.assertEqual(stdout.getvalue().strip(), '345,14428')


if __name__ == '__main__':
    unittest.main()
