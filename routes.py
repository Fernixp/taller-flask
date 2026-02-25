from flask import render_template, redirect, url_for, flash
from app import app
from extension import db
import formularios
from models import Tarea

@app.route('/')
def index():
    """ Vista principal: Listado de tareas y formulario """
    form = formularios.FormAgregarTareas()
    tareas_listado = Tarea.query.all()
    return render_template('index.html', 
                           subtitulo='Gestión de Tareas', 
                           form=form, 
                           tareas=tareas_listado)

@app.route('/about')
def about():
    """ Ruta informativa sobre la aplicación """
    return render_template('about.html')

@app.route('/tareas/crear', methods=['POST'])
def crear_tarea():
    """ Procesa la creación de una nueva tarea """
    form = formularios.FormAgregarTareas()
    if form.validate_on_submit():
        nueva_tarea = Tarea(titulo=form.titulo.data)
        db.session.add(nueva_tarea)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/tareas/eliminar/<int:id>')
def eliminar_tarea(id):
    """ Elimina una tarea específica por su ID """
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/status')
def status():
    """ Endpoint de estado del servidor """
    from flask import jsonify
    data = {
        "status": "online",
        "mensaje": "La API del Taller está funcionando",
        "version": 1.2,
        "servidor": "Flask/Werkzeug"
    }
    return jsonify(data)