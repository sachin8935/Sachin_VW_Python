# Employee Portal

This project is an Employee Portal built with Flask, featuring role-based access control. It allows users to authenticate, manage employee records, and view their profiles based on their roles (Admin, Manager, Employee).

## Project Structure

```
day21
├── app
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── employee.py
│   │   └── role.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── admin.py
│   │   ├── manager.py
│   │   └── employee.py
│   ├── templates
│   │   ├── base.html
│   │   ├── auth
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── admin
│   │   │   ├── dashboard.html
│   │   │   └── manage_users.html
│   │   ├── manager
│   │   │   ├── dashboard.html
│   │   │   └── team.html
│   │   └── employee
│   │       ├── dashboard.html
│   │       └── profile.html
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.js
│   ├── utils
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   └── helpers.py
│   └── config.py
├── migrations
├── tests
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_routes.py
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd day21
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Configure the database URI in `app/config.py`.
   - Run migrations to set up the database schema.

5. **Run the application**:
   ```
   python run.py
   ```

## Usage

- **Authentication**: Users can register and log in to access their respective dashboards.
- **Admin Dashboard**: Admins can manage users and employee records.
- **Manager Dashboard**: Managers can view and manage their team's records.
- **Employee Dashboard**: Employees can view and edit their profiles.

## Testing

To run the tests, use the following command:
```
pytest
```

## License

This project is licensed under the MIT License.