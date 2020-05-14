import unittest
from unittest.mock import mock_open, patch, MagicMock
from optimizer.route_creator import RouteCreator

class TestRouteCreator(unittest.TestCase):

    @patch('optimizer.csv_parser.CSVParser.parse_into_locations')
    def test_get_locations_returns_correct_array(self, mock):
        mock.return_value = ['hi', 'bye']
        self.assertEqual(RouteCreator('filename').get_locations(), ['hi', 'bye'])