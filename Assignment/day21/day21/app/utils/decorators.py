from functools import wraps
from flask import redirect, url_for, flash, abort
from flask_login import current_user

def login_required_custom(f):
    """Custom decorator to check if user is logged in"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(*roles):
    """
    Decorator to restrict access based on user roles.
    Usage: @role_required('admin', 'manager')
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('Please log in to access this page.', 'warning')
                return redirect(url_for('auth.login'))
            
            if current_user.role not in roles:
                flash('You do not have permission to access this page.', 'danger')
                abort(403)
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def can_edit_employee(f):
    """
    Decorator to check if current user can edit a specific employee.
    - Admin: Can edit any employee
    - Manager: Can edit only their team members
    - Employee: Can edit only their own profile
    """
    @wraps(f)
    def decorated_function(id, *args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('auth.login'))
        
        from app.models.employee import Employee
        employee = Employee.query.get_or_404(id)
        
        # Admin can edit anyone
        if current_user.is_admin():
            return f(id, *args, **kwargs)
        
        # Manager can edit their team members
        if current_user.is_manager():
            if current_user.employee_id:
                # Check if employee is in manager's team
                if employee.manager_id == current_user.employee_id:
                    return f(id, *args, **kwargs)
                # Manager can also edit their own profile
                if employee.id == current_user.employee_id:
                    return f(id, *args, **kwargs)
        
        # Employee can edit only their own profile
        if current_user.is_employee():
            if current_user.employee_id and current_user.employee_id == id:
                return f(id, *args, **kwargs)
        
        flash('You do not have permission to edit this employee.', 'danger')
        abort(403)
    
    return decorated_function

def can_view_employee(f):
    """
    Decorator to check if current user can view a specific employee.
    - Admin: Can view any employee
    - Manager: Can view all employees
    - Employee: Can view only their own profile
    """
    @wraps(f)
    def decorated_function(id, *args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('auth.login'))
        
        # Admin and Manager can view anyone
        if current_user.is_admin() or current_user.is_manager():
            return f(id, *args, **kwargs)
        
        # Employee can view only their own profile
        if current_user.is_employee():
            if current_user.employee_id and current_user.employee_id == id:
                return f(id, *args, **kwargs)
        
        flash('You do not have permission to view this employee.', 'danger')
        abort(403)
    
    return decorated_function