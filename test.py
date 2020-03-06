import unittest
from decimal import Decimal
from io import StringIO
from unittest.mock import patch

from bank import Account, Bank


class BankTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank('accounts.csv', 'transactions.csv')

    def test_get_account(self) -> None:
        self.assertIsInstance(self.bank.get_account(345), Account)

    def test_get_transactions(self) -> None:
        self.assertEqual(len(self.bank.get_transactions(345)), 2)

    def test_register_accounts(self) -> None:
        self.assertEqual(len(self.bank.accounts.items()), 1)

    def test_register_transactions(self) -> None:
        self.assertEqual(len(self.bank.transactions.items()), 1)

    def test_calculate_transactions(self) -> None:
        self.bank.calculate_balances()
        self.assertEqual(self.bank.get_account(345).balance, Decimal(132423))

    def test_get_balance(self) -> None:
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.bank.get_balances()
            self.assertEqual(stdout.getvalue().strip(), '345,14428')


if __name__ == '__main__':
    unittest.main()
