import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_6.py")  # Adjust "exercise_1.py" accordingly


class TestDayOfWeek(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_friday(self):
        output = self.run_exercise("5\n")
        self.assertIn("Friday", output)

    def test_tuesday(self):
        output = self.run_exercise("2\n")
        self.assertIn("Tuesday", output)

    def test_sunday(self):
        output = self.run_exercise("7\n")
        self.assertIn("Sunday", output)


if __name__ == '__main__':
    unittest.main()
