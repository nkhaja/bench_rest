import unittest
import json
from Parser import *
from test_data import *
from Paging import *


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
        print len(responses_truncated)
        assert len(responses_truncated) == 4


if __name__ == '__main__':
    unittest.main()
