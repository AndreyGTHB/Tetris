

class Tile:

    def __init__(self, shape):
        if shape == "sq":
            this.coords = [
                {"x": 0, "y": -2},
                {"x": 1, "y": -2},
                {"x": 0, "y": -1},
                {"x": 1, "y": -1}
                ]
        elif shape == "prg":
            self.coords = [
                {"x": 0, 'y': -2},
                {"x": 1, 'y': -2},
                {"x": 2, 'y': -1},
                {"x": 3, 'y': -1}
                ]
        elif shape == "ln":
            self.coords = [
                {'x': 0, 'y': -1},
                {'x': 1, 'y': -1},
                {'x': 2, 'y': -1},
                {'x': 3, 'y': -1}
                ]
        elif shape == "ltr":
            self.coords = [
                {'x': 0, 'y': -1},
                {'x': 1, 'y': -1},
                {'x': 2, 'y': -1},
                {'x': 2, 'y': -2}
                ]
        else:
            raise ValueError("It is not a shape")


class TileTestDrive:
    def test():
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

tester = TileTestDrive
tester.test()








