from tkinter import *
from time import sleep
from random import choice

from classes.Tile import Tile

window = Tk()
window.title("Tetris")

WIDTH = 550
HEIGHT = 600
c = Canvas(window, width=WIDTH, height=HEIGHT)
c.pack()

background = c.create_rectangle(0, 0, WIDTH, HEIGHT, fill="lightblue")

window.update()

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
        tile.move(event)

    window.update()


def drawField():
    for y in range(len(field)):
        for x in range(len(y)):
            if field[y][x] == 1:
                c.create_rectangle(tile_size * x, tile_size * y, tile_size * (x + 1), tile_size * (y + 1), \
                                   fill="orange")
    window.update()


window.bind_all("<Key>", eventListener)

while True:
    tile.fall()
    if tile.collision(field):
        for coord in tile.body:
            field[coord.y][coord.x] = 1
        tile.clear()
        drawField()
        tile = Tile(c, choice(shapes), tile_size)

    window.update()
    sleep(1)
