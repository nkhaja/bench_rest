import urllib2
import json
import math

TRANSACTIONS = 'transactions'
BASE_URL = 'http://resttest.bench.co/transactions/'
URL_CAP = '.json'
PAGE = 'page'

TOTAL_COUNT = "totalCount"
PAGE_SIZE = 10

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
# If not end of range given then goes until last page
# This feature can be leveraged in the future transactions list gets too large
def get_page_window(from_page, to_page=None):

    limit = None

    responses = []

    # A top end of the range is given
    if to_page is not None:

        # Arguments are malformed, must be positive integer range
        if from_page > to_page:
            raise ValueError('from_page arguments must be int < to_page argument')

        for i in range(from_page, to_page+1):
            response = get_page(i)

            if not response:
                break

            responses.append(response)

            elif limit_reached(response):
                break

        return responses

    # return all pages from_page and onwards
    else:
        while True:
            response = get_page(from_page)
            from_page += 1

            # Check to see if we've received all items
            if not response:
                break

            responses.append(response)

            if limit_reached(response):
                break

        return responses


def limit_reached(latest_response):
    if latest_response.get(TOTAL_COUNT) and latest_response.get(PAGE):
        total = latest_response[TOTAL_COUNT]
        page = latest_response[PAGE]
        max_page = math.ceil(float(total)/PAGE_SIZE)

        return page == max_page

    else:
        raise ValueError('latest_response is missing key "totalCount" or "page"')



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
