# utils.py

from models.user import create_user

def create_initial_users(app):
    with app.app_context():
        print("Creating users...")
        create_user('kiki', 'password')
        create_user('user', 'password')
        print("Users created.")
