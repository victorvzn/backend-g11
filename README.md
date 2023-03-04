# Repositorio: Backend de Codigo G11

```
python -m venv env

source env/Scripts/activate

pip install Flask

pip freeze > requirements.txt

```

### flask-con-orm

| Renombra `.env.example` a `.env`

```bash
flask db init => inicializar las migraciones

flask db migrate -m "Agregue tabla niveles" => crear una nueva migracion

flask db upgrade  => ejecuta las migraciones en la base de datos
```

```sql
psql -u username

CREATE DATABASE colegio;

\c colegio

\dl

\d niveles

INSERT INTO niveles (numero, descripcion) VALUES (1, 'Los que recien ingresan al cole');
```

### Links

* https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#installation
* https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/config/
* https://pypi.org/project/python-dotenv/#getting-started
* https://flask-restful.readthedocs.io/en/latest/
* https://tecsup.webex.com/tecsup-sp/url.php?frompanel=false&gourl=https%3A%2F%2Fdocs.sqlalchemy.org%2Fen%2F20%2Fcore%2Fmetadata.html
* https://tecsup.webex.com/tecsup-sp/url.php?frompanel=false&gourl=https%3A%2F%2Fdocs.sqlalchemy.org%2Fen%2F20%2Fcore%2Ftype_basics.html
* https://marshmallow.readthedocs.io/en/stable/