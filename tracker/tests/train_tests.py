import unittest
from tracker import train

class TestTrainMethods(unittest.TestCase):

    def test_get_brownline_routes(self):
        track = train.TrainTracker("key")
        stations = track.get_stations_for_route("brn")
        print(stations)
        self.assertIsNotNone(stations)

    def test_get_stations_for_route_invalid_key(self):
        track = train.TrainTracker("key")
        stations = track.get_stations_for_route("invalid")
        self.assertIsNone(stations)

    def test_get_routes_has_all(self):
        track = train.TrainTracker("key")
        routes = track.get_routes()
        self.assertEqual(8, len(routes))

if __name__ == '__main__':
    unittest.main()