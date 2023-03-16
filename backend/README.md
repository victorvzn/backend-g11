# Repositorio: Backend de Codigo G11

```
python -m venv venv

source venv/Scripts/activate

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

* https://refactoring.guru/es/design-patterns/singleton
* https://marshmallow.rehttps://refactoring.guru/es/design-patterns/singletonadthedocs.io/en/stable/marshmallow.fields.html
* https://flask-jwt-extended.readthedocs.io/en/stable/
* https://jwt.io/
* https://flask-jwt-extended.readthedocs.io/en/stable/options/

** FIRMA frontend

https://www.figma.com/file/BMW7aKyYsYqbjuoyXsoC1a/Tareas-APP?node-id=0-1&t=7PoLuq4wINcgxudo-0
