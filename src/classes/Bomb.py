from classes.Point import *
from settings import *
from math import sqrt


class Bomb:
    def __init__(self, x: int, y: int, radius: int) -> object:
        self.exploded = False

        self.body = Point(x, y)
        self.exp_radius = radius

    def explosion(self, field, score):
        if self.exploded:
            return field, score

        field[self.body.y][self.body.x] = 2  # Deleting this bomb

        for y in range(len(field)):
            for x in range(len(field[y])):
                if field[y][x] == 1:
                    distance = abs(sqrt((self.body.x - x) ** 2 + (self.body.y - y) ** 2))
                    if distance <= self.exp_radius:
                        field[y][x] = 0
                        score += 1

        self.exploded = True
        return field, score

    def collision(self, field):
        if field[self.body.y][self.body.x] == 2:
            return True

        return False
