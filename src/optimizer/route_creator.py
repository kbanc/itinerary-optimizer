import requests
from optimizer.csv_parser import CSVParser

class RouteCreator(object):

    def __init__(self, filename):
        self._locations = CSVParser.parse_into_locations(filename)
        self._route = self._calculate_route()
    
    def get_locations(self):
        return self._locations
    
    def get_route(self):
        return self._route
    
    def get_total_distance(self):
        distance = 0
        for leg in self._route:
            distance += leg['distance']
        return distance
    
    def get_total_duration(self):
        duration = 0
        for leg in self._route:
            duration += leg['duration']
        return duration
    
    def _calculate_route(self): #this could be private
        route = []
        osmAPIAddr = 'http://router.project-osrm.org/trip/v1/driving/'
        routeData = requests.get(osmAPIAddr + self._make_lat_long_string() + '?source=first')

        destinationOrder = [0]*len(self.get_locations())
        for index, waypoint in enumerate(routeData['waypoints']):
            destinationOrder[int(waypoint['waypoint_index'])] = index

        for index, leg in enumerate(routeData['legs']):
            startLocation = self._locations[destinationOrder[index]]
            if index < len(destinationOrder) - 1:
                endLocation = self._locations[destinationOrder[index+1]]
            else:
                endLocation = self._locations[destinationOrder[0]]
            route.append({'start': startLocation, 'end': endLocation, 'distance': leg['distance'],
            'duration': leg['duration']})
        return route


    def _make_lat_long_string(self):
        self._reorder_locations()
        latLongString = ''
        for location in self._locations:
            lat, longitude = location.get_coordinates()
            latLongString = latLongString + '{},{};'.format(lat, longitude)
        return latLongString[:-1]
    
    def _reorder_locations(self):
        for index, location in enumerate(self._locations):
            if location.get_route_restiction() == 'start':
                self._locations.pop(index)
                self._locations.insert(0, location)
                return