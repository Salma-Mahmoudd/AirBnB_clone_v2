#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome_page():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_lang(text):
    return f'C {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run()
