import unittest
import subprocess
import os


class TestExercise2(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_2.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_infant(self):
        """Person is an infant."""
        output = self.run_exercise("1\n")
        self.assertIn("You are an infant.", output)

    def test_child(self):
        """Person is a child."""
        output = self.run_exercise("5\n")
        self.assertIn("You are a child.", output)

    def test_teenager(self):
        """Person is a teenager."""
        output = self.run_exercise("15\n")
        self.assertIn("You are a teenager.", output)

    def test_adult(self):
        """Person is an adult."""
        output = self.run_exercise("25\n")
        self.assertIn("You are an adult.", output)


if __name__ == '__main__':
    unittest.main()
