import unittest
import subprocess
import os


class TestExercise9(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_9.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_sum_greater(self):
        """Sum of the first and last digits is greater than the second."""
        output = self.run_exercise("123\n")
        self.assertIn(">", output)

    def test_sum_lesser(self):
        """Sum of the first and last digits is less than the second."""
        output = self.run_exercise("251\n")
        self.assertIn("<", output)

    def test_sum_equal(self):
        """Sum of the first and last digits is equal to the second."""
        output = self.run_exercise("143\n")
        self.assertIn("=", output)


if __name__ == '__main__':
    unittest.main()
