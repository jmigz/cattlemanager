from datetime import date
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from sqlalchemy import func
from models.user import User, authenticate_user
from models import db
from models import cattle
from utils import get_next_tag_number

def login_view():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        authenticated = authenticate_user(username, password)

        if authenticated:
            user = User.query.filter_by(username=username).first()
            login_user(user)
            return dashboard_view()
        else:
            flash('Invalid credentials')

    return render_template('auth/login.html')

@login_required
def cattle_list_view():
    return render_template('/admin/cattle/cattlelist.html')

@login_required
def cattle_details():
    return render_template('/admin/cattle/details.html')

@login_required
def dashboard_view():
    total_cattle = cattle.Cattle.query.count()
    total_heifers = cattle.Cattle.query.filter_by(sex='heifer').count()
    total_bulls = cattle.Cattle.query.filter_by(sex='bull').count()
    total_pregnant = cattle.Cattle.query.filter_by(is_pregnant=True).count()
    next_tag_number = get_next_tag_number(db, cattle.Cattle)
    
    return render_template('/admin/dashboard.html', total_cattle=total_cattle, total_heifers=total_heifers, total_bulls=total_bulls, total_pregnant=total_pregnant, next_tag_number=next_tag_number)
@login_required
def maintain_cattle_list_view():

    test = "this is a test string for debugging"
    current_date = date.today()
    max_date = current_date.strftime('%Y-%m')


    return render_template('/admin/cattle/add_cattle.html', test=test, max_date=max_date)

@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_required
def protected():
    return 'Protected route: Only authenticated users can access this'

def home():
    return render_template('home.html')
