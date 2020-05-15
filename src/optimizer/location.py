from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

class Location(object):

    def __init__(self, street, city, country, postalcode, mandatory, role, routeRestriction, nearestIntersection=None):
        self._street = street
        self._city = city
        self._country = country
        self._postalcode = postalcode 
        self._mandatory = mandatory
        self._role = role
        self._routeRestriction = routeRestriction
        self._nearestIntersection = nearestIntersection
        self._coord = self._convert_address_to_coordinates()
    
    def get_coordinates(self):
        return self._coord
    
    def get_route_restiction(self):
        return self._routeRestriction
    
    def get_address(self):
        return "{}, {}".format(self._street, self._city)
    
    def get_role(self):
        return self._role
    
    def _convert_address_to_coordinates(self):
        locator = Nominatim(user_agent="itinerary-optimizer")
        attempts = 0
  
        while attempts < 3:
            try:
                location = locator.geocode(self._get_formatted_address())
                return [location.latitude, location.longitude]
            except:
                attempts += 1
                RateLimiter(locator.geocode, min_delay_seconds = 1)
        raise LookupError("Coordinate lookup failed for {}. Check if valid address.".format(self.get_address()))

    
    def _get_formatted_address(self):
        #Nominatim doesn't like using the postal code
        return "{} {} {}".format(self._street, self._city, self._country)

