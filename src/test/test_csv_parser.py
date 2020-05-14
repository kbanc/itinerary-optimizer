import unittest
from unittest.mock import mock_open, patch, MagicMock
from faker import Faker

@patch("optimizer.location.Location")
class TestCSVParser(unittest.TestCase):
        
    
    def test_parse_into_location_takes_filename_arg(self,mockLocation):
        mockLocation.return_value = 'foo'
        from optimizer.csv_parser import CSVParser
        with patch("builtins.open", mock_open(read_data="data, beta")):
            CSVParser.parse_into_locations('myfakename')
    
    def test_throws_error_if_file_not_found(self,  mockLocation):
        mockLocation.return_value = 'foo'
        from optimizer.csv_parser import CSVParser
        with self.assertRaises(Exception) as context:
            CSVParser.parse_into_locations('myfakename')
        self.assertTrue('No such file' in str(context.exception))
    
    def test_creates_location_object_with_data(self, mockLocation):
        mockLocation.return_value = 'foo'
        from optimizer.csv_parser import CSVParser
        with patch("builtins.open", mock_open(read_data="street,city,country,postalcode,mandatory,role,routeRestriction,nearestIntersection\n123 Sesame St,Fairy,Land,987654,TRUE,car,start,bloor")) as m:
            CSVParser.parse_into_locations('myfakename')
            mockLocation.assert_called_with('123 Sesame St', 'Fairy', 'Land', '987654', 'TRUE', 'car', 'start', 'bloor')

    @unittest.skip('still need to fix')
    def test_creates_location_object_with_data_no_intersection(self, mockLocation):
        mockLocation.return_value = 'foo'
        from optimizer.csv_parser import CSVParser
        with patch("builtins.open", mock_open(read_data="street,city,country,postalcode,mandatory,role,routeRestriction,nearestIntersection\n123 Sesame St,Fairy,Land,987654,TRUE,car,start")) as m:
            CSVParser.parse_into_locations('myfakename')
            mockLocation.assert_called_with('123 Sesame St', 'Fairy', 'Land', '987654', 'TRUE', 'car', 'start')

    def test_returns_location_list(self, mockLocation):
        mockLocation.return_value = 'foo'
        from optimizer.csv_parser import CSVParser
        with patch("builtins.open", mock_open(read_data="street,city,country,postalcode,mandatory,role,routeRestriction,nearestIntersection\n123 Sesame St,Fairy,Land,987654,TRUE,car,start,bloor")) as m:
            locations = CSVParser.parse_into_locations('myfakename')
        self.assertEqual(locations, ['foo'])
