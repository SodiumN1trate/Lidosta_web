from sqlalchemy.orm import backref
from settings import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData

# Database

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

_metadata = MetaData(naming_convention=convention)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lidosta_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app, metadata=_metadata)

# Migrate
migrate = Migrate(app, db, render_as_batch=True)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    register_date = db.Column(db.String(50), nullable=True)
    role = db.Column(db.Integer, default=0) 
    ticket = db.relationship("Ticket", cascade="all, delete")

    def __repr__(self):
        return '<User %r>' % self.name

class Ticket(db.Model):
    __tablename__ = "ticket"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    departure = db.Column(db.String(80), nullable=False)
    arrive = db.Column(db.String(80), nullable=False)
    departure_time = db.Column(db.String(80), nullable=False)
    flight_class = db.Column(db.String(80), nullable=False)
    arrive_time = db.Column(db.String(80), nullable=False)
    people_count = db.Column(db.Integer, nullable=False)
    sum = db.Column(db.Integer, nullable=False)
    flight_id = db.Column(db.Integer, nullable=False)
    company_name = db.Column(db.String(80), nullable=False)
    reserved_status = db.Column(db.Integer, default=0)
    user_ticket = db.relationship("UserTicket", cascade="all, delete")

    def __repr__(self):
        return '<Ticket %r>' % self.owner_id

class UserTicket(db.Model):
    __tablename__ = "user_ticket"
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey("ticket.id"))
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    person_id = db.Column(db.Integer, nullable=False)
    birth_day = db.Column(db.Integer, nullable=False)
    birth_month = db.Column(db.Integer, nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    mobile_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<UserTicket %r>' % self.name

class Airport(db.Model):
    __tablename__ = "airport"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    abbreviation = db.Column(db.String(6), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    children = db.relationship("Airplane", cascade="all, delete")

    def __repr__(self):
        return '<Airport %r>' % self.name


class Airplane(db.Model):
    __tablename__ = "airplane"
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(80), nullable=False)
    manufacture_year = db.Column(db.Integer, nullable=False)
    seats_count = db.Column(db.Integer, nullable=False)
    airport_id = db.Column(db.Integer, db.ForeignKey("airport.id"))
    children = db.relationship("Flight", cascade="all, delete")

    def __repr__(self):
        return '<Airplane %r>' % self.model_name

class Flight(db.Model):
    __tablename__ = "flight"
    id = db.Column(db.Integer, primary_key=True)
    departure = db.Column(db.String(80), nullable=False)
    arrive = db.Column(db.String(80), nullable=False)
    departure_date = db.Column(db.String(80), nullable=False)
    arrive_date = db.Column(db.String(80), nullable=False)
    departure_time = db.Column(db.String(80), nullable=False)
    arrive_time = db.Column(db.String(80), nullable=False)
    airplane_id = db.Column(db.Integer, db.ForeignKey("airplane.id"))
    flight_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Flight {self.departure} -> {self.arrive} >'
