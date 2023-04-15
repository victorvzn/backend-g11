import { Router } from 'express'
import { actualizarCategoria, crearCategoria, devolverCategoria, eliminarCategoria, listarCategoria } from '../controllers/categorias.controller.js'

export const categoriaRouter = Router()

categoriaRouter
  .route('/categorias')
  .post(crearCategoria)
  .get(listarCategoria)

categoriaRouter
  .route('/categorias/:id')
  .get(devolverCategoria)
  .patch(actualizarCategoria)
  .put(actualizarCategoria)
  .delete(eliminarCategoria)