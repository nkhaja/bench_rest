class Transaction(object):

    def __init__(self, date, ledger, amount, company):
        self.date = date
        self.ledger = ledger
        self.amount = amount
        self.company = company


class MainAccount(object):
    def __init__(self):
        self.total_balance = 0

        # A list of all trasactions loaded
        self.transactions = []

        # A dictionary of the
        self.daily_balances = {}

        # A list of all dates for which we have transactions
        self.all_dates = []



    def add_transactions(self, transactions):

        num_keys_before = len(self.daily_balances)

        for transaction in transactions:
            self.transactions.append(transaction)
            self.total_balance += transaction.amount

            # First transaction on this date, create an entry
            if self.daily_balances.get(transaction.date) != None:
                self.daily_balances[transaction.date] += transaction.amount

            # Add to existing marginal balance here
            else:
                self.daily_balances[transaction.date] = transaction.amount

            # only re-sort the data if new dates are introduced
            # Longer operation, but would happen once a day
            # unless data from past days not previously documented are added
            if num_keys_before < len(self.daily_balances):
                self.all_dates = sorted(self.daily_balances.keys())


    def print_daily_bal(self):
        # find way to order this later

        running = 0
        for key in self.all_dates:
            running += self.daily_balances[key]
            print key, ': ', running
