from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Employee, Product, Production, Package
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:contraseña@servidor/nombre_de_la_base_de_datos'

# Configurar la base de datos
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)

# Ruta principal para mostrar la lista de empleados
@app.route('/')
def index():
    session = Session()
    employees = session.query(Employee).all()
    session.close()
    return render_template('index.html', employees=employees)

# Ruta para registrar una producción
@app.route('/register_production', methods=['POST'])
def register_production():
    session = Session()
    
    # Obtener los datos del formulario
    employee_id = int(request.form['employee_id'])
    product_id = int(request.form['product_id'])
    production_date = datetime.utcnow()
    package_number = int(request.form['package_number'])
    
    # Obtener el empleado y el producto
    employee = session.query(Employee).filter_by(employee_id=employee_id).first()
    product = session.query(Product).filter_by(product_id=product_id).first()
    
    # Calcular la compensación
    compensation = employee.compensation_per_product
    
    # Crear un registro de producción
    production = Production(
        employee_id=employee_id,
        product_id=product_id,
        production_date=production_date,
        package_number=package_number,
        compensation=compensation
    )
    
    session.add(production)
    session.commit()
    
    session.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)