import unittest
from unittest.mock import patch

import io
import contextlib
import os

from optimizer.main import main

@patch('optimizer.main.prompt', return_value={'filepath': 'filename'})
@patch('optimizer.main.generate_doc')
@patch('optimizer.main.RouteCreator')
class TestMain(unittest.TestCase):

    def test_cli_tool_takes_in_system_arg(self, mockRouteCreator, mockDoc, prompt):
        main()
        mockRouteCreator.assert_called_with('filename')

    def test_cli_tool_returns_correct_path(self, mockRouteCreator, mockDoc, prompt):
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                main()
                s = buf.getvalue()
                self.assertIn('Your itinerary can be found at: {}'.format(os.getcwd()),s)
                