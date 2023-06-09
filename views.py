from datetime import date
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from sqlalchemy import func, not_
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
    session = db.session
    # cattle_list = session.query(cattle.Cattle).all()
    # cattle_list = session.query(cattle.Cattle).filter(cattle.Cattle.removal_reason == None).all()
# Retrieve filter parameters from the query string
    filter_bulls = request.args.get('filter_bulls', '')
    filter_heifers = request.args.get('filter_heifers', '')
    filter_birth_year = request.args.get('filter_birth_year', '')
    filter_pregnant = request.args.get('filter_pregnant', '')

    # Query the database based on the filter parameters


    query = session.query(cattle.Cattle).filter(not_(cattle.Cattle.is_removed))



    if filter_bulls:
        query = query.filter(cattle.Cattle.sex == 'bull')
    if filter_heifers:
        query = query.filter(cattle.Cattle.sex == 'heifer')
    if filter_birth_year:
        query = query.filter(cattle.Cattle.birth_year == filter_birth_year)
    if filter_pregnant:
        query = query.filter(cattle.Cattle.is_pregnant == (filter_pregnant == 'true'))

    # Execute the filtered query and retrieve the cattle list
    
    cattle_list = query.all()

    

    return render_template('admin/cattle/cattlelist.html', cattle_list=cattle_list)

def edit_cattle_details(id):
    selected_cattle = cattle.Cattle.query.get(id)
    if request.method == 'POST':
        # Update the selected cattle with the form data
        selected_cattle.breed = request.form.get('breed')
        selected_cattle.birth_year = int(request.form.get('birth_year'))
        selected_cattle.sex = request.form.get('sex')
        selected_cattle.is_pregnant = request.form.get('is_pregnant')
        
        # Save the changes to the database
        db.session.commit()
        
        # Redirect to the cattle list or any other desired page
        return redirect(url_for('cattle_list_route'))
    
    return render_template('/admin/cattle/edit_cattle.html', selected_cattle=selected_cattle)



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

    
    current_date = date.today()
    max_date = current_date.strftime('%Y-%m-%d')
    next_tag_number = get_next_tag_number(db, cattle.Cattle)


    return render_template('/admin/cattle/add_cattle.html', next_tag_number=next_tag_number, max_date=max_date)

@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_required
def protected():
    return 'Protected route: Only authenticated users can access this'

def home():
    return render_template('home.html')
