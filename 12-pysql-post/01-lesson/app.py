from urllib import request

from flask import Flask, render_template, redirect
from flask import render_template
from flask import request

from mysql.connector import Error

from database import get_cities
import database

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return render_template(
        "index.html",
        heading = "Lesson 12: World exploring"
    )

@app.route("/about")
def about():
    return render_template(
        "about.html",
        author = "Njaal Birkeland!"
    )

@app.route("/cities")
def cities():
    code = request.args.get("country", "NOR").strip().upper()
    if (len(code) !=3 or not code.isascii() or not code.isalpha()):
        return "Invalid code", 400
    try:
        rows = get_cities(code)
    except Error:
        app.log_exception("Database query failed")
        return "Database unavaileble", 503

    return render_template("cities.html", code=code, rows=rows)


@app.route("/add", methods=["GET", "POST"])
def add_city():
    # Uses GET to open input field page:
    if request.method == "GET":
        return render_template(
            "city_form.html",
            name="",
            city_id=None
        )
    # Uses POST to store city data in DB:
    name = request.form.get("name", "").strip()
    if not name or len(name) > 35:
        return "Invalid city name", 400
    database.insert_city(name)
    return redirect("/cities", code=303)


@app.route("/city/<int:city_id>")
def show_city(city_id):
    city = database.get_city(city_id)
    if city is None:
        return "City not found", 404
    return render_template("city_form.html",name=city.name,city_id=city.id)



