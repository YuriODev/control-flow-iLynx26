import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_12.py")  # Adjust "example_10.py" accordingly


class TestEndingWithFive(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_ends_with_5(self):
        output = self.run_exercise("12345\n")
        self.assertIn("True", output)

    def test_not_ends_with_5(self):
        output = self.run_exercise("12346\n")
        self.assertIn("False", output)

    def test_not_ends_with_5_v2(self):
        output = self.run_exercise("12340\n")
        self.assertIn("False", output)


if __name__ == '__main__':
    unittest.main()
