import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_13.py")  # Adjust "example_10.py" accordingly


class TestTwoDigitNumber(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_number_less_than_10(self):
        output = self.run_exercise("5\n")
        self.assertIn("0", output)

    def test_number_greater_than_99(self):
        output = self.run_exercise("123\n")
        self.assertIn("0", output)

    def test_first_digit_greater_than_second_digit(self):
        output = self.run_exercise("54\n")
        self.assertIn("1", output)

    def test_second_digit_greater_than_first_digit(self):
        output = self.run_exercise("23\n")
        self.assertIn("2", output)

    def test_digits_are_equal(self):
        output = self.run_exercise("77\n")
        self.assertIn("=", output)


if __name__ == '__main__':
    unittest.main()
