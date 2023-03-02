from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def initial():
    return {
        'message': 'Bienvenido a mi API'
    }

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    if request.method == 'GET':
        return { 'message': 'Yo soy el GET'}
    elif request.method == 'POST':
        return { 'message': 'Yo soy el POST'}

if __name__ == '__main__':
    # debug -> indica que reinicie el servidor automáticamente al guardar un archivo del proyecto
    app.run(debug=True)