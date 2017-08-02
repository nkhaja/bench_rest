# Used for parsing transactions
from bench_objects import Transaction, MainAccount
import datetime

# Constants
DATE = "Date"
LEDGER = "Ledger"
AMOUNT = "Amount"
COMPANY = "Company"

totalCount = "totalCount"
page = 'page'
TRANSACTIONS = 'transactions'



def parse_transactions(json):
    all_transactions = json[TRANSACTIONS]
    parsed_transactions = []

    for transaction in all_transactions:

        parsed_transaction = parse_transaction(transaction)

        if parsed_transaction != None:
            parsed_transactions.append(parsed_transaction)

    return parsed_transactions

def parse_transaction(transaction):

    try:
        string_date = transaction[DATE]
        date = datetime.datetime.strptime(string_date, '%Y-%m-%d')
        ledger = transaction[LEDGER]
        amount = float(transaction[AMOUNT])
        company = transaction[COMPANY]

        new_transaction = Transaction(date, ledger, amount, company)

        return new_transaction

    except KeyError, ValueError:
        return
