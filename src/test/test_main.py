import unittest
from unittest.mock import patch

import io
import contextlib
import os

class TestMain(unittest.TestCase):

    @patch('optimizer.main.prompt', return_value={'filepath': 'filename'})
    @patch('optimizer.generate_document.generate_doc')
    @patch('optimizer.route_creator.RouteCreator')
    def test_cli_tool_takes_in_system_arg(self, mockRouteCreator, mockDoc, prompt):
        from optimizer.main import main
        from optimizer.route_creator import RouteCreator
        print(RouteCreator == mockRouteCreator)
        main()
        mockRouteCreator.assert_called_with('filename')
    
    @patch('optimizer.main.prompt', return_value={'filepath': 'filename'})
    @patch('optimizer.generate_document.generate_doc')
    @patch('optimizer.route_creator.RouteCreator')
    def test_cli_tool_returns_correct_path(self, mockRouteCreator, mockDoc, prompt):
        from optimizer.main import main
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                main()
                s = buf.getvalue()
                self.assertIn('Your itinerary can be found at: {}'.format(os.getcwd()),s)

