import unittest
import subprocess
import os

class TestNextDayDateValidation(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "example_21.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_end_of_month(self):
        output = self.run_exercise("30\n4\n2020\n")
        self.assertIn("01.05.2020", output)

    def test_end_of_february_leap_year(self):
        output = self.run_exercise("28\n2\n2020\n")
        self.assertIn("29.02.2020", output)

    def test_end_of_year(self):
        output = self.run_exercise("31\n12\n2020\n")
        self.assertIn("01.01.2021", output)

if __name__ == '__main__':
    unittest.main()
