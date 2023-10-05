# Importa las clases de modelos necesarias desde models.py
from models import Employee, Product, Production, Package
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://TPMike69:Mazzilli1001@localhost/shoes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '' 

db = SQLAlchemy(app)

# Rutas y lógica de la aplicación
@app.route('/')
def index():
    # Aquí puedes agregar la lógica para mostrar información en tu página de inicio
    return render_template('index.html')

# Define tus otras rutas y lógica aquí

if __name__ == '__main__':
    app.run(debug=True)

# Ruta y lógica para registrar la producción
@app.route('/register_production', methods=['POST'])
def register_production():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        product_id = request.form['product_id']
        production_date = request.form['production_date']
        package_number = request.form['package_number']
        compensation = request.form['compensation']

        # Crea una nueva producción en la base de datos
        new_production = Production(
            employee_id=employee_id,
            product_id=product_id,
            production_date=production_date,
            package_number=package_number,
            compensation=compensation
        )

        db.session.add(new_production)
        db.session.commit()

        flash('Producción registrada con éxito', 'success')
        return redirect(url_for('index'))

# ... define otras rutas y lógica aquí ...

if __name__ == '__main__':
    app.run(debug=True)
