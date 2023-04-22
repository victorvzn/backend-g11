import { Router } from 'express'

import * as controller from '../controllers/eventos.controllers.js'

import { validarToken } from '../utils/wachiman.js'

export const eventoRouter = Router()

eventoRouter.post('/eventos', validarToken, controller.crearEvento)

eventoRouter.route('/probar/s3').get(controller.probarS3)
