# principio de abierto / cerrado

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError

class NoificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando email a {self.usuario.email}")

class NoificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")

class NoificadorWhatsapp(Notificador):
    def Notificar(self):
        print(f"Enviando WhatsApp a {self.usuario.whatsapp}")