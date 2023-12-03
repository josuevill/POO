# principio de segregacion de la interfaz
# ningun cliente tiene que ser forzado de usar interfazes que no utiliza

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def comer(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass



class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):
    def comer(self):
        print("El robot esta comiendo")

robot = Robot()
humano = Humano()
