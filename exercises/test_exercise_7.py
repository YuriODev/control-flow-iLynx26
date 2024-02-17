import unittest
import subprocess
import os


class TestExercise7(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_7.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_addition(self):
        """Test addition operation."""
        output = self.run_exercise("5\n3\n+\n")
        self.assertIn("8.0", output)

    def test_division_by_zero(self):
        """Test division by zero."""
        output = self.run_exercise("5\n0\n/\n")
        self.assertIn("Division by 0!", output)

    def test_multiplication(self):
        """Test multiplication operation."""
        output = self.run_exercise("5\n3\n*\n")
        self.assertIn("15.0", output)

    def test_subtraction(self):
        """Test subtraction operation."""
        output = self.run_exercise("5\n3\n-\n")
        self.assertIn("2.0", output)


if __name__ == '__main__':
    unittest.main()