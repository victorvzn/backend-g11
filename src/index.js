import express from 'express'
import cors from 'cors'
import dotenv from 'dotenv'

import { usuarioRouter } from './routers/usuarios.routes.js'
import { productoRouter } from './routers/productos.routes.js'

// utilizando todas las variables definidas en el archivo .env como si fueran variables de entorno
dotenv.config()

// TODO: Tarea: En base al MER de la semana09 crear los modelos en prisma con las migraciones correspondientes

const PORT = 3000

const servidor = express()

servidor.use(cors())
servidor.use(express.json())

servidor.use(usuarioRouter)
servidor.use(productoRouter)

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)
})
