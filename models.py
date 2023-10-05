from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'

    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    compensation_per_product = db.Column(db.Float, nullable=False)

class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Production(db.Model):
    __tablename__ = 'productions'

    production_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    production_date = db.Column(db.DateTime, nullable=False)
    package_number = db.Column(db.Integer, nullable=False)
    compensation = db.Column(db.Float, nullable=False)

    employee = db.relationship('Employee', backref=db.backref('productions', lazy=True))
    product = db.relationship('Product', backref=db.backref('productions', lazy=True))

class Package(db.Model):
    __tablename__ = 'packages'

    package_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)
    package_number = db.Column(db.Integer, nullable=False)
    total_compensation = db.Column(db.Float, nullable=False)

    employee = db.relationship('Employee', backref=db.backref('packages', lazy=True))
