from tkinter import *
from classes.Point import *


class Tile:

    def __init__(self, canvas, shape):
        self.canvas = canvas
        self.tile_ids = list()
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
            raise ValueError("It is not a shape")

    def draw(self, cellLength, color):
        c = self.canvas
        for p in self.body:
            x = p.x * cellLength
            y = p.y * cellLength
            padding = 3
            self.tile_ids.append(c.create_rectangle(x, y, x + cellLength - padding, y + cellLength - padding, fill = color))

    def clear(self):
        for tile_id in self.tile_ids:
            self.canvas.delete(tile_id)

