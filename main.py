import time
import random

BLACK = '\033[30m'  #estos son los colores usados
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

control = ""
puntos = 2
puntaje = 0

aciertos = [
    "Ingles no es un idioma oficial en Perú",
    "El gallito de las rocas es el ave nacional",
    "La escarapela no es un simbolo patrio", "Su nombre es Machu Picchu",
    "El pisco es la bebida insignia en el Perú", "fue el 28 de julio de 1821",
    "La papa es peruana", "El cañon del Cotahuasi es el mas profundo del Perú"
]
#Los aciertos en una lista
error = "Debes responder a, b, c o d\nIngrese nuevamente tu respuesta ->"
#Las preguntas en otra lista
Preguntas = [
    YELLOW + "1:¿Cual de estas lenguas no es considerada oficial en el Perú?",
    "2:¿Cual es el ave nacional del Perú?",
    "3:¿Cual de estos simbolos no es un simbolo patrio?",
    "4:¿La estacion cientifica que se encuentra en la Antartida se llama:",
    "5:Es la bebida insignia en el Perú:",
    "6:¿Cuando se dio la declaracion del Perú?",
    "7:Este importante alimento tiene origen peruano:",
    "8:Se considera como uno de los cañones mas profundos del mundo:" + RESET
]
#LAS ALTERNATIVAS EN OTRA LISTA
Alternativas = [
    BLUE + "a) Castellano\nb) Quechua\nc) Inglés\nd) Aimara" + RESET, YELLOW +
    "a) El condor andino\nb) El suri\nc) El gallinazo\nd) El gallito de las rocas"
    + RESET, RED +
    "a) La escarapela\nb) El escudo nacional del Perú\nc) El himno nacional\nd) La bandera del Perú"
    + RESET,
    BLACK + "a) Perú\nb) Machu Picchu\nc) Los Incas\nd)Tahuantinsuyo" + RESET,
    MAGENTA +
    "a) Pisco\nb) Chicha morada\nc) Chicha de Jora\nd) Mate de coca" + RESET,
    CYAN +
    "a) El 4 de julio de 1821\nb) El 28 de julio de 1820\nc) El 4 de julio de 1820\nd) El 28 de julio de 1821"
    + RESET, WHITE + "a) Maiz\nb) Papa\nc) Arroz\nd) Tomate" + RESET, BLUE +
    "a) Cañon del Sonche\nb) Cañon del Colca\nc) Cañon del Cotahuasi\nd) Cañon del Pato"
    + RESET
]
#Estas son las respuestas
Respuesta = ["c", "d", "a", "b", "a", "d", "b", "c"]
#LAS INCORRECTAS EN OTRA LISTA
Incorrectas = [
    "Incorrecto, si se considera un lenguaje nativo del Perú",
    "Incorrecto, no es el ave nacional del Perú",
    "Incorrecto, si se considera un simbolo patrio",
    "Alternativa incorrecta, ese no es su nombre",
    "Incorrecto, no es la bebida insignia del Perú", "Fecha Incorrecta",
    "¡Incorrecto!", "Incorrecto, ese no es el cañon mas profundo"
]
inicio_T = True  #PARA INICIAR EL BUCLE
intentos = 1
puntaje = 0
print("\t\t\t\t\t" + GREEN + "MI TRIVIA" + RESET)
nombre = input(BLUE + "Digite su nombre para empezar -> " + RESET)
print(YELLOW + f"Hola {nombre}, Bienvenido a mi Trivia\n En esta Trivia "
      f"responderas preguntas relacionadas a la historia del Perú" + RESET)
while inicio_T == True:
    conf = input(BLUE + "¿Estas listo para empezar? digita si o no ->" +
                 RESET).lower()  #USO EL
    # FOR Y EL WHILE PARA PEDIR SI O NO#
    while conf == "no" or conf != "si":
        if (conf == "no"):
            conf = input(BLUE + "Tomate tu tiempo te espero ->" +
                         RESET).lower()
        elif not (conf == "si" or conf == "no"):
            conf = input(
                BLACK + "caracteres invalidos, digite si o no ->" +
                RESET).lower()  #metodo lower para asegurar que sean minusculas
    puntos = 2
    if conf == "si":
        print(RED + "Comenzamos en....." + RESET)  #da comienzo a la trivia
        time.sleep(1)
        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)
        for i in range(0, 8):
            print(Preguntas[i]
                  )  #Llamo a las listas para hacer la trivia mas automatica
            time.sleep(1)
            print(Alternativas[i])
            time.sleep(1)
            respuesta = input(BLUE + "Ingrese su respuesta ->" + RESET).lower()
            while respuesta not in ("a", "b", "c", "d"):
                respuesta = input(error).lower()
            print((CYAN + "Comprobando respuesta...." + RESET))
            time.sleep(1)
            if respuesta == Respuesta[
                    i]:  #Si acierta llama la lista de aciertos
                puntaje += puntos
                print(f"Correcto {nombre},{aciertos[i]}")
            else:
                puntaje -= puntos
                print(Incorrectas[i])  #Si falla llama la lista de incorrectas
            time.sleep(1)
            print(F"Ahora tienes {puntaje} puntos"
                  )  #Cada vez que pasa el for muestra el puntaje
            input("Presiona enter para continuar")
            if i == 7:  #Al llegar al final de la trivia muestra
                dado = int(
                    input(
                        "LLegaste a la parte final de la trivia\n"
                        "introduce un numero entre 1 y el 5 para girar la ruleta!->"
                    ))
                print(BLUE + "Girando ruleta...." + RESET)
                for d in range(dado, 0, -1):
                    print(d)
                    time.sleep(2)
                time.sleep(2)
                r = random.randint(1, 5)
                print(YELLOW + f"Felicidades ganaste estos puntos: {r}" +
                      RESET)
                puntaje += r
                print(F"Ahora tienes {puntaje} puntos")
            if i == 7:
                print(BLUE + "¿Quieres repetir la trivia?" + RESET)
                control = input("Digita si o no -> ")
            else:
                if i == 3:  #Aumento los puntos mediante un if que se resetea al reiniciar la trivia
                    print(
                        YELLOW +
                        "Las siguiente preguntas son de nivel intermedio, sumaran\no restaran 4 puntos si aciertas o no"
                        + RESET)
                    time.sleep(2)
                    input(BLUE + "Presione enter para continuar..." + RESET)
                    puntos = 4
                elif i == 6:
                    print(
                        YELLOW +
                        "La ultima pregunta es de nivel dificil\nsu valor aumenta a 8 puntos"
                        + RESET)
                    time.sleep(2)
                    input(GREEN + "Presiona enter para continuar..." + RESET)
                    puntos = 8
                print(BLUE + "Siguiente pregunta en....." + RESET)
                for i in range(2, 0, -1):
                    print(i)
                    time.sleep(1)
    if control != "si":  #Si el jugador quiere continuar
        inicio_T = False  #se le da la opcion de hacerlo contando sus intentos
        print(YELLOW +
              "Gracias por jugar mi trivia espero que te hayas divertido" +
              RESET)
        print(GREEN + f"El puntaje de esta ronda: {puntaje}" + RESET)
        print(GREEN + f"Intentos totales: {intentos}" + RESET)
    else:
        print(GREEN + f"Tu puntaje en esta ronda es de {puntaje}" + RESET)
        intentos += 1
        puntaje = 0
