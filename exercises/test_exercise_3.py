import unittest
import subprocess
import os


class TestExercise3(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_3.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_green(self):
        """Number 0 is green."""
        output = self.run_exercise("0\n")
        self.assertIn("Green", output)

    def test_black(self):
        """Number 24 is black."""
        output = self.run_exercise("24\n")
        self.assertIn("Black", output)

    def test_red(self):
        """Number 23 is red."""
        output = self.run_exercise("23\n")
        self.assertIn("Red", output)

    def test_bet_not_play(self):
        """Number 37 will not play."""
        output = self.run_exercise("37\n")
        self.assertIn("The bet will not play!", output)


if __name__ == '__main__':
    unittest.main()
