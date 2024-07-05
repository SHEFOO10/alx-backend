#!/usr/bin/env python3
""" 1. Basic Babel setup """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


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
    if locale:
        return locale
    user = g.get('user', None)
    user_locale = user['locale'] if user else None
    if user_locale:
        return user_locale
    match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if match:
        return match
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index() -> str:
    """ Returns home page """
    return render_template('6-index.html')


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """ get logged in user """
    login_as = request.args.get('login_as')
    return users.get(int(login_as), None) if login_as else None


@app.before_request
def before_request():
    """ Before Request """
    user = get_user()
    if user:
        g.user = user


@app.context_processor
def inject_user():
    """Inject user into the template context."""
    user = g.get('user', None)
    if user:
        return dict(user=user)
    return dict()


if __name__ == '__main__':
    app.run()
