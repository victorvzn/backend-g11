import { Router } from 'express'
import { actualizarProducto, crearProducto, devolverProducto, eliminarProducto, listarProductos } from '../controllers/productos.controller.js'

export const productoRouter = Router()

// productoRouter.route('/productos').post(crearProducto)

productoRouter.post('/productos', crearProducto)
productoRouter.get('/productos', listarProductos)

productoRouter.get('/productos/:id', devolverProducto)
productoRouter.patch('/productos/:id', actualizarProducto)
productoRouter.put('/productos/:id', actualizarProducto)
productoRouter.delete('/productos/:id', eliminarProducto)