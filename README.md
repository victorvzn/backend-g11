# Authentication + Expressjs

Proyecto para ver auth con express y prisma

### Enunciado del problema

Se necesita una base de datos para poder almacenar los productos de una tienda en la cual se tiene la siguiente informacion: Nombre, precio, precio_oferta, disponible, descripcion, procedencia.
Adicional a ello tenemos usuarios en los cuales tienen las siguientes propiedades: nombre, apellido, correo, password, tipo_usuario (ADMIN, CLIENTE)
HINT: Averiguar como colocar ENUM en prisma
Un cliente puede tener un carrito en la cual puede agregar productos y sus cantidades. NOTA: el usuario solo puede tener como MAXIMO 1 carrito.

### Comandos

```
npx prisma init
npm prisma migrate dev

select * from pg_stat_database;
select numbackends from pg_stat_database;
```

### Links

* https://marmelab.com/react-admin/
* https://www.prisma.io/docs/concepts/components/prisma-schema/relations
* https://www.prisma.io/docs/reference/api-reference/prisma-schema-reference#model-field-scalar-types
* https://www.prisma.io/docs/concepts/components/prisma-cli
* https://www.prisma.io/docs/getting-started/quickstart