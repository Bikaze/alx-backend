#!/usr/bin/env python3
"""
This module initializes a Flask application with Babel for localization
support.
"""

from flask import Flask, render_template
from flask_babel import Babel

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


@app.route('/')
def index() -> str:
    """
    Renders the index page.

    Returns:
        str: The rendered HTML template as a string.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
