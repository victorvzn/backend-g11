import { EventoModel } from '../models/eventos.model.js'
import { UsuarioModel } from '../models/usuarios.model.js'
import { subirImagenes } from '../utils/s3.js'

export const crearEvento = async (req, res) => {
  // TODO: ya no vamos a recibir el usuario por el body, ahora el usuario vendra por el req.user
  const data = req.body

  try {
    const nuevoEvento = await EventoModel.create(data)

    // TODO: reemplaza por req.user (usando autenticacion)
    // TODO: El findById ya no seria necesario porque lo estamos haciendo en el middleware
    // TODO: DEPECRATED
    // const usuarioEncontrado = await UsuarioModel.findById(data.usuario)
    const usuarioEncontrado = req.user

    // Actualizando los eventos que tiene ese usuario
    await UsuarioModel.updateOne(
      // TODO: reemplazar data.usuario > req.user.id
      { _id: usuarioEncontrado.id },
      { eventos: [...usuarioEncontrado.eventos, nuevoEvento._id] }
    )

    return res.status(201).json({
      message: 'Evento creado exitosamente',
      content: nuevoEvento
    })
  } catch (error) {
    return res.status(400).json({
      message: 'Error al crear el evento',
      content: error.message
    })
  }
}

export const probarS3 = async (req, res) => {
  const resultado = await subirImagenes()

  console.log({ resultado })

  res.json({
    message: 'Archivo subido exitosamente'
  })
}
