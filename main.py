from flask import Flask, render_template
app = Flask('app')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/travel_info")
def travel_info():
    return render_template("reissa_informacija.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/passanger_info")
def passanger_ticket_info():
    return render_template("passangers_ticket_info.html")

@app.route("/flight_customization")
def flight_customization():
    return render_template("flight_customization.html")

@app.route("/booking_overview")
def booking_overview():
    return render_template("booking_overview.html")

@app.route("/travel_menu")
def travel_menu():
    return render_template("standarta_piedavajums.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/standart flights")
def standart_flights():
    return render_template("standarta piedavajums.html")

app.run(host='0.0.0.0', port=8080)

