-- https://dbdiagram.io/d

Table niveles {
  id serial pk
  numero int
  descripcion text
}

Table secciones {
  id serial pk
  nombre text
  alumnos int
  nivel_id int
  maestro_id int
}

Table maestros {
  id serial pk
  nombre text
  apellidos text
  correo text
  direccion text
}


Ref: niveles.id < secciones.nivel_id
Ref: maestros.id < secciones.maestro_id
       