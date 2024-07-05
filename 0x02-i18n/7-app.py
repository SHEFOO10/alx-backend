#!/usr/bin/env python3
""" 1. Basic Babel setup """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union
import pytz


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
    if locale and locale in app.config['LANGUAGES']:
        return locale
    user = g.get('user', None)
    if user and 'locale' in user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if match:
        return match
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """ Get timezone """
    timezone = request.args.get('timezone', None)
    if timezone and is_valid_timezone(timezone):
        return locale
    user = g.get('user', None)
    if user and 'timezone' in user\
    and is_valid_timezone(user['timezone']):
        return user['timezone']
    return app.config['BABEL_DEFAULT_TIMEZONE']


def is_valid_timezone(timezone):
    try:
        return bool(pytz.timezone(timezone))
    except pytz.UnknownTimeZoneError:
        return False


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
