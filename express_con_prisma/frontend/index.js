const devolverProductos = async () => {
  const resultado = await fetch('http://127.0.0.1:3000/productos')

  const data = await resultado.json()

  console.log(data)
}

devolverProductos()