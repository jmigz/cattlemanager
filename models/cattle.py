from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models import db

class Cattle(db.Model):
    __tablename__ = 'cattle'
    id = db.Column(db.Integer, primary_key=True)
    tag_number = db.Column(db.String(20), unique=True)
    breed = db.Column(db.String(255))
    birth_year = db.Column(db.Integer)
    age = db.Column(db.Integer)
    weight = db.Column(db.Float, default=0.0)
    sex = db.Column(db.String(10))
    health_status = db.Column(db.String(255), default='')
    vaccinations = db.Column(db.String(255), default='')
    breeding_history = db.Column(db.String(255), default='')
    is_removed = db.Column(db.Boolean, default=False)
    removal_reason = db.Column(db.String(20))

    def __init__(self, breed, birth_year, sex):
        super().__init__()  # Call parent constructor
        self.breed = breed
        self.birth_year = birth_year
        self.sex = sex
        self.age = self.calculate_age()

        # Generate tag number based on birth year
        self.tag_number = self.generate_tag

    def calculate_age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year + 1

    def generate_tag_number(self):
        year = str(self.birth_year)[-2:]
        latest_cattle = Cattle.query.filter(Cattle.tag_number.like(f'HF-{year}-%')).order_by(Cattle.id.desc()).first()

        if latest_cattle:
            latest_number = int(latest_cattle.tag_number.split('-')[-1])
            new_number = latest_number + 1
        else:
            new_number = 1

        return f'HF-{year}-{new_number}'

    def remove(self, removal_reason):
        if removal_reason == 'death':
            self.is_removed = True
            self.removal_reason = 'Death'
        elif removal_reason == 'sold':
            self.is_removed = True
            self.removal_reason = 'Sold'
        elif removal_reason == 'mistake':
            db.session.delete(self)

        db.session.commit()

    def add_cattle(breed, birth_year, sex):
        cattle = Cattle(breed=breed, birth_year=birth_year, sex=sex)
        db.session.add(cattle)
        db.session.commit()
