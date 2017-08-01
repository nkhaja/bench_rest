import urllib2

# Constants
date = "Date"
ledger = "Ledger"
amount = "Amount"
company = "Company"
totalCount = "totalCount"
page = 'page'
transactions = 'transactions'

base_url = 'http://resttest.bench.co/transactions'
url_cap = '.json'



def getPage(page_num):

    requested_url = base_url + str(page_num) + url_cap
    response = urllib2.urlopen(requested_url)

    return response



if __name__ == '__main__':

    foo = urllib2.urlopen('http://resttest.bench.co/transactions/4.json').read()
    print foo
