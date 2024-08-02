#!/usr/bin/env python3
"""Flask app module"""
import pytz
from flask import (
    Flask,
    render_template,
    request,
    g,
)
from flask_babel import Babel, _, format_datetime
from typing import Union, Dict


app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


@babel.timezoneselector
def get_timezone() -> set:
    """Retrieves Timezone for a website"""
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@babel.localeselector
def get_locale() -> str:
    """Find best match with our supported languages."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    head_locale = request.args.get('locale', '')
    if head_locale in app.config['LANGUAGES']:
        return head_locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route("/")
def home() -> str:
    """home page"""
    g.time = format_datetime()
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
