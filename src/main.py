from tkinter import *
from random import choice
from threading import Timer
from random import randint
import json

from classes.Shapes import *
from settings import *


# Загрузка рекордов
record_dict = {1: 1, 2: 2}
with open(RECORD_FILE, "r") as file_object:
    record_dict = json.load(file_object)
records = list(record_dict.items())

player_name = input("What is your name?")
if player_name == "":
    ananimouses = 0
    for key in record_dict:
        if "Ananimouse" in key:
            ananimouses += 1
    player_name = "Ananimouse" + str(ananimouses + 1)

def fitness(item):
    return item[1]



window = Tk()
window.title("Tetris")

c = Canvas(window, width=C_WIDTH, height=C_HEIGHT)
c.pack()

background = c.create_rectangle(0, 0, C_WIDTH, C_HEIGHT, fill="lightblue")

score = 0
game_over = False
field = []
field_ids = []

for str in range(HEIGHT_IN_BLOCKS):
    field_ids.append([])
    field.append([])
    y = TILE_SIZE * str
    for clmn in range(WIDTH_IN_BLOCKS):
        x = TILE_SIZE * clmn
        padding = 3
        field_ids[str].append(
            c.create_rectangle(x, y, x + TILE_SIZE - padding, y + TILE_SIZE - padding, fill="lightblue"))
        field[str].append(0)

c.create_text(30, 10, text="SCORE:", fill="white")

score_text = c.create_text(61, 10, fill="white")
def show_score():
    c.itemconfig(score_text, text=score)


def generateTile():
    newT = randint(1, 5)
    if newT == 1:
        return Sq(c, TILE_SIZE)
    elif newT == 2:
        return Prg(c, TILE_SIZE)
    elif newT == 3:
        return Ln(c, TILE_SIZE)
    elif newT == 4:
        return Ltr(c, TILE_SIZE)
    elif newT == 5:
        return Tbl(c, TILE_SIZE)


run_listener = False


def eventListener(event):
    global run_listener

    if game_over:
        return

    if run_listener:
        return
    run_listener = True

    if event.keysym == "Right" or event.keysym == "Left":
        tile.move(event, field)
    elif event.keysym == "Up":
        tile.rotate(field)
    elif event.keysym == "Down":
        tick(True)

    updateField()
    redraw()

    run_listener = False


def redraw():
    for i_y in range(len(field)):
        for i_x in range(len(field[i_y])):
            num = field[i_y][i_x]
            colour = COLOURS[num]
            stroke_colour = STROKE_COLOURS[num]
            c.itemconfig(field_ids[i_y][i_x], fill=colour, outline=stroke_colour)
    show_score()


def updateField():
    global field

    for i_y in range(len(field)):
        for i_x in range(len(field[i_y])):
            if field[i_y][i_x] == 2:
                field[i_y][i_x] = 0

    for block in tile.body:
        field[block.y][block.x] = 2


def update_record_dict(rec_list):
    record_dict = {}

    for record in rec_list:
        record_dict[record[0]] = record[1]

    return record_dict


def checkBuiltLine():
    for i_y in range(len(field)):
        blocks = 0
        for num in field[i_y]:
            if num == 1:
                blocks += 1
        if blocks == WIDTH_IN_BLOCKS:
            return i_y
    return -1


def tick(artificial = False):
    global tile
    global score
    global game_over
    global records
    global record_dict

    if tile.collision(field):
        for coord in tile.body:
            field[coord.y][coord.x] = 1
        tile = generateTile()
        for block in tile.body:
            if field[block.y][block.x] == 1:
                game_over = True
                c.create_text(C_WIDTH/2, C_HEIGHT/2, text="GAME OVER", fill="red", font=("Helvetica", 30))

                c.create_text(C_WIDTH/2, C_HEIGHT/2 + 40, text="BEST SCORES:", fill="green", font=("Helvetica", 15))

                records.append((player_name, score))
                records = sorted(records, key=fitness, reverse=True)[0:3]

                i = 0
                for record in records:
                    c.create_text(C_WIDTH/2, C_HEIGHT/2 + 60 + 20*i, text=f"{record[0]}: {record[1]}", fill="green", font=("Helvetica", 14))
                    i += 1
                del i

                record_dict = update_record_dict(records)
                    

                with open(RECORD_FILE, "w") as file_object:
                    json.dump(record_dict, file_object)
                
                return
        updateField()
    builtLine = checkBuiltLine()
    if builtLine != -1:
        del field[builtLine]
        field.insert(0, [])
        for n in range(WIDTH_IN_BLOCKS):
            field[0].append(0)
        score += WIDTH_IN_BLOCKS

    tile.fall()
    updateField()
    redraw()
    
    if not artificial:
        t = Timer(0.5, tick)
        t.start()


window.bind_all("<Key>", eventListener)
tile = generateTile()
tick()
window.mainloop()
