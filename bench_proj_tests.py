all_datesimport unittest
import json
from Parser import *
from test_data import *
from Paging import *
import datetime


class ParserTest(unittest.TestCase):

    def test_parse10_good(self):
        data = json.loads(good_input_10)
        transactions = parse_transactions(data)
        assert len(transactions) == 10

    def test_parse10_bad(self):
        data = json.loads(bad_input_10)
        transactions = parse_transactions(data)
        assert len(transactions) == 7

    def test_parse_none(self):
        empty_dict = ''' {

        }'''
        data = json.loads(empty_dict)
        transactions = parse_transactions(data)
        assert len(transactions) == 0

class PagingTest(unittest.TestCase):

    def test_get_specific_page(self):
        response = get_page(1)
        assert response['page'] == 1

        response_page_3 = get_page(3)
        assert response_page_3['page'] == 3

    def test_page_out_of_range(self):
        response = get_page(5)
        assert response == None

    def test_many_pages(self):
        responses = get_page_window(1)
        assert len(responses) == 4

        for i in range(0,4):
            assert responses[i]['page'] == i + 1

        responses_mid_range = get_page_window(1,3)
        for i in range(1,4):
            assert responses[i]['page'] == i + 1


        # should stop making requests once 5th fails
        responses_truncated = get_page_window(1,10)
        assert len(responses_truncated) == 4

class TransactionTest(unittest.TestCase):


    def test_init(self):

        date = datetime.datetime.strptime('2013-12-19', '%Y-%m-%d')

        transaction = Transaction(date, 'test_ledger', 550, 'test_company')

        assert transaction.date == date
        assert transaction.ledger == 'test_ledger'
        assert transaction.amount == 550
        assert transaction.company == 'test_company'


class MainAccountTest(unittest.TestCase):

    def test_add_transactions(self):

        data = json.loads(good_input_10)
        transactions = parse_transactions(data)
        amounts = [-200,-8.94,-9.55,-10.9, -10.9, -22.94,-50.95,-642.79,-1084.32,10000]
        days = [[10000], [-8.94,-9.55,-10.9, -10.9, -22.94,-50.95,-642.79,-1084.32],[-200]]

        total = sum(amounts)

        main_account = MainAccount()
        main_account.add_transactions(transactions)
        assert len(main_account.transactions) == 10
        assert main_account.total_balance == total

        running = 0
        test_running = 0
        for i in range(len(days)):
            key = main_account.all_dates[i]
            running += main_account.daily_balances[key]
            test_running += sum(days[i])

            print 'compare running:' ,running, test_running

            assert running == test_running



if __name__ == '__main__':
    unittest.main()
