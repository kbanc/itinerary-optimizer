import unittest
from unittest.mock import mock_open, patch, MagicMock

import csv
import os 
import datetime

from optimizer.route_creator import RouteCreator
from optimizer.generate_document import generate_doc

class TestRouteCreator(unittest.TestCase):

    def setUp(self):
        self.create_file()
    
    def tearDown(self):
        self.delete_csv_file()
        self.delete_word_doc()
    
    def test_doc_created_with_correct_name(self):
        r = RouteCreator('locations.csv')
        print(r)
        docName = generate_doc(r)
        self.assertEqual(docName, 'Move_itinerary_{}.docx'.format(datetime.datetime.now().date()))

    def create_file(self):
        with open('locations.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['street','city','country','postalcode','mandatory','role','routeRestriction','nearestIntersection'])
            filewriter.writerow(['10 Kings College Rd', 'Toronto', 'Canada', 'M5S3G8', 'TRUE', 'volunteer', 'end'])
            filewriter.writerow(['431 College St', 'Toronto', 'Canada', 'M5T1T1', 'TRUE', 'car', 'start'])

    def delete_csv_file(self):
        os.remove('locations.csv')

    def delete_word_doc(self):
        filename = 'Move_itinerary_{}.docx'.format(datetime.datetime.now().date())
        if os.path.isfile(filename):
            os.remove(filename)

    