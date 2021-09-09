#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Flask Route Definitions"""

from flask import Flask     #from the flask package, import the Flask class

app = Flask(__name__)       # instantiate the Flask class with a parameter __name__ into "app"

@app.route("/")             # @app.route is a decorator that wraps the function underneath it
def index():                # view function that is being wrapped
    return "<h1>Hello World</h1>"


@app.route("/about")
def about_me():
    me = {
        "name": "Nathan",
        "last_name": "Vik",
        "age": 32,
        "address": {
            "street": "Reef Ct",
            "number": 1234
            },
        "email": "nathan.t.vik@gmail.com",
        "bool": True,
        }
    return me