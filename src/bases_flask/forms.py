from wtforms import Form, StringField, PasswordField, EmailField
from wtforms import BooleanField, SubmitField, IntegerField, validators, RadioField

class UserForm(Form):
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message='El campo es requerido')])
    nombre = StringField("Nombre", [
        validators.DataRequired(message='El campo es requerido')])
    apellido = StringField("Apellido", [
        validators.DataRequired(message='El campo es requerido')])
    correo = EmailField("Correo", [
        validators.Email(message='Ingrese correo valido')])


    tamanno = RadioField('Tamaño', choices=[('Chica', 'Chica $40'), ('Mediana', 'Mediana $80'), ('Grande', 'Grande $120')])
    jamon = BooleanField('Jamon $10')
    pinna = BooleanField('Piña $10')
    champinnones = BooleanField('Champiñones $10')
    numPizzas = IntegerField("Numero de Pizzas", [
        validators.DataRequired(message='El campo es requerido')])
    nombre = StringField("Nombre", [
        validators.DataRequired(message='El campo es requerido')])
    direccion = StringField("Dirección", [
        validators.DataRequired(message='El campo es requerido')])
    telefono = StringField("Telefono", [
        validators.DataRequired(message='El campo es requerido')])
    terminar = SubmitField('Terminar')
    quitar = SubmitField('Quitar')
    agregar = SubmitField('Agregar')
    totalVentas = SubmitField('Total de ventas')



    