import { Prisma } from "../prisma.js"

export const crearProducto = async (req, res) => {
  const data = req.body

  // SELECT id FROM categorias WHERE id = ...;
  console.log(data)

  // TODO: Validar si la categoria en la cual se quiere crear el producto no este deshabilitada
  const categoria = await Prisma.categoria.findFirst({
    where: {
      AND: [
        { id: data.categoriaId },
        { disponibilidad: true }
      ]
    },
    select: { id: true, disponibilidad: true },
  })

  if (!categoria) {
    return res.status(400).json({ message: 'Categoria no existe' })
  }
  
  try {
    const nuevoProducto = await Prisma.producto
      .create({ data: {
        ...data,
        fechaVencimiento: new Date(data.fechaVencimiento)
      }})
      
    res.status(200).json({ message: "Producto creado exitosamente", content: nuevoProducto })
  } catch(error) {
      return res.status(400).json({ message: 'Error al crear el producto', content: error.message })
  }
}

export const listarProductos = async (req, res) => {
  // TODO: agregar el listar productos 

  const productos = await Prisma.producto.findMany() 

  res.status(200).json({ content: productos }) 
}

export const devolverProducto = async (req, res) => {
  const { id } = req.params

  const productoEncontrado = await Prisma.producto.findFirst({
    where: { id: Number(id) },
    include:  { categoria: true}
  })

  if (!productoEncontrado) {
    return res.status(400).json({ message: 'Producto no existe' })
  }

  return res.status(200).json({ content: productoEncontrado })
}

export const actualizarProducto = async (req, res) => {
  // TODO: agregar la actualización de productos

  const { id } = req.params
  const data = req.body

  const producto = await Prisma.producto.findFirst({
    where: { id: Number(id) },
    select: { id: true }
  })

  if (!producto) {
    return res.status(400).json({ message: 'Producto no existe' })
  }

  const productoActualizado = await Prisma.producto
    .update({
      where: { id: producto.id },
      data: {
        ...data,
        fechaVencimiento: new Date(data.fechaVencimiento)
      }
    })

  res.json({
    message: "Producto se actualizo exitosamente",
    content: productoActualizado
  })
}

export const eliminarProducto = async (req, res) => {
  // 127.0.0.1:3000/productos/1 > /:id

  const { id } = req.params

  const producto = await Prisma.producto.findFirst({
    // where: { id: parseInt(id) },
    // where: { id: +id },
    where: { id: Number(id) },
    select: { id: true }
  })

  if (!producto) {
    return res.status(400).json({ message: 'Producto no existe' })
  }

  const productoEliminado = await Prisma.producto.delete({
    where: { id: Number(id) }
  })

  res.json({
    message: "Producto eliminado exitosamente",
    content: productoEliminado
  })
}