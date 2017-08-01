import urllib2

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


class Transaction(object):

    def __init__(self, date, ledger, amount, company):
        self.date = date
        self.ledger = ledger
        self.amount = amount
        self.company = company

def get_page(page_num):

    requested_url = BASE_URL + str(page_num) + URL_CAP
    response = urllib2.urlopen(requested_url)

    return response

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
        date = transaction[DATE]
        ledger = transaction[LEDGER]
        amount = transaction[AMOUNT]
        company = transaction[COMPANY]

        new_transaction = Transaction(date, ledger, amount, company)

        return new_transaction

    except KeyError:
        return








if __name__ == '__main__':

    foo = urllib2.urlopen('http://resttest.bench.co/transactions/4.json').read()
    print foo
