# Used for parsing transactions
from bench_objects import Transaction, MainAccount
import datetime

# Constants
DATE = "Date"
LEDGER = "Ledger"
AMOUNT = "Amount"
COMPANY = "Company"
TRANSACTIONS = 'transactions'



def parse_transactions(json_response):

    all_transactions = json_response.get(TRANSACTIONS)
    parsed_transactions = []

    if all_transactions == None:
        return parsed_transactions

    for transaction in all_transactions:

        parsed_transaction = parse_transaction(transaction)

        # None will be returned if parsing errors occurred
        # i.e. malformed response with missing fields
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

    # Land here if response is missing one of the necessary fields
    except KeyError, ValueError:
        return
