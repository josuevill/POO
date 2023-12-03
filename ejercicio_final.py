# from textblob import TextBlob

# class AnalizadorDeSentiminetos:
#     def analizador_sentimiento(self, texto):
#         analisis = TextBlob(texto)
#         if analisis.sentiment.polarity > 0:
#             return "positivo"
#         elif analisis.sentiment.polarity == 0:
#             return "neutral"
#         else:
#             return "negativo"

# analizador = AnalizadorDeSentiminetos()
# resultado = analizador.analizador_sentimiento("Unabled to start")
# print(resultado)

import openai

openai.api_key = "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"
system_init = '''Has de cuenta que eres un analizador de sentimientos.
                 Yo te paso sentimientos y tú analizar el sentimiento de los mensajes.
                 y me das una respuesta con al menos un caracter y como maximo 4 caracteres
                 SÓLO RESPUESTAS NUMÉRICAS, donde -1 es negatividad máxima, o es neutral y 1 es positividad máxima.
                 (Solo puedes responder con ints o floats)'''

mensajes = [{"role": "system", "content": system_init}]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.8 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[1;37m"
        elif polaridad > -0.3 and polaridad < -0.1:
            return "\x1b[1;31m" + "Algo negativo" + "\x1b[1;37m"
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[1;37m"
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo" + "\x1b[1;37m"
        elif polaridad > -0.4 and polaridad < 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[1;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy positivo" + "\x1b[1;37m"
        else:
            return "\x1b[1;31m" + "Muy negativo" + "\x1b[1;37m"

analizador = AnalizadorDeSentimientos()

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

