from classes.Point import *
from settings import *
from math import sqrt


class Bomb:
    def __init__(self, x, y, radius):
        self.exploded = False

        self.body = Point(x, y)
        self.exp_radius = radius

    def explosion(self, field):
        score = 0

        for y in range(len(field)):
            for x in range(len(field[y])):
                if field[y][x] == 1:
                    distance = abs(sqrt((self.body.x-x)**2 + (self.body.y-y)**2))
                    if distance <= self.exp_radius:
                        field[y][x] = 0
                        score += 1

        self.exploded = True
        return field, score

