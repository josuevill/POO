# principio de inversion de dependencias
# Los modulos de alto nivel no tienen que depender de los modulos de alto nivel si no que los dos deben depender de las absracciones
# Las abstracciones a su vez no deben depender de los detalles si no que los detalles deben depender de las abstracciones

# class Diccionario:
#     def verificar_palabra(self, palabra):
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
    
#     def corregir_texto(self, text):
#         pass

from abc import ABC, abstractmethod

class VerificarOrtografia(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificarOrtografia):
    def verficar_palabra(self, palabra):
        pass

class ServicioOnline(VerificarOrtografia):
    def verificar_palabra(self, palabra):
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
    
    def corregir_texto(self, texto):
        pass

corrector = CorrectorOrtografico(Diccionario())