#!/usr/bin/env python3
""" basic flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=True)
def home() -> str:
    """ Return the home page """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
