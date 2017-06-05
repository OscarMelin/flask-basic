# -*- coding: utf-8 -*-

from webapp import app
from flask import Flask, render_template

@app.route("/")
def index():
    return render_template("main.html")
