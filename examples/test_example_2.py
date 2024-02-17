import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_2.py")  # Adjust "exercise_1.py" accordingly


class TestExample2(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_win(self):
        output = self.run_exercise("3\n")
        self.assertIn("win", output)

    def test_draw(self):
        output = self.run_exercise("1\n")
        self.assertIn("draw", output)

    def test_lose(self):
        output = self.run_exercise("0\n")
        self.assertIn("lose", output)



if __name__ == '__main__':
    unittest.main()
