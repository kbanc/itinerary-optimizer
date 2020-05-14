import requests
from optimizer.csv_parser import CSVParser

class RouteCreator(object):

    def __init__(self, filename):
        self._locations = CSVParser.parse_into_locations(filename)
    
    def get_locations(self):
        return self._locations
    
    def calculate_route(self):
        osmAPIAddr = 'http://router.project-osrm.org/trip/v1/driving/'
        requests.get(osmAPIAddr + self._make_lat_long_string())

    def _make_lat_long_string(self):
        latLongString = ''
        for location in self._locations:
            lat, longitude = location.get_coordinates()
            latLongString = latLongString + '{},{};'.format(lat, longitude)
        return latLongString[:-1]
