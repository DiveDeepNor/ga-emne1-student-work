from urllib import request

from flask import Flask, render_template, redirect
from flask import render_template
from flask import request

from mysql.connector import Error

from models import Stays

from database import get_stays

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def index():
    return render_template(
        "index.html",
        heading = "Eksamensoppgave Goxstad Akademiet"
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        author = "Njaal Birkeland!"
    )


@app.route("/stays")
def stays():
    try:
        rows = get_stays()

    except Error:
        app.logger.exception("Database query failed")
        return "Database unavailable", 503

    return render_template("stays.html", rows=rows)