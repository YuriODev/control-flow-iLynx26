import unittest
import subprocess
import os

class TestCoordinateQuarterDetermination(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "example_16.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_quarter_i(self):
        output = self.run_exercise("1\n1\n")
        self.assertIn("I", output)

    def test_quarter_ii(self):
        output = self.run_exercise("-1\n1\n")
        self.assertIn("II", output)

    def test_quarter_iv(self):
        output = self.run_exercise("1\n-1\n")
        self.assertIn("IV", output)

if __name__ == '__main__':
    unittest.main()
