from email import message
from flask import Flask, request, session, render_template
from flask.helpers import flash, url_for
from flask_sqlalchemy import model
import pybase64
import json
from random import randint
from flask_recaptcha import ReCaptcha
from settings import app
from models import Airport, Ticket, db, User, UserTicket, Flight, Airplane
import datetime
from flask_mail import Mail, Message

#Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lidostainfo@gmail.com'
app.config['MAIL_PASSWORD'] = 'lidostainfo123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Captcha settings
recaptcha = ReCaptcha(app=app)
app.config.update(dict(
    RECAPTCHA_ENABLED=True,
    RECAPTCHA_SITE_KEY="6LePVSIbAAAAAMVD_H17vqNVz-7ZSVINa2Ku_dXf",
    RECAPTCHA_SECRET_KEY="6LePVSIbAAAAALG5bw2x34zifd4_874CIfMrTA64"
))
recaptcha = ReCaptcha()
recaptcha.init_app(app)


'''
Funkcija kas izveido ziņu lietotājam. Funkcija pieņem ziņas tekstu un ziņas tipu (error, succes).
Funkcija atgriež sesiju ar izveidoto ziņu.
'''
def create_message(message_value, message_type):
    if message_type.lower() == "error" or message_type.lower() == "succes":
        session['message'] = {"message_value": message_value, "message_type": message_type}
'''
Funkcija kas pārbauda sarakstu uz tukšiem laukiem. Funkcija pieņem sarakstu.
Atgriež 1 jeb True, ja sarakstā ir tukšs lauks.
'''
def array_check_on_gaps(array):
    for row in array: 
        if array[row] == "":
            return 1

'''
Funkcija kas aizsūta verifikācijas kodu uz gmail e-pastu. Funkcija pieņem saņēmēja e-pastu.
Tiek atgriests 1 jeb True kad izdevās aizsūtīt kodu uz e-pastu. Tiek atgriests 0 jeb False, ja nav izdevies aizsūtīt kodu.
Funkcija verifikācijas kodu saglabā sesijā
'''
def send_verification_email(receiver_email):
    try:
        verification_code = str(randint(10000, 100000))
        message_to_sent = f"Verifikācijas kods: {verification_code}"
        message = Message("E-pasta verifikācija \"Lidosta\"",
                            sender='lidostainfo@gmail.com', recipients=[receiver_email])
        message.html = render_template(
            "mail_templates/verification_code.html", verification_code=verification_code)
        mail.send(message)
        session["verification_code"] = verification_code
        return 1
    except:
        return 0


'''
Salīdzina vai lietotāja ierakstītais verifikācijas kods ir vienāds ar aizsūtīto.
'''
def verify_email_logic():
    if request.method == "POST":
        user_typed_verification_code = request.form
        if user_typed_verification_code['ver_code'] == session["verification_code"]:
            session["verification_code"] = None
            session["message"] = None
            return 1
        else:
            return 0

'''
Lietotāja reģistrēšanās loģika.
'''
def user_register_logic():
    if request.method == "POST":
        data = request.form  # Tiek iegūti ievadītie dati
        session['input-values'] = data

        if array_check_on_gaps(data) == 1:  # Pārbauda uz tukšajiem laukiem
            create_message("Aizpildiet visus laukus!", "error")
        else:
            if recaptcha.verify():  # Ja recaptcha ir apstiprināts
                # Pārbauda vai ievadītās paroles garums ir vismaz 8 simboli
                if len(data['password']) < 8:
                    create_message("Parolei jābūt vismaz 8 simbolus garai!", "error")

                # Pārbauda vai ievadītās paroles ir vienādas
                elif data['password'] != data['re-password']:
                    create_message("Ievadītās paroles nesakrīt!", "error")

                else:
                    email_exist = User.query.filter_by(email=data['email']).first()

                    if email_exist != None:  # Pārbauda vai e-pasts jau nav aizņemts
                        create_message("Lietotājs ar tādu e-pastu ir jau reģistrēts!", "error")
                    else:  # Ja visas pārbaudes ir izietas tad tiek pārbaudīts e-pasts.
                        if send_verification_email(data['email']) == 1: # Ja uz e-pastu var aizsūtīt verifikācijas kodu, tad e-pasts eksistē.
                            print("E-pasts aizsūtīts!")
                            return 1 # Tiek atgriests 1 jeb True, lai views.py (routers) lietotāju varētu pārnest uz lapu kur jāieraksta kods.
                        else: # Ja nav izdevies aizsūtīt e-pastu tad tiek atgriezta kļuda ar paziņojumu
                            create_message("Ievadītais e-pasts neēksistē!", "error")
       
            else:  # Ja recaptcha nav apstiprināts
                create_message("Atzīmējat ka nēsat robots!", "error")
    return 0
def register_new_user_to_db():
    try:
        data = session['input-values']
        user = User(name=data['name'], lastname=data['lastname'],
                    email=data['email'], password=pybase64.standard_b64encode(bytes(data['password'], "utf-8")), role=0, register_date=datetime.datetime.now(), wallet=100.0)
        db.session.add(user)
        db.session.commit()
        session["user_data"] = {'name': user.name, 'lastname': user.lastname,
                                'email': user.email, 'id': user.id, 'role': user.role, 'wallet': float(user.wallet)}
        print(session["user_data"])
        session['data'] = None
        return 1
    except:
        return 0
        
def user_login_logic():
    if request.method == "POST":
        data = request.form
        session['data'] = data
        find_user = User.query.filter_by(email=data['email']).first()
        if find_user != None:
            if pybase64.standard_b64decode(find_user.password).decode("utf-8") == data['password']:
                session["input-values"] = None
                session["verification_code"] = None
                session["message"] = None
                session["user_data"] = {'name': find_user.name, 'lastname': find_user.lastname, 'email': find_user.email, 'id':find_user.id, 'role':find_user.role, 'wallet':float(find_user.wallet)}
                return 1
        
        create_message("Kļūda! Pārbaudiet vai ievadītais e-pasts un/vai parole ir ievadīta pareizi!", "error")
    return 0

def get_user_data(id):
    try:
        find_user = User.query.filter_by(id=id).first()
        session["user_data"] = {'name': find_user.name, 'lastname': find_user.lastname,
                                'email': find_user.email, 'id': find_user.id, 'role': find_user.role, 'wallet': float(find_user.wallet)}
        return 1
    except:
        return 0

def user_profile_logic():
    try:
        if get_user_data(session["user_data"]['id']) == 1:
            return 1
        else:
            return 0
    except:
        return 0


def make_reservation_logic():
    user_data = session["user_data"]
    print("Id:", user_data["id"])
    persons = json.loads(pybase64.b64decode(request.cookies.get('persons')).decode("utf-8"))
    flight_customization = json.loads(pybase64.b64decode(request.cookies.get('flight_customization')).decode("utf-8"))
    ticket = Ticket(owner_id=user_data['id'],
                    departure=flight_customization[0],
                    arrive=flight_customization[1],
                    flight_class=flight_customization[4],
                    departure_time=flight_customization[2],
                    arrive_time=flight_customization[3],
                    people_count=len(persons),
                    sum=int(flight_customization[5]) * len(persons),
                    flight_id=randint(1000, 10000),
                    company_name="Lidosta",
                    reserved_status=0
                    )
    db.session.add(ticket)
    db.session.commit()
    for person in persons:
        ticket_for_person = UserTicket(ticket_id=ticket.id,
                                       name=person["name"],
                                       lastname=person["lastname"],
                                       person_id=person["person-id"],
                                       birth_day=person["birth-day"],
                                       birth_month=person["birth-month"],
                                       birth_year=person["birth-year"],
                                       mobile_number=person["telephone-number"]
                                      )
        db.session.add(ticket_for_person)
        db.session.commit()


def get_booked_tickets_list():
    list_of_tickets = Ticket.query.filter_by(owner_id=session['user_data']['id'], reserved_status=0).all()
    return list_of_tickets

def get_buyed_tickets_list():
    list_of_tickets = Ticket.query.filter_by(owner_id=session['user_data']['id'], reserved_status=1).all()
    return list_of_tickets

def leave_profile_logic():
    session["user_data"] = None


def add_flight_to_db(data):
    airplane_id = Airplane.query.filter_by(model_name=data["airplane"]).first().id
    print("airplane id:", airplane_id)
    flight = Flight(
        departure = data["departure"],
        arrive = data["arrive"],
        departure_date = data["departure_date"],
        arrive_date = data["arrive_date"],
        departure_time = data["departure_time"],
        arrive_time = data["arrive_time"],
        flight_price = data["price"],
        airplane_id = airplane_id 
    )
    db.session.add(flight)
    db.session.commit()

def add_airplane_to_db(data):
    airport_id = Airport.query.filter_by(name=data["airport"]).first().id
    airplane = Airplane(
        model_name = data["airplane_model"],
        manufacture_year = data["airplane_manufacture_year"],
        seats_count = data["airplane_seats_count"],
        airport_id = airport_id
    )
    db.session.add(airplane)
    db.session.commit()

def add_airport_to_db(data):
    airport = Airport(
        name = data['airport_name'],
        abbreviation = data['airport_abbreviation'],
        address = data['airport_address']
    )
    db.session.add(airport)
    db.session.commit()


def admin_add_user_to_db(data):
    user = User(
        name = data["name"],
        lastname = data["lastname"],
        email = data["email"],
        password= pybase64.standard_b64encode(bytes(data['password'], "utf-8")),
        register_date = "Admin registred",
        wallet = data["wallet"],
        role = 1 if data["role"] == "Administrators" else  0
    )
    db.session.add(user)
    db.session.commit()

def get_all_airports():
    return Airport.query.all()
    

def get_all_airplanes():
    return Airplane.query.all()


def get_all_flights():
    return Flight.query.all()

def get_all_users():
    return User.query.all()


def update_flight(data):
    flight = Flight.query.filter_by(id=data['id']).first()
    flight.departure = data['departure']
    flight.arrive = data['arrive']
    flight.departure_date = data['departure_date']
    flight.arrive_date = data['arrive_date']
    flight.departure_time = data['departure_time']
    flight.arrive_time = data['arrive_time']
    flight.flight_price = data['price']
    db.session.add(flight)
    db.session.commit()

def update_airplane(data):
    airplane = Airplane.query.filter_by(id=data['id']).first()
    airplane.model_name = data['airplane_model']
    airplane.manufacture_year = data['airplane_manufacture_year']
    airplane.seats_count = data['airplane_seats_count']
    db.session.add(airplane)
    db.session.commit()

def update_airport(data):
    airport = Airport.query.filter_by(id=data['id']).first()
    airport.name = data['airport_name']
    airport.abbreviation = data['airport_abbreviation']
    airport.address = data['airport_address']
    db.session.add(airport)
    db.session.commit()


def admin_update_user(data):
    user = User.query.filter(User.id == data['id']).first()
    user.name = data['name']
    user.lastname = data['lastname']
    user.email = data['email']
    user.wallet = data['wallet']
    user.role = 1 if data["role"] == "Administrators" else 0
    db.session.add(user)
    db.session.commit()


def delete_flight(id):
    db.session.delete(Flight.query.filter(Flight.id == id).first())
    db.session.commit()

def delete_airplane(id):
    db.session.delete(Airplane.query.filter(Airplane.id == id).first())
    db.session.commit()

def delete_airport(id):
    db.session.delete(Airport.query.filter(Airport.id == id).first())
    db.session.commit()

def admin_delete_user(id):
    db.session.delete(User.query.filter(User.id == id).first())
    db.session.commit()

def is_flight_real(data):
    flight_is_real = Flight.query.filter(
        Flight.departure == data['departure'],
        Flight.arrive == data['arrive'],
        Flight.departure_date == data['departure_date'],
        Flight.arrive_date == data['arrive_date'],
        Flight.departure_time == data['departure_time'],
        Flight.arrive_time == data['arrive_time'],
        Flight.flight_price == data['price']
    ).first()
    if flight_is_real == None:
        return 0
    else:
        return 1

def is_admin(data):
        return True if data['role'] == 1 else False


def buy_ticket_logic(id):
    ticket = Ticket.query.filter(Ticket.id == id, Ticket.owner_id == session['user_data']['id'], Ticket.reserved_status == 0).first()
    if ticket == None:
        return "Tādas biļetes nav"
    else:
        if ticket.sum <= session['user_data']['wallet']:
            # Buy ticket
            ticket.reserved_status = 1
            db.session.add(ticket)
            user = User.query.filter(User.id == session['user_data']['id']).first()
            user.wallet -= ticket.sum
            db.session.add(user)
            db.session.commit()
            return 1
        else:
            return "Nepietiek līdzekļu"
