from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f'Estoy estudiando: {self.actividad}')

class Trabajador(Persona):
    def __init__(self,nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f'Estoy trabajando: {self.actividad}')

joe = Estudiante("Joe", 21, "Masculino", "programacion")
mac = Trabajador("Mac", 21, "Masculino", "programacion")

joe.presentarse()
joe.hacer_actividad()
