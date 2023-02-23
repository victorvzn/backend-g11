def greet(name):
    saludo = 'Hola, {}!'.format(name)
    print(saludo)
  
greet('Victor')

def saludar_varios(*args):
    # si anteponemos en un parámetro '*' significa que
    # no hay límite de ese parámetro, este parámetro deber de ir 
    # al último todos los valores que le pasemos a este prámetro
    # se almacenaran en un tupla
    print(args)
    for name in args:
        saludo = 'Hola, {}'.format(name)
        print(saludo)

saludar_varios('Leo', 'Mate', 'Mari', 'Claudia', 'Sofi',' Mati')
saludar_varios('Samy', 'Victor')
saludar_varios() # --> ()
saludar_varios('Mari', 20, True, 10.5)

def informacion_usuario(**kwargs):
    # kwargs -> keyboard argument o se le pasan parámetros por llaves
    print(kwargs)
    print(kwargs['nombre']) # ok
    
    # .get('key_name') -> devuelve el valor si existe la llave, sino existe entonces devolverá None
    print(kwargs.get('estatura', 'NO EXISTE!!!')) # KeyError, estatura no existe
    try:
        print(kwargs['estatura']) # KeyError, estatura no existe
    except:
        print('No existe la llave estatura')

informacion_usuario(nombre='Mari', edad=20, estado_civil='soltero', estatura=1.73)
informacion_usuario(nombre='Pamela', apellido='Lopez', nacionalidad='Colombiana', fecha_nacimiento='31/06/1998')
print('El programa continua')


# Enunciado: recibir dos valores y hacer la división

def dividir(dividendo, divisor):
    # si la división da un erro entonces retornar un mensaje que diga 'División incorrecta'
    try:
      resultado = dividendo / divisor
      return resultado
    except ZeroDivisionError:
        # ingresa aqui cuando la división sea entre 0
        print('No puede haber división entre 0')
    except TypeError:
        # ingresa si la división tiene algún caracter
        print('Las divisiones solo pueden ser entre dos números')
    except:
        # ingresa aqui si no es ninguno de los dos errores anteriores
        return 'Error desconocido'

print(dividir(10, 5)) # --> 2.0
print(dividir(10, 0)) # --> 
print(dividir('a', 'h'))

try:
    print(dividir(5, ))
except:
    print('Falta un parámetro')