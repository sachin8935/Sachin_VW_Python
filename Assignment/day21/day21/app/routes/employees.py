from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app import db
from app.models.user import User
from app.models.employee import Employee
from app.utils.decorators import role_required, can_edit_employee, can_view_employee

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/employees')
@login_required
@role_required('admin', 'manager')
def list_employees():
    """View all employees - Admin & Manager only"""
    employees = Employee.query.all()
    return render_template('employees/list.html', employees=employees)

@employees_bp.route('/employee/<int:id>')
@login_required
@can_view_employee
def view_employee(id):
    """View employee profile"""
    employee = Employee.query.get_or_404(id)
    return render_template('employees/view.html', employee=employee)

@employees_bp.route('/employee/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@can_edit_employee
def edit_employee(id):
    """Edit employee details - restricted by role"""
    employee = Employee.query.get_or_404(id)
    managers = Employee.query.filter(Employee.id != id).all()
    
    if request.method == 'POST':
        employee.name = request.form.get('name')
        employee.email = request.form.get('email')
        employee.department = request.form.get('department')
        
        # Only admin can change manager
        if current_user.is_admin():
            manager_id = request.form.get('manager_id')
            employee.manager_id = int(manager_id) if manager_id else None
        
        db.session.commit()
        flash('Employee updated successfully!', 'success')
        return redirect(url_for('employees.view_employee', id=id))
    
    return render_template('employees/edit.html', employee=employee, managers=managers)

@employees_bp.route('/employee/<int:id>/delete', methods=['POST'])
@login_required
@role_required('admin')
def delete_employee(id):
    """Delete employee - Admin only"""
    employee = Employee.query.get_or_404(id)
    
    # Also delete associated user if exists
    user = User.query.filter_by(employee_id=id).first()
    if user:
        db.session.delete(user)
    
    db.session.delete(employee)
    db.session.commit()
    
    flash('Employee deleted successfully!', 'success')
    return redirect(url_for('employees.list_employees'))

@employees_bp.route('/employee/create', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def create_employee():
    """Create new employee - Admin only"""
    managers = Employee.query.all()
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        department = request.form.get('department')
        manager_id = request.form.get('manager_id')
        
        if Employee.query.filter_by(email=email).first():
            flash('Email already exists.', 'danger')
            return render_template('employees/create.html', managers=managers)
        
        employee = Employee(
            name=name,
            email=email,
            department=department,
            manager_id=int(manager_id) if manager_id else None
        )
        
        db.session.add(employee)
        db.session.commit()
        
        flash('Employee created successfully!', 'success')
        return redirect(url_for('employees.list_employees'))
    
    return render_template('employees/create.html', managers=managers)

@employees_bp.route('/assign-role/<int:user_id>', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def assign_role(user_id):
    """Assign role to user - Admin only"""
    user = User.query.get_or_404(user_id)
    employees = Employee.query.all()
    
    if request.method == 'POST':
        user.role = request.form.get('role')
        employee_id = request.form.get('employee_id')
        user.employee_id = int(employee_id) if employee_id else None
        
        db.session.commit()
        flash('Role assigned successfully!', 'success')
        return redirect(url_for('employees.manage_users'))
    
    return render_template('employees/assign_role.html', user=user, employees=employees)

@employees_bp.route('/users')
@login_required
@role_required('admin')
def manage_users():
    """Manage users - Admin only"""
    users = User.query.all()
    return render_template('employees/users.html', users=users)

@employees_bp.route('/my-profile')
@login_required
def my_profile():
    """View own profile - All authenticated users"""
    if current_user.employee_id:
        return redirect(url_for('employees.view_employee', id=current_user.employee_id))
    flash('No employee profile linked to your account.', 'info')
    if current_user.is_admin() or current_user.is_manager():
        return redirect(url_for('employees.list_employees'))
    return redirect(url_for('auth.login'))

@employees_bp.route('/my-team')
@login_required
@role_required('manager')
def my_team():
    """View manager's team - Manager only"""
    if not current_user.employee_id:
        flash('No employee profile linked to your account.', 'danger')
        return redirect(url_for('employees.list_employees'))
    
    team_members = Employee.query.filter_by(manager_id=current_user.employee_id).all()
    return render_template('employees/team.html', team_members=team_members)
