import unittest
import subprocess
import os


class TestExercise8(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_8.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_digit_in_number(self):
        """Digit is in the number."""
        output = self.run_exercise("123\n2\n")
        self.assertIn("True", output)

    def test_digit_not_in_number(self):
        """Digit is not in the number."""
        output = self.run_exercise("456\n2\n")
        self.assertIn("False", output)

    def test_digit_in_number_2(self):
        """Digit is in the number."""
        output = self.run_exercise("123\n3\n")
        self.assertIn("True", output)


if __name__ == '__main__':
    unittest.main()