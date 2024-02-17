import unittest
import subprocess
import os


class TestExercise14(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_14.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_palindrome_number_true(self):
        """Number is a palindrome."""
        output = self.run_exercise("1221\n")
        self.assertIn("True", output)

    def test_palindrome_number_false(self):
        """Number is not a palindrome."""
        output = self.run_exercise("1234\n")
        self.assertIn("False", output)

    def test_palindrome_number_2(self):
        """Number is a palindrome."""
        output = self.run_exercise("1331\n")
        self.assertIn("True", output)


if __name__ == '__main__':
    unittest.main()
