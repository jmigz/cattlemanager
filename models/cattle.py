from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models import db
from flask import current_app

class Cattle(db.Model):
    __tablename__ = 'cattle'
    id = db.Column(db.Integer, primary_key=True)
    tag_number = db.Column(db.String(20), unique=True)
    breed = db.Column(db.String(255))
    birth_date = db.Column(db.Date)
    age = db.Column(db.Integer)
    weight = db.Column(db.Float, default=0.0)
    sex = db.Column(db.String(10))
    health_status = db.Column(db.String(255), default='')
    is_pregnant = db.Column(db.Boolean, default=False)
    vaccinations = db.Column(db.String(255), default='')
    breeding_history = db.Column(db.String(255), default='')
    is_removed = db.Column(db.Boolean, default=False)
    removal_reason = db.Column(db.String(20))

    def __init__(self, breed, sex, birth_date,is_pregnant):
        super().__init__()  # Call parent constructor
        self.breed = breed
        self.birth_date = birth_date
        self.sex = sex
        self.age = self.calculate_age()
        self.tag_number = self.generate_tag_number()
        self.health_status = 'Healthy'
        self.vaccinations = 'None'
        self.breeding_history = 'None'
        self.is_pregnant = is_pregnant
        self.removal_reason = ''
        

    def calculate_age(self):
        current_year = datetime.now().year
        birth_year = self.birth_date.year
        return current_year - birth_year + 1

    def generate_tag_number(self):
        year = self.birth_date.year
        
        month= self.birth_date.month

        latest_cattle = Cattle.query.filter(Cattle.tag_number.like(f'HF-{year}-{month}-%')).order_by(Cattle.id.desc()).first()

        if latest_cattle:
            latest_number = int(latest_cattle.tag_number.split('-')[-1])
            new_number = latest_number + 1
        else:
            new_number = 1

        return f'HF-{str(year)[-2:]}-{month}-{new_number}'

   

    def remove(self, removal_reason):
        if removal_reason == 'death':
            self.is_removed = True
            self.removal_reason = 'Death'
        elif removal_reason == 'sold':
            self.is_removed = True
            self.removal_reason = 'Sold'
        elif removal_reason == 'mistake':
            db.session.delete(self)
            return  # Exit the method after deleting the object

        db.session.commit()

    @staticmethod
    def add_cattle(breed, birth_date, sex, is_pregnant):
        cattle = Cattle(breed=breed, sex=sex, birth_date=birth_date, is_pregnant=is_pregnant)
        db.session.add(cattle)
        db.session.commit()
