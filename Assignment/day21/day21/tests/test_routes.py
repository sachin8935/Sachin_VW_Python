from app import app, db
from app.models.user import User
from app.models.employee import Employee
from app.models.role import Role
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_login(client):
    response = client.post('/auth/login', data={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_register(client):
    response = client.post('/auth/register', data={'username': 'newuser', 'password': 'newpass'})
    assert response.status_code == 200
    assert b'Registration successful' in response.data

def test_admin_dashboard(client):
    response = client.get('/admin/dashboard')
    assert response.status_code == 200
    assert b'Admin Dashboard' in response.data

def test_manager_dashboard(client):
    response = client.get('/manager/dashboard')
    assert response.status_code == 200
    assert b'Manager Dashboard' in response.data

def test_employee_dashboard(client):
    response = client.get('/employee/dashboard')
    assert response.status_code == 200
    assert b'Employee Dashboard' in response.data

def test_manage_users(client):
    response = client.get('/admin/manage_users')
    assert response.status_code == 200
    assert b'Manage Users' in response.data