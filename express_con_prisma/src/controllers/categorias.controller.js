import { Prisma } from "../prisma.js"

export const crearCategoria = async (req, res) => {
  const body = req.body

  // console.log({body})

  const newCategoria = { data: body }

  const resultado = await Prisma.categoria.create(newCategoria)

  // console.log({resultado})

  res.status(200).json({ message: "La categoria se creo exitosamente" })
}

export const listarCategoria = async (req, res) => {
  const categorias = await Prisma.categoria.findMany()

  res.status(200).json({ content: categorias })
}

export const devolverCategoria = async (req, res) => {
  // 127.0.0.1:3000/categorias/1 > /:id

  const { id } = req.params

  const categoria = await Prisma.categoria.findFirst({
    where: { id: Number(id) },
    include:  { productos: true}
  })

  if (!categoria) {
    return res.status(400).json({ message: 'La categoria no existe' })
  }

  return res.status(200).json({ content: categoria })
}

export const actualizarCategoria = async (req, res) => {
  // 127.0.0.1:3000/categorias/1 > /:id

  const { id } = req.params
  const body = req.body

  // SELECT * FROM categorias;
  // SELECT id FROM categorias;

  const categoria = await Prisma.categoria.findFirst({
    // where: { id: parseInt(id) },
    // where: { id: +id },
    where: { id: Number(id) },
    select: { id: true }
  })

  if (!categoria) {
    return res.status(400).json({ message: 'La categoria no existe' })
  }

  const categoriaActualizada = await Prisma.categoria.update({
    where: { id: categoria.id },
    data: body
  })

  res.json({
    message: "La categoria se actualizo exitosamente",
    content: categoriaActualizada
  })
}

export const eliminarCategoria = async (req, res) => {
  // 127.0.0.1:3000/categorias/1 > /:id

  const { id } = req.params

  const categoria = await Prisma.categoria.findFirst({
    // where: { id: parseInt(id) },
    // where: { id: +id },
    where: { id: Number(id) },
    select: { id: true }
  })

  if (!categoria) {
    return res.status(400).json({ message: 'La categoria no existe' })
  }

  const categoriaEliminada = await Prisma.categoria.delete({
    where: { id: Number(id) }
  })

  res.json({
    message: "La categoria se elimino exitosamente",
    content: categoriaEliminada
  })
}