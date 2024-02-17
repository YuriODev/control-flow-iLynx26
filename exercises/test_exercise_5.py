import unittest
import subprocess
import os


class TestExercise5(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_5.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_no_roots(self):
        """Equation with no roots."""
        output = self.run_exercise("1\n2\n3\n")
        self.assertIn("No roots", output)

    def test_one_root(self):
        """Equation with one root."""
        output = self.run_exercise("1\n-2\n1\n")
        self.assertTrue("1.0" in output or "-1.0" in output)

    def test_two_roots(self):
        """Equation with two distinct roots."""
        output = self.run_exercise("1\n-3\n2\n")
        self.assertIn("and", output)


if __name__ == '__main__':
    unittest.main()
