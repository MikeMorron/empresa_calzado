from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://MikeMorron:Mazzilli1001@MikeMorron.mysql.pythonanywhere-services.com/my_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = ''

my_db= SQLAlchemy(app)

# Importa las clases de modelos necesarias desde models.py
from models import Usuario, Produccion, Etiqueta, Articulo, Paquete

@app.route('/')
def index():
    return render_template('index.html')

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
        new_production = Produccion(
            employee_id=employee_id,
            product_id=product_id,
            production_date=production_date,
            package_number=package_number,
            compensation=compensation
        )

        my_db.session.add(new_production)
        my_db.session.commit()

        flash('Producción registrada con éxito', 'success')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
