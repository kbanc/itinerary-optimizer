import unittest
from unittest.mock import patch

from optimizer.location import Location

class TestLocation(unittest.TestCase):


    def test_location_initialization(self):
        Location(street="10 Kings College Circle", city="Toronto", country="Canada", postalcode="M5S1A1", mandatory="true", role="carpickup", routeRestriction="start")

    def test_initialization_convert_address_to_coord(self):
        newLocation = Location(street="58 Brunswick Ave", city="Toronto", country="Canada", postalcode="M5S2L7", mandatory="true", role="carpickup", routeRestriction="start")
        coordinates = newLocation.get_coordinates()
        self.assertEqual(coordinates, [43.65901691086957, -79.40501374565218])
    
    @patch('geopy.geocoders.Nominatim')
    def test_get_route_restriction(self, mockGeocode):
        newLocation = Location(street="10 Kings College Circle", city="Toronto", country="Canada", postalcode="M5S1A1", mandatory="true", role="carpickup", routeRestriction="start")
        restriction = newLocation.get_route_restiction()
        self.assertEqual(restriction, "start")

