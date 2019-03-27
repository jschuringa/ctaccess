import requests
import json

route_url = 'https://data.cityofchicago.org/resource/8mj8-j3c4.json'

class TrainTracker():
    def __init__(self, key):
        self.key = key

    def get_stations_for_route(self, route):
        # i'd like to move this to a data store that refreshes every x days
        response = requests.get(route_url)
        data = json.loads(response.text)
        stations = [i for i in data if i[route] == True]
        return stations

        

# class Route(self):
#     def __init__(self, direction_id, ):
#         self.

