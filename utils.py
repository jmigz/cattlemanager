# utils.py
from sqlalchemy import func
from datetime import datetime

from models.user import create_user

def create_initial_users(app):
    with app.app_context():
        print("Creating users...")
        create_user('kiki', 'password')
        create_user('user', 'password')
        print("Users created.")

def get_next_tag_number(db, Cattle):
    current_year = datetime.now().year
   
    cur_year= str(current_year)[-2:]

    last_tag_number = db.session.query(func.max(Cattle.tag_number)).scalar()
    if last_tag_number:
        last_number = int(last_tag_number.split('-')[-1])
        if int(last_tag_number.split('-')[1]) == int(cur_year):
            
            next_number = last_number + 1
        else:
            next_number = 1
    else:
        next_number = 1

    next_tag_number = f'HF-{cur_year}-{next_number}'

    return next_tag_number