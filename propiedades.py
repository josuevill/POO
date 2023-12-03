class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre

me = Persona("Lucas", 21)

nombre = me.nombre
print(nombre)

me.nombre = "Joe"

nombre = me.nombre
print(nombre)

del me.nombre
print(nombre)