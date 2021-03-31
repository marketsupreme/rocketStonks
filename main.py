#!/usr/bin/env python3
# projects/IDB3/main.py
# Fares Fraij

from flask import Flask, render_template, Response
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from create_db import app, db, Stock, create_stocks



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
    stock = Stock.query.get(stockName)
    return render_template('nav_bar.html') + render_template('dynamic_stock.html', stock = stock)

@app.route('/static/images/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype = 'image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(10)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

@app.route('/stock/projection/<stockName>')
def stockProjection(stockName):
    return render_template('nav_bar.html') + render_template('dummy_link.html')


# debug=True to avoid restart the local development server manually after each change to your code.
# host='0.0.0.0' to make the server publicly available.
if __name__ == "__main__":
    app.run(debug=True)
