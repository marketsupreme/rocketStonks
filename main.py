#!/usr/bin/env python3
# projects/IDB3/main.py
# Fares Fraij

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('nav_bar.html') + render_template('index.html')


@app.route('/stock/')
def stock():
    return render_template('stocks.html')


@app.route('/stock/AAPL/')
def AAPL():
    return render_template('aapl.html')


@app.route('/stock/HON/')
def HON():
    return render_template('hon.html')


@app.route('/stock/MRNA/', methods=['GET', 'POST'])
def MRNA():
    return render_template('mrna.html')


@app.route('/cat/')
def cat():
    return render_template('categories.html')


@app.route('/cat/bio')
def catBio():
    return render_template('catBiomedical.html')


@app.route('/cat/penny')
def catPenny():
    return render_template('catPenny_Stocks.html')


@app.route('/cat/crypto')
def catCrypto():
    return render_template('catCryptocurrency.html')


@app.route('/cat/industry/')
def catIndustry():
    return render_template('catIndustry.html')


@app.route('/cat/tech/')
def catTech():
    return render_template('catTech.html')

<<<<<<< HEAD
@app.route('/about/')
def about():
	return render_template('about.html')
=======

@app.route('/projections/AAPL')
def projections():
    return render_template('projections_AAPL.html')


@app.route('/about/')
def about():
    return render_template('nav_bar.html') + render_template('hon.html')
>>>>>>> b9478085c815e7e1ee23d9584de022cae5d3d9a3


# debug=True to avoid restart the local development server manually after each change to your code.
# host='0.0.0.0' to make the server publicly available.
if __name__ == "__main__":
    app.run(debug=True)
