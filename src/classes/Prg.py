from classes.Tile import Tile
from classes.Point import Point


class Prg(Tile):
    def __init__(self, c, cell):
        super().__init__( c, "prg", cell)

        self.bodies = [
            self.body.copy(),
            [
                Point(1, -1),
                Point(1, -2),
                Point(0, -2),
                Point(0, -3),
            ]
        ]







