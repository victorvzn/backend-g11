# Backend de Codigo G11 - Veterinaria

**Enunciado:**

Tool: https://dbdiagram.io/d

>  Se requiere guardar las mascotas de un usuario, estas mascotas tienen su 
>  nombre, sexo (Masculino, Femenino), fecha_nacimiento, alergias, foto 
>  a su vez los clientes pueden tener : nombre, apellido, correo, password, 
>  un cliente puede tener varias mascotas y se necesita que cada mascota lleve 
>  un historial de ventas, las ventas pueden tener en su cabecera: 
>  id, total, fecha, serie, numero
>  y en su detalle de las ventas:
>  cantidad, descripcion (producto), precio, importe
>  (multiplicacion de la cantidad y el precio)
>  ademas su tabla de productos en la cual tendremos: id, nombre, precio, disponibilidad
>  y por ultimo manejar la informacion de la siguiente manera
>  se debe de registrar a todo el personal de la veterinaria y solo el personal 
>  autorizado puede agregar, editar o desabilitar productos
>  usuarios (esta tabla sera la tabla de clientes) agregar a esa tabla 
>  tipo_usuario (CLIENTE, ADMINISTRADOR)

### Comandos

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

python.exe manage.py makemigrations gestion --name cree_tabla_usuario
python.exe manage.py migrate gestion
python.exe manage.py showmigrations -> mostrara todas las migraciones en mi proyecto y las que no se ha ejecutado se mostrara 'vacia' [ ] y las que si [X]
python.exe manage.py migrate
python.exe manage.py showmigrations

pip install psycopg2-binary

python.exe manage.py createsuperuser > da un formulario para crear un superusuario con acceso al panel administrativo

python.exe manage.py sqlmigrate gestion 0001 > Mostrar en lenguaje SQL que contiene esa migración
```


### Resources

* https://docs.djangoproject.com/en/4.1/topics/auth/customizing/