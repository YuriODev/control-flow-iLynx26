import unittest
import subprocess
import os


class TestExercise11(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_11.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_leap_year(self):
        """Year is a leap year."""
        output = self.run_exercise("2020\n")
        self.assertIn("Leap year.", output)

    def test_leap_year_2(self):
        """Year is a leap year."""
        output = self.run_exercise("2000\n")
        self.assertIn("Leap year.", output)

    def test_leap_year_3(self):
        """Year is a leap year."""
        output = self.run_exercise("2016\n")
        self.assertIn("Leap year.", output)

    def test_not_leap_year(self):
        """Year is not a leap year."""
        output = self.run_exercise("2019\n")
        self.assertIn("Ordinary year.", output)




if __name__ == '__main__':
    unittest.main()
