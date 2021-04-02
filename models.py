#!/usr/bin/env python3

# ---------------------------
# projects/IDB3/models.py
# Fares Fraij
# ---------------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder="./static", template_folder="./templates")
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:1234@34.66.91.137:5432/postgres')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DB_STRING", 'postgres://postgres:tbtbtb311@localhost:5432/postgres')
# to suppress a warning message
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# ------------
# Book
# ------------


class Stock(db.Model):

    __tablename__ = 'stock'

    name = db.Column(db.String(80), nullable=False)
    ticker = db.Column(db.String(6), primary_key=True)
    exchange = db.Column(db.String(10), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    change = db.Column(db.String(20), nullable=False)
    changePercent = db.Column(db.String(10), nullable=False)
    day = db.Column(db.String(80), nullable=False)
    previousClose = db.Column(db.String(20), nullable=False)
    marketCapitalization = db.Column(db.String(20), nullable=False)
    open = db.Column(db.String(20), nullable=False)
    beta = db.Column(db.String(10), nullable=False)
    peRatio = db.Column(db.String(10), nullable=False)
    eps = db.Column(db.String(10), nullable=False)
    low = db.Column(db.String(20), nullable=False)
    high = db.Column(db.String(20), nullable=False)
    yearlyLow = db.Column(db.String(20), nullable=False)
    yearlyHigh = db.Column(db.String(20), nullable=False)
    dividend = db.Column(db.String(20), nullable=False)
    dividendYield = db.Column(db.String(20), nullable=False)
    volume = db.Column(db.String(30), nullable=False)
    exDividend = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(20), nullable=False)


class StockIntraday(db.Model):

    __tablename__ = 'stockhistory'

    ticker = db.Column(db.String(6), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    id = db.Column(db.Integer, primary_key=True)


class Stock_stats(db.Model):

    __tablename__ = 'stock statistics'

    symbol = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(10), nullable=False)
    MarketCapitalization = db.Column(db.String(20), nullable=False)
    EBITDA = db.Column(db.String(20), nullable=False)
    PERatio = db.Column(db.String(20), nullable=False)
    PEGRatio = db.Column(db.String(20), nullable=False)
    BookValue = db.Column(db.String(20), nullable=False)
    DividendPerShare = db.Column(db.String(20), nullable=False)
    DividendYield = db.Column(db.String(20), nullable=False)
    EPS = db.Column(db.String(20), nullable=False)
    RevenuePerShareTTM = db.Column(db.String(20), nullable=False)
    ProfitMargin = db.Column(db.String(20), nullable=False)
    OperatingMarginTTM = db.Column(db.String(20), nullable=False)
    ReturnOnAssetsTTM = db.Column(db.String(20), nullable=False)
    ReturnOnEquityTTM = db.Column(db.String(20), nullable=False)
    RevenueTTM = db.Column(db.String(20), nullable=False)
    GrossProfitTTM = db.Column(db.String(20), nullable=False)
    DilutedEPSTTM = db.Column(db.String(20), nullable=False)
    QuarterlyEarningsGrowthYOY = db.Column(db.String(20), nullable=False)
    QuarterlyRevenueGrowthYOY = db.Column(db.String(20), nullable=False)
    AnalystTargetPrice = db.Column(db.String(20), nullable=False)
    TrailingPE = db.Column(db.String(20), nullable=False)
    ForwardPE = db.Column(db.String(20), nullable=False)
    PriceToSalesRatioTTM = db.Column(db.String(20), nullable=False)
    PriceToBookRatio = db.Column(db.String(20), nullable=False)
    EVToRevenue = db.Column(db.String(20), nullable=False)
    EVToEBITDA = db.Column(db.String(20), nullable=False)


db.drop_all()
db.create_all()
