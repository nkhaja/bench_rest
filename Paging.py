import urllib2
import json

TRANSACTIONS = 'transactions'
BASE_URL = 'http://resttest.bench.co/transactions/'
URL_CAP = '.json'
PAGE = 'page'

TOTAL_COUNT = "totalCount"

# Loads a single page of json
def get_page(page_num):

    requested_url = BASE_URL + str(page_num) + URL_CAP

    try:
        response = json.load(urllib2.urlopen(requested_url))
        return response
    except urllib2.HTTPError, e:
        print str(e)
    except urllib2.URLError, e:
        print str(e)

    return

# TODO update to stop where total number of cases reached


# loads multiple pages of info within a given range
def get_page_window(from_page, to_page=None):

    responses = []

    # A top end of the range is given
    if to_page is not None:

        # Arguments are malformed, must be positive integer range
        if from_page > to_page:
            raise ValueError('from_page arguments must be int < to_page argument')

        for i in range(from_page, to_page+1):
            response = get_page(i)

            if response == None:
                break

            responses.append(response)

        print 'returning responses'
        return responses

    # return all pages from_page and onwards

    else:
        while True:
            print 'getting a response'
            response = get_page(from_page)
            from_page += 1

            if not response:
                break

            responses.append(response)

        return responses




# class created for disucssion of future steps, not used in implementation

# This class is used to determine whether we have all the pages available

class Pager(object):

    def __init__(self, page, num_items_loaded):
        self.page = page
        self.num_items_loaded = num_items_loaded

    # Checks total_count for more items than are loaded
    # Using request on the most recently visited valid page
    def has_more_pages(fun, *args):
        response = fun(args)

        if not response:
            return False

        return response[TOTAL_COUNT] < self.total_items
