import requests
import json

route_url = 'https://data.cityofchicago.org/resource/8mj8-j3c4.json'

class TrainTracker():
    def __init__(self, key):
        self.key = key

    def get_stations_for_route(self, route):
        # i'd like to move this to a data store that refreshes every x days
        response = requests.get(route_url + f'?{route}=true')
        data = json.loads(response.text)
        return data

        

# class Route(self):
#     def __init__(self, direction_id, ):
#         self.

