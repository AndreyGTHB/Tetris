from classes.Tile import Tile
from classes.Point import Point


class Sq(Tile):
    def __init__(self, c, cell):
        super().__init__(c, "prg", cell)

        self.bodies = [self.body, []]