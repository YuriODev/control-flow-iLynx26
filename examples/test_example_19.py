import unittest
import subprocess
import os

class TestTriangleTypeDetermination(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "example_19.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_rectangular(self):
        output = self.run_exercise("3\n4\n5\n")
        self.assertIn("rectangular", output)

    def test_acute(self):
        output = self.run_exercise("3\n3\n4\n")
        self.assertIn("acute", output)

    def test_obtuse(self):
        output = self.run_exercise("3\n4\n6\n")
        self.assertIn("obtuse", output)

if __name__ == '__main__':
    unittest.main()
