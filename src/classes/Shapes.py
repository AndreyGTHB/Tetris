from classes.Tile import Tile
from classes.Point import Point


class Prg(Tile):
    def __init__(self, cell):
        super().__init__(cell)

        self.body = [
            Point(0, 1),
            Point(1, 1),
            Point(1, 0),
            Point(2, 0)
        ]
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
    def __init__(self, cell):
        super().__init__(cell)

        self.body = [
            Point(0, 0),
            Point(1, 0),
            Point(0, 1),
            Point(1, 1)
        ]
        self.bodies = [self.body]


class Ln(Tile):
    def __init__(self, cell):
        super().__init__(cell)

        self.body = [
            Point(0, 0),
            Point(1, 0),
            Point(2, 0),
            Point(3, 0)
        ]
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
    def __init__(self, cell):
        super().__init__(cell)

        self.body = [
            Point(0, 1),
            Point(1, 1),
            Point(2, 1),
            Point(2, 0)
        ]
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


class Tbl(Tile):
    def __init__(self, cell):
        super().__init__(cell)

        self.body = [
            Point(0, 1),
            Point(1, 1),
            Point(2, 1),
            Point(1, 0)
        ]
        self.bodies = [
            self.body,
            [
                Point(1, 0),
                Point(1, 1),
                Point(1, 2),
                Point(0, 1)
            ],
            [
                Point(0, 1),
                Point(1, 1),
                Point(2, 1),
                Point(1, 2)
            ],
            [
                Point(1, 0),
                Point(1, 1),
                Point(1, 2),
                Point(2, 1)
            ]
        ]
