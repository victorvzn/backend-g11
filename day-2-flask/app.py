import os
from flask import Flask, request, render_template

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return "Mi primera API con Flask"

@app.route("/alumno")
def alumno():
    # este diccionario lo devuelve en formato json por defecto
    return {
        'nombre': 'Victor',
        'edad': 30,
        'promedio': 18.5,
    }

lista_alumnos = [
    {
        'nombre': 'Victor',
        'edad': 30,
        'promedio': 18.5,
    },
    {
        'nombre': 'Claudia',
        'edad': 25,
        'promedio': 19,
    }
]

@app.route("/alumnos", methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'])
def alumnos():
    print("METHOD --> {}".format(request.method))
    if (request.method == 'GET'):
        return lista_alumnos
    elif request.method == 'POST':
        # print(request.json)
        # print(request.get_json())
        lista_alumnos.append(request.json)
        return lista_alumnos

# @app.route("/alumno/<int:age>")
@app.route("/alumno/<nombre>")
def buscar_alumno(nombre):
    for alumno in lista_alumnos:
        if alumno['nombre'] == nombre:
            return alumno

    return { 'message': 'El alumno no existe' }

@app.route("/html")
def html():
    edad = 10
    # return "<button>Dame click</button>"
    return render_template('index.html', edad=edad)

@app.route("/form-data", methods=['POST'])
def form_data():
    print(request.form)
    return 'Form data recibido exitosamente'

@app.route("/files", methods=['POST'])
def files():
    # print(request.files['foto'].read().decode())
    # file_str = request.files['foto'].read().decode('utf-8')
    # f = open('archivo.txt', 'w')
    # f.write(file_str)
    # f.close()
    # Source: https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'Archivo recibido exitosamente'

# debug = si realizamos algún cambio podremos verlo en tiempo real (se reiniciará el servidor)
app.run(debug=True)

# flask run
