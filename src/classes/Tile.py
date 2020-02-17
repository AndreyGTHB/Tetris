from tkinter import *
from time import sleep

from classes.Point import *


class Tile:

    def __init__(self, canvas, shape, cell):
        self.canvas = canvas
        self.tile_ids = list()
        self.cellLen = cell
        if shape == "sq":
            self.body = [
                Point(0, -2),
                Point(1, -2),
                Point(0, -1),
                Point(1, -1)
            ]
        elif shape == "prg":
            self.body = [
                Point(0, -1),
                Point(1, -1),
                Point(1, -2),
                Point(2, -2)
            ]
        elif shape == "ln":
            self.body = [
                Point(0, -1),
                Point(1, -1),
                Point(2, -1),
                Point(3, -1)
            ]
        elif shape == "ltr":
            self.body = [
                Point(0, -1),
                Point(1, -1),
                Point(2, -1),
                Point(2, -2)
            ]
        else:
            raise ValueError("'" + shape + "'", "is not a shape")

        self.draw("lightgreen")

    def draw(self, color):
        c = self.canvas
        for p in self.body:
            x = p.x * self.cellLen
            y = p.y * self.cellLen
            padding = 3
            self.tile_ids.append(
                c.create_rectangle(x, y, x + self.cellLen - padding, y + self.cellLen - padding, fill=color))

    def clear(self):
        for tile_id in self.tile_ids:
            self.canvas.delete(tile_id)

        for i in range(len(self.tile_ids)):
            del (self.tile_ids[0])

    def fall(self):
        for i in range(len(self.body)):
            self.body[i].y += 1
            self.canvas.move(self.tile_ids[i], 0, self.cellLen)

    def move(self, event):
        rightWall = False
        leftWall = False
        for coord in self.body:
            if coord.x == 10:
                rightWall = True
                break
            elif coord.x == 0:
                leftWall = True
                break

        if event.keysym == "Right" and not rightWall:
            for i in range(len(self.body)):
                self.body[i].x += 1
                self.canvas.move(self.tile_ids[i], self.cellLen, 0)
        elif event.keysym == "Left" and not leftWall:
            for i in range(len(self.body)):
                self.body[i].x -= 1
                self.canvas.move(self.tile_ids[i], -self.cellLen, 0)

    def collision(self, field):
        for i in range(len(field)):
            for block in self.body:
                if block.y + 1 == i and field[i][block.x] == 1:
                    return True
                elif block.y >= 11:
                    return True

        return False
