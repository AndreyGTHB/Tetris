from tkinter import *
from threading import Timer
from random import randint
import time
import json
from classes.Bomb import *
from classes.Shapes import *
from libsForGame import *
from settings import *


class Game:
    player_name = None

    c = None
    score_text = None

    drive = None

    game_over = False
    start_time = None

    score = 0
    record_dict = {"k": "v"}
    records = list()

    paused = False
    pause_bg = None
    pause_text = None

    field = list()
    field_ids = list()
    bombs = list()

    tile = None

    def pause(self, state):
        self.paused = state

        if self.paused:
            self.pause_bg = self.c.create_rectangle(0, 0, C_WIDTH, C_HEIGHT, fill="lightblue")
            self.pause_text = self.c.create_text(C_WIDTH / 2, C_HEIGHT / 2, text="PAUSED",
                                                 font=("Helvetica", 30), fill="green")
        else:
            self.c.itemconfig(self.pause_bg, state=HIDDEN)
            self.c.itemconfig(self.pause_text, state=HIDDEN)

    def show_score(self):
        self.c.itemconfig(self.score_text, text=self.score)

    def generateTile(self):
        newT = randint(1, 5)
        if newT == 1:
            return Sq(TILE_SIZE)
        elif newT == 2:
            return Prg(TILE_SIZE)
        elif newT == 3:
            return Ln(TILE_SIZE)
        elif newT == 4:
            return Ltr(TILE_SIZE)
        return Tbl(TILE_SIZE)

    def generate_bomb(self):
        bomb_x = randint(2, WIDTH_IN_BLOCKS - 1)
        bomb_y = randint(2, HEIGHT_IN_BLOCKS - 1)

        block = self.field[bomb_y][bomb_x]
        while block == 1 or block == 2 or block == 3:
            bomb_x = randint(2, WIDTH_IN_BLOCKS - 1)
            bomb_y = randint(2, HEIGHT_IN_BLOCKS - 1)
            block = self.field[bomb_y][bomb_x]

        bomb_r = randint(3, 7)
        return Bomb(bomb_x, bomb_y, bomb_r)

    def check_bomb_collision(self):
        new_bombs = self.bombs
        new_field = self.field
        new_score = self.score

        i_bomb = 0
        for bomb in self.bombs:
            if bomb.collision(self.field):
                new_field, new_score = bomb.explosion(self.field, self.score)
                del new_bombs[i_bomb]
                i_bomb -= 1
            i_bomb += 1
        return new_field, new_bombs, new_score

    def eventListener(self, event):
        if self.game_over:
            return

        key = event.keysym

        if key == "q":
            self.pause(not self.paused)
        elif self.paused:
            return

        if key == "Right" or key == "Left":
            self.tile.move(event, self.field)
        elif key == "Up":
            self.tile.rotate(self.field)
        elif key == "Down":
            self.tick(True)
        elif key == "space":
            while not self.tile.collision(self.field):
                self.tick(True)

        self.updateField()
        self.field, self.bombs, self.score = self.check_bomb_collision()
        self.redraw()

    def redraw(self):
        for i_y in range(len(self.field)):
            for i_x in range(len(self.field[i_y])):
                num = self.field[i_y][i_x]
                fill_colour = COLOURS[num]
                stroke_colour = STROKE_COLOURS[num]
                self.c.itemconfig(self.field_ids[i_y][i_x], fill=fill_colour, outline=stroke_colour)
        self.show_score()

    def updateField(self):
        for i_y in range(len(self.field)):
            for i_x in range(len(self.field[i_y])):
                if self.field[i_y][i_x] == 2 or self.field[i_y][i_x] == 3:
                    self.field[i_y][i_x] = 0

        for bomb in self.bombs:
            self.field[bomb.get_body().y][bomb.get_body().x] = 3

        for block in self.tile.body:
            self.field[block.y][block.x] = 2

    def update_record_dict(self, rec_list):
        rec_dict = {}
        names = []

        for record in rec_list:
            rec_dict[record[0]] = record[1]
            names.append(record[0])

        return rec_dict

    def checkBuiltLine(self):
        for i_y in range(len(self.field)):
            blocks = 0
            for num in self.field[i_y]:
                if num == 1:
                    blocks += 1
            if blocks == WIDTH_IN_BLOCKS:
                return i_y
        return -1

    def tick(self, artificial=False):
        if self.paused:
            t = Timer(0.5, self.tick)
            t.start()
            return
        if self.game_over:
            return

        left_time = int(time.time()) - self.start_time

        if (left_time // 5 - left_time / 5 == 0 or left_time // 5 - left_time / 5 == 0.0) and not artificial and len(
                self.bombs) == 0 and randint(0, 6) == 0:
            self.bombs.append(self.generate_bomb())

        if self.tile.collision(self.field):
            for coord in self.tile.body:
                self.field[coord.y][coord.x] = 1
            self.tile = self.generateTile()
            for block in self.tile.body:
                if self.field[block.y][block.x] == 1:
                    self.game_over = True
                    self.c.create_text(C_WIDTH / 2, C_HEIGHT / 2, text="GAME OVER", fill="red",
                                       font=("Helvetica", 30))

                    self.c.create_text(C_WIDTH / 2, C_HEIGHT / 2 + 40, text="BEST SCORES:", fill="green",
                                       font=("Helvetica", 15))

                    self.records.append((self.player_name, self.score))
                    self.records = sorted(self.records, key=lambda i: i[1], reverse=True)[0:3]

                    i = 0
                    names = []
                    for record in self.records:
                        if not record[0] in names:
                            self.c.create_text(C_WIDTH / 2, C_HEIGHT / 2 + 60 + 20 * i,
                                               text=f"{record[0]}: {record[1]}",
                                               fill="green", font=("Helvetica", 14))
                            names.append(record[0])
                        else:
                            i -= 1
                        i += 1
                    del i
                    del names

                    self.record_dict = self.update_record_dict(self.records)

                    with open(RECORD_FILE, "w") as file_obj:
                        json.dump(self.record_dict, file_obj)
                    utils.push_records()

                    return
            self.updateField()
        builtLine = self.checkBuiltLine()
        if builtLine != -1:
            del self.field[builtLine]
            self.field.insert(0, [])
            for n in range(WIDTH_IN_BLOCKS):
                self.field[0].append(0)
            self.score += WIDTH_IN_BLOCKS

        self.tile.fall()
        self.updateField()

        self.field, self.bombs, self.score = self.check_bomb_collision()

        self.redraw()

        if not artificial:
            t = Timer(0.5, self.tick)
            t.start()


game = Game()
