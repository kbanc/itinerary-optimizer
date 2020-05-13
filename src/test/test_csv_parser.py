import unittest
from unittest.mock import mock_open, patch, MagicMock
from optimizer.csv_parser import CSVParser

class TestCSVParser(unittest.TestCase):
    
    def test_parse_into_location_takes_filename_arg(self):
        with patch("builtins.open", mock_open(read_data="data")) as m:
            CSVParser.parse_into_locations('myfakename')
    
    def test_throws_error_if_file_not_found(self):
        with self.assertRaises(Exception) as context:
            CSVParser.parse_into_locations('myfakename')
        self.assertTrue('No such file' in str(context.exception))