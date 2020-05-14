import yadisk

from functions import *


def main(*args):
    global game_state

    try:
        game_state.drive = yadisk.YaDisk(YD_ID, YD_SECRET, YD_TOKEN)
    except:
        print('No connection')
    download_records()

    with open(RECORD_FILE, "r") as file_object:
        game_state.record_dict = json.load(file_object)
    game_state.records = list(game_state.record_dict.items())

    game_state.player_name = input("What is your name?")
    if game_state.player_name == "":
        ananymouses = 0
        for key in game_state.record_dict:
            if "Anonymous" in key:
                ananymouses += 1
        game_state.player_name = "Anonymous" + str(ananymouses + 1)

    window = Tk()
    window.title("Tetris")

    game_state.c = Canvas(window, width=C_WIDTH, height=C_HEIGHT)
    game_state.c.pack()

    game_state.c.create_rectangle(0, 0, C_WIDTH, C_HEIGHT, fill="lightblue")  # Background

    for str in range(HEIGHT_IN_BLOCKS):
        game_state.field_ids.append([])
        game_state.field.append([])
        y = TILE_SIZE * str
        for clmn in range(WIDTH_IN_BLOCKS):
            x = TILE_SIZE * clmn
            padding = 3
            colour = COLOURS[0]
            game_state.field_ids[str].append(
                game_state.c.create_rectangle(x, y, x + TILE_SIZE - padding, y + TILE_SIZE - padding, fill=colour,
                                              outline=STROKE_COLOURS[0]))
            game_state.field[str].append(0)

    game_state.c.create_text(30, 10, text="SCORE:", fill="white")

    game_state.score_text = game_state.c.create_text(61, 10, fill="white")

    window.bind_all("<Key>", eventListener)
    game_state.tile = generateTile()

    game_state.start_time = int(time.time())
    tick()

    window.mainloop()
    game_state.game_over = True


if __name__ == "__main__":
    main()
