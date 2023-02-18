from pprint import pprint

# Crear una clase Operaciones con sus respectivos métodos
# (sumar, restar, multiplicar y dividir). Esta clase recibirá dos números.

class OperacionesMatematicas:
    def __init__(self, valor_1, valor_2) -> None:
        self.a = valor_1
        self.b = valor_2
        # print(valor_1)
    
    def sumar(self):
        return self.a + self.b
    
    def restar(self):
        return self.a - self.b
    
    def multiplicar(self):
        return self.a * self.b
    
    def dividir(self):
        print(self.a / self.b) # 0.7142857142857143
        return self.__redondear(self.a / self.b) # 0.71
    
    def __redondear(self, numero): # Método privado
        return round(numero, 2)
    
operaciones = OperacionesMatematicas(5, 7)

# print(operaciones.dividir())

# operaciones.__redondear(25.2222) # Object has no attribute


# Crear una clase Usuario que reciba los datos de un usuario
# (nombre, edad, dni, estatura, estado civil) y convertir estos datos en un diccionario

class Usuario:
    def __init__(self, nombre, edad, dni, estatura, estado_civil) -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.estatura = estatura
        self.estado_civil = estado_civil
    
    def toDictionary(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "dni": self.dni,
            "estatura": self.estatura,
            "estado_civil": self.estado_civil
        }

usuario = Usuario("Victor", 36, '22334455', 2.50, 'Cansado')

pprint(usuario.toDictionary())