from classes.Tile import Tile
from classes.Point import Point


class Prg(Tile):
    def __init__(self, c, cell):
        super().__init__(c, "prg", cell)

        self.bodies = [
            self.body.copy(),
            [
                Point(1, -1),
                Point(1, -2),
                Point(0, -2),
                Point(0, -3),
            ]
        ]

        print(self.bodies)

    def rotate(self):
        if self.body == self.bodies[0]:
            self.body = self.bodies[1].copy()
        else:
            self.body = self.bodies[0].copy()

        self.clear()
        self.draw("lightgreen")

    def fall(self):
        super().fall()
        for body in range(len(self.bodies)):
            for i in range(len(self.bodies[body])):
                self.bodies[body][i].y += 1

    def move(self, event, field):
        super().move(event, field)

        if event.keysym == "Right" and self.mayMoveR(field):
            for body in range(len(self.bodies)):
                for i in range(len(self.bodies[body])):
                    self.bodies[body][i].x += 1
        elif event.keysym == "Left" and self.mayMoveL(field):
            for body in range(len(self.bodies)):
                for i in range(len(self.bodies[body])):
                    self.bodies[body][i].y -= 1
