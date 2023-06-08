from datetime import datetime
from flask import render_template, redirect, request, url_for, flash
from models import db, Cattle
from logger import log_action

def add_cattle_route(request):
  
    if request.method == 'POST':
        breed = request.form['breed']
        birth_date = request.form['birth_date']
        sex = request.form['sex']
        is_pregnant = request.form['is_pregnant'] == 'True'

        
        # Extract year and month from the birth_date
    
    if birth_date:
    # Convert the birth_date string to a date object
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()

        birth_year = birth_date.year
        birth_month = birth_date.month
        birth_day = birth_date.day
        
        # Validate birth date
        current_year = datetime.now().year
        current_month = datetime.now().month
        if birth_year > current_year or (birth_year == current_year and birth_month > current_month):
            flash('Invalid birth date. Please select a date before the current date.', 'danger')
            return redirect(url_for('cattle_list'))
    
    # Add the cattle to the database
    cattle = Cattle(breed=breed, birth_date=birth_date, sex=sex, is_pregnant=is_pregnant)
    db.session.add(cattle)
    db.session.commit()
    return render_template('admin/cattle/add_cattle.html')


def remove_cattle_route(id):
    cattle = Cattle.query.get(id)
    if cattle:
        if request.method == 'POST':
            removal_reason = request.form.get('removal_reason')
            cattle.remove(removal_reason)
            log_action(f"Cattle {id} removed. Reason: {removal_reason}")
            flash('Cattle removed successfully.', 'success')
            db.session.commit()
            return redirect(url_for('cattle_list_route'))
        else:
            return render_template('admin/cattle/remove_cattle.html', cattle_id=id, cattle_tag=cattle.tag_number)
    else:
        flash('Cattle not found.', 'error')
        return redirect(url_for('cattle_list_route')) 

