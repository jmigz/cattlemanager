
from flask_sqlalchemy import SQLAlchemy
from . import db


db = SQLAlchemy()
class Cattle(db.Model):
    __tablename__ = 'cattle'
    id = db.Column(db.Integer, primary_key=True)
    tag_number = db.Column(db.String(20), unique=True)
    breed = db.Column(db.String(255))
    age = db.Column(db.Integer)
    weight = db.Column(db.Float)
    sex = db.Column(db.String(10))
    health_status = db.Column(db.String(255))
    vaccinations = db.Column(db.String(255))
    breeding_history = db.Column(db.String(255))
    is_removed = db.Column(db.Boolean, default=False)
    removal_reason = db.Column(db.String(20))

    def __init__(self, tag_number, breed, age, weight, sex, health_status, vaccinations, breeding_history):
        self.tag_number = tag_number
        self.breed = breed
        self.age = age
        self.weight = weight
        self.sex = sex
        self.health_status = health_status
        self.vaccinations = vaccinations
        self.breeding_history = breeding_history

def create_cattle(tag_number, breed, age, weight, sex, health_status, vaccinations, breeding_history):
    cattle = Cattle(
        tag_number=tag_number,
        breed=breed,
        age=age,
        weight=weight,
        sex=sex,
        health_status=health_status,
        vaccinations=vaccinations,
        breeding_history=breeding_history
    )
    db.session.add(cattle)
    db.session.commit()

def list_cattle():
    return Cattle.query.filter_by(is_removed=False).all()

def remove_cattle(cattle_id, removal_reason):
    cattle = Cattle.query.get(cattle_id)
    if removal_reason == 'error':
        db.session.delete(cattle)
    else:
        cattle.is_removed = True
        cattle.removal_reason = removal_reason
    db.session.commit()

def generate_tag_number(year):
    # Query the database to find the latest cattle entry for the given year
    latest_cattle = Cattle.query.filter(Cattle.tag_number.like(f'HF-{year}-%')).order_by(Cattle.id.desc()).first()

    if latest_cattle:
        # Extract the latest number from the tag number and increment it by 1
        latest_number = int(latest_cattle.tag_number.split('-')[-1])
        new_number = latest_number + 1
    else:
        new_number = 1

    # Generate the new tag number
    tag_number = f'HF-{year}-{new_number}'
    return tag_number
def add_cattle(birth_year, breed, age, weight, sex, health_status, vaccinations, breeding_history):
    tag_number = generate_tag_number(birth_year)
    create_cattle(tag_number, breed, age, weight, sex, health_status, vaccinations, breeding_history)

