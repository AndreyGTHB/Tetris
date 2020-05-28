import yadisk

from utils import *
from game import *


def main(*args):
    drive = None
    try:
        drive = yadisk.YaDisk(YD_ID, YD_SECRET, YD_TOKEN)
    except:
        print('No connection')
    download_records(drive)

    with open(RECORD_FILE, "r") as file_object:
        game.record_dict = json.load(file_object)
    game.records = list(game.record_dict.items())

    game.player_name = input("What is your name?")
    if game.player_name == "":
        ananymouses = 0
        for key in game.record_dict:
            if "Anonymous" in key:
                ananymouses += 1
        game.player_name = "Anonymous" + str(ananymouses + 1)

    window = Tk()
    window.title("Tetris")

    game.c = Canvas(window, width=C_WIDTH, height=C_HEIGHT)
    game.c.pack()

    game.c.create_rectangle(0, 0, C_WIDTH, C_HEIGHT, fill="lightblue")  # Background

    for string in range(HEIGHT_IN_BLOCKS):
        game.field_ids.append([])
        game.field.append([])
        y = TILE_SIZE * string
        for clmn in range(WIDTH_IN_BLOCKS):
            x = TILE_SIZE * clmn
            padding = 3
            colour = COLOURS[0]
            game.field_ids[string].append(
                game.c.create_rectangle(x, y, x + TILE_SIZE - padding, y + TILE_SIZE - padding, fill=colour,
                                        outline=STROKE_COLOURS[0]))
            game.field[string].append(0)

    game.c.create_text(30, 10, text="SCORE:", fill="white")

    game.score_text = game.c.create_text(61, 10, fill="white")

    window.bind_all("<Key>", game.eventListener)
    game.tile = game.generateTile()

    game.start_time = int(time.time())
    game.tick()

    window.mainloop()
    push_records(drive)
    game.game_over = True


if __name__ == "__main__":
    main()
