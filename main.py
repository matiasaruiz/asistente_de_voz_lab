import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import datetime


# Speech to text 
def stt():
    
    # El reconocedor de voz
    r = sr.Recognizer()

    # Configuracion de mic
    with sr.Microphone() as origen:
        
        #  Pausa pre escucha
        r.pause_treshold = 0.8

        # Notificacion de cominezo de grabacion
        print("Puedes comenzar a hablar!")

        # Guardar el audio 
        audio = r.listen(origen)

        try:
            
            # Buscar lo escuchado en Google
            rqst = r.recognize_google(audio, languaje="es-ar")

            # Test de que anda
            print("Dijiste: " + rqst)

            # Retornar el request
            return rqst

        # Si no se comprende el audio
        except sr.UnknownValueError:

            print("No entendi lo que has dicho :/")
            return "Sigo esperando"


        # Si no se puede resolver el pedido
        except sr.RequestError:
            print("No hay servicio :/")
            return "Sigo esperando"

        # Error Inesperado    
        except:

            print("Algo salio mal :o")
            return "Sigo esperando"


# Text to Speech

def tts(mensaje):

    # Encender el motor
    engine = pyttsx3.init()

    # Decir el mensaje
    engine.say(mensaje)
    engine.runAndWait()



### FUNCIONES INFORMADORAS ###

# Informar dia de la semana
def what_day_is_tudei():

    # Extraigo que dia es hoy
    dia = datetime.date.today()

    # Extraigo el indice de dia de la semena
    dia_semana = dia.weekday()

    # Diccionario de nombre de los dias
    semana = {0: 'Lunes',
              1: 'Martes',
              2: 'Miércoles',
              3: 'Jueves',
              4: 'Viernes',
              5: 'Sábado',
              6: 'Domingo'}

    # Decir dia de la semana
    tts(f'Hoy es {semana[dia_semana]}')

# Informar la hora
def what_time_is_it():

    # Get Full hora
    hora = datetime.datetime.now()

    # Format hora
    hora_formated = f'La hora es {hora.hour} horas, con {hora.minute} minutos y {hora.second} segundos.'

    # Decir Hora
    tts(hora_formated)

what_time_is_it()