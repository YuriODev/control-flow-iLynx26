import unittest
import subprocess
import os


class TestExercise1(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_1.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_older_alex(self):
        """Alex is older than Tatyana."""
        output = self.run_exercise("30\n25\n")
        self.assertIn("Alex is the eldest.", output)

    def test_older_tatyana(self):
        """Tatyana is older than Alex."""
        output = self.run_exercise("22\n30\n")
        self.assertIn("Tatyana is the eldest.", output)

    def test_same_age(self):
        """Alex and Tatyana are of the same age."""
        output = self.run_exercise("25\n25\n")
        self.assertIn("Alex and Tatyana are of the same age.", output)


if __name__ == '__main__':
    unittest.main()
