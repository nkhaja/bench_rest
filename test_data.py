sample_transaction = {
    "Date": "2013-12-18",
    "Ledger": "Business Meals & Entertainment Expense",
    "Amount": "-8.94"
}

good_input_10 = '''{
    "totalCount": 38,
    "page": 2,
    "transactions": [{
        "Date": "2013-12-19",
        "Ledger": "Travel Expense, Nonlocal",
        "Amount": "-200",
        "Company": "YELLOW CAB COMPANY LTD VANCOUVER"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Business Meals & Entertainment Expense",
        "Amount": "-8.94",
        "Company": "NESTERS MARKET #x0064 VANCOUVER BC"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Travel Expense, Nonlocal",
        "Amount": "-9.55",
        "Company": "VANCOUVER TAXI VANCOUVER BC"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Travel Expense, Nonlocal",
        "Amount": "-10.9",
        "Company": "YELLOW CAB CO LTD VANCOUVER BC"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Travel Expense, Nonlocal",
        "Amount": "-10.9",
        "Company": "YELLOW CAB CO LTD VANCOUVER BC"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Insurance Expense",
        "Amount": "-22.94",
        "Company": "LONDON DRUGS #78 VANCOUVER BC"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Web Hosting & Services Expense",
        "Amount": "-50.95",
        "Company": "LINKEDIN LINKEDIN.COM"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Office Expense",
        "Amount": "-642.79",
        "Company": "COSTCO WHOLESALE #55 CO VANCOUVER"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Business Meals & Entertainment Expense",
        "Amount": "-1084.32",
        "Company": "BC LIQUOR #129 VANCOUVER BC"
    }, {
        "Date": "2013-12-17",
        "Ledger": "",
        "Amount": "10000",
        "Company": "PAYMENT - THANK YOU / PAIEMENT - MERCI"
    }]
} '''





# 3 entries are missing data
bad_input_10 = ''' {
    "totalCount": 38,
    "page": 2,
    "transactions": [{
        "Date": "2013-12-19",

        "Company": "YELLOW CAB COMPANY LTD VANCOUVER"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Business Meals & Entertainment Expense",
        "Amount": "-8.94"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Travel Expense, Nonlocal",
        "Amount": "-9.55",
        "Company": "VANCOUVER TAXI VANCOUVER BC"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Travel Expense, Nonlocal",
        "Amount": "-10.9",
        "Company": "YELLOW CAB CO LTD VANCOUVER BC"
    }, {
        "Ledger": "Travel Expense, Nonlocal",
        "Amount": "-10.9",
        "Company": "YELLOW CAB CO LTD VANCOUVER BC"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Insurance Expense",
        "Amount": "-22.94",
        "Company": "LONDON DRUGS #78 VANCOUVER BC"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Web Hosting & Services Expense",
        "Amount": "-50.95",
        "Company": "LINKEDIN LINKEDIN.COM"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Office Expense",
        "Amount": "-642.79",
        "Company": "COSTCO WHOLESALE #55 CO VANCOUVER"
    }, {
        "Date": "2013-12-18",
        "Ledger": "Business Meals & Entertainment Expense",
        "Amount": "-1084.32",
        "Company": "BC LIQUOR #129 VANCOUVER BC"
    }, {
        "Date": "2013-12-17",
        "Ledger": "",
        "Amount": "10000",
        "Company": "PAYMENT - THANK YOU / PAIEMENT - MERCI"
    }]
} '''




first_page = '''{
    "totalCount": 38,
    "page": 1,
    "transactions": [{
        "Date": "2013-12-22",
        "Ledger": "Phone & Internet Expense",
        "Amount": "-110.71",
        "Company": "SHAW CABLESYSTEMS CALGARY AB"
    }, {
        "Date": "2013-12-21",
        "Ledger": "Travel Expense, Nonlocal",
        "Amount": "-8.1",
        "Company": "BLACK TOP CABS VANCOUVER BC"
    }, {
        "Date": "2013-12-21",
        "Ledger": "Business Meals & Entertainment Expense",
        "Amount": "-9.88",
        "Company": "GUILT & CO. VANCOUVER BC"
    }, {
        "Date": "2013-12-20",
        "Ledger": "Travel Expense, Nonlocal",
        "Amount": "-7.6",
        "Company": "VANCOUVER TAXI VANCOUVER BC"
    }, {
        "Date": "2013-12-20",
        "Ledger": "Business Meals & Entertainment Expense",
        "Amount": "-120",
        "Company": "COMMODORE LANES & BILL VANCOUVER BC"
    }, {
        "Date": "2013-12-20",
        "Ledger": "Business Meals & Entertainment Expense",
        "Amount": "-177.5",
        "Company": "COMMODORE LANES & BILL VANCOUVER BC"
    }, {
        "Date": "2013-12-20",
        "Ledger": "Equipment Expense",
        "Amount": "-1874.75",
        "Company": "NINJA STAR WORLD VANCOUVER BC"
    }, {
        "Date": "2013-12-19",
        "Ledger": "",
        "Amount": "20000",
        "Company": "PAYMENT - THANK YOU / PAIEMENT - MERCI"
    }, {
        "Date": "2013-12-19",
        "Ledger": "Web Hosting & Services Expense",
        "Amount": "-10.99",
        "Company": "DROPBOX xxxxxx8396 CA 9.99 USD @ xx1001"
    }, {
        "Date": "2013-12-19",
        "Ledger": "Business Meals & Entertainment Expense",
        "Amount": "-35.7",
        "Company": "NESTERS MARKET #x0064 VANCOUVER BC"
    }]
}'''
