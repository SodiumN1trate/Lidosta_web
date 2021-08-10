from flask import Flask
from os import urandom

APP_NAME = "Lidosta"

app = Flask(APP_NAME)

SECRET_KEY = '&m\xd6\x1d\xb7N\xe8\x07\xd5;\xcd\xd8\xcf)\x1f\xed\xf8\xfd\xb3 \xcb6\x99'

app.secret_key = SECRET_KEY


