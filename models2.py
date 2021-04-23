#!/usr/bin/env python3

# ---------------------------
# projects/IDB3/models.py
# Fares Fraij
# ---------------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder="./static", template_folder="./templates")
# the uri below is used for GCP
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:1234@34.66.136.81:5432/postgres')
# make sure to type in your password to connect properly
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING", 'postgresql://postgres:Password@localhost:5432/postgres')
# to suppress a warning message
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# ------------
# Book
# ------------

class StockIntraday(db.Model):
    # SQL table for all stocks and their intraday data
    __tablename__ = 'stockhistory'

    ticker = db.Column(db.String(6), nullable=False)
    price = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    open = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(20), nullable=False)
    id = db.Column(db.Integer, primary_key=True)



db.drop_all()
db.create_all()