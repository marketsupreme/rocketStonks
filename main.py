#!/usr/bin/env python3

# ---------------------------
# projects/IDB3/main.py
# Fares Fraij
# ---------------------------

from flask import Flask, render_template

app = Flask(__name__)

# ------------
# index
# ------------


@app.route('/')
def index():
    return render_template('hello.html')

# ------------
# book
# ------------


@app.route('/book/')
def book():
    return render_template('book.html')


# projections page
@app.route('/projections/')
def projections():
    return render_template('projections.html')


# debug=True to avoid restart the local development server manually after each change to your code.
# host='0.0.0.0' to make the server publicly available.
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
