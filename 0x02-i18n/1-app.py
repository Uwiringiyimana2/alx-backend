#!/usr/bin/env python3
"""Flask app module"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """configure available languages"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)


@app.route("/")
def home():
    """home page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
