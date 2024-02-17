import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_5.py")  # Adjust "exercise_1.py" accordingly


class TestDayOfWeek(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_grade_a(self):
        output = self.run_exercise("95\n")
        self.assertIn("Your grade is A.", output)

    def test_grade_c(self):
        output = self.run_exercise("74\n")
        self.assertIn("Your grade is C.", output)

    def test_grade_d(self):
        output = self.run_exercise("60\n")
        self.assertIn("Your grade is D.", output)



if __name__ == '__main__':
    unittest.main()
