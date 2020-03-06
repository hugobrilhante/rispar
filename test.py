import unittest
from decimal import Decimal
from io import StringIO
from unittest.mock import patch

from bank import Account, Bank
from rispatest import create_parser, main


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


class ParseTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.parser = create_parser()

    def test_with_empty_args(self) -> None:
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_with_args(self) -> None:
        with patch('sys.stdout', new=StringIO()) as stdout:
            args = self.parser.parse_args(['--files', 'accounts.csv', 'transactions.csv'])
            main(args)
            self.assertEqual(stdout.getvalue().strip(), '345,132423')


if __name__ == '__main__':
    unittest.main()
