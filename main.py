#!/usr/bin/env python3
# projects/IDB3/main.py
# Fares Fraij

from flask import Flask, render_template, Response, request
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from create_db import app, db, Stock, StockIntraday, StockStats


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('nav_bar.html') + render_template('index.html')


@app.route('/stock/')
def stock():
    stocks = Stock.query.all()
    return render_template('nav_bar.html') + render_template('stocks.html', stocks=stocks)


@app.route('/cat/')
def cat():
    return render_template('nav_bar.html') + render_template('categories.html')


@app.route('/cat/bio')
def catBio():
    stocks = Stock.query.all()
    return render_template('nav_bar.html') + render_template('catBiomedical.html', stocks=stocks)


@app.route('/cat/industry/')
def catIndustry():
    stocks = Stock.query.all()
    return render_template('nav_bar.html') + render_template('catIndustry.html', stocks=stocks)


@app.route('/cat/tech/')
def catTech():
    stocks = Stock.query.all()
    return render_template('nav_bar.html') + render_template('catTech.html', stocks=stocks)


# Projections page TODO
@app.route('/statistics/<stockName>')
def statistics_page(stockName):
    stock = StockStats.query.get(stockName)
    return render_template('nav_bar.html') + render_template('statistics.html', stock=stock)


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
    stock = Stock.query.get(stockName)
    return render_template('nav_bar.html') + render_template('dynamic_stock.html', stock=stock)


@app.route('/cat/<stockName>')
def cat_Bio_Stock(stockName):
    stock = Stock.query.get(stockName)
    return render_template('nav_bar.html') + render_template('dynamic_stock.html', stock=stock)


@app.route('/cat/industry/<stockName>')
def cat_Industry_Stock(stockName):
    stock = Stock.query.get(stockName)
    return render_template('nav_bar.html') + render_template('dynamic_stock.html', stock=stock)


@app.route('/cat/tech/<stockName>')
def cat_Tech_Stock(stockName):
    stock = Stock.query.get(stockName)
    return render_template('nav_bar.html') + render_template('dynamic_stock.html', stock=stock)


@app.route('/static/images/matplotlib/<stockName>.png')
def plot_png(stockName):
    fig = create_figure(stockName)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure(stockName):
    stockData = StockIntraday.query.filter_by(ticker=stockName).all()
    stockData.reverse()
    xs = []
    ys = []
    current = 0
    for i in stockData:
        xs.append(current)
        ys.append(float(i.price))
        current += 1
    minimum = min(ys)
    maximum = max(ys)
    fig = Figure()
    #axis = fig.add_axes([0,0,1,1])
    axis = fig.add_subplot(1, 1, 1, title = '5 Day Graph in USD')
    axis.plot(xs, ys)
    return fig


@app.route('/stock/projection/<stockName>')
def stockProjection(stockName):
    return render_template('nav_bar.html') + render_template('dummy_link.html')

@app.route('/tables/stock')
def stockTable(sortBy = None, asc = True, page = 1):
    sortBy = request.args.get('sortBy')
    asc = request.args.get('asc')
    page = int(request.args.get('page'))
    if sortBy == None:
        stocks = Stock.query.all()
    elif sortBy == 'Price':
        if asc == 'True':
            stocks = Stock.query.order_by(Stock.price.desc()).all()
        else:
            stocks = Stock.query.order_by(Stock.price).all()
    elif sortBy == 'Open':
        if asc == 'True':
            stocks = Stock.query.order_by(Stock.open.desc()).all()
        else:
            stocks = Stock.query.order_by(Stock.open).all()
    elif sortBy == 'PreviousClose':
        if asc == 'True':
            stocks = Stock.query.order_by(Stock.previousClose.desc()).all()
        else:
            stocks = Stock.query.order_by(Stock.previousClose).all()
    elif sortBy == 'Low':
        if asc == 'True':
            stocks = Stock.query.order_by(Stock.low.desc()).all()
        else:
            stocks = Stock.query.order_by(Stock.low).all()
    else:
        if asc == 'True':
            stocks = Stock.query.order_by(Stock.high.desc()).all()
        else:
            stocks = Stock.query.order_by(Stock.high).all()
    return render_template('nav_bar.html') + render_template('stockTable.html', stocks = stocks, page = page, sortBy = sortBy, asc = asc)

'''OLD OLD OLD OLD'''


@app.route('/cat/penny')
def catPenny():
    return render_template('nav_bar.html') + render_template('catPenny_Stocks.html')


@app.route('/cat/crypto')
def catCrypto():
    return render_template('nav_bar.html') + render_template('catCryptocurrency.html')


@app.route('/stock/AAPL/')
def AAPL():
    stock = Stock.query.get('AAPL')
    return render_template('nav_bar.html') + render_template('dynamic_stock.html', stock=stock)


@app.route('/stock/HON/')
def HON():
    stock = Stock.query.get('HON')
    return render_template('nav_bar.html') + render_template('dynamic_stock.html', stock=stock)


@app.route('/stock/MRNA/', methods=['GET', 'POST'])
def MRNA():
    stock = Stock.query.get('MRNA')
    return render_template('nav_bar.html') + render_template('dynamic_stock.html', stock=stock)


# debug=True to avoid restart the local development server manually after each change to your code.
# host='0.0.0.0' to make the server publicly available.
if __name__ == "__main__":
    app.run(debug=True)
