import jwt from 'jsonwebtoken'
import { UsuarioModel } from '../models/usuarios.model.js'

export const validarToken = async (req, res, next) => {
  // TODO: [PARTE 1] Validar que hay el header de autorizacion
  // TODO: [PARTE 1] Validar que la token sea correcto
  // TODO: [PARTE 1] agregaral req.user la informacion del usuario de la token
  if (!req.headers.authorization) {
    return res.status(401).json({
      message: 'Se necesita una token para realizar esta peticion'
    })
  }
  const token = req.headers.authorization.split(' ')[1]

  if (!token) {
    return res.status(401).json({
      message: 'El formato debe ser Bearer YOUR_TOKEN'
    })
  }

  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET)

    const usuarioEncontrado = await UsuarioModel.findOne({
      _id: payload.jti
    })

    console.log({ usuarioEncontrado })

    req.user = usuarioEncontrado

    next()
  } catch (error) {
    // si la token es incorrecta ingresara al catch y/o si el usuario no existe
    return res.status(400).json({
      message: 'Error',
      content: error.message
    })
  }
}
