from flask import Flask, render_template, request
from flask import make_response, jsonify, json
from datetime import datetime
import forms

app = Flask(__name__)


@app.route('/pizzeria', methods = ['GET', 'POST'])
def pizzeria():
    tamanno = ""
    ingredientes = []
    numPizzas = 0
    
    nombre = ""
    direccion = ""
    telefono = ""
    fechaCompra = ""

    tamanCostos = {'Chica': 40, 'Mediana': 80, 'Grande': 120}
    subtotal = 0

    pedido = {}
    pedidosDelDia = []
    ventasDelDia = []
    totalVentasDelDia = 0
    tempPersona = {}
    tempNombre = ""
    tempCostoTotal = 0

    piz_clas = forms.UserForm(request.form)
    if request.method == 'POST' and piz_clas.validate():
        tamanno = piz_clas.tamanno.data
        numPizzas = piz_clas.numPizzas.data
        nombre = piz_clas.nombre.data
        direccion = piz_clas.direccion.data
        telefono = piz_clas.telefono.data
        fechaCompra = datetime.now()
        subtotal = tamanCostos[tamanno]
        
        if piz_clas.jamon.data == True:
            ingredientes.append('jamon')
            subtotal = subtotal + 10
        if piz_clas.champinnones.data == True:
            ingredientes.append('champiñones')
            subtotal = subtotal + 10
        if piz_clas.pinna.data == True:
            ingredientes.append('Piña')
            subtotal = subtotal + 10
        subtotal = subtotal * numPizzas

        pedido = {'tamaño' : tamanno.rstrip(), 'ingredientes': ingredientes, 'numeroDePizzas' : numPizzas,
              'nombreDelCliente': nombre.rstrip(), 'dirección': direccion.rstrip(), 'telefono': telefono.rstrip(), 'fechaDeCompra' : fechaCompra,
              'subTotal': subtotal}
        data_str = request.cookies.get("pizzas")
        data_str3 = request.cookies.get("ventaTotalTotal")

        
        if not data_str:
             return "No hay cookie guardada", 404
        pedidosDelDia = json.loads(data_str)
        



    if piz_clas.agregar.data:
        pedidosDelDia.append(pedido)
        totalVentasDelDia += int(data_str3)



    if piz_clas.terminar.data:
        for persona in pedidosDelDia:
            tempNombre = persona["nombreDelCliente"]
            tempCostoTotal = persona["subTotal"]

            if tempNombre in tempPersona:
                tempPersona[tempNombre] += tempCostoTotal
            else:
                tempPersona[tempNombre] = tempCostoTotal

        ventasDelDia = [{"nombre": tempNombre.rstrip(), "total": total} for tempNombre, total in tempPersona.items()]

        totalVentasDelDia += int(data_str3)
        pedidosDelDia = [] 



    if piz_clas.totalVentas.data:
        data_str2 = request.cookies.get("ventasTotales")
        ventasDelDia = json.loads(data_str2)
        for venta in ventasDelDia:
            totalVentasDelDia += venta['total']
        totalVentasDelDia += int(data_str3)

    if piz_clas.quitar.data:
        registrosBorrar = request.form.getlist('borrarPedidos')
        pedidosDelDia = [
                pedido for pedido in pedidosDelDia
                if pedido["fechaDeCompra"] not in registrosBorrar
            ]

    response=make_response(render_template('Pizzeria.html',
        form=piz_clas, pedidosDelDia = pedidosDelDia, ventasDelDia = ventasDelDia, totalVentasDelDia = totalVentasDelDia))
    if request.method!='GET' and not piz_clas.terminar.data or not piz_clas.totalVentas.data:
        response.set_cookie('pizzas', json.dumps(pedidosDelDia))



    if request.method!='GET':
        response.set_cookie('ventasTotales', json.dumps(ventasDelDia))
        response.set_cookie('ventaTotalTotal', json.dumps(totalVentasDelDia))

    return response

 

@app.route("/get_cookie")
def get_cookie():
     
    data_str = request.cookies.get("pizzas")
    if not data_str:
        return "No hay cookie guardada", 404
 
    pedidosDelDia = json.loads(data_str)
 
    return jsonify(pedidosDelDia)


if __name__ == '__main__':
    app.run(debug=True)