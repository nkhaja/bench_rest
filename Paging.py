import urllib2
import json

TRANSACTIONS = 'transactions'
BASE_URL = 'http://resttest.bench.co/transactions/'
URL_CAP = '.json'

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
