import requests
import json

route_url = 'https://data.cityofchicago.org/resource/8mj8-j3c4.json'
arrivals_url = 'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx'

class TrainTracker():
    def __init__(self, key):
        self.key = key

    def get_stations_for_route(self, route):
        # i'd like to move this to a data store that refreshes every x days
        if(route in self.get_routes().keys()):
            response = requests.get(route_url + f'?{route}=true')
            data = json.loads(response.text)
            return data
        else:
            pass

    def get_routes(self):
        return{"red":"Red", "p": "Purple", "y": "Yellow", "blue": "Blue", "pnk": "Pink", "o": "Orange", "brn": "Brown", "g": "Green"}
        

# class Route(self):
#     def __init__(self, direction_id, ):
#         self.

