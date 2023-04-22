import express from 'express'
import dotenv from 'dotenv'
import cors from 'cors'

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

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)
})
