const pedirAlumnos = async () => {
  const API_URL = 'http://127.0.0.1:5000/alumnos'
  
  const config = { method: 'GET' }

  const response = await fetch(API_URL, config)
  
  const data = await response.json()

  console.log(data)
}

pedirAlumnos()
