from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymsql://MikeMorron:Mazzilli1001@MikeMorron.mysql.pythonanywhere-services.com/MikeMorron$my_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = ''

my_db = SQLAlchemy(app)

# Importa las clases de modelos necesarias desde models.py
from models import Usuario, Produccion, Etiqueta, Articulo, Paquete, Pagos

@app.route('/home/MikeMorron/empresa_calzado/index.html')
def index():
    return render_template('index.html')

@app.route('/app.py', methods=['POST'])
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

        # Asigna un mensaje para mostrar en la plantilla
        message = "Registro exitoso. Ahora puedes generar etiquetas."

        flash(message, 'success')

    return render_template('index.html')


if __name__ == '__main__': 
    app.run(debug=True)