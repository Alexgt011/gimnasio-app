from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3

app = Flask(__name__)
app.secret_key = '12345678'

DATABASE = 'gimnasio.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password)).fetchone()
        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Credenciales incorrectas.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/clientes', methods=['GET', 'POST'])
def newClientes():
    db = get_db()
    if request.method == 'POST':
        db.execute('INSERT INTO clientes (nombre, nit_carnet, plan, fecha_nac, fecha_inicio_plan, fecha_fin_plan) VALUES (?, ?, ?, ?, ?, ?)',
                   (request.form['nombre'], request.form['nit_carnet'], request.form['plan'], request.form['fecha_nac'],
                    request.form['fecha_inicio_plan'], request.form['fecha_fin_plan']))
        db.commit()
        return redirect(url_for('newClientes'))

    clientes = db.execute('SELECT * FROM clientes').fetchall()
    return render_template('clientes/clientes.html', clientes=clientes)

@app.route('/clientes/<int:id>', methods=['GET', 'POST'])
def updateClientes(id):
    db = get_db()
    if request.method == 'POST':
        db.execute('UPDATE clientes SET nombre = ?, nit_carnet = ?, plan = ?, fecha_nac = ?, fecha_inicio_plan = ?, fecha_fin_plan = ? WHERE id = ?',
                   (request.form['nombre'], request.form['nit_carnet'], request.form['plan'], request.form['fecha_nac'],
                    request.form['fecha_inicio_plan'], request.form['fecha_fin_plan'], id))
        db.commit()
        return redirect(url_for('newClientes'))

    cliente = db.execute('SELECT * FROM clientes WHERE id = ?', (id,)).fetchone()
    return render_template('clientes/update_cliente.html', cliente=cliente)

@app.post('/<int:id>/delete/')
def delete(id):
    db = get_db()
    db.execute('DELETE FROM clientes WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('newClientes'))

@app.route('/instructores', methods=['GET', 'POST'])
def instructores():
    db = get_db()
    instructores = db.execute('SELECT * FROM instructores').fetchall()
    return render_template('instructores/instructores.html', instructores=instructores)

@app.route('/newinstructores', methods=['GET', 'POST'])
def newinstructor():
    db = get_db()
    if request.method == 'POST':
        db.execute('INSERT INTO instructores (nombre, edad, direccion, rol, turno_ini, turno_fin, user_name, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                   (request.form['nombre'], request.form['edad'], request.form['direccion'], request.form['rol'],
                    request.form['turno_ini'], request.form['turno_fin'], request.form['user_name'], request.form['password']))
        db.commit()
        return redirect(url_for('instructores'))
    return render_template('instructores/new/newinstructor.html')

@app.route('/instructores/<int:id>', methods=['GET', 'POST'])
def updateInstructores(id):
    db = get_db()
    if request.method == 'POST':
        db.execute('UPDATE instructores SET nombre = ?, edad = ?, direccion = ?, rol = ?, turno_ini = ?, turno_fin = ?, user_name = ?, password = ? WHERE id = ?',
                   (request.form['nombre'], request.form['edad'], request.form['direccion'], request.form['rol'],
                    request.form['turno_ini'], request.form['turno_fin'], request.form['user_name'], request.form['password'], id))
        db.commit()
        return redirect(url_for('instructores'))

    instructor = db.execute('SELECT * FROM instructores WHERE id = ?', (id,)).fetchone()
    return render_template('instructores/update/updateinstructor.html', instructor=instructor)

@app.post('/<int:id>/deleteinstructor/')
def deleteinstructor(id):
    db = get_db()
    db.execute('DELETE FROM instructores WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('instructores'))

@app.route('/planes', methods=['GET', 'POST'])
def nPlanes():
    db = get_db()
    if request.method == 'POST':
        db.execute('INSERT INTO planes (nombre, tiempo_dur, incluye, precio) VALUES (?, ?, ?, ?)',
                   (request.form['nombre'], request.form['tiempo_dur'], request.form['incluye'], request.form['precio']))
        db.commit()
        return redirect(url_for('nPlanes'))

    planes = db.execute('SELECT * FROM planes').fetchall()
    return render_template('planes/planes.html', planes_db=planes)

@app.route('/planes/<int:id>', methods=['GET', 'POST'])
def updatePlanes(id):
    db = get_db()
    if request.method == 'POST':
        db.execute('UPDATE planes SET nombre = ?, tiempo_dur = ?, incluye = ?, precio = ? WHERE id = ?',
                   (request.form['nombre'], request.form['tiempo_dur'], request.form['incluye'], request.form['precio'], id))
        db.commit()
        return redirect(url_for('nPlanes'))

    plan = db.execute('SELECT * FROM planes WHERE id = ?', (id,)).fetchone()
    return render_template('planes/update_planes.html', plan=plan)

@app.post('/<int:id>/deletePlan/')
def deletePlan(id):
    db = get_db()
    db.execute('DELETE FROM planes WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('nPlanes'))

@app.route('/promociones', methods=['GET', 'POST'])
def promociones():
    db = get_db()
    if request.method == 'POST':
        db.execute('INSERT INTO promociones (nombre, fecha_elab, fecha_venc, precio) VALUES (?, ?, ?, ?)',
                   (request.form['nombre'], request.form['fecha_elab'], request.form['fecha_venc'], request.form['precio']))
        db.commit()
        return redirect(url_for('promociones'))

    promociones = db.execute('SELECT * FROM promociones').fetchall()
    return render_template('promociones/promociones.html', planes_db=promociones)

@app.route('/promociones/<int:id>', methods=['GET', 'POST'])
def updatepromociones(id):
    db = get_db()
    if request.method == 'POST':
        db.execute('UPDATE promociones SET fecha_ini = ?, fecha_fin = ?, tipo_prom = ? WHERE id = ?',
                   (request.form['fecha_ini'], request.form['fecha_fin'], request.form['tipo_prom'], id))
        db.commit()
        return redirect(url_for('promociones'))

    plan = db.execute('SELECT * FROM promociones WHERE id = ?', (id,)).fetchone()
    return render_template('promociones/update_promociones.html', plan=plan)

if __name__ == '__main__':
    app.run(debug=True)"// Cambios para la v2.0" 
"// Fix aplicado para versi¢n 2.1" 
"// Funcionalidades para versi¢n 3.0" 
"// Nueva interfaz agregada" 
