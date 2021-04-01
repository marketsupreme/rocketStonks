#!/usr/bin/env python3

# ---------------------------
# projects/IDB3/models.py
# Fares Fraij
# ---------------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder="./static", template_folder="./templates")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgresql://postgres:1234@34.66.91.137:5432/postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

# ------------
# Book
# ------------
class Stock(db.Model):

    __tablename__ = 'stock'

    name = db.Column(db.String(80), nullable = False) #
    ticker = db.Column(db.String(6), primary_key = True) #
    exchange = db.Column(db.String(10), nullable = False) #
    price = db.Column(db.String(20), nullable = False) #
    change = db.Column(db.String(20), nullable = False) #
    changePercent = db.Column(db.String(10), nullable = False) #
    day = db.Column(db.String(80), nullable = False) #
    previousClose = db.Column(db.String(20), nullable = False) #
    marketCapitalization = db.Column(db.String(20), nullable = False) #
    open = db.Column(db.String(20), nullable = False) #
    beta = db.Column(db.String(10), nullable = False) #
    peRatio = db.Column(db.String(10), nullable = False) #
    eps = db.Column(db.String(10), nullable = False) #
    low = db.Column(db.String(20), nullable = False) #
    high = db.Column(db.String(20), nullable = False) #
    yearlyLow = db.Column(db.String(20), nullable = False) #
    yearlyHigh = db.Column(db.String(20), nullable = False) #
    dividend = db.Column(db.String(20), nullable = False) #
    dividendYield = db.Column(db.String(20), nullable = False) #
    volume = db.Column(db.String(30), nullable = False) #
    exDividend = db.Column(db.String(80), nullable = False) #
    category = db.Column(db.String(20), nullable = False) #

class StockIntraday(db.Model):

    __tablename__ = 'stockhistory'

    ticker = db.Column(db.String(6), nullable = False)
    price = db.Column(db.String(20), nullable = False)
    date = db.Column(db.String(20), nullable = False)
    id = db.Column(db.Integer, primary_key = True)

db.drop_all()
db.create_all()
