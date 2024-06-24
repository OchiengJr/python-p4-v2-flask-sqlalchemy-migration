from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates

# Contains definitions of tables and associated schema constructs
metadata = MetaData()

# Create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

class Employee(db.Model):
    """
    Employee model that represents an employee in the database.
    """
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Employee ID: {self.id}, Name: {self.name}, Salary: {self.salary}>'

    @validates('name')
    def validate_name(self, key, name):
        """
        Validate the name field to ensure it is not empty.
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        if len(name) > 100:
            raise ValueError("Name cannot exceed 100 characters.")
        return name

    @validates('salary')
    def validate_salary(self, key, salary):
        """
        Validate the salary field to ensure it is a positive integer.
        """
        if salary < 0:
            raise ValueError("Salary must be a positive integer.")
        return salary

    @staticmethod
    def create_employee(name, salary):
        """
        Create a new employee record and add it to the session.
        """
        new_employee = Employee(name=name, salary=salary)
        db.session.add(new_employee)
        db.session.commit()
        return new_employee

    def update_employee(self, name=None, salary=None):
        """
        Update the employee record with new values for name and salary.
        """
        if name:
            self.name = name
        if salary:
            self.salary = salary
        db.session.commit()

    def delete_employee(self):
        """
        Delete the employee record from the session.
        """
        db.session.delete(self)
        db.session.commit()
