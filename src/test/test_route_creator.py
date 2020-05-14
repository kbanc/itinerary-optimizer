import unittest
from unittest.mock import mock_open, patch, MagicMock
from faker import Faker
from optimizer.route_creator import RouteCreator

class TestRouteCreator(unittest.TestCase):

    class MockLocation(object):
        def __init__(self):
            fake = Faker()
            self.lat = fake.latitude()
            self.long = fake.longitude()
            self.routeRestriction = None

        def get_coordinates(self):
            return [self.lat, self.long]
        
        def get_route_restiction(self):
            return self.routeRestriction

    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_get_locations_returns_correct_array(self, mock):
        mock.return_value = ['hi', 'bye']
        self.assertEqual(RouteCreator('filename').get_locations(), ['hi', 'bye'])
    
    @patch('requests.get')
    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_travelling_salesman_calls_correct_endpoint(self, mockRouter, mockGet):
        location1 = self.MockLocation()
        location2 = self.MockLocation()
        location1.routeRestriction = 'start'
        mockRouter.return_value = [location1, location2]
        RouteCreator('filename').calculate_route()
        mockGet.assert_called_with('http://router.project-osrm.org/trip/v1/driving/{},{};{},{}?source=first'.format(location1.lat, location1.long, location2.lat, location2.long))

    @patch('requests.get')
    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_travelling_salesman_calls_correct_endpoint_with_three_locations(self, mockRouter, mockGet):
        location1 = self.MockLocation()
        location2 = self.MockLocation()
        location3 = self.MockLocation()
        location1.routeRestriction = 'start'
        mockRouter.return_value = [location1, location2, location3]
        RouteCreator('filename').calculate_route()
        mockGet.assert_called_with('http://router.project-osrm.org/trip/v1/driving/{},{};{},{};{},{}?source=first'.format(\
        location1.lat, location1.long, location2.lat, location2.long, location3.lat, location3.long))

    @patch('requests.get')
    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_travelling_salesman_calls_correct_endpoint_with_correct_coordinate_order(self, mockRouter, mockGet):
        location1 = self.MockLocation()
        location2 = self.MockLocation()
        location3 = self.MockLocation()
        location2.routeRestriction = 'start'
        mockRouter.return_value = [location1, location2, location3]
        RouteCreator('filename').calculate_route()
        mockGet.assert_called_with('http://router.project-osrm.org/trip/v1/driving/{},{};{},{};{},{}?source=first'.format(\
        location2.lat, location2.long, location1.lat, location1.long,location3.lat, location3.long))

    def test_travelling_salesman_parses_route(self):
        pass

    def test_total_distance_returns_correct_val(self):
        pass

    def test_total_time_returns_correct_val(self):
        pass