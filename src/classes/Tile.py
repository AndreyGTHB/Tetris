from tkinter import *
from time import sleep
from abc import abstractmethod

from classes.Point import *


class Tile:

    def __init__(self, canvas, shape, cell):
        self.canvas = canvas
        self.tile_ids = list()
        self.cellLen = cell

        self.current_turn = 0
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

        self.bodies = [self.body]

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
            self.canvas.move(self.tile_ids[i], 0, self.cellLen)

        for body in range(len(self.bodies)):
            for i in range(len(self.bodies[body])):
                self.bodies[body][i].y += 1

    def mayMoveL(self, field):
        for coord in self.body:
            if coord.x == 0:
                return False

        for str in range(len(field)):
            ys = field[str]
            for t in self.body:
                if t.y == str and ys[t.x - 1] == 1:
                    return False

        return True

    def mayMoveR(self, field):
        for coord in self.body:
            if coord.x == 9:
                return False

        for str in range(len(field)):
            ys = field[str]
            for t in self.body:
                if t.y == str and ys[t.x + 1] == 1:
                    return False

        return True

    def move(self, event, field):

        if event.keysym == "Right" and self.mayMoveR(field):
            for i in range(len(self.body)):
                self.canvas.move(self.tile_ids[i], self.cellLen, 0)

            for body in range(len(self.bodies)):
                for i in range(len(self.bodies[body])):
                    self.bodies[body][i].x += 1

        elif event.keysym == "Left" and self.mayMoveL(field):
            for i in range(len(self.body)):
                self.canvas.move(self.tile_ids[i], -self.cellLen, 0)

            for body in range(len(self.bodies)):
                for i in range(len(self.bodies[body])):
                    self.bodies[body][i].y -= 1

    def collision(self, field):
        for block in self.body:
            if block.y >= 11 or field[block.y + 1][block.x] == 1:
                return True
        return False

    def rotate(self):
        self.current_turn += 1

        if self.current_turn >= len(self.bodies):
            self.current_turn = 0

        self.body = self.bodies[self.current_turn]
        self.clear()
        self.draw("lightgreen")

    def mayRotate(self):
        pass
