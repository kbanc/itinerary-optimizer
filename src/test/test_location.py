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
    
    @patch('geopy.geocoders.Nominatim')
    def test_get_route_restriction(self, mockGeocode):
        newLocation = Location(street="10 Kings College Circle", city="Toronto", country="Canada", postalcode="M5S1A1", mandatory="true", role="carpickup", routeRestriction="start")
        restriction = newLocation.get_route_restiction()
        self.assertEqual(restriction, "start")

    @patch('geopy.geocoders.Nominatim')
    def test_get_address(self, mockGeocode):
        newLocation = Location(street="10 Kings College Circle", city="Toronto", country="Canada", postalcode="M5S1A1", mandatory="true", role="carpickup", routeRestriction="start")
        address = newLocation.get_address()
        self.assertEqual(address, "10 Kings College Circle, Toronto")

    @patch('geopy.geocoders.Nominatim')
    def test_get_role(self, mockGeocode):
        newLocation = Location(street="10 Kings College Circle", city="Toronto", country="Canada", postalcode="M5S1A1", mandatory="true", role="carpickup", routeRestriction="start")
        notes = newLocation.get_role()
        self.assertEqual(notes, "carpickup")

