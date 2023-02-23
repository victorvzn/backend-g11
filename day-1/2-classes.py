class Persona:
  # cuando una variable se define dentro de una clase pasa a llamarse ATRIBUTO
  estatura = 1.80
  peso = 80
  signo_zodiacal = 'LEO'

  def sumar(self, *args):
    # self es como el this en el caso de js, c#, c++
    # cuando una función se declara o se define denro de una clase pasa a llamrse METODO
    # Recibir un número ilimitado de numeros para realizar su sumatoria
    acumulador = 0
    for numero in args:
      acumulador += numero
    return acumulador
  
  def saludar(self, nombre):
    return 'Hola {}'.format(nombre)
  

# cuando sacamos unan 'copia' de la clase para utilizarla estamos creando una instancia
persona1 = Persona()
persona2 = Persona()

# modifico los atributos de esa persona en particular
persona1.peso = 70
persona2.peso = 50

# todas las modificaciones que hacemos es independiente de la instancia
print(persona1.peso) # --> 70
print(persona2.peso) # --> 50

print(persona1.sumar(10, 5, 41, 526, 489, 63))
print(persona1.sumar(5, 8, 65, 985, 492, 520, 700))