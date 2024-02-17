import unittest
import subprocess
import os


class TestExercise10(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_10.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_right_angled_triangle(self):
        """Triangle is right-angled."""
        output = self.run_exercise("0\n0\n0\n2\n4\n0\n")
        self.assertIn("Yes", output)

    def test_not_right_angled_triangle(self):
        """Triangle is not right-angled."""
        output = self.run_exercise("0\n0\n0\n0\n0\n0\n")
        self.assertIn("No", output)


if __name__ == '__main__':
    unittest.main()
