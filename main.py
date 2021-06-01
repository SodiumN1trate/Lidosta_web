from flask import Flask, render_template
app = Flask('app')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about us")
def about_us():
    return render_template("about us.html")

@app.route("/travel info")
def travel_info():
    return render_template("reissa informacija.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/passanger info")
def passanger_ticket_info():
    return render_template("passangers ticket info.html")

@app.route("/flight customization")
def flight_customization():
    return render_template("flight customization.html")

@app.route("/booking overview")
def booking_overview():
    return render_template("booking overview.html")

app.run(host='0.0.0.0', port=8080)
