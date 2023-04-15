import express from 'express'
import cors from 'cors'

// TODO: Tarea: En base al MER de la semana09 crear los modelos en prisma con las migraciones correspondientes

const PORT = 3000

const servidor = express()

servidor.use(cors())
servidor.use(express.json())

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)
})