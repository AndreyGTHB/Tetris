from classes.Tile import Tile


class Sq(Tile):
    def __init__(self, c, cell):
        super().__init__(c, "sq", cell)
