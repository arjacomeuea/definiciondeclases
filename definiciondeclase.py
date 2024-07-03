# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado (encapsulación)
        self.__edad = edad  # atributo privado (encapsulación)

    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")

    def saludo(self):
        print(f"Hola, me llamo {self.__nombre}.")

# Clase derivada
class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.__matricula = matricula  # atributo privado (encapsulación)

    def mostrar_informacion(self):
        super().mostrar_informacion()  # Llamada al método de la clase base
        print(f"Matrícula: {self.__matricula}")

    def saludo(self):
        print(f"Hola, soy {self._Persona__nombre} y soy un estudiante.")  # Acceso a atributo privado de Persona

# Ejemplo de polimorfismo
def saludo_persona(persona):
    persona.saludo()

# Crear instancias de las clases
persona1 = Persona("Juan", 40)
estudiante1 = Estudiante("Carlos", 20, "A12345")

# Mostrar información
persona1.mostrar_informacion()
estudiante1.mostrar_informacion()

# Demostrar polimorfismo
saludo_persona(persona1)
saludo_persona(estudiante1)
