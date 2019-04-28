from PotHoleReporter import db, loginManager
from datetime import datetime
from flask_login import UserMixin

@loginManager.user_loader
def loadUser(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    town = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"User('{self.town}', '{self.email}')"

class Towns(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    town = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Towns('{self.town}')"

class Tickets(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    town = db.Column(db.String(), nullable=False)
    size = db.Column(db.Integer(), nullable=False)
    xcord = db.Column(db.String(), nullable=False)
    ycord = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    datePosted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Tickets('{self.town}', '{self.size}', '{self.xcord}', '{self.ycord}', '{self.datePosted}')"