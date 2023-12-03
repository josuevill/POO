# principio de responsabilidad unica
# una clase solo tiene que tener una razon para cambiar
# cada clase solo tiene que tener una responsabilidad o tarea

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia - 2)
            print("Has movido el auto")
        else:
            print("No hay suficinete combustible")
    
    def obtener_posicion(self):
        return self.posicion
    
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

tanque = TanqueDeCombustible()
auto = Auto(tanque)

print(auto.obtener_posicion())
auto.mover(10)
print(auto.obtener_posicion())
auto.mover(20)
print(auto.obtener_posicion())
auto.mover(60)
print(auto.obtener_posicion())
auto.mover(100)
print(auto.obtener_posicion())
auto.mover(100)
print(auto.obtener_posicion())