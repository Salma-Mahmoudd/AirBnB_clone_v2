#!/usr/bin/python3
"""Script that starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(esc):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities():
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == '__main__':
    app.run()
