# Backend de Codigo G11 - Veterinaria

```bash
python -m venv venv

source venv/Scripts/activate

pip install django

python.exe -m pip install --upgrade pip

pip freeze > requirements.txt

pip install -r requirements.txt


django-admin startproject veterinaria -> crea un nuevo proyecto en la ubicación de la terminal
python.exe manage.py startapp gestion -> crea una nueva aplicacion para el proyecto
python.exe manage.py runserver       -> levanta el servidor de django en DESARROLLO

python.exe manage.py showmigrations -> mostrara todas las migraciones en mi proyecto y las que no se ha ejecutado se mostrara 'vacia' [ ] y las que si [X]

python.exe manage.py migrate

pip install psycopg2-binary

python.exe manage.py createsuperuser > da un formulario para crear un superusuario con acceso al panel administrativo

python.exe manage.py makemigrations

python.exe manage.py sqlmigrate gestion 0001 > Mostrar en lenguaje SQL que contiene esa migración
```