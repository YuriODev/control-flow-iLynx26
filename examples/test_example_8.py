import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_8.py")  # Adjust "exercise_1.py" accordingly


class TestRomanNumeralConversion(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)
    
    def test_roman_one(self):
        output = self.run_exercise("1\n")
        self.assertIn("I", output)

    def test_roman_two(self):
        output = self.run_exercise("2\n")
        self.assertIn("II", output)
    
    def test_roman_three(self):
        output = self.run_exercise("3\n")
        self.assertIn("III", output)

    def test_roman_four(self):
        output = self.run_exercise("4\n")
        self.assertIn("IV", output)
    
    def test_roman_five(self):
        output = self.run_exercise("5\n")
        self.assertIn("V", output)

    def test_roman_six(self):
        output = self.run_exercise("6\n")
        self.assertIn("VI", output)

    def test_roman_seven(self):
        output = self.run_exercise("7\n")
        self.assertIn("VII", output)

    def test_roman_eight(self):
        output = self.run_exercise("8\n")
        self.assertIn("VIII", output)

    def test_roman_nine(self):
        output = self.run_exercise("9\n")
        self.assertIn("IX", output)

    def test_roman_ten(self):
        output = self.run_exercise("10\n")
        self.assertIn("X", output)


if __name__ == '__main__':
    unittest.main()
