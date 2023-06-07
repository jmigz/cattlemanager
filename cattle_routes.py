from datetime import datetime
from flask import render_template, redirect, url_for, flash
from models import db, Cattle
from logger import log_action

def add_cattle_route(request):
    test = "this is a test string for debugging"
    if request.method == 'POST':
        breed = request.form['breed']
        birth_date = request.form['birth_year']
        sex = request.form['sex']
        
        # Extract year and month from the birth_date
        birth_year, birth_month = birth_date.split('-')
        birth_year = int(birth_year)
        birth_month = int(birth_month)
        
        # Validate birth date
        current_year = datetime.now().year
        current_month = datetime.now().month
        if birth_year > current_year or (birth_year == current_year and birth_month > current_month):
            flash('Invalid birth date. Please select a date before the current date.', 'danger')
            return redirect(url_for('add_cattle'))
        
        # Add the cattle to the database
        cattle = Cattle(breed=breed, birth_year=birth_year, sex=sex)
        db.session.add(cattle)
        db.session.commit()
    return render_template('admin/cattle/add_cattle.html', test=test)

def remove_cattle_route(request):
    cattle_id = request.form.get('cattle_id')
    removal_reason = request.form.get('removal_reason')

    cattle = Cattle.query.get(cattle_id)
    if cattle:
        cattle.remove(removal_reason)
        log_action(f"Cattle {cattle_id} removed. Reason: {removal_reason}")
        flash('Cattle removed successfully.', 'success')
    else:
        flash('Cattle not found.', 'error')

    return redirect(url_for('cattle_list'))
