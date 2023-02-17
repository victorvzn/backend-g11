def suma(a, b):
  return a + b

# resultado_suma = suma(1, 2)
# print(resultado_suma)

def resta(a, b):
  return a - b

def multiplicacion(a, b):
  return a * b

def division(a, b):
  return a / b

def calcularResultadoPorOperacion(operacion, valor_1, valor_2):
  print(type(valor_1), type(valor_2))
  if (operacion == 'suma'):
    return suma(valor_1, valor_2)
  elif operacion == 'resta':
    return resta(valor_1, valor_2)
  else:
    return 'La operación no existe'

operacion = input('Ingrese el tipo de operación: ')
valor_1 = int(input('Ingrese el tupo de operación: '))
valor_2 = int(input('Ingrese el tupo de operación: '))

# resultado = calcularResultadoPorOperacion(operacion, valor_1, valor_2)

# print('El resultado de la operación que solicito es: ' + str(resultado))

nombre = input('Ingresesu nombre: ')
edad = input('Ingrese su edad: ')
print(f'Hola {nombre}, tu tienen {edad} años')
print('Hola {}, tu tienes {} años'.format(nombre, edad))