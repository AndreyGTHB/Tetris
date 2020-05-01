from tkinter import *
from threading import Timer
from random import randint
import time
import json
import yadisk

from GameState import GameState
from classes.Bomb import *
from classes.Shapes import *
from settings import *

game_state = GameState()


# Загрузка рекордов
def download_records():
    records = json.load(open('records.json', 'r'))
    try:
        game_state.drive.download("/records.json", "records.json")
    except:
        with open('records.json', 'w') as file:
            json.dump(records, file)
        print('Can not download records')


def push_records():
    try:
        game_state.drive.remove("/records.json", permanently=True)
        game_state.drive.upload("records.json", "/records.json")
    except:
        print('Can not push records')


def pause():  # Add argument (pause/unpause)
    global game_state

    if game_state.paused:
        game_state.c.itemconfig(game_state.pause_bg, state=HIDDEN)
        game_state.c.itemconfig(game_state.pause_text, state=HIDDEN)
        game_state.paused = False
    else:
        game_state.pause_bg = game_state.c.create_rectangle(0, 0, C_WIDTH, C_HEIGHT, fill="lightblue")
        game_state.pause_text = game_state.c.create_text(C_WIDTH / 2, C_HEIGHT / 2, text="PAUSED",
                                                         font=("Helvetica", 30), fill="green")
        game_state.paused = True


def show_score():
    game_state.c.itemconfig(game_state.score_text, text=game_state.score)


def generateTile():
    newT = randint(1, 5)
    if newT == 1:
        return Sq(game_state.c, TILE_SIZE)
    elif newT == 2:
        return Prg(game_state.c, TILE_SIZE)
    elif newT == 3:
        return Ln(game_state.c, TILE_SIZE)
    elif newT == 4:
        return Ltr(game_state.c, TILE_SIZE)
    return Tbl(game_state.c, TILE_SIZE)


def generate_bomb():
    bomb_x = randint(2, WIDTH_IN_BLOCKS - 1)
    bomb_y = randint(2, HEIGHT_IN_BLOCKS - 1)

    block = game_state.field[bomb_y][bomb_x]
    while block == 1 or block == 2 or block == 3:
        bomb_x = randint(2, WIDTH_IN_BLOCKS - 1)
        bomb_y = randint(2, HEIGHT_IN_BLOCKS - 1)
        block = game_state.field[bomb_y][bomb_x]

    bomb_r = randint(3, 7)
    return Bomb(bomb_x, bomb_y, bomb_r)


def check_bomb_collision():
    new_bombs = game_state.bombs
    new_field = game_state.field
    new_score = game_state.score

    i_bomb = 0
    for bomb in game_state.bombs:
        if bomb.collision(game_state.field):
            new_field, new_score = bomb.explosion(game_state.field, game_state.score)
            del new_bombs[i_bomb]
            i_bomb -= 1
        i_bomb += 1
    return new_field, new_bombs, new_score


def eventListener(event):
    global game_state

    if game_state.game_over:
        return

    key = event.keysym

    if key == "q":
        pause()
    elif game_state.paused:
        return

    if key == "Right" or key == "Left":
        game_state.tile.move(event, game_state.field)
    elif key == "Up":
        game_state.tile.rotate(game_state.field)
    elif key == "Down":
        tick(True)
    elif key == "space":
        while not game_state.tile.collision(game_state.field):
            tick(True)

    updateField()
    game_state.field, game_state.bombs, game_state.score = check_bomb_collision()
    redraw()


def redraw():
    for i_y in range(len(game_state.field)):
        for i_x in range(len(game_state.field[i_y])):
            num = game_state.field[i_y][i_x]
            fill_colour = COLOURS[num]
            stroke_colour = STROKE_COLOURS[num]
            game_state.c.itemconfig(game_state.field_ids[i_y][i_x], fill=fill_colour, outline=stroke_colour)
    show_score()


def updateField():
    global game_state
    for i_y in range(len(game_state.field)):
        for i_x in range(len(game_state.field[i_y])):
            if game_state.field[i_y][i_x] == 2 or game_state.field[i_y][i_x] == 3:
                game_state.field[i_y][i_x] = 0

    for bomb in game_state.bombs:
        game_state.field[bomb.get_body().y][bomb.get_body().x] = 3

    for block in game_state.tile.body:
        game_state.field[block.y][block.x] = 2


def update_record_dict(rec_list):
    rec_dict = {}
    names = []

    for record in rec_list:
        rec_dict[record[0]] = record[1]
        names.append(record[0])

    return rec_dict


def checkBuiltLine():
    for i_y in range(len(game_state.field)):
        blocks = 0
        for num in game_state.field[i_y]:
            if num == 1:
                blocks += 1
        if blocks == WIDTH_IN_BLOCKS:
            return i_y
    return -1


def tick(artificial=False):
    global game_state

    if game_state.paused:
        t = Timer(0.5, tick)
        t.start()
        return
    if game_state.game_over:
        return

    left_time = int(time.time()) - game_state.start_time

    if (left_time // 5 - left_time / 5 == 0 or left_time // 5 - left_time / 5 == 0.0) and not artificial and len(
            game_state.bombs) == 0 and randint(0, 6) == 0:
        game_state.bombs.append(generate_bomb())

    if game_state.tile.collision(game_state.field):
        for coord in game_state.tile.body:
            game_state.field[coord.y][coord.x] = 1
        game_state.tile = generateTile()
        for block in game_state.tile.body:
            if game_state.field[block.y][block.x] == 1:
                game_state.game_over = True
                game_state.c.create_text(C_WIDTH / 2, C_HEIGHT / 2, text="GAME OVER", fill="red",
                                         font=("Helvetica", 30))

                game_state.c.create_text(C_WIDTH / 2, C_HEIGHT / 2 + 40, text="BEST SCORES:", fill="green",
                                         font=("Helvetica", 15))

                game_state.records.append((game_state.player_name, game_state.score))
                game_state.records = sorted(game_state.records, key=lambda i: i[1], reverse=True)[0:3]

                i = 0
                names = []
                for record in game_state.records:
                    if not record[0] in names:
                        game_state.c.create_text(C_WIDTH / 2, C_HEIGHT / 2 + 60 + 20 * i,
                                                 text=f"{record[0]}: {record[1]}",
                                                 fill="green", font=("Helvetica", 14))
                        names.append(record[0])
                    else:
                        i -= 1
                    i += 1
                del i
                del names

                game_state.record_dict = update_record_dict(game_state.records)

                with open(RECORD_FILE, "w") as file_obj:
                    json.dump(game_state.record_dict, file_obj)
                push_records()

                return
        updateField()
    builtLine = checkBuiltLine()
    if builtLine != -1:
        del game_state.field[builtLine]
        game_state.field.insert(0, [])
        for n in range(WIDTH_IN_BLOCKS):
            game_state.field[0].append(0)
        game_state.score += WIDTH_IN_BLOCKS

    game_state.tile.fall()
    updateField()

    game_state.field, game_state.bombs, game_state.score = check_bomb_collision()

    redraw()

    if not artificial:
        t = Timer(0.5, tick)
        t.start()


def main(*args):
    global game_state

    try:
        game_state.drive = yadisk.YaDisk(YD_ID, YD_SECRET, YD_TOKEN)
    except:
        print('No connection')
    download_records()

    with open(RECORD_FILE, "r") as file_object:
        game_state.record_dict = json.load(file_object)
    game_state.records = list(game_state.record_dict.items())

    game_state.player_name = input("What is your name?")
    if game_state.player_name == "":
        ananymouses = 0
        for key in game_state.record_dict:
            if "Anonymous" in key:
                ananymouses += 1
        player_name = "Anonymous" + str(ananymouses + 1)

    window = Tk()
    window.title("Tetris")

    game_state.c = Canvas(window, width=C_WIDTH, height=C_HEIGHT)
    game_state.c.pack()

    game_state.c.create_rectangle(0, 0, C_WIDTH, C_HEIGHT, fill="lightblue") # Background

    for str in range(HEIGHT_IN_BLOCKS):
        game_state.field_ids.append([])
        game_state.field.append([])
        y = TILE_SIZE * str
        for clmn in range(WIDTH_IN_BLOCKS):
            x = TILE_SIZE * clmn
            padding = 3
            colour = COLOURS[0]
            game_state.field_ids[str].append(
                game_state.c.create_rectangle(x, y, x + TILE_SIZE - padding, y + TILE_SIZE - padding, fill=colour,
                                              outline=STROKE_COLOURS[0]))
            game_state.field[str].append(0)

    game_state.c.create_text(30, 10, text="SCORE:", fill="white")

    game_state.score_text = game_state.c.create_text(61, 10, fill="white")

    window.bind_all("<Key>", eventListener)
    game_state.tile = generateTile()

    game_state.start_time = int(time.time())
    tick()

    window.mainloop()
    game_state.game_over = True


main()
