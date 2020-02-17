from tkinter import *
from random import choice
from threading import Timer

from classes.Tile import Tile

window = Tk()
window.title("Tetris")

WIDTH = 500
HEIGHT = 600
c = Canvas(window, width=WIDTH, height=HEIGHT)
c.pack()

background = c.create_rectangle(0, 0, WIDTH, HEIGHT, fill="lightblue")

tile_size = 50

field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

shapes = ['sq', 'ltr', 'ln', 'prg']
tile = Tile(c, choice(shapes), tile_size)


def eventListener(event):
    global tile

    if event.keysym == "Right" or event.keysym == "Left":
        tile.move(event, field)


def drawField():
    for i_y in range(len(field)):
        y = field[i_y]
        for x in range(len(y)):
            if field[i_y][x] == 1:
                c.create_rectangle(tile_size * x, tile_size * i_y, tile_size * (x + 1), tile_size * (i_y + 1), \
                                   fill="orange")


window.bind_all("<Key>", eventListener)


def tick():
    global tile

    tile.fall()
    if tile.collision(field):
        for coord in tile.body:
            field[coord.y][coord.x] = 1
        tile.clear()
        drawField()
        tile = Tile(c, choice(shapes), tile_size)

    t = Timer(0.6, tick)
    t.start()


tick()
window.mainloop()
