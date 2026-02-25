from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class FormAgregarTareas(FlaskForm):
    """ Formulario para la creación de nuevas tareas """
    titulo = StringField('Título de la Tarea', validators=[
        DataRequired(message="El título es obligatorio"),
        Length(min=3, max=100, message="El título debe tener entre 3 y 100 caracteres")
    ])
    enviar = SubmitField('Guardar Tarea')