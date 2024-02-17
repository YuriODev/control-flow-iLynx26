import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_10.py")  # Adjust "example_10.py" accordingly

class TestDaysInAMonth(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_january(self):
        output = self.run_exercise("January\n")
        self.assertIn("January has 31 days in it.", output)

    def test_february(self):
        output = self.run_exercise("February\n")
        self.assertIn("February has 28 or 29 days in it.", output)

    def test_march(self):
        output = self.run_exercise("March\n")
        self.assertIn("March has 31 days in it.", output)

    def test_april(self):
        output = self.run_exercise("April\n")
        self.assertIn("April has 30 days in it.", output)

    def test_may(self):
        output = self.run_exercise("May\n")
        self.assertIn("May has 31 days in it.", output)

    def test_june(self):
        output = self.run_exercise("June\n")
        self.assertIn("June has 30 days in it.", output)

    def test_july(self):
        output = self.run_exercise("July\n")
        self.assertIn("July has 31 days in it.", output)

    def test_august(self):
        output = self.run_exercise("August\n")
        self.assertIn("August has 31 days in it.", output)

    def test_september(self):
        output = self.run_exercise("September\n")
        self.assertIn("September has 30 days in it.", output)

    def test_october(self):
        output = self.run_exercise("October\n")
        self.assertIn("October has 31 days in it.", output)

    def test_november(self):
        output = self.run_exercise("November\n")
        self.assertIn("November has 30 days in it.", output)

    def test_december(self):
        output = self.run_exercise("December\n")
        self.assertIn("December has 31 days in it.", output)

    def test_invalid_month(self):
        output = self.run_exercise("InvalidMonth\n")
        self.assertIn("Invalid month name", output)


if __name__ == '__main__':
    unittest.main()
