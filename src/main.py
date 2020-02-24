from tkinter import *
from random import choice
from threading import Timer
from random import randint

from classes.Shapes import *

window = Tk()
window.title("Tetris")

WIDTH = 500
HEIGHT = 600
c = Canvas(window, width=WIDTH, height=HEIGHT)
c.pack()

background = c.create_rectangle(0, 0, WIDTH, HEIGHT, fill="lightblue")

tile_size = 50

field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

field_ids = []

shapes = ['sq', 'ltr', 'ln', 'prg']
tile = Prg(c, tile_size)

def generateTile():

    newT = randint(1, 4)
    if newT == 1:
        return Sq(c, tile_size)
    elif newT == 2:
        return Prg(c, tile_size)
    elif newT == 3:
        return Ln(c, tile_size)
    elif newT == 4:
        return Ltr(c, tile_size)


run_listener = False

def eventListener(event):
    global tile
    global run_listener

    if run_listener:
        return
    run_listener = True

    if event.keysym == "Right" or event.keysym == "Left":
        tile.move(event, field)
    elif event.keysym == "Up":
        tile.rotate(field)

    redraw()

    run_listener = False


def redrawField():
    global field_ids

    for id in field_ids:
        c.delete(id)

    for i_y in range(len(field)):
        y = field[i_y]
        for x in range(len(y)):
            if field[i_y][x] == 1:
                field_ids.append(c.create_rectangle(tile_size * x, tile_size * i_y, tile_size * (x + 1), tile_size * (i_y + 1), \
                                   fill="orange"))

def redraw(field=False):
    if field:
        redrawField()
    tile.clear()
    tile.draw("lightgreen")


window.bind_all("<Key>", eventListener)

def tick():
    global tile

    if tile.collision(field):
        for coord in tile.body:
            field[coord.y][coord.x] = 1
        tile.clear()
        tile = generateTile()
        redraw(field=True)

    tile.fall()
    redraw()

    t = Timer(0.5, tick)
    t.start()

tile = generateTile()
tick()
window.mainloop()
