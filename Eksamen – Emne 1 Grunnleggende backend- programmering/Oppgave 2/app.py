from calendar import error
from urllib import request

from flask import Flask, render_template, request, redirect

from datetime import date

from mysql.connector import Error

from database import get_stays
import database

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


@app.route("/add", methods=["GET", "POST"])
def add_stay():
    # Bruker GET to open input field page:
    if request.method == "GET":
        return render_template(
            "add_form.html", pets=database.get_pets(), rooms=database.get_rooms())

    # Bruk POST til å hente data fra HTML-skjemaet:
    form = request.form

    pet_id = form.get("pet_id", "")
    room_id = form.get("room_id", "")
    check_in = form.get("check_in", "")
    check_out = form.get("check_out", "")

    if not all([pet_id, room_id, check_in, check_out]):
        return render_template(
            "add_form.html",
            pets=database.get_pets(),
            rooms=database.get_rooms(),
            error="Alle feltene må fylles ut."
        ), 400

    try:
        check_in_date = date.fromisoformat(check_in)
        check_out_date = date.fromisoformat(check_out)

    except ValueError:
        return render_template(
            "add_form.html",
            pets=database.get_pets(),
            rooms=database.get_rooms(),
            error="Ugyldig dato."
        ), 400

    if check_out_date <= check_in_date:
        return render_template(
            "add_form.html",
            pets=database.get_pets(),
            rooms=database.get_rooms(),
            error="Utsjekksdato må være etter innsjekksdato."
        ), 400

    try:
        pet_id = int(pet_id)
        room_id = int(room_id)


    except ValueError:
        return render_template(
            "add_form.html",
            pets=database.get_pets(),
            rooms=database.get_rooms(),
            error="Ugyldig ID. Velg et kjæledyr og et rom fra listene."
        ), 400

    try:
        result = database.add_stay(
            pet_id, room_id, check_in_date, check_out_date
        )

    except Error:
        app.logger.exception("Failed to register stay")
        return render_template(
            "add_form.html",
            pets=database.get_pets(),
            rooms=database.get_rooms(),
            error="Kunne ikke registrere oppholdet."
        ), 503

    if result:
        return redirect("/stays", code=303)

    return render_template(
        "add_form.html",
        pets=database.get_pets(),
        rooms=database.get_rooms(),
        error="Rommet er allerede opptatt i valgt periode."
    ), 409



@app.route("/edit/<int:stay_id>", methods=["GET", "POST"])
def edit_stay(stay_id):

    stay = database.get_stay(stay_id)

    if stay is None:
        return "Oppholdet ble ikke funnet.", 404

    pets = database.get_pets()
    rooms = database.get_rooms()

    # GET: Vise eksisterende opphold
    if request.method == "GET":
        return render_template(
            "edit_stay.html",
            stay=stay,
            pets=pets,
            rooms=rooms
        )

    # POST: Hente data fra redigeringsskjemaet
    form = request.form

    pet_id = form.get("pet_id", "")
    room_id = form.get("room_id", "")
    check_in = form.get("check_in", "")
    check_out = form.get("check_out", "")

    # Kontrollere at alle feltene er fylt ut
    if not all([pet_id, room_id, check_in, check_out]):
        return render_template(
            "edit_stay.html",
            stay=stay,
            pets=pets,
            rooms=rooms,
            error="Alle feltene må fylles ut."
        ), 400

    # Kontrollere datoformat
    try:
        check_in_date = date.fromisoformat(check_in)
        check_out_date = date.fromisoformat(check_out)

    except ValueError:
        return render_template(
            "edit_stay.html",
            stay=stay,
            pets=pets,
            rooms=rooms,
            error="Ugyldig dato."
        ), 400

    # Kontrollere datoenes rekkefølge
    if check_out_date <= check_in_date:
        return render_template(
            "edit_stay.html",
            stay=stay,
            pets=pets,
            rooms=rooms,
            error="Utsjekksdato må være etter innsjekksdato."
        ), 400

    # Konvertere ID til heltall
    try:
        pet_id = int(pet_id)
        room_id = int(room_id)

    except ValueError:
        return render_template(
            "edit_stay.html",
            stay=stay,
            pets=pets,
            rooms=rooms,
            error="Ugyldig ID."
        ), 400

    # Kontrollere at kjæledyr og rom finnes
    valid_pet_ids = {pet.pet_id for pet in pets}
    valid_room_ids = {room.room_id for room in rooms}

    if pet_id not in valid_pet_ids or room_id not in valid_room_ids:
        return render_template(
            "edit_stay.html",
            stay=stay,
            pets=pets,
            rooms=rooms,
            error="Ugyldig valg av kjæledyr eller rom."
        ), 400

    # Oppdatere oppholdet i databasen
    try:
        result = database.update_stay(
            stay_id, pet_id, room_id, check_in_date, check_out_date
        )

    except Error:
        app.logger.exception("Failed to update stay")
        return render_template(
            "edit_stay.html",
            stay=stay,
            pets=pets,
            rooms=rooms,
            error="Kunne ikke oppdatere oppholdet."
        ), 503

    # Kontrollere resultatet
    if result:
        return redirect("/stays", code=303)

    return render_template(
        "edit_stay.html",
        stay=stay,
        pets=pets,
        rooms=rooms,
        error="Rommet er allerede opptatt i valgt periode."
    ), 409
