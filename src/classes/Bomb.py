from classes.Point import *
from settings import *
from math import sqrt


class Bomb:
    def __init__(self, x: int, y: int, radius: int):
        self.exploded = False

        self.__body = Point(x, y)
        self.exp_radius = radius

    def explosion(self, field, score):
        if self.exploded:
            return field, score

        field[self.get_body().y][self.get_body().x] = 2  # Deleting this bomb

        for y in range(len(field)):
            for x in range(len(field[y])):
                if field[y][x] == 1:
                    if self.get_body().x - x == 0:
                        distance = abs(self.get_body().y - y)
                    elif self.get_body().y - y == 0:
                        distance = abs(self.get_body().y - y)
                    else:
                        distance = abs(sqrt((self.get_body().x - x) ** 2 + (self.get_body().y - y) ** 2))
                    if distance <= self.exp_radius:
                        field[y][x] = 0
                        score += 1

        self.exploded = True
        return field, score

    def collision(self, field):
        if field[self.get_body().y][self.get_body().x] == 2:
            return True

        return False

    def get_body(self):
        return self.__body
