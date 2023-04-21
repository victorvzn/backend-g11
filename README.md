                                                                                                                                                                            # Backend de Codigo G11 -  Semana10 (MONGODB)

### Comandos

```
db          > muestra en que base de datos nos ubicamos
show dbs    > lista las bases de datos que existen en mi servidor
use DB_NAME > crear y movernos a esa base de datos, si no existe la crea y si existe solamente nos movemos

-- COMANDOS PRACTICOS
-- Para insertar
db.personas.insertOne({ nombre: 'Eduardo', apellido: 'de Rivero', correo: 'ederiveroman@gmail.com' })
db.personas.intertMany( [ { nombre: 'Maria' }, { sexo: 'M', fechaNacimiento: new Date('1995-07-31') } ] )
db.personas.insertMany( [ { nombre: 'Maria' }, { sexo: 'M', fechaNacimiento: new Date('1995-07-31') } ] )
db.personas.insertOne({ nombre: 'Juan', sexo: 'M'})
                                                                                                      
use personas

-- Para buscar
-- SELECT * FROM personas;
db.personas.find()

-- Hacer busquedas mas especificas
db.personas.find({ $or: [ { nombre : 'Juan' }, { nombre: 'Eduardo' } ] } )


db.personas.insertOne({ nombre: 'Victor', apellido: 'Villazón', correo: 'vvillazon@gmail.com' })
db.personas.insertMany([{ nombre: 'Maria' }, { sexo: 'M', fechaNacimiento: new Date('1995-07-31') }])
db.personas.find()
db.personas.insertOne({nombre: 'Juan', sexo: 'M'})

db.personas.find({ nombre: 'Juan' })
db.personas.find({ nombre: 'Juan', sexo: 'F' })

db.personas.find({ $or: [ {nombre: 'Juan' }, { nombre: 'Victor' } ] })

-- Actualizaciones
-- Primero va el valor a buscar y luego los campos a actualizar

db.productos.updateOne({ nombre: 'piña'}, { $set: { precio: 5, disponible: false } } )

db.productos.updateMany({ precio: { $gt: 1 } }, { $set: { disponible: false } } )
db.productos.updateMany({ precio: { $gt: 1 } }, { $set: { disponible: true } } )

db.productos.deleteOne({ nombre: 'piña' })
db.productos.deleteMany({ precio: { $gt: 1 } })

db.categorias.insertMany([
  {
    nombre: 'Abarrotes',
    descripcion: 'Todo relacionado a abarrotes',
    productos: [
      {
        nombre: 'Detergente ayudin',
        descripcion: 'A la grasa le pone fin',
        precio: 7.50
      },
      {
        nombre: 'Cepillo dental',
        descripcion: 'Poderoso Cepillo',
        precio: 1.80
      }
    ]
  },
  {
    nombre: 'Verduras',
    descripcion: 'Ricas verduras para la casa',
    productos: [
      {
        nombre: 'Beterraga',
        precio: 1.50
        descripcion: null
      }
    ]
  }
])
```

### Ejercicios

```
--- Insertar en la tabla productos los siguientes valores:
[
  {
    nombre: 'piña',
    precio: 1.80,
    disponible: true
  },
  {
    nombre: 'frambuesa',
    precio: 5.20,
    disponible: true
  },
  {
    nombre: 'pitahaya',
    precio: 4.50,
    disponible: false
  },
  {
    nombre: 'sauco',
    precio: 8.50,
    disponible: true
  },
]

-- Buscar todos los productos cuyo nombre sea 'pitahaya'
db.productos.find({ nombre: 'pitahaya' })

-- Buscar todos los productos cuyo nombre sea 'frambuesa' o 'sauco'
db.productos.find({ $or: [ { nombre: 'frambuesa' }, { nombre: 'sauco' } ] })

-- Buscar todos los productos cuyo nombre sea 'toronja' o 'piña' y su precio sea mayor a 1.00
db.productos.find({$or: [ { nombre: 'toronja' }, { nombre: 'piña' } ], $and: [ { precio: { $gt: 1.00 } } ] })
db.productos.find({
  $and: [
    {
      $or: [ { nombre: 'toronja' }, { nombre: 'piña' } ],
      precio: { $gt: 1.00 }
    }
  ]
})

-- Buscar todos los productos que valgan menos de 5.00 y que esten disponibles
db.productos.find({
  $and: [
    {
      precio: { $lt: 5.00 },
      disponible: { $eq: true }
    }
  ]
})

db.productos.find({
  precio: {
    $lt: 5.00
  },
  disponible: true
})

db.productos.find({
  $and: [
    {
      precio: { $lt: 5.00 }
    },
    {
      disponible: { $eq: true }
    } 
  ]
})

db.categorias.aggregate([
    { $match: {nombre: 'Verduras'}},
    { $unwind: '$productos'},
    { $match: {'productos.precio': {$gt: 2.5}}},
    { $group: {_id: '$_id', productos: {$push: '$productos'}}}
])
```


### Links

* https://www.mongodb.com/docs/manual/reference/operator/query/
* https://www.mongodb.com/try/download/shell
* https://stackoverflow.com/questions/15117030/how-to-filter-array-in-subdocument-with-mongodb