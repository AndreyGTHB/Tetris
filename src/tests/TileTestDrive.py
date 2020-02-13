from classes.Tile import Tile
from tkinter import *
import time

from classes.Point import Point


class TileTestDrive:

    def test_constructor(self):
        try:
            tile = Tile("ltr")
        except Exception:
            print("Test 1 failed")
        else:
            print("Test 1 completed")

        try:
            tile = Tile("gg")
        except ValueError:
            print("Test 2 completed")
        else:
            print("Test 2 failed")

        tile = Tile("sq")
        if tile.body[2].x == 0 and tile.bodyp[2].y == -1:
            print("Test 3 completed")
        else:
            print("Test 3 failed")

    def test_draw(self):
        """
        This method draws a Tile of type "sq"
        green in the coordinates "{x: 0, y: 0} - {x: 1, y: 1}"
        """

        window = Tk()
        window.title("DrawTest")
        c = Canvas(width=550, height=600)
        c.pack()

        tile = Tile(c, "sq")
        tile.body = [Point(0, 0),
                     Point(1, 0),
                     Point(0, 1),
                     Point(1, 1)
                     ]

        tile.draw(50, "green")
        window.update()
        time.sleep(2)

        tile.clear()
        window.update()
        time.sleep(2)



tester = TileTestDrive()

tester.test_draw()
