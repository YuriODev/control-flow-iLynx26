import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_3.py")  # Adjust "exercise_1.py" accordingly


class TestExample3(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_positive_number(self):
        output = self.run_exercise("10\n")
        self.assertIn("It is a positive number", output)

    def test_negative_number(self):
        output = self.run_exercise("-1\n")
        self.assertIn("It is a negative number", output)

    def test_zero(self):
        output = self.run_exercise("0\n")
        self.assertIn("It is Zero", output)


if __name__ == '__main__':
    unittest.main()
