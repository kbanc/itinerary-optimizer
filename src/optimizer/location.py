from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

class Location(object):

    def __init__(self, street, city, country, postalcode, mandatory, role, routeRestriction, nearestIntersection=None):
        self._street = street
        self._city = city
        self._country = country
        #Nominatim doesn't like using the postal code
        #self._postalcode = postalcode 
        self._mandatory = mandatory
        self._role = role
        self._routeRestriction = routeRestriction
        self._nearestIntersection = nearestIntersection
        self._coord = self._convert_address_to_coordinates()
    
    def get_coordinates(self):
        return self._coord
    
    def _convert_address_to_coordinates(self):
        locator = Nominatim(user_agent="itinerary-optimizer")
        attempts = 0
  
        while attempts < 3:
            try:
                location = locator.geocode(self._get_address())
                return [location.latitude, location.longitude]
            except:
                print("trying again")
                attempts += 1
                RateLimiter(locator.geocode, min_delay_seconds = 1)
        print("Coordinate lookup failed")
        return [0, 0]

    
    def _get_address(self):
        return "{} {} {}".format(self._street, self._city, self._country)

