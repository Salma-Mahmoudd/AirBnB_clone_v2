#!/usr/bin/python3
"""Script that starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(esc):
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    return render_template("7-states_list.html", states=storage.all(State))


@app.route("/states/<id>", strict_slashes=False)
def state_with_cities(id):
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html", state="Not found!")


if __name__ == '__main__':
    app.run()
