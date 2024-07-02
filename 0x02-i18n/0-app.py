#!/usr/bin/env python3
""" basic flask app """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def home() -> str:
    """ Return the home page """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
