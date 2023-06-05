from datetime import datetime
from flask import Flask, request, redirect, render_template
from flask_login import LoginManager, login_required
from dotenv import load_dotenv
import os
from models import db
from flask_migrate import Migrate
from views import cattle_list_view, login_view, cattle_details, logout, protected, home
from models.user import User

# Get the values of environment variables
database_url = os.environ.get('DATABASE_URL')
secret_key = os.environ.get('SECRET_KEY')

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

@app.template_filter('format_date')
def format_date(date):
    if date == 'now':
        return datetime.now().strftime('%Y')
    else:
        date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')  # Convert date string to datetime object
        return date_obj.strftime('%Y')


@login_manager.user_loader
def load_user(user_id):
    if user_id.isdigit():
        user = User.query.get(int(user_id))
    else:
        user = User.query.filter_by(username=user_id).first()
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Call the login_view function from views.py
    return login_view()


@app.route('/cattlelist')
def cattle_list_route():
    return cattle_list_view()

@app.route('/admin/cattle/details')
def cattle_details():
    return cattle_details()


@app.route('/dashboard')
@login_required
def hello():
    # Render the hello page template
    return render_template('/admin/dashboard.html')


def authenticate_user(username, password):
    # Perform database query to validate user credentials
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        return True

    return False


@app.route('/logout')
@login_required
def logout():
    return logout()


@app.route('/protected')
@login_required
def protected():
    return protected()


@app.route('/')
def home_route():
    return home()


if __name__ == '__main__':
    app.run(debug=True)
