import unittest
import subprocess
import os


class TestExercise12(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_12.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_replace_even_digits(self):
        """Even digits are replaced by '*'."""
        output = self.run_exercise("2468\n")
        self.assertIn("****", output)

    def test_no_even_digits(self):
        """No even digits to replace."""
        output = self.run_exercise("1357\n")
        self.assertIn("1357", output)

    

if __name__ == '__main__':
    unittest.main()
