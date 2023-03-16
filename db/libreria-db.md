// Hecho con https://dbdiagram.io/d

// ENUNCIADO

// Se requiere un sistema para almacenar los articulos de una libreria, en la cual en los productos se debe almacenar: nombre, precio, fecha_creacion, categoria, imagen.
// A su vez, la categoria debe contener: nombre, imagen, estado.
// Ademas, se debe gestionar las operaciones por los usuarios siendo estos ADMIN o PERSONAL (los ADMIN solo pueden crear y eliminar cat y prod) y los trabajadores (PERSONAL) solo pueden visualizar y editar.
// Un usuario debe tener su nombre, apellido, correo, password, tipo siendo
este por defecto PERSONAL (solo un ADMIN puede crear otro ADMIN)


Enum TIPO_USUARIO {
  ADMIN
  PERSONAL
}

Table usuario {
  id serial [pk]
  nombre text
  apellido text
  correo text unique
  password text
  tipo TIPO_USUARIO
  fecha_creacion datetime
}

Table productos {
  id serial [pk]
  nombre text
  precio float
  imagen text
  categoria_id int
  fecha_creacion datetime
}

Table categorias {
  id serial [pk]
  nombre text
  imagen text
  estado boolean
  fecha_creacion datetime
}

Ref: "productos"."categoria_id" > "categorias"."id"

