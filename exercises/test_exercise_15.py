import unittest
import subprocess
import os


class TestExercise15(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_15.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_end_of_month_transition(self):
        """Test end-of-month transition."""
        output = self.run_exercise("31\n1\n2020\n")
        self.assertIn("1.2.2020", output)

    def test_leap_year_feb_end(self):
        """Test February end in a leap year."""
        output = self.run_exercise("29\n2\n2020\n")
        self.assertIn("1.3.2020", output)

    def test_end_of_year_transition(self):
        """Test end-of-year transition."""
        output = self.run_exercise("31\n12\n2020\n")
        self.assertIn("1.1.2021", output)


if __name__ == '__main__':
    unittest.main()
