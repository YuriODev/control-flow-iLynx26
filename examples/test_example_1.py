import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_1.py")  # Adjust "exercise_1.py" accordingly


class TestExample1(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_cold_temperature(self):
        output = self.run_exercise("-5\n")
        self.assertIn("A cold, isn't it?", output)

    def test_cool_temperature(self):
        output = self.run_exercise("5\n")
        self.assertIn("Cool.", output)

    def test_nice_weather(self):
        output = self.run_exercise("15\n")
        self.assertIn("Nice weather we're having.", output)


if __name__ == '__main__':
    unittest.main()
