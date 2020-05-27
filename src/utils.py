import yadisk
import json
from game import game


def download_records():
    try:
        game.drive.download("/records.json", "records.json")
    except:
        with open('records.json', 'w') as file:
            json.dump({}, file)
        print('Can not download records')


def push_records():
    try:
        game.drive.remove("/records.json", permanently=True)
        game.drive.upload("records.json", "/records.json")
    except:
        print('Can not push records')
