#!/usr/bin/env python3
"""
This module initializes a Flask application with Babel for localization support
and includes language selection based on the client's Accept-Language header.
"""

from flask import Flask, render_template, request
from flask_babel import Babel
# from typing import Optional

# Create Flask application
app = Flask(__name__)


# Configure Babel
class Config:
    """
    Configuration class for Babel settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


# @babel.localeselector
def get_locale() -> str:
    """
    Determines the best match with the client's Accept-Language header.

    Returns:
        str: The best match language code or the default language if no match
        is found.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Register the locale selector function with Babel
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Renders the index page.

    Returns:
        str: The rendered HTML template as a string.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
