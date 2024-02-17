import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_14.py")  # Adjust "example_10.py" accordingly


class TestOvertimePay(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_without_overtime(self):
        output = self.run_exercise("40\n25\n")
        self.assertIn("1000.0", output)

    def test_with_overtime(self):
        output = self.run_exercise("50\n40\n")
        self.assertIn("2200.0", output)

    
if __name__ == '__main__':
    unittest.main()
