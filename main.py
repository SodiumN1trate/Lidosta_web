# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, make_response
import pybase64
import json
from random import randint
app = Flask('app')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    return render_template("templates/about_us.html")

@app.route("/travel_info")
def travel_info():
    return render_template("templates/travel_info.html")

@app.route("/login")
def login():
    return render_template("templates/login.html")

@app.route("/register")
def register():
    return render_template("templates/register.html")

@app.route("/flight_customization")
def flight_customization():
    return render_template("templates/flight_customization.html")

@app.route("/passanger_info")
def passanger_ticket_info():
    return render_template("templates/passangers_ticket_info.html")

@app.route("/booking_overview")
def booking_overview():
    persons = json.loads(pybase64.b64decode(request.cookies.get('persons')))
    print(persons)
    flight_customization = json.loads(pybase64.b64decode(request.cookies.get('flight_customization')))
    print(flight_customization)
    return render_template("templates/booking_overview.html", departure_country=flight_customization[0], arrive_country=flight_customization[1], flight_class=flight_customization[2], passengers=len(persons), departure_time=flight_customization[3], arrive_time=flight_customization[4], flight_number=randint(1000, 10000), sum_of_all=len(persons)*int(flight_customization[5]))

@app.route("/profile")
def profile():
    return render_template("templates/profile.html")

@app.route("/standart_flights")
def standart_flights():
    return render_template("templates/standart_flights.html")

@app.route("/admin")
def admin():
    return render_template("templates/administration.html")

app.run(host='0.0.0.0', port=8080)

