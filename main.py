from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template("index.html")


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        canttarros = int(request.form['canttarros'])
        preciototal = None
        preciosindcto = None
        cantdcto = None
        if edad < 18:
            preciototal = canttarros * 9000
        elif edad >= 18 and edad <= 30:
            preciosindcto = canttarros * 9000
            cantdcto = (canttarros * 9000) * 0.15
            preciototal = (canttarros * 9000) * 0.85
        elif edad > 30:
            preciosindcto = canttarros * 9000
            cantdcto = (canttarros * 9000) * 0.25
            preciototal = (canttarros * 9000) * 0.75
        return render_template('ejercicio1.html', nombre=nombre, preciosindcto=preciosindcto, preciototal=preciototal,
                               cantdcto=cantdcto)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        contrasena = str(request.form['contrasena'])
        if nombre == 'juan' and contrasena == 'admin':
            resultado = 'Bienvenido Administrador juan'
        elif nombre == 'pepe' and contrasena == 'user':
            resultado = 'Bienvenido Usuario pepe'
        else:
            resultado = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html', resultado=resultado)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)
