import openai

openai.api_key = "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"
system_init = '''Has de cuenta que eres un analizador de sentimientos.
                 Yo te paso sentimientos y tú analizar el sentimiento de los mensajes.
                 y me das una respuesta con al menos un caracter y como maximo 4 caracteres
                 SÓLO RESPUESTAS NUMÉRICAS, donde -1 es negatividad máxima, o es neutral y 1 es positividad máxima.
                 (Solo puedes responder con ints o floats)'''

mensajes = [{"role": "system", "content": system_init}]

class Sentimiento():
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos

    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy negativo", "31")

rangos = [
    ((-0.6,-0.3), Sentimiento("negativo", "31")),
    ((-0.3,-0.1), Sentimiento("algo negativo", "31")),
    ((-0.1,0.1), Sentimiento("neutral", "33")),
    ((0.1,-0.4), Sentimiento("algo positivo", "32")),
    ((0.4,0.9), Sentimiento("positivo", "32")),
    ((0.9,1), Sentimiento("muy positivo", "32")),
]

analizador = AnalizadorDeSentimientos(rangos)

while True:
    user_prompt = input("\x1b[1;33m" + "\nDime algo: " + "\x1b[1;37m")
    mensajes.append({"role": "user", "content": user_prompt})
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )

    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role": "assistant", "content": respuesta})

    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)
