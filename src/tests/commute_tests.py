from unittest import TestCase

from peewee import *
import src.secret_config
from src.loader import Cities, Trips

#db = MySQLDatabase("test_commute", user="root", host="127.0.0.1", port=3306, password=src.secret_config.dbpassword)

class testLoader(TestCase):

    def test_process_trips(self):
        Cities.load_cities()
        Trips.process_trips(debug=True);
