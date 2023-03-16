# Repositorio: Backend de Codigo G11 - Semana05

# Enunciado para crear el diagrama de base de datos con https://dbdiagram.io/d

```
Se requiere un sistema para almacenar los articulos de una libreria, en la cual en los productos se debe almacenar: nombre, precio, fecha_creacion, categoria, imagen.

A su vez, la categoria debe contener: nombre, imagen, estado.

Ademas, se debe gestionar las operaciones por los usuarios siendo estos ADMIN o PERSONAL (los ADMIN solo pueden crear y eliminar cat y prod) y los trabajadores (PERSONAL) solo pueden visualizar y editar.

Un usuario debe tener su nombre, apellido, correo, password, tipo siendo
este por defecto PERSONAL (solo un ADMIN puede crear otro ADMIN)
```

### Comando usados en el proyecto

```
python -m venv venv

source venv/Scripts/activate

pip install flask flask-restful flask-sqlalchemy flask-cors marshmallow marshmallow-sqlalchemy python-dotenv psycopg2-binary
pip install Flask-Migrate
pip install bcrypt

python.exe -m pip install --upgrade pip

pip freeze > requirements.txt

pip install -r requirements.txt
```

### Comandos en Posgtres

```
psql -U postgres

CREATE DATABASE libreria;

\c libreria

\dt

\d usuarios

SEECT * FROM usuarios;

```

### Comandos para manejar las migraciones

```
flask db init => Inicializa las migraciones

flask db migrate -m "Agregue tabla usuarios" => crear una nueva migracion

flask db upgrade  => ejecuta las migraciones en la base de datos
```

### Enlaces

* ----