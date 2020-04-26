from tkinter import *
from threading import Timer
from random import randint
import time
import json
import yadisk


from classes.Bomb import *
from classes.Shapes import *
from settings import *


# Загрузка рекордов
def download_records():
    records = json.load(open('records.json', 'r'))
    try:
        drive.download("/records.json", "records.json")
    except:
        with open('records.json', 'w') as file:
            json.dump(records, file)
        print('Can not download records')


def push_records():
    try:
        drive.remove("/records.json", permanently=True)
        drive.upload("records.json", "/records.json")
    except:
        print('Can not push records')


def pause():
    global paused
    global pause_bg
    global pause_text

    if paused:
        c.itemconfig(pause_bg, state=HIDDEN)
        c.itemconfig(pause_text, state=HIDDEN)
        paused = False
    else:
        pause_bg = c.create_rectangle(0, 0, C_WIDTH, C_HEIGHT, fill="lightblue")
        pause_text = c.create_text(C_WIDTH / 2, C_HEIGHT / 2, text="PAUSED", font=("Helvetica", 30), fill="green")
        paused = True


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


def generate_bomb():
    bomb_x = randint(2, WIDTH_IN_BLOCKS - 1)
    bomb_y = randint(2, HEIGHT_IN_BLOCKS - 1)

    block = field[bomb_y][bomb_x]
    while block == 1 or block == 2 or block == 3:
        bomb_x = randint(2, WIDTH_IN_BLOCKS - 1)
        bomb_y = randint(2, HEIGHT_IN_BLOCKS - 1)
        block = field[bomb_y][bomb_x]

    bomb_r = randint(3, 7)
    return Bomb(bomb_x, bomb_y, bomb_r)


def check_bomb_collision():
    new_bombs = bombs
    new_field = field
    new_score = score

    i_bomb = 0
    for bomb in bombs:
        if bomb.collision(field):
            new_field, new_score = bomb.explosion(field, score)
            del new_bombs[i_bomb]
            i_bomb -= 1
        i_bomb += 1
    return new_field, new_bombs, new_score


def eventListener(event):
    global paused
    global bombs
    global field
    global score

    if game_over:
        return
    run_listener = True

    key = event.keysym

    if key == "q":
        pause()
    elif paused:
        return

    if key == "Right" or key == "Left":
        tile.move(event, field)
    elif key == "Up":
        tile.rotate(field)
    elif key == "Down":
        tick(True)
    elif key == "space":
        while not tile.collision(field):
            tick(True)

    updateField()
    field, bombs, score = check_bomb_collision()
    redraw()


def redraw():
    for i_y in range(len(field)):
        for i_x in range(len(field[i_y])):
            num = field[i_y][i_x]
            fill_colour = COLOURS[num]
            stroke_colour = STROKE_COLOURS[num]
            c.itemconfig(field_ids[i_y][i_x], fill=fill_colour, outline=stroke_colour)
    show_score()


def updateField():
    global field

    for i_y in range(len(field)):
        for i_x in range(len(field[i_y])):
            if field[i_y][i_x] == 2 or field[i_y][i_x] == 3:
                field[i_y][i_x] = 0

    for bomb in bombs:
        field[bomb.get_body().y][bomb.get_body().x] = 3

    for block in tile.body:
        field[block.y][block.x] = 2


def update_record_dict(rec_list):
    rec_dict = {}
    names = []

    for record in rec_list:
        rec_dict[record[0]] = record[1]
        names.append(record[0])

    return rec_dict


def checkBuiltLine():
    for i_y in range(len(field)):
        blocks = 0
        for num in field[i_y]:
            if num == 1:
                blocks += 1
        if blocks == WIDTH_IN_BLOCKS:
            return i_y
    return -1


def tick(artificial=False):
    global tile
    global score
    global game_over
    global records
    global record_dict
    global field
    global bombs

    if paused:
        t = Timer(0.5, tick)
        t.start()
        return
    if game_over:
        return

    left_time = int(time.time()) - start_time

    if (left_time // 5 - left_time / 5 == 0 or left_time // 5 - left_time / 5 == 0.0) and not artificial and len(
            bombs) == 0 and randint(0, 4) == 0:
        bombs.append(generate_bomb())

    if tile.collision(field):
        for coord in tile.body:
            field[coord.y][coord.x] = 1
        tile = generateTile()
        for block in tile.body:
            if field[block.y][block.x] == 1:
                game_over = True
                c.create_text(C_WIDTH / 2, C_HEIGHT / 2, text="GAME OVER", fill="red", font=("Helvetica", 30))

                c.create_text(C_WIDTH / 2, C_HEIGHT / 2 + 40, text="BEST SCORES:", fill="green", font=("Helvetica", 15))

                records.append((player_name, score))
                records = sorted(records, key=fitness, reverse=True)[0:3]

                i = 0
                names = []
                for record in records:
                    if not record[0] in names:
                        c.create_text(C_WIDTH / 2, C_HEIGHT / 2 + 60 + 20 * i, text=f"{record[0]}: {record[1]}",
                                      fill="green", font=("Helvetica", 14))
                        names.append(record[0])
                    else:
                        i -= 1
                    i += 1
                del i
                del names

                record_dict = update_record_dict(records)

                with open(RECORD_FILE, "w") as file_obj:
                    json.dump(record_dict, file_obj)
                push_records()

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

    field, bombs, score = check_bomb_collision()

    redraw()

    if not artificial:
        t = Timer(0.5, tick)
        t.start()


drive = None
try:
    drive = yadisk.YaDisk(YD_ID, YD_SECRET, YD_TOKEN)
except:
    print('No connection')
download_records()


record_dict = {1: 1}
with open(RECORD_FILE, "r") as file_object:
    record_dict = json.load(file_object)
records = list(record_dict.items())

player_name = input("What is your name?")
if player_name == "":
    ananymouses = 0
    for key in record_dict:
        if "Anonymous" in key:
            ananymouses += 1
    player_name = "Anonymous" + str(ananymouses + 1)


def fitness(item):
    return item[1]


window = Tk()
window.title("Tetris")

c = Canvas(window, width=C_WIDTH, height=C_HEIGHT)
c.pack()

background = c.create_rectangle(0, 0, C_WIDTH, C_HEIGHT, fill="lightblue")

score = 0

game_over = False

paused = False
pause_bg = None
pause_text = None

field = []
field_ids = []
for str in range(HEIGHT_IN_BLOCKS):
    field_ids.append([])
    field.append([])
    y = TILE_SIZE * str
    for clmn in range(WIDTH_IN_BLOCKS):
        x = TILE_SIZE * clmn
        padding = 3
        colour = COLOURS[0]
        field_ids[str].append(
            c.create_rectangle(x, y, x + TILE_SIZE - padding, y + TILE_SIZE - padding, fill=colour,
                               outline=STROKE_COLOURS[0]))
        field[str].append(0)
bombs = list()

c.create_text(30, 10, text="SCORE:", fill="white")

score_text = c.create_text(61, 10, fill="white")

window.bind_all("<Key>", eventListener)
tile = generateTile()

start_time = int(time.time())
tick()

window.mainloop()
game_over = True
