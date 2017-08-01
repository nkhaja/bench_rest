import urllib2
import datetime

# Constants
DATE = "Date"
LEDGER = "Ledger"
AMOUNT = "Amount"
COMPANY = "Company"

totalCount = "totalCount"
page = 'page'
TRANSACTIONS = 'transactions'

BASE_URL = 'http://resttest.bench.co/transactions'
URL_CAP = '.json'


# Global Vars (subsitute for DB)

total_transaction_count = 0
page = 1


def get_page(page_num):

    requested_url = BASE_URL + str(page_num) + URL_CAP
    response = urllib2.urlopen(requested_url)

    return response


# Parsing
def parse_transactions(json):
    all_transactions = json[transactions]
    parsed_transactions = []

    for transaction in all_transactions:

        parsed_transaction = parse_transaction(transaction)

        if parsed_transaction != None:
            parsed_transactions.append(parsed_transaction)

    return parsed_transactions

def parse_transaction(transaction):

    try:

        string_date = transaction[DATE]
        date = datetime.datetime(string_date, '%Y-%m-%d')
        ledger = transaction[LEDGER]
        amount = int(transaction[AMOUNT])
        company = transaction[COMPANY]

        new_transaction = Transaction(date, ledger, amount, company)

        return new_transaction

    except KeyError, ValueError:
        return

def next_page():
    pass









if __name__ == '__main__':

    foo = urllib2.urlopen('http://resttest.bench.co/transactions/4.json').read()
    print foo
