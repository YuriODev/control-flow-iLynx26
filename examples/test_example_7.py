import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_7.py")  # Adjust "exercise_1.py" accordingly


class TestMagicDate(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_magic_date(self):
        output = self.run_exercise("2\n10\n20\n")
        self.assertIn("The date is magic!", output)

    def test_not_magic_date(self):
        output = self.run_exercise("3\n11\n21\n")
        self.assertIn("The date is not magic.", output)


if __name__ == '__main__':
    unittest.main()
