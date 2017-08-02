import urllib2
import datetime
import json
from bench_objects import *
from Parser import *

# Constants
totalCount = "totalCount"
page = 'page'
TRANSACTIONS = 'transactions'

BASE_URL = 'http://resttest.bench.co/transactions/'
URL_CAP = '.json'


# Global Vars (subsitute for DB)
total_transaction_count = 0
last_page = 1

main_account = MainAccount()

def get_page(page_num):

    requested_url = BASE_URL + str(page_num) + URL_CAP

    try:
        response = json.load(urllib2.urlopen(requested_url))
        return response
    except urllib2.HTTPError:
        print urllib2.HTTPError

    return


# TODO update to stop where total number of cases reached

def get_page_window(from_page, to_page=None):

    responses = []

    if to_page is not None:

        if from_page > to_page:
            raise ValueError('from_page arguments must be int < to_page argument')

        for i in range(from_page, to_page+1):
            response = get_page(i)

            if response:
                responses.append(response)

            return responses
    else:
        while True:
            print 'getting a response'
            response = get_page(from_page)
            from_page += 1

            if not response:
                break

            responses.append(response)

        return responses

def get_all_transactions():

    loaded_transactions = []

    responses = get_page_window(1)

    for response in responses:

        print 'parsing transactions'
        transactions = parse_transactions(response)
        print 'finished parsing transactions'
        loaded_transactions += transactions


    return loaded_transactions


def main_app():
    print 'Welcome to the Bench.co Rest API \n'
    print 'Please type one of the following commands: \n '
    options = ''' 1. total_balance: gives total balance for all transactions
                  available on this API

2. daily_balance: gives the daily running balance from
   transactions on this API

3. quit: exits the app
    '''

    print options
    main_account = MainAccount()
    all_transactions = get_all_transactions()
    main_account.add_transactions(all_transactions)

    while True:

        user_input = raw_input('enter command: ')

        if user_input == str(1) or user_input == 'total_balance':
            print main_account.total_balance


        elif user_input == str(2) or user_input == 'daily_balance':
            main_account.print_daily_bal()

        elif user_input == str(3) or user_input == 'quit':
            print('Goodbye!')
            break

        else:
            print 'please enter a valid input'
            print 'enter the digits corresponding to the desired command'
            print ' or enter the name of the desired command'
            print options
            print user_input
            print type(user_input)

if __name__ == '__main__':

    main_app()
