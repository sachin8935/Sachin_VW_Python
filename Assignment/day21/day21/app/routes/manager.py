from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Employee
from app.utils.decorators import role_required

manager_bp = Blueprint('manager', __name__)

@manager_bp.route('/manager/dashboard')
@role_required('manager')
def dashboard():
    return render_template('manager/dashboard.html')

@manager_bp.route('/manager/team')
@role_required('manager')
def team():
    employees = Employee.query.all()
    return render_template('manager/team.html', employees=employees)

@manager_bp.route('/manager/edit_employee/<int:employee_id>', methods=['GET', 'POST'])
@role_required('manager')
def edit_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.email = request.form['email']
        employee.department = request.form['department']
        # Add any additional fields as necessary
        # Save changes to the database
        employee.save()
        flash('Employee record updated successfully!', 'success')
        return redirect(url_for('manager.team'))
    return render_template('manager/edit_employee.html', employee=employee)