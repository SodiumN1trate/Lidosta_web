from flask import Flask, render_template, request, make_response, redirect, session
from flask.helpers import flash, url_for
import pybase64
import json
from random import randint
from flask_recaptcha import ReCaptcha
from settings import app
from models import db, User
import datetime


# Captcha settings
recaptcha = ReCaptcha(app=app)
app.config.update(dict(
    RECAPTCHA_ENABLED=True,
    RECAPTCHA_SITE_KEY="6LePVSIbAAAAAMVD_H17vqNVz-7ZSVINa2Ku_dXf",
    RECAPTCHA_SECRET_KEY="6LePVSIbAAAAALG5bw2x34zifd4_874CIfMrTA64"
))
recaptcha = ReCaptcha()
recaptcha.init_app(app)


def create_message(message_value, message_type):
    if message_type.lower() == "error" or message_type.lower() == "succes":
        session['message'] = ""
        session['message'] = {"message_value": message_value,
                            "message_type": message_type}

def user_register_logic():
    if request.method == "POST":
        data = request.form  # Tiek iegūti ievadītie dati

        for row in data:  # Cikls kas pārbauda vai kāds no ievadītajiem laukiem nav tukšs
            if data[row] == "":
                create_message("Aizpildiet visus laukus!", "error")

        if recaptcha.verify():  # Ja recaptcha ir apstiprināts
            # Pārbauda vai ievadītās paroles garums ir vismaz 8 simboli
            if len(data['password']) < 8:
                create_message("Parolei jābūt vismaz 8 simbolus garai!", "error")

            # Pārbauda vai ievadītās paroles ir vienādas
            elif data['password'] != data['re-password']:
                create_message("Ievadītās paroles nesakrīt!", "error")
            else:
                user_exist = User.query.filter_by(
                    name=data['name'], lastname=data['lastname']).first()
                email_exist = User.query.filter_by(
                    email=data['email']).first()

                if user_exist != None:  # Datubāzē pārbauda vai lietotājs ar tādu vārdu un uzvārdu jau neeksistē
                    create_message("Lietotājs ar tādu vārdu un uzvārdu ir reģistrēts!", "error")

                elif email_exist != None:  # Pārbauda vai e-pasts jau nav aizņemts
                    create_message("Lietotājs ar tādu e-pastu ir jau reģistrēts!", "error")

                else:  # Ja visas pārbaudes ir izietas tad lietotājs tiek reģistrēts. Dati tiek aizsūtīti uz datubāzi.
                    user = User(name=data['name'], lastname=data['lastname'],
                                email=data['email'], password=data['password'], register_date=datetime.datetime.now())
                    db.session.add(user)
                    db.session.commit()
                    return 1

            
    else:  # Ja recaptcha nav apstiprināts
        create_message("Atzīmējat ka nēsat robots!", "error")

    # Visi ievadītie dati tiek saglabāti sesijā tālākai apstrādei
    session['input-values'] = data
