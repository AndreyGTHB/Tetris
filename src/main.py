from tkinter import *
from random import choice
from threading import Timer

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


def eventListener(event):
    global tile

    if event.keysym == "Right" or event.keysym == "Left":
        tile.move(event, field)
    elif event.keysym == "Up":
        tile.rotate()

    redraw()


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
        tile = Prg(c, tile_size)
        redraw(field=True)

    tile.fall()
    redraw()

    t = Timer(0.4, tick)
    t.start()

tick()
window.mainloop()
