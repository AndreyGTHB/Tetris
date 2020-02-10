from tkinter import *


class Tile:

    def __init__(self, canvas, shape):
        self.canvas = canvas
        if shape == "sq":
            self.body = [
                {"x": 0, "y": -2},
                {"x": 1, "y": -2},
                {"x": 0, "y": -1},
                {"x": 1, "y": -1}
            ]
        elif shape == "prg":
            self.body = [
                {"x": 0, 'y': -2},
                {"x": 1, 'y': -2},
                {"x": 2, 'y': -1},
                {"x": 3, 'y': -1}
            ]
        elif shape == "ln":
            self.body = [
                {'x': 0, 'y': -1},
                {'x': 1, 'y': -1},
                {'x': 2, 'y': -1},
                {'x': 3, 'y': -1}
            ]
        elif shape == "ltr":
            self.body = [
                {'x': 0, 'y': -1},
                {'x': 1, 'y': -1},
                {'x': 2, 'y': -1},
                {'x': 2, 'y': -2}
            ]
        else:
            raise ValueError("It is not a shape")

    def draw(self, cellLength, color):
        c = self.canvas
        for p in self.points:
            x = p.x * cellLength
            y = p.y * cellLength
            padding = 4
            c.create_rectangle(x, y, x + cellLength-padding, y + cellLength-padding, fill = color)
