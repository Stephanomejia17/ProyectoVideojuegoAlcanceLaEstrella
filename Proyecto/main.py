import random


def random_preguntas() -> str:
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

    numero_aleatorio = random.randint(0, 39)
    pregunta_seleccionada = preguntas.pop(numero_aleatorio)
    print(numero_aleatorio)
    return pregunta_seleccionada


def creacion_de_tablero(tablero):
    for i in range(0, 4):
        tablero.append([])
        for j in range(0, 5):
            tablero[i].append(0)
    return tablero


def lanzar_dado() -> int:
    alea = random.randint(1, 6)
    return alea


tablero = []
creacion_de_tablero(tablero)
x = "-"
print("a) Ingrese 1 para comenzar el juego\n", "b) Ingrese 5 para salir del juego\n")
eleccion = int(input())
player = 1

if eleccion == 1:
    pos_p1 = [0, 0]
    pos_p2 = [0, 0]
    while True:
        if player == 1:
            player = 2
        elif player == 2:
            player = 1
        print("Jugador ", player, " presione 0 para lanzar el dado")
        avance = int(input())

        if avance == 0:
            dado = lanzar_dado()
            print("DADO: ", dado)
            aux = dado

            for i in range(0, 4):
                if (i + 1) % 2 == 0:
                    if(player == 1):
                        for j in range(-1, -6, -1):
                            dado -= 1
                            if dado == 0:
                                tablero[i][j] = player
                                pos_p1[1] = j + pos_p1[1]
                                pos_p1[0] = j + pos_p1[0]
                                break
                    else:
                        for j in range(-1, -6, -1):
                            dado -= 1
                            if dado == 0:
                                tablero[i][j] = player
                                pos_p2[1] = j + 5
                                pos_p2[0] = j + 5
                                break

                else:
                    if(player == 1):
                        for j in range(pos_p1[1], 5):
                            dado -= 1
                            if dado == 0:
                                tablero[i][j] = player
                                pos_p1[1] = j + pos_p1[1]
                                pos_p1[0] = j + pos_p1[0]
                                break
                    else:
                        for j in range(pos_p2[1], 5):
                            dado -= 1
                            if dado == 0:
                                tablero[i][j] = player
                                pos_p2[1] = j + pos_p2[1]
                                pos_p2[0] = j + pos_p2[0]
                                break

                if dado == 0:
                    break

        print(pos_p1, pos_p2)
        print(tablero[0])
        print(tablero[1])
        print(tablero[2])
        print(tablero[3])




