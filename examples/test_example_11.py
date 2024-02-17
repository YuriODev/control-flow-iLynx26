import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_11.py")  # Adjust "example_10.py" accordingly


class TestTaxCalculation(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_no_tax(self):
        output = self.run_exercise("1000\n10000\n20000\n500\n")
        self.assertIn("The tax calculated from the amount is 0.00", output)

    def test_low_tax(self):
        output = self.run_exercise("1000\n10000\n20000\n10000\n")
        self.assertIn("The tax calculated from the amount is 1000.00", output)

    def test_medium_tax(self):
        output = self.run_exercise("1000\n10000\n20000\n15000\n")
        self.assertIn("The tax calculated from the amount is 3750.00", output)

    def test_high_tax(self):
        output = self.run_exercise("1000\n10000\n20000\n25000\n")
        self.assertIn("The tax calculated from the amount is 12500.00", output)


if __name__ == '__main__':
    unittest.main()
