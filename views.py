from re import L
from flask import render_template, redirect, request, session
from flask.helpers import flash, make_response, send_file, send_from_directory, url_for
import pybase64
import json
from random import randint
from settings import app
from business_logic import *
import os

@app.route("/")
def index():
    cards = get_all_flight_cards()
    pages = len(cards) // 3 if len(cards) % 3 == 0 else len(cards) // 3 + 1
    response = make_response(render_template("index.html", flights=get_all_flights(), pages=pages, flight_cards=cards, airplanes=get_all_airplanes()))
    response.set_cookie("cards", json.dumps(set_all_cards_in_cookies()))
    return response

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
                print("Not valid user data")
                flash("Neeksistē norādītais lidojums")
                return redirect(url_for("index"))
            else:
                user_data = session["user_data"]
                return render_template("templates/flight_customization.html", data=data[0])
        except:
            print("Cant receive user data")
            flash("Nepieciešams reģistrēties vai ieiet profilā")
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
        return render_template("templates/booking_overview.html", departure_country=flight_customization[0], arrive_country=flight_customization[1], airplane_model = flight_customization[2], flight_class=flight_customization[5], passengers=len(persons), departure_time=flight_customization[3], arrive_time=flight_customization[4], flight_number=randint(1000, 10000), sum_of_all=len(persons)*int(flight_customization[6]))
    except:
        return redirect(url_for("flight_customization"))

@app.route("/profile")
def profile():
    if user_profile_logic() == 1:
        message_type = session['message']['message_type'] if session['message'] else 0,
        message_value = session['message']['message_value'] if session['message'] else 0
        list_with_booked_tickets_for_user = get_booked_tickets_list()
        list_with_buyed_tickets_for_use = get_buyed_tickets_list()
        return render_template("templates/profile.html",
            name=session['user_data']['name'],
            lastname=session['user_data']['lastname'],
            email=session['user_data']['email'],
            wallet=session['user_data']['wallet'],
            role=session['user_data']['role'],
            reserved_tickets=list_with_booked_tickets_for_user,
            buyed_tickets=list_with_buyed_tickets_for_use,
            message_type=message_type[0],
            message_value=message_value
        )
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
    print(data)
    if str(data) == "0":
        create_message("Atzīmētais lidojums neēksistē!", "error")
        print("Selected flight doesn't exist 1")
        return redirect(url_for('index'))
    else:
        if is_flight_real(data[0]):
            session['message'] = ""
            return redirect(url_for('flight_customization'))
        else:
            create_message("Atzīmētais lidojums neēksistē!", "error")
            print("Selected flight doesn't exist 2")
            return redirect(url_for('index'))

# Lietotāja biļešu pārvalde
@app.route("/buy-ticket/<ticket_id>")
def buy_ticket(ticket_id):
    ticket = buy_ticket_logic(ticket_id)
    if ticket == 1:
        flash("Paldies! Veiksmīgi tika iegādāta biļete.")
    else:
        flash(ticket)


    return redirect(url_for("profile"))


@app.route("/edit_ticket/<ticket_id>-<owner_id>")
def edit_ticket(ticket_id, owner_id):
    data = is_ticket_owner(ticket_id, owner_id)
    if data == 0:
        print("Not valid data")
        return redirect(url_for("index"))
    else:
        return render_template("templates/user_edit_ticket.html", flight_main_data=data['ticket'], users_data=data['all_users'], ticket_id=ticket_id)


@app.route("/edit_ticket/save/<ticket_id>")
def edit_ticket_save(ticket_id):
    persons = json.loads(pybase64.b64decode(request.cookies.get('persons')).decode("utf-8"))
    if update_user_ticket_users(persons, ticket_id) == 1:
        flash("Veiksmīgi tika veiktais izmaiņas rezervācijā!")
        return redirect(url_for('profile'))
    else:
        return "Error"

@app.route("/upload/<ticket_id>-<owner_id>")
def upload_reservation(ticket_id, owner_id):
    data = is_ticket_owner(ticket_id, owner_id)
    if data == 0:
        return redirect(url_for("profile"))
    else:
        html_content = f'''
            <table>
                <tr>
                    <th>{data["owner"].name + " " + data["owner"].lastname}</th>
                    <th>Rez. Nr. {1}</th>
                </tr>
                <tr>
                    <th>Lidojums</th>
                    <th>{data["ticket"].departure + "-" + data["ticket"].arrive}</th>
                </tr>
                <tr>
                    <th>Izlidošana</th>
                    <th>{data["ticket"].departure_time}</th>
                </tr>
                <tr>
                    <th>Izlidošana</th>
                    <th>{data["ticket"].arrive_time}</th>
                </tr>
                <tr>
                    <th>Lidmašīna</th>
                    <th>{data["ticket"].airplane_name}</th>
                </tr>
            </table>
        
        '''
        html_text = '''
            <!DOCTYPE html>
            <html lang="lv">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                    <style>
                        table, th{
                            text-align: left;
                            border: 1px solid black;
                            border-collapse: collapse;
                        }
                        th{
                            width: 300px;
                        }
                    </style>
                </head>
                <body>
                    ''' + html_content + '''
                </body>
            </html>
        '''
        path = os.getcwd()
        file = open(path+f"\media\{ data['owner'].name }_reserved_ticket.html", "w",  encoding="utf-8")
        file.write(html_text)
        file.close()
        return send_file(path+f"\media\\{data['owner'].name}_reserved_ticket.html", as_attachment=True)

@app.route("/delete/<ticket_id>-<owner_id>")
def delete_reservation(ticket_id, owner_id):
    data = is_ticket_owner(ticket_id, owner_id)
    if data == 0:
        return redirect(url_for("index"))
    else:
        delete_user_reservation(ticket_id, owner_id)
        flash("Veiksmīgi tika dzēsta rezervācijā!")
        return redirect(url_for('profile'))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
