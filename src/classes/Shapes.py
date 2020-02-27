from classes.Tile import Tile
from classes.Point import Point


class Prg(Tile):
    def __init__(self, c, cell):
        super().__init__(c, "prg", cell)

        self.bodies = [
            self.body,
            [
                Point(1, 2),
                Point(1, 1),
                Point(0, 1),
                Point(0, 0),
            ]
        ]


class Sq(Tile):
    def __init__(self, c, cell):
        super().__init__(c, "sq", cell)


class Ln(Tile):
    def __init__(self, c, cell):
        super().__init__(c, "ln", cell)

        self.bodies = [
            self.body,
            [
                Point(1, -1),
                Point(1, 0),
                Point(1, 1),
                Point(1, 2),
            ]
        ]


class Ltr(Tile):
    def __init__(self, c, cell):
        super().__init__(c, "ltr", cell)

        self.bodies = [
            self.body,
            [
                Point(2, 2),
                Point(2, 1),
                Point(2, 0),
                Point(1, 0),
            ],
            [
                Point(2, 1),
                Point(1, 1),
                Point(0, 1),
                Point(0, 2),
            ],
            [
                Point(1, 0),
                Point(1, 1),
                Point(1, 2),
                Point(2, 2),
            ]
        ]
