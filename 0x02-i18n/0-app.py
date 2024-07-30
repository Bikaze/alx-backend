#!/usr/bin/env python3
"""
This module initializes a Flask application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Renders the index page.

    Returns:
        str: The rendered HTML template as a string.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
