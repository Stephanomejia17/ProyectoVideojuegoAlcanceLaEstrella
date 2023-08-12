import random

preguntas = ["¿Cuál es la capital de Australia?",
                 "¿En qué año ocurrió la Revolución Industrial?",
                 "¿Qué famoso pintor fue conocido por cortar una parte de su propio oído?",
                 "¿Cuál es el río más largo del mundo?",
                 "¿Qué famoso autor escribió 'Romeo y Julieta'?",
                 "¿En qué continente se encuentra el Desierto del Sahara?",
                 "¿Cuál es el elemento químico más abundante en la corteza terrestre?",
                 "¿Qué año marcó el inicio de la Primera Guerra Mundial?",
                 "¿Cuál es la montaña más alta de América del Norte?",
                 "¿Qué famosa científica polaca ganó dos premios Nobel en diferentes campos?",
                 "¿En qué año se firmó la Declaración de Independencia de Estados Unidos?",
                 "¿Cuál es la moneda oficial de Japón?",
                 "¿Qué planetas conforman los planetas interiores del sistema solar?",
                 "¿Qué famoso líder luchó por los derechos civiles de los afroamericanos en Estados Unidos?",
                 "¿Cuál es la obra literaria más famosa de Miguel de Cervantes?",
                 "¿Cuál es el océano más grande de la Tierra?",
                 "¿Quién pintó la 'Mona Lisa'?",
                 "¿Cuál es la moneda oficial de China?",
                 "¿Cuál es el proceso por el cual las plantas convierten la luz solar en energía?",
                 "¿Cuál es la montaña más alta de África?",
                 "¿En qué año llegó Cristóbal Colón a América?",
                 "¿Qué famoso líder pacifista indio luchó por la independencia de su país del dominio británico?",
                 "¿Cuál es el país más grande del mundo por territorio?",
                 "¿Qué famosa científica descubrió la radioactividad?",
                 "¿En qué continente se encuentra el país de Egipto?",
                 "¿Cuál es el proceso de cambio de estado de la materia de sólido a líquido?",
                 "¿Quién escribió '1984'?",
                 "¿Qué famoso discurso comenzaba con las palabras 'Tengo un sueño'?",
                 "¿Cuál es la moneda oficial de México?",
                 "¿Qué famoso pintor impresionista pintó 'Los nenúfares'?",
                 "¿Cuál es el río más largo de América del Sur?",
                 "¿Qué famoso científico formuló la teoría de la relatividad?",
                 "¿En qué ciudad se encuentra la famosa ópera 'La Scala'?",
                 "¿Cuál es el metal más ligero y abundante en la Tierra?",
                 "¿Quién escribió 'Don Quijote de la Mancha'?",
                 "¿Qué imperio fue gobernado por Julio César?",
                 "¿En qué año llegó el hombre a la luna por primera vez?",
                 "¿Cuál es el océano más pequeño del mundo?",
                 "¿Qué famoso físico formuló las leyes del movimiento y la gravedad?",
                 "¿Cuál es el proceso de conversión de gas a líquido llamado en meteorología?"]
respuestas = [
    "c",  # Respuesta 1
    "b",  # Respuesta 2
    "b",  # Respuesta 3
    "b",  # Respuesta 4
    "a",  # Respuesta 5
    "b",  # Respuesta 6
    "b",  # Respuesta 7
    "b",  # Respuesta 8
    "a",  # Respuesta 9
    "b",  # Respuesta 10
    "a",  # Respuesta 11
    "b",  # Respuesta 12
    "b",  # Respuesta 13
    "c",  # Respuesta 14
    "b",  # Respuesta 15
    "b",  # Respuesta 16
    "b",  # Respuesta 17
    "a",  # Respuesta 18
    "a",  # Respuesta 19
    "a",  # Respuesta 20
    "a",  # Respuesta 21
    "b",  # Respuesta 22
    "b",  # Respuesta 23
    "b",  # Respuesta 24
    "a",  # Respuesta 25
    "b",  # Respuesta 26
    "b",  # Respuesta 27
    "c",  # Respuesta 28
    "a",  # Respuesta 29
    "b",  # Respuesta 30
    "a",  # Respuesta 31
    "b",  # Respuesta 32
    "b",  # Respuesta 33
    "b",  # Respuesta 34
    "a",  # Respuesta 35
    "a",  # Respuesta 36
    "a",  # Respuesta 37
    "c",  # Respuesta 38
    "b",  # Respuesta 39
    "a",  # Respuesta 40
]

opciones = [
    ["a) Melbourne", "b) Sídney", "c) Canberra (Correcta)"],
    ["a) 1650", "b) 1750 (Correcta)", "c) 1850"],
    ["a) Leonardo da Vinci", "b) Vincent van Gogh (Correcta)", "c) Pablo Picasso"],
    ["a) Río Amazonas", "b) Río Nilo (Correcta)", "c) Río Yangtsé"],
    ["a) William Shakespeare (Correcta)", "b) Charles Dickens", "c) Jane Austen"],
    ["a) Asia", "b) África (Correcta)", "c) América"],
    ["a) Hierro", "b) Silicio (Correcta)", "c) Oxígeno"],
    ["a) 1905", "b) 1914 (Correcta)", "c) 1920"],
    ["a) Montaña McKinley (Correcta)", "b) Montaña Everest", "c) Montaña Kilimanjaro"],
    ["a) Rosalind Franklin", "b) Marie Curie (Correcta)", "c) Ada Lovelace"],
    ["a) 1776 (Correcta)", "b) 1789", "c) 1804"],
    ["a) Dólar japonés", "b) Yen japonés (Correcta)", "c) Yuan japonés"],
    ["a) Marte, Júpiter, Saturno, Urano, Neptuno", "b) Mercurio, Venus, Tierra, Marte (Correcta)", "c) Júpiter, Saturno, Urano, Neptuno"],
    ["a) Abraham Lincoln", "b) Malcolm X", "c) Martin Luther King Jr. (Correcta)"],
    ["a) 'La Divina Comedia'", "b) 'El Quijote' (Correcta)", "c) 'Cien años de soledad'"],
    ["a) Océano Atlántico", "b) Océano Pacífico (Correcta)", "c) Océano Índico"],
    ["a) Vincent van Gogh", "b) Leonardo da Vinci (Correcta)", "c) Pablo Picasso"],
    ["a) Yuan (Correcta)", "b) Yen", "c) Won"],
    ["a) Fotosíntesis (Correcta)", "b) Respiración", "c) Fermentación"],
    ["a) Kilimanjaro (Correcta)", "b) Mont Blanc", "c) Aconcagua"],
    ["a) 1492 (Correcta)", "b) 1500", "c) 1532"],
    ["a) Jawaharlal Nehru", "b) Mohandas Gandhi (Correcta)", "c) Indira Gandhi"],
    ["a) China", "b) Rusia (Correcta)", "c) Estados Unidos"],
    ["a) Rosalind Franklin", "b) Marie Curie (Correcta)", "c) Ada Lovelace"],
    ["a) África (Correcta)", "b) Asia", "c) Europa"],
    ["a) Condensación", "b) Fusión (Correcta)", "c) Sublimación"],
    ["a) Aldous Huxley", "b) George Orwell (Correcta)", "c) Ray Bradbury"],
    ["a) Discurso de Gettysburg", "b) Discurso de la Luna", "c) Discurso de Martin Luther King Jr. (Correcta)"],
    ["a) Peso mexicano (Correcta)", "b) Dólar mexicano", "c) Euro"],
    ["a) Pierre-Auguste Renoir", "b) Claude Monet (Correcta)", "c) Edgar Degas"],
    ["a) Río Amazonas (Correcta)", "b) Río Paraná", "c) Río Orinoco"],
    ["a) Galileo Galilei", "b) Albert Einstein (Correcta)", "c) Niels Bohr"],
    ["a) París", "b) Milán (Correcta)", "c) Viena"],
    ["a) Hierro", "b) Aluminio (Correcta)", "c) Oro"],
    ["a) Miguel de Cervantes (Correcta)", "b) Gabriel García Márquez", "c) Jorge Luis Borges"],
    ["a) Imperio Romano (Correcta)", "b) Imperio Persa", "c) Imperio Mongol"],
    ["a) 1969 (Correcta)", "b) 1972", "c) 1981"],
    ["a) Océano Pacífico", "b) Océano Índico", "c) Océano Ártico (Correcta)"],
    ["a) Galileo Galilei", "b) Isaac Newton (Correcta)", "c) Albert Einstein"],
    ["a) Condensación (Correcta)", "b) Evaporación", "c) Sublimación"]]


def random_preguntas(preguntas, respuestas, opciones, castigos) -> str:
    numero_aleatorio = random.randint(0, len(preguntas)-1)
    pregunta_seleccionada = preguntas.pop(numero_aleatorio)
    respuesta_correcta = respuestas.pop(numero_aleatorio)
    opciones = opciones.pop(numero_aleatorio)
    castigo = castigos.pop(numero_aleatorio)
    return pregunta_seleccionada, respuesta_correcta, opciones, castigo

def creacion_tablero(tablero):
    for i in range(1, 21):
        tablero.append(0)

def lanzar_dado():
    return random.randint(1, 6)


def aplicar_castigo(jugador, castigo):
    if castigo == 1 and jugador[0] >= 3:
        jugador[0] -= 3
    elif castigo == 2 and jugador[0] >= 2:
        jugador[0] -= 2
    elif castigo == 3:
        jugador[0] = 0


def imprimir_tablero(tablero):
    print(tablero[:5])
    print(tablero[-11:-16:-1])
    print(tablero[10:15])
    print(tablero[-1:-6:-1])


def clear_tablero(tablero):
    for i in range(0, len(tablero)):
        tablero[i] = 0


tablero = []
player = 1
posicion_p1 = [0]
posicion_p2 = [0]
aciertos = [0,0]
dado = 0
x = "-"
castigos = ['Puente', 'Resbalón', 'Calavera']
castigos_aleatorios = []
ganador = 0
for i in range(0, 40):
    castigos_aleatorios.append(random.randint(1,3))
creacion_tablero(tablero)

print("AMBOS JUGADORES COMIENZAN DESDE LA POSICION 0...")
while True:
    jugada = input("Presionar enter para lanzar el dado...")
    if jugada == "":
        print(x*50,"\nTURNO DE JUGADOR: ", player,"\n")
        print("EL JUGADOR", player,"TIENE",  aciertos[player-1], "ACIERTOS")

        if(player == 1):
            dado = lanzar_dado()

            print("\nDADO: ", dado, "\n", x*50)
            tablero[posicion_p1[0]] = player
            pregunta_seleccionada, respuesta_correcta, opciones_de_respuesta, castigo_selec = random_preguntas(preguntas, respuestas, opciones, castigos_aleatorios)

            print("\nPREGUNTA: ", pregunta_seleccionada, "\n")
            for i in range(0, 3):
                print(opciones_de_respuesta[i])
            print("CASTIGO: ", castigos[castigo_selec-1], "\n")
            respuesta_jugador = str(input(":"))
            if(respuesta_jugador == respuesta_correcta):
                print("ACTUALIZANDO POSICION...")
                posicion_p1[0] = posicion_p1[0] + dado
                clear_tablero(tablero)
                if (posicion_p1[0] <= 19):
                    tablero[posicion_p1[0]] = player
                else:
                    posicion_p1[0] = 19
                tablero[posicion_p2[0]] = 2
                if(posicion_p1[0] == posicion_p2[0]):
                    print("AMBOS JUGADORES SE ENCUENTRAN EN LA MISMA POSICIÓN!")
                imprimir_tablero(tablero)
                aciertos[0] += 1
                if(posicion_p1[0] >= 19):
                    print(x*50,"\nSE ACABÓ EL JUEGO\n",x*50)
                    posicion_p1[0] = 19
                    clear_tablero(tablero)
                    tablero[posicion_p2[0]] = 2
                    tablero[posicion_p1[0]] = player
                    imprimir_tablero(tablero)

                    ganador = player
                    break

            else:
                print("APLICANDO CASTIGO...")
                aplicar_castigo(posicion_p1, castigo_selec)
                clear_tablero(tablero)
                tablero[posicion_p2[0]] = 2
                tablero[posicion_p1[0]] = player
                imprimir_tablero(tablero)


        else:
            dado = lanzar_dado()
            imprimir_tablero(tablero)

            print(x * 50, "\nDADO: ", dado, "\n", x * 50)
            tablero[posicion_p2[0]] = player
            pregunta_seleccionada, respuesta_correcta, opciones_de_respuesta, castigo_selec = random_preguntas(
                preguntas, respuestas, opciones, castigos_aleatorios)

            print("\nPREGUNTA: ", pregunta_seleccionada, "\n")
            for i in range(0, 3):
                print(opciones_de_respuesta[i])
            print("CASTIGO: ", castigos[castigo_selec - 1], "\n")
            respuesta_jugador = str(input(":"))
            if (respuesta_jugador == respuesta_correcta):
                print("ACTUALIZANDO POSICION...")
                posicion_p2[0] = posicion_p2[0] + dado
                clear_tablero(tablero)
                if(posicion_p2[0] <= 19):
                    tablero[posicion_p2[0]] = player
                else:
                    posicion_p2[0] = 19
                tablero[posicion_p1[0]] = 1
                if (posicion_p1[0] == posicion_p2[0]):
                    print("AMBOS JUGADORES SE ENCUENTRAN EN LA MISMA POSICIÓN!")
                imprimir_tablero(tablero)
                aciertos[1] += 1
                if (posicion_p2[0] == 19):
                    print(x * 50, "\nSE ACABÓ EL JUEGO\n", x * 50)
                    clear_tablero(tablero)
                    tablero[posicion_p1[0]] = 1
                    tablero[posicion_p2[0]] = player
                    imprimir_tablero(tablero)

                    ganador = player

                    break

            else:
                print("APLICANDO CASTIGO...")
                aplicar_castigo(posicion_p2, castigo_selec)
                clear_tablero(tablero)
                tablero[posicion_p1[0]] = 1
                tablero[posicion_p2[0]] = player
                imprimir_tablero(tablero)

    if(player == 1):
        player = 2
    else:
        player = 1

print("ACIERTOS DE JUGADOR 1: ", aciertos[0], "\nACIERTOS DE JUGADOR 2: ", aciertos[1])


