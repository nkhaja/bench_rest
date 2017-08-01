import urllib2
import datetime
from bench_objects import Transaction, MainAccount
from Parser import parse_transactions

# Constants
totalCount = "totalCount"
page = 'page'
TRANSACTIONS = 'transactions'

BASE_URL = 'http://resttest.bench.co/transactions/'
URL_CAP = '.json'


# Global Vars (subsitute for DB)
total_transaction_count = 0
page = 1


def get_page(page_num):

    requested_url = BASE_URL + str(page_num) + URL_CAP

    try:
        response = urllib2.urlopen(requested_url).read()
        return response
    except urllib2.HTTPError:
        print urllib2.HTTPError

    return


# TODO update to stop where total number of cases reached
def get_page_window(from_page, to_page=None):

    if from_page > to_page:
        raise ValueError('from_page arguments must be int < to_page argument')

    responses = []

    if to_page is not None:

        for i in range(from_page, to_page+1):
            response = get_page(i)

            if response:
                responses.append(response)

            return responses
    else:
        while True:
            response = get_page(from_page)

            if not response:
                break

            responses.append(response)

        return responses


if __name__ == '__main__':

    print get_page_window(1,3)
