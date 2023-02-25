# Instalación de Postgres

Pasos:

1. Instalar postgres desde https://www.postgresql.org/
    - Asignar contraseña de root
2. Modificar la variable de entorno PATH con la ruta de instalación de postgres: C:\Program Files\PostgreSQL\15\bin
3. En la terminal accederemos a postgres con el siguiente comando:

```
$ psql -U postgres
  Contraseña para usuario postgres:****
  psql (15.2)
  postgres=#
```

# Creando tablas

Datos = Columna, mismo tipo de dato
Tabla = Conjunto de filas
Registro o fila = agrupamiento de datos

* Comando para crear una base de datos

## DDL y DML

- DDL: Data Definition Language, Definir: tablas, bd, columnas
- DML: Data Manipulation Language, Manipular la informacion: agregar, editar, eliminar y visualizar

# Resources

* https://www.postgresql.org/docs/current/sql-createdatabase.html
* https://www.postgresql.org/docs/current/sql-createtable.html
* https://www.postgresql.org/docs/current/datatype.html