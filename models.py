# models.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password

def create_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

def list_users():
    return User.query.all()

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        return True

    return False
