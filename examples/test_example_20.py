import unittest
import subprocess
import os

class TestIdenticalDigitsCounting(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "example_20.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_three_identical_digits(self):
        output = self.run_exercise("777\n")
        self.assertIn("3", output)

    def test_two_identical_digits(self):
        output = self.run_exercise("727\n")
        self.assertIn("2", output)

    def test_no_identical_digits(self):
        output = self.run_exercise("123\n")
        self.assertIn("0", output)

if __name__ == '__main__':
    unittest.main()
