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


def drawx(x, y):
    """Draw X player."""
    # print("Valor de x: " + str(x))
    # print("Valor de y: " + str(y))

    pencolor('blue')
    line(x, y , x+40 , y+40)
    line(x, y+40 , x+40 , y)


def drawo(x, y):
    """Draw O player."""
    up()

    goto(x+15,y)
    down()
    # print("Valor de x: " + str(x))
    # print("Valor de y: " + str(y))
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
    i= 0
    v = 0



    x = int(floor(x))
    y = int(floor(y))
    # print("Valor de x: " + str(x))
    # print("Valor de y: " + str(y))

    if x in quadx and y in quady:
        print("Dato Invalido")
        return False
    elif c<9:
        quadx[0][c]=x
        quady[0][c]=y
      


    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player
c= 0
quadx=np.zeros (shape = (1,9))
quady=np.zeros (shape = (1,9))
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()