from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Modelo para los empleados
class Employee(Base):
    empleado = 'employees'

    employee_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    compensation_per_product = Column(Float, nullable=False)

    # Relación uno a muchos con las producciones del empleado
    productions = relationship('Production', backref='employee', lazy='dynamic')

#Modelo para los productos
class Product(Base):
    productos = 'products'

    product_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    # Relación uno a muchos con las producciones
    productions = relationship('Production', backref='product', lazy='dynamic')

# Modelo para las producciones
class Production(Base):
    produccion = 'productions'

    production_id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    production_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    package_number = Column(Integer, nullable=False)
    compensation = Column(Float, nullable=False)

# Modelo para los paquetes
class Package(Base):
    paquetes = 'packages'

    package_id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'), nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    end_date = Column(DateTime, nullable=False)
    total_compensation = Column(Float, nullable=False)

# Configuración de la base de datos
engine = create_engine('mysql+pymysql://TPMike69:Mazzilli1001@TPMike69.mysql.pythonanywhere-services.com/shoes')
Base.metadata.create_all(engine)
