from tkinter import *
from time import sleep

from Point import *


class Tile:

    def __init__(self, window, field, canvas, shape, cell):
        self.window = window
        self.field = field
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

        for coord in self.body:
            if coord.x >= 0 and coord.y >= 0 and coord.x <=11 and coord.y <= 12:
                self.field[coord.y][coord.x] = 1

    def draw(self, color):
        c = self.canvas
        for p in self.body:
            x = p.x * self.cellLen
            y = p.y * self.cellLen
            padding = 3
            self.tile_ids.append(c.create_rectangle(x, y, x + self.cellLen - padding, y + self.cellLen - padding, fill=color))
        self.window.update()


    def clear(self):
        for tile_id in self.tile_ids:
            self.canvas.delete(tile_id)
        self.window.update()
        
        for i in range(len(self.tile_ids)):
            del (self.tile_ids[0])

    def fall(self):
        for coord in self.body:
            if coord.x >= 0 and coord.y >= 0 and coord.x <=11 and coord.y <= 12:
                self.field[coord.y][coord.x] = 0
        
        for i in range(len(self.body)):
            self.body[i].y += 1
            self.canvas.move(self.tile_ids[i], 0, self.cellLen)
        self.window.update()
        
        for coord in self.body:
            if coord.x >= 0 and coord.y >= 0 and coord.x <=11 and coord.y <= 12:
                self.field[coord.y][coord.x] = 1


    def move(self, event):
        rightWall = False
        leftWall = False
        for coord in self.body:
            if coord.x == 11:
                rightWall = True
                break
            elif coord.x == 0:
                leftWall = True
                break

        for coord in self.body:
            if coord.x >= 0 and coord.y >= 0 and coord.x <=11 and coord.y <= 12:
                self.field[coord.y][coord.x] = 0

        
        if event.keysym == "Right" and not rightWall:
            for i in range(len(self.body)):
                self.body[i].x += 1
                self.canvas.move(self.tile_ids[i], self.cellLen, 0)
        elif event.keysym == "Left" and not leftWall:
            for i in range(len(self.body)):
                self.body[i].x -= 1
                self.canvas.move(self.tile_ids[i], -self.cellLen, 0)
        self.window.update()

        for coord in self.body:
            if coord.x >= 0 and coord.y >= 0 and coord.x <=11 and coord.y <= 12:
                self.field[coord.y][coord.x] = 1






