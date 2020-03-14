from classes.Point import *
from settings import *


class Tile:

    def __init__(self, canvas, shape, cell):
        self.canvas = canvas
        self.tile_ids = list()
        self.cellLen = cell

        self.current_turn = 0
        if shape == "sq":
            self.body = [
                Point(0, 0),
                Point(1, 0),
                Point(0, 1),
                Point(1, 1)
            ]
        elif shape == "prg":
            self.body = [
                Point(0, 1),
                Point(1, 1),
                Point(1, 0),
                Point(2, 0)
            ]
        elif shape == "ln":
            self.body = [
                Point(0, 0),
                Point(1, 0),
                Point(2, 0),
                Point(3, 0)
            ]
        elif shape == "ltr":
            self.body = [
                Point(0, 1),
                Point(1, 1),
                Point(2, 1),
                Point(2, 0)
            ]
        elif shape == "tbl":
            self.body = [
                Point(0, 1),
                Point(1, 1),
                Point(2, 1),
                Point(1, 0)
            ]
        else:
            raise ValueError("'" + shape + "'", "is not a shape")

        self.bodies = [self.body]

    def fall(self):
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
            if coord.x == WIDTH_IN_BLOCKS-1:
                return False

        for str in range(len(field)):
            ys = field[str]
            for t in self.body:
                if t.y == str and ys[t.x + 1] == 1:
                    return False

        return True

    def move(self, event, field):

        if event.keysym == "Right" and self.mayMoveR(field):
            for body in range(len(self.bodies)):
                for i in range(len(self.bodies[body])):
                    self.bodies[body][i].x += 1

        elif event.keysym == "Left" and self.mayMoveL(field):
            for body in range(len(self.bodies)):
                for i in range(len(self.bodies[body])):
                    self.bodies[body][i].x -= 1

    def collision(self, field):
        for block in self.body:
            if block.y >= HEIGHT_IN_BLOCKS-1:
                return True
            elif field[block.y + 1][block.x] == 1:
                return True
        return False

    def rotate(self, field):

        if self.mayRotate(field):
            self.current_turn += 1
            if self.current_turn >= len(self.bodies):
                self.current_turn = 0
            self.body = self.bodies[self.current_turn]

    def mayRotate(self, field):
        if self.current_turn + 1 >= len(self.bodies):
            next_turn = 0
        else:
            next_turn = self.current_turn + 1
        nextBody = self.bodies[next_turn]

        for block in nextBody:
            if block.x > WIDTH_IN_BLOCKS-1 or block.x < 0 or block.y > HEIGHT_IN_BLOCKS-1 or block.y < 0:  # If block out of field
                return False
            elif field[block.y][block.x] == 1:  # If block in built
                return False

        return True
