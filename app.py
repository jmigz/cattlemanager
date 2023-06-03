from flask import Flask, request, current_app, redirect, url_for, flash, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
import os
import psycopg2
from flask_migrate import Migrate


# Get the values of environment variables
database_url = os.environ.get('DATABASE_URL')
secret_key = os.environ.get('SECRET_KEY')

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


def create_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()


def list_users():
    return User.query.all()


login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password


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


@app.route('/cattle')
def cattle_index():
    return render_template('cattle/index.html')


@app.route('/cattle/details')
def cattle_details():
    return render_template('cattle/details.html')


@app.route('/hello')
@login_required
def hello():
    # Render the hello page template
    return render_template('hello.html')


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


if __name__ == '__main__':
    with app.app_context():
        inspector = inspect(db.engine)
        table_names = inspector.get_table_names()
        for table_name in table_names:
            print(table_name)
        user_columns = inspector.get_columns('users')
        for column in user_columns:
            print(column['name'])
            
        db.create_all()
        # Uncomment the following line if you want to create a user
        # create_user('kiki', 'password')
        users = list_users()
        for user in users:
            print(user)

    app.run()
