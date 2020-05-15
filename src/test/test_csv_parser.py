import unittest
from unittest.mock import mock_open, patch

from optimizer.csv_parser import CSVParser

class TestCSVParser(unittest.TestCase):

    @patch("optimizer.csv_parser.Location")
    def test_parse_into_location_takes_filename_arg(self,mockLocation):
        mockLocation.return_value = 'foo'
        with patch("builtins.open", mock_open(read_data="data, beta")):
            CSVParser.parse_into_locations('myfakename')
    
    @patch("optimizer.csv_parser.Location")
    def test_throws_error_if_file_not_found(self,  mockLocation):
        mockLocation.return_value = "foo"
        with self.assertRaises(Exception) as context:
            CSVParser.parse_into_locations('myfakename')
        self.assertTrue("No such file" in str(context.exception))
    
    @patch("optimizer.csv_parser.Location")
    def test_creates_location_object_with_data(self, mockLocation):
        mockLocation.return_value = "foo"
        with patch("builtins.open", mock_open(read_data="street,city,country,postalcode,mandatory,role,routeRestriction,nearestIntersection\n123 Sesame St,Fairy,Land,987654,TRUE,car,start,bloor")):
            CSVParser.parse_into_locations('myfakename')
            mockLocation.assert_called_with('123 Sesame St', 'Fairy', 'Land', '987654', 'TRUE', 'car', 'start', 'bloor')

    @patch("optimizer.csv_parser.Location")
    def test_creates_location_object_with_data_no_intersection(self, mockLocation):
        mockLocation.return_value = 'foo'
        with patch("builtins.open", mock_open(read_data="street,city,country,postalcode,mandatory,role,routeRestriction,nearestIntersection\n123 Sesame St,Fairy,Land,987654,TRUE,car,start")):
            CSVParser.parse_into_locations('myfakename')
            mockLocation.assert_called_with('123 Sesame St', 'Fairy', 'Land', '987654', 'TRUE', 'car', 'start')
    
    @patch("optimizer.csv_parser.Location", side_effect=LookupError('Coordinate lookup failed for 123 Sesame St, Fairy. Check if valid address.'))
    def test_raises_error_if_location_coordinates_not_successfully_converted(self, mockLocation):
        with self.assertRaises(Exception) as context:
            with patch("builtins.open", mock_open(read_data="street,city,country,postalcode,mandatory,role,routeRestriction,nearestIntersection\n123 Sesame St,Fairy,Land,987654,TRUE,car,start")):
                CSVParser.parse_into_locations('myfakename')
        self.assertTrue('Coordinate lookup failed for 123 Sesame St, Fairy. Check if valid address.' in str(context.exception))


    @patch("optimizer.csv_parser.Location")
    def test_returns_location_list(self, mockLocation):
        mockLocation.return_value = 'foo'
        from optimizer.location import Location
        with patch("builtins.open", mock_open(read_data="street,city,country,postalcode,mandatory,role,routeRestriction,nearestIntersection\n123 Sesame St,Fairy,Land,987654,TRUE,car,start,bloor")):
            locations = CSVParser.parse_into_locations('myfakename')
        self.assertEqual(locations, ['foo'])
