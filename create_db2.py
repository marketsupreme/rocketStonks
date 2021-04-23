#!/usr/bin/env python3

# ---------------------------
# projects/IDB3/create_db.py
# Fares Fraij
# ---------------------------

import json
from models2 import app, db, StockIntraday

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

def create_stocks():
    """
    populate stock table
    """
    stocks = load_json('stocks.json')
    # parsing JSON dictionaries
    for category, stockList in stocks.items():
        for stock in stockList:
            for date in stockList[stock]["TIME_SERIES_INTRADAY"]["Time Series (15min)"]:
                date = date
                price = float(stockList[stock]["TIME_SERIES_INTRADAY"]["Time Series (15min)"][date]["4. close"])
                open = float(stockList[stock]["TIME_SERIES_INTRADAY"]["Time Series (15min)"][date]["1. open"])
                high = float(stockList[stock]["TIME_SERIES_INTRADAY"]["Time Series (15min)"][date]["2. high"])
                low = float(stockList[stock]["TIME_SERIES_INTRADAY"]["Time Series (15min)"][date]["3. low"])
                volume = float(stockList[stock]["TIME_SERIES_INTRADAY"]["Time Series (15min)"][date]["5. volume"])
                ticker = stockList[stock]["OVERVIEW"]["Symbol"]
                newStockIntraday = StockIntraday(
                    date=date, price=price, ticker=ticker, open=open, high=high, volume=volume, low=low)

                db.session.add(newStockIntraday)
                db.session.commit()


create_stocks()