import unittest
import subprocess
import os


class TestExercise4(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_4.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_initial_level(self):
        """Grade 1 is initial level."""
        output = self.run_exercise("1\n")
        self.assertIn("initial level", output)

    def test_average_level(self):
        """Grade 5 is average level."""
        output = self.run_exercise("5\n")
        self.assertIn("average level", output)

    def test_sufficient_level(self):
        """Grade 8 is sufficient level."""
        output = self.run_exercise("8\n")
        self.assertIn("sufficient level", output)

    def test_high_level(self):
        """Grade 11 is high level."""
        output = self.run_exercise("11\n")
        self.assertIn("high level", output)

    def test_level_absent(self):
        """Grade 13 is level absent."""
        output = self.run_exercise("13\n")
        self.assertIn("level is absent", output)


if __name__ == '__main__':
    unittest.main()
