from flask import Flask, request
from psycopg2 import connect
from flask_cors import CORS

app = Flask(__name__)

# Le estamos diciendo que puede acceder cualquier origen, cualquier metodo y enviar cualquier header
CORS(
    app,
    CORS_METHODS=['GET', 'POST', 'PUT', 'DELETE'],
    CORS_ORIGINS=['http://localhost:5000', 'http://127.0.0.1:5000']
)

# me conecto a la bd
conexion = connect(host='localhost', database='pruebas', user='postgres', password='root')

@app.route('/', methods=['GET'])
def initial():
    return {
        'message': 'Bienvenido a mi API'
    }

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    if request.method == 'GET':

        # creo un cursor que es el responsable de hacer lecturas y escrituras a la bd
        cursor = conexion.cursor()

        # ejecuto una query
        cursor.execute('SELECT * FROM alumnos;')

        # extraigo la informacion de la ejecucion de la query
        resultado = cursor.fetchall()

        print(resultado)

        alumnos_resultado = []

        for alumno in resultado:
            info_almno = {
                'id': alumno[0],
                'nombre': alumno[1],
                'apellido': alumno[2],
                'sexo': alumno[3],
                'fecha_creacion': alumno[4],
                'matriculado': alumno[5],
            }
            alumnos_resultado.append(info_almno)

        cursor.close()

        # return { 'message': 'Yo soy el GET'}
        return {
            'results': alumnos_resultado
        }

    elif request.method == 'POST':
        data = request.json

        print(data)

        cursor = conexion.cursor()

        cursor.execute(
            # 'INSERT INTO ALUMNOS (nombre, apellido, matriculado) VVALUES ({}, {}, {})',
            'INSERT INTO ALUMNOS (nombre, apellido, matriculado) VALUES (%s, %s, %s)',
            (
                data.get('nombre'), data.get('apellido'), data.get('matriculado')
            )
        )

        conexion.commit()

        cursor.close()
        
        return { 'message': 'Alumno ingresado correctamente '}
        # return { 'results': data }

@app.route('/alumnos/<id>', methods=['GET', 'PUT', 'DELETE'])
def gestion_alumno(id):
    if request.method == 'GET':
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM alumnos WHERE id = %s', (id,))

        alumno = cursor.fetchone()

        # Si el alumno no existe indicar en el message que el alumno no existe, de lo contrario devolver el alumno

        if alumno == None:
            return {
                "message": "Alumno no existe"
            }
        
        print(alumno)

        return {
            'id': alumno[0],
            'nombre': alumno[1],
            'apellido': alumno[2],
            'sexo': alumno[3],
            'fecha_creacion': alumno[4],
            'matriculado': alumno[5],
        }
    
    if request.method == 'PUT':
        # TODO: Recibir la información del body y el id por la url y modificar la data del alumno, primero validar si el alumno existe, si no existe no hacer ninguna modificacion, si existe hacer la modificacion
        data = request.json

        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM alumnos WHERE id = %s', (id,))

        alumno = cursor.fetchone()

        if alumno == None:
            return {
                "message": "Alumno no existe"
            }

        cursor.execute(
            'UPDATE ALUMNOS SET nombre=%s, apellido=%s, matriculado=%s WHERE id = %s',
            (
                data.get('nombre'), data.get('apellido'), data.get('matriculado'), id
            )
        )

        conexion.commit()

        cursor.close()

        return { 'message': 'Alumno actualizado correctamente '}

    if request.method == 'DELETE':
        # TODO: Recibir el id por la url y validar si el alumno existe, si existe, eliminarlo (hacer un delete) caso contrario indicar que el alumno no existe
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM alumnos WHERE id = %s', (id,))

        alumno = cursor.fetchone()

        if alumno == None:
            return {
                "message": "Alumno no existe"
            }

        cursor.execute(
            'DELETE FROM alumnos WHERE id = %s',
            (id,)
        )

        conexion.commit()

        cursor.close()

        return { 'message': 'Alumno eliminado correctamente '}

if __name__ == '__main__':
    # debug -> indica que reinicie el servidor automáticamente al guardar un archivo del proyecto
    app.run(debug=True)