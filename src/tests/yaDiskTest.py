from settings import *
import yadisk


disk = yadisk.YaDisk(YD_ID, YD_SECRET, YD_TOKEN)

print(disk.get_disk_info())

disk.download("/records.json", "../records.json")

