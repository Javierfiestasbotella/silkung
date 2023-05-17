
import os
from dotenv import load_dotenv
import openai
import spacy

load_dotenv()

#llamamos a la clave que está en el archivo .env
api_key = os.getenv('OPENAI_API_KEY')

#ahora le decimos que es nuestra clave la que tiene que utilizar
openai.api_key = api_key

preguntas_anteriores = []
respuestas_anteriores = []

def preguntar_chat_gpt(prompt, modelo="text-davinci-002"):
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=0.7,
        max_tokens=200
    )
    return respuesta.choices[0].text.strip()

def iniciar_chatbot():
    print('Bienvenido a nuestro chatbot basico; escribe salir si quieres terminar')
    while True:
        conversacion_historica= ''
        ingreso_usuario = input('\nTu:')
        if ingreso_usuario.lower() == 'salir':
            break

        for pregunta, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
            conversacion_historica += f'El usuario pregunta: {pregunta}/n'
            conversacion_historica += f'Buda Silkung responde: {respuesta}/n'


        prompt = f'El usuario pregunta: {ingreso_usuario}\n'
        conversacion_historica += prompt
        respuesta_gpt = preguntar_chat_gpt(conversacion_historica)
        print(f'{respuesta_gpt}')

        preguntas_anteriores.append(ingreso_usuario)
        respuestas_anteriores.append(respuesta_gpt)
if __name__ == "__main__":
    iniciar_chatbot()


