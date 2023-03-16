# Repositorio: Backend de Codigo G11 - Semana05

# Enunciado para crear el diagrama de base de datos con https://dbdiagram.io/d

```
Se requiere un sistema para almacenar los articulos de una libreria, en la cual en los productos se debe almacenar: nombre, precio, fecha_creacion, categoria, imagen.

A su vez, la categoria debe contener: nombre, imagen, estado.

Ademas, se debe gestionar las operaciones por los usuarios siendo estos ADMIN o PERSONAL (los ADMIN solo pueden crear y eliminar cat y prod) y los trabajadores (PERSONAL) solo pueden visualizar y editar.

Un usuario debe tener su nombre, apellido, correo, password, tipo siendo
este por defecto PERSONAL (solo un ADMIN puede crear otro ADMIN)
```

### Comando usados

```
python -m venv venv

source venv/Scripts/activate

pip install flask flask-restful flask-sqlalchemy flask-cors marshmallow marshmallow-sqlalchemy python-dotenv psycopg2-binary

python.exe -m pip install --upgrade pip

pip freeze > requirements.txt

pip install -r requirements.txt

flask db init => inicializar las migraciones

flask db migrate -m "Agregue tabla niveles" => crear una nueva migracion

flask db upgrade  => ejecuta las migraciones en la base de datos

psql -u username

CREATE DATABASE tareas;

\c tareas

\dl
```


### Enlaces

* ----