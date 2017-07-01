#! timetravel.py

from datetime import datetime
from datetime import date
import time
import googlemaps
import secret_config
import csv
import os

client = googlemaps.Client(key=secret_config.API_KEY)
dest = secret_config.DESTINATION
timeObj = datetime.now()
data = []


# Swap origin and destination in PM, based on settings in secret_config.py
def swapInPm():
    if (secret_config.SWAP_IN_PM and (time.strftime("%p", time.localtime()) == 'PM')):
        return True
    else:
        return False


for orig in secret_config.ORIGINS:

    if not (swapInPm()):
        response = client.directions(orig, dest, departure_time=time.time(), traffic_model='best_guess')
    else:
        response = client.directions(orig, dest, departure_time=time.time(), traffic_model='best_guess')

    data.insert(len(data), [str(date.today()), str(time.strftime('%A', time.localtime())),
                            str(time.strftime('%T', time.localtime())), dest, orig,
                            response[0]['legs'][0]['duration_in_traffic']['value']])

path = os.path.join(os.path.dirname(__file__), 'timetravel.csv')

with open(path, 'a') as fp:
    fw = csv.writer(fp, delimiter=',')
    fw.writerows(data)
