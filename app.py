from flask import Flask, request, current_app, redirect, url_for, flash, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from dotenv import load_dotenv

from sqlalchemy import inspect
from datetime import datetime
import os
from dotenv import load_dotenv
import psycopg2
from models import db
from flask_migrate import Migrate
from models.user import User
from models.cattle import Cattle



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


def create_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()


def list_users():
    return User.query.all()


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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        authenticated = authenticate_user(username, password)

        if authenticated:
            # Create a user object and login the user
            user = User.query.filter_by(username=username).first()
            login_user(user)
            return redirect(url_for('hello'))
        else:
            flash('Invalid credentials')

    return render_template('auth/login.html')


@app.route('/admin/cattle')
def cattle_index():
    return render_template('cattle/cattlelist.html')


@app.route('/admin/cattle/details')
def cattle_details():
    return render_template('cattle/details.html')


@app.route('/hello')
@login_required
def hello():
    # Render the hello page template
    return render_template('/admin/hello.html')


def authenticate_user(username, password):
    # Perform database query to validate user credentials
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        return True

    return False


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/protected')
@login_required
def protected():
    return 'Protected route: Only authenticated users can access this'


@app.route('/')
def home():
    return render_template('home.html')


# Create users and list them
# with app.app_context():
    # db.drop_all()
    # db.create_all()
    # inspector = inspect(db.engine)
    # table_names = inspector.get_table_names()
    # for table_name in table_names:
    #     print(table_name)
    # user_columns = inspector.get_columns('users')
    # for column in user_columns:
    #     print(column['name'])
    # create_user('kiki', 'password')

    # create_user('admin', 'password')
    # users = list_users()
    # for user in users:
    #     print(user)


if __name__ == '__main__':
    app.run(debug=True)
