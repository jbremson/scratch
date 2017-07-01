import config
import secret_config
import googlemaps
import concurrent.futures

"""https://docs.python.org/dev/library/concurrent.futures.html#threadpoolexecutor"""

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
    print("{} - {}".format(city_list, get_duration(response)))

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    future_to_trip_time = {executor.submit(get_estimate, pair): pair for pair in combinations(config.cities)}
    for future in concurrent.futures.as_completed(future_to_trip_time):
        try:
            data = future.result()
        except Exception as e:
            print(e)
        else:
            print(data)
