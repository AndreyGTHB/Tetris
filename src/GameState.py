

class GameState:
    player_name = None

    c = None
    score_text = None

    drive = None

    game_over = False
    start_time = None

    score = 0
    record_dict = {"k": "v"}
    records = list()

    paused = False
    pause_bg = None
    pause_text = None

    field = list()
    field_ids = list()
    bombs = list()

    tile = None

