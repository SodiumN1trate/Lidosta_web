from flask import Flask

# Šeit var un vajaga veidot aplikācijas globālos mainīgo, ja nepieciešams

APP_NAME = "Lidosta"

app = Flask(APP_NAME)

SECRET_KEY = '\x9c2;\xeew5d/.)_\x00\xf0:\xc8\x92x?\x8bwo\xf2NB'

app.secret_key = SECRET_KEY
