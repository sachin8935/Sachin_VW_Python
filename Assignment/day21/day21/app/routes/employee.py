from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.employee import Employee
from flask_login import login_required, current_user

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('employee/dashboard.html')

@employee_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    employee = Employee.query.filter_by(id=current_user.id).first()
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.email = request.form['email']
        employee.department = request.form['department']
        # Add any additional fields as necessary
        employee.save()  # Assuming a save method exists in the Employee model
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('employee.profile'))
    return render_template('employee/profile.html', employee=employee)