class Transaction(object):

    def __init__(self, date, ledger, amount, company):
        self.date = date
        self.ledger = ledger
        self.amount = amount
        self.company = company


class MainAccount(object):
    def __init__(self):
        self.total_balance = 0
        self.transactions = []
        self.daily_balances = {}
        self.ordered_balances = []



    def add_transactions(self, transactions):

        num_keys_before = len(self.daily_balances)

        for transaction in transactions:
            self.transactions.append(transaction)
            self.total_balance += transaction.amount


            if self.daily_balances.get(transaction.date) != None:
                self.daily_balances[transaction.date] += transaction.amount
            else:
                self.daily_balances[transaction.date] = transaction.amount

            if num_keys_before < len(self.daily_balances):
                self.ordered_balances = sorted(self.daily_balances.keys())


    def print_daily_bal(self):
        # find way to order this later

        running = 0
        for key in self.ordered_balances:
            running += self.daily_balances[key]
            print key, ': ', running 
