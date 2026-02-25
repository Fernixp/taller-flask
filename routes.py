from flask import jsonify, render_template
from app import app
from extension import db
import formularios
from models import Tarea

@app.route('/')
def html():
    return render_template('index.html', subtitulo='Panel dinámico sincronizado')

@app.route('/status')
def status():
    data = {
        "status": "online",
        "mensaje": "La API del Taller está funcionando",
        "version": 1.0,
        "servidor": "Flask/Werkzeug"
    }
    return jsonify(data)

@app.route('/about')
def about():
    formulario = formularios.FormAgregarTareas()
    return render_template('about.html', form=formulario)

@app.route('/saludo')
def saludo():
    return 'Hola bienvenido a Taller Apps'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Hola {nombre} bienvenido a Taller Apps'

""" Ruta para subir formulario a db """
@app.route('/tareas', methods = ['POST'])
def tareas():
        formulario = formularios.FormAgregarTareas()
        if formulario.validate_on_submit() :
                nueva_tarea = Tarea (titulo =  formulario.titulo.data)
                db.session.add(nueva_tarea)
                db.session.commit()
                print('se envio correctamente', formulario.titulo.data)
                return render_template('about.html', 
                                       form = formulario,
                                       titulo = formulario.titulo.data)
        return render_template('about.html', form = formulario)