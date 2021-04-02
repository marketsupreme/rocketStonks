#!/usr/bin/env python3

# ---------------------------
# projects/IDB3/create_db.py
# Fares Fraij
# ---------------------------

import json
from models import app, db, Stock, StockIntraday, StockStats

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
            price = float(stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["05. price"])
            change = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["09. change"]
            changePercent = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["10. change percent"]
            previousClose = float(stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["08. previous close"])
            open = float(stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["02. open"])
            low = float(stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["04. low"])
            high = float(stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["03. high"])
            volume = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["06. volume"]
            day = stockList[stock]["GLOBAL_QUOTE"]["Global Quote"]["07. latest trading day"]

            newStock = Stock(name=name, ticker=ticker, exchange=exchange, price=price, change=change,
                             changePercent=changePercent, day=day, previousClose=previousClose, marketCapitalization=marketCapitalization,
                             open=open, beta=beta, peRatio=peRatio, eps=eps, low=low, high=high, yearlyLow=yearlyLow,
                             yearlyHigh=yearlyHigh, dividend=dividend, dividendYield=dividendYield, volume=volume, exDividend=exDividend,
                             category=category)

            db.session.add(newStock)
            db.session.commit()

            for date in stockList[stock]["TIME_SERIES_INTRADAY"]["Time Series (15min)"]:
                date = date
                price = stockList[stock]["TIME_SERIES_INTRADAY"]["Time Series (15min)"][date][
                    "4. close"]
                ticker = stockList[stock]["OVERVIEW"]["Symbol"]
                newStockIntraday = StockIntraday(
                    date=date, price=price, ticker=ticker)

                db.session.add(newStockIntraday)
                db.session.commit()

    create_stock_statistics()


def create_stock_statistics():
    stocks = load_json('stocks.json')

    for category, stockList in stocks.items():
        for stock in stockList.keys():
            overview = stockList[stock]['OVERVIEW']

            symbol = overview['Symbol']
            name = overview['Name']
            description = overview['Description']
            currency = overview['Currency']
            country = overview['Country']
            MarketCapitalization = overview['MarketCapitalization']
            EBITDA = overview['EBITDA']
            PERatio = overview['PERatio']
            PEGRatio = overview['PEGRatio']
            BookValue = overview['BookValue']
            DividendPerShare = overview['DividendPerShare']
            DividendYield = overview['DividendYield']
            EPS = overview['EPS']
            RevenuePerShareTTM = overview['RevenuePerShareTTM']
            ProfitMargin = overview['ProfitMargin']
            OperatingMarginTTM = overview['OperatingMarginTTM']
            ReturnOnAssetsTTM = overview['ReturnOnAssetsTTM']
            ReturnOnEquityTTM = overview['ReturnOnEquityTTM']
            RevenueTTM = overview['RevenueTTM']
            GrossProfitTTM = overview['GrossProfitTTM']
            DilutedEPSTTM = overview['DilutedEPSTTM']
            QuarterlyEarningsGrowthYOY = overview['QuarterlyEarningsGrowthYOY']
            QuarterlyRevenueGrowthYOY = overview['QuarterlyRevenueGrowthYOY']
            AnalystTargetPrice = overview['AnalystTargetPrice']
            TrailingPE = overview['TrailingPE']
            ForwardPE = overview['ForwardPE']
            PriceToSalesRatioTTM = overview['PriceToSalesRatioTTM']
            PriceToBookRatio = overview['PriceToBookRatio']
            EVToRevenue = overview['EVToRevenue']
            EVToEBITDA = overview['EVToEBITDA']

            new_StockStats = StockStats(symbol=symbol, name=name, description=description, currency=currency, country=country, MarketCapitalization=MarketCapitalization, EBITDA=EBITDA, PERatio=PERatio, PEGRatio=PEGRatio, BookValue=BookValue, DividendPerShare=DividendPerShare, DividendYield=DividendYield, EPS=EPS, RevenuePerShareTTM=RevenuePerShareTTM, ProfitMargin=ProfitMargin, OperatingMarginTTM=OperatingMarginTTM, ReturnOnAssetsTTM=ReturnOnAssetsTTM,
                                        ReturnOnEquityTTM=ReturnOnEquityTTM, RevenueTTM=RevenueTTM, GrossProfitTTM=GrossProfitTTM, DilutedEPSTTM=DilutedEPSTTM, QuarterlyEarningsGrowthYOY=QuarterlyEarningsGrowthYOY, QuarterlyRevenueGrowthYOY=QuarterlyRevenueGrowthYOY, AnalystTargetPrice=AnalystTargetPrice, TrailingPE=TrailingPE, ForwardPE=ForwardPE, PriceToSalesRatioTTM=PriceToSalesRatioTTM, PriceToBookRatio=PriceToBookRatio, EVToRevenue=EVToRevenue, EVToEBITDA=EVToEBITDA)

            db.session.add(new_StockStats)
            db.session.commit()


create_stocks()
