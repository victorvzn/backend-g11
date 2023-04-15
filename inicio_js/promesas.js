// Es un objeto que representa la culminación de exito o error de una operación asincrona

async function ejecucion () {

  console.log('Sumar')
  console.log('Restar')

  const promesa = new Promise((resolve, reject) => {
    setTimeout(() => {
      // resolve('Informacion guardada en la base de datos')
      reject(new Error('Error al guardar el registro en la base de datos'))
    }, 5000)
  })

  // .then > sirve para indicar si la priomesa se ejecuto existosamente osea termino sin problemas
  // .catch > sirve para indicar si fallo la ejecución de la promesa

  // promesa
  //   .then(respuesta => console.log(respuesta))
  //   .catch(error => console.log(error))

  try {
    const respuesta = await promesa
    console.log(respuesta)
  } catch(error) {
    console.error('Error al ejecutar la promesa')
    console.error(error.message)
  }

  console.log('FINALIZÓ!')
}

function saludo (n) {
  console.log('Hola mundo ' + n)
}

saludo(1)
ejecucion()
saludo(2)
