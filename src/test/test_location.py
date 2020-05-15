import unittest
from unittest.mock import patch

from optimizer.location import Location

class TestLocation(unittest.TestCase):


    def test_location_initialization(self):
        Location(street="10 Kings College Circle", city="Toronto", country="Canada", postalcode="M5S1A1", mandatory="true", role="carpickup", routeRestriction="start")

    def test_initialization_convert_address_to_coord(self):
        newLocation = Location(street="481 Queen St W", city="Toronto", country="Canada", postalcode="M5V2A9", mandatory="true", role="carpickup", routeRestriction="start")
        coordinates = newLocation.get_coordinates()
        self.assertEqual(coordinates, [43.6482699, -79.3978559])
    
    @patch('optimizer.location.Nominatim')
    def test_address_to_coord_raises_exception_if_cannot_convert(self, mockGeocode):
        mockGeocode.return_value.geocode = lambda location: 1/0
        with self.assertRaises(Exception) as context:
            Location(street="123 Fake Address", city="Toronto", country="Canada", postalcode="M5V2A9", mandatory="true", role="carpickup", routeRestriction="start")
        self.assertTrue('Coordinate lookup failed for 123 Fake Address, Toronto. Check if valid address.' in str(context.exception))

    @patch('optimizer.location.Nominatim')
    def test_get_route_restriction(self, mockGeocode):
        newLocation = Location(street="10 Kings College Circle", city="Toronto", country="Canada", postalcode="M5S1A1", mandatory="true", role="carpickup", routeRestriction="start")
        restriction = newLocation.get_route_restiction()
        self.assertEqual(restriction, "start")

    @patch('optimizer.location.Nominatim')
    def test_get_address(self, mockGeocode):
        newLocation = Location(street="10 Kings College Circle", city="Toronto", country="Canada", postalcode="M5S1A1", mandatory="true", role="carpickup", routeRestriction="start")
        address = newLocation.get_address()
        self.assertEqual(address, "10 Kings College Circle, Toronto")

    @patch('optimizer.location.Nominatim')
    def test_get_role(self, mockGeocode):
        newLocation = Location(street="10 Kings College Circle", city="Toronto", country="Canada", postalcode="M5S1A1", mandatory="true", role="carpickup", routeRestriction="start")
        notes = newLocation.get_role()
        self.assertEqual(notes, "carpickup")

