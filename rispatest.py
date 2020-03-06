import argparse

from bank import Bank


def create_parser():
    parser = argparse.ArgumentParser(description='Script to calculate balances')
    parser.add_argument('--files',
                        nargs=2,
                        required=True,
                        metavar=('account.csv', 'transactions.csv'),
                        help="Enter the .csv files")
    return parser


def main(args):
    bank = Bank(*args.files)
    bank.calculate_balances()
    bank.get_balances()


if __name__ == '__main__':
    main(create_parser().parse_args())
