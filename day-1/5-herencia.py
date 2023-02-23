class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print('Buenos días!')

class Beneficio:
      def __init__(self, detalle):
          self.detalle = detalle
      
      def mostrar_beneficios(self):
          return {
              'detalle': self.detalle
          }

class Alumno(Persona):
    def __init__(self, nombre, apellido, grado):
        self.grado = grado
        # llamando al constructor de la clase que estoy heredando
        super().__init__(nombre, apellido)
    
    def saludar(self):
        # Polimorfismo > polo (muchas) + morfo (formas) -> DEpendiendo de donde se mande a llamar el metodo este tendra un comportamiento u otro, en este caso estamos modificando el comportamiento del metodo de la clase padre 'saludar'
        saludo_padre = super().saludar()
        print(saludo_padre + 'Yo soy un alumno')
    
    def dar_vueltas(self):
        print('Dando vueltas...')

class Docente(Persona, Beneficio):
    def __init__(self, nombre, apellido, seguro_social, detalle):
        self.seguro_social = seguro_social
        # En el caso de utilizar herencia multiple el uso del comodin super() queda obsoleto ya que no se puede indicar a cual de las dos clases estamos haciendo referencia, para ello, se utiliza el nombre de la clase directamente y con ello se indica el metodo a utilizar
        # Se le pasa el 'self' para indicar tambien lo que seria la misma instancia para evitar cruce de informacion
        Persona.__init__(self, nombre, apellido)
        Beneficio.__init__(self, detalle)
    
    def evaluar(self):
        print('Evaluando...')

sami = Alumno('Sami', 'Villa', 'primero')
leo = Docente('Leo', 'Villa', '11335566', 'Pizza 15% dcto.')

sami.saludar()
print(leo.saludar())

print(leo.mostrar_beneficios())
