from optimizer.csv_parser import CSVParser

class RouteCreator(object):

    def __init__(self, filename):
        self._locations = CSVParser.parse_into_locations(filename)
    
    def get_locations(self):
        return self._locations