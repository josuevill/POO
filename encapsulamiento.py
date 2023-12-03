""" class MiClase:
    def __init__(self):
        self.__atributo_privado = "Valor"
    
    def __hablar(self):
        print("hola, como estas")

objeto = MiClase()
print(objeto.__atributo_privado) """

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, new_nombre):
        self._nombre = new_nombre



me = Persona("Lucas",21)
nombre = me.get_nombre()
print(nombre)

me.set_nombre("Juan")
nombre = me.get_nombre()
print(nombre)