from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from models.user import User, authenticate_user

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
    return render_template('/admin/dashboard.html')
@login_required
def maintain_cattle_list_view():
    return render_template('/admin/cattle/addremove.html')

@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_required
def protected():
    return 'Protected route: Only authenticated users can access this'

def home():
    return render_template('home.html')
