#!/usr/bin/env python3
""" 1. Basic Babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Config Class for languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages """
    locale = request.args.get('locale', None)
    return (
        locale if locale
        else request.accept_languages.best_match(app.config['LANGUAGES'])
    )


@app.route('/')
def index() -> str:
    """ Returns home page """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
