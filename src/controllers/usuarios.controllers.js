import { UsuarioModel } from '../models/usuarios.model.js'
import bcrypt from 'bcryptjs'
import jwt from 'jsonwebtoken'

export const registroUsuario = async (req, res) => {
  const data = req.body

  try {
    const nuevoUsuario = await UsuarioModel.create(data)

    console.log(nuevoUsuario)

    return res.status(201).json({
      message: 'Usuario creado exitosamente'
    })
  } catch (error) {
    return res.status(400).json({
      message: 'Error al crear el usuario',
      content: error.message
    })
  }
}

export const loginUsuario = async (req, res) => {
  // TODO: buscar el usuario y devolver su JWT si existe
  const { correo, password } = req.body

  try {
    const usuarioEncontrado = await UsuarioModel.findOne({ correo }).exec()

    console.log({ usuarioEncontrado })

    if (!usuarioEncontrado) {
      throw new Error('El usuario no existe')
    }

    const isVerifiedPassword = bcrypt.compareSync(password, usuarioEncontrado.password)

    if (isVerifiedPassword) {
      const payload = { jti: usuarioEncontrado.id, nombre: usuarioEncontrado.nombre }
      const secretKey = process.env.JWT_SECRET
      const options = { expiresIn: '1h' }

      const token = jwt.sign(payload, secretKey, options)

      return res.json({ content: token })
    } else {
      throw new Error('Credenciales incorrectas')
    }
  } catch (error) {
    return res.status(400).json({
      message: 'Error al autenticar al usuario',
      content: error.message
    })
  }
}
