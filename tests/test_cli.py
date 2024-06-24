import unittest
from click.testing import CliRunner
import json

from app import create_app  # Make sure to import your Flask app setup

class TestCli(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.app = create_app()  # You need to create an app context for the CLI

    def test_show_cv_info(self):
        """Test the 'cv-info' command to ensure it includes personal information."""
        with self.app.app_context():
            result = self.runner.invoke(self.app.cli, ['cv-info'])

            self.assertEqual(list(json.loads(result.output).keys()), ['personal', 'experience', 'education'])
            self.assertEqual(result.exit_code, 0)
