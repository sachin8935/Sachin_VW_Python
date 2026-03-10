from app import db

class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=True)
    
    # Self-referential relationship for manager-employee hierarchy
    manager = db.relationship('Employee', remote_side=[id], backref='team_members')
    
    def __repr__(self):
        return f'<Employee {self.name}>'