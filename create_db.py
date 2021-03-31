#!/usr/bin/env python3

# ---------------------------
# projects/IDB3/create_db.py
# Fares Fraij
# ---------------------------

import json
from models import app, db, Stock

# ------------
# load_json
# ------------
def load_json(filename):
    """
    return a python dict jsn
    filename a json file
    """
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

# ------------
# create_books
# ------------
def create_stocks():
    """
    populate stock table
    """
    stocks = load_json('stocks.json')

    for category, stockList in stocks.items():
        for stock in stockList:
            name = stockList[stock]["OVERVIEW"]["Name"]
            ticker = stockList[stock]["OVERVIEW"]["Symbol"]
            exchange = stockList[stock]["OVERVIEW"]["Exchange"]
            marketCapitalization = stockList[stock]["OVERVIEW"]["MarketCapitalization"]
            beta = stockList[stock]["OVERVIEW"]["Beta"]
            peRatio = stockList[stock]["OVERVIEW"]["PERatio"]
            eps = stockList[stock]["OVERVIEW"]["EPS"]
            yearlyLow = stockList[stock]["OVERVIEW"]["52WeekLow"]
            yearlyHigh = stockList[stock]["OVERVIEW"]["52WeekHigh"]
            dividend = stockList[stock]["OVERVIEW"]["ForwardAnnualDividendRate"]
            dividendYield = stockList[stock]["OVERVIEW"]["ForwardAnnualDividendYield"]
            exDividend = stockList[stock]["OVERVIEW"]["ExDividendDate"]
            category = category
            price = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["05. price"]
            change = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["09. change"]
            changePercent = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["10. change percent"]
            previousClose = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["08. previous close"]
            open = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["02. open"]
            low = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["04. low"]
            high = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["03. high"]
            volume = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["06. volume"]
            day = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["07. latest trading day"]
		
            newStock = Stock(name = name, ticker = ticker, exchange = exchange, price = price, change = change, \
            changePercent = changePercent, day = day, previousClose = previousClose, marketCapitalization = marketCapitalization, \
            open = open, beta = beta, peRatio = peRatio, eps = eps, low = low, high = high, yearlyLow = yearlyLow, \
            yearlyHigh = yearlyHigh, dividend = dividend, dividendYield = dividendYield, volume = volume, exDividend = exDividend, \
            category = category)
        
            # After I create the book, I can then add it to my session.
            db.session.add(newStock)
            # commit the session to my DB.
            db.session.commit()
	
create_stocks()
