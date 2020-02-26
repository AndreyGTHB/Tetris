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
blocks = []
field_ids = []
colours = ["lightblue", "orange", "lightgreen"]
stroke_colours = ["lightblue", "black", "black"]

for str in range(12):
    field_ids.append([])
    y = tile_size * str
    for clmn in range(10):
        x = tile_size * clmn
        padding = 3
        field_ids[str].append(
            c.create_rectangle(x, y, x + tile_size - padding, y + tile_size - padding, fill="lightblue"))


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

    updateField()
    redraw()

    run_listener = False


def redraw():
    for i_y in range(len(field)):
        for i_x in range(len(field[i_y])):
            num = field[i_y][i_x]
            colour = colours[num]
            stroke_colour = stroke_colours[num]
            c.itemconfig(field_ids[i_y][i_x], fill=colour, outline=stroke_colour)


def updateField():
    global field

    for i_y in range(len(field)):
        for i_x in range(len(field[i_y])):
            field[i_y][i_x] = 0

    for block in tile.body:
        field[block.y][block.x] = 2

    for block in blocks:
        field[block.y][block.x] = 1


def tick():
    global tile

    if tile.collision(field):
        for coord in tile.body:
            blocks.append(coord)
        tile.clear()
        tile = generateTile()
        updateField()

    tile.fall()
    updateField()
    redraw()

    t = Timer(0.5, tick)
    t.start()


window.bind_all("<Key>", eventListener)
tile = generateTile()
tick()
window.mainloop()
