import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_9.py")  # Adjust "exercise_1.py" accordingly


class TestSoftwarePackageDiscount(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)
    
    def test_no_discount(self):
        output = self.run_exercise("3\n")
        self.assertIn("£8100.00", output)

    def test_discount_ten_percent(self):
        output = self.run_exercise("15\n")
        self.assertIn("£36450.00", output)

    def test_discount_twenty_percent(self):
        output = self.run_exercise("30\n")
        self.assertIn("£64800.00", output)

    def test_discount_thirty_percent(self):
        output = self.run_exercise("75\n")
        self.assertIn("£141750.00", output)

    def test_discount_forty_percent(self):
        output = self.run_exercise("150\n")
        self.assertIn("£243000.00", output)


if __name__ == '__main__':
    unittest.main()
