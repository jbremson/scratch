"""Load cities info into Cities table from config.py."""

from concurrent.futures import Future, Executor, ThreadPoolExecutor
import googlemaps
from peewee import *
from src import config, secret_config
from threading import Lock


db = MySQLDatabase("commute", user="commuter", host="127.0.0.1", port=3306, password=secret_config.commuter_password)
client = googlemaps.Client(key=secret_config.KEY)


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

class BaseCommute(Model):

    class Meta:
        database = db

class Cities(BaseCommute):
    """ORM to the 'cities' table."""
    id = IntegerField()
    name = CharField()
    region = CharField()

    @classmethod
    def load_cities(cls):
        with db.atomic():
            for region, city_list in config.cities.items():
                for city in city_list:
                    try:
                        Cities(name=city, region=region).save()
                    except IntegrityError: #skip entries that are already there.
                        pass

class DummyExecutor(Executor):

    def __init__(self, *args, **kwargs):
        self._shutdown = False
        self._shutdownLock = Lock()

    def submit(self, fn, *args, **kwargs):
        with self._shutdownLock:
            if self._shutdown:
                raise RuntimeError('cannot schedule new futures after shutdown')

            f = Future()
            try:
                result = fn(*args, **kwargs)
            except BaseException as e:
                f.set_exception(e)
            else:
                f.set_result(result)

            return f

    def shutdown(self, wait=True):
        with self._shutdownLock:
            self._shutdown = True

class Trips(BaseCommute):
    """ORM to the 'trips' table."""
    id = IntegerField()
    origin = IntegerField()
    destination = IntegerField()
    time = IntegerField()
    text_time = CharField()


    @staticmethod
    def estimate(city_pair):
        name_to_id = dict()
        response = client.directions(city_pair[0], city_pair[1], departure_time='now')
        out = response[0]['legs'][0]['duration_in_traffic']
        o = Trips(origin=Cities.get(Cities.name==city_pair[0]).id,
              destination=Cities.get(Cities.name==city_pair[1]).id,
              time=out['value'], text_time=out['text'])
        o.save()
        print(out)


    @classmethod
    def process_trips(cls, debug=False):
        regions_list = Cities.select(Cities.region).distinct()
        Exec = DummyExecutor if debug else ThreadPoolExecutor
        for region in regions_list:
            if region.region=='':
                continue
            city_list = [a.name for a in Cities.select(Cities.name).where(Cities.region == region.region)]
            with Exec(max_workers=20) as executor:
                future_to_trip_time = {executor.submit(cls.estimate, pair): pair for pair in
                                       combinations(city_list)}





