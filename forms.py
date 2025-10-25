from wtforms import Form, StringField, PasswordField, EmailField
from wtforms import BooleanField, SubmitField, IntegerField, validators

class UserForm(Form):
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message='El campo es requerido')])
    nombre = StringField("Nombre", [
        validators.DataRequired(message='El campo es requerido')])
    apellido = StringField("Apellido", [
        validators.DataRequired(message='El campo es requerido')])
    correo = EmailField("Correo", [
        validators.Email(message='Ingrese correo valido')])


    