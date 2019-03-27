import unittest
from tracker import train

class TestTrainMethods(unittest.TestCase):

    def test_get_brownline_routes(self):
        track = train.TrainTracker("key")
        stations = track.get_stations_for_route("brn")
        print(stations)
        self.assertIsNotNone(stations)

if __name__ == '__main__':
    unittest.main()