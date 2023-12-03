# principio de sustitucion de liskov's
# las clases derivadas tienen que ser sustituibles por sus clases bases

# class Ave:
#     def volar(self):
#         return "Estoy volando"

# class Pinguino(Ave):
#     def volar(self):
#         return "no puedo volar" 

# # variable de parametro
# def hacer_volar(ave = Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"

class AveNoVoladora(Ave):
    pass
