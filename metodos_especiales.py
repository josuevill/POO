class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):              # devuelve una representacion del objeto en una cadena de texto
        return f'Persona(nombre={self.nombre}, edad={self.edad})'

    def __repr__(self):             # representacion del objeto
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self, otro):        # sobrecarga
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)

joe = Persona("Joe",21)
pedro = Persona("Pedro", 30)
maria = Persona("Maria", 18)

nueva_persona = joe + pedro + maria
print(nueva_persona)
