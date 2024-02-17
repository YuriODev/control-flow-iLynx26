import unittest
import subprocess
import os


class TestExercise13(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_13.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_all_digits_different(self):
        """All digits in the number are different."""
        output = self.run_exercise("1234\n")
        self.assertIn("True", output)

    def test_some_digits_same(self):
        """Some digits in the number are the same."""
        output = self.run_exercise("1123\n")
        self.assertIn("False", output)

    def test_all_digits_same(self):
        """All digits in the number are the same."""
        output = self.run_exercise("1111\n")
        self.assertIn("False", output)


if __name__ == '__main__':
    unittest.main()
