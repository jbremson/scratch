import config
import secret_config
import googlemaps
import time
from datetime import timedelta

client = googlemaps.Client(key=secret_config.KEY)

def get_duration(response):
    print(response[0]['legs'][0]['duration_in_traffic'])

def combinations(list):
    """Take a list, return pair combos where the pair values are not equal.

    Arguments:
        list, list of strings.
    """
    for first in list:
        for second in list:
            if first == second:
                continue
            yield (first, second)

def get_estimate(city_list):
    response = client.directions(city_list[0], city_list[1], departure_time='now')
    return get_duration(response)

for pair in combinations(config.cities):
    print(pair)
    print(get_estimate(pair))