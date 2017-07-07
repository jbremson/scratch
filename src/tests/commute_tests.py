from unittest import TestCase

from src.loader import Cities, Trips

class testLoader(TestCase):

    def test_process_trips(self):
        Cities.load_cities()
        Trips.process_trips(debug=True);
