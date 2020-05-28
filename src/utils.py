import yadisk
import json


def download_records(drive):
    try:
        drive.download("/records.json", "records.json")
    except:
        with open('records.json', 'w') as file:
            json.dump({}, file)
        print('Can not download records')


def push_records(drive):
    try:
        drive.remove("/records.json", permanently=True)
        drive.upload("records.json", "/records.json")
    except:
        print('Can not push records')
