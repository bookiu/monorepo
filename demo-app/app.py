#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"


@app.route("/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    app.run(debug=True)
