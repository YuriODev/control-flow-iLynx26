import unittest
import subprocess
import os


class TestExercise16(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_16.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_start_of_month_transition(self):
        """Test start-of-month transition."""
        output = self.run_exercise("1\n2\n2020\n")
        self.assertIn("31.01.2020", output)

    def test_leap_year_feb_start(self):
        """Test February start in a leap year."""
        output = self.run_exercise("1\n3\n2020\n")
        self.assertIn("29.02.2020", output)

    def test_start_of_year_transition(self):
        """Test start-of-year transition."""
        output = self.run_exercise("1\n1\n2021\n")
        self.assertIn("31.12.2020", output)


if __name__ == '__main__':
    unittest.main()
