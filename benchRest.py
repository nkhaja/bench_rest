from bench_objects import *
from Parser import *
from Paging import *

# Constants
totalCount = "totalCount"
page = 'page'
TRANSACTIONS = 'transactions'

BASE_URL = 'http://resttest.bench.co/transactions/'
URL_CAP = '.json'

#global var
main_account = MainAccount()


def get_all_transactions():

    loaded_transactions = []

    responses = get_page_window(1)

    for response in responses:

        transactions = parse_transactions(response)
        loaded_transactions += transactions

    return loaded_transactions


def main_app():
    print 'Welcome to the Bench.co Rest API \n'
    print 'Please type one of the following commands: \n '
    options = ''' \n\n 1. total_balance: gives total balance for all transactions
                  available on this API

2. daily_balance: gives the daily running balance from
   transactions on this API

3. quit: exits the app
    \n\n'''

    print options
    main_account = MainAccount()
    all_transactions = get_all_transactions()
    main_account.add_transactions(all_transactions)

    while True:

        user_input = raw_input('enter command: ')

        if user_input == str(1) or user_input == 'total_balance':
            print '\n'
            print main_account.total_balance
            print '\n'

        elif user_input == str(2) or user_input == 'daily_balance':
            print '\n'
            main_account.print_daily_bal()
            print '\n'

        elif user_input == str(3) or user_input == 'quit':
            print '\n'
            print('Goodbye!')
            print '\n'
            break

        else:
            print 'please enter a valid input'
            print 'enter the digits corresponding to the desired command'
            print ' or enter the name of the desired command'
            print options

if __name__ == '__main__':

    main_app()
