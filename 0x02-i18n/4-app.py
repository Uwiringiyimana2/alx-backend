#!/usr/bin/env python3
"""Flask app module"""
from flask import (
    Flask,
    render_template,
    request,
)
from flask_babel import Babel, _


app = Flask(__name__)


class Config:
    """configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Find best match with our supported languages."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    """home page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
