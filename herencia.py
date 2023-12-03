class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola")

class Artistas:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class EmpleadoArtista(Persona,Artistas):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artistas.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        print(f'Hola, soy: {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}')


roberto = EmpleadoArtista("Roberto",43,"argentino","joder", "google", 10000)

roberto.presentarse()

herencia = issubclass(EmpleadoArtista,Artistas)
instancia = isinstance(roberto,EmpleadoArtista)

print(instancia)

# herencia simple