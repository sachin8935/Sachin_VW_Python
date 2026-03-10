from app import create_app, db
from app.models.user import User
from app.models.employee import Employee

app = create_app()

def seed_database():
    """Seed the database with initial data"""
    with app.app_context():
        # Check if data already exists
        if User.query.first():
            print("Database already seeded.")
            return
        
        # Create sample employees
        ceo = Employee(name='John CEO', email='john@company.com', department='Executive')
        db.session.add(ceo)
        db.session.commit()
        
        manager1 = Employee(name='Alice Manager', email='alice@company.com', department='Engineering', manager_id=ceo.id)
        manager2 = Employee(name='Bob Manager', email='bob@company.com', department='Sales', manager_id=ceo.id)
        db.session.add(manager1)
        db.session.add(manager2)
        db.session.commit()
        
        emp1 = Employee(name='Charlie Dev', email='charlie@company.com', department='Engineering', manager_id=manager1.id)
        emp2 = Employee(name='Diana Dev', email='diana@company.com', department='Engineering', manager_id=manager1.id)
        emp3 = Employee(name='Eve Sales', email='eve@company.com', department='Sales', manager_id=manager2.id)
        db.session.add_all([emp1, emp2, emp3])
        db.session.commit()
        
        # Create users with different roles
        admin_user = User(username='admin', role='admin', employee_id=ceo.id)
        admin_user.set_password('admin123')
        
        manager_user = User(username='manager', role='manager', employee_id=manager1.id)
        manager_user.set_password('manager123')
        
        employee_user = User(username='employee', role='employee', employee_id=emp1.id)
        employee_user.set_password('employee123')
        
        db.session.add_all([admin_user, manager_user, employee_user])
        db.session.commit()
        
        print("Database seeded successfully!")
        print("\nTest credentials:")
        print("Admin - username: admin, password: admin123")
        print("Manager - username: manager, password: manager123")
        print("Employee - username: employee, password: employee123")

if __name__ == '__main__':
    seed_database()
    app.run(debug=True, port=5001)