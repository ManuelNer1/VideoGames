"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line

import numpy as np


def grid():

    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

    # Lo que se edito aqupi fue ajustar la posicion de las x y
    # y porque la funcion utiliza los dos puntos de referencia
    # para poder dibujar la linea, ademas que con la funcion
    # pencolor se cambio el color de la figura


def drawx(x, y):
    """Draw X player."""

    pencolor('blue')
    line(x, y, x+40, y+40)
    line(x, y+40, x+40, y)

    # Parecido a la función pasada lo que tambien se edito fue
    # que la coordenada x y el tamaño del circulo
    # ademas que tambien la funcion pencolor se cambio el color


def drawo(x, y):
    """Draw O player."""
    up()

    goto(x + 15, y)
    down()
    pencolor('red')
    circle(15)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 44) * 44 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    global c
    global quadx
    global quady

    x = int(floor(x))
    y = int(floor(y))

    # Aqui es donde realiza la comparacion de las posiciones, si
    # ya existe te envia un mensaje de dato invalido
    # y no te deja poner una figura. En caso de que sea correcto,
    # te permite poner la figura y las coordenadas
    # se guardan en la matriz

    if x in quadx and y in quady:
        print("Dato Invalido")
        return False
    elif c < 9:
        quadx[0][c] = x
        quady[0][c] = y

    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player

# Se implemento un contador que se usara más adelante en el código
# para insertar los datos en las matrices
# Y las matrices se crearon con el fin de guardar las
# posiciones de las figuras ya presionadas


c = 0


quadx = np.zeros(shape=(1, 9))
quady = np.zeros(shape=(1, 9))
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
# This is a new line that ends the file