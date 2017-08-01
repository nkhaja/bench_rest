import urllib2

# Constants
date = "Date"
ledger = "Ledger"
amount = "Amount"
company = "Company"
totalCount = "totalCount"
page = 'page'
transactions = 'transactions'

if __name__ == '__main__':

    foo = urllib2.urlopen("http://resttest.bench.co/transactions/4.json").read()
    print foo
