import unittest
import subprocess
import os

class TestChessboardCellColorMatching(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "example_18.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_same_color_yes(self):
        output = self.run_exercise("1\n1\n2\n2\n")
        self.assertIn("Yes", output)

    def test_different_color_no(self):
        output = self.run_exercise("1\n1\n2\n3\n")
        self.assertIn("No", output)

    def test_same_color_edge_case(self):
        output = self.run_exercise("8\n8\n1\n1\n")
        self.assertIn("Yes", output)

if __name__ == '__main__':
    unittest.main()
