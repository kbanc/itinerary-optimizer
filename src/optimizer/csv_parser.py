import os
import csv

from optimizer.location import Location

class CSVParser(object):

    @classmethod
    def parse_into_locations(klass, filename):
        locationList = []
        with open(filename) as data:
            csvReader = csv.reader(data, delimiter=",")
            csvReader.__next__() #skipping over row of headers
            for row in csvReader:
                args = ()
                if len(row) < 8:
                    args = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                else:
                    args = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                locationList.append(Location(*args))
  
        return locationList

