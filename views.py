from flask import render_template, redirect, request, session
from flask.helpers import url_for
import pybase64
import json
from random import randint
from settings import app
from business_logic import user_register_logic

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
    try: # Mēģina iegūt vajadzīgās sesijas
        return render_template("templates/register.html", message_value=session['message']["message_value"], message_type=session['message']["message_type"], name=session['input-values']['name'], lastname=session['input-values']['lastname'], email=session['input-values']['email'])
    except: # Ja netiek atrastas vajadzīgās sesijas, tiek vienkārši aizsūtīta .html lapa
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



# User register
@app.route("/register_user", methods=["POST"])
def register_user():
    if user_register_logic() == 1:
        return "Reģistrēts!"
    else:
        return redirect(url_for('register'))

  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

