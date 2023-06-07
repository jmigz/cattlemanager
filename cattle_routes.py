from flask import render_template, redirect, url_for, flash
from models import db, Cattle
from logger import log_action

def add_cattle_route(request):
    print("i got here")
    if request.method == 'POST':
        breed = request.form['breed']
        age = int(request.form['age'])
        weight = float(request.form['weight'])
        sex = request.form['sex']
        health_status = request.form['health_status']
        vaccinations = request.form['vaccinations']
        breeding_history = request.form['breeding_history']
        
        print(request.form)
        # Add the cattle to the database
        Cattle.add_cattle(breed, age, weight, sex, health_status, vaccinations, breeding_history)
        
        flash('Cattle added successfully.', 'success')
        return redirect(url_for('cattle_list_route'))
    
    return render_template('add_cattle.html')


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
