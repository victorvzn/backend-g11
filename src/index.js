import express from 'express'
import dotenv from 'dotenv'
import cors from 'cors'
import mongoose from 'mongoose'

import * as rutas from './routes/index.js'

dotenv.config()

const servidor = express()

const PORT = process.env.PORT || 3000

servidor.use(express.json())

servidor.use(
  cors({
    methods: ['GET', 'POST', 'PUT', 'DELETE'],
    origin: ['*']
  })
)

servidor.use(rutas.usuarioRouter)
servidor.use(rutas.eventoRouter)

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)

  conectarBD()
})

function conectarBD () {
  mongoose
    .connect(process.env.MONGODB_URI)
    .then(() => {
      console.log('Base de datos conectada 🔌')
    })
    .catch(err => {
      console.error('Error al conectarse a la base de datos')
      console.error(err.message)
    })
}
