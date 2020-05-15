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

    class MockResponse(object):
        def json(self):
            return {
                'waypoints': [
                    {"waypoint_index": 0},
                    {"waypoint_index": 2},
                    {"waypoint_index": 1}
                ],
                'trips': [{'legs': [{
                    "weight": 681.9,
                    "duration": 442.8,
                    "distance": 2442.7
                },
                    {
                    "weight": 377.8,
                    "duration": 250.5,
                    "distance": 1533.6
                },
                    {
                    "weight": 494.1,
                    "duration": 385.4,
                    "distance": 2286.8
                }
                ]
                }]
            }

    @patch('requests.get')
    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_get_locations_returns_correct_array(self, mock, mockGet):
        location1 = self.MockLocation()
        mock.return_value = [location1]
        self.assertEqual(RouteCreator(
            'filename').get_locations(), [location1])

    @patch('requests.get')
    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_init_constructs_route_calls_correct_endpoint(self, mockRouter, mockGet):
        location1 = self.MockLocation()
        location2 = self.MockLocation()
        location1.routeRestriction = 'start'
        mockRouter.return_value = [location1, location2]
        RouteCreator('filename')
        mockGet.assert_called_with('http://127.0.0.1:5000/trip/v1/driving/{},{};{},{}?source=first'.format(
            location1.lat, location1.long, location2.lat, location2.long))

    @patch('requests.get')
    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_init_constructs_route_calls_correct_endpoint_with_three_locations(self, mockRouter, mockGet):
        location1 = self.MockLocation()
        location2 = self.MockLocation()
        location3 = self.MockLocation()
        location1.routeRestriction = 'start'
        mockRouter.return_value = [location1, location2, location3]
        RouteCreator('filename')
        mockGet.assert_called_with('http://127.0.0.1:5000/trip/v1/driving/{},{};{},{};{},{}?source=first'.format(
            location1.lat, location1.long, location2.lat, location2.long, location3.lat, location3.long))

    @patch('requests.get')
    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_init_constructs_route_calls_correct_endpoint_with_correct_coordinate_order(self, mockRouter, mockGet):
        location1 = self.MockLocation()
        location2 = self.MockLocation()
        location3 = self.MockLocation()
        location2.routeRestriction = 'start'
        mockRouter.return_value = [location1, location2, location3]
        RouteCreator('filename')
        mockGet.assert_called_with('http://127.0.0.1:5000/trip/v1/driving/{},{};{},{};{},{}?source=first'.format(
            location2.lat, location2.long, location1.lat, location1.long, location3.lat, location3.long))

    @patch('requests.get')
    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_get_route_returns_expected_response(self, mockRouter, mockGet):
        location1 = self.MockLocation()
        location2 = self.MockLocation()
        location3 = self.MockLocation()
        location2.routeRestriction = 'start'
        mockGet.return_value = self.MockResponse()
        mockRouter.return_value = [location1, location2, location3]
        expectedRoute = [{'start': location2,
                          'end': location3,
                          "duration": 442.8,
                          "distance": 2442.7
                          },
                         {'start': location3,
                          'end': location1,
                          "duration": 250.5,
                          "distance": 1533.6
                          },
                         {'start': location1,
                          'end': location2,
                          "duration": 385.4,
                          "distance": 2286.8
                          }
                         ]

        route = RouteCreator('filename').get_route()
        self.assertEqual(route, expectedRoute)

    @patch('requests.get')
    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_total_distance_returns_correct_val(self, mockRouter, mockGet):
        location1 = self.MockLocation()
        location2 = self.MockLocation()
        location3 = self.MockLocation()
        location2.routeRestriction = 'start'
        mockGet.return_value = self.MockResponse()
        mockRouter.return_value = [location1, location2, location3]

        distance = RouteCreator('filename').get_total_distance()
        self.assertEqual(distance, 2442.7+1533.6+2286.8)

    @patch('requests.get')
    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_total_time_returns_correct_val(self, mockRouter, mockGet):
        location1 = self.MockLocation()
        location2 = self.MockLocation()
        location3 = self.MockLocation()
        location2.routeRestriction = 'start'
        mockGet.return_value = self.MockResponse()
        mockRouter.return_value = [location1, location2, location3]

        distance = RouteCreator('filename').get_total_duration()
        self.assertEqual(distance, 442.8+250.5+385.4)
