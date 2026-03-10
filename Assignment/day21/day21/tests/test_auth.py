from flask import Flask, session
import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_register(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'password': 'testpass',
        'role': 'employee'
    })
    assert response.status_code == 200
    assert b'Registration successful' in response.data

def test_login(client):
    client.post('/register', data={
        'username': 'testuser',
        'password': 'testpass',
        'role': 'employee'
    })
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 200
    assert b'Login successful' in response.data
    assert 'user_id' in session

def test_login_fail(client):
    response = client.post('/login', data={
        'username': 'wronguser',
        'password': 'wrongpass'
    })
    assert response.status_code == 401
    assert b'Invalid credentials' in response.data

def test_logout(client):
    client.post('/register', data={
        'username': 'testuser',
        'password': 'testpass',
        'role': 'employee'
    })
    client.post('/login', data={
        'username': 'testuser',
        'password': 'testpass'
    })
    response = client.get('/logout')
    assert response.status_code == 200
    assert 'user_id' not in session