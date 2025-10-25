from flask import Flask, render_template

app = Flask(_name_)
""" desde donde arrancará mi proyecto es lo que indica el ('/') """
@app.route('/index')
def index():
    titulo = "Pagina de inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template('index.html', titulo = titulo, listado = listado)

@app.route('/calculos')
def calculos():
    return render_template('calculos.html')

@app.route('/distancia')
def distancia():
    return render_template('distancia.html')

""" variable tipo string llamada user """
@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:num>')
def func(num):
    return f"El numero es: {num}"

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return f"La suma es: {num1 + num2}"

""" La ruta user recibe dos parametros diferentes, entonces 
NO se confundira con la del user de la de arriba. Lo ÚNICO que
debe ser diferente es que el metodo debe ser diferente """
@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {} - Nombre: {}".format(id,username)

@app.route('/suma/<float:n1>/<float:n2>')
def func1(n1, n2):
    return "La suma es: {}".format(n1+n2)

@app.route('/default/')
@app.route('/default/<string:dft>')
def func2(dft="sss"):
    return "El valor de dft es: "+dft

""" ----------------------------- Hoy 18 de octubre ----------------------------- """
@app.route("/prueba")
def func4():
    return ''' 
    <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <title>Pagina Prueba</title>
        </head>
        <body>
            <h1>Hola, esta es una página de prueba</h1>
            <p>Esta página es para probar el retorno de HTML en Flask</p>
        </body>
    </html> 
'''


""" crear sistema de arranque del proyecto """
if _name_ == '_main_':
    app.run(debug=True)