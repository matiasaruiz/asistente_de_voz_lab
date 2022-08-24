import pyttsx3
import pyaudio
import speech_recognition as sr
import pywhatkit
import pyjokes
import datetime
import webbrowser
import wikipedia


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

# Saludo inicial
def saludo_inicial():

    # Extraigo la hora
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        tiempo = 'Buenas Noches!'
    elif 6 <= hora.hour < 13:
        tiempo = 'Buen Dia!'
    else:
        tiempo = 'Buenas tardes!'



    tts(f'{tiempo} Soy Iris, tu asistente personal, en que puedo servirte?')


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


# Gestor de pedidos

def iris():

    saludo_inicial()

    # Loop Central
    corte = True
    while corte:

        # adquirir pedido
        pedido = stt().lower()

        if 'abrir mail' in pedido:
            tts('Por supuesto, abriendo Youtube')
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
            continue
        elif 'abrir navegador' or 'abrir buscador' in pedido:
            tts('Por supuesto, abriendo su navegador')
            webbrowser.open('https://www.google.com/')
            continue
        elif 'que dia es hoy' in pedido:
            what_day_is_tudei()
            continue
        elif 'que hora es' or 'la hora' in pedido:
            what_time_is_it()
            continue
        elif 'busca en wikipedia' in pedido:
            tts('Buscando eso en wikipedia')
            pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            tts('Wikipedia dice: ')
            tts(pedido)
            continue
        elif 'busca en internet' in pedido:
            tts('Buscando en internet')
            pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            tts(f"Esto es lo que he encontrado al respecto de {pedido}")
            continue
        elif 'reproduci' or 'reproduce' or 'reproducir' or 'play' in pedido:
            tts('Reproduciendo')
            pedido.replace('reproduci','')
            pedido.replace('reproduce', '')
            pedido.replace('reproducir', '')
            pedido.replace('play', '')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            tts(pyjokes.get_joke('es'))
            continue
        elif 'hasta luego' or 'chau' in pedido:
            tts('Hasta luego')
            continue
