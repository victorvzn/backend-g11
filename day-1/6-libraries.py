from camelcase import CamelCase

instance = CamelCase()

texto = 'buenas noches, como estan'
resultado = instance.hump(texto)
print(resultado)


# Desde python 3.8, se pueden añadir los tipos
def sumar(num1: int, num2: int):
    """Función que sirve para sumar dos números y retorna el resultado"""
    return num1 + num2

sumar(10, 5)
