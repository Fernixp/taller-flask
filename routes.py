from flask import jsonify, render_template
from app import app

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
    return render_template('about.html')

@app.route('/saludo')
def saludo():
    return 'Hola bienvenido a Taller Apps'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Hola {nombre} bienvenido a Taller Apps'