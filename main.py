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
    return render_template('nav_bar.html') + render_template('stocks.html')


@app.route('/stock/AAPL/')
def AAPL():
    return render_template('nav_bar.html') + render_template('aapl.html')


@app.route('/stock/HON/')
def HON():
    return render_template('nav_bar.html') + render_template('hon.html')


@app.route('/stock/MRNA/', methods=['GET', 'POST'])
def MRNA():
    return render_template('nav_bar.html') + render_template('mrna.html')


@app.route('/cat/')
def cat():
    return render_template('nav_bar.html') + render_template('categories.html')


@app.route('/cat/bio')
def catBio():
    return render_template('nav_bar.html') + render_template('catBiomedical.html')


@app.route('/cat/penny')
def catPenny():
    return render_template('nav_bar.html') + render_template('catPenny_Stocks.html')


@app.route('/cat/crypto')
def catCrypto():
    return render_template('nav_bar.html') + render_template('catCryptocurrency.html')


@app.route('/cat/industry/')
def catIndustry():
    return render_template('nav_bar.html') + render_template('catIndustry.html')


@app.route('/cat/tech/')
def catTech():
    return render_template('nav_bar.html') + render_template('catTech.html')

# Projections page
@app.route('/projections/AAPL')
def projections_AAPL():
    return render_template('nav_bar.html') + render_template('projections_AAPL.html')


@app.route('/projections/HON')
def projections_HON():
    return render_template('nav_bar.html') + render_template('projections_HON.html')


@app.route('/projections/MRNA')
def projections_MRNA():
    return render_template('nav_bar.html') + render_template('projections_MRNA.html')


@app.route('/about/')
def about():
    return render_template('nav_bar.html') + render_template('about.html')


@app.route('/dummy/')
def dummy():
    return render_template('nav_bar.html') + render_template('dummy_link.html')

@app.route('/stock/<stockName>')
def stockPage(stockName):
    # the following dict values will be created with DB calls in future
    stock = {}
    stock['name'] = 'Microsoft'
    stock['ticker'] = 'MSFT'
    stock['exchange'] = 'NYSE'
    stock['price'] = '100'
    stock['change'] = '+10'
    stock['changePercent'] = '+10%'
    stock['day'] = 'Today'
    stock['projection'] = "'stockProjection', stockName = '" + stockName + "'"
    stock['previousClose'] = '90'
    stock['marketCapitalization'] = '10000000'
    stock['open'] = '90'
    stock['beta'] = '0.12'
    stock['peRatio'] = '0.56'
    stock['eps'] = '0.18'
    stock['low'] = '89'
    stock['high'] = '101'
    stock['earningDate'] = 'Feb. 12, 2021'
    stock['yearlyLow'] = '15'
    stock['yearlyHigh'] = '115'
    stock['dividend'] = '3.78'
    stock['dividendYield'] = '0.83'
    stock['volume'] = '100000'
    stock['exDividend'] = 'Mar. 14, 2021'
    stock['avgVolume'] = '800000'
    return render_template('nav_bar.html') + render_template('dynamic_stock.html', stock = stock)

@app.route('/stock/projection/<stockName>')
def stockProjection(stockName):
    return render_template('nav_bar.html') + render_template('dummy_link.html')
# debug=True to avoid restart the local development server manually after each change to your code.
# host='0.0.0.0' to make the server publicly available.
if __name__ == "__main__":
    app.run(debug=True)
