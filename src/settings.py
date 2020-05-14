from GameState import GameState

WIDTH_IN_BLOCKS = 10
HEIGHT_IN_BLOCKS = 12
TILE_SIZE = 50

C_WIDTH = WIDTH_IN_BLOCKS * TILE_SIZE
C_HEIGHT = HEIGHT_IN_BLOCKS * TILE_SIZE

C_SIZE = (C_WIDTH, C_HEIGHT)
SIZE_IN_BLOCKS = (WIDTH_IN_BLOCKS, HEIGHT_IN_BLOCKS)


COLOURS = ("lightblue", "orange", "lightgreen", "red")
STROKE_COLOURS = ("lightblue", "black", "black", "black")


RECORD_FILE = "records.json"

# YaDisk
YD_ID = "4191264719824131aabb9b31192a8e8d"
YD_SECRET = "bc75f9c7eba4442db73f76eec7d9b7c6"
YD_TOKEN = "AgAAAAA-TyNOAAY5GNxFJzPLVklhlFZizdFW1Xg"


game_state = GameState()
