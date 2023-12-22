#!/usr/bin/env python3
'''Task 0: Basic Flask app
'''

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    '''Config class'''

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route('/')
def index():
    '''default route'''
    return render_template("1-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
