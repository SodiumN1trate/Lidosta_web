from settings import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Databse
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lidosta_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# Migrate
migrate = Migrate(app, db, render_as_batch=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    register_date = db.Column(db.String(50), nullable=True)
    
    def __repr__(self):
        return '<User %r>' % self.name
