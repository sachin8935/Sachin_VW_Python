from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Employee, Role
from app.utils.decorators import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/dashboard')
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/admin/manage_users', methods=['GET', 'POST'])
@admin_required
def manage_users():
    if request.method == 'POST':
        # Logic for creating or editing users
        pass
    users = Employee.query.all()  # Fetch all users
    return render_template('admin/manage_users.html', users=users)

@admin_bp.route('/admin/delete_user/<int:user_id>', methods=['POST'])
@admin_required
def delete_user(user_id):
    user = Employee.query.get_or_404(user_id)
    # Logic to delete the user
    flash('User deleted successfully.', 'success')
    return redirect(url_for('admin.manage_users'))

@admin_bp.route('/admin/assign_role/<int:user_id>', methods=['POST'])
@admin_required
def assign_role(user_id):
    user = Employee.query.get_or_404(user_id)
    role_id = request.form.get('role_id')
    # Logic to assign role to user
    flash('Role assigned successfully.', 'success')
    return redirect(url_for('admin.manage_users'))