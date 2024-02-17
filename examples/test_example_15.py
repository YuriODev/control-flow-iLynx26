import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_15.py")  # Adjust "example_10.py" accordingly


class TestCircleBelonging(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_point_inside_circle(self):
        output = self.run_exercise("1\n1\n2\n")  # Assuming radius is 2
        self.assertIn("belongs", output)

    def test_point_outside_circle(self):
        output = self.run_exercise("3\n3\n2\n")
        self.assertIn("outside", output)

    
if __name__ == '__main__':
    unittest.main()
