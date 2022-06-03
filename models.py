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
    wallet = db.Column(db.Float, default=0)
    role = db.Column(db.Integer, default=0) 
    ticket = db.relationship("Ticket", cascade="all, delete")

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name, 
            'lastname': self.lastname,
            'email': self.email,
            'register_date': self.register_date,
            'wallet': self.wallet,
            'role': self.role
        }

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
    airplane_name = db.Column(db.String(80), nullable=True)
    user_ticket = db.relationship("UserTicket", cascade="all, delete")

    def __repr__(self):
        return '<Ticket %r>' % self.owner_id

    def serialize(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'departure': self.departure,
            'arrive': self.arrive,
            'departure_time': self.departure_time,
            'flight_class': self.flight_class,
            'arrive_time': self.arrive_time,
            'people_count': self.departure_time,
            'sum': self.flight_class,
            'flight_id': self.arrive_time,
            'company_name': self.departure_time,
            'reserved_status': self.flight_class,
            'airplane_name': self.arrive_time
        }

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
    
    def serialize(self):
        return {
            'id': self.id,
            'ticket_id': self.ticket_id,
            'name': self.name,
            'lastname': self.lastname,
            'person_id': self.person_id,
            'birth_day': self.birth_day,
            'birth_month': self.birth_month,
            'birth_year': self.birth_year,
            'mobile_number': self.mobile_number
        }

class Airport(db.Model):
    __tablename__ = "airport"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    abbreviation = db.Column(db.String(6), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    children = db.relationship("Airplane", cascade="all, delete")

    def __repr__(self):
        return '<Airport %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'abbreviation': self.abbreviation,
            'address': self.address,
            'airplanes': self.children
        }

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

    def serialize(self):
        return {
            'id': self.id,
            'model_name': self.model_name,
            'manufacture_year': self.manufacture_year,
            'seats_count': self.seats_count,
            'airport_id': self.airport_id
        }

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
    description = db.Column(db.Text, nullable=True)
    image_link = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Flight {self.departure} -> {self.arrive} >'

    def serialize(self):
        return {
            'id': self.id,
            'departure': self.departure,
            'arrive': self.arrive,
            'departure_date': self.departure_date,
            'arrive_date': self.arrive_date,
            'departure_time': self.departure_time,
            'arrive_time': self.arrive_time,
            'airplane_id': self.airplane_id,
            'flight_price': self.flight_price,
            'description': self.description,
            'image_link': self.image_link
        }
