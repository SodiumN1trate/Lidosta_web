from re import L
from flask import render_template, redirect, request, session
from flask.helpers import url_for
import pybase64
import json
from random import randint
from settings import app
from business_logic import is_admin, admin_delete_user , admin_update_user, is_admin, is_flight_real, user_register_logic, verify_email_logic, user_login_logic, user_profile_logic, make_reservation_logic, create_message, register_new_user_to_db, get_booked_tickets_list,  get_buyed_tickets_list, leave_profile_logic, add_flight_to_db, add_airplane_to_db, add_airport_to_db, get_all_airports, get_all_airplanes, get_all_flights, update_flight, update_airplane, update_airport, delete_flight, delete_airplane, delete_airport, get_all_users, admin_add_user_to_db

@app.route("/")
def index():
    try:
        return render_template("index.html", flights=get_all_flights(), message_value=session['message']['message_value'], message_type=session['message']['message_type'])
    except:
        return render_template("index.html", flights=get_all_flights())
@app.route("/about_us")
def about_us():
    return render_template("templates/about_us.html")

@app.route("/travel_info")
def travel_info():
    return render_template("templates/travel_info.html")

@app.route("/login")
def login():
    try:
        return render_template("templates/login.html", message_value=session['message']["message_value"], message_type=session['message']["message_type"], email=session['data']['email'])
    except:
        return render_template("templates/login.html")

@app.route("/register")
def register():
    try:
        return render_template("templates/register.html", message_value=session['message']["message_value"], message_type=session['message']["message_type"], name=session['input-values']['name'], lastname=session['input-values']['lastname'], email=session['input-values']['email'])
    except:
        return render_template("templates/register.html")

@app.route("/flight_customization")
def flight_customization():
    try:
        try:
            data = json.loads(request.cookies.get('flight_data'))
            if data == 0:
                return redirect(url_for("index"))
            else:
                user_data = session["user_data"]
                return render_template("templates/flight_customization.html", data=data[0])
        except:
            return redirect(url_for("index"))
    except:
        create_message("Nepieciešams sākumā ielogoties!", "error")
        return redirect(url_for("login"))

@app.route("/passanger_info")
def passanger_ticket_info():
    try:
        flight_customization = json.loads(pybase64.b64decode(request.cookies.get('flight_customization')).decode("utf-8"))
        return render_template("templates/passangers_ticket_info.html")
    except:
        return redirect(url_for("flight_customization"))

@app.route("/booking_overview")
def booking_overview():
    try:
        persons = json.loads(pybase64.b64decode(request.cookies.get('persons')).decode("utf-8"))
        flight_customization = json.loads(pybase64.b64decode(request.cookies.get('flight_customization')).decode("utf-8"))
        return render_template("templates/booking_overview.html", departure_country=flight_customization[0], arrive_country=flight_customization[1], flight_class=flight_customization[4], passengers=len(persons), departure_time=flight_customization[2], arrive_time=flight_customization[3], flight_number=randint(1000, 10000), sum_of_all=len(persons)*int(flight_customization[5]))
    except:
        return redirect(url_for("flight_customization"))

@app.route("/profile")
def profile():
    if user_profile_logic() == 1:
        list_with_booked_tickets_for_user = get_booked_tickets_list()
        list_with_buyed_tickets_for_use = get_buyed_tickets_list()
        return render_template("templates/profile.html", name=session['user_data']['name'], lastname=session['user_data']['lastname'], email=session['user_data']['email'], wallet=session['user_data']['wallet'], role=session['user_data']['role'], reserved_tickets=list_with_booked_tickets_for_user, buyed_tickets=list_with_buyed_tickets_for_use)
    else:
        return redirect(url_for('login'))


@app.route("/standart_flights")
def standart_flights():
    return render_template("templates/standart_flights.html")

# Admin pages
@app.route("/admin")
def admin():
    try:
        if session['user_data']['role'] == 1:
            return redirect(url_for('admin_flights'))
        else:
            return redirect(url_for('login'))
    except:
        return redirect(url_for('login'))

@app.route("/admin/flights")
def admin_flights():
    if session['user_data']['role'] == 1:
        get_all_airplanes()
        return render_template("templates/administration_flights.html", airplanes=get_all_airplanes(), flights=get_all_flights(), airports=get_all_airports())
    else:
        return redirect(url_for('login'))

@app.route("/admin/airports")
def admin_airports():
    if session['user_data']['role'] == 1:
        return render_template("templates/administration_airports.html", airports=get_all_airports())
    else:
        return redirect(url_for('login'))


@app.route("/admin/airplanes")
def admin_airplanes():
    if session['user_data']['role'] == 1:
        return render_template("templates/administration_airplanes.html", airports=get_all_airports(), airplanes=get_all_airplanes())
    else:
        return redirect(url_for('login'))


@app.route("/admin/users")
def admin_users():
    if session['user_data']['role'] == 1:
        return render_template("templates/administration_users.html", users=get_all_users())
    else:
        return redirect(url_for('login'))

# User register
@app.route("/register_user", methods=["POST"])
def register_user():
    if user_register_logic() == 1:
        return render_template('templates/email_verify.html')
    else:
        return redirect(url_for('register'))


@app.route("/verify_email_checker", methods=["POST"])
def verify_email_checker():
    if verify_email_logic() == 1:
        register_new_user_to_db()
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('register'))



# Route's kas pārbauda lietotāja ievadīto informāciju
@app.route("/login_check", methods=["POST"])
def login_check():
    if user_login_logic() == 1:
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('login'))


# Route's kas aizsūta datus uz datubāzi un redirecto uz profile ar message 
@app.route("/make_reservation")
def make_reservation():
    make_reservation_logic()
    return redirect(url_for('profile'))

# Leave profile
@app.route("/leave")
def leave():
    leave_profile_logic()
    return redirect(url_for('login'))


# Admin add flight
@app.route("/admin/add_row")
def add_row():
    if session['user_data'] and is_admin(session['user_data']):
        data = json.loads(request.cookies.get('data'))[0]
        print(data)

        if data["title"] == "flights":
            add_flight_to_db(data)
            return redirect(url_for('admin_flights'))

        elif data["title"] == "airplanes":
            add_airplane_to_db(data)
            return redirect(url_for('admin_airplanes'))

        elif data["title"]  == "airports":
            add_airport_to_db(data)
            return redirect(url_for('admin_airports'))
        
        elif data["title"] == "users":
            admin_add_user_to_db(data)
            return redirect(url_for('admin_users'))
    else:
        return redirect(url_for("login"))


@app.route("/admin/edit_row")
def edit_row():
    if session['user_data'] and is_admin(session['user_data']):
        data = json.loads(request.cookies.get('edited_data'))[0]
        print(data)
        if data["title"] == "flights":
            update_flight(data)
            return redirect(url_for('admin_flights'))

        elif data["title"] == "airplanes":
            update_airplane(data)
            return redirect(url_for('admin_airplanes'))

        elif data["title"] == "airports":
            update_airport(data)
            return redirect(url_for('admin_airports'))
        
        elif data["title"] == "users":
            admin_update_user(data)
            return redirect(url_for('admin_users'))
    else:
        return redirect(url_for("login"))

@app.route("/admin/delete_row/<title>-<id>")
def delete_row(title, id):
    if session['user_data'] and is_admin(session['user_data']):
        if title == "flights":
            delete_flight(id)
            return redirect(url_for('admin_flights'))
            
        elif title == "airplanes":
            delete_airplane(id)
            return redirect(url_for('admin_airplanes'))

        elif title == "airports":
            delete_airport(id)
            return redirect(url_for('admin_airports'))

        elif title == "users":
            admin_delete_user(id)
            return redirect(url_for('admin_users'))
    else:
        return redirect(url_for("login"))
        
@app.route("/check_flight")
def check_flight():
    data = json.loads(request.cookies.get('flight_data'))
    if str(data) == "0":
        create_message("Atzīmētais lidojums neēksistē!", "error")
        return redirect(url_for('index'))
    else:
        if is_flight_real(data[0]):
            session['message'] = ""
            return redirect(url_for('flight_customization'))
        else:
            create_message("Atzīmētais lidojums neēksistē!", "error")
            return redirect(url_for('index'))
            
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
create_message
